#!/usr/bin/env python3
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from leads import LEADS, PROTECTED, NICHE, OVERRIDES
from core import theme_for, esc
from render_a import (
  render_hvac_v1, render_hvac_v2, render_hvac_v3,
  render_dental_v1, render_dental_v2, render_dental_v3,
  render_auto_v1, render_auto_v2, render_auto_v3,
)
from render_b import (
  render_vet_v1, render_vet_v2, render_vet_v3,
  render_legal_v1, render_legal_v2, render_legal_v3,
  render_spa_v1, render_spa_v2, render_spa_v3,
  render_plumbing_v1, render_plumbing_v2, render_plumbing_v3,
)

ROOT = Path("/workspace/wensite-previews")
PREVIEWS = ROOT / "previews"
assert (ROOT / "shared/preview-chrome.js").exists()
assert (ROOT / "shared/preview-chrome.css").exists()

RENDERERS = {
  "hvac": {1: render_hvac_v1, 2: render_hvac_v2, 3: render_hvac_v3},
  "dental": {1: render_dental_v1, 2: render_dental_v2, 3: render_dental_v3},
  "auto": {1: render_auto_v1, 2: render_auto_v2, 3: render_auto_v3},
  "vet": {1: render_vet_v1, 2: render_vet_v2, 3: render_vet_v3},
  "legal": {1: render_legal_v1, 2: render_legal_v2, 3: render_legal_v3},
  "spa": {1: render_spa_v1, 2: render_spa_v2, 3: render_spa_v3},
  "plumbing": {1: render_plumbing_v1, 2: render_plumbing_v2, 3: render_plumbing_v3},
}
VARIANT_META = {
  1: {"label": "Signature", "note": "Primary niche-forward mobile rebuild"},
  2: {"label": "Alternate", "note": "Second layout within same niche system"},
  3: {"label": "Editorial", "note": "Third composition for A/B feel"},
}

