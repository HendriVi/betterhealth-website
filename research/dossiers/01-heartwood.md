# 01 · Heartwood Collective — https://www.thehwc.com

**Group A · Editorial design, premium positioning, psychological recognition**
**Captured:** 2026-10-30 · Chromium (Playwright) at 1440×900 and 390×844 · REA 6.8.0 run on the homepage only (passive; network/console empty, third-party origins filtered; see `../evidence/rea-summary.md` and `../evidence/<site>/rea/`) (see `../00-availability-report.md`)
**Evidence folder:** `../evidence/01-heartwood/` (manifest.json lists every capture with status and timestamp)

Labels: **[V]** Verified (a file in `evidence/` shows it) · **[I]** Interpretation (my reading of what a verified fact does) · **[H]** Hypothesis (a testable guess, not demonstrated).

Pages captured (all HTTP 200, desktop + mobile): `/` · `/team` · `/tuning-offsites` · `/companies` · `/investors` · `/book`.
Not captured: `/privacy-policy`, retreat pages, Substack/podcast (external). The booking form on `/book` is not visible to the capture (see §6).

---

## 1. Business model, customer, commercial context

- **[V]** Offer: embedded coaching and consulting for startup teams and, on a separate page, for investors (`/companies`, `/investors`). Named service: **Core** ("embedded coaching and consulting model", `companies_desktop.json` → fullText). Meta description: "We embed expert coaches inside startups to align founders, teams, and culture" (`home_desktop.json`).
- **[V]** Buyer segmentation is a first-class choice: nav has "For Companies" and "For Investors"; the homepage asks "What are you building?" with two buttons, *Companies* and *Portfolios* (`home_desktop_full.jpg`, lower third).
- **[V]** Price is not shown on any captured page. The only commercial terms visible are a banner: "off-site tuning session at cost to three selected teams in 2026" with an application link, and a "Nominate a team" button (`tuning-offsites_desktop.json`).
- **[V]** Footer: "2025 Heartwood Collective, a part of Project Atlas LLC."
- **[I]** This is a relationship-sold, high-consideration B2B service. The site's job is to make a first conversation feel worth having, not to close a sale.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/home_desktop_viewport.png` |
| Homepage full page (6,696 px tall) | `screens/home_desktop_full.jpg` |
| Homepage mobile (6,372 px tall) | `screens/home_mobile_full.jpg` |
| Companies page | `screens/companies_desktop_full.jpg` |
| Investors page | `screens/investors_desktop_full.jpg` |
| Team page | `screens/team_desktop_full.jpg` |
| Booking page, first viewport | `screens/book_desktop_viewport.png` |

## 3. Measured visual specifications

All values from `data/home_desktop.json` unless noted. Computed styles, not estimates.

**Typefaces loaded [V]:** Spectral (500, 700), Newsreader (400), Montserrat (400, 700), and a custom display face named **PORTAL**.

**Type scale (desktop, 1440 px) [V]**

| Role | Face | Size / line-height | Letter-spacing | Notes |
|---|---|---|---|---|
| Hero statement words ("RESPONSIVE", "SEE CLEARLY") | PORTAL 500 | 143.9 px / 143.9 px (1.0) | 2.88 px (0.02 em) | Thin all-caps display, sizes vary per phrase: 57.9, 69.7, 96.3, 143.9 px |
| Section headline (H2) | Spectral 500 | 38.5 px / 54.7 px (1.42) | 1.92 px (0.05 em) | White on dark |
| Eyebrow / label (H3) | Spectral 500 | 19.5 px / 29.0 px | 0.97 px (0.05 em) | Gold on dark |
| Footer column heads (H4) | Spectral 500 | 26.4 px / 38.6 px | 1.32 px | |
| Body / lead paragraph | Montserrat 400 | 19.5 px / 27.2 px (1.4) | — | Most common paragraph style |
| Small text, footer links | Montserrat 400 | 14.3 px / 20.0 px | 0.97 px | |
| Mission statement | Montserrat 700 | 28.1 px / 39.3 px | — | Centered, 2 instances |

**Mobile (390 px) [V]:** hero words scale to 55 px, 44 px and 31.9 px (`home_mobile.json`); H2 to 29.2 px; footer heads to 22.1 px. The largest display word shrinks to about 38 % of its desktop size (143.9 → 55 px).

**Colour [V]** (most frequent computed values; hex converted from rgb):
`#12251E` deep green (page background for dark sections) · `#CF9651` gold/ochre (one full-bleed section, eyebrow text, logo accent) · `#6C3613` brown (hero tint, body text on light pages) · `#F5F1E3` cream (announcement bar, form card) · `#FCFCFC` off-white (text on dark).
Green, gold and brown each own whole sections; white or cream is used for type on them.

