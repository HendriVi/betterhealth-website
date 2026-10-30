# Visual design specification

**Purpose:** a reference concrete enough that a coding agent can build any of the three art directions (`05-art-directions.md`) without inventing the design language.
**Structure:** Part 1 rules shared by all directions · Part 2 component specifications · Part 3 token sets for Direction A, B and C · Part 4 visual quality criteria.
**Provenance:** where a value comes from a measured competitor range, the source is given as *(measured: site)*. Where it is a design decision, it is marked *(decision)*. Nothing here claims that a value raises conversion.
**Not yet verified:** all values need to be checked in a browser build (`06-implementation-qc-protocol.md`). Contrast ratios in Part 3 were computed from the hex values with the WCAG formula.

---

## Part 1 · Shared rules

### 1.1 Viewports and layout

| Item | Value |
|---|---|
| Design baselines | 390 px (mobile), 768 px (tablet), 1024 px (small desktop), 1440 px (desktop) *(decision; 1440 and 390 match the research captures)* |
| Max page width | 1440 px; content container 1200 px *(decision; competitors measured 1120–1480 px: Wild 1280, Function 1376, Heartwood 1398)* |
| Reading measure | 640–680 px wide, 60–72 characters per line *(decision; competitors' text columns measured 562–810 px)* |
| Grid | 12 columns on desktop, 24 px gutters; 4 columns on mobile, 16 px gutters, 24 px side margins *(decision)* |
| Section vertical padding | desktop 120 px (A: 96 px; B: 160 px), mobile 72 px *(decision; measured 48–240 px across sites)* |
| Spacing scale | 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 120 · 160 px. No other values *(decision)* |
| Homepage length target | 7,000–9,500 px at 1440 px *(decision; measured range of the premium-medical sites 6,666–13,571 px)* |

### 1.2 Typography rules (all directions)

- Body text: **18 px / 1.6** on desktop, **17 px / 1.6** on mobile *(measured: Parsley and Spring 18 px; Chenot 20.8 px; Function 16 px; below 16 px is not used for running text)*.
- Large headings use line-height **0.95–1.1** and tracking **−0.01 to −0.02 em** where the face is a serif or grotesque display face *(measured: Biograph, Parsley, Function)*; uppercase labels use **+0.08 to +0.14 em** *(measured: Kusnacht 0.04 em, Chenot 0.06–0.10 em, Lanserhof 0.08 em)*.
- Maximum three type sizes per section plus the label size.
- Fluid headings with `clamp()`; no heading below 28 px on mobile for H2, 36 px for H1 *(measured mobile H1: 28 px Spring, 41 Biograph, 48 Parsley, 57 Function)*.
- Italic is used for emphasis within a heading, never for body text. At most one emphasised phrase per heading.
- Fonts are **self-hosted** (WOFF2, `font-display: swap`) to avoid third-party requests that disclose visitors' IP addresses *(decision; relevant to a medical site and Swiss data protection; confirm with counsel)*.
- Language: German first, English second. Allow **+30 % text length** in German in every component.

### 1.3 Imagery rules

- Every photograph is **real** (commissioned or owned). No stock images of brains, neurons, DNA, silhouettes, handshakes or people looking at screens *(decision)*.
- One identifiable photograph of the treating physician appears on the homepage above the fold's first scroll, or within the first two sections, with name, role and one line about what they do in the process *(decision; reason: competitors that sell a clinician's judgment show named clinicians; those that do not show one rely on logos and quotes)*.
- Aspect ratios: hero 16:9 desktop / 4:5 mobile; portrait 4:5; inline 3:2; diagram frames 4:3. Maximum file size 250 KB per image at delivered size; `loading="lazy"` below the fold; explicit `width` and `height` to prevent layout shift.
- Alt text describes content in a sentence; decorative images have `alt=""`.
- No faces of patients. No testimonial photographs.

### 1.4 Motion rules

