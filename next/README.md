# BetterHealth preview site (`/next/`)

Direction C "The System" with accents of A "The Formulation" (see `research/synthesis/05-art-directions.md`, `07-decisions-and-facts.md`).
**Staging only:** `noindex`, highlighted `[placeholders]`, form not connected. The live site (`/index.html`) is unchanged.

- German: `index.html` · English: `en/index.html`. Both are generated: edit `src/content.py` (text, facts) or `src/build.py` (markup), then run `python3 next/src/build.py`.
- Styles `assets/css/main.css`, script `assets/js/main.js` (progressive enhancement), fonts `assets/fonts/` (self-hosted; licences alongside).
- Check: `node research/scripts/qc-check.mjs <url> --tokens=research/synthesis/tokens/direction-C.json --out=qc/round-N --label=home-de`; log in `research/qc/deviations.md`.
- Before launch: fill every placeholder, confirm every item in `research/synthesis/07-decisions-and-facts.md` §6, connect the form after the data-protection review, add legal pages, add photographs.
