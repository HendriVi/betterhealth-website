# Implementation and visual quality-control protocol

**Audience:** Codex (or another coding agent) converting an **approved** art direction into the BetterHealth website.
**Precondition:** the owner has chosen a direction (`05-art-directions.md`) and filled the facts listed in §1. **No code is written before that.**
**Tools that exist now (tested):** `research/scripts/qc-check.mjs` (objective checks), `research/scripts/compare-shots.py` (screenshot change report), token files `research/synthesis/tokens/direction-{A,B,C}.json`, Playwright with Chromium.
**Not yet tested:** a real build; the checks were run once against the current `index.html` and found one genuine contrast problem (12.5 px sage text on cream, 3.52:1) after one false-positive bug was fixed (translucent backgrounds), which is why §6 insists on reading failures before acting on them.

---

## 1. Inputs required before building

1. Chosen direction and any named component swaps (spec Part 3 tokens apply unmodified).
2. **Facts** (`[placeholders]` in the playbook): physician name, title, qualifications, registration; first-assessment duration, fee (CHF, unit), inclusions, exclusions, credit rule; response time; telephone; opening hours; address; languages; emergency number; confidentiality practices (hosting, retention, who reads messages).
3. **Assets:** physician portrait; practice-room photographs (B requires the shot list; A requires two; C requires two); logo or wordmark text.
4. **Fonts:** WOFF2 files for the direction's faces, downloaded and self-hosted (no runtime requests to font CDNs).
5. German copy approved by a native speaker; English copy approved by the owner.
6. Confirmation of the points in playbook §10 with counsel (at minimum: contact form hosting, whether messaging apps are used, analytics/cookies).

If any item is missing, build the page with visible `[placeholder]` text styled in `--accent` so it cannot be mistaken for final content, and list it in the hand-off.

## 2. Build rules

- **Stack:** static HTML + CSS + minimal JavaScript, matching the current repo (`index.html`, GitHub Pages, `.nojekyll`). No framework unless the owner asks. No runtime dependency on external CDNs.
- **Tokens as CSS custom properties** at `:root`, named exactly as in the spec (`--paper`, `--ink`, …). Components use only these variables; no raw hex in component rules.
- **Type scale** with `clamp()` exactly as specified; spacing from the spec's scale only.
- **Structure first:** write semantic HTML for every section from the playbook skeleton before styling; then style.
- **Bilingual:** `de` default at `/`, `en` at `/en/`, each with `lang` and `hreflang`; shared CSS.
- **No content hidden until scroll** (spec §1.4). Reveal animations are cosmetic and off for `prefers-reduced-motion`.
- **Forms:** four inputs maximum; posting to a destination chosen by the owner after the data-protection review; no third-party form embed that changes the page's look.
- **Do not copy** competitor wording, images, fonts or branding (all 12 dossiers list what not to copy).
- **Do not modify** the existing pages until the new site is verified: build in a new directory (for example `/next/`), then swap.

## 3. Build order

1. Tokens and base styles (reset, type, links, focus ring, buttons, form fields).
2. Components C1–C12 as a static `/components.html` showing each in isolation at 390 and 1440 px.
3. Homepage assembled from components in the direction's section order.
4. Remaining pages from playbook §7.
5. Language variant.
6. Performance and accessibility pass.

Run the QC loop (§4) after each of steps 2, 3 and 4.

## 4. The QC loop

```
node research/scripts/qc-check.mjs <url> \
  --tokens=research/synthesis/tokens/direction-X.json \
  --out=qc/round-N --label=<page>
python3 research/scripts/compare-shots.py qc/round-(N-1) qc/round-N
```

1. **Serve locally** (`python3 -m http.server` from the build directory).
2. **Run the objective checker.** It records at 1440, 1024, 768 and 390 px: viewport and full-page screenshots; horizontal overflow; fonts not in the token list; text and background colours not in the palette; contrast below 4.5:1 (3:1 for large text); `h1` count and skipped heading levels; images without `alt`; touch targets under 44 px (at 390); heading and body sizes outside the token range; text still invisible after scrolling; console errors and failed requests.
3. **Read every failure before acting.** The checker has already produced a false positive once (translucent backgrounds). Classify each failure as **true defect**, **false positive** (explain why, and fix the checker if it is a bug), or **accepted deviation** (owner-approved, recorded in the log).
4. **Fix true defects**, change at most one concern per commit (for example "contrast of labels"), re-run.
5. **Compare screenshots** with the previous round. A fix must change only the areas you intended; unexpected change above 2 % of pixels is investigated.
6. **Stop** when all objective checks pass at all four widths, or after **five rounds**, whichever comes first. After five rounds, stop and report what remains and why.
7. Only then run the **critical assessment** (§5).

