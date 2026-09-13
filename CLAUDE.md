# CFBL 3-Brand Marketing and Curriculum Engine

This file is the durable record of the system. A conversation ends. This does not.
Read it before doing anything, and update it when a decision changes.

The Airtable base is the operational record: records, copy, shot notes, and
publish state all live there and are not at risk when a session ends. What lives
here instead is the reasoning. Why MUSA cannot say register. Why the publish
decision is a formula and not a checkbox. Why the reading series went to the
Institute. That reasoning is the part that gets lost, and losing it is how a
system gets rebuilt wrong six months later.

## The stack

Airtable holds the data. Make.com moves it. One Shopify account carries all three
brands and is the source of record for products, articles, and newsletters.
Buffer publishes to Instagram and LinkedIn.

Shopify is the source of record. Airtable is derived. When the two disagree,
Shopify is right.

## Where the standard actually lives

The `cfbl-marketing` skill is explicit that **it does not carry brand rules and
this file must not pretend to either**. Rules that change need to live somewhere
Niki edits directly, or they go stale and the work comes back wrong.

That home used to be the Notion page Marketing & Content Engine. **Notion was
emptied and deleted, confirmed by Niki on 2026-09-10.** The page is gone and with
it the accumulated what-not-to-repeat log, the visual standard and the learning
loop. One fragment survived only because the skill file happened to quote it as a
cautionary example.

**The living standard is now `tbleatoO3KDm2VZbS`, The Standard, in this base.**
Read it before producing anything. If it and this file disagree, The Standard
wins, then fix this file. Seeded 2026-09-10 with sixteen principles recovered from
the three sources that outlived Notion: the skill file, the operations connector
code, and the alt text on Niki's own design files in Shopify.

The split is deliberate. Durable architecture lives here, in a repo, under version
control. Anything that changes lives in The Standard, in Airtable, where she
already works. A file she does not edit is a file that will be wrong within a
month.

**The skill was rewritten against Airtable on 2026-09-10** and now lives in this
repo at `.claude/skills/cfbl-marketing/`, with references for allocation,
production, the asset library, and Airtable state. The process rules were kept,
the Notion substrate was replaced, and the CE claims were corrected against the
store.

The account-level synced copies are still installed and still point at Notion.
`cfbl-marketing`, `cfbl-content-creator` and `cfbl-weekly-marketing` all need
deleting from Niki's Claude skill settings, which only she can do. Until then the
stale ones can still fire, and two of them are retired by their own successor.

The skill also mandates process this build does not yet implement: founder
presence at least once a week; at least half conversational CTAs; roughly three
parts value to one part promotion, counted not estimated; one lighthearted post
not landing the same day as a heavy clinical piece; layout varies from the prior
cycle within each brand; and the ask list goes somewhere dated and owned rather
than into chat.

**Every one of those came from the 2026-08-16 snapshot and none has been
reconfirmed since.** Treat them as provisional. The Sunday-to-Saturday week came
from the same batch and Niki retired it on 2026-09-10, which is reason to check
the rest rather than assume them.

**The cadence anchor is the blog, not the calendar week.** It runs every other
week. Post and email on day 0, social on day 2. Build the schedule around those
dates.

**Two genuine conflicts to resolve, not to quietly pick a side on.**

The skill says none of the connected tools publish, posting stays with Niki, and
nothing is finished without her explicit yes on that specific piece. This build
has an auto-publishing Buffer scenario and a Publish Guard designed to remove
approval fields. Those cannot both be right.

The skill delivers to Metricool as a bulk CSV. This build delivers to Buffer.

## The mark

**The rainbow tree is the practice's founding symbol. It is never a palette
question and it is never removed.**

Eight years old. On the building, the car, the signage, the logo. The spectrum is
inclusion and community, which is the foundation the practice was built on.

On 2026-09-10 this system called it decoration carrying no information and
proposed recoloring it to the Institute greens. That was wrong on its own terms.
The test is whether an element carries information, and this one carries the most
important thing the practice communicates. Do not propose removing it, muting it,
or reducing it to brand colors, and do not treat it as a differentiation problem:
the practice predates the market's version of it.

