#!/usr/bin/env python3
"""Idempotent performance pass for stamped previews (Home/Services/Contact).

What it does to every HTML page inside a stamped preview folder
(a top-level folder whose index.html uses shared/preview-chrome.css):
  * Google Fonts: every css2 URL referenced (via <link> or @import inside the local CSS)
    is self-hosted under shared/fonts/*.woff2 with font-display:swap, same families,
    weights, styles and unicode-range subsets as Google serves (cyrillic/greek/vietnamese
    subsets dropped only if no page uses those characters). Preconnects to Google removed.
  * Local stylesheets (preview-chrome.css, stamp/shell.css, brand.css, ...) are inlined
    into ONE <style> block at the position of the first stylesheet link, in the same order,
    so there are zero render-blocking CSS requests. Source CSS files stay the source of truth.
  * Home hero <img> (assets/photos/*-hero.*): fetchpriority="high", real width/height,
    srcset with the 800w mobile variant (<name>-800.jpg, made by _ops/perf_heroes.mjs) when present,
    and a matching <link rel="preload" as="image" imagesrcset=...> in <head>.
  * Preview chrome bar (Private preview / countdown / Activate) is pre-rendered as the first child of
    <body> (markup mirrors shared/preview-chrome.js, which now reuses it) so it paints with the first
    frame instead of being injected at the end of the page and shoving the hero down (layout shift).
    If you change the bar markup/copy in preview-chrome.js, change CHROME_TPL here too and re-run.
Everything generated lives between <!-- ws-perf:start ... --> and <!-- ws-perf:end -->;
the start marker records the original stylesheet hrefs, so re-running rebuilds the block
from current sources (run again after editing shared/stamp/shell.css or a brand.css).

Usage: python3 _ops/perf_inline.py [--check]
"""
import os, re, sys, json, hashlib, urllib.request, urllib.parse, struct

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(ROOT, 'shared', 'fonts')
CACHE = os.path.join(FONT_DIR, 'google-css-cache.json')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'
DROP_SUBSETS = {'cyrillic', 'cyrillic-ext', 'greek', 'greek-ext', 'vietnamese'}
START_RE = re.compile(r'<!-- ws-perf:start (.*?) -->.*?<!-- ws-perf:end -->\n?', re.S)

def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = r.read()
    return d if binary else d.decode('utf-8')

_cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}

def google_css(url):
    url = url.replace('&amp;', '&')
    if url not in _cache:
        _cache[url] = fetch(url)
        os.makedirs(FONT_DIR, exist_ok=True)
        json.dump(_cache, open(CACHE, 'w'), indent=1, sort_keys=True)
    return _cache[url]

def parse_faces(css):
    """-> list of (subset, face_css_body_dict_text, gstatic_url)"""
    out = []
    for m in re.finditer(r'/\*\s*([\w-]+)\s*\*/\s*@font-face\s*\{(.*?)\}', css, re.S):
        subset, body = m.group(1), m.group(2)
        u = re.search(r'url\((https://fonts\.gstatic\.com/[^)]+)\)', body).group(1)
        out.append((subset, body, u))
    return out

def local_font(gurl, family):
    fam = re.sub(r'[^a-z0-9]+', '-', family.lower()).strip('-')
    name = f"{fam}-{hashlib.sha1(gurl.encode()).hexdigest()[:10]}.woff2"
    path = os.path.join(FONT_DIR, name)
    if not os.path.exists(path):
        open(path, 'wb').write(fetch(gurl, binary=True))
    return '/shared/fonts/' + name

def unicode_ranges(body):
    m = re.search(r'unicode-range:\s*([^;]+);', body)
    rs = []
    if not m: return rs
    for part in m.group(1).split(','):
        part = part.strip().upper().replace('U+', '')
        if '-' in part:
            a, b = part.split('-'); rs.append((int(a, 16), int(b, 16)))
        elif '?' in part:
            rs.append((int(part.replace('?', '0'), 16), int(part.replace('?', 'F'), 16)))
        else:
            rs.append((int(part, 16), int(part, 16)))
    return rs

USED_CHARS = set()

