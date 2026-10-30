# 05 · Chenot — https://www.chenot.com

**Group A · Branded medical methodology, programme packaging, price presentation, scientific authority**
**Captured:** 2026-10-30 · Chromium (Playwright) 1440×900 and 390×844 · REA not yet run
**Evidence folder:** `../evidence/05-chenot/` (cookie banner declined with "DENY")

Labels: **[V]** Verified · **[I]** Interpretation · **[H]** Hypothesis · **[U]** Unverified.

Pages captured (all 200): `/` · `/chenot-method/` · `/about-chenot/world-best-detox-programme/` · `/contact-us/`.
Not captured: individual programme pages (so the unit and duration behind each price are unknown), destination pages, booking page (`/book-your-stay/`), press, products.
**Capture note:** the standard full-page screenshots show blank white areas below the hero because content reveals on scroll. A second capture mode photographs the page screen by screen: use `screens/*_desktop_stitched.jpg` for desktop. The sticky header repeats in every frame of the stitched images; that is a capture artefact. One grey box in the stitched homepage is a video that had not loaded.

---

## 1. Business model, customer, commercial context

- **[V]** A group of destination wellness and "medical wellness" properties: Chenot Palace Weggis (Switzerland), Chenot Palace Gabala (Azerbaijan), Chenot Espace L'Albereta (Italy), Chenot Espace One&Only Portonovi (Montenegro), Chenot Spa Selman Marrakech, plus a products line (`contact-us_desktop.json` form options and `home_desktop.json`).
- **[V]** The commercial core is a trademarked method: **Chenot Method®**, **Chenot Diet®** and **Chenot Lifestyle Biomarkers®** (`chenot-method_desktop.json`). Company claim: "Since 1970 we have empowered thousands of people…".
- **[V]** Five named core programmes with a price shown on the homepage: Advanced Detox **CHF 5'500**; Recover & Energise **CHF 6'400**; Prevention & Ageing Well **CHF 7'100**; Sleep Cycles **CHF 7'960**; Body Insights & Optimisation **CHF 6'100**. **[U]** The captured text gives no unit (per night, per stay, number of days). The programme pages that would say so were not captured.
- **[V]** The site is built on WordPress with Elementor (generator meta: "Elementor 4.3.5"); forms use WS Form (`/wp-json/ws-form/v1/submit`).
- **[I]** The buyer is a premium wellness traveller drawn to anti-ageing and "detox" outcomes. The product is a branded, repeatable programme at fixed prices.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/home_desktop_viewport.png` |
| Homepage desktop, stitched | `screens/home_desktop_stitched.jpg` |
| Method page, stitched | `screens/chenot-method_desktop_stitched.jpg` |
| Science / award page, stitched | `screens/about-chenot-world-best-detox-programme_desktop_stitched.jpg` |
| Contact, stitched | `screens/contact-us_desktop_stitched.jpg` |
| Homepage mobile | `screens/home_mobile_full.jpg` (may show the same scroll-reveal blanks; not re-captured) |

## 3. Measured visual specifications

From `data/home_desktop.json`.

**Typefaces loaded [V]:** **Brandon Grotesque** (400, 700; headings, uppercase), **Verlag** (300, 400, 700; body), **Portrait** 400 (the italic serif accent word "detox" in the hero), plus an icon font.

| Role | Face | Size / line-height | Letter-spacing | Case |
|---|---|---|---|---|
| H1 hero | Brandon Grotesque 400 | 54.6 px / 73.7 px (1.35) | 3.28 px (0.06 em) | uppercase, white; second line "detox" in Portrait italic |
| H2 large section title | Brandon Grotesque 400 | 37.6 px / 50.8 px (1.35) | 2.26 px (0.06 em) | uppercase |
| H2 medium | Brandon Grotesque 400 | 28.2 px / 38.1 px (1.35) | 1.69 px (0.06 em) | uppercase |
| H2 card title | Brandon Grotesque 400 | 19.4 px / 26.2 px (1.35) | 1.94 px (0.10 em) | uppercase |
| H3 card tag | Brandon Grotesque 400 | 14 px / 22.4 px (1.6) | 1.4 px (0.10 em) | uppercase |
| Body | Verlag 300 | 20.8 px / 30.4 px (1.46) | 0.21 px | sentence case |
| Card body | Verlag | 16 px / 23.4 px (1.46) | | |
| Buttons | Brandon Grotesque 700 | 12 px | 1.2 px (0.10 em) | uppercase |

**Mobile [V]:** H1 42.8 px, H2 32.4 px and 24.3 px, card H2 18.1 px.
**Colour [V]:** black text (`#000000`) on `#F7F8F9` (page) and `#F7F5F1` (warm cream) alternating backgrounds, a full-black band for the award banner, white text on photographs, grey `#A2A19C` for secondary text.
**Layout [V]:** `max-width` 1260 px and 990 px. Section heights at 1440 px: hero 900 · award band 271 · intro 447 · "ageing is dynamic…" 1,213 · exclusive experiences 644 · "inspiring world" 1,169 · **core programmes 949** · destinations 932 · products 1,350 · news 623. Page 8,xxx px.
**Components [V, from stitched screenshots]:**
- Header: a thin bar with "MENU" and a language selector at left, the wordmark **CHENOT** centred, "CONTACT US" and "RESERVE YOUR STAY" at right. It is sticky.
- Buttons: **pill outlines** (computed radius 36 px), 12–14 px bold uppercase with 0.1 em tracking, padding 20 × 47.4 px on the large variant.
- Award band: a full-width black strip with a laurel "Winner — World's Best Detox Programme" badge and a sentence.
- Programme cards: five narrow vertical cards in a row, each with a tall photograph, an uppercase title, a small tag ("DETOX PROGRAMME"), a short description, a CHF price and a "View …" link.
- Destination carousel with arrow control.