**The CBL Brand Guide sets a minimum size of 2 inches, 200 pixels.** The guide
therefore already concedes the mark does not work small. A reduced version for
profile circles and favicons is not a deviation from the guide, it is the thing
the guide implies is needed and does not yet exist.

The guide states the meaning directly: unity, inclusivity, and the
interconnectedness of mind, body and spirit. Clear space is the width of the C
from the logotype, and half the height of the o between mark and name. A
horizontal secondary lockup exists and the guide says to use it only when
necessary.

The mark belongs to Center for Balanced Living. **Professional Education's avoid
list names the rainbow CFBL logo directly**, so the CFBL Institute logo drafted on
2026-09-10 sits against the manual. That is Niki's call, not this file's, but it
should be a decision rather than an oversight.

The brand palettes below sit around the mark. They do not replace it.

## Two public brands, three internal visual systems

**The governing document is the Brand + Marketing Operating Manual, v1.0, August
2026, approved by Niki.** It is in her Canva as
`Dr_Niki_Serravalle_Brand_Marketing_Operating_Manual.docx`. Its source foundation
is the CFBL Brand Kit Master. Confirmed current 2026-09-10. It outranks this file,
the skill, and The Standard.

Its non-negotiable premise, in its own words: the public does not need to learn a
family tree of sub-brands. It needs two clear destinations. **Center for Balanced
Living** for the practice, and **Dr. Niki Serravalle** for authority, education,
writing, speaking and books. CFBL Institute and MUSA are internal design languages
and product imprints. They do not compete for attention as equal public
identities.

Its closing rule: if a person must understand the brand architecture before they
can understand the content, the content is not ready.

**Correction, 2026-09-10.** This file previously described three co-equal brands
with three print traditions. That was wrong. The manual lists "third-brand
explanation" under Stop, and its AI section says explicitly not to treat CFBL
Institute or MUSA as equal public identities. The internal systems are real and
worth preserving; they are just never the signature.

| Internal system | Signs as | Category line | Account |
|---|---|---|---|
| CFBL Clinical | Center for Balanced Living | Trauma-informed therapy and psychological assessment | @centerforbalancedliving |
| Core Dr. Niki (bridge) | Dr. Niki Serravalle | Make It Make Sense | @drserravalle |
| Professional Education | Dr. Niki Serravalle | Professional Education | @drserravalle |
| Books + Essays | Dr. Niki Serravalle | Books + Essays | @drserravalle |

The public brand leads and is the largest identity on the asset. The category line
sits underneath. One category line, never a list of programs. MUSA may appear as a
subtle imprint on Books + Essays; it is never the identity.

Three systems share restraint, generous whitespace, clean alignment, limited
accents and serious typography. CFBL Clinical and Professional Education share
Cormorant SC as a family signature. **Books + Essays breaks from that family on
purpose** so the writing reads as an independent credential.

**CFBL Clinical.** Editorial, a well-made magazine feature. Open with a specific
human moment, then the idea. Photography carries the post. Asymmetric, generous
whitespace. Warm, human, credible, clinically accurate without a jargon wall.
Palette Cobalt Blue #2B5275, Ocean and Sky Blue #4E9FBF, Sand #EED9C5, #9D654E,
Warm Gray #3D2D29. Cormorant SC headlines, Montserrat body. Default signature is a
sand field, a navy headline, one graphic accent. Carries the rainbow logo. Avoid
busy patterns, neon, high saturation, harsh gradients, cartoons, long all-caps
lines, or more than one headline hierarchy.

**Core Dr. Niki, the bridge.** Public-facing psychology explanation and Make It
Make Sense. It borrows rather than owning a palette, which is why published Make
It Make Sense cards read in navy and sand duotone. It must not read as the
practice's intake voice or as either owned system on the same account.

**Professional Education.** Scholarly, a serious field guide, **photography led**.
Lead with the mechanism or the finding, not with the reader. Name the evidence
base. Palette Forest #3D5A52, Sage #6F8F7A, Sage Mist #B8C9BC, Soft Sky #C2D7E9,
Cream #EAE2D0, Paper #F0EAE0, Deep Ink #2A3530. Cormorant SC headlines, Lora body,
Inter or Source Sans Pro for metadata only. Imagery is assessment materials,
teaching context, clinical concepts, restrained natural detail. No wellness
imagery. **Avoid parent-brand navy or terracotta as primary fields, the rainbow
CFBL logo, decorative botanicals, spa gradients, and parent-brand appointment
language.**

