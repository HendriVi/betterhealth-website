# 10 · Parsley Health — https://www.parsleyhealth.com

**Group B · Framing of complex or poorly understood symptoms, comprehensive care, membership and insurance**
**Captured:** 2026-10-30 · Chromium (Playwright) 1440×900 and 390×844 · REA 6.8.0 run on the homepage only (passive; network/console empty, third-party origins filtered; see `../evidence/rea-summary.md` and `../evidence/<site>/rea/`)
**Evidence folder:** `../evidence/10-parsley/`

Labels: **[V]** Verified · **[I]** Interpretation · **[H]** Hypothesis · **[U]** Unverified.

Pages captured (all 200): `/` · `/insurance` · `/care` · `/labs` · `/contact` · `/join/care` (sign-up step 1).
Not captured: `/care/conditions` and condition pages, clinician pages, the Parsley Symptom Index page, store, later steps of sign-up.

---

## 1. Business model, customer, commercial context

- **[V]** Clinician-led "functional medicine" practice delivered mainly by telehealth, with a centre in New York (footer address: 126 5th Ave, New York). Meta description: "Find functional medicine doctors for advanced lab testing and holistic healthcare… to treat the root cause of your health issue."
- **[V]** Two offers, shown under "Two ways to get started" (`home_desktop.json`):
  - **Complete Care Membership** (ongoing care): 5 medical visits, 2 functional nutrition coach visits, labs and prescriptions, optional supplements and specialty tests, care-team support. **$150/month or $1,500/year in-network; $275/month self-pay** ($2,750/year). 12-month commitment; "Free 48-hour cancellation"; "Lab testing costs not included in membership fees"; Medicare/Medicaid not accepted (`insurance_desktop.json`).
  - **Clinical Lab Review** ("Lab insights"): a clinician visit to review blood work from the past six months. **$250/visit, self-pay only**, "$250 credit will be applied to Complete Care membership if you sign up post-visit."
- **[V]** Claim: "Parsley Health is the first and only functional medicine provider to accept insurance nationwide. Membership starts at $150/month with in-network coverage… No five-figure program fees, no long wait times."
- **[V]** An announcement bar: "Parsley is in-network nationwide and FSA/HSA eligible. [Verify insurance]". A supplements store exists (a cart drawer text "was added to cart" is in the DOM).
- **[I]** The buyer is a person with long-standing, hard-to-explain symptoms who has not found answers in conventional care, and who wants a doctor-led plan without paying concierge prices.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/home_desktop_viewport.png` |
| Homepage full page (10,757 px) | `screens/home_desktop_full.jpg` |
| Homepage mobile (11,654 px) | `screens/home_mobile_full.jpg` |
| Insurance and pricing | `screens/insurance_desktop_full.jpg` |
| Sign-up step 1 | `screens/join-care_desktop_full.jpg` |
| Care, Labs, Contact | `screens/care_desktop_full.jpg`, `labs_…`, `contact_…` |

## 3. Measured visual specifications

From `data/home_desktop.json`.

**Typefaces loaded [V]:** **Teodor** 300 (light serif; headings), **EuclidCircularB** 300 / 400 / 500 (body and UI).

| Role | Face | Size / line-height | Letter-spacing |
|---|---|---|---|
| H1 | Teodor 300 | 64 px / 71.7 px (1.12) | −1.28 px (−0.02 em) |
| H2 | Teodor 300 | 48 px / 53.8 px (1.12) | −0.96 px (−0.02 em) |
| H3 (offers, 38 / 32 px) | Teodor 300 | 38 px / 41.8 px; 32 px / 36.8 px | −0.01 em |
| Condition card titles | EuclidCircularB 500 | 21 px / 29.4 px | −0.21 px |
| Body | EuclidCircularB 400 | 18 px / 28.8 px; 20 px / 32 px | |
| Eyebrow label | EuclidCircularB 500 | 11 px / 12 px, uppercase | 0.88 px (0.08 em) |
| Buttons | EuclidCircularB 500 | 14–16 px | −0.01 em |

**Mobile [V]:** H1 48 px, H2 36 px, H3 34 px.
**Colour [V]:** `#284849` deep teal (text and dark fills; 893 uses) · `#F8F6F2` warm cream (page) · `#4A786A` green (links, secondary buttons) · `#6FB29F` mint (accents on dark) · `#333333` body copy · `#132D2E` darkest teal (closing CTA heading) · `#FCFBFA`. Pastel gradients (mint to lilac) behind the testimonial.
**Layout [V]:** `max-width` 1440 px (16 uses) and 1480 px; cards 235–279 px wide. Page 10,757 px. Buttons are fully rounded pills (radius 33,554,400 px); padding 8 × 24 (small), 12 × 24, 16 × 32 px.
**Components [V, screenshot]:**
- Announcement bar (mint-tinted) with a "Verify insurance" pill; dark-teal header with five text links and a white "Join now" pill.
- Hero: left-aligned H1 in grey-teal serif over a soft beige gradient, a large cropped portrait of a smiling woman at the right, two buttons (filled "Verify insurance", outlined "Join now"), then a strip of five outlined icon badges (*Insurance accepted · Board-certified clinicians · Advanced lab testing · Nationwide telehealth · HSA/FSA eligible*).
- Alternating text + portrait sections (text left, photograph right).
- A block of eight insurer logos (BlueCross BlueShield, UnitedHealthcare, Anthem, Cigna, Empire, Horizon, Aetna, Florida Blue).
- A dark-teal band with two white offer cards; the Complete Care card shows a five-dot timeline across (*5 medical visits · 2 functional nutrition coach visits · Labs and prescriptions · Supplements (optional) · Specialty tests (optional) · Care team support*).
- A pastel-gradient testimonial with five stars and a large quote.
- A horizontally scrolling set of condition cards with a photograph, a title, a symptom list and a link.
- A comparison table with four columns (Primary Care Provider, Functional Medicine Clinic, Concierge Clinic, Parsley Health) and five rows; an FAQ accordion; a closing section "Ready for a different kind of care?"

