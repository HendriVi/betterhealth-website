# 07 · Function Health — https://www.functionhealth.com

**Group B · Membership positioning, diagnostic value communication, pricing, acquisition**
**Captured:** 2026-10-30 · Chromium (Playwright) 1440×900 and 390×844 · REA 6.8.0 run on the homepage only (passive; network/console empty, third-party origins filtered; see `../evidence/rea-summary.md` and `../evidence/<site>/rea/`)
**Evidence folder:** `../evidence/07-function/` (cookie banner "Your Privacy Choices" was not dismissed: it is visible at the lower left of the first viewport)

Labels: **[V]** Verified · **[I]** Interpretation · **[H]** Hypothesis · **[U]** Unverified.

Pages captured (all 200): `/` · `/about` · `/pricing` · `/how-it-works` · `/contact-us`.
Not captured: `/what-we-test`, `/imaging`, `/faq`, the app at `my.functionhealth.com/signup` (separate domain, not visited), testimonial videos.
Note: the filename `07-function` is the site id used in `evidence/`; this dossier file is named `07-function-health.md`.

---

## 1. Business model, customer, commercial context

- **[V]** Consumer lab-testing membership. Offer: "Every year. Starting with 160+ lab tests detecting 1000+ conditions. Just $365 per year—$1 per day." (`home_desktop.json`).
- **[V]** The pricing page: "Test twice a year for just $365", "What could cost you $15,000 is $365", "Your health shouldn't depend on insurance." Membership "Charged annually at $365"; "Membership renews at then-current price." MRI and CT can be added; add-on tests are extra (`pricing_desktop.json`).
- **[V]** Footer fine print: the first-year price "includes full access to 160+ lab tests, with a leading nationwide provider, in all states except New York and New Jersey." And: "Function Health is a healthcare technology company and not a laboratory or medical provider… does not offer medical advice, laboratory services, a diagnosis, medical treatment, or any form of medical opinion". Testing is at "2,000+ Quest locations nationwide" or an at-home draw.
- **[V]** The same pages say elsewhere "Clinicians review every result and flag issues" and "Personalized protocol for instant action". The captured text does not reconcile this with the disclaimer.
- **[V]** The pricing page footnote reads "*Function Day offer expires at 12:00 PM ET on 10/8/2026." The capture date was 2026-10-30, so this footnote was already out of date when captured.
- **[I]** The buyer is a health-conscious, self-paying adult who finds the standard checkup too thin. The product is access, data and a plan, priced low enough to feel like a subscription.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/home_desktop_viewport.png` |
| Homepage full page (12,262 px) | `screens/home_desktop_full.jpg` |
| Homepage mobile (13,990 px) | `screens/home_mobile_full.jpg` |
| Pricing | `screens/pricing_desktop_full.jpg` |
| How it works | `screens/how-it-works_desktop_full.jpg` |

## 3. Measured visual specifications

From `data/home_desktop.json`.

**Typefaces loaded [V]:** **Financier Display** 300 (roman and italic; headings), **FT Base** 300 / 400 / 600 (body and UI), **Fragment Mono** 400 (11 px micro-labels).

| Role | Face | Size / line-height | Letter-spacing |
|---|---|---|---|
| H1 "Check your health." | Financier Display 300 | 80 px / 72 px (0.9) | normal |
| H2 section titles | Financier Display 300 | 64 px / 64 px (1.0) | normal |
| H3 feature titles | Financier Display 300 | 34 px / 39.1 px; 45 px / 45 px for the six category names | normal |
| Body | FT Base 300 | 16 px / 24 px | normal |
| Small | FT Base | 14 px / 21 px | |
| Micro-labels | Fragment Mono 400 | 11 px / 13.2 px, uppercase | |
| Buttons | FT Base 600 | 16 px | |

**Mobile [V]:** H1 57.3 px, H2 48.2 px, H3 27.1 px.
**Headline device [V, screenshot]:** most H2s are set in roman with the key phrase in *italic terracotta* ("Testing is *easy*", "Monitor early indicators of *1000s of diseases*", "160+ lab tests *chosen by top doctors*", "The new standard *for health*", "Real people. *Real results.*").
**Colour [V]:** `#2A2B2F` text · `#515151` secondary · **`#B05A36` terracotta** (accent: italics, buttons, links; 271 uses) · **`#FEF9EF` cream** (page background) · `#F5EEE1` panel · `#D1C9BF` rules.
**Layout [V]:** `max-width` 1376 px (13 uses, main container), 1392, 888, 640, 340 and 320 px (cards). Page 12,262 px; the final section "Life is short? We disagree." is 440 px tall with 120/96 px vertical padding.
**Components [V]:**
- **Buttons:** fully rounded pills (radius 999 px), padding 12 × 25 px, 16 px semibold. Two forms: cream fill with terracotta text on dark images ("Start testing", "See how it works") and terracotta fill with cream text on the page ("Submit").
- Top announcement bar in terracotta: "Use your HSA/FSA funds to Join Function."
- Header: logo left; centred links (How it works, What we test, Imaging, FAQs, About); right: Log in, "Start testing", search.
- Hero: a full-bleed photograph (a hand reaching toward sunlit foliage) with the H1 in cream; below it a three-item strip "160+ lab tests / Whole body / $1 per day" in mono micro-type.
- Three step cards ("01 160+ lab tests / 02 Results explained / 03 Follow your plan") each with a small chart illustration.
- A horizontally scrolling band of disease names (Pancreatic cancer, Ovarian cancer, Sickle cell disease, Rheumatoid arthritis, Anemia, Gout…) beside a small chart card; a "PAUSE MOTION" control.
- A 3 × 2 grid of biomarker categories (Hormones & thyroid; Cancer & other silent risks; Heart & metabolic; Aging; Mental health & focus; "+More: all-in-one lab testing"), each listing five or six named markers in small grey type.
- A row of "bring your results wherever you go" integration chips (Your doctor, Claude, ChatGPT, Perplexity).
- Celebrity portrait tiles and press-logo row; four vertical video thumbnails; a stat panel (75M+, 2,000+) with a bar chart and a map; a comparison table; a board-of-doctors list; a zip-code field; footer with newsletter.

