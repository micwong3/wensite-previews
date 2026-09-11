# Wensite previews

Private mobile rebuilds for SMB outreach. Static HTML/CSS/JS only.

## GitHub Pages

1. Repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / folder: `/ (root)`
4. After the deploy, pages are served from:

`https://micwong3.github.io/wensite-previews/`

### Example paths

- Directory: https://micwong3.github.io/wensite-previews/
- Kenworthey v1: https://micwong3.github.io/wensite-previews/previews/kenworthey-law/v1/
- Heller v1: https://micwong3.github.io/wensite-previews/previews/heller-org/v1/
- Activate: https://micwong3.github.io/wensite-previews/activate.html?biz=kenworthey-law

Relative links are used throughout so the project site works under this base path. `.nojekyll` is included.

## Shared chrome

Every preview loads `shared/preview-chrome.css` + `shared/preview-chrome.js`.

- Sticky **Private preview** bar
- Countdown **48–72 hours from first load**, `localStorage` key per slug
- Single **Activate this site — $99/mo** path (no second sticky call bar)

## Local review samples

Open these two first on a ~390px viewport:

1. `previews/kenworthey-law/v1/index.html`
2. `previews/heller-org/v1/index.html`

## Manifest

See `MANIFEST.json` for slug, phone, source URL, variant paths, and scrape notes.

## Push

Parent agent pushes. Do not commit scrape dumps (`scrapes/` is gitignored).