**Layout [V]**
- Only one `max-width` value appears: 1398.4 px (a wrapper). Text blocks are narrow and centred; I did not capture column grids, so no grid claim is made.
- Section heights at 1440 px wide (`home_desktop.json` → sections): header 157 · full-viewport hero 753 · mission block **951** · gold statement block **1,106** · malachite-texture block **1,191** · closing "see clearly / move together" block **1,141**. Total page 6,696 px.
- The mission block contains one eyebrow, one 3-line statement and one link, in about 950 px of height (see `home_desktop_full.jpg`): very low density.

**Components [V]**
- Primary button "Get Started": white fill, dark-green text, 5 px radius, 0 × 35.2 px padding. Secondary buttons ("Companies", "Portfolios", "Newsletter + Podcast"): transparent with a thin light outline, same 5 px radius and padding.
- Text link "Get a Coach": no box, underline rule beneath (hero-adjacent).
- Header: logo at left, a two-line hamburger icon at right, on every viewport width captured (`book_desktop_viewport.png`). The nav list items were not captured by the script (the `nav` field is empty); the link inventory comes from the footer: Home, The Team, For Companies, For Investors.
- A thin announcement bar sits above the header on every page.
- Conceptual diagram on the homepage: three concentric white circles labelled *Individual*, *Team*, *Cultural Practices* with gold curved labels (*Growth*, *Coherence*) on a malachite-green marble image (`home_desktop_full.jpg`, around y = 2,967).
- Imagery [V]: a sand-dune photograph (hero), a macro marble/malachite texture used as full-bleed background in two places, one documentary-style photograph of five people sitting in a circle outdoors, a larger marble texture behind the footer. 8 `<img>` elements on the homepage (`images` field), most with `object-fit: cover`.

## 4. Art-direction analysis

- **[V]** The page alternates large flat colour fields (dark green → gold → texture → dark green) with very little content in each. Text occupies a small fraction of every field; the largest type is a hairline-thin all-caps display face.
- **[I]** The thin display type at 96–144 px against flat colour reads as a poster or a printed announcement, not as a software or consulting site. The contrast with the heavier Montserrat bold mission line and the serif Spectral headings creates three typographic voices: whisper (PORTAL), statement (Montserrat bold), reflection (Spectral).
- **[I]** The textures (sand, marble) are natural-material references that tie to the brand name ("Heartwood") and to the idea of layers and patterns in the copy. The one photograph of a human group is the only literal image of the service, and it is placed beneath the "See clearly / Move together" words with the headline overlapping its top edge (`home_desktop_full.jpg`, second chunk). The overlap is a deliberate departure from a stacked headline-then-image layout.
- **[I]** The diagram of nested circles is the only explanatory graphic. It turns the abstract claim "we work at every layer of your organization" into a picture, placed right beside that sentence.
- **[H]** The large empty colour fields slow scrolling and give each idea room, which may make the offer feel considered and unhurried. This is untested here.
- **Differences from typical coaching sites [I]:** no stock-photo smiling faces, no logo wall, no testimonial carousel, and no price table appear on the homepage.

## 5. Copywriting analysis

Verified copy (from `home_desktop.json` and `companies_desktop.json`):

- Hero statement: "Don't just survive the storm—become a leader who reads the weather." (set as a vertical line in the gold block).
- Positioning: "RESPONSIVE COACHING AND CONSULTING — to equip leaders and teams with the cultural intelligence to move quickly, foster innovation, and execute on their goals."
- Mission: "We facilitate the growth of individuals and groups to create high-functioning teams."
- Problem frame: "Behind every problem is a pattern waiting to be understood." / "Bringing hidden dynamics into view unlocks what high-growth teams need most: faster decisions, steadier leadership, and the ability to stay aligned, even in uncertainty."
- Offer: "Core is our embedded coaching and consulting model designed to strengthen your entire organization, not just individual leaders. Most coaching supports personal growth. Core connects it to performance, team alignment, and culture change, where the real leverage lives."
- CTAs: "Get a Coach", "Get Started", "Let's Chat", "Book a consultation to get a plan customized for your team." Booking page: "LET'S BEGIN WHERE YOU ARE — Start the conversation that could change everything".

Analysis:
- **[I] Reframe (Schwartz, problem-aware stage):** the copy moves the reader from a visible problem to an unseen cause ("behind every problem is a pattern"). It does not describe symptoms the reader would recognise personally; it names a category ("hidden dynamics").
- **[I] Differentiation (Dunford):** the contrast "Most coaching supports personal growth. Core connects it to…" positions against individual executive coaching. The stated alternative is embedded team-level work, not a method with a proprietary name beyond "Core".
- **[V] Concrete vs abstract:** the page lists five outcomes ("Develop leaders who stay present and effective under pressure", "Build teams that work together, not just side by side", …). Nouns are mostly abstract (*alignment, coherence, culture, clarity*). No numbers, durations, session counts, fees or named clients appear on the pages captured.
- **[V] Proof:** the homepage contains no testimonials or logos in the captured text. The `/team` page lists four named practitioners with credentials (e.g. "Brandon Houston, MA, LPC", "Katherine Folk-Sullivan, PCC", "Dr. Kari Sulenes") and states the team draws on "Psychotherapy, Gestalt theory, Somatics, Internal Family Systems, Trauma-Informed Coaching".
- **[V] Voice:** second person and first-person plural, present tense, medium-length sentences, emotionally neutral, a few metaphors (storm/weather, layers, patterns). Vocabulary is systems-oriented rather than clinical.
- **[V] CTA wording** is soft and low-commitment (*Get Started, Let's Chat, Let's Begin Where You Are*). The only specific action is the consultation: "to get a plan customized for your team".
- **[I] Language × typography:** the most important idea is the one set in the biggest type. The "see clearly / move together" pair is 96 px and 70 px; the sentence explaining it is 19 px. The reader receives the claim visually first, then the explanation.