The layout-led version of this system, plates and figure numbers and ruled tables
without photography, was retired on 2026-08-16 when photography-led work
outperformed it. A predecessor skill carried the stale rule, the work came back
wrong, and Niki spent a Sunday re-teaching something she had written down. Do not
restate it.

**Books + Essays.** Literary, first person, analytical, direct. One idea per
piece. Trust the reader to finish the thought. Never explain the piece. Palette
Bone #F1E8D8, Parchment #EDE0C8, **Oxblood #6E1F23**, Ochre #C5A572, Walnut
#4A4036, Ink #1F1A16. **DM Serif Display** titles and drop caps, **EB Garamond**
body. Editorial variety inside a locked system, pull quotes with hairlines,
generous reading measure. Photography led, image-oblique, **never image-absent**.
**Avoid Cormorant, any CFBL or Institute color, decorative botanicals, women
journaling, coffee-and-journal flat lays, credentials above the essay title, pure
black, and marketing-heavy CTAs.**

Oxblood was recorded here as #5A0C11 until 2026-09-10. Wrong color. The
type-led, image-sparse version of this system was retired around 2026-08-11 and
had reached a live shot note before being corrected.

A bare link to a full essay is continuation, not a call to action, the way a
magazine runs an excerpt and says where the rest lives. The promotional framing
around it is what is forbidden. On LinkedIn write the excerpt long.

**Two registers live inside this one system and they are not interchangeable.**
The book is interior and oblique. The essays are direct, argued, addressed to a
reader in pain, and useful in a way the book deliberately is not. So a post
carrying an essay may say something a reader can act on. A post carrying a book
excerpt may not. "Never explain the piece" governs the framing around the work,
not the prose inside it.

Established 2026-09-10 by reading what actually shipped. **The Distance Between
Us ran as a four-part series in June 2026** on Shopify blog
`gid://shopify/Blog/120677892402`, Essays, Books & Other Publications. Parts one
and two sit with the person who needed distance, three and four with the person
who was left. Handles `family-estrangement-series`, `family-estrangement-part-2`,
`the-distance-between-us-part-3`, `relationship-repair-distance-us-4`.

Until that read, this system was being run as if the whole category were the
book, which would have flattened the essays into obliqueness they do not have.
Four thesis lines are already published and need no new writing: "They are living
inside a nervous system that did the best it could with what it had." "Cutting
off contact often works. That is exactly why people do it." "The phone sits
there. Able to ring. Not ringing." "Hold the door open without standing in the
doorway."

What worked in that series was the structure, not the volume: four parts, both
sides of one silence, neither side made the villain. The form is repeatable and
the next one is a subject rather than a word count.

**Letters from the Practice** is Clinical, because an events letter has to be able
to say register.

**Make It Make Sense, MIMS, is the blog.** It routes to Dr. Niki Serravalle on the
bridge treatment, not to the practice, per the manual's routing table. Bimonthly,
every other week, and it is the cadence anchor for the whole calendar. Post and
email day 0, social day 2. Call it Make It Make Sense, never "the blog." The
pipeline through January 2027 is in Content Pipeline, each row prefixed MIMS with
its full SEO package.

Professional Education and Books + Essays share the @drserravalle account. One
system per day on it.

### Routing, from the manual

| If the content is mainly about | Publish from | System |
|---|---|---|
| Therapy, evaluations, groups, the team, local resources, referral access | Center for Balanced Living | CFBL Clinical |
| Public psychology explanation, Make It Make Sense | Dr. Niki Serravalle | Core Dr. Niki bridge |
| Clinician skills, clinical reasoning, CE, consultation, advanced training | Dr. Niki Serravalle | Professional Education |
| Books, essays, author ideas, writing process, reading life | Dr. Niki Serravalle | Books + Essays |
| A topic genuinely serving two audiences | Two tailored assets | Each audience's correct system |

### Reel endings

Two master end cards, and they are **attached, never regenerated per reel**. The
practice ending is a sand ground with a navy wordmark. The Dr. Niki ending keeps
the identity fixed and changes only the category line. Use one destination, never
stack follow and subscribe and register and buy. Keep endings 9:16 and retain a
clean editable master.

