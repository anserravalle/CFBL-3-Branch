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
serious field guide. Plates with captions and figure numbers. Ruled tables.
Marginal annotation. Nothing decorative that does not carry information. This
serves the mission directly: adult learners who want a deep dive rather than a
certificate should be able to see the difference before they read a word. Posts
to Handle Beta.

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

Asset codes are `ACCOUNT-MMDD-LETTER`. Accounts are `CFBL`, `INST`, `MUSA`.
Example: `CFBL-0916-A`. The photographer names the file the code and nothing
else. Renaming breaks the link between the record and the asset.

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
the old one. The replacement of 10967062 with 10989870 may have broken the
Website Activity Sync scenario. Unverified.

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

**What the Doctor Is Reading.** Monthly. One theme, one book, and what the book
licenses a clinician to say in a room with a client. Assigned to the Institute
rather than MUSA: the audience is the Institute audience, the grammar is a plate
with a caption and a citation line, and a reading community has to be able to say
join us, which MUSA cannot. Each month sorts the book's claims into the four
tiers.

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
Retire those crons.

There is an empty record in Brands and Asset Kits with no name and no tag. It
cannot match anything, but it is debris from an intake test.
