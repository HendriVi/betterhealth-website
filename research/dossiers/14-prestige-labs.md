# 14 · Prestige Labs — https://www.prestigelabs.com

**Group C · Health-adjacent direct-response communication, product presentation, trust, retention, commercialisation**
**Captured:** 2026-10-30 · Chromium (Playwright) 1440×900 and 390×844 · REA not yet run
**Evidence folder:** `../evidence/14-prestigelabs/`

Labels: **[V]** Verified · **[I]** Interpretation · **[H]** Hypothesis · **[U]** Unverified.

Pages captured: `/` (200) · `/page/about-us` · `/product/collagen-powder` · `/contact`.
**Status-code note [V]:** the last three returned **HTTP 404** in the capture, yet each rendered real content (an About page, a product page with price and options, a contact form). The status code is therefore not evidence that the pages are missing; **[U]** the cause (how the storefront serves these routes) was not investigated. The earlier uploaded dossier recorded only a "JavaScript required" message for this site; in a real browser the homepage renders fully, so that earlier limitation does not apply to this capture.
Not captured: shop category pages (links are `/#tag-…` anchors), cart and checkout, FAQ, refund policy, affiliate page, the blog (`blog.prestigelabs.com`), support.

---

## 1. Business model, customer, commercial context

- **[V]** Online store for nutritional supplements: protein, pre-workout, sleep, fat burner, collagen, multivitamins, bundles. Meta description: "Helping you get real fitness and health results with our premium-quality, science-driven vitamins and supplements. You're the hero, we're just the sidekick!"
- **[V]** Prices on the homepage range from $9.99 (Energy+ caffeine capsules) to **$499.99** (Ultimate 2.0 Men's / Women's bundles). Other examples: Prestige Multi + Him $39.99; Sleep $59.99; Strength Booster $69.99; Collagen Powder $49.99; Challenger Stack $299.99; Shred Stack $199.99; Strength Stack $199.99 (`home_desktop.json`).
- **[V]** The product page offers "Subscribe and Save 10 % for 1 month" versus "Purchase just this product"; the homepage promotes "Earn up to $50 Prestige Cash & free shipping — Build your own bundle today". The footer links "Become an Affiliate", "Account Login" and a newsletter ("Join the Prestige Labs community").
- **[V]** Legal entity in the footer: "GLS Labs LLC, 9550 South Eastern Avenue Suite 253, Las Vegas NV 89123".
- **[V]** Relationship to other subjects: the Acquisition.com page says its founders founded Prestige Labs and that it was sold in 2021 (company-reported). Prestige Labs' own pages in this capture do not mention that.
- **[I]** The buyer is a fitness-minded consumer buying repeatedly. Commercial success depends on repeat orders, bundles and subscriptions, not on a single high-value decision.

## 2. Screenshots and page references

| What | File |
|---|---|
| Homepage first viewport | `screens/home_desktop_viewport.png` |
| Homepage full page (4,787 px) | `screens/home_desktop_full.jpg` |
| Homepage mobile (4,483 px) | `screens/home_mobile_full.jpg` |
| About us | `screens/page-about-us_desktop_full.jpg` |
| Product page | `screens/product-collagen-powder_desktop_full.jpg` |
| Contact | `screens/contact_desktop_full.jpg` |

## 3. Measured visual specifications

From `data/home_desktop.json`.

**Typefaces loaded [V]:** **Barlow Semi Condensed** (400–700; headlines), **futura_reg / futura_bold** (product names and body), **Inter** (trust-badge titles), Montserrat 400.

| Role | Face | Size / line-height | Notes |
|---|---|---|---|
| H2 "Endless Support for Every Goal" | Barlow Semi Condensed 700 | 64 px / 120 px | −1.28 px tracking; a 120 px line-height is unusually open for a 64 px heading |
| Sub-headline | Barlow Semi Condensed | 28 px / 42 px | |
| Product names (H3) | futura_bold 700 | 20 px / 28 px | |
| Trust-badge titles (H4) | Inter 700 | 16 px / 18 px | 1.28 px tracking |
| Nav links | | 24 px 700 | |
| Body | futura_reg 400 | 16 px / 24 px | `#212529` |
| Buttons | | 16 px 600 uppercase; 30 px in the large "SHOP BUNDLES" | |

