# 03 · Kusnacht Practice — https://kusnachtpractice.com

**Group A · Ultra-premium psychiatric care, confidentiality, individualised treatment, high-ticket communication**
**Captured:** 2026-10-30 · Chromium (Playwright) 1440×900 and 390×844 · REA not yet run
**Evidence folder:** `../evidence/03-kusnacht/` (consent banner declined with "Deny" before capture)

Labels: **[V]** Verified · **[I]** Interpretation · **[H]** Hypothesis · **[U]** Unverified.

Pages captured (all 200): `/` · `/pricing/` · `/our-approach/` · `/contact/`.
Not captured: team, FAQ, treatment pages, hospitality, health assessments, `/de/`. The enquiry form, if any, was not found (the `forms` field is empty on every captured page).

---

## 1. Business model, customer, commercial context

- **[V]** Private residential treatment in Switzerland for mental health, addiction and behavioural disorders, plus precision medicine, internal medicine, longevity ("BIO-R® method for rejuvenation & longevity"), health assessments and aesthetic medicine (nav and homepage, `home_desktop.json`).
- **[V]** Price is published: "Our programmes begin at **CHF 117,300 per week**. This includes all treatment costs, excluding travel to and from Zurich, unrelated medical expenses, and Continuing Care. Fees are paid directly by the client. We do not work with insurance providers, but we can offer a detailed written quotation upon request." Swiss-resident insured clients "may qualify for partial reimbursement… (KVG)" (`pricing_desktop.json`).
- **[V]** The pricing page lists 15 inclusions, from "Comprehensive medical and psychiatric assessment", "Bespoke treatment plan" and "24/7 medical and clinical supervision" to "Ultra luxury private villa overlooking Lake Zurich", "private chef, chauffeur" and "Limousine service to all appointments".
- **[V]** Languages offered in the header: English, Deutsch, French, Arabic (`/`, `/de/`, `/fr/`, `/ar/`).
- **[I]** The buyer is an ultra-high-net-worth individual or their family. The page sells discretion and a total-care environment; the price is stated to filter, not to persuade.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/home_desktop_viewport.png` |
| Homepage full page (8,033 px) | `screens/home_desktop_full.jpg` |
| Homepage mobile (9,668 px) | `screens/home_mobile_full.jpg` |
| Pricing | `screens/pricing_desktop_full.jpg` |
| Contact | `screens/contact_desktop_full.jpg` |
| Our approach | `screens/our-approach_desktop_full.jpg` |

**Capture caveat [V]:** in `home_desktop_full.jpg` a white band of about 500 px appears directly under the hero and before "Your future is yours to shape". The text and image beneath it render, so it is probably a scroll-triggered reveal that had not fired when the screenshot was taken. **[U]** I have not confirmed this. It is not treated as a design feature.

## 3. Measured visual specifications

From `data/home_desktop.json`.

**Typefaces loaded [V]:** **ltMuseum** weight 300 (headings, a light serif in uppercase) and **suisseIntl** 400 (body and UI, a Swiss-style grotesque).

| Role | Face | Size / line-height | Letter-spacing | Case | Colour |
|---|---|---|---|---|---|
| H1 | ltMuseum 300 | 40 px / 48 px (1.2) | 1.6 px (0.04 em) | uppercase | `#FEFEFE` on image |
| H2 | ltMuseum 300 | 24 px / 32 px (1.33) | 0.96 px (0.04 em) | uppercase | `#2C2825` or `#FEFEFE` |
| Nav / links | suisseIntl 400 | 12 px | 0.96 px | uppercase | `#2C2825` |
| Menu list items | suisseIntl 300 | 18 px | 0.72 px | sentence case | `#2C2825` |
| Body | suisseIntl 400 | 14 px / 20 px; 16 px / 24 px | — | | `#2C2825` / white |
| Small | suisseIntl 400 | 12 px / 16 px | | | white on image |