## The filename is the state

Inherited from the earlier Notion system and kept deliberately.

A file that is present ships. A file that is absent does not, and nothing needs
to be told so. There is no approval field, because a field can disagree with
reality and a file cannot.

The previous iteration of this practice failed for a specific and documented
reason: three separate status fields, a Stage field with nine options, a
Publication Approval field with five, an Automation Status field with five, and
thirty-three properties. Four competing approval surfaces that could each
disagree with the others. Do not reintroduce a second approval surface. If a new
requirement seems to need one, it does not.

Asset codes are `ACCOUNT-MMDD-LETTER`. Accounts are `CFBL`, `INST`, `DRS`,
`MUSA`. Example: `CFBL-0916-A`.

**The code goes at the front and a descriptive slug may follow it**, so
`INST-0920-A_WTDIR_Hinshaw.png` is correct and preferred. This is not a
compromise, it is the fix for a real defect found on 2026-09-10.

Niki's actual design files are named `MMDD_ACCOUNT_Slug.png`, for example
`0907_DRS_WTDIR_Herman.png`. The old connector's parser, `api/_lib/naming.js` in
`cfbl-operations-connector`, only accepts a stem that BEGINS `CFBL-`, `DRS-` or
`MUSA-` followed by four digits and a letter, and has no `INST` account at all.
Not one of her real files parses. The publisher was matching a convention nothing
was named in, which is a sufficient explanation for that system appearing to do
nothing. Any matcher built here must accept the code as a prefix with arbitrary
text after it, and must know `INST`.

## Airtable

Base `appP8PQe3dvqxosjR`, CFBL 3-Brand Engine.

**Brands and Asset Kits** `tbl93bjxUvFkMhYDd`. One record per brand. Holds the
brand tag key, the asset kit URL, the social destination, the print tradition,
the voice rules, the Buffer profile ids, the Canva brand kit id, the base URL,
the Shopify blog ids, and the tag match token.

| Brand | Record | Tag key | Handle |
|---|---|---|---|
| CFBL Clinical | `reccomuvFnOj8ZRh2` | `cfbl-clinical` | Alpha |
| CFBL Institute | `recMEt3EqbugUYnVp` | `cfbl-institute` | Beta |
| MUSA | `rec6rhNGbkMOzUcof` | `musa` | Beta |

**Content Pipeline** `tbl4AGvnuD3YjS1n2`. One record per post. Linked Brand is a
link to a single Brands record. Field ids that matter when writing through the
API:

| Field | Id |
|---|---|
| Post Title | `fldT3rxsRGhBImY51` |
| Status | `fldxqW2MeWa8SVXP0` |
| Source | `fldZuyv3l8w6ekHPY` |
| Raw Source Text | `fldehDLy9OfsPKVC5` |
| LinkedIn Copy | `fld1IeJAsECNK81ZP` |
| IG Caption | `fldo8bih3beKKkvru` |
| TikTok Script | `fldxIkIqOh1iYol4h` |
| Validation Notes | `fldSzvVtrB3lH8ZBv` |
| Publish Date | `fld8BoSHB8PvU5flb` |
| Linked Brand | `fldY4q7egTH64RsVK` |
| Asset Code | `fldweEocympgyLeph` |
| Shot Note | `fldjJuwxFxXRgkQYx` |
| Assets | `fldMNd6QL698CnbXZ` |
| Landing URL | `fld6ivH5a2EIaxXTF` |
| Publish Guard | `fldW3H4VlhItFHcsK` |
| Send Queue | `fldPtQ84IMxF3olns` |
| Post to LinkedIn | `fldJI37cwjQ3Lx8oV` |
| Post to Instagram | `fldUnD62OhsOrhr9s` |
| Post to TikTok | `fldUJgetjGUWqEt0U` |

**Curriculum Vault** `tbldTobI99OtH0DRe`.