def font_faces_css(gurls):
    blocks, seen = [], set()
    for gu in gurls:
        for subset, body, u in parse_faces(google_css(gu)):
            if subset in DROP_SUBSETS:
                rs = unicode_ranges(body)
                if not any(a <= c <= b for c in USED_CHARS for a, b in rs):
                    continue
            fam = re.search(r"font-family:\s*'([^']+)'", body).group(1)
            body2 = body.replace(u, local_font(u, fam))
            if 'font-display' not in body2:
                body2 += 'font-display: swap;'
            key = re.sub(r'\s+', '', body2)
            if key in seen: continue
            seen.add(key)
            blocks.append('@font-face{' + re.sub(r'\s*\n\s*', '', body2).strip() + '}')
    return ''.join(blocks)

IMPORT_RE = re.compile(r'@import\s+url\(\s*["\']?(https://fonts\.googleapis\.com/[^"\')]+)["\']?\s*\)\s*;?')

def minify(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};,>])\s*', r'\1', css)
    css = re.sub(r';}', '}', css)
    return css.strip()

def jpeg_png_size(path):
    with open(path, 'rb') as f:
        d = f.read()
    if d[:8] == b'\x89PNG\r\n\x1a\n':
        return struct.unpack('>II', d[16:24])
    i = 2
    while i < len(d):
        if d[i] != 0xFF: i += 1; continue
        mk = d[i + 1]
        if mk in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            h, w = struct.unpack('>HH', d[i + 5:i + 9]); return w, h
        seg = struct.unpack('>H', d[i + 2:i + 4])[0]; i += 2 + seg
    return None

CHROME_RE = re.compile(r'<!-- ws-perf:chrome start -->.*?<!-- ws-perf:chrome end -->\n?', re.S)
CHROME_TPL = ('<!-- ws-perf:chrome start -->\n'
  '<div class="ws-chrome" role="banner" data-ws-prerendered><div class="ws-chrome-inner"><div class="ws-chrome-copyblock">'
  '<div class="ws-chrome-top"><span class="ws-badge">Private preview</span><span class="ws-timer" data-ws-timer aria-live="polite">\u2014</span></div>'
  '<p class="ws-copy">A private rebuild for <strong>{name}</strong>. Not a live site \u2014 claim it before this preview expires.</p></div>'
  '<a class="ws-activate" data-ws-activate href="{href}">Activate this site \u2014 $99/mo</a></div></div>\n'
  '<!-- ws-perf:chrome end -->\n')

def add_chrome(html):
    html = CHROME_RE.sub('', html)
    m = re.search(r'<body\b[^>]*>', html)
    if not m or 'shared/preview-chrome.js' not in html or 'data-ws-track-only' in html:
        return html
    tag = m.group(0)
    name = attr(tag, 'data-preview-name') or 'this business'
    name = name.replace('<', '&lt;')
    slug = attr(tag, 'data-preview-slug') or 'preview'
    href = attr(tag, 'data-activate-href')
    if not href:
        root = attr(tag, 'data-ws-root')
        href = (re.sub(r'/?$', '/', root) if root else '../../../') + 'activate.html?biz=' + urllib.parse.quote(slug, safe='')
    new_tag = tag
    cls = attr(tag, 'class')
    if cls is None:
        new_tag = tag[:-1] + ' class="ws-has-chrome">'
    elif 'ws-has-chrome' not in cls.split():
        new_tag = re.sub(r'\bclass="([^"]*)"', lambda k: f'class="{k.group(1)} ws-has-chrome"', tag, count=1)
    return html[:m.start()] + new_tag + '\n' + CHROME_TPL.format(name=name, href=href) + html[m.end():].lstrip('\n')

LINK_RE = re.compile(r'[ \t]*<link\b[^>]*>\n?', re.I)

def attr(tag, name):
    m = re.search(r'\b' + name + r'\s*=\s*"([^"]*)"', tag, re.I)
    return m.group(1) if m else None