### Deviation log (kept in `qc/deviations.md`)

| Round | Page | Viewport | Check | Finding | Class | Action | Status |
|---|---|---|---|---|---|---|---|
| 1 | home | 390 | contrast | `.program-label` `#738b7f` on `#fffaf0` = 3.52:1 | true defect | darken to `--ink-2` | fixed (round 2) |

(The first row is the real finding from the current site, included as the format example.)

## 5. Critical assessment of aesthetic coherence (separate pass)

**Rule:** perform this pass **after** the objective checks pass, as a different step with different inputs. The reviewer (a second agent run, or the owner) sees **only the screenshots** (`*-viewport.png`, `*-full.png` at 1440 and 390), the direction description (`05-…`) and the spec's Part 4. It does **not** read the code or the checker's report. The review is written before any fix.

### 5.1 Scores (1–5; ≥ 4 on every line to pass)

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| **Concept legibility** | The concept cannot be guessed | Visible in places | A first-time viewer could describe the concept ("a document", "a quiet room", "a map") without being told |
| **Hierarchy** | Several equal-weight competing elements per screen | Mostly clear; occasional ties | One dominant element per screen; the primary action is findable in 2 seconds |
| **Rhythm and spacing** | Irregular gaps, crowded or arbitrary | Mostly consistent | Spacing follows the scale throughout; sections differ in length deliberately |
| **Typography** | Faces or sizes mixed without reason | Correct but flat | The type does the work the direction names (A: exactness; B: calm; C: precision), with no more than three sizes per section |
| **Material and imagery** | Stock-like, mixed treatments | Acceptable, uneven | One treatment throughout; every image is specific to the practice |
| **Fit with voice and content** | Layout and copy feel like different documents | Mostly aligned | Layout makes the copy easier to read and believe |

### 5.2 Anti-pattern checklist (any "yes" is a failure to fix)

Generic or "template" signs to look for in the screenshots:
- A gradient blob, aurora or mesh gradient as a background.
- A violet-to-blue or similar "AI" gradient on text or buttons.
- Glass-morphism cards (blurred translucent panels).
- A three-icon feature grid with line icons.
- Uniform rounded cards with the same shadow repeated through the page.
- Emoji, or sparkle icons, as bullets or decoration.
- Centred everything, including long paragraphs.
- A hero with a stock photograph of a brain, a silhouette or a person looking at a screen.
- A "trusted by" logo row, an invented award or an invented review count.
- A countdown, a coupon, or "limited places" language.
- Lorem ipsum or filler headings such as "Our Services", "Why Choose Us".
- More than one primary-action style on the page.
- Any component that looks like it was copied from a competitor's page (compare against the dossier screenshots).

### 5.3 Output of the pass

A short report: the six scores with one sentence each; the checklist with yes/no and the screenshot region for each "yes"; the three changes that would most improve coherence, ranked. The owner decides which to apply; the loop in §4 restarts for any change.

## 6. What the checker cannot do

- It cannot judge beauty, tone, or whether copy is true.
- It cannot detect an image that looks like stock. Only §5 can.
- Contrast on gradient or image backgrounds is **skipped** (unknown), so those areas need a human check at the screenshot level.
- It checks the first visible `h1/h2/h3/p` for size, not every instance.
- Colour checks compare exact hex values; anti-aliased or blended effects are not modelled.
- It does not measure performance (no Lighthouse). If a performance budget is required, add a Lighthouse run to the loop; its use was not tested here.
- Failed external requests will show up as console errors; the build should have none, since no CDNs are allowed.

## 7. Release checklist (all must be yes)

1. Objective checks pass at 1440, 1024, 768, 390.
2. Critical assessment scores all ≥ 4 and the anti-pattern list is clear.
3. No `[placeholder]` text remains.
4. Every statement of fact (fees, credentials, durations) has been confirmed in writing by the owner.
5. German and English versions both pass the checks.
6. Privacy, imprint and cookie text approved by counsel.
7. A rollback exists: the previous site remains in Git history and in `/legacy/` for 30 days.
8. A one-page hand-off lists: deviations accepted, tests proposed (playbook §8), measures to track (qualified enquiry rate, completed enquiry rate, enquiry suitability, consult-to-patient conversion).

## 8. Re-running the comparative research

After launch, re-capture BetterHealth with `research/scripts/capture.mjs` (add an entry to `sites.json`), and compare its measured type scale, section heights and form fields against this specification. Record any mismatch in `qc/deviations.md`.