- Transitions 180–320 ms, `ease-out`. No parallax. No autoplay video with sound; video may not be the only carrier of information.
- **All content must be visible without scroll-triggered animation.** Reveal effects may only change opacity and a translation of ≤ 16 px, must complete within 400 ms, and must not hide content for users who disable JavaScript or set `prefers-reduced-motion` *(reason: in this research, Kusnacht, Chenot and others hid content until scrolled, which broke full-page capture)*.
- Honour `prefers-reduced-motion: reduce` by disabling all transitions except focus changes.

### 1.5 Accessibility minimums

| Item | Requirement |
|---|---|
| Text contrast | ≥ 4.5:1 body, ≥ 3:1 for text ≥ 24 px or ≥ 19 px bold |
| Focus | visible 2 px outline, 2 px offset, colour contrast ≥ 3:1 with adjacent colours |
| Touch targets | ≥ 44 × 44 px |
| Form inputs | font-size ≥ 16 px (prevents mobile zoom); visible labels above fields; error text linked with `aria-describedby` |
| Structure | one `h1` per page; landmark roles; skip link; `lang` and `hreflang` for `de` and `en` |
| Colour | information is never carried by colour alone |

### 1.6 Interaction pattern for the single action

- One primary action per screen: **"Request a confidential conversation"** (wording in the playbook). One style for it across the whole site *(measured: Function, Spring, Kusnacht, Acquisition each reserve one colour/shape for the action)*.
- The primary action appears: in the header on all pages, at the end of the hero, after the process section, after the fee section and in the final section.
- A telephone number and a secure message option sit beside it in the header on desktop and in the contact section on mobile.

---

## Part 2 · Component specifications

Each component lists structure, content rules, and sizing. Direction tokens (Part 3) supply colours, faces and radii.

### C1 Header
- Height 72 px desktop, 64 px mobile. Wordmark left; 4 links (Approach, Care, About, Insights); right: telephone link, primary button. Mobile: wordmark, button, menu icon.
- Sticky; background is the page ground colour at 92 % opacity with no blur effect. Border-bottom 1 px `--rule` only after the user scrolls.
- Language switch (DE | EN) in the footer and in the mobile menu.

### C2 Hero
- Left-aligned heading (max 14 words), one supporting sentence (max 28 words), primary button, secondary text link ("See how a first visit works").
- Beneath: a **fact strip** of 3–4 operational facts, each ≤ 4 words with a one-line explanation (e.g. length of first visit, who sees you, how soon you are contacted, how fees are set). Only facts the practice can verify; no outcome figures.
- Height: min 640 px, max 100 vh at 1440 × 900.

### C3 Section header
- Label (uppercase, 12 px) · heading · optional one-sentence lead. Always in this order. Label is a topic word, not a slogan.

### C4 Recognition list (problem in patient words)
- 3–6 short entries. Each: a sentence in first-person plural or second person describing an experience (≤ 18 words), followed by one line stating the clinical question it raises (≤ 18 words).
- Layout: two columns desktop (entries stacked), one column mobile. No icons.

### C5 Process steps
- 4 numbered steps (01–04), each with title (≤ 5 words), 2 sentences (≤ 40 words total) and one line stating what the patient receives or does.
- Between steps a thin connector line on desktop. Step 1 has a link to the first-visit detail page.
- A **deliverable mock-up** panel beside the steps shows a fictional example formulation summary, labelled "Example, fictional data" *(mechanism measured at Biograph, Function)*.

### C6 Offer / fee card
- Name, one-sentence purpose, **fee in CHF with unit**, duration, a ruled list of inclusions (4–8 items), a ruled list of exclusions (2–4 items), terms (cancellation, payment, how the fee relates to later care), primary button.
- If the fee is credited toward ongoing care, say so in the card's first line of terms.
- Maximum two cards side by side; third options go on a separate page.

### C7 Clinician block
- Portrait (4:5), name, title, qualifications as a plain list (degree, specialist title, registration), "What you will work on with Dr. X" (3 bullets), languages spoken, a link to full CV. No awards without issuer and year.

