# drserravalle.com: build state and cutover runbook

Started 12 November 2026. Read `HANDOFF_2026-11-12.md` first for the decision itself.

**Decision recorded 12 November 2026, Niki: the Institute moves by 1 December 2026,**
before the Q1 promotion. Under the agreed rule, that means drserravalle.com must be
able to sell the Q1 programs by 1 December, and the CFBL store stops selling them on
the same day. Never both at once, never mid-promotion.

## The two stores

| | balancedlivingde.com | drserravalle.com |
|---|---|---|
| Store name | Center for Balanced Living | Dr. Niki Serravalle |
| myshopify | (CFBL store) | `jjqgvb-pp.myshopify.com` |
| Plan | | Basic |
| Live theme | `CFBL v2.25 parent group links` | Whisper (Shopify default, untouched) |
| Build theme | | **Horizon, unpublished**, `gid://shopify/OnlineStoreTheme/159294324854` |

The Shopify connector serves one store at a time. Everything in this file marked
**[CFBL]** needs the connector switched back to the CFBL store, which means Niki
re-authorizes.

## What exists on drserravalle.com now (12 Nov)

Nothing below is visible to the public. Pages and articles are hidden, products are
draft, and the theme is unpublished.

- The four Shopify "Example product" listings, which were active and public, are now **draft**.
- Blogs: `essays` (Essays), `make-it-make-sense` (Make It Make Sense), `clinical-notes`
  (Clinical Notes). Comments closed on all three.
- Article metafield definitions `custom.series` (text) and `custom.next_step` (JSON:
  eyebrow, title, text, links `[{label, url}]`).
