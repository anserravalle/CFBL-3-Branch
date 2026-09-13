# CFBL Marketing System: current state

Authoritative description of the system as it exists on 13 September 2026, at the
handoff from Claude as primary operator to ChatGPT/Work.

For how to run the cycle, see `OPERATOR_SPEC.md`.
For infrastructure, see `CODEX_MAINTENANCE.md`.
For what is dead, see `RETIRED_SYSTEMS.md`.
For live defects, see `OPEN_ISSUES.md`.
For why decisions were made, see `CLAUDE.md`, which is history and reasoning, not
current operating instruction.

## What we are marketing, and to whom

A trauma-informed psychology practice in Townsend, Delaware, and the professional
identity of the psychologist who owns it. Four audiences, two front doors.

| Audience | What they want | Public identity | Internal system |
|---|---|---|---|
| Prospective clients and their parents | Therapy, psychological and neurodevelopmental evaluation, groups, access to care | Center for Balanced Living | CFBL Clinical |
| The general public reading about psychology | An explanation that makes sense | Dr. Niki Serravalle | Core Dr. Niki, the bridge |
| Licensed clinicians | Clinical reasoning, CE, consultation, advanced training | Dr. Niki Serravalle | Professional Education |
| Readers | Essays, the book, the writing life | Dr. Niki Serravalle | Books + Essays |

## The two public identities

**There are two, not four.** The governing document is the Brand + Marketing
Operating Manual v1.0, August 2026, held in Niki's Canva. It outranks every file
in this repository.

- **Center for Balanced Living**, `@centerforbalancedliving`, the practice.
- **Dr. Niki Serravalle**, `@drserravalle`, authority, education, writing,
  speaking and books.

CFBL Institute / Professional Education and MUSA / Books + Essays are **internal
content and visual systems**. They are real, they are distinct, and they are
never additional public social identities. The manual's closing rule: if a person
must understand the brand architecture before they can understand the content,
the content is not ready.

Professional Education and Books + Essays share the `@drserravalle` account. One
system per day on it.

## The four visual systems

Every asset signs with the public brand largest, and one category line underneath.
Never a list of programs.

**CFBL Clinical.** Editorial, a well-made magazine feature. Open with a specific
human moment, then the idea. Warm, human, credible, clinically accurate without a
jargon wall.
Palette Cobalt Blue `#2B5275`, Ocean and Sky Blue `#4E9FBF`, Sand `#EED9C5`,
Terracotta `#9D654E`, Warm Gray `#3D2D29`. Cormorant SC headlines, Montserrat
body. Carries the rainbow logo.
Signs as Center for Balanced Living / Trauma-informed therapy and psychological
assessment.
Avoid: busy patterns, neon, high saturation, harsh gradients, cartoons, long
all-caps lines, more than one headline hierarchy.

**Core Dr. Niki, the bridge.** Public psychology explanation and Make It Make
Sense. Borrows rather than owning a palette, which is why published Make It Make
Sense cards read navy and sand duotone. Must not read as the practice's intake
voice.
Signs as Dr. Niki Serravalle / Make It Make Sense.

**Professional Education.** Scholarly, a serious field guide, photography led.
Lead with the mechanism or the finding, not with the reader. Name the evidence
base.
Palette Forest `#3D5A52`, Sage `#6F8F7A`, Sage Mist `#B8C9BC`, Soft Sky `#C2D7E9`,
Cream `#EAE2D0`, Paper `#F0EAE0`, Deep Ink `#2A3530`. Cormorant SC headlines,
Lora body, Inter or Source Sans Pro for metadata only.
Imagery is assessment materials, teaching context, clinical concepts, restrained
natural detail.
Signs as Dr. Niki Serravalle / Professional Education.
Avoid: wellness imagery, parent-brand navy or terracotta as primary fields, the
rainbow CFBL logo, decorative botanicals, spa gradients, parent-brand appointment
language.

