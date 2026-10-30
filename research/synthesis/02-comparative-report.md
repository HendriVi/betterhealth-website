# Comparative design and conversion report

**Scope:** the 12 sites with dossiers in `../dossiers/` (Heartwood, Biograph, Kusnacht, Lanserhof, Chenot, Function Health, Wild Health, Parsley Health, Acquisition.com, Gym Launch, Spring Health, Prestige Labs). **Neko Health and One Medical are not included**: both blocked automated capture (Vercel checkpoint; CloudFront 403) and no files were provided.
**Date:** 2026-10-30. Every statement traces to a dossier, and from there to a file in `../evidence/`.

## 0. How to read this report

**Evidence grades** used in the matrix:

| Grade | Meaning |
|---|---|
| **E1** | Observed on the live page (screenshot or computed style). Says the mechanism exists; says nothing about whether it works. |
| **E2** | E1 plus a company-reported metric on the page or in a dossier source (e.g. "92 %"). Not independently verified, usually without method. |
| **E3** | A documented experiment with baseline, measure and method. **None collected so far.** |
| **E4** | Independent third-party data (traffic, revenue, audited results). **None collected so far.** |

**Consequence:** nothing in this report is commercially supported. Every finding is either an observed mechanism (E1) or a company claim (E2). The recommendations below are hypotheses for BetterHealth to test; none is a proven conversion principle. Searching for E3/E4 evidence (including the Metalab/Framer case study for Biograph) is the next research task.

**Not measured anywhere in this study:** conversion rates, bounce, scroll depth, load time, accessibility audits, REA bundle/network analysis.

## 1. Cross-site facts that were measured

These are comparisons of captured data, not interpretations.

### 1.1 Page length and density (desktop, 1440 px wide; `docHeight` in each site's data)

| Site | Page height | Largest heading (desktop) |
|---|---|---|
| Acquisition.com | 3,390 px | 40 px (hero question) |
| Prestige Labs | 4,787 px | 64 px |
| Spring Health | 6,672 px | 54.4 px |
| Lanserhof | 6,666 px | 60 / 69 px (two-voice) |
| Heartwood | 6,696 px | 143.9 px (display face) |
| Wild Health | 7,546 px | 56 px |
| Kusnacht | 8,033 px | 40 px |
| Gym Launch | 8,255 px | 100 px |
| Parsley | 10,757 px | 64 px |
| Function Health | 12,262 px | 80 px |
| Biograph | 13,571 px | 68 px |

The two ultra-premium psychiatric/medical-spa sites with the quietest pages (Kusnacht, Lanserhof) use **smaller** headings (40–69 px) than the product-led sites; the largest type belongs to Heartwood (a hairline display face) and Gym Launch (heavy rounded uppercase). Size alone does not track "premium".

### 1.2 Typography pairings (computed `font-family`)

| Pattern | Sites |
|---|---|
| Light display **serif** heading + grotesque/humanist body | Kusnacht (ltMuseum 300 + Suisse), Parsley (Teodor 300 + Euclid), Function (Financier Display 300 + FT Base), Chenot (Brandon Grotesque caps + Portrait italic accent + Verlag), Heartwood (Spectral + Montserrat + a display face), Lanserhof (Frutiger Serif italic + Neue Frutiger) |
| **Single grotesque**, all headings weight 400, tight negative tracking | Biograph (Aeonik + Apercu; a serif only for one quote), Spring Health (one family, Muoto) |
| Heavy geometric/rounded sans, uppercase | Acquisition.com (Poppins 800), Gym Launch (Rohnrounded Black), Prestige Labs (Barlow Semi Condensed) |
| Neutral geometric sans, mixed | Wild Health (Poppins + Lato) |

Letter-spacing on large headings: **negative** (−0.01 to −0.02 em) at Biograph, Parsley, Function; **positive and uppercase** (0.04–0.10 em) at Kusnacht, Chenot, Lanserhof (the uppercase line), Heartwood.
**Two-voice headline** (a small italic/serif line above or inside a bolder line, or an accent word in italic colour): Lanserhof, Chenot, Function, Heartwood (display + serif). Seen at 4 of 12.

### 1.3 Colour and accent usage

