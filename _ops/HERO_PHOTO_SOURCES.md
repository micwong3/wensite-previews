# Hero photo sources

Rule: use the lead's own website photo when it has a decent one; otherwise a free-license niche stock photo (Unsplash or Pexels, commercial use, no attribution required) with **no business names, signs, logos, phone numbers or readable plates**. Never reuse one business's own photo for another lead.

Fixed 2026-09-28: 12 auto-body previews had been stamped with Harden Auto Body's storefront (sign: "HARDEN AUTO BODY, INC. (216) 382-3232") because `_gen/emailqueue25/stamp.py` used it as the only "auto" hero. Harden's own preview keeps its own photo.

Pipeline after replacing a hero: `SHARP_PATH=/workspace/perf-tools/node_modules/sharp node _ops/perf_heroes.mjs list.txt` (1200px ≤90 KiB + 800px ≤45 KiB), then `python3 _ops/perf_inline.py` (width/height, srcset, preload). Delete the old `*-hero-800.jpg` and any `/tmp/photos-orig-backup/<name>` copy first, or the 800px variant is rebuilt from the old photo.

## The 12 auto-body previews

| Preview | Type | Source | License | Notes |
|---|---|---|---|---|
| bloomington-collision | Stock | https://www.pexels.com/photo/a-person-buffing-a-car-5233261/; file https://images.pexels.com/photos/5233261/pexels-photo-5233261.jpeg | Pexels License (https://www.pexels.com/license/); photographer: (Pexels contributor) | Hands polishing a car hood with a buffer. Own site (bloomingtoncollision.weebly.com, 6 pages) has no usable photo: only an Angie's List badge and 250px thumbnails. Copy kept as `assets/photos/stock/auto-body-buff-pexels-5233261.jpg`. |
| chinoz-auto-body | Lead's own site | https://static.wixstatic.com/media/c6c9db_820d05f261324b148b38a00bcaafba95~mv2.jpg (found on https://chinozaragoza.wixsite.com/mysite) | Lead's own website asset, used only in their own preview | Storefront at 7135 Alabama Ave with their own sign; full frame. |
| hh-auto-collision | Lead's own site | https://handhautocollisionrepair.weebly.com/uploads/1/3/2/7/132787462/published/h-h-auto-collision-repair-building.jpg?1597376468 (found on https://handhautocollisionrepair.weebly.com/) | Lead's own website asset, used only in their own preview | Their own building with their own sign/phone; left 20% cropped (billboard). |
| impact-paint-body | Stock | https://unsplash.com/photos/un-hombre-encerando-un-coche-en-un-garaje-CsZjHjFN3N8 (id CsZjHjFN3N8); file https://images.unsplash.com/photo-1708805282706-f44730b7e527 | Unsplash License (https://unsplash.com/license); photographer: Zac Nielson | Detailer polishing a black car; cropped to 4:3 (top part). Own site (impactpaintandbody.weebly.com, 5 pages) has only 250px thumbnails and a 920x259 theme banner. Copy kept as `assets/photos/stock/auto-body-detail-unsplash-CsZjHjFN3N8.jpg`. |
| jj-auto-body-pinellas | Lead's own site | https://static.wixstatic.com/media/61dc04_2c93712679ac4370adefd2d72629318d~mv2_d_2592_1936_s_2.jpg (found on https://jjbodyworks.wixsite.com/jjautobody) | Lead's own website asset, used only in their own preview | White/blue Cobra (#93) in their shop; full frame. |
| jjs-auto-body-paint | Lead's own site | https://static.wixstatic.com/media/917da6_3da884c9e10d4a62be83a6410dc1f149~mv2_d_4032_3024_s_4_2.jpg (found on https://jjsautobodyusa.wixsite.com/home) | Lead's own website asset, used only in their own preview | Restored 1962 Cadillac on their lot; left 6% cropped; front plate blurred. Encoded at 1000px wide (1200px could not reach 90 KiB). |
| lowe-autobody | Lead's own site | https://static.wixstatic.com/media/06634c_4e200db5e5a440c78d0851220ab718e3~mv2_d_1440_1213_s_2.jpg (found on https://tstults2912.wixsite.com/loweautobody) | Lead's own website asset, used only in their own preview | Custom-finished Jeep (their uploaded work photo; no plate visible); full frame. |
| nievas-body-shop | Lead's own site | https://static.wixstatic.com/media/4ca4c7_659d43e3130144afb83211773459af7c~mv2.jpg (found on https://nievasbodyshop.wixsite.com/my-site-1) | Lead's own website asset, used only in their own preview | Teal Impala inside their shop; full frame (source is 960px wide). |
| ricks-paint-body | Stock | https://www.pexels.com/photo/close-up-of-man-painting-car-details-14615263/; file https://images.pexels.com/photos/14615263/pexels-photo-14615263.jpeg | Pexels License (https://www.pexels.com/license/); photographer: Dextar Studio | Spray gun painting car panels in a booth. Own site: the only own photo is a 628x487 team shot (too small for the hero); every other image is stock/blog art (one is another shop's "subaru-collision-center" image). Copy kept as `assets/photos/stock/auto-body-spray-pexels-14615263.jpg`. |
| sa-usa-auto-repair | Lead's own site | https://static.wixstatic.com/media/6d5e33_56be8f12fa284252996889ad92f389a1~mv2.jpeg (found on https://sausaautorepair.wixsite.com/my-site) | Lead's own website asset, used only in their own preview | BMW M4 in front of their own "USA AUTO REPAIR PAINT & BODY" storefront; no front plate; full frame. |
| williams-collision-repair | Lead's own site | https://static.wixstatic.com/media/ae8d44_8b79f64224071fba24ca37687d2a4b67.jpg (found on https://williamscollision.wixsite.com/repair) | Lead's own website asset, used only in their own preview | Cobra body in their paint booth; cropped top 4% / bottom 14.5% to remove the camera date stamp. |
| wjj-auto-collision | Lead's own site | https://static.wixstatic.com/media/83360f_3cf31b0ac103424b8af7027985d01420~mv2.jpg (found on https://wjjautocollision.wixsite.com/website) | Lead's own website asset, used only in their own preview | "After" half of their before/after collage (repaired RAV4, plate already blacked out); cropped to exclude a neighbouring building sign. Encoded at 1000px wide. |

## Stock pool for future auto-body stamps (`assets/photos/stock/`)

`_gen/emailqueue25/stamp.py` HERO_BY_CAT["auto"] now rotates these 4 (no names/signs/logos/phones/plates):

| File | Source | License |
|---|---|---|
| auto-body-spray-pexels-14615263.jpg | https://www.pexels.com/photo/close-up-of-man-painting-car-details-14615263/ | Pexels License |
| auto-body-buff-pexels-5233261.jpg | https://www.pexels.com/photo/a-person-buffing-a-car-5233261/ | Pexels License |
| auto-body-detail-unsplash-CsZjHjFN3N8.jpg | https://unsplash.com/photos/CsZjHjFN3N8 (Zac Nielson) | Unsplash License |
| auto-body-panel-unsplash-G6sI_6B_FFY.jpg | https://unsplash.com/photos/a-person-wearing-gloves-and-gloves-is-painting-a-blue-car-G6sI_6B_FFY | Unsplash License |

The "spa" pool was emptied (it pointed at Happy Feet Relaxing's banner, which has the name printed on it); stamp.py now refuses to stamp a spa lead until a clean spa photo is added.

## Audit of every preview hero (perceptual-hash duplicate scan of assets/photos, then visual check)

- **Harden storefront (name + phone) on 12 other shops**: fixed above.
- **serenity-nail-salon-spa-hero.jpg** was a copy of Happy Feet Relaxing's banner (text "Happy Feet Relaxing"). No Serenity page shows it (the home is the Three.js hero); only `serenity-nail-salon-spa/site.json` referenced it. Replaced with Serenity's own site background (roses): https://serenitynailsalonspa.weebly.com/uploads/1/2/3/8/123851645/background-images/1404200096.jpeg. happy-feet-relaxing keeps its own banner.
- Shared niche stock photos with **no** names, signs, logos or phones (OK, left as is): electrician-at-panel photo on 18 HVAC/plumbing previews; bathtub photo on 10 plumbing/home-service previews; dentist-and-patient (5) and X-ray-review (3) photos on dental previews; pen-on-paper photo on 7 law previews (+ levine-law draft); handshake photo on john-holler-law and rashid-law.
- No gallery images exist on stamped Services/Contact pages; logos under assets/logos are per business (no cross-use).
