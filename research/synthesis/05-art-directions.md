# Three art directions for BetterHealth

**Basis:** 12 captured sites (dossiers `../dossiers/`), comparative report (`02-…`), visual specification (`03-…`), playbook (`04-…`).
**Status:** proposals for selection. Nothing has been built. **Everything about their commercial effect is a hypothesis**: no competitor mechanism cited here has experimental evidence behind it (all E1/E2 in the report's grading). Each direction is meant to stand alone; combining them would produce an average and is not recommended.
**Replaces** the earlier draft `../art-directions.md`, which was written before any site had been captured.

Shared constraints (from the spec): physician-led, self-pay, Aarau, German first; one responsible physician shown; fee and first visit described concretely; confidential first contact; real photographs only; no outcome percentages without method; no urgency devices; palette outside the Parsley/Spring/current-BetterHealth family.

---

## A · "The Formulation"

### Concept
The website looks and behaves like the thing BetterHealth produces: a **written clinical formulation**. A visitor learns what the practice does by seeing a document that is structured the way the practice thinks: observation, interpretation, plan, review. The page is the proof of method.

### Visual principles
- Paper ground, near-black ink, **one** ultramarine used only for the action and for emphasis words.
- Hairline rules, numbered sections ("01 Observation"), monospaced labels, margin notes. The decoration is information.
- Diagrams are drawn in 1.5 px strokes, with plain-language labels.
- Almost no photography. Two images only: the physician and the practice room.

### Compositional approach
- 12-column grid with a **3-column left rail** for margin notes (labels, definitions, "why we ask this") in sections that explain method. Body text in cols 4–9; diagram or document component in cols 4–12.
- Section rhythm: label → heading (serif, one italic emphasised phrase) → lead sentence → content. Section padding 96 px.
- **Signature component, "the formulation sheet":** a page-shaped panel (A4 proportion, 1 px rule border, paper-2 ground) showing a fictional, clearly labelled formulation summary with numbered observations, a confidence note per statement ("likely / possible / unclear"), and a short plan. It is shown large in the process section and reused on the approach page.

### Typography (tokens in spec §3.A)
Source Serif 4 light for headings with italic emphasis; IBM Plex Sans for text; IBM Plex Mono for labels, numbers and confidence tags.
Hero H1 at `clamp(44px, 6vw, 80px)`, line-height 1.0, tracking −0.02 em. Mono labels 12 px uppercase.

### Image direction
- Physician: tight, daylight, plain background, looking at camera, 4:5.
- Practice room: wide, uncluttered, one window, no staging, 3:2.
- No gradients, no illustrations of brains. Diagrams are typographic: nodes labelled "sleep", "attention", "stress response", "history", "daily context", connected with lines of varying weight to show strength of the link *(drawn per patient in the example sheet)*.

### Writing style
Dry, exact, courteous. Short sentences. States confidence and limits. Uses "we think", "possible", "unclear" as visible tags. No metaphors for care. (Playbook §3.)

### Homepage narrative (desktop heights are targets)

| # | Section | Component | Approx. height | Content |
|---|---|---|---|---|
| 1 | Hero | C2 | 720 px | H1 "A clearer explanation for symptoms that haven't made sense."; sub; primary + text link; fact strip in mono |
| 2 | 01 Observation | C4 | 760 px | Four recognition entries with the clinical question beneath each; margin note: "Why we start here" |
| 3 | 02 Interpretation | C11 | 880 px | The diagram of linked factors; caption "We look at these together because each can affect the others." |
| 4 | 03 Method | C5 + sheet | 1,100 px | Five steps left, formulation sheet right |
| 5 | 04 Scope | C3 list | 700 px | Six concerns, each with its clinical question |
| 6 | 05 Physician | C7 | 700 px | Portrait, qualifications, what they do in the process |
| 7 | 06 Schedule of fees | C6 | 720 px | Offer card styled as a schedule; inclusions / exclusions columns |
| 8 | 07 Limits and referral | C3 | 520 px | Who it is for, who it is not for, emergencies |
| 9 | 08 Questions | C9 | 900 px | Ten questions in three groups |
| 10 | 09 Contact | C10 | 720 px | Telephone, secure message, four-input form, "what happens next" |
| | | | **≈ 7,700 px** | within the 7,000–9,500 px target |

### Mechanisms drawn from the research
Process as numbered steps with a deliverable mock-up (Biograph, Function); itemised fee and exclusions (Kusnacht, Parsley); accent word in headings (Function, Lanserhof, Chenot); a single explanatory diagram (Heartwood, Spring); a "why we ask" rail adapting Biograph's FAQ approach to hard cases; FAQ for the family member (Kusnacht).

### Commercial rationale (hypothesis)
*Premise:* the practice's value is explanation. A visitor who can see an example of the explanation can judge it before contacting. *Fit:* suits readers who compare providers on substance. *Evidence:* none for this specific pattern; the closest observed is Biograph's dashboard mock-up and Function's step panels (both E1). *Test:* does a visible example sheet increase completed enquiries from qualified visitors compared with a text-only process section?

### Risks and mitigations
- Cold if the writing is cold → keep the physician's portrait and a plain-voiced first paragraph high on the page; test with real readers.
- Looks like a research paper to non-technical readers → keep the sheet's language plain; label it "Example".
- The fictional example may be mistaken for a real patient → the label and a visible "invented for illustration" note.
- Reliance on typography: needs good German typesetting (hyphenation, quotation marks) → `lang="de"`, `hyphens: auto`.

### What it deliberately rejects
Photography of brains or people; coloured gradients; trademarked method names; outcome statistics.

---

## B · "The Quiet Room"

### Concept
The website is what a first conversation should feel like: unhurried, private, and attentive. It does not argue; it makes room. The first thing a visitor should sense is that **nobody will rush them and nobody will find out**.

### Visual principles
- Warm blush ground, aubergine-black ink, plum for the single action.
- One thought per screen. Wide margins, long pauses (160 px between sections).
- Photographs of light and material in the real practice, no faces apart from the physician.
- Type does the emotional work: a large, light serif with an italic voice for the key phrase.

### Compositional approach
- Text column 640 px in columns 2–7; an image or a blank column in 9–12, alternating sides every section.
- Sections are written as prose paragraphs with at most one list on the page.
- A slim **fact line** (one line, small, under the hero) carries the operational facts so the slow pacing never hides the practicalities.
- A sticky action: the header button and a small bottom-right "Call `[number]`" on mobile.
- Reveal motion is limited to a 12 px fade-up and is optional (spec §1.4).

### Typography (tokens in spec §3.B)
Instrument Serif for headings (roman and italic), Instrument Sans for text. H1 `clamp(48px, 7vw, 96px)`, line-height 1.02. Body 19 px / 1.65. Labels uppercase, +0.14 em.

### Image direction (shot list, to be photographed in the practice)
1. Window light on a wall at two times of day (hero candidate).
2. Hands holding a cup or a pen, no face.
3. A plant on a sill; paper and a pen on a table.
4. The entrance without signage readable.
5. A corridor with soft light.
6. The physician, seated, daylight, looking at camera.
All in one colour treatment (warm, low contrast, no filter effects), matching the palette. Do not mix with illustration or stock.

### Writing style
Gentle, second person, plain. Describes what the person may be carrying, then what happens. Allows long sentences when they read naturally; never abstract nouns in stacks. Confidentiality is a full section, in operational terms.

### Homepage narrative

| # | Section | Approx. height | Content |
|---|---|---|---|
| 1 | Hero | 760 px | One sentence, one image of light, primary button, fact line |
| 2 | "What you may be carrying" | 820 px | Recognition in a short paragraph, not a list |
| 3 | "What we do differently" | 760 px | Reframe: explanation first; no "root cause" promise |
| 4 | "A first conversation" | 980 px | Four short paragraphs (talk, gather, formulate, plan) plus the review line |
| 5 | The physician | 760 px | Portrait, name, qualifications, one paragraph in their voice |
| 6 | Fees | 600 px | A quiet table: first assessment, what it includes, what it does not |
| 7 | "Privacy, in practice" | 820 px | A large statement and five operational points |
| 8 | Questions | 880 px | Ten questions |
| 9 | "Start with a conversation" | 760 px | Telephone, message, form |
| | | **≈ 7,200 px** | |

### Mechanisms drawn from the research
Face-free, warm imagery and anonymity statements (Kusnacht); one idea per field and slow pacing (Heartwood, Lanserhof, with the caution that this can hide information); no-form first contact (Kusnacht, Chenot) with data-protection review; family-member FAQ (Kusnacht); published fee with exclusions (Kusnacht, Parsley).

### Commercial rationale (hypothesis)
*Premise:* for stigmatised or sensitive presentations, privacy and pacing are the main barriers to contacting a practice. *Fit:* readers who have been dismissed or who fear exposure. *Evidence:* only the observed prominence of privacy at the most expensive psychiatric site (Kusnacht, E1). *Test:* completed enquiries and quality of enquiries with a privacy-led page versus a method-led page.

### Risks and mitigations
- Too slow, too empty: some visitors compare providers on facts → fact line, sticky action, short page index at the top of long sections.
- Reads as generic "wellness" → keep the language clinical in the fee, process and limits sections; no spa vocabulary.
- Photography quality is decisive: poor pictures will ruin it → commission a photographer; if not possible, use type and colour alone and no pictures.
- The abundant whitespace lowers density for older readers' search for facts → test with 55+ participants.

### What it deliberately rejects
Dense feature lists; icon grids; stock imagery; any technology-as-product framing.

---

## C · "The System"

### Concept
BetterHealth treats the brain as part of a living system (body, behaviour, context). The site makes that system **visible and explorable**: a single clinical map is the interface. It signals a precision-medicine practice without using equipment as the product.

### Visual principles
- Dark graphite ground for the map and key explanation; bone-coloured light sections for reading.
- One ice-blue for strokes and the action.
- Monospaced data labels; calm, precise motion that explains, not decorates (lines draw once; no looping).
- Information density is higher than in A or B.

### Compositional approach
- Hero: left text, right a **clinical map** (1,200 × 800 px at 1440 wide): four labelled layers (*history*, *brain function*, *physiology*, *daily context*), with a few named relationships drawn between them. Hovering or tapping a layer reveals one sentence and a link ("what we assess here").
- **Accessible fallback:** the same content as a visible list under the map and for keyboard and screen-reader users; the map is never the only way to reach any information.
- Alternating dark and bone sections. Reading sections are single-column 680 px.
- The concerns section uses a **graded selector list** (adapted from Lanserhof's focus-area list) but with all items visible, active item enlarged: *sleep that does not restore · attention and focus · persistent anxiety · low mood · stress and exhaustion · complex presentations*.

### Typography (tokens in spec §3.C)
Bricolage Grotesque 500 for headings (tight, −0.03 em), Hanken Grotesk for text, JetBrains Mono for labels. H1 `clamp(40px, 5.5vw, 72px)`.

### Image direction
Mostly drawn, not photographed: the map, small linear diagrams, and a few data-like figures that are clearly **explanatory** (not patient data). Photographs limited to the physician and the practice room, treated in a cool tone to sit on the dark ground. No brain scans, no generic neuron imagery.

### Writing style
Confident and explanatory. States hypotheses as hypotheses. Short paragraphs with named factors. Uses a few defined terms (for example "formulation") and explains each once. No brand-name jargon.

### Homepage narrative

| # | Section | Ground | Approx. height | Content |
|---|---|---|---|---|
| 1 | Hero with map | dark | 820 px | H1, sub, primary button, interactive map |
| 2 | "Four layers, one picture" | dark | 760 px | The four layers with one sentence each and a relationship example |
| 3 | Recognition | bone | 700 px | Four experiences in patient words with the clinical question |
| 4 | Method | bone | 900 px | Five steps; a formulation summary excerpt |
| 5 | Concerns we assess | dark | 860 px | Graded selector list; each item: the clinical question and what assessment includes |
| 6 | Physician | bone | 700 px | Portrait and qualifications |
| 7 | Fees | bone | 700 px | Offer card |
| 8 | Limits and privacy | bone | 640 px | Two columns |
| 9 | Questions | bone | 880 px | Ten questions |
| 10 | Contact | dark | 740 px | Telephone, message, form |
| | | | **≈ 7,700 px** | |

### Mechanisms drawn from the research
A single diagram for a complex model (Heartwood, Spring); a categorised grid of what is assessed (Function, Wild Health) but organised by patient concern, not by test count; dark section for the "pillars" (Biograph); graded selector list (Lanserhof); product-like clarity of a complex service (Spring). The existing BetterHealth site already contains a "clinical map" concept, which this direction carries forward.

### Commercial rationale (hypothesis)
*Premise:* a precision-psychiatry practice benefits from being understood as having a method; a visible model can make that quickly graspable and separate the practice from generic psychiatry sites. *Fit:* analytic, data-comfortable readers. *Evidence:* E1 only (the observed use of diagrams and dark data sections). *Test:* time to first enquiry and enquiry quality with the map versus a static diagram.

### Risks and mitigations
- Overcomplexity; the map becoming the product → limit to four layers; every layer links to a plain page; test comprehension with five first-time visitors.
- **Technology-as-benefit trap** (Biograph, Function, Wild Health counts of tests) → no counts of tests anywhere; tests appear only as answers to a stated clinical question.
- Accessibility of interactive diagrams → keyboard operable, list fallback, no hover-only content.
- Highest build cost (custom SVG, interaction, testing) and a dark ground that can feel clinical-cold → bone sections carry the reading; keep the physician's portrait warm.

### What it deliberately rejects
Counting tests; celebrity or investor-style proof; mood imagery; looping animation.

---

## Choosing

| | A Formulation | B Quiet Room | C System |
|---|---|---|---|
| What it says first | "We explain, and here is how." | "You will not be rushed or exposed." | "There is a method, and you can see it." |
| Strongest reader | Compares providers on substance | Hesitant, privacy-sensitive | Analytic, curious |
| Image dependence | Low | **High** (needs real photographs) | Medium (needs drawn map) |
| Build cost | Low–medium | Low (if photographs exist) | **High** |
| Main risk | Cold | Slow, generic | Overcomplicated |
| Closest observed mechanisms | Biograph, Function, Kusnacht fee | Kusnacht, Heartwood | Heartwood diagram, Spring, Lanserhof list |
| Differs from current BetterHealth site by | layout, palette, type | palette, type, imagery | palette, type, dark ground |

**My reading (hypothesis, not a result):** the practice's stated idea is *explanation*, which A states most directly and at lowest cost. B is the strongest on privacy and depends on photographs that do not yet exist. C is the most distinctive and the most expensive, and risks a technology-as-benefit message. If forced to rank by fit with the positioning in the playbook: **A, then C, then B**. If the practice's main barrier is patients' fear of being identified, B moves first.

**Selection options**
1. Pick one direction as is.
2. Pick one and name up to two **components** from another (for example A with B's fee presentation), without mixing palettes, faces or imagery.
3. Ask for the evidence gaps (commercial search, missing pages, Neko Health and One Medical) to be closed first.

No code will be written until a direction is chosen.
