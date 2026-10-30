# 04 · Lanserhof — https://lanserhof.com/en

**Group A · Luxury medical hospitality, visual restraint, institutional credibility, diagnostics**
**Captured:** 2026-10-30 · Chromium (Playwright) 1440×900 and 390×844 · REA not yet run
**Evidence folder:** `../evidence/04-lanserhof/` (cookie banner declined with "Reject")

Labels: **[V]** Verified · **[I]** Interpretation · **[H]** Hypothesis · **[U]** Unverified.

Pages captured (all 200): `/en` · `/en/lanserhof-marbella` · `/en/medicine-naturopathy` · `/en/contact` · `/en/chat?prompt=Help me choose a programme.` (the AI assistant, opened from the "Start your journey" button).
Not captured: `/en/booking`, programme pages, individual resort pages other than Marbella, press.
Inner heading styles were measured with an extra Playwright script (not saved in `evidence/`; its results are quoted here and should be re-run into the evidence folder).

---

## 1. Business model, customer, commercial context

- **[V]** Medical wellness resorts ("medical spa") in four places: Lans (Tyrol, Austria), Tegernsee (Bavaria), Sylt (North Sea, Germany), Marbella (Costa del Sol, Spain), selling stays built around programmes (`en_desktop.json`).
- **[V]** The offer is organised as **thirteen focus areas**, including Classic Detox, Longevity Medicine, Weight Regulation, **Stress Resilience**, Deep Sleep, Pre- & Rehabilitation, Immune Regulation, **Brain Health**, Gender-specific Health, Sports Performance, Wellbeing Retreat, Beauty & Aesthetics, Spiritual Energy.
- **[V]** No prices appear on the captured pages. Primary actions are "Book now" (`/booking`), "Contact us" and "Start your journey" (AI assistant).
- **[V]** The brand's own claim is "At the World's Best Medical Spa", and the page lists awards, including "World's Best Medical Spa — International Spa Awards 2025" (see §5).
- **[I]** The buyer is a wealthy leisure or health traveller choosing between destinations and programmes. The relationship is a stay, not ongoing clinical care.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/en_desktop_viewport.png` |
| Homepage full page (6,666 px) | `screens/en_desktop_full.jpg` |
| Homepage mobile (viewport only, see §10) | `screens/en_mobile_viewport.png` |
| Contact | `screens/en-contact_desktop_full.jpg` |
| AI assistant consent screen | `screens/en-chat_desktop_viewport.png` |
| Medicine & naturopathy | `screens/en-medicine-naturopathy_desktop_full.jpg` |

## 3. Measured visual specifications

**Typefaces loaded [V]:** Neue Frutiger World (300, 400, 450, 500, 700) and **Frutiger Serif LT Pro 300 italic**.

The `<h1>`/`<h2>` elements measure 16 px at the wrapper level; the visible type is in child spans. Measured on the spans (Playwright, desktop):

| Role | Face | Size / line-height | Letter-spacing | Style |
|---|---|---|---|---|
| H1 line 1 "Home of" | Frutiger Serif LT Pro 300 | 60 px / 60 px | 3.87 px (0.065 em) | italic, sentence case |
| H1 line 2 "HEALTH & BEAUTY" | Neue Frutiger World | larger line; the "&" is 69 px italic serif uppercase | 2.56 px | uppercase |
| H2 line 1 ("The Ultimate", "World Class", "Thirteen paths.") | Frutiger Serif LT Pro 300 | 36 px / 36 px (1.0) | 2.32 px (0.065 em) | italic |
| H2 line 2 ("HEALTH & BEAUTY EXPERIENCE", "MEDICAL EXPERTISE", "ONE FOCUS.") | Neue Frutiger World 450 | 41.4 px / 41.4 px (1.0) | 1.54 px (0.037 em) | uppercase |
| "Mountains and sea" | Frutiger Serif LT Pro 300 | 48 px / 48 px | 3.10 px | italic |
| Footer column heads | Neue Frutiger World 500 | 14 px / 20 px | 1.12 px (0.08 em) | uppercase |
| Body | Neue Frutiger World 400 | 16 px / 24 px | — | `#1B1D21` |
| Small body | Neue Frutiger World | 14 px / 19.25 px; 12 px / 16 px (`#6E737D`) | — | |

The pattern is a **two-voice headline**: a smaller italic serif line followed by a larger uppercase grotesque line, line-height 1.0, in every H2.
**Mobile [V]:** the same proportions at roughly 50 %: H1 30 px / 34.5 px; H2 25 px / 28.75 px.

**Focus-area list [V]** (links in the "Thirteen paths" section) uses a graded scale: the active item 28 px `#1B1D21`; the next ones 22 px `#44484F`; then 18 px `#6E737D`; the rest 16 px `#9EA3AD`; all weight 300, letter-spacing 0.2 px. The screenshot (`en_desktop_full.jpg`) shows a vertical selector in which the active item is dark and large and distant items fade out; the description and a "Learn more" button below update with the active item.