**Imagery [V]:** warm natural light, skin tones, faces; photographs of named public figures and members; UI illustrations drawn in the same terracotta/cream palette.

## 4. Art-direction analysis

- **[V]** The palette is two colours plus ink: cream background and a single terracotta accent, used for every action and every italic highlight.
- **[I]** The italic-accent-word device does two jobs. It keeps the type calm (thin serif at 64 px) and tells a scanning reader which words matter. Every section can be summarised by reading only the italic words.
- **[I]** A thin, high-contrast display serif plus a light grotesque against cream reads as editorial and lifestyle, closer to a magazine than a medical portal. The data illustrations use the same colours so the product feels part of the brand.
- **[V]** The page is long (12,262 px) but every block uses the same width, the same heading size and the same pill button, so it reads as one system.
- **[I]** Faces dominate the proof sections (celebrities, members), while the biomarker section is text-only and small; the visual weight sits on trust, not on the science.

## 5. Copywriting analysis

Verified copy:
- "Check your health. Every year. Starting with 160+ lab tests detecting 1000+ conditions. Just $365 per year—$1 per day." (imperative headline, then one sentence of quantities).
- "Testing is easy" → "01 160+ lab tests — Test at 2,000+ labs or we'll come to you; 02 Results explained — By top doctors and 1000s of hours of research; 03 Follow your plan — Take action. Test again."
- "Monitor early indicators of 1000s of diseases"; "Most testing starts after a problem. Function tracks your data over time to reveal patterns and early signs unique to you."
- Comparison: "Not your average checkup — Lab tests annually: **160+** vs **~26** (standard checkup)", plus a list of tests included.
- Price frame: "What could cost you $15,000 is $365. Your health shouldn't depend on insurance."
- Close: "Life is short? We disagree."
- Mental-health category: "Mental health & focus" lists Cortisol, High-Sensitivity C-Reactive Protein (hs-CRP), Iron, Ferritin, Methylmalonic Acid (MMA).

Analysis:
- **[I] Offer and price (Hormozi lens):** the offer is a stack of countable items and one small price, expressed three ways (annual, per day, versus a $15,000 alternative). The comparison anchor is unsourced in the captured text.
- **[V] Numbers:** 160+, 1000+, 1000s, 2,000+, 75M+, ~26, $365, $1, $15,000. Several are not defined or sourced on the page ("1000+ conditions", "~26", "$15,000").
- **[V] Internal wording differences:** the homepage says "160+ lab tests"; the how-it-works page says "Your membership includes 100+ biomarkers" and "60+ lab tests included midway through the year". **[U]** These may count different things (tests vs biomarkers, first vs second visit); the pages do not explain the difference.
- **[I] Awareness stage:** the headline assumes the reader already wants testing; the main job is to justify price and credibility. The comparison table acts as a reframe: a standard checkup is shown as incomplete.
- **[V] Proof types in order:** star-quality quotes (named TV and podcast figures) → press logos → member video stories ("The cancer signals doctors missed") → scale stats → board of named doctors with titles. The testimonial headlines are outcome stories about cancer and diabetes.
- **[V] Voice:** short, declarative, second person, plain nouns; friendly; frequent sentence fragments.
- **[V] CTA wording:** "Start testing" (primary, repeated), "See how it works", "See all tests", "Join Function", "Unlock your insights", "Test your levels". The primary action is a concrete verb.

