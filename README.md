# Wensite previews

Private mobile rebuilds for SMB outreach. Static HTML/CSS/JS only.

## GitHub Pages + custom domain

1. Repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / folder: `/ (root)`
4. Custom domain: **sitesremade.com** (`CNAME` file at repo root)

After DNS verifies, pages are served from:

`https://sitesremade.com/`

Until DNS/TLS is live, GitHub still builds from `main /`. The old project-pages host (`https://micwong3.github.io/wensite-previews/…`) will **not** match clean root paths — that is expected.

### Example paths (weak-site 10, clean URLs)

- Gallery: https://sitesremade.com/index-weaksite.html
- LGSL Home: https://sitesremade.com/lgsl-mechanical/
- Activate: https://sitesremade.com/activate.html?biz=lgsl-mechanical

Older v1/v2/v3 batches stay under `/previews/<slug>/…` (e.g. Kenworthey letterhead).

`.nojekyll` is included.

## Shared chrome

Every preview loads `shared/preview-chrome.css` + `shared/preview-chrome.js`.

- Sticky **Private preview** bar
- Countdown **48–72 hours from first load**, `localStorage` key per slug
- Single **Activate this site — $99/mo** path (no second sticky call bar)

## Local review samples

Open these two first on a ~390px viewport:

1. `previews/kenworthey-law/v1/index.html`
2. `previews/heller-org/v1/index.html`

Weak-site gold stamp: `lgsl-mechanical/index.html`

## Manifest

See `MANIFEST.json` for the Flatiron/Irvine 8 and `MANIFEST-weaksite.json` for the pilot 10.

## Push

Parent agent pushes. Do not commit scrape dumps (`scrapes/` is gitignored).

## Multi-page stamp

See **TEMPLATES.md**. Reference lead: `lgsl-mechanical/` (Home · Services · Contact).
Activate ($99/mo) is injected by shared chrome on every page; countdown stays.

DNS records: `_ops/GODADDY_DNS_sitesremade.md`

## Performance pass (mobile LCP)

Stamped preview pages (Home/Services/Contact) get their CSS inlined and fonts self-hosted by
`python3 _ops/perf_inline.py` (idempotent; everything it writes sits between `<!-- ws-perf:start -->`
and `<!-- ws-perf:end -->`). **Re-run it after editing `shared/preview-chrome.css`,
`shared/stamp/shell.css` or any `brand.css`**, or after stamping a new preview, otherwise the page keeps
the old inlined copy. Hero photos: `_ops/perf_heroes.mjs` (max 1200px, <=90 KiB, plus a 800w variant for srcset).
Self-hosted Google Fonts (OFL) live in `shared/fonts/`.