### C8 Evidence block
- Required fields: *what was measured · in whom (n) · over what period · by which instrument · who ran it · source link (ungated)*. A block missing any field does not ship. Biomarker changes are labelled as such and not as outcomes.
- If no BetterHealth outcome data exist, this block carries a "How we track progress" explanation and the validated scales used, with no percentage.

### C9 FAQ accordion
- 8–12 questions, grouped under 3 labels (Before you contact us · The first visit · Fees and privacy). Answers ≤ 90 words. First item open by default on mobile is closed; on desktop the first is open. Includes: the hard case, the "asking for someone else" case, and the "does this replace my current doctor" case.

### C10 Enquiry form
- Fields: first name (required); one of email or phone (required, choice is shown); preferred contact time (select, optional); "Anything you want us to know first" (optional text area, labelled *no need to describe symptoms*).
- Above the button: what happens next, in three lines (who reads this, when you will hear back, what is not stored). Below: consent text. No marketing opt-in checkbox on this form.
- Maximum **4 visible inputs**, of which 2 required *(measured counter-example: Chenot requires 7 inputs; Parsley asks 2)*.

### C11 Diagram frame
- A single explanatory diagram, 4:3, drawn in the direction's line style, with a one-sentence caption stating what the reader should conclude. Labels ≥ 14 px. No decorative brain imagery.

### C12 Footer
- Four columns: Care (links), About (links), Contact (address, telephone, hours, secure message), Legal (privacy, imprint). A one-sentence note on confidentiality and on what the practice does not do (e.g. emergencies: refer to emergency services; number placeholder).

---

## Part 3 · Token sets

### 3.A Direction A · "The Formulation"

| Token | Value | Notes |
|---|---|---|
| `--paper` | `#F6F3EC` | page ground |
| `--paper-2` | `#ECE7DA` | panels |
| `--ink` | `#16181D` | text; 16.03:1 on paper |
| `--ink-2` | `#4A4E57` | secondary text; 7.52:1 on paper, 6.75:1 on paper-2 |
| `--rule` | `#CFC8B8` | hairlines |
| `--accent` | `#2432A8` | ultramarine; actions and emphasis; 9.04:1 on paper; white text on accent 10.02:1 |
| Display face | Source Serif 4, weight 300–400, optical size auto | italics for the emphasised phrase |
| Text face | IBM Plex Sans 400 / 500 | |
| Label/number face | IBM Plex Mono 500, 12 px, uppercase, +0.08 em | |
| H1 | `clamp(44px, 6vw, 80px)` / 1.0, −0.02 em | |
| H2 | `clamp(32px, 4vw, 48px)` / 1.08, −0.015 em | |
| H3 | 28 px / 1.2 | |
| Body | 18 px / 1.6 (mobile 17 px) | |
| Radius | buttons 2 px; cards 0 px | |
| Button | height 52 px, padding 0 28 px, accent fill, white text 16 px/500; secondary: 1 px `--ink` outline | |
| Line style | 1 px `--ink` hairlines; diagrams drawn with 1.5 px strokes | |
| Section padding | 96 px desktop | |
| Grid | 12 col with a left 3-column "margin notes" rail on sections C4, C5, C8 | |

### 3.B Direction B · "The Quiet Room"

| Token | Value | Notes |
|---|---|---|
| `--blush` | `#F3EAE6` | page ground |
| `--blush-2` | `#E7D8D2` | panels |
| `--ink` | `#231B29` | text; 14.06:1 on blush |
| `--ink-2` | `#5B4F62` | secondary; 6.47:1 on blush, 5.53:1 on blush-2 |
| `--accent` | `#5A2A52` | plum; actions; white on accent 11.12:1; accent on blush 9.39:1 |
| `--rule` | `#D6C3BD` | hairlines |
| Display face | Instrument Serif 400 (roman + italic) | |
| Text face | Instrument Sans 400 / 500 | |
| Label | Instrument Sans 500, 12 px, uppercase, +0.14 em | |
| H1 | `clamp(48px, 7vw, 96px)` / 1.02, −0.01 em | |
| H2 | `clamp(36px, 5vw, 56px)` / 1.05 | |
| H3 | 30 px / 1.2 | |
| Body | 19 px / 1.65 (mobile 17 px) | |
| Radius | buttons 999 px (pill); images 4 px | |
| Button | height 56 px, padding 0 36 px, plum fill, blush text 16 px/500 | |
| Section padding | 160 px desktop | |
| Text column | single column 640 px, offset left on 12-col grid (cols 2–7), image in cols 9–12 | |