def main():
    chrome_css = (ROOT/"shared/preview-chrome.css").read_bytes()
    chrome_js = (ROOT/"shared/preview-chrome.js").read_bytes()

    # Snapshot protected file counts
    protected_before = {s: sum(1 for _ in (PREVIEWS/s).rglob('*') if _.is_file()) if (PREVIEWS/s).exists() else 0 for s in PROTECTED}

    manifest = {
        "project": "Wensite",
        "batch": "pilot-10-global",
        "generated": "2026-09-11",
        "revision": "sanity-check-fix-1",
        "base_url": "https://micwong3.github.io/wensite-previews/",
        "offer": {"activate": "$99/mo via shared chrome only", "countdown_hours": "48-72 localStorage"},
        "shared_chrome": {
            "css": "shared/preview-chrome.css",
            "js": "shared/preview-chrome.js",
            "reused_existing": True,
            "activate_path": "chrome-only",
        },
        "sanity_fixes": [
            "Distinct fonts + layouts per niche (spa/hvac/dental/legal/auto/plumbing/vet)",
            "Vertical-specific H2 copy (no shared template H2)",
            "Unique SVG/wordmarks (no letter-square)",
            "Single Activate via shared chrome; removed in-page Activate + sticky Activate",
        ],
        "protected_slugs_untouched": sorted(PROTECTED),
        "leads": [],
        "scrape_failures": [],
        "review_samples": [
            "previews/blooming-moon-spa/v1/index.html",
            "previews/bacharach-law/v1/index.html",
            "previews/build-pro-mechanical/v1/index.html",
        ],
    }

    for lead in LEADS:
        assert lead["slug"] not in PROTECTED
        lead_dir = PREVIEWS / lead["slug"]
        lead_dir.mkdir(parents=True, exist_ok=True)
        variants = []
        for v in (1,2,3):
            html = RENDERERS[lead["cat"]][v](lead)
            assert "Services built for mobile calls" not in html
            assert 'id="activate"' not in html
            assert "sticky-cta" not in html
            assert "Activate this site" not in html
            assert "letter-mark" not in html
            # no generic single-letter square mark class from old builder
            vdir = lead_dir / f"v{v}"
            vdir.mkdir(parents=True, exist_ok=True)
            (vdir/"index.html").write_text(html, encoding="utf-8")
            rel = f"previews/{lead['slug']}/v{v}/index.html"
            variants.append({"id": f"v{v}", "label": VARIANT_META[v]["label"], "note": VARIANT_META[v]["note"],
                             "path": rel, "url": f"https://micwong3.github.io/wensite-previews/{rel}"})
        entry = {
            "slug": lead["slug"], "name": lead["name"], "market": lead["market"], "cat": lead["cat"],
            "phone": lead["phone"], "website": lead["website"], "address": lead["address"],
            "scrape_ok": lead["scrape_ok"], "niche_fonts": theme_for(lead)["fonts_href"], "variants": variants,
        }
        if not lead["scrape_ok"]:
            entry["scrape_note"] = lead.get("scrape_note")
            manifest["scrape_failures"].append({"slug": lead["slug"], "website": lead["website"], "note": lead.get("scrape_note")})
        manifest["leads"].append(entry)
        print(f"OK {lead['slug']} ({lead['cat']}): v1-v3")

    # Ensure chrome untouched
    assert (ROOT/"shared/preview-chrome.css").read_bytes() == chrome_css
    assert (ROOT/"shared/preview-chrome.js").read_bytes() == chrome_js

    protected_after = {s: sum(1 for _ in (PREVIEWS/s).rglob('*') if _.is_file()) if (PREVIEWS/s).exists() else 0 for s in PROTECTED}
    assert protected_before == protected_after, (protected_before, protected_after)
    print("Protected slugs untouched:", protected_after)

    (ROOT/"MANIFEST-global.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    cards = []
    for e in manifest["leads"]:
        links = " · ".join(f'<a href="{esc(v["path"])}">{esc(v["id"].upper())}</a>' for v in e["variants"])
        flag = "" if e["scrape_ok"] else ' <span style="color:#a35b00;font-size:12px">scrape partial</span>'
        cards.append(f'<article style="background:#fff;border:1px solid #ddd;border-radius:14px;padding:14px;margin:10px 0"><h2 style="margin:0 0 6px;font-size:1.05rem">{esc(e["name"])}{flag}</h2><p style="margin:0 0 8px;color:#666;font-size:14px">{esc(e["market"])} · {esc(e["cat"])} · {esc(e["phone"])}</p><p style="margin:0">{links}</p></article>')
    (ROOT/"index-global.html").write_text(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Wensite — GLOBAL pilot 10</title></head>
<body style="font-family:system-ui;background:#f7f4ef;margin:0">
<main style="width:min(880px,calc(100% - 32px));margin:28px auto">
<h1>GLOBAL pilot — niche-distinct previews</h1>
<p>Activate = shared chrome only · 48–72h countdown · $99/mo</p>
{''.join(cards)}
<p><a href="MANIFEST-global.json">MANIFEST-global.json</a></p>
<p>Review samples: <a href="previews/blooming-moon-spa/v1/">spa v1</a> ·
<a href="previews/bacharach-law/v1/">legal v1</a> ·
<a href="previews/build-pro-mechanical/v1/">hvac v1</a></p>
</main></body></html>""", encoding="utf-8")

    # Convenience review copies with fixed relative chrome paths
    review = ROOT/"review-samples"
    review.mkdir(exist_ok=True)
    for slug in ["blooming-moon-spa","bacharach-law","build-pro-mechanical"]:
        html = (PREVIEWS/slug/"v1"/"index.html").read_text(encoding="utf-8")
        fixed = html.replace('href="../../../shared/', 'href="../shared/').replace('src="../../../shared/', 'src="../shared/')
        (review/f"{slug}-v1.html").write_text(fixed, encoding="utf-8")
        print("REVIEW", review/f"{slug}-v1.html")

    # Do not create/overwrite index.html if Flatiron owns it — only append marker if exists
    index_path = ROOT/"index.html"
    if index_path.exists():
        existing = index_path.read_text(encoding="utf-8")
        marker = "<!-- GLOBAL-PILOT-10 -->"
        if marker not in existing:
            block = f"""\n{marker}\n<section id=\"global-pilot-10\" style=\"width:min(880px,calc(100% - 32px));margin:24px auto\"><h2>GLOBAL pilot 10</h2><p><a href=\"index-global.html\">Open GLOBAL gallery</a> · <a href=\"MANIFEST-global.json\">MANIFEST-global.json</a></p></section>\n<!-- /GLOBAL-PILOT-10 -->\n"""
            if "</body>" in existing:
                existing = existing.replace("</body>", block+"\n</body>")
            else:
                existing += block
            index_path.write_text(existing, encoding="utf-8")
            print("Appended GLOBAL section to index.html")
    else:
        print("No root index.html — left index-global.html only")

    print("DONE leads", len(manifest["leads"]), "failures", len(manifest["scrape_failures"]))

if __name__ == "__main__":
    main()
