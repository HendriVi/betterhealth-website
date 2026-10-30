// Objective visual QC for a built BetterHealth page against a token file.
// Usage: node research/scripts/qc-check.mjs <url> --tokens=<tokens.json> [--out=<dir>] [--label=<name>]
//
// For each viewport (1440, 1024, 768, 390) it saves viewport + full-page screenshots and records:
//   overflow     horizontal scroll present
//   fonts        text whose primary font family is not in tokens.fonts
//   colours      text/background colours not in tokens.colours (hex, case-insensitive)
//   contrast     text with contrast below 4.5:1 (3:1 when >= 24px, or >= 18.66px and bold)
//   headings     number of h1, skipped levels
//   images       <img> without alt attribute
//   targets      (390 only) buttons/links outside paragraphs smaller than 44px in either direction
//   sizes        h1/h2/h3/body font-size outside tokens.sizes[viewport]
//   hidden       text elements still at opacity < 0.1 or visibility hidden after scrolling the whole page
//   console      console errors and failed requests
// Exit code 1 if any check fails. Writes <out>/<label>-report.json and a Markdown summary.
// It cannot judge aesthetic quality; see research/synthesis/06-implementation-qc-protocol.md.

import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';

const { chromium } = createRequire(import.meta.url)('playwright');
const args = process.argv.slice(2);
const opt = (n, d) => (args.find(a => a.startsWith(`--${n}=`)) || `=${d}`).split('=').slice(1).join('=');
const url = args.find(a => !a.startsWith('--'));
if (!url) { console.error('usage: qc-check.mjs <url> --tokens=<file> [--out=<dir>] [--label=<name>]'); process.exit(2); }
const tokens = JSON.parse(await fs.readFile(opt('tokens', ''), 'utf8'));
const outDir = opt('out', 'qc-out'); const label = opt('label', 'page');
await fs.mkdir(outDir, { recursive: true });

const VIEWPORTS = [
  { name: '1440', width: 1440, height: 900 }, { name: '1024', width: 1024, height: 768 },
  { name: '768', width: 768, height: 1024 }, { name: '390', width: 390, height: 844, mobile: true },
];
const allowedColours = new Set(tokens.colours.map(c => c.toLowerCase()));
const allowedFonts = tokens.fonts.map(f => f.toLowerCase());

const browser = await chromium.launch();
const report = { url, label, tokens: opt('tokens', ''), checkedAt: new Date().toISOString(), viewports: {}, failures: [] };