**Colour [V]:** `#1B1D21` ink · `#F4F4F5` page background · `#E3E5E8` light grey (button fill and dividers; the most frequent computed colour) · `#FAFAFA` text on images · greys `#6E737D`, `#9EA3AD`, `#44484F` · dark button `#26282B`. Text panels have soft pastel gradients (cream, rose, grey) visible in the screenshot; individual values were not extracted.

**Layout [V]:**
- Homepage sections are each exactly **900 px tall** (the capture viewport height): 0, 900, 1,800, 2,700, 3,600, 4,500; the last (questions + footer) is 1,266 px. Page 6,666 px. **[I]** The sections are built as full-viewport slides.
- Each content slide is split: a text panel about 38–40 % of the width and a full-bleed photograph about 60–62 %, alternating sides (text left on slide 2, right on slide 3, left on slide 4, left (narrow) on slide 5). The text panel has a soft-gradient top holding the heading and a lighter lower block holding one paragraph and one pill button.
- The four-resort section is four vertical photo strips of equal width, each with an italic serif place name and an uppercase region line.
- Awards: a horizontal row of laurel-style badges with name, issuer and year, with a slider control.
- A `max-width` of 1280 px is used for the footer container; text columns 377 px, 610 px.

**Components [V]:**
- Header: **three floating pills** over the hero: left "☰ Start your journey ✦" (with a sparkle icon), centre stacked logotype **LAN / SER / HOF** in heavy white capitals, right "Contact us | Book now". Pills are 8 px × 14 px padding, fully rounded (radius computed as 33,554,400 px, i.e. a pill). "Book now" is filled `#E3E5E8` with ink text; "Our medical expertise" is filled `#26282B`.
- Hero: a looping video or rotating images. Two captures show two different hero frames (a woman walking uphill toward a house at `en_desktop_viewport.png`; a massage room at `en_desktop_full.jpg`), so the hero changes over time.
- A scroll-down chevron below the hero text.

**Imagery [V]:** architecture and landscape dominate (timber and glass buildings, spiral staircase, dune grass, mountains), natural light, muted earth tones. People appear small or from behind, and clinicians appear once (a woman and a man seated with a tablet, `en_desktop_full.jpg`, slide "World Class Medical Expertise").

## 4. Art-direction analysis

- **[V]** The page is restrained in colour: grey, cream, one dark pill colour, no accent hue. All colour comes from photographs.
- **[I]** The italic-serif-over-uppercase-sans pairing gives each heading a softer first line and a firmer second line. The serif "Home of / The Ultimate / World Class / Thirteen paths." works as a lead-in; the uppercase line states the subject.
- **[I]** Full-viewport slides with a 40/60 split give each message equal weight and a predictable rhythm; there is no dense section anywhere on the homepage.
- **[V]** The pastel gradient panels next to photographs pick up the photograph's colour (peach beside the dune image, rose beside the interior), so the text panel reads as part of the picture, not as a block laid on top.
- **[I]** Showing buildings far more than people is typical of hospitality; it sells place and calm. For a clinical practice it does the opposite of showing who treats you.
- **[V]** The one image with clinicians shows them seated at ease in a lounge, not in white coats at a desk.

## 5. Copywriting analysis

Verified copy (`en_desktop.json`):
- Hero: "Home of Health & Beauty. At the World's Best Medical Spa, we give our guests the most precious gift of all: health, energy and quality of life."
- Concept: "The globally unique Lanserhof concept combines cutting-edge medical science with proven natural healing methods. Healthier, more vital, younger, more beautiful – with individually tailored programs…"
- Choice: "Thirteen paths. One focus. One of them is yours."
- Focus-area descriptions, e.g. *Stress Resilience*: "A medically guided approach to strengthening your stress resilience by addressing both the physiological and psychological effects of stress." *Brain Health*: "Understanding and protecting cognitive health through early detection of neurological risks and targeted preventive strategies." *Longevity Medicine*: "Precision diagnostics and targeted therapies to influence your biological aging."
- Expertise: "Leading medical experts work together across disciplines to understand your health as a whole."
- Awards: "Independent juries and international experts regularly rank the Lanserhof concept as the benchmark in medical wellness."
- Contact: "Our reservation team knows every resort personally and takes the time to find the dates, programme and room that fit your life right now."

Analysis:
- **[I] Awareness stage:** the visitor knows they want a medical-wellness stay; the page's job is to differentiate and to help choose a programme ("One of them is yours").
- **[I] Offer packaging:** thirteen named focus areas turn a broad service into labelled entry points, each with a one-sentence benefit. The reader finds their own situation by name.
- **[V] Concrete vs abstract:** the focus-area sentences are specific about method ("early detection of neurological risks", "medication-free therapies", "GLP-1 treatments where appropriate") but contain no numbers, durations or outcomes. The hero uses superlatives.
- **[V] Substantiation on the page:** the hero claim "World's Best Medical Spa" is matched, further down, by a listed award of that name (International Spa Awards 2025, "Seven Stars Luxury Hospitality & Lifestyle Awards" for the "World's Best Medical Spa" entry in the capture text), along with some twenty other named awards with years. **[U]** Whether those awards are independently judged or paid-entry was not checked.
- **[V] Voice:** polished, benefit-led, warm, with abundant adjectives and sentence fragments in headings. The programme copy is more measured than the hero.
- **[V] CTA wording:** "Start your journey", "Contact us", "Book now", "Our medical expertise", "Learn more". The only CTA that responds to a visitor's uncertainty is "Start your journey", which opens an AI assistant prompt "Help me choose a programme."