**Books + Essays.** Literary, first person, analytical, direct. One idea per
piece. Trust the reader to finish the thought. Never explain the piece.
Palette Bone `#F1E8D8`, Parchment `#EDE0C8`, Oxblood `#6E1F23`, Ochre `#C5A572`,
Walnut `#4A4036`, Ink `#1F1A16`. DM Serif Display titles and drop caps, EB
Garamond body. Breaks from the Cormorant family on purpose, so the writing reads
as an independent credential.
Photography led, image-oblique, never image-absent.
Signs as Dr. Niki Serravalle / Books + Essays. MUSA may appear as a subtle
imprint; it is never the identity.
Avoid: Cormorant, any CFBL or Institute color, decorative botanicals, women
journaling, coffee-and-journal flat lays, credentials above the essay title, pure
black, marketing-heavy CTAs.

**Two registers live inside Books + Essays and they are not interchangeable.**
The book is interior and oblique. The essays are direct, argued, addressed to a
reader in pain, and useful in a way the book deliberately is not. A post carrying
an essay may say something a reader can act on. A post carrying a book excerpt may
not. "Never explain the piece" governs the framing around the work, not the prose
inside it.

## The mark

The rainbow tree is the practice's founding symbol, eight years old, on the
building, the car, the signage and the logo. The spectrum is inclusion and
community. It is never a palette question and it is never removed, muted, or
recolored. The Brand Guide sets a 2 inch / 200 pixel minimum, clear space the
width of the C from the logotype.

It belongs to Center for Balanced Living. Professional Education's avoid list
names it directly, so it does not appear on Institute work.

## Routing

| If the content is mainly about | Publish from | System |
|---|---|---|
| Therapy, evaluations, groups, the team, local resources, referral access | Center for Balanced Living | CFBL Clinical |
| Public psychology explanation, Make It Make Sense | Dr. Niki Serravalle | Core Dr. Niki bridge |
| Clinician skills, clinical reasoning, CE, consultation, advanced training | Dr. Niki Serravalle | Professional Education |
| Books, essays, author ideas, writing process, reading life | Dr. Niki Serravalle | Books + Essays |
| A topic genuinely serving two audiences | Two tailored assets | Each audience's correct system |

## The active stack

| System | Role |
|---|---|
| **Airtable** | Operational marketing database and The Standard |
| **Shopify** | Source of truth for products, offers, pages, articles, availability, pricing, all public website information |
| **Google Drive** | Authentic photography, video and source media |
| **Canva, Adobe** | Creative production |
| **Buffer** | Scheduling and publishing |
| **Google Calendar** | Dates and scheduling information |
| **GitHub / Codex** | Durable technical architecture, code, integrations, maintenance, repairs |
| **ChatGPT / Work** | Primary marketing operator, strategist, content producer, creative director, cross-app execution |
| **Niki** | Final approval authority |

**Shopify is the source of record. Airtable is derived. When they disagree,
Shopify is right.**

Notion and Metricool are retired. See `RETIRED_SYSTEMS.md`.

## Where current information is verified

Never state any of the following from memory. Read the record.

- **Products, prices, seats, availability, CE credit** → the Shopify product
  record itself. Read `descriptionHtml`, `variant.inventoryQuantity`,
  `inventoryPolicy`, `inventoryItem.tracked`. Untracked inventory is not zero
  inventory. A summarized web fetch of a page is not the record.
- **Articles and blogs** → Shopify, by blog ID rather than by tag.
- **Published assets and their history** → Shopify Files, which carries
  descriptive alt text.
- **A clinician's scope of practice** → that clinician's own bio, quoted, or ask
  the person.
- **Dates** → Google Calendar.

## Continuing education, stated exactly

Getting this wrong is an ethics problem, not a marketing one. Verified against
Shopify 2026-09-10 and unchanged since. Re-verify before any CE claim ships.

**Foundations of Trauma Therapy**, 18 and 19 September 2026, provides 12 hours of
instruction across two days. This pilot cohort is the delivery that completes CFBL
Institute's NBCC accreditation application, and **the hours count toward your
practice rather than your license renewal**. DRAFT status, 14 seats remaining, not
publicly purchasable. It is running and it is closed. **Do not promote it.** The
material may be used for teaching content and brand posts that do not reference a
cohort or imply enrollment.