- 30 articles imported **hidden** (verified 12 Nov: 8 essays, 22 Make It Make Sense, all unpublished, images on the new store's CDN, metafields set), original publish dates kept, tagged `migrated-from-cfbl`:
  8 essays (both series), 22 Make It Make Sense. Source of truth for the import is
  `source/articles_manifest.json`, scraped 12 Nov from the CFBL public storefront.
- Link rewriting in the bodies: practice pages (`/pages/...`) became absolute
  `https://balancedlivingde.com/pages/...` so the posts keep feeding the practice;
  links between moving posts became local (`/blogs/make-it-make-sense/...`).
- Every Make It Make Sense next-step card was recovered from the rendered CFBL page
  and stored in `custom.next_step` with absolute CFBL URLs. The 988 card on Recognizing
  the Signs of Suicide Risk keeps `tel:988` and its "call 911" line.
- Theme build in `theme/` (layout `drs`, stylesheet, 10 sections, 11 templates),
  uploaded to Horizon.
- Pages, hidden (verified 12 Nov): About, Speaking, The Stories We Told, MUSA, Professional Education,
  EMDR Consultation, Clinical Supervision, Continuing Education Policies. Bodies in
  `import/pages.json`. Anything not in the record is marked `[NEEDS NIKI]`.

## Palette: combined (Niki, 12 November 2026)

One palette drawn from all three brand palettes, on every page: Bone #F1E8D8 ground,
Ink #1F1A16 text, Walnut #4A4036 secondary, Ochre #C5A572 hairlines, Deep Ink #2A3530
footer with Cream #EAE2D0 text. The three accents coexist: Cobalt #2B5275 for Make It
Make Sense, Forest #3D5A52 for Professional Education, Oxblood #6E1F23 for Books +
Essays. Fields: Sand, Sage Mist, Parchment. Type systems still differ by section.
This deliberately overrides the Operating Manual's Books + Essays avoid list ("any
CFBL or Institute color") for drserravalle.com. Social assets still follow the manual.

## How the theme decides the visual system

`layout/drs.liquid` sets a body class, and `assets/drs.css` defines each system's
tokens on that class.

| Page | System | Category line |
|---|---|---|
| Home, About, Speaking, Make It Make Sense | `sys-bridge`, navy and sand duotone, Cormorant SC and Lora | Psychologist, author, educator / Make It Make Sense |
| Essays, the book, MUSA (`page.book`, `page.musa`) | `sys-essays`, Bone, Oxblood, DM Serif Display, EB Garamond, drop cap | Books + Essays |
| Professional Education, consultation, supervision, policies, products, Clinical Notes | `sys-edu`, Forest, Sage, Paper, Cormorant SC, Lora, Inter for metadata | Professional Education |

Any block can render in another system by carrying `class="blk sys-essays"`. The book
feature on the home page does this. The rainbow CFBL mark appears nowhere on this
site, per Professional Education's avoid list. The footer carries one practice
cross-link.

The newsletter form tags subscribers `newsletter` plus a list tag by system:
`list-mims`, `list-essays` or `list-institute`. `list-mims` matches the CFBL tag so the
imported list and new signups land in the same segment.

## Before 1 December: Niki only (Shopify admin, drserravalle.com)

1. **Payments.** Settings, Payments: activate Shopify Payments. Without it the Institute
   products cannot sell.
2. **Store name** has a trailing space ("Dr. Niki Serravalle "). It shows at checkout. Settings, General.
3. **Sender email** and domain authentication for drserravalle.com, so Make It Make Sense
   email does not land in spam.
4. **Refund policy.** Settings, Policies. It must say the same thing as the CE
   policies page: full refund at 7 or more days in writing; inside 7 days, one free
   transfer or a refund less 10 percent; none after the program begins.
5. **Customer accounts** and the Whisper theme can stay as they are. Horizon replaces
   Whisper at cutover.
6. Review the hidden pages and the theme preview (Online Store, Themes, Horizon, Preview).

## Before 1 December: Claude

- [x] **Done 12 Nov.** Seven Institute products read from the CFBL admin and recreated
      on drserravalle.com as **draft**, same handles, prices, variants, seat counts and
      inventory settings. Descriptions read back byte-identical to the source.
      Records in `source/institute_products_admin.json`.
- [x] **Done 12 Nov.** No CFBL orders since 15 October, so no Q1 seats were sold and
      nothing stays served from CFBL. **Re-check on 30 November:** any seat sold on CFBL
      before cutover reduces the new product's inventory by one.
- [ ] Confirm with EMDRIA that the approval for Nature-Informed EMDR (3 EMDRIA Credits)
      covers the March 5, 2027 offering, not only the October 2026 one.
- [ ] Not yet on sale: EMDR Basic Training, the single-day Foundations intensive (Mar 20),
      Report Writing. Each needs a price, then a draft product here, not on CFBL.
- [ ] **[CFBL]** Export customers tagged `list-mims` with marketing consent, then import
      into drserravalle.com. Keep the consent column. Never import anyone who did not
      consent.
- [x] Professional Education program rows filled 12 Nov (six rows, CE lines copied from
      the product records). Price and Register appear automatically once products go active.
- [x] Files copied 12 Nov: 281 created, 4 skipped because the products already carry
      them (`source/files_moved.json`). Filenames preserved exactly. Shopify will not
      import a video from its own video CDN as a Video, so 45 reels under 20 MB are
      stored as plain mp4 files. The 11 larger ones (What the Doctor Is Reading films,
      book launch reels, MUSA essay reels) went through a staged upload and are real
      Video files.
- [x] Article-body images repointed 12 Nov: `logosig.png` in five posts and the five
      images in Recognizing the Signs of Suicide Risk now load from this store. No hidden
      article references the CFBL CDN.
- [ ] Move What the Doctor Is Reading from the CFBL Institute page into Clinical Notes
      or a section on Professional Education.
- [x] Menus `drs-main`, `drs-footer-read`, `drs-footer-more` created 12 Nov. `main-menu` is left alone because the live Whisper theme reads it. Header order: Make It Make Sense, Essays, The Book,
      Professional Education, About.
- [ ] Featured image decision: the Santa post's image is a generated clinician
      (`Nano_Banana_2_-_A_female_psychologist...`). The hard rules forbid generated
      clinicians. Replace it before the post goes public on the new site.

- [ ] Two small copy fixes, live on CFBL too:
      *Everyone Is Stressed* ends "Copyright 2026 Center for Balanced Living", which is
      wrong on drserravalle.com. The summary of *The Difference Between Clinical and
      Just Being Hard* ends "Written for real people in the MOT area," which looks
      unintended.
- [ ] Bylines: the four Courtroom essays read "Niki Serravalle", everything else
      "Dr. Niki Serravalle". The essay template hides the byline, so this only shows in
      feeds and admin. Pick one.

- [x] Office portrait used uncropped in the home hero. The shelf signs are Niki's and stay (Niki, 12 Nov).
- [x] Home hero quote is Niki's own published line from the MUSA page (confirmed 12 Nov).

## Cutover day, 1 December (in this order)

1. **drserravalle.com:** set the Institute products active. Publish the hidden pages
   and articles. Publish Horizon (Niki: theme publishing is blocked for the connector).
2. **[CFBL]** Set the CFBL Institute products to draft. Hide, do not delete, the moving
   articles and pages. A Shopify redirect only fires when the old path returns 404.
3. **[CFBL]** Rename the CFBL blog handles (`essays` to `essays-archive`,
   `balanced-living-blog-make-it-make-sense` to `mims-archive`, `clinical-notes` to
   `clinical-notes-archive`). An empty blog still renders, so its index never 404s,
   and the redirect never fires, until the handle changes.
4. **[CFBL]** Import `redirects-writing.csv` and `redirects-institute.csv` (Online
   Store, Navigation, URL Redirects, Import). All targets are absolute drserravalle.com URLs.
5. **[CFBL]** Main menu `main-menu-2026`: remove Writing and most of For Professionals,
   add one link, "Dr. Serravalle", to `https://drserravalle.com`. Keep
   `/pages/niki-serravalle` (team bio) and `/pages/credentials` on CFBL, and add a
   drserravalle.com link to the bio.
6. Spot-check: five old essay and Make It Make Sense URLs, every Institute product URL,
   and the 988 card.
7. **EMDRIA and NBCC.** The provider name stays CFBL Institute. The provider web address
   changes. Send the notice (draft below) the same day.

## Notice to EMDRIA and NBCC (draft, Niki sends)

> Subject: CFBL Institute, change of provider web address
>
> CFBL Institute's program pages and continuing education policies have moved from
> balancedlivingde.com to drserravalle.com, effective December 1, 2026. The provider
> name, administrator, contact email, policies and programs are unchanged. Former
> addresses redirect automatically.
>
> Policies: https://drserravalle.com/pages/policies
> Programs: https://drserravalle.com/pages/professional-education
>
> [Provider number] / Angela Serravalle, PsyD, LPCMH, NCC

Legal name on the signature because this is a credentialing communication.

## Copy conflicts found during the build (decide, then fix CFBL too)

- The CFBL Institute FAQ says a cancellation gets "a transfer or a credit toward a future
  cohort." The published CE policies say otherwise (refund rules above). The new site
  carries only the policies.
- The CFBL consultation page says "EMDRIA approved trainer." Not repeated on the new site
  until confirmed, since EMDR Basic Training is listed as in development.
- The CFBL MUSA page still calls the book "forthcoming." It was published today.

## Cutover moved up, 14 November 2026 (Niki: "shut the other pages down or archive")

Done on drserravalle.com:
- Live theme is `Horizon (SEO)`. Pages and 30 articles are public. Refund policy set by Niki.
- Six Institute products set ACTIVE and published to Online Store: both Foundations
  products, the ADHD differential workshop, the gender-diverse assessment workshop,
  and both EMDR consultation products.
- `nature-informed-emdr` stays DRAFT until EMDRIA approval is confirmed for March 5, 2027.

Still to do on the CFBL store, blocked on Niki re-authorizing the Shopify connector for
balancedlivingde.com:
1. Check CFBL orders since 12 November for the moved products and reduce seats here if any sold.
2. Set the six matching CFBL products to draft (leave Nature-Informed EMDR until the
   EMDRIA question is answered).
3. Hide the moved pages and articles, rename the three blog handles, import both redirect CSVs.
4. Swap the CFBL main menu to one "Dr. Serravalle" link.
Until step 2 is done the same seats are for sale on both sites.

## CFBL side completed, 14 November 2026

No CFBL orders since 21 September, so no seats to reconcile.

- 50 redirects created with `urlRedirectCreate` (both CSVs, minus `/blogs/clinical-notes`).
  `/products/nature-informed-emdr` and its landing page point to
  `https://drserravalle.com/pages/workshops` until the product there goes active.
- Seven CFBL Institute products set to DRAFT.
- Eleven pages hidden: cfbl-institute, professional-clinical-trainings, courses-certification,
  consultation, clinical-supervision, cfbl-institute-policies, the Nature-Informed EMDR and
  Foundations landing pages, musa-writing, the-stories-we-told, publications.
- 22 Make It Make Sense articles and 8 essays hidden. Blog handles renamed to
  `mims-archive` and `essays-archive`. Clinical Notes left alone (one unpublished template).
- Menus: `main-menu-2026` is now Therapy, Evaluations, Our Team, Community, Contact Us,
  Dr. Serravalle. `footer` swaps CFBL Institute for a drserravalle.com link.
  `for-professionals` points to drserravalle.com. `about` drops Musa.
- Verified by curl: 16 old addresses land on the right drserravalle.com page with 200.

Draft theme `CFBL v2.26 streamlined` (189965467954), unpublished: home "Choose Your Path"
now Therapy, Psychological Evaluations, Dr. Serravalle; Make It Make Sense feature and
What the Doctor Is Reading shelf disabled. Live theme v2.25 still shows the old path
cards and an empty blog feature until Niki publishes v2.26.

Still open: export `list-mims` subscribers, EMDRIA/NBCC address notice, EMDRIA approval
for March 5, `career-development` page still published, Parenting With Purpose is active
and tagged Wellness Group, "Therapy in Middletown" page wording.

## What the Doctor Is Reading moved, 14 November 2026

Section copied byte for byte from the CFBL live theme into `sections/drs-reading-shelf.liquid`
(35,846 bytes, uploaded by staged upload plus `themeFilesUpsert` with a URL body). Content
is in `source/wtdir/`. It sits last on `page.education.json` in draft theme
`Horizon (reading shelf)` (159378243702). Eyebrow changed to "A reading series for
clinicians"; the "See the full library" button removed. Films still load from the CFBL
store's video CDN, so do not delete those files from the practice store.
Open: the shelf sculpture image shows the rainbow CBL tree, which the Professional
Education avoid list names. Niki's call.
Publish order: `Horizon (reading shelf)` on drserravalle.com first, then
`CFBL v2.26 streamlined` on the practice site.