**Asset Library** `tblgSCefEKXy1Gag0`. Added 2026-09-12. One row per photograph,
video or composed card, linked both ways to Content Pipeline. Fields: Filename
`fldIt3f5WCwCG4B00`, Description `fldEweTTLgPjcgnR2`, Drive link
`fldlYM9Z9brCLU06f`, Where `fldIGsnXUb9cxeIKF`, Who is in it `fldBdBFo6bhMnQ0DH`,
Kind `fld4k6ZE2ZWCiLKAh`, State `fld0x6zkiytqCIBKO`, Used on `fldbvrEDxT576TpZq`.

**It exists because a filename is not a description.** Fifteen records sat waiting
on files while a Drive folder held thirty usable images, and nothing connected the
two because the only thing describing an image was its name.
`propertybutterflyonflower.jpeg` sounds like it serves the Nature-Informed EMDR
record and does not: it is a wide roadside garden and that record asks for one
object shot close. Nobody finds that out without opening the file.

Description is the only field that matters and it is written after looking, never
from the filename. It says what a stranger would see, and it names anything
disqualifying: a slogan on a shelf, a visible outlet, a person without written
permission, a prop that already appears on another panel.

**This is a catalog, not a workflow.** Nothing in it decides whether anything
publishes. Publish Guard on Content Pipeline remains the only ship or no-ship
decision, and State here must never be treated as an approval. The lineage this
system replaces died of four competing approval surfaces.

`Where` exists to serve the rule that a carousel's interiors come from the same
room as its cover. `Used on` exists so the same waiting-room photograph does not
quietly become the whole feed.

**Any automated matcher must be scoped to the marketing folders and never allowed
to search Drive generally.** Searching for "Fisher" and "Walker," who are book
authors in the reading series, returns client evaluation files with those
surnames. Found 2026-09-12.

**The Standard** `tbleatoO3KDm2VZbS`. The living standard, replacing the deleted
Notion page. One row per durable principle. Fields: Principle
`fldjOmKv7ci6fe9qI`, Kind `fldAplH5BD1tk24Oo`, Detail `fldmJEYfoPerke27f`, Date
established `fldaInnGkJ3OXg7qn`, Source `fldVNeMHgZ6adzR3F`, Provenance
`fldrPFOjxYV6YEgBb`. Six fields on purpose. The system this replaces died of
thirty-three properties.

Write the knowledge, not the adjective. "Too Canva" is not knowledge. "A solid
color ground with a boxed headshot reads as an academic slide" is.

Send Queue is a formula, not a select. It reads the three venue checkboxes and
only names a platform when the linked brand actually has a profile id for it. A
checkbox alone does not queue a post.

### Publish Guard

The single ship or no-ship decision. Eight nested conditions, eight closing
parens.

```
IF(COUNTA({Linked Brand}) = 0, "BLOCKED - no brand linked",
IF(FIND("|", ARRAYJOIN({Brand Key}, "|")) > 0, "BLOCKED - more than one brand linked",
IF(COUNTA({Destination Route}) = 0, "BLOCKED - no destination",
IF(ARRAYJOIN({Kit ID}, "") = "", "BLOCKED - no asset kit",
IF(AND({Brand Tag Raw} != "", ARRAYJOIN({Brand Key}, "") != {Brand Tag Raw}), "BLOCKED - tag does not match linked brand",
IF({Asset Code} = "", "Not scheduled",
IF({Assets} = BLANK(), "Waiting on " & {Asset Code},
IF(AND({LinkedIn Copy} = "", {IG Caption} = "", {TikTok Script} = ""), "Waiting on copy", "READY"))))))))
```

`COUNTA` on a link field returns 1 no matter how many records are linked, so it
cannot detect two brands on one record. The `FIND("|", ARRAYJOIN(...))` test is
what catches that. A comma separator does not work here because array coercion
supplies no delimiter of its own.

### Tracked links

```
IF(ARRAYJOIN({Profile LinkedIn}, "") = "", "",
IF(AND({Landing URL} = "", ARRAYJOIN({Brand Base URL}, "") = ""), "",
IF({Landing URL} != "", {Landing URL}, ARRAYJOIN({Brand Base URL}, ""))
 & "?utm_source=linkedin&utm_medium=social&utm_campaign=" & ARRAYJOIN({Brand Key}, "")
 & "&utm_content=" & RECORD_ID()))
```

`utm_content` carries the Airtable record id, which makes attribution post-level
rather than campaign-level. That is the whole reason to do it this way.