**Imagery [V]:** bright, saturated outdoor photography (a runner against Alpine peaks; two women walking beside a lake), studio treatment imagery (a woman suspended in red hammocks), macro close-ups (DNA helix, red light). Colour comes from the photographs; the interface is black on off-white.

## 4. Art-direction analysis

- **[V]** The hero's headline is a two-voice construction, as at Lanserhof: an uppercase sans line ("GET READY TO") over one italic serif word ("detox") — the single largest typographic gesture on the page.
- **[I]** Tracked uppercase sans headings at 0.06–0.10 em on off-white with thin outline pill buttons is a generic luxury-wellness look. The page's distinguishing assets are the trademarked terms (®) and the programme cards, not the visual identity.
- **[I]** The black award band directly under the hero places an institutional-looking claim at the first point of scroll, before any explanation.
- **[V]** The page alternates warm cream and cool off-white backgrounds (`#F7F5F1`, `#F7F8F9`), a subtle change that separates sections without borders.
- **[I]** The mix of photography styles (landscape, studio, macro, spa) is wider than at Lanserhof and Kusnacht, which makes the brand feel more like a catalogue than an authored identity.

## 5. Copywriting analysis

Verified copy:
- Hero: "GET READY TO *detox*". Award band: "Awarded World's Best Detox Programme 2026 for the sixth year in a row, alongside clinical research confirming the unique benefits of the Chenot Method®."
- "LIVE HEALTHIER FOR LONGER — At Chenot we believe growing older is not synonymous with a decline in health… You have the potential to reach the age of 120 and still be fully active."
- "AGEING IS A DYNAMIC PROCESS THAT CAN BE GUIDED, SLOWED AND IMPROVED. Since 1970 we have empowered thousands of people to make meaningful change and optimise their health, slow down or even reverse biological ageing."
- Method page: "At Chenot, we do not treat disease. Instead, we address the root cause: ageing." "Think of each of your cells as a battery. With time they become rusty and lose energy…" "80% of your health is influenced by your lifestyle, and only 20% is predetermined by your genes."
- Science page: "Detoxification… addressing the twelve hallmarks of aging"; "the failure of cellular detoxification becomes a root cause of both physical and mental deterioration."
- Evidence block: "The clinical study published in 2025 reveals the unique benefits of Chenot's plant-based fasting-mimicking diet: Lower IGF-1… Higher ketones (BHB)… More cellular clean-up (autophagy markers)… Longevity genes upregulated (SIRT1 and FOXO1)." followed by "DOWNLOAD THE STUDY — Simply complete the form below to receive the full study by email."
- Programme copy, e.g. "Recover & Energise programme reduces chronic stress and fatigue which restores optimal energy levels." "Sleep Cycles… targeted treatments timed to your chronotype".

Analysis:
- **[I] Mechanism-first selling (Schwartz, solution-aware to product-aware):** the visitor is given a causal story ("cells are batteries", "detoxification clears debris", "ageing is the root cause") before programmes. The story is the product's differentiator.
- **[V] Branded method:** three ® terms give the offer a name that cannot be compared directly with others. This is an April Dunford-style category-ownership device. **[I]** It also makes the offer harder for a reader to evaluate independently.
- **[V] Evidence handling:**
  - A "clinical study published in 2025" is mentioned; the captured text names no authors, journal, sample size, comparison group or duration.
  - The reported results are **biomarkers** (IGF-1, ketones, autophagy markers, SIRT1/FOXO1 activity). No clinical outcomes (symptoms, disease incidence, function) are reported in the captured text.
  - The full study is behind an **email form**, which also works as lead capture.
  - The award's issuer is shown only as a badge image; its name was not extracted. **[U]** Whether it is independent.
