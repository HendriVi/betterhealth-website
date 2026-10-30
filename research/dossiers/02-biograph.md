# 02 · Biograph — https://www.biograph.com

**Group A · Premium healthcare presentation, clinical authority, membership architecture**
**Captured:** 2026-10-30 · Chromium (Playwright) 1440×900 and 390×844 · REA not yet run
**Evidence folder:** `../evidence/02-biograph/`

Labels: **[V]** Verified (a file in `evidence/` shows it) · **[I]** Interpretation · **[H]** Hypothesis · **[U]** Unverified / not inspected.

Pages captured: `/` (200) · `/how-biograph-works` (200) · `/memberships` (200) · `/contact` (**502**, error page recorded, nothing inferred from it).
Not captured: `members.biograph.com/get-started`, the sign-up flow all primary buttons lead to (separate subdomain, not visited). Compare page, FAQ page, clinic pages, blog, employer page.
**Not yet done:** the Metalab/Framer design case study the master prompt asks for. It has not been fetched, so nothing about it is claimed here.

---

## 1. Business model, customer, commercial context

- **[V]** A physician-led preventive-health assessment sold as a membership with two tiers, **Core** and **Black**, in New York City and the San Francisco Bay Area (`memberships_desktop.json`, `home_desktop.json`).
- **[V]** Price shown: **Core "$7,500 for the first year"**, "Subsequent-year pricing varies by recommended tier" (`memberships_desktop.json` → fullText). The Black tier price was not found in the captured text.
- **[V]** A second audience is signposted in the navigation: "For Employers".
- **[V]** Biograph positions itself as an addition to a regular doctor: "Biograph doesn't replace your primary care physician (PCP). Instead, it complements traditional healthcare…" (FAQ, `home_desktop.json`).
- **[V]** The site is built with Framer (`<meta name="generator" content="Framer d57bcd3">`).
- **[I]** The buyer is a healthy, affluent, data-minded adult paying out of pocket for earlier detection. The site's job is to justify a four-figure price and a booking before the visitor has any symptom.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/home_desktop_viewport.png` |
| Homepage full page (13,571 px) | `screens/home_desktop_full.jpg` |
| Homepage mobile (14,096 px) | `screens/home_mobile_full.jpg` |
| Memberships | `screens/memberships_desktop_full.jpg` |
| How it works | `screens/how-biograph-works_desktop_full.jpg` |

## 3. Measured visual specifications

From `data/home_desktop.json` unless noted.

**Typefaces loaded [V]:** Aeonik Regular (headings), Apercu Pro Regular / Medium / Bold (body and UI), Instrument Serif (the large testimonial quote, visible in `home_desktop_full.jpg`).

| Role | Face | Size / line-height | Letter-spacing | Colour |
|---|---|---|---|---|
| H1 | Aeonik 400 | 68 px / 64.6 px (0.95) | −1.36 px (−0.02 em) | white on photo; `#27272C` on memberships |
| H2 section titles | Aeonik 400 | 52 px / 52 px (1.0) | −0.52 px (−0.01 em) | `#27272C` or white |
| Tier titles H2/H3 | Aeonik 400 | 32 px / 38.4 px | — | |
| Card titles H3 | Aeonik 400 | 24 px / 28.8 px | — | |
| Step and feature titles | Apercu Pro 400 | 16 px / 24 px (1.5) | — | `#27272C` |
| Body | Apercu Pro 400 | 16 px / 24 px | — | `#686873` (grey) |
| Small body in cards | Apercu Pro 400 | 14 px / 21 px; 12 px / 18 px | — | white on dark cards |

All headings are weight 400. Hierarchy comes from size, tight leading and negative tracking, not from bold.
**Mobile [V]:** H1 41 px, H2 32 px (24 px on the memberships tier titles).

**Colour [V]:** `#000000` (largest by count) · `#27272C` (ink) · `#686873` (secondary text) · `#F9F9F9` (alternate light background) · `#FFFFFF`. Also a link blue `rgb(0,0,238)`, the browser default, which appears on unstyled inline links in the capture (986 elements); treat it as a rendering artefact of Framer's anchors, not a design colour.

**Layout [V]:** max-width values 1600 px (16 uses), 1480 px (5), 460, 400, 370, 305 px (cards, 22 uses). Page height 13,571 px (desktop). Button radius 8 px; card radius 16 px. The `sections` array is empty because Framer does not use a simple wrapper, so section heights are not given; positions below come from `home_desktop_full.jpg`.

