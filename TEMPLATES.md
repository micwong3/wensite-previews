# Wensite stamp — multi-page template

This is the **Project Wensite** stamp for high-volume lead previews.
Gold stamp lead: **`lgsl-mechanical/`** (Home · Services · Contact).

Hosted at **`https://sitesremade.com/<slug>/`** (custom domain, site root). Activate stays at `/activate.html?biz=<slug>`.

## Goals

1. **Multi-page IA** — not a long-scroll one-pager. Thin secondary pages.
2. **Home sells in ~1 viewport** — hero photo + proof + one primary CTA above the fold.
3. **Activate ($99/mo)** one click from every page via shared chrome (countdown stays).
4. **Desktop-first**, reusable chrome/tokens — swap content, keep craft.
5. **Claim-light** — rewrite real offerings only; never invent prices/hours/licenses/team.

## Folder layout

```
<slug>/                     # repo root (clean URL /<slug>/)
  index.html              # Home
  services/index.html     # Services
  contact/index.html      # Contact
  site.json               # content + brand tokens (source of truth)
  brand.css               # CSS variables for this lead

shared/
  preview-chrome.css      # Private preview bar
  preview-chrome.js       # Countdown + Activate ($99/mo)
  stamp/shell.css         # Reusable site header/footer/cards/buttons
```

Relative paths must work on GitHub Pages at site root:

`https://sitesremade.com/<slug>/`

- Home (`<slug>/index.html`): `../shared/…`, `../assets/photos/<slug>-hero.jpg`
- Nested (`<slug>/services/` and `contact/`): `../../shared/…`

Do **not** nest new stamps under `previews/` (that prefix is only for older v1/v2/v3 batches).

## Stamp a new lead (checklist)

1. **Copy** `lgsl-mechanical/` → `<new-slug>/`
2. **Edit `site.json`**
   - `slug`, `name`, `phone`, `phoneTel`, `market`, `tagline`, `sourceUrl`
   - `services[]` from scrape only
   - `proof[]`, `about`, `tokens`
3. **Swap hero**
   - Place photo at `assets/photos/<slug>-hero.jpg`
   - Update `site.json` → `heroPhoto` (`../assets/photos/<slug>-hero.jpg`) and `<img src>` on Home
4. **Update `brand.css`**
   - Map `tokens` → `:root` CSS variables (ink, accent, fonts)
5. **Find/replace in the three HTML files**
   - Business name, phone, `tel:` links, market copy
   - `data-preview-slug`, `data-preview-name`, `data-activate-href`, `data-ws-root`
   - Nav + footer Activate links (`/<slug>/`, `/<slug>/services/`, `/<slug>/contact/`)
6. **Wire Activate**
   - Every page: `data-activate-href="/activate.html?biz=<slug>"` and `data-ws-root="/"`
   - Add slug → display name in `activate.html` `names` map (and `rootSlugs` so Back works)
7. **Verify**
   - Open Home, Services, Contact locally
   - Chrome Activate + countdown on every page
   - Relative CSS/JS/photo paths resolve at site root
   - No invented claims vs scrape

## Activate wiring

Shared chrome injects a sticky bar on every page that loads:

```html
<link rel="stylesheet" href="…/shared/preview-chrome.css">
<script src="…/shared/preview-chrome.js"></script>
```

Body attributes:

| Attribute | Purpose |
|-----------|---------|
| `data-preview-slug` | localStorage countdown key + Activate query |
| `data-preview-name` | Chrome copy |
| `data-activate-href` | Explicit path to `activate.html?biz=…` |
| `data-ws-root` | Fallback root if `data-activate-href` omitted |

Footer may also include `data-ws-activate-link` — JS rewrites href to the same Activate URL.

**Do not** add a second sticky call bar that competes with Activate. Primary business CTA is the phone button in the site header/hero.

## Content rules

- Scrape first. If Google Sites / Weebly is thin → **claim-light**.
- Polish = hierarchy, typography, clarity — not new services or fake reviews.
- Prefer “call or text to schedule” over invented hours.
- `site.json` is the checklist for the next stamp; HTML is the rendered preview.

## IA pattern

| Page | Job |
|------|-----|
| Home | Sell in one viewport: photo + proof + one CTA |
| Services | List real offerings only |
| Contact | Phone + market; thin |

## Quality bar

Desktop-first (~1180px). Aim for Levine-level craft with vertical-specific brand tokens.
