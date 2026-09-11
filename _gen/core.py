from leads import NICHE, OVERRIDES
from marks import mark_svg

def esc(s):
    return (str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;"))

def theme_for(lead):
    t = dict(NICHE[lead["cat"]])
    t.update(OVERRIDES.get(lead["slug"], {}))
    return t

def services_cards(lead):
    return "".join(f'<article class="svc"><h3>{esc(t)}</h3><p>{esc(d)}</p></article>' for t,d in lead["services"])

def proofs_html(lead):
    return "".join(f'<div class="proof">{esc(p)}</div>' for p in lead["proofs"])

def footer(lead):
    bits = [f"<strong>{esc(lead['name'])}</strong>", f"<p>{esc(lead['address'])}</p>",
            f'<p><a href="tel:{esc(lead["phone_tel"])}">{esc(lead["phone"])}</a></p>']
    if lead.get("email"):
        bits.append(f'<p><a href="mailto:{esc(lead["email"])}">{esc(lead["email"])}</a></p>')
    if lead.get("hours"):
        bits.append(f"<p>{esc(lead['hours'])}</p>")
    bits.append(f'<p class="fine">Preview inspired by {esc(lead["website"])} · Not the live site</p>')
    return f'<footer class="site-footer"><div class="wrap">{"".join(bits)}</div></footer>'

def shell_open(lead, variant, extra_css):
    t = theme_for(lead)
    dark = lead["cat"] == "auto"
    title = f"{lead['short']} — mobile preview v{variant}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="robots" content="noindex,nofollow" />
<meta name="description" content="{esc(lead['tagline'])}" />
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?{t['fonts_href']}&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../../../shared/preview-chrome.css" />
<style>
:root {{
  --bg: {t['bg']}; --ink: {t['ink']}; --muted: {t['muted']};
  --card: {t['card']}; --accent: {t['accent']}; --accent2: {t['accent2']};
  --display: {t['font_display']}; --body: {t['font_body']};
  --line: {"rgba(255,255,255,.12)" if dark else "rgba(12,20,30,.08)"};
  --shadow: 0 12px 40px {"rgba(0,0,0,.45)" if dark else "rgba(20,30,40,.08)"};
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  margin: 0; font-family: var(--body); color: var(--ink); background: var(--bg);
  line-height: 1.55; -webkit-font-smoothing: antialiased;
}}
h1,h2,h3 {{ font-family: var(--display); line-height: 1.12; margin: 0 0 .45em; font-weight: 700; }}
h1 {{ font-size: clamp(2rem, 7.2vw, 2.75rem); letter-spacing: -0.02em; }}
h2 {{ font-size: clamp(1.35rem, 4.5vw, 1.7rem); }}
p {{ margin: 0 0 1em; color: var(--muted); }}
a {{ color: inherit; }}
.wrap {{ width: min(700px, calc(100% - 28px)); margin: 0 auto; }}
.mark {{ width: 52px; height: 52px; color: var(--accent); display: block; margin-bottom: 14px; }}
.mark-wide {{ width: min(180px, 70vw); height: auto; }}
.eyebrow {{ font-size: 11px; letter-spacing: .16em; text-transform: uppercase; font-weight: 700; color: var(--accent); margin: 0 0 10px; }}
.btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 8px; min-height: 50px; padding: 0 22px; border-radius: 999px; text-decoration: none; font-weight: 700; font-size: 15px; border: 0; }}
.btn-primary {{ background: var(--accent); color: #fff; }}
.btn-row {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 18px; }}
.topbar {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 16px 0 6px; }}
.topbar .brand-name {{ font-weight: 800; font-size: 14px; letter-spacing: .02em; }}
.topbar a.call {{ font-size: 13px; font-weight: 700; color: var(--accent); text-decoration: none; white-space: nowrap; }}
.svc-grid {{ display: grid; gap: 12px; }}
.svc {{ background: var(--card); border: 1px solid var(--line); border-radius: 18px; padding: 16px 16px 14px; box-shadow: var(--shadow); }}
.svc h3 {{ font-size: 1.05rem; margin-bottom: 6px; }}
.svc p {{ margin: 0; font-size: 14px; }}
.proofs {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 8px 0 28px; }}
.proof {{ background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 14px; font-size: 13px; font-weight: 700; }}
.site-footer {{ padding: 8px 0 48px; font-size: 14px; color: var(--muted); }}
.site-footer strong {{ display: block; color: var(--ink); margin-bottom: 6px; font-size: 15px; }}
.site-footer a {{ color: var(--accent); font-weight: 700; text-decoration: none; }}
.fine {{ font-size: 12px; opacity: .75; margin-top: 10px; }}
section.block {{ padding: 8px 0 22px; }}
{extra_css}
</style>
</head>
<body class="niche-{esc(lead['cat'])} v{variant}" data-preview-slug="{esc(lead['slug'])}" data-preview-name="{esc(lead['name'])}">
"""

def shell_close():
    # Chrome-only Activate — no in-page Activate, no sticky bar competing with chrome
    return '\n<script src="../../../shared/preview-chrome.js"></script>\n</body>\n</html>\n'
