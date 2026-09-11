from core import esc, shell_open, shell_close, footer, services_cards, proofs_html
from marks import mark_svg

def render_vet_v1(lead):
    css=""".niche-vet .hero{background:var(--card);border-radius:28px;padding:24px 20px;margin:10px 0 18px;border:1px solid var(--line);box-shadow:var(--shadow);position:relative;overflow:hidden}
.niche-vet .hero::after{content:"";position:absolute;right:-20px;top:-20px;width:140px;height:140px;background:radial-gradient(circle,color-mix(in srgb,var(--accent2) 45%,transparent),transparent 70%)}
.niche-vet .mark{width:58px;height:58px}"""
    return shell_open(lead,1,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <header class="hero">{mark_svg(lead)}<p class="eyebrow">Independent Melbourne vet</p>
    <h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></header>
  <section class="block"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_vet_v2(lead):
    css=""".niche-vet.v2 .hours-card{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 18px}
.niche-vet.v2 .hours-card div{background:var(--accent);color:#fff;border-radius:18px;padding:16px}
.niche-vet.v2 .hours-card div:nth-child(2){background:var(--accent2);color:#1e3329}
.niche-vet.v2 .hours-card b{display:block;font-size:1.3rem;font-family:var(--display)}"""
    return shell_open(lead,2,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['name'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">Book</a></div>
  {mark_svg(lead)}<h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
  <div class="hours-card"><div><span style="opacity:.85;font-size:12px">Weekdays</span><b>8am–7pm</b></div>
    <div><span style="font-size:12px">Saturday</span><b>9–11am</b></div></div>
  <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a>
  <section class="block" style="margin-top:22px"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_vet_v3(lead):
    css=""".niche-vet.v3 .team{background:#1e3329;color:#f3f7f4;border-radius:24px;padding:22px;margin:14px 0}
.niche-vet.v3 .team p{color:rgba(243,247,244,.78)}.niche-vet.v3 .team .eyebrow{color:var(--accent2)}.niche-vet.v3 .mark{color:var(--accent2)}"""
    return shell_open(lead,3,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <div class="team">{mark_svg(lead)}
    <p class="eyebrow">Dr Trevor Cannell & Dr Sharon Rowland</p>
    <h1 style="color:#fff">{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" style="background:var(--accent2);color:#1e3329" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></div>
  <section class="block"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_legal_v1(lead):
    css=""".niche-legal .mast{border-bottom:2px solid var(--ink);padding:18px 0 20px;margin-bottom:18px}
.niche-legal .mast h1{font-weight:600;max-width:18ch}.niche-legal .svc h3{font-family:var(--display);font-weight:600}"""
    return shell_open(lead,1,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <header class="mast">{mark_svg(lead)}
    <p class="eyebrow">{esc(lead['market'])}</p><h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></header>
  <section class="block"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_legal_v2(lead):
    css=""".niche-legal.v2 .ruled{background:var(--ink);color:#f4f1ea;border-radius:4px;padding:24px 20px;margin:12px 0 18px}
.niche-legal.v2 .ruled p{color:rgba(244,241,234,.75)}.niche-legal.v2 .ruled .eyebrow{color:var(--accent2)}.niche-legal.v2 .ruled h1{color:#fff}
.niche-legal.v2 .btn-primary{background:var(--accent2);color:#1a1a1a}.niche-legal.v2 .mark{color:var(--accent2)}"""
    return shell_open(lead,2,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['name'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">Call</a></div>
  <header class="ruled">{mark_svg(lead)}<p class="eyebrow">{esc(lead['market'])}</p>
    <h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></header>
  <section class="block"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_legal_v3(lead):
    css=""".niche-legal.v3 .quote{font-family:var(--display);font-size:1.55rem;color:var(--ink);line-height:1.25;border-left:3px solid var(--accent2);padding-left:14px;margin:12px 0 18px}"""
    return shell_open(lead,3,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <p class="quote">{esc(lead['tagline'])}</p><p>{esc(lead['blurb'])}</p>
  <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a>
  <section class="block" style="margin-top:24px"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_spa_v1(lead):
    css=""".niche-spa .bloom{background:linear-gradient(165deg,#fffafb 0%,#f3e6ee 100%);border-radius:32px;padding:28px 20px;margin:12px 0 18px;border:1px solid rgba(107,69,112,.12)}
.niche-spa h1{font-weight:500;font-size:clamp(2.1rem,7.5vw,2.9rem)}.niche-spa .mark{width:64px;height:64px}.niche-spa .svc{border-radius:22px;background:#fffafb}"""
    return shell_open(lead,1,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <header class="bloom">{mark_svg(lead)}<p class="eyebrow">{esc(lead['market'])}</p>
    <h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></header>
  <section class="block"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_spa_v2(lead):
    css=""".niche-spa.v2 .rituals .svc{border-radius:0;box-shadow:none;background:transparent;border-left:0;border-right:0;border-color:rgba(107,69,112,.15);padding:18px 4px}
.niche-spa.v2 .moon-banner{text-align:center;padding:30px 16px;border-radius:999px 999px 28px 28px;background:#2a2030;color:#f7f0f4;margin:10px 0 18px}
.niche-spa.v2 .moon-banner p{color:rgba(247,240,244,.75)}.niche-spa.v2 .moon-banner .mark{margin:0 auto 12px;color:var(--accent2)}
.niche-spa.v2 .btn-primary{background:var(--accent2);color:#2a2030}"""
    return shell_open(lead,2,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['name'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">Book</a></div>
  <header class="moon-banner">{mark_svg(lead)}
    <h1 style="color:#fff;font-weight:500">{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></header>
  <section class="block"><h2>{esc(lead['h2_services'])}</h2><div class="rituals svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_spa_v3(lead):
    css=""".niche-spa.v3 .chip-row{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}
.niche-spa.v3 .chip{padding:8px 12px;border-radius:999px;background:#fff;border:1px solid var(--line);font-size:12px;font-weight:600}
.niche-spa.v3 .loc{background:color-mix(in srgb,var(--accent2) 25%,#fff);border-radius:20px;padding:16px;margin-bottom:16px}"""
    chips="".join(f'<span class="chip">{esc(p)}</span>' for p in lead["proofs"])
    return shell_open(lead,3,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  {mark_svg(lead)}<h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
  <div class="chip-row">{chips}</div>
  <div class="loc"><strong style="color:var(--ink)">{esc(lead['address'])}</strong>
    <p style="margin:.35em 0 0">{esc(lead.get('hours',''))}</p></div>
  <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a>
  <section class="block"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_plumbing_v1(lead):
    css=""".niche-plumbing .banner{background:var(--accent);color:#fff;border-radius:8px;padding:22px 18px;margin:12px 0}
.niche-plumbing .banner h1{color:#fff;text-transform:uppercase;letter-spacing:.02em}
.niche-plumbing .banner p{color:rgba(255,255,255,.85)}.niche-plumbing .banner .eyebrow{color:var(--accent2)}
.niche-plumbing .mark{color:var(--accent2)}.niche-plumbing .btn-primary{background:var(--accent2);color:#0d2137}
.niche-plumbing .svc h3{font-family:var(--display);text-transform:uppercase;letter-spacing:.03em;font-size:1.2rem}"""
    return shell_open(lead,1,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name" style="font-family:var(--display);font-size:18px;letter-spacing:.04em">KUHN PLUMBING</div>
    <a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <header class="banner">{mark_svg(lead)}<p class="eyebrow">Chicago · Since 1908</p>
    <h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></header>
  <section class="block"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_plumbing_v2(lead):
    css=""".niche-plumbing.v2 .alert{display:flex;align-items:center;justify-content:space-between;gap:10px;background:#fff3cd;border:2px solid var(--accent2);border-radius:12px;padding:14px 16px;margin:12px 0;font-weight:700}
.niche-plumbing.v2 .grid-tight .svc{border-radius:10px;border-top:4px solid var(--accent)}"""
    return shell_open(lead,2,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">Kuhn Plumbing</div><a class="call" href="tel:{esc(lead['phone_tel'])}">Emergency line</a></div>
  <div class="alert"><span>Emergency plumbing available</span><span style="color:var(--accent)">{esc(lead['phone'])}</span></div>
  <h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
  <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a>
  <section class="block grid-tight" style="margin-top:20px"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_plumbing_v3(lead):
    css=""".niche-plumbing.v3 .year{font-family:var(--display);font-size:clamp(3rem,14vw,5rem);color:var(--accent);line-height:.9;margin:8px 0 6px}
.niche-plumbing.v3 .svc{display:grid;grid-template-columns:auto 1fr;gap:12px;align-items:start}
.niche-plumbing.v3 .ico{width:28px;height:28px;background:var(--accent);border-radius:6px}"""
    svcs="".join(f'<article class="svc"><div class="ico"></div><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></article>' for t,d in lead["services"])
    return shell_open(lead,3,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">Kuhn Plumbing</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <div class="year">1908</div><h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
  <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a>
  <section class="block" style="margin-top:22px"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{svcs}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()
