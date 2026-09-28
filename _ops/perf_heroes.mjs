// Re-encode preview hero photos: max 1200px wide, mozjpeg progressive, highest quality <= 90 KiB.
// Usage: SHARP_PATH=.../node_modules/sharp node _ops/perf_heroes.mjs list.txt  (list = repo-relative hero paths)
// Also writes <name>-800.jpg (<=45 KiB) for srcset. Originals are read from /tmp/photos-orig-backup if present (avoids re-encoding twice).
// Needs sharp: npm i sharp somewhere, then SHARP_PATH=/path/to/node_modules/sharp node _ops/perf_heroes.mjs list.txt
import fs from 'fs';
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const sharp = require(process.env.SHARP_PATH || 'sharp');
const LIMIT = 90 * 1024, MAXW = 1200;
const files = fs.readFileSync(process.argv[2], 'utf8').split('\n').filter(Boolean);
for (const f of files) {
  const src = fs.readFileSync(f);
  const meta = await sharp(src).metadata();
  if (meta.format !== 'jpeg') { console.log('skip (not jpeg)', f); continue; }
  if (src.length <= LIMIT && meta.width <= MAXW) { console.log('ok already', f, src.length); continue; }
  const w = Math.min(meta.width, MAXW);
  let best = null;
  for (let q = 82; q >= 50; q -= 2) {
    const out = await sharp(src).rotate().resize({ width: w, withoutEnlargement: true })
      .jpeg({ quality: q, mozjpeg: true, progressive: true, chromaSubsampling: '4:2:0' }).toBuffer();
    if (out.length <= LIMIT) { best = { q, out }; break; }
  }
  if (!best) { console.log('FAILED to hit limit', f); continue; }
  if (best.out.length >= src.length && meta.width <= MAXW) { console.log('keep original (already smaller)', f, src.length); continue; }
  fs.writeFileSync(f, best.out);
  const m2 = await sharp(best.out).metadata();
  console.log(f, `${meta.width}x${meta.height} ${src.length}B -> ${m2.width}x${m2.height} ${best.out.length}B q${best.q}`);
}

// Mobile variant: <name>-800.jpg (800px wide) for srcset; phones (412 CSS px x DPR 1.75) pick this one.
for (const f of files) {
  const out = f.replace(/\.jpe?g$/, '-800.jpg');
  if (out === f || fs.existsSync(out)) continue;
  const srcPath = fs.existsSync('/tmp/photos-orig-backup/' + f.split('/').pop()) ? '/tmp/photos-orig-backup/' + f.split('/').pop() : f;
  const src = fs.readFileSync(srcPath);
  const meta = await sharp(src).metadata();
  if (meta.format !== 'jpeg' || meta.width <= 800) continue;
  let best = null;
  for (let q = 82; q >= 50; q -= 2) {
    const buf = await sharp(src).rotate().resize({ width: 800 }).jpeg({ quality: q, mozjpeg: true, progressive: true, chromaSubsampling: '4:2:0' }).toBuffer();
    if (buf.length <= 45 * 1024) { best = { q, buf }; break; }
  }
  if (!best) { console.log('800w FAILED', f); continue; }
  fs.writeFileSync(out, best.buf);
  console.log(out, `800w ${best.buf.length}B q${best.q}`);
}