**Imagery [V]:** warm, close-cropped portraits of smiling people in natural light, with tones matching the palette (red blouse, cream shirt). The photographs are the only strong colour on an otherwise teal-and-cream page.

## 4. Art-direction analysis

- **[V]** Light serif headings in dark teal on cream, pill buttons, green accents.
- **[I]** The imagery of reassuring, direct-to-camera faces and the plain, benefit-led layout read as consumer health, not luxury. The serif keeps the page from looking like a generic telehealth app.
- **[V]** The insurer-logo block is placed immediately after the first promise; it is the only logo block and is prominent. **[I]** For this audience, "does my insurance cover this?" is a gate question and the layout answers it visually.
- **[I]** The two-card dark band makes the offer the visual centre of the page: it is the only large dark area and the only element with a timeline graphic.
- **[V]** **Palette overlap with BetterHealth's current site.** Parsley's computed colours are `#284849` (deep teal), `#F8F6F2` (cream), `#4A786A` (green), `#6FB29F` (mint). The CSS variables in BetterHealth's current `index.html` are `--deep:#153533`, `--cream:#fffcf4`, `--sage:#738b7f`, `--aqua:#7bbeb2`, `--ink:#0f1f1f`. **[I]** The two schemes are in the same family (dark teal, warm cream, sage, mint). A new BetterHealth identity should not rely on that family alone to differentiate.

## 5. Copywriting analysis

Verified copy:
- H1: "Medical care that uncovers the root cause of your symptoms." Sub: "Work with a board-certified functional medicine clinician and dedicated care team focused on root cause care, so you can feel better and stay well. Now accepting insurance nationwide."
- "Finally, a doctor who asks why — not just what. Proactive care from clinicians who are trained to uncover the root cause of complex conditions. Resolve your symptoms and start feeling like the best version of yourself again."
- Condition framing: "We get to the root of complex and chronic conditions": cards for Gut & Digestive Health; Hormone Health & Balance; Autoimmune & Inflammation; **Unexplained Symptoms** ("Allergic reactions, anxiety, bloating, brain fog, fatigue, headaches, insomnia, joint pain, low mood, skin rashes"); **Mental & Emotional Health** ("Agitation, anxiety, brain fog, changes in appetite or weight, difficulty concentrating, fatigue, feeling hopeless, insomnia, irritability, loss of interest in activities, low mood"); Heart Health; Longevity & Healthspan.
- Proof headline: "**89% of Parsley members improve or eliminate symptoms within a year**" with quote cards from members (first names).
- Clinician credibility: "Board-certified, with advanced functional medicine training · Can prescribe medication when needed, including GLP-1s and hormone therapies · Track your health progress via clinically validated Parsley Symptom Index (PSI)" with a founder quote from Dr. Robin Berzin, MD.
- Comparison: "Get more out of medicine than you ever thought possible" (rows: Finds the root cause; Accepts insurance; Typical cost — Copays / $$$ out of pocket / $$$$ annual fee / **From $150/month**; Dedicated care team; Tracks progress).
- FAQ includes "Does this replace my primary care doctor?" and "Which Parsley program is right for me?"
- Sign-up page: "Let's get your care plan started. We'll match you with a functional medicine clinician licensed in your state."

