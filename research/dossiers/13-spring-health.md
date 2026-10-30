# 13 · Spring Health — https://www.springhealth.com

**Group C · Evidence-driven mental-health communication, outcomes, corporate buyers, credibility, translating complex services into a clear offer**
**Captured:** 2026-10-30 · Chromium (Playwright) 1440×900 and 390×844 · REA 6.8.0 run on the homepage only (passive; network/console empty, third-party origins filtered; see `../evidence/rea-summary.md` and `../evidence/<site>/rea/`)
**Evidence folder:** `../evidence/13-springhealth/`

Labels: **[V]** Verified · **[I]** Interpretation · **[H]** Hypothesis · **[U]** Unverified.

Pages captured (all 200): `/` · `/individuals/how-it-works` · `/what-we-do/organizational-support` · `/solutions/for-health-plans` · `/solutions/for-brokers-consultants` · `/case-studies`.
Not captured: the sign-up flow at `care.springhealth.com/register/unified` (separate app domain), `/demo`, therapy, medication-support and coaching pages, "Our methodology", "Our impact" pages, individual case studies.
**Note on framing:** the master prompt describes Spring Health's corporate buyers. In these captures the **homepage is addressed to individuals** ("Find your therapist. Keep your progress."), and the employer message sits in one band and in a separate "For Businesses" section.

---

## 1. Business model, customer, commercial context

- **[V]** Mental-health care delivered through employers and health plans: "Employers and health plans make Spring Health available so members can access personalized mental health care through one connected platform." Services: therapy, coaching, medication management, self-guided tools, specialty programs, crisis support (FAQ, `home_desktop.json`).
- **[V]** Payment routes: "Access to Spring Health is available to individuals covered by participating insurance plans, employers offering Spring Health as a benefit, and those who choose to enroll in our self-pay options." Homepage strip: "OVER 170 MILLION PEOPLE COVERED · Hundreds of insurance plans · Thousands of benefit plans · As low as $0 per session".
- **[V]** Customers named in the FAQ: "Highmark, Target, The Coca-Cola Company, BlackRock, Microsoft, Pfizer, and Wawa". The FAQ also says "More than 170 million people worldwide have access" while the hero says "covered"; the two words are used for the same figure.
- **[V]** The company describes itself as "a global mental health company built on one AI-native platform". "Guide, Spring Health's AI, supports members throughout their mental health journey."
- **[V]** The site is built on Webflow (generator meta "Webflow").
- **[I]** Two buyers are served by one site: the patient (who needs to know it is covered and easy) and the employer or plan (who needs to know it is measurable and cost-effective). The product itself is a managed network and matching platform.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/home_desktop_viewport.png` |
| Homepage full page (6,672 px) | `screens/home_desktop_full.jpg` |
| Homepage mobile (5,143 px) | `screens/home_mobile_full.jpg` |
| How it works (individuals) | `screens/individuals-how-it-works_desktop_full.jpg` |
| Case studies | `screens/case-studies_desktop_full.jpg` |
| Organizational support | `screens/what-we-do-organizational-support_desktop_full.jpg` |

## 3. Measured visual specifications

From `data/home_desktop.json`.

**Typeface [V]:** one family, **Muoto 205 Tf** (400 and 500), for everything.

| Role | Weight | Size / line-height | Colour |
|---|---|---|---|
| H1 "Find your therapist. Keep your progress." | 400 | 54.4 px / 54.4 px (1.0) | white; second sentence in bright green over the hero photo |
| H2 section titles | 400 | 49.9 px / 54.9 px (1.1); FAQ 52 px / 57.2 px | `#01382E` deep green |
| H3 card titles | 500 | 26 px / 32.5 px | `#007055` green |
| Body | 400 | 18 px / 27 px | `#504F4F` or `#5F5E5E` |
| Lead / sub | 400 | 21.2 px / 27 px | |
| Small | 400 | 14 px / 27 px | `#150C06` |
| Buttons | 500 | 16.6 px | |