**Mobile [V]:** H1 24 px; H2 20–24 px. The largest heading on desktop is only 40 px, small for a hero.
**Colour [V]:** `#2C2825` warm near-black (ink), `#FEFEFE`, `#686F45` olive green (used on the call-to-action panel and the "Get in touch" button), `#111827` (footer links), `#E2E2E2` (rules), `#7D7D7D` (muted). Image colour is warm amber, cream and brown.
**Layout [V]:** a `max-width` of 1920 px appears 12 times (full-bleed sections), 562 px for text columns. Section vertical padding is 48 px on text sections. Section heights at 1440 px: 1,800 (hero + reveal band) · 905 · 800 · 905 · 800 · 601 · 778 · 896; page 8,033 px.
**Structure [V, from screenshot]:**
- Fixed top bar: menu icon, "Our approach", search icon; centred wordmark "KUSNACHT (K) PRACTICE"; at right a phone number, "Contact us", language selector.
- Full-viewport hero with a looping video (the text "Pause Video" is in the DOM), "FIND YOUR WAY BACK TO YOURSELF" in white, one line of description at the bottom, and an olive "GET IN TOUCH" button at the lower right.
- Text–image rows: a narrow left text column (about 240 px wide in the screenshot) with a tall portrait image on the right, with a large empty middle.
- Two **50/50 full-bleed tiles** side by side (Mental health & addiction | Precision medicine; Internal medicine | Rejuvenation & longevity), each with a small label above a larger centred white title on a photograph. Each tile 720 × 800 px.
- A team list: nine roles (psychiatrists, psychologists and psychotherapists, internal medicine doctors, longevity doctors, precision medicine experts, complementary therapists, personal trainers, nutritionists, nurses) as a hairline-separated list.
- A privacy section with a two-image slider.
- A closing section: a misty lake photograph with an **olive panel** at the right holding the heading, a paragraph and a white button "We're ready, connect with us".
- Footer: wordmark, four columns of links.

**Imagery [V]:** a consistent warm palette (amber, cream, olive, brown). Subjects: autumn leaves (video hero), a hand pressed against a wall, a person's shadow, oil droplets, an eye, a hand holding glasses, a stethoscope on a desk with a notebook, brown fabric, a lake with sailboats at dawn, a hotel-like corridor with a motion-blurred figure. **No faces and no clinic exteriors or interiors in clinical use** appear on the homepage.

## 4. Art-direction analysis

- **[V]** Headings are a thin serif in capitals at 24 px with +4 % tracking, far smaller than the hero type on Heartwood or Biograph. The page is quiet: its hierarchy is carried by image size, not by type size.
- **[I]** The image set works as a mood board: warm light, shadows, skin, fabric, water. This avoids showing patients or distress, and avoids showing medical equipment except for one stethoscope. It communicates calm and privacy through absence.
- **[V]** The two-tile rows give four service lines equal visual weight; the viewer chooses by image and title.
- **[I]** Large unfilled space is used between the narrow text block and the portrait image. It slows reading and signals luxury, but at 1440 px it leaves the page with long passages of white.
- **[I]** One saturated colour (olive `#686F45`) is reserved for the single point of action. In an otherwise warm-neutral page this makes the CTA identifiable without a heavy button.
- **[V]** The serif/grotesque pairing (ltMuseum / Suisse) is a recognisable luxury-Swiss combination; both are commercial typefaces.

## 5. Copywriting analysis

Verified copy (`home_desktop.json`, `pricing_desktop.json`, `contact_desktop.json`):
- Hero: "Your healing begins here" / "Find your way back to yourself". Description: "The world-renowned private treatment center dedicated to mental health and addiction in Zurich, Switzerland."
- "Your future is yours to shape. Because we believe in your potential, we want to guide you towards a life filled with meaning, balance, and lasting renewal."
- "Your healing is personal. So is our approach. … We go beyond symptom management to find the root causes."
- "Medical excellence. Dedicated in-house team… **At Kusnacht Practice we have more doctors than clients.**"
- Privacy: "Total privacy and discretion encompass everything we do. From the very first contact… we ensure you remain anonymous. Each client is treated in one of our 10 luxury villas… no exterior signage or branding."
- Contact: "We treat all enquiries with the utmost discretion. Every journey begins with a conversation rooted in trust and understanding."