## Make

Team 2907664.

**6216427, CFBL 1 Shopify Intake.** Active, webhook driven. Shopify pushes to
Make rather than Make polling Shopify, which sidesteps app scopes entirely. Flow:
webhook, then create the Airtable record as Needs Manual Review, then search
Brands by tag, then promote to Draft and link the brand if a brand matched.

Quarantine by default, promote on match. When the brand search returns nothing
the branch halts and the record stays in Needs Manual Review. That halt is the
fail-safe, not a bug. Never make the intake guess a brand.

**6219321, CFBL 2 Article Intake.** On demand only. Routes by Shopify blog id
rather than by tag, which proved correct when a Clinical article carried a stray
`brand:musa` tag: the blog it lives in is a stronger signal than a tag someone
typed. No dedup yet, which is the only reason it is not on a schedule. Do not
schedule it until dedup exists.

**6214861, CFBL 3 Buffer Publisher.** Router with an Instagram, a LinkedIn, and a
TikTok branch, each filtered on Send Queue. Never run live.

Connections: Airtable read only 10987115, CFBL Airtable Write 10993299 which is
the one in use, Buffer 10987143, Shopify 10989870.

## Things already established, do not relitigate

**TikTok cannot publish through this stack.** Make's TikTok app is ads only and
reauthorizing does not change that. Keep writing scripts if they are useful, post
manually. Do not spend another session on this.

**Shopify allows one connection per store in Make.** Creating a new one replaces
the old one. The replacement of 10967062 with 10989870 **did** break Website
Activity Sync, scenario 6203896. Confirmed 2026-09-10 by a Make error email:
scenario validation failed, four problems, account 10967062 not found plus three
references to Notion account 10967276, also gone.

Do not repair it. Read its blueprint first: module 3 carries a filter named
"TEST LOCK - Notion writes disabled" whose condition is `READ_ONLY_TEST` equals
`ENABLE_NOTION_SYNC`, which can never be true. Every Notion write in that scenario
is downstream of that filter, so it has never written anything. Two executions,
two operations, in its whole life. It reads Shopify pages and articles and would
write them into a Notion Website Activity database that is being retired, which is
work CFBL 2 Article Intake already does into Airtable.

It ran daily at 06:00 and failed at initialization, emailing Niki an error every
morning. **Deactivated 2026-09-10, and it did not stay off.** By that evening it
was `isActive` true again with `nextExec` set to 2026-09-12T10:00:00Z, without
having been edited since 2026-09-08. Deactivated a second time and verified
`isActive` false, `nextExec` null.

**Treat a third error email as evidence that something re-enables it, and delete
it at that point rather than deactivating again.** Export the blueprint first.
Until then it stays, because its create-or-update router is the dedup pattern the
article intake still needs.

Keep the blueprint. Its router is the create-or-update dedup pattern that CFBL 2
Article Intake is missing: query the destination by a natural key, then branch on
whether the result count is 1 or 0. Port that rather than inventing one.

**Reauthorizing an OAuth connection replays the original grant.** It does not add
scopes. A new scope needs a new connection.

**Do connections on desktop.** Mobile Safari accepts the OAuth flow, shows the
connection in the dropdown, and never persists it server side. The error is
Status Code Error 400, no access token specified.

**Shopify MCP refuses webhookSubscriptionCreate** and classifies it as data
exfiltration. That is correct behavior. Do not retry it. Create webhooks in the
Shopify admin Notifications UI.

**Airtable modules in Make nest field values under a `record` object.** Sending a
`fields` key returns 422, could not find field fields.

**Airtable search modules reject empty strings for optional parameters.** Sending
an empty `view`, `fields`, or `sort` returns parameter validation failed. Omit
them.

**Shopify numeric ids fail into Airtable text fields even with typecast.** Use
`admin_graphql_api_id`, which is already a string GID.

**`scenarios_run` with a data payload against a webhook scenario reports SUCCESS
and does nothing.** Check the execution log, not the return value.

## Content ratio

Thirty percent marketing, thirty percent brand building, thirty percent community
building. Read across the month, not the week. A single week will not divide
evenly and forcing it produces filler.

Marketing sells the workshops and the evaluations. Brand building demonstrates
expertise without selling anything. Community building asks a question and works
the replies, or shows the people in the practice.