## 6. Conversion journey and offer architecture

**Observed path [V]:**
1. Homepage: mission → "Get a Coach" (→ `/book`).
2. Same page, later: "What are you building?" → *Companies* (→ `/companies`) or *Portfolios* (→ `/investors`).
3. `/companies`: pattern headline → "How we work" → Core offering → "Let's Chat" (→ `/book`).
4. `/book`: "LET'S BEGIN WHERE YOU ARE", a cream card with the Heartwood logo that starts at y ≈ 808 on the first viewport; the form itself was not captured (no `<form>` or fields were found by the script, probably an embedded third-party frame).
5. Persistent: "Get Started" (white button, closing block) → `/book`; announcement bar → off-site application (Airtable form).

**[V]** Every primary CTA leads to the same destination, `/book`. Different entry points (hero link, closing button, Companies page button) share one endpoint.
**[V]** There is no price, no package list, no step-by-step description of what happens after the consultation, and no FAQ on the captured pages.
**[I]** Friction points a first-time visitor could meet: not knowing the cost or the engagement length; not seeing evidence of results before booking; the consultation's content and duration are not stated.
**[U]** The booking form fields, validation and confirmation were not inspected, so how much information is requested is unknown.

## 7. Commercial or experimental evidence

- **Not yet researched.** No web search for revenue, traffic, client counts or A/B tests has been run for this dossier. Nothing here supports a claim that the site converts well. The uploaded dossier states that no website conversion data is publicly known; I have not checked that independently.
- Source for any later search: company's Substack and podcast links listed in the footer (`home_desktop.json` → ctas).

## 8. Distinctive mechanisms worth investigating further

1. **One idea per colour field**, each field large and almost empty (heights 951–1,191 px, each holding a short statement of roughly 15–35 words by my count of `fullText`).
2. **A hairline display typeface at very large size** used for the two-line statements, paired with a bold sans for the mission line and a serif for headings.
3. **Headline overlapping a photograph** (SEE CLEARLY / MOVE TOGETHER over the group image).
4. **Audience fork as a question**: "What are you building?" with two outlined buttons.
5. **A single diagram** (nested circles) beside the sentence it illustrates.
6. **Material textures** (sand, malachite marble) instead of photography of people or places.
7. **A single destination for all CTAs** (`/book`).

## 9. Transferable principles for BetterHealth

(These are mechanisms, not styling to copy. All remain hypotheses until tested.)
- **[H]** Give each key idea its own full screen with very little else on it; it may suit a reader who is anxious or overloaded.
- **[H]** Offer an audience fork as a plain question near the end of the homepage (e.g. for private patients and for companies), with two equal buttons, and give each its own page.
- **[H]** Use one purpose-built diagram next to the sentence it explains. For BetterHealth this could show how brain, body and context interact, not circles of "individual / team / culture".
- **[H]** Point every call to action at one enquiry page so the path is predictable.
- **[H]** Use natural-material or abstract imagery to avoid stock clinical imagery, but only where it does not replace real photographs of the clinician and the practice, because a clinical service needs a visible, identifiable person.

## 10. Limitations, open questions, misapplication risks

- **Limits of this dossier:** only six pages captured; nav items and the booking form not captured; REA homepage inspection only; no performance, network or accessibility measurements; no hover or menu states; no hex values were verified against the stylesheet (colours are computed values converted from rgb).
- **Open questions:** What does the booking form ask? Does the hamburger menu list more than the four footer links? Is the "PORTAL" typeface a licensed commercial face or custom? How long does a visitor stay on each large empty field?
- **Misapplication risks for BetterHealth:**
  - Heartwood sells a team-level, relational service with no clinical risk. A clinical practice must state scope, credentials, fees, confidentiality and what a first appointment involves; the page captured states none of these for its own service.
  - Very empty sections and thin all-caps type are weak for older readers and for accessibility (contrast of thin strokes). Test with real users.
  - Poster-like pacing hides information. A patient comparing providers may need facts sooner.
  - The absence of proof on the homepage is a gap, not a strategy to copy. Its effect on conversion is unknown.
  - Do not reuse the logo, the PORTAL face, the dune or marble imagery or any of the copy.