**Homepage section order [V, from the screenshot]:**
1. Full-viewport hero: night-time photo of a lit glass building; H1 bottom-left; below it one line of copy and "Join Biograph"; bottom-right a three-cell strip: "Up to 30+ Assessments", "1 in 6 members Discover urgent findings", "Clinician-led Expert medical guidance". Top bar: wordmark, centred nav, "Login" and "Join Biograph".
2. White "How Biograph works" with a small-caps label above the H2, three vertical photo cards (MRI bed with coloured light; a tablet video call with a doctor; a runner at dusk), each numbered 1–3 with two lines of text.
3. One large Instrument Serif testimonial, attributed to a named person with a descriptor.
4. Three bordered stat cells: "96 %", "1 in 6", "2 of 3", each with a sentence of explanation, then a "Learn about our impact" button.
5. "Featured in" row: WWD, Healthline, Forbes, The Wall Street Journal, Esquire.
6. Dark section "The four pillars of chronic disease": horizontal cards, each with a glowing orb image, a large number or percentage, and a one-sentence explanation (Heart disease, Cancer risk, Metabolic dysfunction, Neurodegenerative disease).
7. "The most comprehensive health assessment": a list of 22 named tests, each with a one-line explanation, then "Up to 30+ Assessments".
8. "A private retreat built around your health": two clinic cards (New York City, San Francisco Bay Area).
9. "Membership options designed to fit your goals": Core and Black side by side, each with an itemised list.
10. "World-class care doesn't end at Biograph": a logo grid of academic medical centres (Cedars-Sinai, UCLA, UCSF, Stanford Medicine, Harvard Medical School, Baylor, Emory, UT Southwestern, NYU and others).
11. "Trusted by industry leaders": a wall of ten named testimonials styled like social posts, with name, role and platform icon.
12. FAQ accordion with five questions.
13. Full-bleed closing photo with "Live healthier for longer" and a button.
14. Footer: four link columns, trademark notice, legal links.

**Imagery [V]:** a dark, photographic, cinematic register for the hero and closing CTA; saturated, neon-lit studio imagery for the three process cards; abstract glowing orbs for the disease pillars; real people in photographs of testimonial authors. Hero image rendered at 1440×900 from a 1440×822 file, `object-fit: cover`.

## 4. Art-direction analysis

- **[V]** The page alternates dark photographic fields (hero, pillars, closing CTA) with white or `#F9F9F9` text-led fields. Each white field has one centred title, one sentence and one button.
- **[I]** The first impression is a luxury-architecture one: a lit building at night, a single line of large type placed at the lower left, three tiny facts at the lower right. It borrows the visual language of premium hospitality and design, not hospitals.
- **[I]** The three-step cards use unusually saturated colour (pink and blue light, orange sunset) inside an otherwise neutral page. This makes the process feel experiential. The colour comes from the photographs, not from the UI.
- **[V]** Type is a single large grotesque with no bold anywhere in headings, set tight (−1 % to −2 % tracking). Everything else is small (12–16 px). The gap between 52–68 px headings and 16 px body creates strong hierarchy with very few styles.
- **[I]** The grey body text (`#686873`) at 16 px on white is lower contrast than the ink colour; it signals "supporting" information, but it is a legibility trade-off.
- **[I]** The page reuses one section pattern (small-caps label → large title → one sentence → one button) many times, which makes a very long page (13,571 px) easy to scan.
- **[V]** The testimonials section deliberately imitates social-media posts (name, role, platform icon). **[I]** This signals real, attributable people and is cheaper to read than video.

## 5. Copywriting analysis

Verified copy (`home_desktop.json`, `memberships_desktop.json`):
- H1: "Act now, live longer." Sub: "In a single day, we collect comprehensive health data to uncover hidden risks and deliver personalized insights to optimize your long-term health."
- Method: "This isn't an annual physical. It's the most complete health evaluation available, with 30+ advanced diagnostics completed in a single day."
- Review: "Our team translates your results into a detailed risk profile, which you'll review 1:1 with a Biograph doctor a few weeks after your visit."
- Ongoing: "Your plan combines MD guidance, expert support, and repeat assessments to track progress, identify risks, and improve your health over time."
- Problem frame: "These four disease categories account for the majority of preventable illness and premature death, yet they often develop silently for years."
- Tier copy: "Your comprehensive baseline assessment" (Core) vs "Advanced diagnostics with year-round oversight" (Black), each with an "Ideal for those who want:" list.
- Urgent findings FAQ: "If any concerning findings are detected, one of Biograph's doctors will reach out to you right away…"

Analysis:
- **[I] Awareness stage (Schwartz):** the headline assumes a problem-aware but solution-unaware visitor ("Act now"). The disease pillars then create urgency using population statistics (e.g. "Nº1 Heart disease… every 40 seconds in the U.S.").
- **[I] Offer construction (Hormozi lens):** the offer is built as a stack of named deliverables (22 tests, a risk report, a physician review, nutrition and exercise consults, a year-end check-in), with a price anchor visible before enquiry. The "Core" and "Black" tiers use a good-better structure.
- **[I] Differentiation (Dunford):** "This isn't an annual physical" and the FAQ answer to "How is Biograph different from a regular doctor or a concierge medical practice?" position against the existing alternative, and make clear it complements the PCP rather than replacing them.
- **[V] Concrete claims:** many numbers appear (30+ assessments, 6 clinical touchpoints, 20+ in Core, $7,500). Some are **company-reported outcomes with no method shown on the page**: "96 % of returning members report measurable progress", "1 in 6 members discover urgent findings", "2 of 3 patients that received cardiac and brain imaging showed signs of vascular issues not seen on blood results". The page does not state denominators, time frames or how "measurable progress" is defined. I treat these as marketing claims, not evidence of clinical effectiveness.
- **[V] Proof types, in order of appearance:** one named testimonial → three statistics → press logos → clinical-partner logos → ten more testimonials from named founders and executives → FAQ.
- **[V] Objection handling:** the FAQ answers: how is this different from my doctor; I feel healthy; what if something concerning is found; am I too young; who leads the medical team. This addresses the fear of being told something frightening without support.
- **[V] Voice:** confident, short declaratives, second person, nearly no hedging in the marketing copy ("the most comprehensive health assessment", "the most advanced approach"). Superlatives are unqualified. **[I]** This works for a product brand but would be inappropriate for a clinician making individual claims.
- **[V] CTA wording:** "Join Biograph" (primary, repeated), "Learn more", "Learn about our impact", "Compare memberships", "Discover Core / Discover Black". All primary buttons are action-oriented but low-detail.