## 6. Conversion journey and offer architecture

**Observed path [V]:** hero "Start testing" → `https://my.functionhealth.com/signup?code=…` (separate app domain, a code parameter in the URL; not visited). Alternatives: "How it works" four steps (Schedule tests → Get insights → Test again → Monitor for life); a pricing page with the same button; a one-field zip-code input to "see testing options" (not required); a newsletter form ("Subscribe and get 9 health guides for living 100 healthy years", email required).
- **[V]** Visitor sees price, scope and process before any account is created. The how-it-works page has a four-step process with benefit bullets under each (e.g. "Built to HIPAA-standards", "Personalized food and supplement guides").
- **[I]** Friction: the page asserts "No insurance needed" but the fine print excludes New York and New Jersey and says price renews at "then-current price"; the stale promotion footnote could confuse a careful reader.
- **[U]** Sign-up questions, payment flow and what "Share your health history" collects were not inspected.

## 7. Commercial or experimental evidence

- **Not yet researched.** No membership counts, revenue or experiment results collected. "75M+ results delivered" and "2,000+ locations" are the company's own figures. Nothing here shows the page converts at any particular rate.

## 8. Distinctive mechanisms worth investigating further

1. **One price said three ways** (annual / per day / versus $15,000).
2. **Italic accent word in headings** to carry the scanning message.
3. **Comparison table** against a "standard checkup" (160+ vs ~26).
4. **A category grid that names actual markers**, including mental health & focus.
5. **Four-step process with a repeating "retest" step**, selling the relationship over time.
6. **Board of named doctors** with credentials under the heading "Built with the world's top doctors".
7. **Celebrity quote tiles** plus outcome-focused member videos.
8. **Zip-code field** to make testing logistics concrete before signing up.
9. **Single accent colour** for every action.

## 9. Transferable principles for BetterHealth

(All **[H]**.)
- State the first-step price, what it includes, and what is extra, in one place, with the unit and renewal terms.
- Use one accent colour for every action, and use italic emphasis on the key phrase of each heading so a skimming reader gets the argument.
- Show a four-step process that includes the follow-up and re-assessment step, to signal continuity of care.
- Name what is assessed in the language of the patient's concern ("sleep and energy", "focus", "stress"), with a few concrete examples, but do not present a count of tests as the benefit.
- Use named, credentialed clinicians and state exactly what each of them does; here, the board is advisory, whereas BetterHealth's clinician is the treating doctor.
- Put a concrete logistics element (location, how to book) before the enquiry button.

## 10. Limitations, open questions, misapplication risks

- **Limits:** REA homepage inspection only; cookie banner left open in screenshots; `/what-we-test`, `/imaging`, `/faq` not captured; sign-up app not visited; videos not played; animations and the "PAUSE MOTION" behaviour not measured; no hover states.
- **Open questions:** What is behind "1000+ conditions" and "~26"? Why do 160+ tests and 100+ biomarkers both appear? Is the board advisory only? How does the stale promotion affect trust?
- **Misapplication risks for BetterHealth:**
  - Function's model is standardised, high-volume testing with a low price; BetterHealth's value is individual clinical judgment. Counting tests (160+) as the benefit would invite the wrong comparison.
  - The disclaimer that the company is "not a medical provider" next to "clinicians review every result" shows a tension that a licensed practice must avoid; BetterHealth must state clearly who is the responsible physician.
  - Celebrity endorsements and member cancer stories are not usable under medical-advertising and confidentiality norms.
  - Fear-based framing ("cancer signals doctors missed") is inappropriate for a psychiatric practice with anxious patients.
  - Biomarker panels for "mental health & focus" (cortisol, hs-CRP, ferritin) are presented without any stated clinical role; implying that such markers diagnose mental conditions would be misleading.
  - An unsourced "$15,000 versus $365" claim is a pricing device that BetterHealth could not copy without a verifiable comparison.