| Site | Dominant ground | Single action colour |
|---|---|---|
| Heartwood | dark green `#12251E` + gold/brown fields | gold `#CF9651` (labels), white button |
| Biograph | black / white / `#F9F9F9` | none (black buttons) |
| Kusnacht | white + warm photography | olive `#686F45` |
| Lanserhof | `#F4F4F5` grey | dark pill `#26282B`; no accent hue |
| Chenot | `#F7F8F9` / `#F7F5F1` | black outlines; no accent hue |
| Function | cream `#FEF9EF` | terracotta `#B05A36` |
| Parsley | cream `#F8F6F2` | deep teal `#284849`, green `#4A786A` |
| Wild Health | navy `#08151F` (dark) | mint `#B2D7C7` |
| Spring Health | cream + deep green `#01382E` | neon mint `#8DFF9D` |
| Acquisition.com | white / navy `#131628` | purple `#6F00FF` |
| Gym Launch | black / white | gold `#A78B21` |
| Prestige Labs | white / black | purple `#2F075F` |

**Observation:** the four sites with a single accent colour reserved for actions (Function, Spring, Acquisition, Kusnacht) all use one pill or one filled shape for it. The two with no accent hue (Lanserhof, Chenot) let photographs carry colour.
**Overlap warning:** BetterHealth's current CSS variables (`--deep:#153533`, `--cream:#fffcf4`, `--sage:#738b7f`, `--aqua:#7bbeb2`) sit in the same family as Parsley (`#284849`, `#F8F6F2`, `#4A786A`, `#6FB29F`) and close to Spring Health's green and cream.

### 1.4 Price and fee visibility

| Visible price on captured pages | Sites |
|---|---|
| Published with scope | Kusnacht (from CHF 117,300/week, 15 inclusions); Biograph (Core $7,500 first year); Function ($365/yr, 160+ tests); Wild Health (Peak $25,000/yr; Elite by enquiry); Parsley ($150/mo or $1,500/yr in-network, $275/mo self-pay, $250 lab review); Chenot (CHF 5,500–7,960 per programme, **unit not stated on captured pages**) |
| Price via eligibility check | Spring Health ("as low as $0 per session", coverage check) |
| Not shown | Heartwood, Lanserhof, Acquisition.com (workshop), Gym Launch (coaching) |

Six of the twelve sites show a service price with its scope (Kusnacht, Biograph, Function, Wild Health, Parsley, Chenot); Spring Health shows a range through a coverage check; Prestige Labs shows product prices; four show none on the captured pages. Where a service price is shown, it is attached to a defined list of inclusions (Kusnacht, Biograph, Wild Health, Parsley, Function). The exception in unit clarity is Chenot, whose captured pages do not say what the CHF figure covers.

### 1.5 First-contact methods

| Method | Sites |
|---|---|
| Phone number in the header | Kusnacht (captured on the homepage), Gym Launch (on every captured page) |
| Messaging apps / call scheduling | Kusnacht (WhatsApp, iMessage), Chenot (WhatsApp, "Schedule a call") |
| Two-field start (email + ZIP) with reason given | Parsley |
| Coverage check as first step | Spring Health, Parsley |
| Long form (7 required inputs) | Chenot |
| Application framing ("Apply…") | Wild Health, Gym Launch, Acquisition.com (qualification call) |
| AI assistant with explicit consent screen | Lanserhof |
| External app/form on another domain | Biograph, Function, Wild Health, Spring Health |

### 1.6 Human presence

Faces dominate the hero or first proof at Parsley, Function, Spring Health (domestic photograph), Acquisition.com and Gym Launch. **No faces** in the first screens at Kusnacht (abstract warm imagery), Lanserhof (architecture/landscape; one clinician image mid-page), Chenot (mostly people in activity, small), Biograph (building, then process photographs). Heartwood uses textures plus one group photograph.

### 1.7 Proof types observed

Counts and rates (Acquisition, Gym Launch, Wild Health, Spring Health, Biograph); named celebrity or executive quotes (Function, Biograph, Wild Health); member videos (Function); press logos (Function, Biograph, Gym Launch); partner institutions (Biograph); award strips (Lanserhof, Chenot); named clinician boards (Function, Wild Health, Parsley); regulator-style disclaimers (Prestige Labs, Acquisition.com); third-party ratings (Gym Launch: Google 4.4 from 120 reviews; Spring Health: 4.8 rating figure).
**Outcome claims with no method on the captured page:** Wild Health (69 %, 47 %, 58 % biomarker changes), Parsley (89 %), Spring Health (92 %, 4.8), Biograph (96 %, 1 in 6, 2 of 3), Chenot (biomarker study, full text email-gated), Gym Launch (revenue figures), Acquisition.com (97.1 % retention, 81 NPS).
**Internal inconsistencies noticed:** Function (160+ tests vs 100+ biomarkers; promotion past its stated expiry), Gym Launch (6,000+ vs 5,000+ gym owners), Acquisition.com ($250m+ vs $200,000,000), Spring Health ("covered" vs "have access").