## 6. Conversion journey and offer architecture

**Observed path [V]:** hero "Join Biograph" → `https://members.biograph.com/get-started` (a separate member-app domain, not visited). Alternative paths: "Learn more" → `/how-biograph-works`; nav → `/memberships` → "Join Biograph" or "Compare memberships" (`/memberships/compare`).
- **[V]** The visitor sees: what happens (3 steps), what is tested (22 named tests), who reviews it (physician 1:1), what it costs (Core, first year), what the clinic looks like, what happens if something is found, who the team is (FAQ link).
- **[V]** Memberships page also lists a "Your Core Journey" sequence: Pre-Visit Call → Biograph Visit → Comprehensive Results Review → Initial Exercise & Nutrition Consultation → Year-End Check-In.
- **[I]** Friction a visitor may face: the page is very long before the first price (the homepage shows tiers but the price appears on `/memberships`); the main CTA goes to a different domain, which could break the visual continuity; the Black price was not found in captured text.
- **[U]** The sign-up flow, what information it asks for, and whether payment is taken upfront were not inspected.

## 7. Commercial or experimental evidence

- **Not yet researched** beyond what the page says. The uploaded dossier states that Framer's case study names Metalab and reports a "2.3× improvement in mobile performance". I have not fetched it, so this is **[U]**. Note that page-load performance is not conversion.
- No third-party funding, revenue, membership counts or A/B test results have been collected. The statistics on the page are company-reported (§5).

## 8. Distinctive mechanisms worth investigating further

1. **Journey made visible:** a numbered three-step process directly after the hero, then a five-stage "journey" list on the membership page.
2. **Price shown with scope:** "$7,500 for the first year" next to "20+ Assessments" and "6 Clinical Touchpoints".
3. **Dashboard mock-up** in the process section: a fictional "Welcome back, John — Here's an overview of your health" panel with risk labels (e.g. "Increased Risk") is used to show the deliverable.
4. **Urgent-findings protocol** stated in the FAQ and a "1 in 6" claim in the hero: the site names the frightening case instead of hiding it.
5. **Stat cells with large numerals** (96 %, 1 in 6, 2 of 3) in a bordered three-column row.
6. **Institutional proof from partners** (academic medical centres) rather than from Biograph's own staff.
7. **Social-post-style testimonials** from recognisable founders.
8. **Restraint in type:** one grotesque, all weight 400, tight tracking.

## 9. Transferable principles for BetterHealth

(All **[H]**; none shown to raise conversion.)
- Show the process as three to five numbered steps right after the opening, using photographs or a mock-up of the actual deliverable (here, a formulation or care-plan summary, with fictional data and a clear "example" label).
- State what a first engagement includes, in what time, and what it costs, in one place.
- Name the hard case ("what if you find something serious") and say exactly who calls and how fast.
- Say plainly how the practice relates to the patient's existing doctors.
- Use one typeface family with generous size contrast and no bold headings if the goal is quiet confidence.
- Use a repeatable section pattern (label → title → sentence → button) to keep a long page scannable.

## 10. Limitations, open questions, misapplication risks

- **Limits:** no REA run, no hover states, accordion not opened, sign-up flow not visited, `/contact` returned 502, Black tier price and compare page not read, case study not fetched, 5 FAQ answers read only partly.
- **Open questions:** What does the sign-up ask for? What are the statistics based on? How does the page perform on conversion? Is the sun-set photography licensed or commissioned?
- **Misapplication risks for BetterHealth:**
  - Biograph sells a standardised, equipment-heavy product to a mass-premium market with venture-scale marketing. BetterHealth is a small, physician-led practice; its differentiator is judgment, not an inventory of 22 tests.
  - Unqualified superlatives ("most comprehensive", "most advanced") and unreferenced percentages would be hard to defend for a clinician and may breach medical advertising rules.
  - Celebrity or executive testimonials are a form of proof BetterHealth cannot use for confidentiality and professional-conduct reasons.
  - Fear-based statistics ("someone has a heart attack every 40 seconds") may be inappropriate for patients with anxiety-related conditions.
  - Cinematic night-time imagery signals a facility, not a relationship with a clinician.