def process(page):
    html = open(page, encoding='utf-8').read()
    orig = html
    pdir = os.path.dirname(page)
    m = START_RE.search(html)
    if m:
        hrefs = json.loads(m.group(1))['links']
        insert_at = m.start()
        html = html[:m.start()] + html[m.end():]
    else:
        head_end = html.lower().index('</head>')
        hrefs, first = [], None
        new, pos = [], 0
        for lm in LINK_RE.finditer(html[:head_end]):
            tag = lm.group(0); rel = (attr(tag, 'rel') or '').lower(); href = attr(tag, 'href') or ''
            drop = False
            if rel == 'stylesheet' and (href.startswith('https://fonts.googleapis.com/') or not re.match(r'^[a-z]+:|^//', href)):
                hrefs.append(href); drop = True
            elif rel == 'preconnect' and ('fonts.googleapis.com' in href or 'fonts.gstatic.com' in href):
                drop = True
            elif rel == 'preload' and attr(tag, 'as') == 'image' and 'assets/photos/' in href:
                drop = True
            if drop:
                if first is None: first = lm.start()
                new.append(html[pos:lm.start()]); pos = lm.end()
        if not hrefs:
            return False
        new.append(html[pos:]); html = ''.join(new)
        insert_at = first
    # build CSS
    gurls, parts = [], []
    for h in hrefs:
        if h.startswith('https://fonts.googleapis.com/'):
            gurls.append(h.replace('&amp;', '&')); continue
        src = os.path.normpath(os.path.join(pdir, h))
        css = open(src, encoding='utf-8').read()
        for im in IMPORT_RE.finditer(css): gurls.append(im.group(1))
        parts.append(minify(IMPORT_RE.sub('', css)))
    faces = font_faces_css(list(dict.fromkeys(gurls)))
    # hero image
    preload = ''
    def fix_img(im):
        nonlocal preload
        tag = im.group(0); src = attr(tag, 'src')
        path = os.path.normpath(os.path.join(pdir, src))
        wh = jpeg_png_size(path) if os.path.exists(path) else None
        t = tag
        if wh:
            for n, v in (('width', wh[0]), ('height', wh[1])):
                t = re.sub(r'\b' + n + r'="\d+"', f'{n}="{v}"', t) if re.search(r'\b' + n + r'="', t) else t.replace('<img', f'<img {n}="{v}"', 1)
        if 'fetchpriority=' not in t:
            t = t[:-1].rstrip('/').rstrip() + ' fetchpriority="high">'
        small = re.sub(r'\.jpe?g$', '-800.jpg', src)
        spath = os.path.normpath(os.path.join(pdir, small))
        if small != src and os.path.exists(spath) and wh:
            srcset = f'{small} 800w, {src} {wh[0]}w'
            sizes = '(min-width: 960px) 48vw, 100vw'
            t = re.sub(r'\s(srcset|sizes)="[^"]*"', '', t)
            t = t.replace(f'src="{src}"', f'src="{src}" srcset="{srcset}" sizes="{sizes}"', 1)
            preload = f'<link rel="preload" as="image" href="{src}" imagesrcset="{srcset}" imagesizes="{sizes}" fetchpriority="high">\n'
        else:
            preload = f'<link rel="preload" as="image" href="{src}" fetchpriority="high">\n'
        return t
    html = re.sub(r'<img\b[^>]*src="[^"]*assets/photos/[^"]*-hero\.[a-z]+"[^>]*>', fix_img, html, count=1)
    meta = json.dumps({'links': hrefs}, separators=(',', ':'))
    block = (f'<!-- ws-perf:start {meta} -->\n' + preload +
             '<style data-ws-perf>' + faces + ''.join(parts) + '</style>\n<!-- ws-perf:end -->\n')
    html = html[:insert_at] + block + html[insert_at:]
    html = add_chrome(html)
    if html != orig:
        open(page, 'w', encoding='utf-8').write(html)
        return True
    return False

def stamped_dirs():
    out = []
    for d in sorted(os.listdir(ROOT)):
        idx = os.path.join(ROOT, d, 'index.html')
        if d.startswith(('.', '_')) or d in ('previews', 'review-samples', 'reference', 'scrapes', 'screenshots', 'assets', 'shared'):
            continue
        if os.path.isfile(idx) and 'shared/preview-chrome.css' in open(idx, encoding='utf-8').read():
            out.append(d)
    return out

def main():
    dirs = stamped_dirs()
    pages = []
    for d in dirs:
        for r, _, fs in os.walk(os.path.join(ROOT, d)):
            pages += [os.path.join(r, f) for f in fs if f.endswith('.html')]
    for p in pages:
        txt = re.sub(r'<[^>]+>', ' ', open(p, encoding='utf-8').read())
        USED_CHARS.update(ord(c) for c in txt if ord(c) > 0x24F)
    changed = [p for p in sorted(pages) if process(p)]
    print(f'{len(dirs)} stamped folders, {len(pages)} pages, {len(changed)} changed')
    for p in changed: print('  ', os.path.relpath(p, ROOT))

if __name__ == '__main__':
    main()
