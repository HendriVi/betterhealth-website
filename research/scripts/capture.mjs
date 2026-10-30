// Evidence capture harness for the 14-site reverse-engineering study.
// Usage: node research/scripts/capture.mjs [siteId ...] [--pages=6] [--cdp-port=9222]
//
// For each site it records, per page and per viewport (1440 / 390):
//   - viewport + full-page screenshots
//   - computed styles of headings, body copy, links/buttons, nav
//   - font faces actually loaded (document.fonts), colour frequency
//   - top-level section boxes (order, height, background)
//   - heading outline, CTA inventory (label + destination), forms + fields
// Everything is written under research/evidence/<siteId>/ with a manifest.json
// that records the timestamp, URL, viewport and HTTP status of every capture.
// Chromium is launched with a CDP port so REA's inspect-web-page /
// analyze-web-bundle can attach to the same browser during a run.
//
// Nothing here submits forms or clicks purchase/booking controls.

import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// require() also finds a globally installed Playwright, which ESM import does not.
const { chromium } = createRequire(import.meta.url)('playwright');
const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const args = process.argv.slice(2);
const opt = (name, dflt) => (args.find(a => a.startsWith(`--${name}=`)) || `=${dflt}`).split('=')[1];
const maxPages = Number(opt('pages', 6));
const cdpPort = Number(opt('cdp-port', 9222));
const only = args.filter(a => !a.startsWith('--'));
// --extra=/path1,/path2 adds specific pages (resolved against the site URL) to the discovered set.
const extra = opt('extra', '').split(',').filter(Boolean);
// --append keeps captures already in manifest.json (use with --extra to add pages without redoing the site).
const append = args.includes('--append');

const sites = JSON.parse(await fs.readFile(path.join(here, 'sites.json'), 'utf8'))
  .filter(s => only.length === 0 || only.includes(s.id));

const VIEWPORTS = [
  { name: 'desktop', width: 1440, height: 900 },
  { name: 'mobile', width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 3 },
];

// Secondary pages worth capturing, matched against link text and href.
const PAGE_HINTS = [
  /about|team|who-we-are|our-story|clinicians|doctors/i,
  /pricing|membership|plans|cost|fees|join/i,
  /how-it-works|approach|method|programme|program|services|treatment/i,
  /results|outcomes|evidence|science|research|case-stud|reviews|testimonials/i,
  /contact|book|enquir|inquir|get-started|apply|consult/i,
];

async function extract(page) {
  return page.evaluate(() => {
    const pick = el => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 200),
        fontFamily: cs.fontFamily, fontSize: cs.fontSize, fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight, letterSpacing: cs.letterSpacing, textTransform: cs.textTransform,
        color: cs.color, backgroundColor: cs.backgroundColor,
        x: Math.round(r.x), y: Math.round(r.y + scrollY), w: Math.round(r.width), h: Math.round(r.height),
      };
    };
    const visible = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
    const all = sel => [...document.querySelectorAll(sel)].filter(visible);

    const colorCount = {};
    for (const el of all('body *').slice(0, 4000)) {
      const cs = getComputedStyle(el);
      for (const v of [cs.color, cs.backgroundColor, cs.borderTopColor]) {
        if (v && v !== 'rgba(0, 0, 0, 0)') colorCount[v] = (colorCount[v] || 0) + 1;
      }
    }

    // Top-level sections: the direct children of the deepest wrapper that holds most of the page.
    let container = document.querySelector('main') || document.body;
    while (container.children.length === 1 && container.firstElementChild) container = container.firstElementChild;
    const sections = [...container.children].filter(visible).map((el, i) => {
      const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
      const h = el.querySelector('h1,h2,h3');
      return { index: i, tag: el.tagName.toLowerCase(), cls: String(el.className).slice(0, 80),
        top: Math.round(r.top + scrollY), height: Math.round(r.height), width: Math.round(r.width),
        background: cs.backgroundColor, backgroundImage: cs.backgroundImage !== 'none',
        paddingTop: cs.paddingTop, paddingBottom: cs.paddingBottom,
        heading: h ? h.innerText.trim().slice(0, 140) : null };
    });

    const maxWidths = {};
    for (const el of all('body *').slice(0, 4000)) {
      const mw = getComputedStyle(el).maxWidth;
      if (mw !== 'none' && mw.endsWith('px')) maxWidths[mw] = (maxWidths[mw] || 0) + 1;
    }

    return {
      title: document.title,
      metaDescription: document.querySelector('meta[name="description"]')?.content || null,
      generator: document.querySelector('meta[name="generator"]')?.content || null,
      docHeight: document.documentElement.scrollHeight,
      fontsLoaded: [...document.fonts].filter(f => f.status === 'loaded')
        .map(f => `${f.family} ${f.weight} ${f.style}`).filter((v, i, a) => a.indexOf(v) === i),
      body: pick(document.body),
      headings: all('h1,h2,h3,h4').map(el => ({ level: el.tagName, ...pick(el) })),
      paragraphs: all('p').slice(0, 40).map(pick),
      ctas: all('a,button').map(el => ({ ...pick(el), href: el.href || null,
        borderRadius: getComputedStyle(el).borderRadius, padding: getComputedStyle(el).padding }))
        .filter(c => c.text && c.text.length < 60),
      nav: all('header a, nav a').map(el => ({ text: el.innerText.trim(), href: el.href })).filter(n => n.text),
      forms: all('form').map(f => ({ action: f.action, fields: [...f.querySelectorAll('input,select,textarea')]
        .map(i => ({ type: i.type, name: i.name, label: i.labels?.[0]?.innerText?.trim() || i.placeholder || i.ariaLabel, required: i.required })) })),
      images: all('img').slice(0, 60).map(img => ({ src: img.currentSrc, alt: img.alt,
        w: img.getBoundingClientRect().width | 0, h: img.getBoundingClientRect().height | 0,
        natural: `${img.naturalWidth}x${img.naturalHeight}`, objectFit: getComputedStyle(img).objectFit })),
      colors: Object.entries(colorCount).sort((a, b) => b[1] - a[1]).slice(0, 25),
      maxWidths: Object.entries(maxWidths).sort((a, b) => b[1] - a[1]).slice(0, 12),
      sections,
      fullText: document.body.innerText.slice(0, 60000),
    };
  });
}

