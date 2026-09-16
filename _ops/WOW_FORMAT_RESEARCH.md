# What sells Wensite previews (vs Awwwards theater)

Date: 2026-09-16  
Audience: Michael + Project Wensite  
Question: Should we chase Three.js / Awwwards-style spectacle for SMB preview sells ($99/mo Activate)?

## TL;DR

**No — not as the default stamp.**  
Awwwards Site of the Day winners (Cartier, Into the Amazon, Inkwell) win on immersive WebGL storytelling for brands with huge creative budgets. Our buyer is a local owner deciding in **1–5 minutes** whether a rebuild looks more professional than their Weebly/Google Sites page. What sells Activate is **premium craft + conversion clarity**, not floating orbs.

**Recommended bar:** “Awwwards-adjacent” local professional sites (dental / law nominees) + hard conversion research — **GSAP/scroll polish, real photography, trust, sticky call CTA** — not WebGL demos.

---

## What Awwwards is rewarding (2024–2026)

Patterns from SOTD / case studies:

| Pattern | Examples | Stack vibe |
|--------|----------|------------|
| Immersive 3D worlds / alcoves | Cartier Watches & Wonders | Three.js, Blender, Lenis, GSAP |
| Scroll-as-film narrative | Inkwell, Into the Amazon | ScrollTrigger, no skip nav |
| Continuous homepage timeline | Working Stiff Films | **DOM + GSAP only** (no WebGL) |
| Gesture / discovery | Cartier | Hidden interactions |

Jury weights roughly: **Design 40% · Usability 30% · Creativity 20% · Content 10%**.

**Implication for us:** Creativity theater scores high on Awwwards; **usability + content** still matter, and Working Stiff explicitly chose **GSAP/DOM over WebGL** for control + performance. That’s the transferable lesson.

Local-service Awwwards *nominees* that match our ICP better:

- Dental: Harmony Dental, Brentwood Dentistry, Atelier Dental (trust, luxe, clean service showcase)
- Law: Shulman & Hill, Eskesen (advocacy, clarity, responsive)

These look “expensive” without requiring a 3D engine.

---

## What actually converts local SMB sites

Industry consensus (local service / contractor / dental / law):

1. **Phone in header + sticky mobile Call** — local searches end in calls; bury the number and you lose.
2. **Above-the-fold clarity** — what you do + who for + where, in ~1 viewport (matches Michael’s 1–5 min owner decision).
3. **Trust strip** — reviews, licensed/insured, years, real photos (not stock theater).
4. **Service pages / clear IA** — Home · Services · Contact beats infinite scroll for decision speed (already our stamp).
5. **Speed** — ~7% conversion hit per extra second; WebGL often fights this on mid phones.
6. **Short forms / one CTA** — Activate path should feel as obvious as Call Now.
7. **Benchmarks** — ~2–4% organic → contact is “good” for service sites; focused pages higher. Our KPI is **Activate**, so treat preview like a landing page: one story, one CTA.

Sources synthesized: local CRO guides (GrowWithBA, Social Element, ToTheMax, Hometown Digital, LOGOS benchmarks) — consistent on calls/trust/speed over spectacle.

---

## Buyer mismatch: Awwwards SOTD vs Sites Remade lead

| Dimension | Awwwards SOTD buyer | Our SMS/Email lead |
|-----------|---------------------|--------------------|
| Role | Brand / agency creative | Owner-operator |
| Session | Explore / delight | “Is this better than my site?” |
| Time | Minutes of scroll theater | 1–5 minutes |
| Device | Desktop showcase | Mixed; phone after SMS |
| Risk | Prestige project | “Will this get me jobs?” |
| Success metric | Jury score | Activate $99/mo |

Floating particles read as **agency demo**, not “my shop will look more legit.”

---

## What would sell the most (ranked)

### Tier A — Build this stamp (default for volume)

**“Premium local professional”** (Levine gold bar + dental/law nominee energy)

- Desktop-first, fast LCP, no WebGL required
- Large real hero photo (original site or niche)
- Distinct niche typography + color (not shared LGSL orange for everyone)
- Micro-motion: GSAP fade/slide on scroll, hover on cards — **3D depth via layout/shadow/parallax of photos**, not meshes
- Sticky Activate + Call
- Proof strip with **real** claims only
- Services as editorial cards, Contact with phone/email/map-area

**Why it sells:** Owner instantly sees “this looks like a real business website.” Matches conversion research. Stamps at 100/day.

### Tier B — Selective wow (1–2 niches, not all 25)

**Scroll-story Home** (Working Stiff pattern)

- One continuous Home narrative: Problem → Proof → Services teaser → Activate
- GSAP ScrollTrigger section pin / wipe between photo panels
- Still multi-page Services + Contact for decision speed

Use for **spa / dental / law** where aesthetics = purchase. Skip for emergency HVAC/plumbing (they want speed + phone).

### Tier C — Avoid as default

- Full Three.js particle/orb demos
- Autoplay heavy WebGL on mobile SMS landings
- Scroll-locked stories with no way to Call in 2 taps

Keep Three.js only if we ever sell **brand experience** to a different ICP.

---

## Serenity Three.js prototype — verdict

Current Serenity page: tasteful type + soft UI, but **orb/particle motion feels 2D/gimmicky** and doesn’t prove salon craft. Owner takeaway is unclear vs a strong photo grid + GSAP.

**Next experiment (recommended):** rebuild Serenity as Tier A/B — full-bleed nail/spa photography, scroll-triggered reveals, no WebGL — and A/B owner reaction vs LGSL stamp.

---

## Recommended product decision

1. **Park WebGL as default stamp.**
2. **Invest in “Premium Local” stamp v2:** typography systems per niche, photo-forward heroes, GSAP micro-interactions, sticky Activate.
3. **Optional Tier B scroll-story** for beauty/dental/law only.
4. Keep **Home / Services / Contact** IA (decision-fast).
5. Measure: time-to-Activate click, not Awwwards score.

---

## References (starting points)

- https://www.awwwards.com/sites/cartier-watches-wonders-2025
- https://www.awwwards.com/inkwell-a-scroll-driven-narrative-for-ais-most-stealth-player.html
- https://www.awwwards.com/working-stiff-films-case-study.html
- https://www.awwwards.com/sites/harmony-dental-west-covina
- https://www.awwwards.com/sites/atelier-dental
- Local CRO: growwithba.com/blog/local-business-website-design ; tothemaxmedia.com service-business guide