The Institute is not a product catalog. It exists to build a brand clinicians
trust. Institute brand posts should be able to run with no product mentioned at
all.

## Recurring series

**What the Doctor Is Reading.** Already launched in September 2026, not new.
`WTDIR_00_Intro.png` in Shopify Files states the real structure: **a subject a
month, a book a week, a short film on Sunday, twelve subjects from September 2026
to August 2027.** September's subject is trauma across modalities, and week cards
already exist for Herman, van der Kolk, Fisher and Pete Walker. Assigned to the
Institute rather than MUSA: the audience is the Institute audience, and a reading
community has to be able to say join us, which MUSA cannot. Each book gets sorted
into the four tiers.

**Settled 2026-09-10.** The Institute Review was the discarded first name.
`0902_DRS_InstituteReview_intro.png` was made on 2 September as one month, one
theme, one book. Roughly twenty hours later What the Doctor Is Reading superseded
it at a book a week. Nothing was made under the old name afterwards. One series.

Separately, THE CFBL SHELF runs on the practice account, parent-facing, currently
Lisa Damour. Different audience, not a duplicate.

**Do not announce a launch.** On 2026-09-10 a record was built announcing this
series as new, with a monthly cadence and an invented October pick, because the
existing Shopify Files were not read first. Read what already shipped before
building a series.

**Letters from the Practice.** Clinical. Events and community.

**Staff spotlight.** Two questions to all staff twice a year, including
administrative staff, plus a weekly quote with a photograph. Two questions rather
than five because the earlier version died of collection burden, and administrative
staff cannot answer clinician questions. The two:

1. What do you want someone to feel in the first two minutes of contact with us?
2. What is a small part of your job that matters more than it looks like it does?

Quotes run as written, trimmed for length only. The series works because the
quotes sound like the people who said them rather than like the owner. Smoothing
them into one voice turns it into advertising.

Get a written yes from each person before publishing their words and photograph.
Administrative staff feel more pressure to agree than clinicians do.

## The four tiers

The Institute's sorting framework, from the Foundations program design. Every
claim goes in one of four places, and each place licenses a different strength of
statement.

Established. Emerging. Theoretical. Clinical wisdom.

Clinical wisdom is not a dismissal. It is frequently correct and simply has not
been tested yet.

Worked example that is safe to state publicly: HPA axis dysregulation in PTSD is
established, and the dorsal and ventral vagal distinction in polyvagal theory is
not. The polyvagal claim is defensible in public because the pre-read packet
cites Grossman (2023), Biological Psychology.

## Continuing education, stated exactly

Never flatten approved and pending, and never state either from memory. Read the
Shopify product record. Getting this wrong is an ethics problem, not a marketing
one. Verified against Shopify 2026-09-10:

**Foundations of Trauma Therapy**, 18 and 19 September 2026, provides 12 hours of
instruction across two days. This pilot cohort is the delivery that **completes
CFBL Institute's NBCC accreditation application**, and **the hours count toward
your practice rather than your license renewal**. DRAFT status, 14 seats
remaining, not publicly purchasable. It is running and it is closed. Do not
promote it. The material may be used for teaching content and brand posts that do
not reference a cohort or imply enrollment.

**Nature-Informed EMDR** is genuinely **EMDRIA Approved for 3 EMDRIA Credits** and
the product page leads with it. Friday 2 October 2026, 2:00 to 5:00pm Eastern,
live on Zoom. Credit requires live real-time attendance. Prerequisite is
completion of an EMDRIA-Approved Basic EMDR Training. ACTIVE, 99 dollars, 10
seats, tracked, policy DENY.

Two earlier claims were wrong. This file said Foundations was simply NBCC
accreditation pending with no CE claim possible. The skill file said it carries 12
NBCC clock hours with ACEP approval pending. Neither matches the store.

## Hard rules

No em dashes, anywhere, ever. Regular hyphens only.

**American English, anywhere, ever.** This is a Delaware practice writing for an
American audience. Organize, recognize, realize, analyze. Color, behavior, favor.
Center, not centre. License, not licence, which matters most in the continuing
education language: hours count toward practice rather than license renewal.
Catalog, gray, judgment, traveling, canceled, program.