- **[V] Absolute and outcome claims** ("reverse biological ageing", "reach the age of 120", "we address the root cause: ageing", "eliminate toxins") appear without qualification. I have not assessed them against the medical literature; they are listed here because the master prompt requires distinguishing observed claims from evidence, and the page does not supply the evidence in its text.
- **[V] Voice:** instructive and certain, with metaphor (battery, rust, cleanup, lanes: "you can shift lanes at any point"). Few conditionals.
- **[V] CTA wording:** "Reserve your stay", "Contact us", "Find out more about the science behind Chenot", "Watch the film", "Discover exclusive experiences", "View Advanced Detox", "Download the study".

## 6. Conversion journey and offer architecture

**Observed path [V]:** hero → award band → "Reserve your stay" (`/book-your-stay/`, not captured) → …; mid-page: programme cards with price → "View …" (programme page); science page: "Reserve your award winning detox" and "Download the study" (email); contact page form.
- **[V]** Prices are visible on the homepage in the programme cards, before any enquiry.
- **[V]** The **contact form** (`contact-us_desktop.json`) has a first selector "Section" (Chenot Group, each destination, Chenot Products, Business Development & Partnership, Press & Media), then **required** Interest, First name, Last name, Email, Phone and Notes, an optional Title, two optional newsletter checkboxes, a **required** privacy-policy checkbox, and reCAPTCHA. That is seven required inputs. The page promises "one of [our] team will respond to your request within 24 hours."
- **[V]** Alternatives to the form: WhatsApp (Weggis answered 9:00–18:00 GMT+1; Gabala via WhatsApp "24/7"), phone numbers per property, "Schedule a call" at Weggis.
- **[I]** Friction: the form is long for a first contact; the price shown has no unit; the visitor must choose among five programmes and five destinations; the programme cards use the same tag ("DETOX PROGRAMME") for different goals, so differences must be read in each description.
- **[U]** Booking flow, programme-page content and the email-gated study were not followed.

## 7. Commercial or experimental evidence

- **Not yet researched.** No revenue, occupancy or conversion data collected. The study and award are the company's own presentation. I have not read the study.

## 8. Distinctive mechanisms worth investigating further

1. **A trademarked method name** (®) used as the organising idea across the site.
2. **Programme cards with visible prices** in a five-across row.
3. **An award band directly under the hero** (black strip, laurel badge).
4. **Evidence as lead magnet:** study summary on the page, full text by email.
5. **A causal metaphor for the mechanism** (cells as batteries; cleanup).
6. **Routing in the contact form** by property or department.
7. **Contact options by channel and hours stated explicitly** (WhatsApp, call scheduling, 24-hour response promise).

## 9. Transferable principles for BetterHealth

(All **[H]**.)
- Give the clinical approach a plain, descriptive name that the practice can own, **without** trademark-style branding or invented jargon, and explain its steps once, clearly.
- Show the price next to each defined service, **with its unit and what it includes**. Chenot shows the first part but not the second.
- Offer a short, readable summary of the evidence for the approach on the page, with authors, journal, year and what was measured (outcomes versus biomarkers), and let readers download the source. Do not gate it behind an email address.
- Say how fast an enquiry is answered and through which channels, as Chenot does with its 24-hour promise.
- Keep the first-contact form short: Chenot's seven required fields are a counter-example.

## 10. Limitations, open questions, misapplication risks

- **Limits:** no REA run; menu overlay not opened; programme and booking pages not captured; units of the prices unknown; mobile full-page capture likely shows the same blank reveal areas and was not redone; hover states not captured; study not read; award issuer not identified.
- **Open questions:** What do the prices cover (nights, programme length)? What are the study's design and outcomes? Which body issues the award? How is the 24-hour response measured?
- **Misapplication risks for BetterHealth:**
  - Chenot's claims ("reverse biological ageing", "address the root cause: ageing", "eliminate toxins", reaching 120) are the kind of unqualified promise the uploaded dossiers also flag. A physician-led practice cannot make them and should not borrow the vocabulary ("detox", "root cause").
  - A trademarked method name with ® signals a product, not a physician's reasoning; it may undermine the idea that the doctor's individual judgment is the service.
  - Biomarker changes presented as proof of benefit would be misleading in a psychiatric context, where patients need outcome measures such as symptoms and function.
  - Lead-capturing evidence behind an email gate conflicts with a confidentiality-first positioning.
  - Different photography styles on one page weaken identity; BetterHealth needs one consistent image language.
