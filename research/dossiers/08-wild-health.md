# 08 · Wild Health — https://www.wildhealth.com

**Group B · Precision medicine, individualisation, high-value membership, clinical service packaging**
**Captured:** 2026-10-30 · Chromium (Playwright) 1440×900 and 390×844 · REA not yet run
**Evidence folder:** `../evidence/08-wildhealth/`

Labels: **[V]** Verified · **[I]** Interpretation · **[H]** Hypothesis · **[U]** Unverified.

Pages captured (all 200): `/` (page title "Wild Health | Premium") · `/team` · `/membership`.
Not captured: `/what-to-expect`, the application form (HubSpot, external), the Typeform consult booking, the comparison document linked as "HERE" (Google Drive), podcast, blog, FAQ page.

---

## 1. Business model, customer, commercial context

- **[V]** "Concierge Precision Medicine to Maximize Health Span" (H1). A membership practice combining genetic and biomarker testing, physician visits and coaching. The captured pages sell a **Premium** concierge membership in two tiers: **Peak, "$25,000 annually"**, and **Elite, "Inquire for pricing & availability"** (`home_desktop.json`, `membership_desktop.json`).
- **[V]** Peak lists 11 inclusions, among them Comprehensive Genetic Analysis, Unlimited Physician Visits, Executive Care Coordination, a "Diamond Lab Panel (200 biomarkers)", Unlimited Follow-Up Labs, Unlimited Health Coaching Sessions, 2 × Advanced Testing Options, a Biometric Tracking Device and member-exclusive events. Elite adds "Direct Access to Concierge Doctor", "Direct Access to Care Team" and "Unlimited Advanced Testing & Imaging".
- **[V]** A second, lower-priced offer exists: the banner on `/team` reads "NEW: Discover concierge medicine reimagined - explore Wild Health Premium. **Now accepting most major insurers in your state. Join at a lower price!**" (`team_desktop.json`). The captured homepage is specifically the Premium page.
- **[V]** Team page names ten staff: four physicians, two health coaches, a registered dietitian, two care coordinators, an operations manager. Founder: "Dr. Matt Dawson, Wild Health Founder" appears in a video on the homepage.
- **[V]** The site runs on Webflow (a `webflow-icons` font is loaded; the CTAs go to HubSpot and Typeform forms).
- **[I]** The buyer is an executive or high earner who wants a doctor, a data set and a coach in one paid relationship. The site's job is to justify a $25,000 annual fee and to turn interest into an application.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/home_desktop_viewport.png` |
| Homepage full page (7,546 px) | `screens/home_desktop_full.jpg` |
| Homepage mobile (10,119 px) | `screens/home_mobile_full.jpg` |
| Membership page | `screens/membership_desktop_full.jpg` |
| Team page | `screens/team_desktop_full.jpg` |

## 3. Measured visual specifications

From `data/home_desktop.json`.

**Typefaces loaded [V]:** **Poppins** (400, 500, 700; headings), **Lato** (400, 700, 400 italic; body), Be Vietnam Pro 400.

| Role | Face | Size / line-height |
|---|---|---|
| H1 | Poppins 500 | 56 px / 67.2 px (1.2) |
| H2 section titles | Poppins 500 | 56 px / 72.8 px (1.3) |
| H3 large (results, team) | Poppins 500 | 56 px / 67.2 px; closing 48 px / 57.6 px |
| Tier names | Poppins 500 | 40 px / 40 px, letter-spacing 0.8 px |
| Stat numerals | Poppins 500 | 32 px / 44.8 px |
| Stat labels | Poppins 500 | 24 px / 33.6 px |
| Feature titles | Poppins 700 | 20 px / 30 px |
| Body | Lato 400 | 16 px / 22.4 px; lead 18 px / 30.6 px; long text 16 px / 27.2 px |
| Buttons | Poppins 500 | 14 px |

