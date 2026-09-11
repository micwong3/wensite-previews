from core import esc, shell_open, shell_close, footer, services_cards, proofs_html, mark_svg
# mark_svg imported via core? Fix - import from marks
from marks import mark_svg

def render_hvac_v1(lead):
    css = """
.niche-hvac .hero { margin:10px 0 18px; border-radius:28px; overflow:hidden; background:linear-gradient(145deg,#0c1b2a 0%,var(--accent) 100%); color:#fff; padding:28px 22px 26px; box-shadow:var(--shadow); }
.niche-hvac .hero .mark { color:var(--accent2); width:56px; height:56px; }
.niche-hvac .hero h1, .niche-hvac .hero .eyebrow { color:#fff; }
.niche-hvac .hero p { color:rgba(255,255,255,.82); }
.niche-hvac .hero .btn-primary { background:var(--accent2); color:#111; }
.niche-hvac .meter { display:flex; gap:8px; margin-top:18px; flex-wrap:wrap; }
.niche-hvac .meter span { background:rgba(255,255,255,.12); border:1px solid rgba(255,255,255,.18); border-radius:999px; padding:7px 12px; font-size:12px; font-weight:700; }
"""
    return shell_open(lead,1,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div>
    <a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <header class="hero">{mark_svg(lead)}
    <p class="eyebrow">{esc(lead['market'])} · HVAC</p>
    <h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <div class="btn-row"><a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></div>
    <div class="meter">{''.join(f'<span>{esc(p)}</span>' for p in lead['proofs'][:3])}</div>
  </header>
  <section class="block"><p class="eyebrow">Services</p><h2>{esc(lead['h2_services'])}</h2>
    <div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><p class="eyebrow">Local proof</p><h2>{esc(lead['h2_proof'])}</h2>
    <div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_hvac_v2(lead):
    css = """
.niche-hvac.v2 .panel { background:var(--card); border-radius:22px; padding:22px 18px; border:1px solid var(--line); box-shadow:var(--shadow); margin-bottom:14px; }
.niche-hvac.v2 .temp { background:#0c1b2a; color:#fff; border-radius:22px; padding:20px; display:flex; align-items:center; justify-content:space-between; margin:12px 0; }
.niche-hvac.v2 .temp b { font-family:var(--display); font-size:2.4rem; color:var(--accent2); }
.niche-hvac.v2 .rail a { display:flex; justify-content:space-between; gap:12px; align-items:center; text-decoration:none; padding:16px 0; border-bottom:1px solid var(--line); }
.niche-hvac.v2 .rail a:last-child { border-bottom:0; }
.niche-hvac.v2 .rail strong { color:var(--ink); font-size:15px; }
.niche-hvac.v2 .rail span { color:var(--muted); font-size:13px; max-width:58%; text-align:right; }
"""
    rails="".join(f'<a href="tel:{esc(lead["phone_tel"])}"><strong>{esc(t)}</strong><span>{esc(d)}</span></a>' for t,d in lead["services"])
    return shell_open(lead,2,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['name'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">Call now</a></div>
  <div class="temp"><div><div class="eyebrow" style="color:var(--accent2)">Ready when you are</div><div style="font-weight:700">{esc(lead['market'])}</div></div><b>A/C</b></div>
  <div class="panel">{mark_svg(lead)}<h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></div>
  <section class="block panel"><p class="eyebrow">Tap to call</p><h2>{esc(lead['h2_services'])}</h2><div class="rail">{rails}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_hvac_v3(lead):
    css=""".niche-hvac.v3 .big{font-family:var(--display);font-size:clamp(2.2rem,8vw,3rem);letter-spacing:-.03em;margin:0 0 12px}
.niche-hvac.v3 .cols .svc{border-left:4px solid var(--accent);border-radius:12px}"""
    return shell_open(lead,3,css)+f"""
<div class="wrap" style="padding-top:18px">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  {mark_svg(lead)}<p class="eyebrow">{esc(lead['market'])}</p>
  <p class="big">{esc(lead['tagline'])}</p><p>{esc(lead['blurb'])}</p>
  <div class="btn-row"><a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></div>
  <section class="block" style="margin-top:26px"><h2>{esc(lead['h2_services'])}</h2><div class="cols svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_dental_v1(lead):
    css=""".niche-dental .hero-card{background:var(--card);border-radius:28px;padding:26px 20px;border:1px solid var(--line);box-shadow:var(--shadow);margin:10px 0 20px;background-image:radial-gradient(80% 60% at 100% 0%,color-mix(in srgb,var(--accent2) 18%,transparent),transparent 60%)}
.niche-dental .mark-wide{color:var(--accent);margin-bottom:18px;height:36px;width:auto;max-width:200px}
.niche-dental h1{font-weight:600}"""
    return shell_open(lead,1,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <header class="hero-card">{mark_svg(lead)}
    <p class="eyebrow">{esc(lead['market'])}</p><h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <div class="btn-row"><a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></div>
  </header>
  <section class="block"><p class="eyebrow">Care menu</p><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_dental_v2(lead):
    css=""".niche-dental.v2{background:#1c2b33;color:#f7f3ec}
.niche-dental.v2 p{color:rgba(247,243,236,.72)}
.niche-dental.v2 .topbar .brand-name,.niche-dental.v2 h1,.niche-dental.v2 h2,.niche-dental.v2 h3{color:#fff}
.niche-dental.v2 .clinic{border:1px solid rgba(255,255,255,.14);border-radius:24px;padding:22px;background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.02));margin:12px 0 18px}
.niche-dental.v2 .svc{background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.1)}
.niche-dental.v2 .proof{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.1);color:#fff}
.niche-dental.v2 .btn-primary{background:var(--accent2);color:#1c2b33}
.niche-dental.v2 .topbar a.call,.niche-dental.v2 .eyebrow,.niche-dental.v2 .mark,.niche-dental.v2 .mark-wide{color:var(--accent2)}
.niche-dental.v2 .site-footer,.niche-dental.v2 .site-footer strong{color:rgba(247,243,236,.8)}"""
    return shell_open(lead,2,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['short'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">Tap to call</a></div>
  <header class="clinic">{mark_svg(lead)}<h1>{esc(lead['name'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></header>
  <section class="block"><h2>{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_dental_v3(lead):
    css=""".niche-dental.v3 .timeline{border-left:2px solid color-mix(in srgb,var(--accent) 35%,transparent);margin:18px 0 24px;padding-left:18px}
.niche-dental.v3 .timeline .svc{box-shadow:none;margin-bottom:12px}
.niche-dental.v3 .addr{background:color-mix(in srgb,var(--accent) 8%,#fff);border-radius:20px;padding:18px;margin-bottom:18px}"""
    return shell_open(lead,3,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name">{esc(lead['name'])}</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <p class="eyebrow">{esc(lead['market'])}</p><h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
  <div class="addr"><strong style="color:var(--ink)">{esc(lead['address'])}</strong>
    <p style="margin:.4em 0 0">{esc(lead.get('hours') or 'Call for appointment times')}</p></div>
  <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a>
  <section class="block timeline"><h2>{esc(lead['h2_services'])}</h2>{services_cards(lead)}</section>
  <section class="block"><h2>{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_auto_v1(lead):
    css=""".niche-auto .stripe{background:var(--accent);color:#fff;padding:8px 0;font-weight:800;text-transform:uppercase;letter-spacing:.08em;font-size:12px;text-align:center;font-family:var(--display)}
.niche-auto .hero{padding:22px 0 10px}.niche-auto h1{text-transform:uppercase}
.niche-auto .svc{background:#1a1a1a;border-color:rgba(255,255,255,.1)}
.niche-auto .svc h3{color:#fff;font-family:var(--display);text-transform:uppercase;letter-spacing:.04em}
.niche-auto .proof{background:#1a1a1a;color:#fff;border-color:rgba(255,255,255,.1)}
.niche-auto .topbar .brand-name{color:#fff;font-family:var(--display);letter-spacing:.06em}
.niche-auto .topbar a.call{color:var(--accent2)}.niche-auto .site-footer strong{color:#fff}
.niche-auto .mark-wide{color:var(--accent2)}"""
    return shell_open(lead,1,css)+f"""
<div class="stripe">Insurance approved · Free estimates · 24/7 towing</div>
<div class="wrap">
  <div class="topbar"><div class="brand-name">OMEGA MP AUTOBODY</div><a class="call" href="tel:{esc(lead['phone_tel'])}">{esc(lead['phone'])}</a></div>
  <header class="hero">{mark_svg(lead)}<h1>{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></header>
  <section class="block"><h2 style="color:#fff">{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
  <section class="block"><h2 style="color:#fff">{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_auto_v2(lead):
    css=""".niche-auto.v2 .bento{display:grid;gap:10px;margin:14px 0 20px}
.niche-auto.v2 .bento .big{background:linear-gradient(135deg,var(--accent),#7a0000);border-radius:18px;padding:22px;color:#fff}
.niche-auto.v2 .tile{background:#1a1a1a;border-radius:16px;padding:16px;border:1px solid rgba(255,255,255,.1);color:#fff}
.niche-auto.v2 .tile b{display:block;font-family:var(--display);font-size:1.2rem;margin-bottom:4px}"""
    tiles="".join(f'<div class="tile"><b>{esc(p)}</b><span style="color:#aaa;font-size:13px">Toronto west end</span></div>' for p in lead["proofs"])
    return shell_open(lead,2,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name" style="color:#fff">OMEGA MP</div><a class="call" href="tel:{esc(lead['phone_tel'])}">416-769-5341</a></div>
  <div class="bento"><div class="big"><p class="eyebrow" style="color:var(--accent2)">{esc(lead['market'])}</p>
    <h1>{esc(lead['tagline'])}</h1><p style="color:rgba(255,255,255,.85)">{esc(lead['blurb'])}</p>
    <a class="btn btn-primary" style="background:#111;border:1px solid rgba(255,255,255,.25)" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a></div>{tiles}</div>
  <section class="block"><h2 style="color:#fff">{esc(lead['h2_services'])}</h2><div class="svc-grid">{services_cards(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()

def render_auto_v3(lead):
    css=""".niche-auto.v3 .stack a.row{display:grid;grid-template-columns:48px 1fr;gap:12px;align-items:start;text-decoration:none;padding:16px;margin-bottom:10px;border-radius:14px;background:#1a1a1a;border:1px solid rgba(255,255,255,.1);color:#fff}
.niche-auto.v3 .num{font-family:var(--display);font-size:1.4rem;color:var(--accent2)}"""
    rows="".join(f'<a class="row" href="tel:{esc(lead["phone_tel"])}"><span class="num">{i:02d}</span><span><strong style="display:block;font-family:var(--display);letter-spacing:.04em;text-transform:uppercase">{esc(t)}</strong><span style="color:#aaa;font-size:13px">{esc(d)}</span></span></a>' for i,(t,d) in enumerate(lead["services"],1))
    return shell_open(lead,3,css)+f"""
<div class="wrap">
  <div class="topbar"><div class="brand-name" style="color:#fff">OMEGA MP AUTOBODY</div><a class="call" href="tel:{esc(lead['phone_tel'])}">Call shop</a></div>
  <p class="eyebrow" style="color:var(--accent2)">The Junction · Toronto</p>
  <h1 style="color:#fff">{esc(lead['tagline'])}</h1><p>{esc(lead['blurb'])}</p>
  <a class="btn btn-primary" href="tel:{esc(lead['phone_tel'])}">{esc(lead['cta'])}</a>
  <section class="block stack" style="margin-top:22px"><h2 style="color:#fff">{esc(lead['h2_services'])}</h2>{rows}</section>
  <section class="block"><h2 style="color:#fff">{esc(lead['h2_proof'])}</h2><div class="proofs">{proofs_html(lead)}</div></section>
</div>{footer(lead)}"""+shell_close()
