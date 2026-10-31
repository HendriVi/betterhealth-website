# Deviation log: BetterHealth preview (`/next/`), Direction C + A accents

Checker: `research/scripts/qc-check.mjs` with `research/synthesis/tokens/direction-C.json`. Rounds 1–4, 2026-10-30. Screenshots and reports of the last round: `round-4/`.

| Round | Viewport | Check | Finding | Class | Action | Status |
|---|---|---|---|---|---|---|
| 0 | all | contrast (checker) | 48 "failures" on the old site, 47 caused by translucent backgrounds being treated as opaque | checker bug | composite alpha layers; gradients/images = unknown | fixed |
| 1 | 1440 | visual review (not found by checker) | `hyphens:auto` broke headings and navigation ("An-satz", "BetterHe-alth", "Stresssys-tem"); header wrapped onto two lines | true defect | hyphenation only in running text; header `nowrap`; shorter header CTA; "Fragen" removed from nav | fixed (round 2) |
| 1 | 390 | touch targets | `a.textlink` 29 px, footer link 26 px high | true defect | min-height 44 px | fixed |
| 2 | 390 | visual review | full-page screenshot 446 px wide on a 390 px viewport: horizontal overflow from the `nowrap` header; **the checker did not report it** | true defect + checker bug | `innerWidth` equals page width on a zoomed-out mobile page; checker now compares `scrollWidth` with the nominal viewport width; header uses a third, shorter CTA label under 640 px | fixed (round 3) |
| 3 | 390 | touch targets | wordmark link 35 px high | true defect | min-height 44 px | fixed (round 4) |
| 4 | 1440 | page height | 9,785 px vs the 9,500 px target in spec §1.1 | **accepted deviation** | none; within the 6.7–13.6k range measured on comparable sites | accepted (owner may overrule) |
| 4 | all | all objective checks, DE and EN | pass at 1440, 1024, 768, 390 | — | — | — |
| 4 | 1440 | aesthetic (see `critical-assessment-round-4.md`) | material/imagery 3/5: no photographs yet; fee panel leaves an empty dark area on the right | open | needs portrait and practice photographs; consider two-column fee layout | open |
| 5 | all | content update from the owner's reference document | all objective checks pass in DE and EN at 1440, 1024, 768, 390 | — | — | — |
| 5 | 1440 | page height | 10,358 px (was 9,785) after added content | **accepted deviation** | none | accepted (owner may overrule) |
| 6 | all | structure | the build had been one long page although the playbook (§7) and every reference site are multi-page | true defect (my error) | rebuilt as 9 pages per language; homepage now 6,478 px | fixed |
| 6 | 1440 | contrast (checker) | homepage "process in detail" link was pale text on a pale ground (1.03:1) | true defect | dark link style on light sections | fixed |
| 6 | 390 | touch targets | phone link in the call-to-action strip 38 px, footer link 43 px wide | true defect | min sizes | fixed |
| 6 | all | all objective checks | pass on 14 content pages (7 per language) at 1440, 1024, 768, 390 | — | — | — |
