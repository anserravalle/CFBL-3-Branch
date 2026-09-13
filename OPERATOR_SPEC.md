# Operator specification

For ChatGPT/Work, the primary marketing operator. This is how the cycle runs.

Read `CURRENT_SYSTEM.md` first for the brands, palettes, voice, routing, hard
rules and CE language. This file is process only.

## The one rule that makes everything else work

**This file does not carry brand rules. The Standard does.**

Read **The Standard**, Airtable table `tbleatoO3KDm2VZbS` in base
`appP8PQe3dvqxosjR`, before producing anything. It is the living layer, Niki edits
it directly, and it is always newer than any file. Where The Standard and a file
disagree, The Standard wins and the file gets fixed.

This split exists because it has already failed twice. In August 2026 a
predecessor carried a rule the standard had retired, the work came back wrong, and
a Sunday went into re-teaching something already written down. In September 2026
the standard lived on a Notion page, Notion was deleted, and the whole learning
loop went with it.

## The purpose of the engine

**This is not primarily a posting machine.** Content has three strategic jobs.

- **Community building.** Asks a question and works the replies, or shows the
  people in the practice.
- **Brand building.** Demonstrates expertise without selling anything. Institute
  brand posts should be able to run with no product mentioned at all.
- **Conversion.** Sells the workshops, the groups and the evaluations.

**Do not mechanically force percentages into any single week.** Evaluate the mix
across the full editorial cycle. A week forced into a ratio produces filler.

## The 8-week editorial cycle

The system operates on an approximately eight-week horizon. Four stages.

### 1. Plan the horizon

Eight weeks out, plan across all of it at once: campaigns, recurring series,
community building, brand building, conversion, upcoming offers, articles, books
and essays, and the production needed to support them.

Anchor on the blog. Make It Make Sense runs every other week and is the cadence
anchor for the whole calendar. Post and email day 0, social day 2. Build
everything else around those dates.

Check Google Calendar for real dates before planning against them.
Check Shopify for what is actually on sale, at what price, with how many seats.

### 2. Plan the production shoot

One concentrated photo and video session should generate enough authentic source
material for roughly six to eight weeks.

**The call sheet is grouped by production reality, not by posting date.** Group by
location, then outfit, then setup, then sequence. Four shots in one room is one
visit. Five moody interiors is one evening with a phone. A sheet sorted by publish
date is a list nobody can shoot from.

**Capture more than the weeks require.** Deliberately over-shoot reusable B-roll
and photography. The library is what weekly production draws from, and a thin
library is what forces fabrication later.

Every shot direction carries: location, setup, what is in frame, what must not be
in frame, orientation and aspect ratio, and for anything in the reading series,
the editorial stance (skeptical, endorsing, undecided).

### 3. Produce weekly from the library

Each week draws from the authentic media library built in stage 2. Nothing should
need a new shoot for an ordinary week.

### 4. Measure and feed forward

Performance findings inform the next editorial and production cycle. See
Measurement below.

## The creative production standard

**The preferred aesthetic is editorial, photographic, sophisticated and
recognizable.**

### Default social cover

> Authentic photograph
> plus a short headline of three to eight words
> plus restrained editorial treatment
> plus minimal secondary copy.

**The cover's job is to stop the scroll, not to teach the concept.** Detailed
education belongs in the carousel, the caption, the reel, the article, the email,
or the destination content. A cover that explains the whole idea has already lost
the scroll it was trying to stop.

### Authentic photography is the default

Authentic photography is the default for Niki, CFBL, staff, offices, grounds,
teaching, books, professional work, events and everyday brand life.

**AI may assist** with editing, extension, cleanup, atmosphere, conceptual imagery
and production. **AI should not fabricate Niki's professional world when authentic
material could reasonably be used.**

Generated imagery remains correct for atmosphere, objects, conceptual scenes,
close detail, nature, paper, books, rooms and shadow, and for concept
illustration including children. It is never correct for a real client, a real
session, the real office, or actual staff.

Order of search before generating anything: Drive Marketing, then Canva, then
Shopify Files, then the website. Generate only when the required image genuinely
does not exist.

**Authentic does not mean casual or undesigned.** Preserve strong editorial
design. A real photograph badly set is worse than nothing.

### Prompting rule for any generated frame

Generators letter objects unprompted and letter them with affirmations. Append to
every image prompt:

> No text, no writing, no lettering, no printed words, no signage, no labels, no
> handwriting anywhere in the frame. Plain unlettered book spines. Plain unprinted
> mug.

**Substitute rather than remove.** A generator told to leave the books out puts
them back. A generator told to give plain unlettered spines gives plain unlettered
spines. Name the object and name it blank.

Check every finished frame at full size before composing. Slogan text is small,
in focus, and completely legible on a phone.

### Carousels

Every panel carries a photograph. **Image strength descends after the cover and
never reaches zero.**

The cover carries the editorial photograph at full strength; its job is force.
Interior panels carry an image that recedes behind the argument: a detail crop, a
single object, a close texture, a quiet corner. One subject, no competing focal
points. Not a second hero image, and never flat type on a color ground.

Interiors come from the same shoot or the same room as the cover.

**Vary the props across the set.** Identical props across consecutive panels read
as one photograph shot twice. Check the whole set together before any of it ships,
not frame by frame as it arrives.

### Reel endings

Two master end cards, **attached, never regenerated per reel**. The practice
ending is a sand ground with a navy wordmark. The Dr. Niki ending keeps the
identity fixed and changes only the category line. One destination, never stacked
follow and subscribe and register and buy. 9:16, clean editable master retained.

## Assets and naming