## 6. Conversion journey and offer architecture

**Observed path [V]:** hero pills → *Book now* (`/booking`, not captured) · *Contact us* (`/contact`) · *Start your journey* (AI assistant). Mid-page: focus-area selector → programme page ("Learn more"). Closing section: "Questions about your stay?" → Contact us.
- **[V]** The **AI assistant page** states, before any chat: "You are chatting with an AI that answers your questions about Lanserhof and recommends suitable programmes. Using the chat is voluntary. If you do not consent, there is no disadvantage for you; you can also send us your questions via our contact form." Then three trust blocks: "We protect your data — Personal details such as names or email addresses are detected automatically and replaced with placeholders. The AI model never sees your data."; "Processing in Europe only — … pseudonymized and processed exclusively in the EU. We do not store them permanently. When the chat ends, the history is deleted."; "Less is more — We do not need your name or contact details… Information about your health is voluntary: you decide what you tell us." A consent statement follows (`en-chat_desktop.json`).
- **[V]** The contact page lists, for each resort, an address, a phone number and an email, with no form captured.
- **[I]** The visitor can progress without ever being asked for personal data: via browsing, the AI recommender (with minimised data) or a direct phone call.
- **[U]** I did not give consent or send a message in the chat, so its answers and the booking flow were not inspected.

## 7. Commercial or experimental evidence

- **Not yet researched.** No revenue, occupancy or conversion data collected. The awards on the page are the company's own presentation.

## 8. Distinctive mechanisms worth investigating further

1. **One concept, many named entry points** (thirteen focus areas) instead of one long list of treatments.
2. **Graded-scale selector list** where the active focus is large and dark and distant items fade.
3. **Two-voice headlines** (italic serif lead-in + uppercase sans subject).
4. **Full-viewport 40/60 split slides** with gradient text panels tinted by the photograph.
5. **A privacy-first AI assistant:** explicit statement of AI use, voluntary consent, data minimisation, EU processing, deletion at session end, "health information is voluntary".
6. **Floating pill header** with the logo centred and actions in two clusters.
7. **A dense awards strip** as institutional proof.
8. **Reservation team framed as people who "know every resort personally".**

## 9. Transferable principles for BetterHealth

(All **[H]**.)
- Name a small number of "ways in" (for BetterHealth perhaps four to six, e.g. persistent anxiety, burnout, attention, sleep, complex presentations) each with one sentence stating the clinical question addressed, linking to one page.
- If any digital assistant or form is offered, state in plain words what is and is not collected, where it is processed, how long it is kept, and that health information is optional. This is directly relevant for a Swiss medical practice.
- Use a repeatable full-screen slide pattern with one message and one button per screen to keep the homepage short and legible.
- Pair a softer lead-in line with a firmer subject line in headings, if the typeface licence allows a comparable pairing.
- Where proof is mostly third-party recognition, list it with issuer and year, not as logos alone. For BetterHealth the equivalent would be qualifications, society memberships and publications, not awards.

## 10. Limitations, open questions, misapplication risks

- **Limits:**
  - On mobile (390 px) the page scrolls inside `<main>` (scrollHeight 7,195 px, clientHeight 730 px); the document height is only 844 px. The "full-page" mobile screenshot therefore shows a single viewport. Mobile layout below the hero has **not** been captured; it needs a scroll-container capture.
  - The hero video was not examined; no hover, menu or focus-area interaction was captured; the booking flow and AI replies were not tested; no REA run.
  - The heading measurements come from an ad hoc script not yet saved into `evidence/`.
- **Open questions:** What does `/booking` ask? Are prices shown on programme pages? How are the awards chosen? What does the AI recommend, and is it clinically reviewed?
- **Misapplication risks for BetterHealth:**
  - Lanserhof sells a destination; its imagery is architecture and landscape. A physician-led practice that copies this would hide its main asset, the clinician.
  - "Health & Beauty", "younger, more beautiful", "World's Best" and thirteen overlapping offers would read as an anti-ageing/wellness promise, which conflicts with a precision-psychiatry positioning and with Swiss medical-advertising norms.
  - The awards strip is not replicable for a new practice and should not be mimicked with invented badges.
  - A "wheel" selector hides most options at any moment; for a clinical decision, a plain visible list may be clearer. This is untested.
  - An AI recommender for a mental-health practice needs separate clinical-safety and data-protection review before any use.