for (const vp of VIEWPORTS) {
  const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, isMobile: !!vp.mobile, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  const consoleErrors = [], failed = [];
  page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text().slice(0, 200)); });
  page.on('requestfailed', r => failed.push(`${r.url().slice(0, 120)} ${r.failure()?.errorText}`));
  await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
  await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 500) { scrollTo(0, y); await new Promise(r => setTimeout(r, 100)); } scrollTo(0, 0); });
  await page.waitForTimeout(800);
  await page.screenshot({ path: path.join(outDir, `${label}-${vp.name}-viewport.png`) });
  await page.screenshot({ path: path.join(outDir, `${label}-${vp.name}-full.png`), fullPage: true });

  const data = await page.evaluate(({ allowedColours, allowedFonts, isMobile, vpWidth }) => {
    const toHex = s => { const m = s.match(/rgba?\(([^)]+)\)/); if (!m) return null; const [r, g, b, a = 1] = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); if (a === 0) return null; return '#' + [r, g, b].map(v => Math.round(v).toString(16).padStart(2, '0')).join(''); };
    const lum = h => { const [r, g, b] = [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255).map(c => c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
    const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };
    // Composite semi-transparent background layers from the element up to the first opaque layer.
    // A gradient or image on the way makes the result unknown (img: true), and contrast is then skipped.
    const rgba = str => { const m = str.match(/rgba?\(([^)]+)\)/); if (!m) return null; const [r, g, b, a = 1] = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return { r, g, b, a }; };
    const bgOf = el => {
      const layers = [];
      for (let e = el; e; e = e.parentElement) {
        const cs = getComputedStyle(e);
        if (cs.backgroundImage !== 'none') return { img: true };
        const c = rgba(cs.backgroundColor); if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; }
      }
      let base = { r: 255, g: 255, b: 255 };
      for (const c of layers.reverse()) base = { r: c.r * c.a + base.r * (1 - c.a), g: c.g * c.a + base.g * (1 - c.a), b: c.b * c.a + base.b * (1 - c.a) };
      return { hex: '#' + [base.r, base.g, base.b].map(v => Math.round(v).toString(16).padStart(2, '0')).join('') };
    };
    const sel = el => el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '');
    const visible = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
    const hasOwnText = el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    const out = { fonts: [], colours: [], contrast: [], images: [], targets: [], hidden: [], sizes: {}, headings: { h1: 0, skipped: [] } };
    const textEls = [...document.querySelectorAll('body *')].filter(el => visible(el) && hasOwnText(el));
    for (const el of textEls) {
      const cs = getComputedStyle(el); const fam = cs.fontFamily.split(',')[0].replace(/["']/g, '').trim().toLowerCase();
      if (!allowedFonts.includes(fam)) out.fonts.push({ sel: sel(el), fam });
      const fg = toHex(cs.color); const bg = bgOf(el);
      if (fg && !allowedColours.includes(fg)) out.colours.push({ sel: sel(el), kind: 'text', hex: fg });
      if (bg.hex && !allowedColours.includes(bg.hex)) out.colours.push({ sel: sel(el), kind: 'background', hex: bg.hex });
      if (fg && bg.hex) {
        const px = parseFloat(cs.fontSize), bold = parseInt(cs.fontWeight) >= 700; const large = px >= 24 || (px >= 18.66 && bold);
        const r = ratio(fg, bg.hex); if (r < (large ? 3 : 4.5)) out.contrast.push({ sel: sel(el), fg, bg: bg.hex, ratio: +r.toFixed(2), px });
      }
      if (parseFloat(cs.opacity) < 0.1 || cs.visibility === 'hidden') out.hidden.push(sel(el));
    }
    for (const img of document.images) if (!img.hasAttribute('alt')) out.images.push(img.currentSrc.slice(-60));
    let last = 0; for (const h of document.querySelectorAll('h1,h2,h3,h4,h5,h6')) { const l = +h.tagName[1]; if (l === 1) out.headings.h1++; if (last && l > last + 1) out.headings.skipped.push(`${sel(h)} h${last}->h${l}`); last = l; }
    for (const t of ['h1', 'h2', 'h3', 'p']) { const e = [...document.querySelectorAll(t)].find(visible); if (e) out.sizes[t] = parseFloat(getComputedStyle(e).fontSize); }
    if (isMobile) for (const el of document.querySelectorAll('a,button')) { if (!visible(el) || el.closest('p,li > p')) continue; const r = el.getBoundingClientRect(); if (r.width < 44 || r.height < 44) out.targets.push({ sel: sel(el), w: Math.round(r.width), h: Math.round(r.height) }); }
    out.overflow = document.documentElement.scrollWidth > vpWidth + 1; // nominal width: on mobile, a zoomed-out page would make innerWidth equal scrollWidth
    out.scrollWidth = document.documentElement.scrollWidth;
    return out;
  }, { allowedColours: [...allowedColours], allowedFonts, isMobile: !!vp.mobile, vpWidth: vp.width });

  const sizeFail = [];
  for (const [t, v] of Object.entries(data.sizes)) { const rng = tokens.sizes?.[vp.name]?.[t]; if (rng && (v < rng[0] - 1 || v > rng[1] + 1)) sizeFail.push({ tag: t, size: v, allowed: rng }); }
  const uniq = (a, k) => [...new Map(a.map(x => [k(x), x])).values()];
  const v = { overflow: data.overflow, scrollWidth: data.scrollWidth, fonts: uniq(data.fonts, x => x.fam), colours: uniq(data.colours, x => x.kind + x.hex),
    contrast: data.contrast.slice(0, 15), h1Count: data.headings.h1, headingSkips: data.headings.skipped, imagesWithoutAlt: data.images, touchTargets: data.targets.slice(0, 15),
    sizes: data.sizes, sizeFailures: sizeFail, hiddenText: data.hidden.slice(0, 15), consoleErrors, failedRequests: failed };
  report.viewports[vp.name] = v;
  const f = [];
  if (v.overflow) f.push('horizontal overflow'); if (v.fonts.length) f.push(`${v.fonts.length} off-token font(s)`); if (v.colours.length) f.push(`${v.colours.length} off-token colour(s)`);
  if (data.contrast.length) f.push(`${data.contrast.length} contrast failure(s)`); if (v.h1Count !== 1) f.push(`h1 count ${v.h1Count}`); if (v.headingSkips.length) f.push('heading level skipped');
  if (v.imagesWithoutAlt.length) f.push(`${v.imagesWithoutAlt.length} image(s) without alt`); if (v.touchTargets.length) f.push(`${v.touchTargets.length} small touch target(s)`);
  if (sizeFail.length) f.push(`${sizeFail.length} size mismatch(es)`); if (v.hiddenText.length) f.push(`${v.hiddenText.length} text element(s) hidden after scroll`); if (consoleErrors.length) f.push(`${consoleErrors.length} console error(s)`);
  for (const x of f) report.failures.push(`${vp.name}px: ${x}`);
  await ctx.close();
}
await browser.close();
await fs.writeFile(path.join(outDir, `${label}-report.json`), JSON.stringify(report, null, 2));
const md = [`# QC report: ${label}`, `URL: ${url}`, `Checked: ${report.checkedAt}`, '', report.failures.length ? `**${report.failures.length} failure(s)**` : '**All objective checks passed**', '', ...report.failures.map(x => `- ${x}`)].join('\n');
await fs.writeFile(path.join(outDir, `${label}-report.md`), md);
console.log(md); process.exit(report.failures.length ? 1 : 0);
