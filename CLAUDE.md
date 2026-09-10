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
this file must not pretend to either**. The living standard is the Notion page
**Marketing & Content Engine** (`3bbe8dd3-03bf-81f9-a509-e5acacd65f88`), which
Niki edits directly and which is therefore always newer than any file. It holds
brand grammar, the visual standard, the learning loop, and what not to repeat.
Read it before producing anything. If it and this file disagree, Notion wins, then
fix this file.

**Status, 2026-09-10: unresolved and blocking.** The Notion MCP connection in this
session returns 401, API token is invalid, on every call. Niki has separately said
she deleted everything in Notion. So either the standard is gone or it is merely
unreachable from here, and those need different responses. Until that is settled,
anything produced is being produced without the standard, and that fact should be
stated rather than papered over.

The skill also mandates process this build does not yet implement: the week runs
**Sunday through Saturday, planned Thursday to Saturday of the week before**; a
blog drags its own dates, post and email on day 0 and social on day 2; founder
presence at least once a week; at least half conversational CTAs; roughly three
parts value to one part promotion, counted not estimated; one lighthearted post
not landing the same day as a heavy clinical piece; layout varies from the prior
cycle within each brand; and the ask list goes out as dated Notion Tasks with an
owner, never as a chat list or a document.

**Two genuine conflicts to resolve, not to quietly pick a side on.**

The skill says none of the connected tools publish, posting stays with Niki, and
nothing is finished without her explicit yes on that specific piece. This build
has an auto-publishing Buffer scenario and a Publish Guard designed to remove
approval fields. Those cannot both be right.

The skill delivers to Metricool as a bulk CSV. This build delivers to Buffer.

## The three brands

Three brands, two social handles, three print traditions. The traditions are the
point. Palette is the weakest possible differentiator and it is the one everyone
uses. Each brand takes its visual grammar from a different tradition of the
printed page, which is why the system cannot be copied with a template swap.

**CFBL Clinical** is editorial. The tradition is a well-made magazine feature.
Photography carries weight, type sits beside it rather than over it, layouts are
asymmetric, whitespace is generous but purposeful. Warm, human, credible. It
should feel like something you would read in a waiting room and keep. Posts to
Handle Alpha. This brand may invite, may say register, may link to a product.

**CFBL Institute** is scholarly. The tradition is a scientific monograph or a
serious field guide, but **photography leads**. The monograph apparatus sits
around the photograph rather than replacing it: a photographic plate with a roman
numeral and a citation caption, a figure number on a diagram, a ruled table only
where the table carries information. Nothing decorative. This serves the mission
directly: adult learners who want a deep dive rather than a certificate should be
able to see the difference before they read a word. Posts to Handle Beta.

**Correction, 2026-09-10.** An earlier version of this file said "plates with
captions and figure numbers, ruled tables, marginal annotation" with no mention of
photography. That is the exact rule the `cfbl-marketing` skill records as retired
on 2026-08-16, when Notion had already logged that photography-led Institute
content outperformed the layout-led version. A predecessor skill carried the stale
rule, the work came back wrong, and Niki spent a Sunday re-teaching something she
had already written down. Do not restate the layout rule without the photograph.

**MUSA** is literary. The tradition is a book page and an essay in a good
magazine. Type-led, image-sparse, image oblique when present. Drop caps, pull
quotes, wide margins, a single column that trusts the reader. It never explains
itself. Posts to Handle Beta.

MUSA is all the writing: the book, the essays, the excerpts. MUSA carries a
LinkedIn profile and a bare link to a piece of writing is a continuation of the
work, which is permitted. Promotional framing around that link is not. The rule
is about voice, not venue.

The newsletter Letters from the Practice is Clinical, not MUSA, because an events
letter has to be able to say register and MUSA cannot say register. Make It Make
Sense is the other newsletter.

Institute and MUSA share Handle Beta. One brand per day on Beta. Two posts on the
same page on the same day compete with each other.

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

It runs daily at 06:00 and now fails at initialization, which emails Niki an error
every morning. It should be deactivated, not fixed and not deleted.

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

The Institute is not a product catalogue. It exists to build a brand clinicians
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

**Unresolved.** `0902_DRS_InstituteReview_intro.png` announces The Institute
Review as "one month, one theme, one book, a book review for therapists," one day
before the WTDIR intro card. Either it was renamed or there are two book series
competing on the same handle. Niki has to say which before either runs again.

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

## Foundations of Trauma Therapy

The pilot is **NBCC accreditation pending**. Nothing may claim or imply CE credit
for it until that clears. It is running and it is closed. Do not promote it. The
material may be used for teaching content and brand posts that do not reference a
cohort or imply enrollment.

## Hard rules

No em dashes, anywhere, ever. Regular hyphens only.

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

The asset matcher does not exist. Files are attached to records by hand. An
hourly job should match uploaded filenames to Asset Codes and attach them.

Where composed images live is undecided. Buffer needs a permanent public URL and
Airtable attachment URLs expire, so Shopify Files is the likely answer.

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

Website Activity Sync, scenario 6203896, is awaiting deactivation by Niki. See the
established-facts section above for why it should not be repaired.

There is an empty record in Brands and Asset Kits with no name and no tag. It
cannot match anything, but it is debris from an intake test.