Analysis:
- **[I] Awareness stage:** the visitor is assumed to be problem-aware and solution-aware but not provider-aware; the copy is about the provider's qualities (privacy, team ratio, personalisation), not about symptoms.
- **[V] Concrete vs abstract:** concrete facts: price from CHF 117,300/week, 10 villas, "more doctors than clients", 15 inclusions, nine staff roles, 24/7 supervision, a written quotation on request. Abstract: "world-renowned", "transformative", "profound healing", "root causes". The homepage names no clinicians and shows no outcomes, testimonials or accreditations in the captured text; **[U]** the team page may contain them.
- **[V] Superlatives** ("world-leading", "world-renowned", "ultra luxury", "unparalleled discretion") are used without sources on the captured pages.
- **[I] Objection handling:** the highest-priority objection is exposure ("Will anyone find out?"), answered at the start, in the contact page and in a dedicated homepage section. The second is "Is this a real medical service or a spa?", answered by the team list, 24/7 supervision, and the "more doctors than clients" line.
- **[V] Voice:** warm and formal, second person, long compound sentences with stacked abstract nouns; short imperative CTAs ("Discover", "Get in touch", "We're ready, connect with us").
- **[V] Contact page FAQ questions** show the family-member objection: "How do I convince someone that I care about to visit Kusnacht Practice for therapy?"

## 6. Conversion journey and offer architecture

**Observed path [V]:** homepage "Get in touch" (hero) → `/contact/`. Contact page: "Speak to us" with channel buttons **WhatsApp**, **iMessage**, **Treatment enquiry**; separate phone numbers and email addresses for "General enquiries" and "Treatment enquiries"; a postal address; a five-question FAQ.
- **[V]** The first contact options require no form and no disclosure: messaging apps and telephone.
- **[V]** The phone number is permanently visible in the header.
- **[V]** The pricing page ends with "Start your journey", a paragraph on discretion and a connect button.
- **[I]** Friction a visitor could meet: no description of what happens in the first call; no stated response time; the price is stated for the entry programme only; the pricing figure may be a barrier for non-ultra-premium visitors (intended).
- **[U]** What the "Treatment enquiry" button opens (form, chat, or modal) was not tested.

## 7. Commercial or experimental evidence

- **Not yet researched.** No third-party information about revenue, patient numbers, outcomes or conversion has been collected. Statements such as "world-renowned" and "10 luxury villas" are the company's own.

## 8. Distinctive mechanisms worth investigating further

1. **Published price and inclusions list** at the highest tier of the market.
2. **No-form first contact:** WhatsApp, iMessage, telephone, with separate numbers for general and treatment enquiries.
3. **Anonymity as a feature with specifics:** no signage on villas, anonymous from first contact.
4. **A face-free, warm-toned image language** instead of clinical or lifestyle imagery.
5. **Four service lines as two 50/50 image tiles.**
6. **A single accent colour for the CTA** (olive).
7. **A "more doctors than clients" ratio claim** as proof of care intensity.
8. **FAQ written from the family member's viewpoint.**

## 9. Transferable principles for BetterHealth

(All **[H]**.)
- Offer two or three low-disclosure ways to start (telephone, secure message, short enquiry) and say that nothing needs to be explained in the first contact.
- Show a fee or fee range and what it includes; state that it is paid directly and not by insurance, if true.
- State confidentiality in concrete operational terms (how enquiries are handled, who sees them) rather than as a general promise.
- Reserve one accent colour for the single action.
- Use imagery that signals calm and privacy without showing patients: light, hands, rooms, water. Combine with at least one real photograph of the clinician.
- Write an FAQ for the person asking on behalf of someone else.

## 10. Limitations, open questions, misapplication risks

- **Limits:** no REA run; hero video not examined; scroll-reveal band unresolved; menu overlay not opened; no form or chat tested; team, FAQ and treatment pages not captured; hover states not captured.
- **Open questions:** What do the three "Speak to us" buttons do? Does the team page name clinicians with qualifications? How quickly is a first call answered?
- **Misapplication risks for BetterHealth:**
  - Kusnacht's price (from CHF 117,300/week), 24/7 residential model and villa hospitality have no equivalent in a small outpatient practice. Copying "ultra luxury" language would promise something BetterHealth does not offer.
  - Unsourced superlatives ("world-renowned", "root causes") are a regulatory and credibility risk for a physician.
  - A page with no named clinicians in its homepage text is a weakness for a practice whose product is a specific physician's judgment.
  - Very small headings and wide empty areas may reduce readability.
  - A WhatsApp or iMessage first contact for medical enquiries has data-protection implications under Swiss law; legal review is needed before copying it.
