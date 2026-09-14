# GoDaddy DNS for sitesremade.com → GitHub Pages

Repo: `micwong3/wensite-previews`  
Pages: legacy, branch `main`, folder `/ (root)`  
CNAME file in repo: `sitesremade.com`

GitHub Pages will serve this repo at **site root** (not `/wensite-previews/`). Weak-site Homes are `https://sitesremade.com/<slug>/`.

## Records to set (DNS → Manage DNS)

Remove any existing A, AAAA, or CNAME on `@` (apex) and `www` that conflict (parking, forwarding, old host, “Parked”, etc.).

### Apex A (host `@`)

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | `@` | `185.199.108.153` | 600 or default |
| A | `@` | `185.199.109.153` | 600 or default |
| A | `@` | `185.199.110.153` | 600 or default |
| A | `@` | `185.199.111.153` | 600 or default |

All four are required (GitHub Pages).

### Apex AAAA (optional IPv6, host `@`)

| Type | Name | Value | TTL |
|------|------|-------|-----|
| AAAA | `@` | `2606:50c0:8000::153` | 600 or default |
| AAAA | `@` | `2606:50c0:8001::153` | 600 or default |
| AAAA | `@` | `2606:50c0:8002::153` | 600 or default |
| AAAA | `@` | `2606:50c0:8003::153` | 600 or default |

### www CNAME

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | `www` | `micwong3.github.io.` | 600 or default |

Trailing dot is fine if GoDaddy accepts it; otherwise `micwong3.github.io` (no `https://`).

`www` → `sitesremade.com` also works if you prefer an alias to apex, but GitHub’s documented www target is `micwong3.github.io`.

## After save

1. Wait for GitHub domain verification (Pages settings / API `protected_domain_state`). Can take minutes to a few hours.
2. TLS certificate is issued after the domain verifies. HTTPS enforce may fail until then — that is OK.
3. Test:
   - `https://sitesremade.com/lgsl-mechanical/`
   - `https://sitesremade.com/activate.html?biz=lgsl-mechanical`
   - `https://www.sitesremade.com/lgsl-mechanical/` (after www CNAME)
4. Until DNS is live, GitHub still builds the site; `https://micwong3.github.io/wensite-previews/lgsl-mechanical/` may 404 because this is a **project** Pages site and clean paths live at the custom-domain root. Expected.

## Do not

- Put `https://` in DNS values
- Leave an old A record for the GoDaddy parked IP alongside GitHub’s A records
- Rewrite SMS/email drafts until Sanity gets 200s on the new host
