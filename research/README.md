# BetterHealth competitive reverse-engineering study

Research workspace for the 14-site investigation defined in the master prompt.
Nothing in this folder changes the BetterHealth website.

**Status (2026-10-30):** network access opened mid-session; 12 of 14 sites captured; dossiers 01–05 (Group A) written. Neko Health (Vercel checkpoint) and One Medical (CloudFront 403) are blocked by bot protection and are not bypassed. REA has not been run. Original blocker history: [`00-availability-report.md`](00-availability-report.md).

## Layout

```
research/
  00-availability-report.md   why the investigation is paused and what unblocks it
  scripts/sites.json          the 14 mandatory subjects (ids, groups, entry URLs)
  scripts/capture.mjs         evidence capture harness (Playwright + CDP port for REA)
  scripts/digest.py, preview.py, stitch.py, compress.py   helpers (digest data, shrink screenshots, join scroll frames, shrink files)
  evidence/<site-id>/         raw evidence, written only by the harness or REA
    manifest.json             every capture: URL, final URL, HTTP status, viewport, timestamp, errors
    screens/<page>_<viewport>_{viewport,full}.png
    data/<page>_<viewport>.json   computed styles, fonts, colours, sections, CTAs, forms, full text
  dossiers/<site-id>.md       one dossier per site (written only from evidence/)
  synthesis/                  cross-site matrix + the six final deliverables (after all 14)
```

## Inspection protocol

1. **Capture** (`node research/scripts/capture.mjs [site-id ...]`): for each site,
   homepage plus up to five discovered pages (about/team, pricing/membership,
   approach/how-it-works, evidence/results, contact/booking), at 1440×900 and
   390×844. Viewport and full-page screenshots, computed styles, loaded font
   faces, colour frequency, max-width values, section boxes, heading outline,
   CTA inventory with destinations, form fields. No forms are submitted and no
   booking or checkout steps are completed.
2. **REA pass**: while the harness browser is open (CDP on port 9222), run
   `rea list-browser-targets`, `rea inspect-web-page` and
   `rea analyze-web-bundle` against each page and store the JSON output in
   `evidence/<site-id>/rea/`. Interaction states (menus, hover, form validation)
   are captured with `capture-browser-scenario` / `capture-web-screenshot`.
3. **Commercial evidence**: web search for published experiments, case studies
   (e.g. Metalab/Framer for Biograph), revenue and growth data. Each source is
   logged with URL and access date, and classified as experiment / company-reported /
   third-party estimate.
4. **Dossier**: written from steps 1–3 only, using the 10-section template from
   the master prompt. Every statement is tagged **Verified** (cites a screenshot
   file, data JSON field or source URL), **Interpretation**, or **Hypothesis**.
5. A site is marked complete in the progress table only when its dossier exists
   and every Verified claim resolves to a file in `evidence/`.

## Progress

| # | Site | Group | Captured | REA | Dossier |
|---|------|-------|----------|-----|---------|
| 01 | Heartwood Collective | A | captured | – | [dossier](dossiers/01-heartwood.md) |
| 02 | Biograph | A | captured | – | [dossier](dossiers/02-biograph.md) |
| 03 | Kusnacht Practice | A | captured | – | [dossier](dossiers/03-kusnacht.md) |
| 04 | Lanserhof | A | captured | – | [dossier](dossiers/04-lanserhof.md) |
| 05 | Chenot | A | captured | – | [dossier](dossiers/05-chenot.md) |
| 06 | Neko Health | B | blocked by bot protection | – | – |
| 07 | Function Health | B | captured | – | [dossier](dossiers/07-function-health.md) |
| 08 | Wild Health | B | captured | – | [dossier](dossiers/08-wild-health.md) |
| 09 | One Medical | B | blocked by bot protection | – | – |
| 10 | Parsley Health | B | captured | – | [dossier](dossiers/10-parsley-health.md) |
| 11 | Acquisition.com | C | captured | – | [dossier](dossiers/11-acquisition-com.md) |
| 12 | Gym Launch | C | captured | – | – |
| 13 | Spring Health | C | captured | – | – |
| 14 | Prestige Labs | C | captured | – | – |