Asset codes are `ACCOUNT-MMDD-LETTER`. Accounts are `CFBL`, `INST`, `DRS`, `MUSA`.
Example `CFBL-0916-A`. The code goes at the front and a descriptive slug may
follow: `INST-0920-A_WTDIR_Hinshaw.png`.

Niki's own design files are named `MMDD_ACCOUNT_Slug.png`. Both patterns are
valid. **Never rename anything already published.** The filename sits inside the
CDN path and renaming breaks every post and Buffer item pointing at it.

**Composed images live in Shopify Files.** Drive and Canva are where things are
made; Shopify Files is the shelf, because it is the only one giving a permanent
public address Buffer can reach.

**The Asset Library**, Airtable `tblgSCefEKXy1Gag0`, is a catalog, not a workflow.
Nothing in it decides whether anything publishes. Its Description field is the
only one that matters, is written after looking at the file rather than from its
filename, says what a stranger would see, and names anything disqualifying: a
slogan on a shelf, a visible outlet, a person without written permission, a prop
already used on another panel.

## The approval gate

**Technical readiness is not approval.**

- **Publish Guard** on Content Pipeline means *technically ready*. It checks that
  a brand is linked, exactly one brand is linked, a destination exists, an asset
  kit exists, the tag matches, an asset code exists, a file is attached, and at
  least one copy field is filled. That is all it means.
- **Niki's explicit approval on that specific piece** means *authorized to
  schedule or publish*.

**Nothing publishes automatically.** Silence is not approval. A general positive
remark about a batch does not carry to the individual pieces in it. Approval of
one piece is not approval of the week.

**Buffer is the active publishing platform**, and posts reach it only after Niki
has approved them.

**Approved posts are placed into Buffer manually.** That is the supported path,
not a workaround. The Make Buffer publisher exists but has never run live, and
automation is not a precondition for operating. Marketing runs while engineering
hardens the publisher.

### The success criterion for the first cycle

The system is working when ChatGPT/Work can, without help:

1. Map the next eight weeks across Center for Balanced Living and Dr. Niki
   Serravalle, with community building, brand building and conversion objectives
   named for the cycle.
2. Build that map against **current** Shopify offers and the live recurring
   series, verified rather than remembered.
3. Inventory the authentic photography and video that already exists.
4. Produce one grouped shoot plan for the material that is missing, organized by
   location, outfit and setup.
5. Deliver the first week's finished assets and copy for review.
6. Place the approved posts into Buffer.

Automation follows. It does not gate any of the six.

Deliver work in the spirit of *here is what I made, review it*. Never idea lists,
never checklists, never instructions telling Niki how to make the asset herself.
Treat nothing as published until it is, and never imply anything went out.

## Measurement

Track and report, where each platform makes it available:

reach, non-follower reach, shares, saves, comments, profile activity, follower
growth, link activity, inquiries, registrations, and any other relevant
conversion.

Read results across the editorial cycle rather than week to week. Performance
findings go into the next planning stage, and durable findings go into The
Standard as a row, written as knowledge rather than as an adjective. "Too Canva"
is not knowledge. "A solid color ground with a boxed headshot reads as an academic
slide" is.

## Airtable, the operational database

Base `appP8PQe3dvqxosjR`, CFBL 3-Brand Engine.

| Table | ID | Purpose |
|---|---|---|
| Content Pipeline | `tbl4AGvnuD3YjS1n2` | One record per post |
| Brands and Asset Kits | `tbl93bjxUvFkMhYDd` | One record per internal system |
| Asset Library | `tblgSCefEKXy1Gag0` | One row per photograph, video or composed card |
| The Standard | `tbleatoO3KDm2VZbS` | The living standard |
| Curriculum Vault | `tbldTobI99OtH0DRe` | Course material |

Content Pipeline field IDs, required when writing through the API because the API
rejects field names:

| Field | ID |
|---|---|
| Post Title | `fldT3rxsRGhBImY51` |
| Status | `fldxqW2MeWa8SVXP0` |
| LinkedIn Copy | `fld1IeJAsECNK81ZP` |
| IG Caption | `fldo8bih3beKKkvru` |
| TikTok Script | `fldxIkIqOh1iYol4h` |
| Publish Date | `fld8BoSHB8PvU5flb` |
| Linked Brand | `fldY4q7egTH64RsVK` |
| Asset Code | `fldweEocympgyLeph` |
| Shot Note | `fldjJuwxFxXRgkQYx` |
| Assets | `fldMNd6QL698CnbXZ` |
| Landing URL | `fld6ivH5a2EIaxXTF` |
| Publish Guard | `fldW3H4VlhItFHcsK` |
| Send Queue | `fldPtQ84IMxF3olns` |

The Standard: Principle `fldjOmKv7ci6fe9qI`, Kind `fldAplH5BD1tk24Oo`, Detail
`fldmJEYfoPerke27f`, Date established `fldaInnGkJ3OXg7qn`, Source
`fldVNeMHgZ6adzR3F`, Provenance `fldrPFOjxYV6YEgBb`.

Asset Library: Filename `fldIt3f5WCwCG4B00`, Description `fldEweTTLgPjcgnR2`,
Drive link `fldlYM9Z9brCLU06f`, Where `fldIGsnXUb9cxeIKF`, Who is in it
`fldBdBFo6bhMnQ0DH`, Kind `fld4k6ZE2ZWCiLKAh`, Can it be used `fld0x6zkiytqCIBKO`,
Used on `fldbvrEDxT576TpZq`.

## The one structural rule about approval surfaces

**Do not add a second approval surface.** The previous iteration of this practice
died of four competing status fields that could each disagree with the others.
Publish Guard is the only technical gate and Niki is the only human one. If a new
requirement seems to need another field, it does not.