**Mobile [V]:** H1 28 px; H2 25 px.
**Colour [V]:** `#150C06` near-black brown (253 uses) · `#01382E` deep green (headings; the dark employer band) · `#007055` mid green · **`#8DFF9D` mint green** (all primary buttons; text on them `#01382E`) · `#504F4F` / `#5F5E5E` greys · off-white cream page sections.
**Layout [V]:** `max-width` 1800 px (16 uses), 1200 and 1120 px for text. Section heights at 1440 px: hero 791 · care types 969 · coverage 1,217 · outcomes 1,355 · employer band 589 · FAQ 862; page 6,672 px. Button radius 8 px; padding 14 × 30 px (large), 10 × 16 px (header).
**Components [V, screenshot]:**
- Header: logo, "For Individuals / For Businesses / Resources / About", then "Request a demo", "Log in" and a mint "Get started".
- Hero: a photograph of a parent and toddler at a kitchen counter with a dark overlay; the two-colour H1; a one-line description; a mint button "Find your therapist"; a three-line stat list ("OVER 170 MILLION PEOPLE COVERED").
- Three white cards (Therapy, Self-Guided Care, Coaching), each with a short description and a **product screenshot** (symptom chips such as Anxiety, Depression, Burnout; a chat interface "Welcome back, Alex"; a goals picker).
- A **Venn diagram** of two pastel circles (blue = insurers: Aetna, UnitedHealthcare, BCBS, Cigna, Anthem, Point32Health, Carelon, Optum, Harvard Pilgrim; green = employers: Microsoft, Wawa, Duolingo, Pfizer, The Coca-Cola Company, General Mills, BlackRock and others) with the Spring Health logo in the overlap, and a "Check your coverage" button below ("It takes 10 seconds").
- An outcome block: a green ring "**92 %** Feel real clinical improvements" and "**4.8** ★★★★★ Average therapy session ratings", followed by a row of member quotes with dates and photographs.
- A dark-green employer band "Looking to partner with Spring Health for your organization?" with "Request a demo" and an outlined "Learn More".
- A four-question FAQ accordion; a large multi-column footer.

**Imagery [V]:** warm, candid, domestic photographs (parent and child in a kitchen; a person with a hand on their forehead) and product screenshots. No clinicians appear in the first screens.

## 4. Art-direction analysis

- **[V]** Single typeface, a deep green plus one neon-mint action colour, rounded 8 px buttons and soft cards on cream.
- **[I]** The mint buttons are the only high-saturation element on the page, so the action is always the brightest thing in view.
- **[I]** The product screenshots inside cards make an intangible service (therapy matching, AI support, coaching) look like a concrete product the reader can picture using.
- **[I]** The Venn diagram turns a complicated payment fact (insurance and employer benefits, which change) into one image; the overlap holds the brand.
- **[V]** At 28 px on mobile, the H1 is half the desktop size, which keeps a long two-sentence headline on a few lines.
- **[I]** The page signals "healthcare technology" more than "clinic": no clinician faces, interface screenshots, large corporate logo walls.

## 5. Copywriting analysis

Verified copy:
- H1: "Find your therapist. Keep your progress." Sub: "Therapy, coaching, and wellness tools for wherever life takes you."
- "Care that adapts to your needs" — *Therapy:* "Support through everyday challenges, navigating life changes, managing symptoms of anxiety or depression, and more." *Self-Guided Care:* "Hundreds of self-paced activities to manage stress and build healthy habits and access to safe AI support." *Coaching:* "One-on-one coaching for the goals you're already working toward: stress, habits, career."
- "Care that transitions with your coverage — Insurance and employer benefits change. Your care experience won't have to."
- "Care that makes a difference — Feel real clinical improvements — Average therapy session ratings" (92 % and 4.8 in the graphics).
- Member quotes: "…a safe space to be honest, to feel, and to heal. My therapist listens, truly listens in a way I have never experienced." "I have been struggling with the idea of therapy. It has been incredibly hard to find a therapist that I felt I could be candid with."
- How it works: "Step 1: Check your coverage — Step 2: Tell us about you: Take 3–5 minutes to tell us what's going on. You'll receive a personalized care plan — Step 3: Review your matches: See therapists matched to you based on clinical specialty, real outcomes, and what matters to you — Step 4: Schedule your visit… Appointments are often available as soon as tomorrow — Step 5: Start care." Stats: "40k+ vetted providers · $0 to start · Appointments within 1 day".
- Case-study metrics (employer side): "1400% increase in engagement compared to their traditional EAP", "$283 per member per month in health plan savings" (Hearst).