Units follow the same rule. Feet and inches in a shot note, never meters. A
direction reading "phone two meters back" tells an American nothing about where
to stand.

Same scope as the em dash rule: captions, copy, email, documents, shot notes,
Airtable fields, code comments and commit messages. Caught by Niki on 2026-09-13
in a caption one step from publishing, after it had already reached two captions,
two shot notes, an entry in The Standard and six lines of this file. A British
spelling in a caption does not read as a typo. It reads as though someone else
wrote it, which on a personal account is the one thing copy cannot afford.

Never put protected health information or identifiable client information into
any connected system.

Never open or copy the body of a client inquiry email. Only the date and the count
are ever extracted. This is a clinical practice and those are patients.

Never ask for a credential in chat and never accept one there. Tokens go from the
issuing platform directly into the platform that needs them. A token that reaches
a conversation is compromised and must be rotated.

Never read personnel files to find marketing material. Staff HR folders hold
credentialing, evaluations, contracts, and departure records. Headshots come from
Drive, Marketing, Headshot.

No generated clinicians, therapy offices, sessions, or clients. No fabricated
quotes attributed to real staff.

## Open items

Article intake needs dedup before it can go on a schedule.

The Wednesday call sheet is still manual. It should be a scheduled run that
assigns codes, writes shot notes, and emails the sheet out.

The September one was built by hand on 2026-09-10 as a published page at
`https://claude.ai/code/artifact/7876aa18-7119-4178-8129-5b8ece22c5b8`. Fourteen
shots, printable, and it remembers what has been ticked off. **It is grouped by
where she has to stand rather than by publish date**, which is the thing that
makes it a call sheet rather than a schedule: four of the fourteen are in her
office and can be done in one visit, five are moody interiors that are one evening
with a phone. Whatever automates this must keep that grouping. Sorting by date
produces a list nobody can shoot from.

The asset matcher does not exist. Files are attached to records by hand. An
hourly job should match uploaded filenames to Asset Codes and attach them.

**Decided 2026-09-10. Composed images live in Shopify Files.** Drive and Canva
are where things are made; Shopify Files is the shelf. It is the only one of the
three that gives a permanent public address Buffer can reach, Airtable attachment
URLs expire, and Niki's finished work is already there. Nothing to migrate.

Two things found when that was settled. **An app is dumping her Instagram feed
into the same folder**, as `instagram-image-<uuid>.jpg` at 1080x1350 with no alt
text, several a day at 18:01, 22:01 and 23:01. It already outnumbers the design
work and will bury the library. Find it and turn it off. And **three naming
conventions are running at once** in her own files: `WTDIR_wk1_Herman` with no
date, `SPOT_01_Serravalle_quote` numbering a series, `0911_CFBL_ADHDEvals`
date-first. Use date-first going forward. **Never rename what is already
published**: the filename sits inside the CDN path, so renaming breaks every post,
Buffer item and Metricool record pointing at it. The matcher accepts all three
patterns instead.

The Canva composition step is unbuilt. The photograph arrives, the brand kit is
applied, the composed file exports. Canva brand kit ids are in the Brands table.

The earlier Vercel connector, cfbl-operations-connector, still runs an hourly
publish cron and a Monday analytics cron against Notion. Notion has been emptied.
Retire those crons, but **export the Metricool history first**. That connector
already has `listScheduledPosts(blogId, start, end)` and a live Metricool token in
Vercel. Metricool holds every caption the old system published, for blogIds
6760980 Center for Balanced Living and 6760856 Dr Serravalle, with MUSA
interleaved on the Dr Serravalle account. Do not delete the Vercel project, rotate
the token, or cancel Metricool until that history is out.

There is an empty record in Brands and Asset Kits with no name and no tag. It
cannot match anything, but it is debris from an intake test.

**A month became a blog instead of an article.** Shopify carries Letters from
CFBL, handle `newsletter`, with sixteen articles, and alongside it Letters From
The Practice: September 2026, handle
`letters-from-the-practice-september-2026`, with zero. CFBL 2 Article Intake
routes by blog id, so anything published into the new one is invisible to it.
Publish the September letter as an article inside Letters from CFBL and retire
the empty blog. Found 2026-09-10.