**Nature-Informed EMDR** is **EMDRIA Approved for 3 EMDRIA Credits** and the
product page leads with it. Friday 2 October 2026, 2:00 to 5:00pm Eastern, live on
Zoom. Credit requires live real-time attendance. Prerequisite is completion of an
EMDRIA-Approved Basic EMDR Training. ACTIVE, 99 dollars, 10 seats, tracked,
policy DENY.

Never flatten approved and pending.

## Recurring series

**Make It Make Sense (MIMS)** is the blog and the cadence anchor for the whole
calendar. Every other week. Post and email day 0, social day 2. Routes to Dr. Niki
Serravalle on the bridge treatment. Call it Make It Make Sense, never "the blog."

**What the Doctor Is Reading.** Professional Education. A subject a month, a book
a week, a short film on Sunday, twelve subjects from September 2026 to August
2027. September is trauma across modalities: Herman, van der Kolk, Fisher, Pete
Walker. The set is fixed and stays fixed: the same reading chair, the same window,
the same floor lamp, the same shelf. Recognition across twelve months depends on
it. Her expression carries the editorial stance, so the shot note says skeptical,
endorsing or undecided.

**THE CFBL SHELF.** Practice account, parent-facing. Different audience from What
the Doctor Is Reading, not a duplicate.

**Letters from the Practice.** CFBL Clinical, because an events letter has to be
able to say register.

**Staff spotlight.** Two questions to all staff twice a year, including
administrative staff, plus a weekly quote with a photograph. Quotes run as
written, trimmed for length only. **Get a written yes from each person before
publishing their words or photograph.** Administrative staff feel more pressure to
agree than clinicians do.

**Permission Slips**, the humor pillar. Warm first, funny second. Clever, not
silly. Never at a client's expense, never diagnosing for laughs. Reached No. 11 on
2026-09-09, so the next is No. 12. The lighthearted post never lands the same day
as a heavy clinical piece.

## The four tiers

The Institute's sorting framework. Every claim sits in one, and each licenses a
different strength of statement.

- **Established.** Replicated across independent samples, survives attempts to
  knock it down. State it plainly.
- **Emerging.** Real data, thin replication. Use it and say it is early.
- **Theoretical.** Organizes observations. May be elegant, useful, and still not
  established. Scaffolding for the clinician, not an explanation for a client.
- **Clinical wisdom.** What experienced clinicians do and teach. Often correct,
  rarely tested. Name it as practice knowledge and hold it loosely enough to drop.

Clinical wisdom is not a dismissal.

## Hard rules

These are non-negotiable and apply to captions, copy, email, documents, shot
notes, Airtable fields, code comments and commit messages.

**No em dashes, anywhere, ever.** Regular hyphens only.

**American English, anywhere, ever.** Organize, recognize, realize, analyze.
Color, behavior, favor. Center, not centre. License, not licence, which matters
most in the CE language. Catalog, gray, judgment, traveling, canceled, program.
Feet and inches, never meters.

**Never put protected health information or identifiable client information into
any connected system.**

**Never open or copy the body of a client inquiry email.** Only the date and the
count are ever extracted. This is a clinical practice and those are patients.

**Never ask for a credential in chat and never accept one there.** Tokens go from
the issuing platform directly into the platform that needs them. A token that
reaches a conversation is compromised and must be rotated.

**Never read personnel files for marketing material.** Staff HR folders hold
credentialing, evaluations, contracts and departure records. Headshots come from
Drive / Marketing / Headshot.

**No generated clinicians, therapy offices, sessions, or clients. No fabricated
quotes attributed to real staff.**

**Any automated search of Drive must be scoped to the marketing folders.**
Searching generally for "Fisher" or "Walker", who are book authors in the reading
series, returns client evaluation files with those surnames.