### 3.C Direction C · "The System"

| Token | Value | Notes |
|---|---|---|
| `--graphite` | `#12151A` | dark ground |
| `--graphite-2` | `#1B2027` | panels |
| `--text` | `#ECEAE4` | on graphite 15.21:1; on graphite-2 13.61:1 |
| `--text-2` | `#A9AEB6` | 8.20:1 on graphite; 7.34:1 on graphite-2 |
| `--ice` | `#9FD9E6` | actions and diagram strokes; 11.80:1 on graphite; text `#0C1A1F` on ice 11.45:1 |
| `--bone` | `#EFEDE6` | light-section ground; ink `#12151A` on bone 15.62:1 |
| `--line` | `#2B323B` | hairlines on dark |
| Display face | Bricolage Grotesque 500 (opsz variable) | |
| Text face | Hanken Grotesk 400 / 500 | |
| Data/label face | JetBrains Mono 500, 12 px, +0.06 em | |
| H1 | `clamp(40px, 5.5vw, 72px)` / 1.0, −0.03 em | |
| H2 | `clamp(30px, 3.6vw, 44px)` / 1.1, −0.02 em | |
| H3 | 24 px / 1.25 | |
| Body | 18 px / 1.6 | |
| Radius | buttons 8 px; panels 12 px | |
| Button | height 52 px, padding 0 28 px, ice fill, `#0C1A1F` text 16 px/600 | |
| Section rhythm | alternating dark and bone sections; the diagram section is always dark | |
| Diagram | the central "clinical map" at 1,200 × 800 px in 1.5 px ice strokes on graphite | |

**Palette note [V from measurements]:** none of the three palettes is in the family of Parsley (`#284849/#F8F6F2/#4A786A`), Spring Health (`#01382E/#8DFF9D`) or the current BetterHealth CSS (`#153533/#fffcf4/#738b7f/#7bbeb2`). Function's terracotta (`#B05A36`), Kusnacht's olive (`#686F45`) and Heartwood's green/gold/brown are also not used.

---

## Part 4 · Visual quality criteria

A build passes visual review only if **all objective criteria pass** and the **critical assessment** (`06-…`) scores ≥ 4 of 5 on every dimension.

**Objective (machine-checkable):**
1. All colours used in computed styles belong to the direction's token set (± 0 tolerance on text and backgrounds).
2. All font families on `h1–h6`, `p`, `a`, `button`, `label`, `input` belong to the direction's faces.
3. Font sizes on headings and body match the type scale at 1440 and 390 px (± 1 px).
4. Spacing between sections equals one value of the scale.
5. Contrast ≥ 4.5:1 for all text under 24 px; ≥ 3:1 for large text.
6. No horizontal scroll at 390, 768, 1024, 1440 px.
7. Touch targets ≥ 44 px at 390 px.
8. Exactly one `h1`; no heading level skipped.
9. One primary-action style site-wide; one primary action visible per viewport.
10. No image without `alt`; no layout shift above 0.1 CLS in a local run.
11. No content hidden until scroll (all text visible in a full-page screenshot with JavaScript on).

**Aesthetic (critical assessment):** composition, hierarchy, rhythm, material (imagery/line), voice-visual fit, and absence of generic "template" signs. Defined with a rubric and anti-patterns in `06-implementation-qc-protocol.md`.