Analysis:
- **[I] Awareness stage:** the hero speaks to people who already want therapy and need to find a person ("Find your therapist"). The second sentence ("Keep your progress") addresses a known frustration: starting again with each new provider or plan.
- **[I] Differentiation (Dunford):** the unique claim is continuity across coverage changes; the Venn diagram is the visual proof.
- **[V] The outcome numbers:** "92 % feel real clinical improvements" and "4.8 average therapy session ratings" are shown as large figures with a ring and stars. The captured page text contains **no sample size, time frame, instrument (such as PHQ-9 or GAD-7), definition of "improvement" or source**; I found no footnote in the captured text. **[U]** The "Our impact" and methodology pages, which may hold the method, were not captured. "Real outcomes" is also used as a matching criterion ("matched… based on clinical specialty, real outcomes").
- **[V] Employer metrics** ("1400 % increase in engagement", "$283 per member per month in savings") are customer-case claims on a separate page; the captured excerpt has no method note.
- **[V] Plain vocabulary:** the individual pages avoid clinical jargon and describe actions: *check, tell us, review, schedule, start*. The FAQ and the business pages use more corporate language ("workforce mental health", "de-identified reporting on engagement, outcomes, and impact").
- **[V] Objection handling:** cost ("As low as $0 per session", "$0 to start", "First 6+ sessions covered by your employer*"); wait time ("Appointments within 1 day"); fear of the first step ("Take 3–5 minutes to tell us what's going on"); lock-in to a provider ("Keep your progress").
- **[V] Safety statements:** "access to safe AI support"; "Guide, Spring Health's AI". Crisis support is listed as a service in the FAQ.
- **[V] CTA wording:** four mint buttons ("Find your therapist", "Get care today", "Check your coverage", "Get started") all go to the same registration URL `care.springhealth.com/register/unified`; "Request a demo" is the business action.

## 6. Conversion journey and offer architecture

**Observed path [V]:** any mint button → `care.springhealth.com/register/unified` (not visited). The how-it-works page sets out five steps beginning with a coverage check (3–5 minute assessment, match list, scheduling).
- **[V]** The page places the price question first: coverage check before any clinical question, and "It takes 10 seconds" under the first button.
- **[V]** The employer path is separate ("For Businesses", "Request a demo"), and the footer adds health plan, broker/consultant, channel partner and provider ("Apply here") routes.
- **[I]** Friction is low on the visible side (no price negotiation, no call to book). The main uncertainty a visitor may have is whether their plan is covered, which the page answers with a tool.
- **[U]** The registration steps and what the digital assessment asks were not inspected.

## 7. Commercial or experimental evidence

- **Not yet researched.** Funding, customer counts, outcomes publications and any independent evaluation have not been collected. The 92 %, 4.8, 170 million and employer figures are company-reported.

## 8. Distinctive mechanisms worth investigating further

1. **Coverage as the first interaction** ("Check your coverage — it takes 10 seconds").
2. **One diagram for a complicated access model** (insurers vs employers, with the brand in the overlap).
3. **Product screenshots** embedded in service cards.
4. **A single outcome ring + a star rating** as the proof block, followed by dated member quotes.
5. **A five-step "how it works"** ending with "appointments often as soon as tomorrow".
6. **Two-colour H1** (second sentence in green).
7. **A single mint action colour** and one destination for four different buttons.
8. **Separate routes for buyers** (individual, employer, health plan, broker, provider) in the header and footer.

## 9. Transferable principles for BetterHealth

(All **[H]**.)
- Answer the practical question (what it costs, whether it is available for the visitor, how soon the first appointment is) before asking for clinical detail.
- Describe the first steps as five short, plain actions with a time for each ("3–5 minutes", "within X days").
- If an outcome measure is shown, name the instrument (e.g. a validated symptom scale), the number of patients, the period, and what "improved" means; otherwise show a description of how progress is tracked, not a percentage.
- Use dated, first-person patient quotes only with consent and in a form that protects identity; for a small private practice, the practice's own written description of its process may be safer than quotes.
- Use one action colour and keep the action label specific.
- A single explanatory diagram can carry a complex fact (for BetterHealth, perhaps how assessment, treatment and follow-up connect).

## 10. Limitations, open questions, misapplication risks

- **Limits:** REA homepage inspection only; registration and demo flows not visited; "Our impact"/methodology pages not captured; the accordion and the ring animation not examined; the full-page screenshot shows carousel quotes cut at the edges; no hover states; the numbers 92 % and 4.8 were read from the screenshot, not from the DOM text.
- **Open questions:** What defines "clinical improvement"? How many members, over what period? What is the difference between "covered" and "have access" for the 170 million figure? What does the digital assessment ask?
- **Misapplication risks for BetterHealth:**
  - Spring Health's model is an insurance- and employer-funded platform at scale. Insurer logos, "$0 per session", "40k+ providers" and a network-matching flow have no equivalent in a self-pay, physician-led practice.
  - A headline percentage ("92 %") without method would be hard to defend for a clinician, and a psychiatric practice's patients may compare it with their own experience.
  - AI "support" features in mental health raise clinical safety and data-protection questions that a small practice would need to address separately.
  - The page almost never shows a clinician; BetterHealth's value depends on the physician being visible.
  - The corporate customer-logo wall relies on contracts BetterHealth does not have; inventing similar social proof would be misleading.
