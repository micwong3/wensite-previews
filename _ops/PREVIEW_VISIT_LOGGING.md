# Preview visit / click logging

Every stamped preview loads `shared/preview-chrome.js`; its top block logs events.
`activate.html` loads the same file with `data-ws-track-only` (logging only, no chrome banner).

- **Sheet:** "Wensite Preview Visits" — https://docs.google.com/spreadsheets/d/1hj6xY9_dzfzZRC4LMsFp2IOVcxqsC4gczMd_hV2I5ro/edit
- **Sink:** Google Apps Script web app — source in `_ops/preview-visit-logger.gs`
- **Client switch:** `TRACK_ENDPOINT` (line ~7 of `shared/preview-chrome.js`). Empty string = logging off.

## Columns (one row per event)
| col | meaning |
|---|---|
| ts_et | client time, America/New_York, e.g. `2026-09-28T11:42:47-04:00` |
| preview_slug | `body[data-preview-slug]` (activate.html: `?biz=`) |
| event | `page_view` \| `cta_click` \| `activate_click` |
| page | `home` \| `services` \| `contact` \| `activate` \| `other` (from path) |
| path | `location.pathname` |
| referrer | `document.referrer` (≤300 chars) |
| ua | `navigator.userAgent` (≤180 chars) |
| src | `?s=` on landing (email1, sms1…), kept in sessionStorage per slug for the visit; `""` if none |
| is_test | `?test=1` (sticky in localStorage; `?test=0` clears) or localhost/127.0.0.1 |
| is_bot | UA matches crawler/link-preview regex or `navigator.webdriver` — still logged, just flagged |

## Fire rules
- `page_view` once per slug+path per tab session per 30 min (sessionStorage dedupe).
- `activate_click`: `.ws-activate`, `[data-ws-activate]`, `[data-ws-activate-link]`, `a[href*="activate.html"]`, `a[href="#activate"]`.
- `cta_click`: `.btn-primary`, `.nav-cta`, `.home-actions .btn-primary` (if not already an activate link).
- Transport: `navigator.sendBeacon` (text/plain) → fallback `fetch(no-cors, keepalive)`. Every step is try/catch — never breaks UX.

## Deploy the sink (one-time, ~2 min)
1. Open https://script.google.com → New project → name "Wensite Preview Visit Logger".
2. Replace `Code.gs` with `_ops/preview-visit-logger.gs`. Save.
3. Deploy → New deployment → gear → **Web app**. Execute as **Me**, Who has access **Anyone**. Deploy, authorize (Advanced → Go to project if warned).
4. Copy the `https://script.google.com/macros/s/…/exec` URL.
5. Put it in `TRACK_ENDPOINT` in `shared/preview-chrome.js`, commit, push. Pages rebuilds in ~1 min.

Code changes later: Deploy → Manage deployments → edit → Version "New version" (keeps the same /exec URL).

## Verify
- `curl -sL "$TRACK_ENDPOINT"` → `{"ok":true,"sink":"wensite-preview-visits",...}`
- Open `https://sitesremade.com/<slug>/?s=selftest&test=1` in your own browser → a `page_view` row with `is_test=TRUE` lands in the sheet within seconds.
- Filter real traffic in the sheet with `is_test = FALSE AND is_bot = FALSE`.
