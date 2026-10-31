# BetterHealth preview site (`/next/`)

Direction C "The System" with accents of A "The Formulation" (see `research/synthesis/05-art-directions.md`, `07-decisions-and-facts.md`).
**Staging only:** `noindex`, highlighted `[placeholders]`, form not connected. The live site (`/index.html`) is unchanged.

**Pages (German in `next/`, English in `next/en/`):** home · Ansatz/Approach · Begleitung/Support · Erster Termin/First visit (process, fee) · Über uns/About · Fragen/Questions · Kontakt/Contact · Datenschutz/Privacy · Impressum/Imprint.

- All pages are generated: edit `src/content.py` (text, facts, form endpoint) or `src/build.py` (markup), then run `python3 next/src/build.py`.
- Styles `assets/css/main.css`, script `assets/js/main.js` (progressive enhancement), fonts `assets/fonts/` (self-hosted; licences alongside).
- Check: `node research/scripts/qc-check.mjs <url> --tokens=research/synthesis/tokens/direction-C.json --out=qc/round-N --label=<page>`; log in `research/qc/deviations.md`.
- Form: set `FACTS["form_endpoint"]` in `src/content.py` to the URL of your server; empty shows a preview notice.
- Before launch: fill every placeholder, add photographs, have a lawyer review the legal pages and medical wording.