async function settle(page) {
  // Scroll through so lazy content and scroll-triggered sections render before capture.
  await page.evaluate(async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(800);
}

async function discoverPages(page, base) {
  const links = await page.$$eval('a[href]', as => as.map(a => ({ href: a.href, text: a.innerText.trim() })));
  const host = new URL(base).host;
  const picked = [];
  for (const hint of PAGE_HINTS) {
    const hit = links.find(l => {
      try { return new URL(l.href).host === host && !SKIP.test(l.href) && (hint.test(l.href) || hint.test(l.text)) && !picked.includes(l.href.split('#')[0]); }
      catch { return false; }
    });
    if (hit) picked.push(hit.href.split('#')[0]);
  }
  return picked.slice(0, maxPages - 1);
}

// Legal, account and utility pages are never useful design evidence.
const SKIP = /privacy|terms|legal|cookie|agreement|data-processing|career|jobs|login|log-in|sign-?in|cart|account|press|blog\/|podcast|imprint|impressum|accessib|sitemap|\.pdf/i;

async function dismissConsent(page) {
  // Prefer declining; fall back to accepting so the banner does not cover the capture.
  for (const re of [/^(decline|reject|deny|only (necessary|essential)|necessary only)/i, /^(accept|agree|allow|got it|ok)/i]) {
    for (const el of await page.$$('button, a[role="button"], [role="button"]')) {
      const t = ((await el.innerText().catch(() => '')) || '').trim();
      if (t.length < 40 && re.test(t) && await el.isVisible().catch(() => false)) {
        await el.click({ timeout: 2000 }).catch(() => {});
        await page.waitForTimeout(600);
        return t;
      }
    }
  }
  return null;
}

const slug = u => (new URL(u).pathname.replace(/\/+$/, '').replace(/[^a-z0-9]+/gi, '-').replace(/^-/, '') || 'home');

const browser = await chromium.launch({ args: [`--remote-debugging-port=${cdpPort}`] });
for (const site of sites) {
  const dir = path.join(root, 'evidence', site.id);
  await fs.mkdir(path.join(dir, 'screens'), { recursive: true });
  await fs.mkdir(path.join(dir, 'data'), { recursive: true });
  let manifest = { site, startedAt: new Date().toISOString(), captures: [], errors: [] };
  if (append) manifest = JSON.parse(await fs.readFile(path.join(dir, 'manifest.json'), 'utf8'));

  const pages = append ? [] : [site.url];
  for (const e of extra) pages.push(new URL(e, site.url).href);
  for (const vp of VIEWPORTS) {
    const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height },
      isMobile: vp.isMobile, hasTouch: vp.hasTouch, deviceScaleFactor: vp.deviceScaleFactor || 1, locale: 'en-US' });
    const page = await ctx.newPage();
    for (const url of pages) {
      const name = `${slug(url)}_${vp.name}`;
      try {
        const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
        await page.waitForLoadState('networkidle', { timeout: 15000 }).catch(() => {});
        const consent = await dismissConsent(page);
        await settle(page);
        // Extend in place so the running desktop loop also visits the discovered pages.
        if (!append && vp.name === 'desktop' && url === site.url) {
          for (const p of await discoverPages(page, site.url)) if (!pages.includes(p) && p !== page.url().split('#')[0]) pages.push(p);
        }
        await page.screenshot({ path: path.join(dir, 'screens', `${name}_viewport.png`) });
        await page.screenshot({ path: path.join(dir, 'screens', `${name}_full.png`), fullPage: true }).catch(e => manifest.errors.push({ url, vp: vp.name, step: 'fullpage', error: String(e) }));
        const data = await extract(page);
        await fs.writeFile(path.join(dir, 'data', `${name}.json`), JSON.stringify(data, null, 2));
        manifest.captures = manifest.captures.filter(c => !(c.url === url && c.viewport === `${vp.width}x${vp.height}`));
        manifest.captures.push({ url, finalUrl: page.url(), status: res?.status() ?? null, consentClicked: consent, viewport: `${vp.width}x${vp.height}`,
          capturedAt: new Date().toISOString(), screens: [`${name}_viewport.png`, `${name}_full.png`], data: `${name}.json` });
        console.log(`ok  ${site.id} ${vp.name} ${url}`);
      } catch (e) {
        manifest.errors.push({ url, vp: vp.name, error: String(e).slice(0, 500) });
        console.log(`ERR ${site.id} ${vp.name} ${url}: ${String(e).split('\n')[0]}`);
      }
    }
    await ctx.close();
  }
  manifest.finishedAt = new Date().toISOString();
  await fs.writeFile(path.join(dir, 'manifest.json'), JSON.stringify(manifest, null, 2));
}
await browser.close();