## 2. Mechanism matrix

*Relevance* = my reading of fit for a small, physician-led, self-pay clinical practice (**High / Medium / Low / Avoid**). It is a judgment, not a result.

| # | Mechanism | Seen at | Purpose (interpretation) | Evidence | Relevance |
|---|---|---|---|---|---|
| 1 | Numbered 3–5 step process shown early, with a mock-up of the deliverable | Biograph, Function, Spring, Parsley (timeline) | Reduce uncertainty about what happens | E1 | **High** |
| 2 | Defined first step with price, scope, duration and credit toward the full programme | Parsley ($250 lab review credited), Biograph (Core), Function | Lower the risk of the first commitment | E1 | **High** |
| 3 | Published fee with itemised inclusions and the exclusions stated | Kusnacht, Parsley, Biograph | Qualify and build trust through transparency | E1 | **High** |
| 4 | No-form first contact (phone, message) | Kusnacht, Chenot | Protect privacy; reduce disclosure burden | E1 | **High** (needs data-protection review) |
| 5 | Minimal-field start with the reason stated | Parsley (email + ZIP) | Reduce friction while explaining need | E1 | **High** |
| 6 | Privacy statement in operational terms (what is collected, where processed, how long kept, health info optional) | Lanserhof (AI assistant page) | Make confidentiality credible | E1 | **High** |
| 7 | "Why, not what" reframe + symptom lists in patient words | Parsley, Heartwood ("behind every problem is a pattern") | Recognise the unexplained | E1 | **High** (avoid "root cause" promise) |
| 8 | Concerns grouped by patient problem, one-line clinical question each | Lanserhof (13 focus areas), Parsley (condition cards) | Self-selection | E1 | **High** |
| 9 | FAQ that answers the hard case (what if something is found; family member) | Biograph, Kusnacht | Objection handling | E1 | **High** |
| 10 | Named clinicians with roles; staff-credential FAQ | Wild Health, Function (board), Parsley | Accountability | E1 | **High** (BetterHealth's clinician must be central) |
| 11 | Audience fork as a plain question with two buttons | Heartwood ("What are you building?"), Spring (individual/business) | Segmentation | E1 | Medium (only if a corporate offer exists) |
| 12 | One diagram carrying a complex idea | Heartwood (nested circles), Spring (Venn) | Compress explanation | E1 | **High** |
| 13 | One accent colour reserved for the action | Function, Spring, Kusnacht, Acquisition | Single, findable action | E1 | **High** |
| 14 | Two-voice heading (soft lead-in + firm subject) / accent word | Lanserhof, Chenot, Function | Hierarchy and skim-readability | E1 | Medium |
| 15 | Face-free, warm, material imagery | Kusnacht, Heartwood | Calm and privacy without showing patients | E1 | Medium (needs a real clinician photo too) |
| 16 | Full-viewport slides, one message each | Lanserhof, Kusnacht | Pacing | E1 | Medium (hides information; test) |
| 17 | Trademarked method name (®) | Chenot | Own a category | E1 | **Avoid** (obscures the clinician's judgment; see §3.6) |
| 18 | Unqualified superlatives / reversal / "root cause: ageing" | Chenot, Wild Health, Parsley, Biograph | Persuasion | E1 | **Avoid** |
| 19 | Outcome percentages without method | Wild, Parsley, Spring, Biograph, Chenot | Proof | E2 | **Avoid** unless fully sourced |
| 20 | Celebrity/executive testimonials | Function, Biograph, Wild | Borrowed authority | E1 | **Avoid** (confidentiality, conduct rules) |
| 21 | Urgency, coupon codes, loyalty currency | Prestige, Gym Launch | Short-term sales | E1 | **Avoid** |
| 22 | Qualification stated openly ("who is the right fit") | Acquisition.com | Self-selection | E1 | **High** if framed as clinical suitability |
| 23 | Evidence gated behind an email form | Chenot | Lead capture | E1 | **Avoid** (conflicts with confidentiality) |
| 24 | Free explanatory material before enquiry | Acquisition, Gym Launch, Function (guides) | Reciprocity | E1 | Medium (ungated) |
| 25 | Third-party review widget with count | Gym Launch | Credibility | E1 | Low (practice size; privacy) |
| 26 | Two-tier price table with top tier unpriced | Wild Health | Qualify by enquiry | E1 | Low |
| 27 | Insurer/coverage block | Parsley, Spring | Answer the "is it covered" gate question | E1 | Low (self-pay), but the principle of answering the cost gate holds |

## 3. Findings by topic

### 3.1 Premium positioning and perceived value
- **Observed:** premium is carried by (a) price shown with a long inclusions list (Kusnacht, Wild Health), (b) photography of place and light (Kusnacht, Lanserhof, Biograph hero), (c) restraint in the interface (single accent, few type styles). The product-led sites (Gym Launch, Prestige, Acquisition) are loud and dense; they do not use these cues.
- **Interpretation:** the sites that charge the most (Kusnacht, Wild Health, Biograph) are not the ones with the largest type or most animation. They state a high price early and list what it covers.
- **Hypothesis for BetterHealth:** perceived value will be driven more by the specificity of what the first assessment contains and who delivers it than by the visual idiom.

### 3.2 Trust and authority
- **Observed:** authority types differ by risk. Procedural (clinical process, urgent-findings protocol, FAQ): Biograph. Institutional (awards, partner hospitals): Lanserhof, Biograph. Personal (named doctors with roles and credentials): Wild Health, Function, Parsley. Operational privacy: Kusnacht, Lanserhof.
- **Interpretation:** a small practice cannot supply the first two at scale; it can supply the last two with high specificity.

### 3.3 Customer-problem recognition
- **Observed:** Parsley ("a doctor who asks why — not just what"; symptom lists including anxiety, brain fog, low mood), Heartwood ("behind every problem is a pattern"), Gym Launch (outcome question), Spring ("Find your therapist. Keep your progress.").
- **Hypothesis:** recognition works best when the page lists the experience in the patient's words and then names the clinical question; the "root cause" frame is attractive but over-promises for psychiatric presentations.

### 3.4 Persuasive communication
- **Observed (Schwartz stage):** most sites assume the visitor is already problem-aware and solution-aware; they compete on differentiation (Dunford): "not an annual physical" (Biograph), "not an event" (Acquisition), "continuity across coverage" (Spring), "root cause" (Parsley), method ownership (Chenot).
- **Observed (Miller):** only Prestige Labs states the customer-as-hero / brand-as-guide frame in its own words.
- **Gap:** no site in the set sells to a visitor who does not yet know their symptoms have a name; this is where BetterHealth's "persistent symptoms" positioning is unusual.

### 3.5 Clinical and scientific credibility
- **Observed:** credibility is claimed in three ways: a named board (Function, Wild), a study (Chenot, email-gated; Function's "1000s of hours of research"), or biomarker percentages (Wild, Spring). In none of the captured pages is a full method (n, period, instrument) shown next to a headline figure.
- **Implication:** a physician-led practice that shows its method, including its limits, would be doing something none of these sites does on the page.

### 3.6 Offer construction and price justification
- **Observed:** price + inclusions lists (Biograph, Wild, Parsley, Kusnacht); price said three ways (Function); credit toward the next step (Parsley); minimal commitment language ("12-month commitment; free 48-hour cancellation": Parsley).
- **Contradiction:** Chenot's trademarked method (®) vs Parsley's descriptive "functional medicine": branding the method increases ownability and reduces comparability. For a clinician whose product is individual judgment, a branded method may work against the message.

### 3.7 Navigation and information architecture
- **Observed:** top-level links: 4–7 (Function 5; Parsley 5; Heartwood 4; Chenot 3 + menu). Audience routes in header or footer at Spring (5 routes), Heartwood (2), Function (employers/practitioners in footer).
- **Observed:** all calls to action converge on one destination at Heartwood (/book) and Spring (one registration URL).

### 3.8 Typography and visual composition
See §1.2 and §1.3. The measured common ground among the premium-medical sites: weight 300–400 headings, tight leading (0.9–1.2) on large sizes, body 16–20.8 px with 1.5–1.6 line-height, one reserved action colour or none.

### 3.9 Image strategy and art direction
Four distinct strategies were observed: (1) real faces and kitchens (Parsley, Spring, Function); (2) architecture and landscape (Lanserhof, Biograph hero, Chenot); (3) face-free material and light (Kusnacht, Heartwood textures); (4) product and event photography (Gym Launch, Prestige, Acquisition). Mixed styles on one page (Chenot) weaken identity.

### 3.10 Calls to action and booking
Verb phrases that name the next step ("Start testing", "Verify insurance", "Check your coverage") appear where price or eligibility is central; relational phrases ("Get in touch", "Let's Chat", "Get Started") appear where the first step is a conversation (Kusnacht, Heartwood). Application language ("Apply for Access") appears where selection is part of the offer (Wild, Gym Launch).

### 3.11 Customer qualification and decision-making
Qualification is explicit at Acquisition.com (revenue threshold, industry fit), Gym Launch ("Qualify for a quick call"), Wild Health ("Apply"), and implicit through price at Kusnacht. Parsley qualifies by state licensure and insurance. None qualifies by clinical suitability, which is what BetterHealth would need.

## 4. Contradictions and why both may work (hypotheses)

| Contradiction | Side A | Side B | Why both may be viable |
|---|---|---|---|
| Price shown vs hidden | Kusnacht, Biograph, Function, Parsley | Heartwood, Lanserhof, Wild Elite | Visible price qualifies buyers who compare; hidden price suits relationship sales or very high ticket. Unknown which works better; no test data. |
| Sparse, slow pages vs long dense pages | Heartwood, Kusnacht, Lanserhof (6.7–8 kpx, little text per screen) | Biograph, Function, Parsley (10.7–13.6 kpx, many sections) | Slow pages suit emotional recognition; long pages suit comparison shopping. |
| Faces vs no faces | Parsley, Spring, Function | Kusnacht, Lanserhof | Faces help consumer healthcare with insurance and volume; face-free imagery protects privacy for stigmatised conditions. |
| Hedged vs absolute claims | Prestige (hedged + disclaimer), Acquisition (disclaimer) | Chenot, Wild, Biograph (absolutes) | Regulated product vs service; likely different regulatory exposure. |
| Method ownership vs plain description | Chenot (®) | Parsley, Spring | Ownable brand vs ease of evaluation. |
| Qualification by selection vs access for all | Wild, Acquisition, Gym Launch | Function, Spring, Parsley | Premium scarcity vs volume access. |

## 5. What applies to a small, physician-led, premium, self-pay practice

**Apply (High relevance):** process as numbered steps with a deliverable mock-up (1); defined first step with price, scope and credit (2); itemised fee with exclusions (3); low-disclosure first contact (4, 5); operational privacy statement (6); problem-first recognition in patient words (7); concerns grouped by patient problem (8); FAQ for hard cases and for the family member (9); named clinician with specific role (10); one explanatory diagram (12); one action colour (13); openly stated suitability (22).

**Adapt carefully (Medium):** two-voice headings (14); face-free imagery together with a real clinician photograph (15); slide-like pacing (16); an audience fork if and only if a corporate offer exists (11); free ungated explanatory material (24).

**Do not use:** trademarked method names (17); unqualified superlatives, reversal or "root cause" promises (18); outcome percentages without full method (19); celebrity testimonials (20); urgency, coupons, loyalty currency (21); email-gated evidence (23); inventing logo walls, awards or review counts.

**Unsupported or unproven in any case:** that any of these mechanisms raises qualified enquiries. All need testing in BetterHealth's own funnel.

## 6. Gaps that limit this report

1. No E3/E4 evidence collected (experiments, revenue, traffic).
2. REA not run: no bundle, network or accessibility data.
3. Key funnel pages not captured: Acquisition (workshop, roadmap), Gym Launch (modal, Skool), Spring (sign-up), Biograph (sign-up), Chenot (programme and booking pages), Parsley (conditions, later sign-up steps).
4. Neko Health and One Medical missing.
5. Mobile layouts were captured as screenshots but not analysed in depth; Lanserhof's mobile page scrolls inside a container and is not fully captured.
6. Hover, menu and form-validation states were not captured for any site.
