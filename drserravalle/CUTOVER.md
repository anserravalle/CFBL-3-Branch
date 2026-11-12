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

- [ ] `Dr_Niki_MUSA.jpg` (office portrait, used as the home hero) shows a shelf sign
      reading "...low-vibin' sketchy-ass energy..." above her shoulder, plus "#Believe" and
      "Be Here Now" signs. The home hero crops them out (waist-up crop, set in the intro
      section). A retouched file is still better before the photo is used anywhere else. Check other photos taken in the office
      for the same sign.

- [ ] Home hero quote is a stand-in from MUSA "Why I Write". Replace with Niki's own
      line about her why for the whole site.

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