**Mobile [V]:** H1 38.4 px, H2 38 px, H3 30 px.
**Colour [V]:** white and 90 % white text on a very dark navy `#08151F` page; `#03293B` deep teal (button text, body ink on light areas); `#12567C` blue; **`#B2D7C7` mint** (every filled button, 50 px radius, padding 12 × 28 px). The page is dark throughout; the hero uses a dark marbled texture.
**Layout [V]:** `max-width` 1280, 1248, 992, 960, 800, 886 px. Section heights at 1440 px: hero 970 · tiers 1,293 · pull-quote 302 · tests 1,232 · results 611 · team 560 · testimonials 480 · video 415 · closing 201 · FAQ 704; page 7,546 px.
**Components [V, screenshot]:**
- Header: wordmark "wild health" (lowercase serif), links "Memberships", "What to Expect", then "Sign In" and an outlined pill "Apply for Access".
- Hero: centred H1, one paragraph, three columns separated by thin vertical rules (*Personalized*, *Proven*, *Premium*) each with an icon and a two-line explanation, then a mint button.
- **Two tier cards** side by side on dark panels: Peak (price, one-line promise, button, ruled list of 11 inclusions) and Elite (price by enquiry, button, accordion items).
- Pull quote with round headshot and attribution.
- **Six category cards** (Baseline, Early Cancer Detection, Heart Health, Sleep & Recovery, Nutrition, Performance), each a list of tests with small line icons.
- **Three result rings** with percentages (69 %, 47 %, 58 %), arrows and a short sentence.
- Testimonials in large quotation marks; a founder video with a custom player; FAQ accordion; closing H3 "Commit to achieving your best health today." with button.
- Footer lists email, **phone and fax** numbers.

## 4. Art-direction analysis

- **[V]** A single dark theme, one accent (mint), and Poppins for all headings give the page a technology-product look; there is no serif, no photography of rooms or places in the captured viewport, and the one large background is an abstract dark texture.
- **[I]** The dark navy with mint reads as "clinical technology / biohacking" and suits a data-led offer. It reads cooler and more generic than the editorial sites in Group A.
- **[I]** The tier cards are laid out like a software pricing table: two columns, a price, a button, a checklist. This pattern makes the offer instantly comparable, at the cost of making the practice look like a product.
- **[I]** The results rings borrow the style of fitness apps (circular progress with arrows); they signal measurement before the reader reads any caption.
- **[V]** The page contains very little human imagery in the first screens; faces appear in small round testimonial avatars and in the video.

## 5. Copywriting analysis

Verified copy:
- H1: "Concierge Precision Medicine to **Extend Longevity / Elevate Performance / Sharpen Mental Acuity / Maximize Health Span**" (the last words rotate).
- "Our patients see real, measurable results—from increased energy to the reversal of chronic conditions—all backed by clinical research and a commitment to ongoing innovation."
- "Personalized / Proven / Premium": one-sentence promises each.
- Results block, headed "**Clinically Proven Results**": "*69%* Reduction of Inflammation — Patients at risk of cardiovascular disease saw a 69% reduction in C-Reactive Protein (CRP)…"; "*47%* Improvement of Diabetic Markers — Patients at risk for diabetes saw a 47% improvement of Hemoglobin A1C…"; "*58%* Reduced Risk of Cardiovascular Disease — Patients at risk for cardiovascular disease saw a 58% reduction in Low-Density Lipoprotein (LDL-P)…".
- Membership page "Top Member Goals": Increase Energy; Improve Cognitive Function; Extend Longevity; Reduce Inflammation; **Prevent or Reverse Disease**; Decrease Insulin Resistance; Improve Chronic Conditions; Body Recomposition; Improve Physical Fitness. "Health Care, Not Sick Care".
- FAQ: "Our Premium program is **the most comprehensive and effective concierge medical service on the market**."

Analysis:
- **[V] What the results block does and does not state:** each figure is a change in a **blood biomarker** (CRP, HbA1c, LDL-P). The page gives **no number of patients, time period, comparison group, baseline values, or source** in the captured text. The third card's headline says "Reduced Risk of Cardiovascular Disease" while its sentence describes an LDL-P reduction. The block is headed "Clinically Proven Results". **[I]** A reader may take the percentages as outcomes in a controlled study; the page does not say that they are.
- **[V] Outcome promises:** "reversal of chronic conditions" and "Prevent or Reverse Disease" appear as general claims without qualification.
- **[I] Offer packaging (Hormozi lens):** the offer is built as a list of unlimited items ("Unlimited Physician Visits", "Unlimited Follow-Up Labs", "Unlimited Health Coaching Sessions") to make the price feel like a bundle with no usage anxiety. The top tier withholds the price, which can signal exclusivity and also qualifies by enquiry.
- **[V] Aspirational vocabulary:** longevity, performance, mental acuity, health span, maximum potential, "personally and professionally", "white-glove". The first sentence on the page is about the outcome, not about the problem.
- **[V] Proof:** a quote from a named biohacker-author who is also a member; testimonials from named executives (e.g. "Senior Partner, RHR International"; "CEO, Anvil and Executive Chairman, Hanu"); an anonymous "Melissa, Doctor, Wild Health Member for 3 Years"; the founder's video. Clinical staff are named on `/team`.
- **[V] Voice:** confident, brand-led, with imperatives ("Commit to achieving your best health today.").
- **[V] CTA wording:** "Apply for Access", "Inquire About Membership", "Apply for Membership", "Book a Premium Consult", "Meet Your Health Team", "Apply For Premium". The verb "apply" frames the purchase as selection.