Analysis:
- **[I] Reframe (Schwartz):** the headline shifts the reader from "what is wrong" to "why": "a doctor who asks why — not just what". This describes the reader's frustration (they were treated for labels) and positions Parsley's method as the answer. It is a direct example of naming an under-served problem: unexplained or multi-system symptoms.
- **[I] Differentiation (Dunford):** the comparison table sets four alternatives against five attributes, so the reader can see the category Parsley claims (root-cause care + insurance + dedicated team). **[V]** The claim "first and only … to accept insurance nationwide" is a unique-attribute statement with no source on the page.
- **[V] Repetition of "root cause":** it appears in the page title, the H1, the sub-headline, the H2 above the conditions and the comparison table. **[I]** This is a single idea repeated, which makes the positioning memorable but also commits the practice to a causal promise.
- **[V] The 89 % claim:** the captured text gives no denominator, definition of "improve", survey method or source; the Parsley Symptom Index is named elsewhere as the tracking tool. **[U]** Whether the 89 % comes from that index was not checked.
- **[V] Concrete vs abstract:** prices, visit counts, 48-hour cancellation, 12-month commitment and insurer names are concrete; "feel like the best version of yourself" is abstract.
- **[V] Testimonials** use first names with an initial ("Sam P.", "Kate M.") and star ratings; no job titles or celebrities. They tell recovery-after-struggle stories ("after 10+ years of struggling").
- **[V] Voice:** warm, plain, second person, short sentences, "Finally,…", em-dash contrasts ("why — not just what").
- **[V] CTA wording:** "Verify insurance" (first button), "Join now", "Check eligibility", "Learn more about insurance", "Review your labs", "See what we treat".

## 6. Conversion journey and offer architecture

**Observed path [V]:** announcement bar or hero "Verify insurance" → `/join/care` step 1 ("Get personalized care… Location → Insurance"): two fields, **email** and **ZIP code**, with the note that the patient "must be physically in your state when you have any telehealth visits"; terms and HIPAA notice acceptance on continue.
- **[V]** A second path is the paid $250 Clinical Lab Review (`/join/labs`), explicitly offered to visitors who are "not ready for Complete Care yet" and credited against the membership.
- **[V]** The **insurance page** states what is and is not covered: Complete Care visits, labs and prescriptions are billed to insurance; "Lab testing costs not included in membership fees"; Medicare/Medicaid not accepted; self-pay prices listed.
- **[I]** The journey asks for the minimum first (email and ZIP), and ties it to a clear reason ("to match you with licensed clinicians in your state"). The lower-commitment $250 first step reduces the risk of a 12-month commitment.
- **[V]** The page lists a 12-month commitment with a 48-hour cancellation.
- **[U]** Steps after ZIP (insurance details, scheduling, payment) were not inspected. The DOM marks the fields "required: false" although labelled with asterisks; actual validation was not tested.

## 7. Commercial or experimental evidence

- **Not yet researched.** No funding, membership counts, outcomes data or experiments collected. The 89 % figure and "first and only" claim are the company's own.

## 8. Distinctive mechanisms worth investigating further

1. **A paid, low-commitment first step with credit toward the full relationship** ($250 lab review, credited to membership).
2. **"Why, not what" reframing** for patients whose symptoms span several systems.
3. **Symptom lists written in patients' words** inside each condition card (including anxiety, brain fog, low mood, difficulty concentrating).
4. **A comparison table against three alternatives**, including concierge care.
5. **Insurer logos** and an eligibility check as the first action.
6. **A two-field start** (email, ZIP) with the reason stated.
7. **A named outcome instrument** (Parsley Symptom Index) as the visible way progress is tracked.
8. **Itemised price terms:** commitment length, cancellation window, what is excluded.
9. **Announcement bar** repeating the main eligibility message on every page.

## 9. Transferable principles for BetterHealth

(All **[H]**.)
- Offer a defined, self-pay first step with a price, a duration and a clear deliverable, and state whether its fee is credited toward ongoing care.
- Write the problem pages in the patient's own symptom words (sleep that does not restore, loss of focus, constant tension, low mood despite doing everything right) and then show the clinical questions the doctor asks.
- If the practice tracks progress with a validated instrument, name it and say what it measures, and report outcomes only with sample, period and method.
- Show a short comparison of care options that is factually checkable and not self-flattering, or skip it.
- Ask for the minimum at first contact and say why each field is needed.
- State commitment length, cancellation terms and exclusions in plain words next to the price.
- Do not rely on teal, cream and sage as the main differentiator (see §4).

## 10. Limitations, open questions, misapplication risks

- **Limits:** REA homepage inspection only; condition pages and clinician pages not captured; sign-up steps after step 1 not completed; the carousel, accordion and comparison-table icons not inspected; mobile layout viewed only in the capture; no hover states.
- **Open questions:** What is the basis of "89 %"? How is the Parsley Symptom Index validated? What does the insurance step ask? How are visit counts handled for patients who need more care?
- **Misapplication risks for BetterHealth:**
  - Parsley's model depends on insurance billing in the US; BetterHealth is self-pay in Switzerland, so the insurer-logo block, "Verify insurance" button and in-network price do not transfer.
  - "Root cause" is a promise of a single underlying explanation. For psychiatric and complex conditions the causes are often multiple and unresolved; the uploaded dossier also warned against universal root-cause claims. Use language such as "work out what is contributing" instead.
  - "Functional medicine" brings its own contested evidence base; I have not assessed it here, and BetterHealth should not adopt the label without a clinical decision.
  - "First and only" and "89 % improve or eliminate symptoms" are unsourced on the page; a physician cannot publish equivalents without data.
  - The condition cards list many symptoms under one practice, which may signal a generalist; BetterHealth needs to stay specific.
  - Teal, cream and sage would make BetterHealth resemble this site (§4).