**Mobile [V]:** H2 25 px; product H3 16 px.
**Colour [V]:** **`#2F075F` deep purple** (every button and brand accent) · black and white · `#F2F2F2` and `#F5F5F5` backgrounds · `#212529` body text · **`#007BFF` bright blue** (778 uses: Bootstrap's default link colour, appearing on the cart link and on unstyled anchors). **[I]** The `#212529` and `#007BFF` values together are Bootstrap's default text and link colours, which suggests parts of the site use default styling.
**Layout [V]:** `max-width` 1200 px. Page 4,787 px; the hero carousel images are 2000 × 800 shown at 1440 × 600.
**Components [V, screenshot]:**
- Header: logo, nav (SHOP, ABOUT US, SUPPORT, BLOG) at 24 px bold, a purple "Login" button, a cart count.
- **Promo hero carousel**: a Halloween promotion — "20 % OFF PROTEIN — USE CODE: SPOOKY20", "Oct 28–Nov 1" — with a large orange button and arrows.
- Trust strip of three badges with icons: "Third-Party Certified — For Purity & Quality", "Clinically Dosed Formulas — GMP Certified", "Satisfaction Guaranteed — 30-Day No Hassle Returns".
- "Endless Support for Every Goal" with a row of outlined **filter pills** (Shop all, Best sellers, Bundles, Strength & Recovery Series, Weight Management Series, Health & Wellness Series, Protein Series) plus a purple "Build Your Own Bundle" button, then a **product carousel** (white cards, product photo, name, price, one-line claim).
- Split promo "Smart Savings, Stronger You" beside a black "SHOP BUNDLES" product image; a full-width purple banner with oversized white type "MEET OUR BEST SELLERS" partly hidden behind product jars; a brand-story block with a gym photograph; a black banner "EARN UP TO $50 PRESTIGE CASH & FREE SHIPPING"; a small-print legal footer.

**Imagery [V]:** studio product photography on purple, black or white; one athletic action photograph. The bottles share a purple-and-gold label design that matches the site's palette.

## 4. Art-direction analysis

- **[V]** A consumer-product storefront: large type behind product photography, bold promotional banners, a prominent coupon code.
- **[I]** The purple bottles and purple buttons make the brand recognisable as one colour; the page works as a product shelf.
- **[I]** The oversized white text partially hidden by product images ("MEET OUR BEST SELLERS", "SHOP BUNDLES") adds depth but reduces legibility (letters are cut).
- **[V]** The default-looking blue link colour and 120 px line-height suggest some template-level styling that was not fully customised. **[U]** Whether these are visible to shoppers was not tested.

## 5. Copywriting analysis

Verified copy:
- "Endless Support for Every Goal — Train Harder, Live Healthier, and Transform Your Physique."
- Trust claims: "Third-Party Certified — For Purity & Quality", "Clinically Dosed Formulas — GMP Certified", "Satisfaction Guaranteed — 30-Day No Hassle Returns". The captured text names no certifier.
- Brand story: "Because every hero needs a sidekick… Your goals are our goals, and our intention is that you never stop working towards your full potential."
- About page: "Prestige Labs is a premium line of nutritional supplements that deliver transformative physical and performance results… formulated using only the highest quality ingredients, produced by industry-leading manufacturers in cGMP-certified facilities, and are required to pass rigorous testing and third-party substantiation… Developed by Ph.D. biochemists and experts in health and nutrition".
- Product claims use "support" phrasing: Sleep "Promotes deep, restorative sleep for better recovery and more energy the next day"; Strength Booster "Helps enhance strength, energy, and performance by optimizing hormone levels naturally"; Crush "Supports healthy eating patterns by helping maintain balanced blood sugar, supporting cortisol balance, and promoting a resilient stress response"; EFA Complex "supports hormone health, mood health, and overall reproductive wellness".
- Footer: "*These Statements Have Not Been Evaluated By The Food And Drug Administration. The Products And Information On This Website Are Not Intended To Diagnose, Treat, Cure Or Prevent Any Disease… Please Consult Your Physician."

Analysis:
- **[I] Narrative frame (Donald Miller lens):** "You're the hero, we're just the sidekick!" is a direct use of the customer-as-hero, brand-as-guide structure: the brand states its role and returns the agency to the customer ("if you are willing to put in the effort and do the work, then you deserve the highest level of support").
- **[V] Claims and caveats on the same page:** the benefit language is hedged with "support", "helps", "promotes", and the page carries a standard regulatory disclaimer. Words like "transform", "transformative physical and performance results" and "clinically dosed" appear in marketing copy. **[U]** The captured text does not say which studies underlie "clinically dosed".
- **[V] Trust badges** are generic (certified for purity, GMP, satisfaction guarantee) and unattributed in the text.
- **[V] Retention and value mechanics:** bundles with listed contents and prices; "Build Your Own Bundle"; "Subscribe and Save 10 %"; "Prestige Cash"; free shipping; affiliate programme; email list. These are commercial mechanisms, not claims about health.
- **[V] Voice:** energetic, imperative ("Train Harder"), short slogans, mixed with technical specifics in product lines (e.g. "12.3g hydrolyzed collagen peptides per serving", "150 mg of caffeine per capsule").
- **[V] CTA wording:** "SHOP ALL", "SHOP NOW & CLAIM YOUR 20 % OFF", "SHOP BUNDLES", "BUILD YOUR OWN BUNDLE TODAY", "LEARN MORE ABOUT WHO WE ARE".

## 6. Conversion journey and offer architecture

**Observed path [V]:** promo carousel / filter pills / product cards → product page (price, availability, months, quantity, subtotal, "Subscribe and Save" vs one-time) → cart (`/cart`) → login (`/login`).
- **[V]** The first screen contains a time-limited discount code; the trust strip sits directly under it; products with prices follow.
- **[V]** The contact page offers a form (name, email, subject, message, a captcha-like field), a phone number and an email.
- **[U]** Checkout, shipping costs, subscription terms and the cart behaviour were not inspected.

## 7. Commercial or experimental evidence

- **Not yet researched.** No revenue, customer or conversion data collected. The sale figure mentioned on the Acquisition.com page is company-reported and not checked.

## 8. Distinctive mechanisms worth investigating further

1. **Customer-as-hero framing** stated in the page's own words.
2. **A three-badge trust strip** immediately under the promotional hero.
3. **Bundle architecture** (named bundles with contents and fixed prices; "Build your own bundle").
4. **Subscribe-and-save default option** on the product page.
5. **A store-credit currency** ("Prestige Cash") with free shipping.
6. **Hedged benefit language plus a regulatory disclaimer** on every page.
7. **Series-based filter pills** organising products by goal (Strength & Recovery, Weight Management, Health & Wellness, Protein).

## 9. Transferable principles for BetterHealth

(All **[H]**; this site is the least comparable in the set.)
- Place the practical assurances a patient needs (who reviews you, how confidentiality works, what the first visit is, what it costs) in a short strip near the top, with named sources and not generic badges.
- State the limits of what the service can do in the same visual space as the promise; a regulatory-style disclaimer is not a design feature to copy, but the discipline of pairing a claim with its limit is.
- Use goal-based grouping for the practice's offers (by the problem a patient comes with), not by product.
- Keep the patient as the active party in the story, with the clinician as a guide. The "sidekick" device is a good test of tone, but it should be expressed in sober language.
- Do not use time-limited discounts, coupon codes, loyalty currency or subscription defaults in clinical care.

## 10. Limitations, open questions, misapplication risks

- **Limits:** no REA run; only four pages; three returned a 404 status although they rendered; no checkout, cart or subscription terms; filter pills and carousel not operated; no hover states; the badges' certifier unknown; mobile layout not examined beyond the capture.
- **Open questions:** Why do those routes return 404? Which body certifies the products? What are the subscription terms? Is the brand's current owner the same as the founders cited by Acquisition.com?
- **Misapplication risks for BetterHealth:**
  - A supplement store sells a repeat consumer product at low prices; a clinical practice sells judgment and continuity. Almost none of the commercial mechanics (coupons, bundles, loyalty cash, subscription defaults) are appropriate.
  - Product copy that links supplements to "mood health", "cortisol balance" and "stress response" is a regulatory-style claim area; a psychiatric practice should not echo this language or suggest that over-the-counter products treat mental-health conditions.
  - Promotional urgency ("Oct 28–Nov 1", "SPOOKY20") would undermine trust in a confidential medical service.
  - Overlapping oversized type and default-styled links lower legibility and polish; BetterHealth's quality bar must be higher.