## 6. Conversion journey and offer architecture

**Observed path [V]:** hero button "Inquire About Membership" and header "Apply for Access" → a HubSpot form at `u297m.share.hsforms.com` (external, not opened). Tier buttons "Apply for Membership" → same form. A "Book a Premium Consult" button → a Typeform. Contact: `premium@wildhealth.com`, `support@wildhealth.com`, a phone and a fax number.
- **[V]** The visitor sees: the price of Peak, the inclusions, the test list by category, the clinical team, FAQs including "Do you have physicians on-staff?" ("Yes – we have a full staff of board-certified physicians… licensed to service patients in all 50 states.") and "Can I upgrade my membership?".
- **[V]** The Elite price is withheld; the FAQ "How does your premium program compare to similar offerings?" links a comparison document on Google Drive.
- **[I]** Friction: all CTAs lead to external forms, so the visitor leaves the site's visual identity; the effect on conversion is unknown. Mid-journey, the visitor must decide between two tiers with overlapping lists. The insurance-accepting lower-priced offer is mentioned only on the `/team` banner in these captures.
- **[U]** What the HubSpot form asks and what happens after "applying" (screening, call, payment) were not inspected.

## 7. Commercial or experimental evidence

- **Not yet researched.** No member counts, revenue, funding or experiments collected. The results block cannot be used as evidence of effectiveness for the reasons in §5.

## 8. Distinctive mechanisms worth investigating further

1. **Two-tier price table with the top tier unpriced.**
2. **"Unlimited" as the organising word** in the inclusion lists.
3. **Application framing** ("Apply for Access/Membership") for a paid service.
4. **Test inventory grouped by goal** (Early Cancer Detection, Heart Health, Sleep & Recovery, Nutrition, Performance).
5. **Three-ring results display** with percentages above one-sentence captions.
6. **Founder video** at the end of the proof section.
7. **Rotating H1 outcome words** (longevity / performance / mental acuity / health span).
8. **Named clinical team page** with roles, tied to an FAQ on staff credentials.

## 9. Transferable principles for BetterHealth

(All **[H]**.)
- State what a membership or care package includes as a plain checklist and say what is limited and what is not.
- If any outcome figure is shown, give: how many patients, over what period, with what baseline, measured how, and by whom. Present clinical outcomes (symptoms, function) and label biomarker changes as biomarker changes.
- Group the clinical offering by the patient's goal or concern, not by the equipment.
- Put the treating clinicians on a named team page and answer the "are they board-certified, where are they licensed" question in the FAQ.
- Consider application or screening language only if the practice truly selects patients; otherwise it overpromises exclusivity.
- Keep the enquiry in the site's own design so the visitor does not land on an unrelated form.

## 10. Limitations, open questions, misapplication risks

- **Limits:** no REA run; external forms and the comparison document not opened; hero rotation, accordions, video and hover states not examined; `/what-to-expect` and the lower-price insurance offer not captured; dark-theme contrast not measured.
- **Open questions:** What do the results figures come from? What does the application ask? What does the insurance-accepting offer include? How are the three rings animated?
- **Misapplication risks for BetterHealth:**
  - A $25,000 concierge model and "unlimited" access are not feasible for a small practice with limited physician time; copying them promises availability BetterHealth cannot deliver.
  - Percent changes in biomarkers headed "Clinically Proven Results", without sample or method, and "reverse disease" claims would not be defensible for a clinician; psychiatric outcomes also lack the simple biomarkers used here.
  - The software-style pricing table with a checklist makes care look like a commodity, which can undercut the message that the physician's reasoning is the service.
  - "Executive" and "performance" language may attract the wrong expectations for a practice treating clinical conditions.
  - Phone-and-fax contact details signal a conventional medical office; they show the site is not only a marketing page, which is a trust cue, but it is not a model for confidentiality.
