# Open issues

Genuine unresolved technical issues as of 13 September 2026. Settled decisions and
historical reasoning are not here; they are in `RETIRED_SYSTEMS.md` and
`CLAUDE.md`.

Each issue states what is wrong, how it was verified, and what blocks it.

---

## 1. CFBL 1 Shopify Intake is down

**Make scenario `6216427`.** `isActive` false, `isinvalid` true, 14 errors across
20 executions. Verified 2026-09-13 via the Make API.

This is the webhook that creates Airtable records from Shopify product events.
While it is down, nothing flows into Content Pipeline automatically from the
store. The repository previously described it as active, which was wrong and has
been corrected.

Owner: Codex. Not yet diagnosed.

---

## 2. Article Intake has no dedup

**Make scenario `6219321`.** On-demand only, and that is the only thing preventing
duplicate records. It must not be put on a schedule until it can query the
destination by a natural key and branch on whether the result count is 1 or 0.

The pattern to port is in the Website Activity Sync blueprint. Export that
blueprint before deleting the scenario.

Owner: Codex.

---

## 3. The asset matcher does not exist

Files are attached to Content Pipeline records by hand. An hourly job should match
uploaded filenames to Asset Codes and attach them.

Three constraints any implementation must satisfy:

- Accept the asset code as a **prefix with arbitrary text after it**, and know the
  `INST` account. The old parser (`api/_lib/naming.js`) accepts only stems
  beginning `CFBL-`, `DRS-` or `MUSA-` and has no `INST`, so not one real design
  file parses.
- Accept the `MMDD_ACCOUNT_Slug` pattern as well, since that is how Niki's files
  are actually named. Never rename published files to fit a parser; the filename
  sits inside the CDN path.
- **Be scoped to the marketing folders.** A general Drive search for "Fisher" or
  "Walker" returns client evaluation files with those surnames.

Owner: Codex.

---

## 4. The Vercel connector crons still fire against a dead endpoint

`cfbl-operations-connector` still runs an hourly publish cron and a Monday
analytics cron against a Notion workspace that returns 401. They are failing
rather than writing, but they are still scheduled.

**Retire them.** There is no longer a sequencing constraint. The export that
previously had to happen first is closed as unavailable, see below.

Not verifiable from the current session; no Vercel access.

Owner: Codex.

### Closed, not blocking: the Metricool caption history

The published caption history for blogIds `6760980` and `6760856` was previously
recorded as a blocking dependency, on the reasoning that it had to be exported
through the connector's `listScheduledPosts(blogId, start, end)` before anything
was decommissioned.

**Metricool has been canceled.** That history is therefore treated as
unavailable, and it is a historical limitation rather than an open task. Nothing
waits on it. The connector, its token and its crons can be retired on their own
schedule.

If any of that history is later found to matter, it is a recovery question for
Metricool support, not a dependency inside this system. Do not reintroduce it as
a blocker.

---

## 5. Website Activity Sync re-enabled itself once

**Make scenario `6203896`.** Deactivated 2026-09-10, found `isActive` true again
the same evening with a next run scheduled and no edit in between. Deactivated a
second time. Verified still off on 2026-09-13: `isActive` false, `nextExec` null.

Retained only for its create-or-update router, which issue 2 needs. If an error
email arrives from it, export the blueprint and delete the scenario rather than
deactivating a third time.

Owner: Codex. Monitoring only.

---

## 6. An app is dumping the Instagram feed into Shopify Files

Files land as `instagram-image-<uuid>.jpg` at 1080x1350 with no alt text, several
a day at 18:01, 22:01 and 23:01. They already outnumber the design work in the
same folder and will bury the asset library.

The app has not been identified. Find it and disconnect it.

Owner: Codex.

---

## 7. Brand typefaces are unavailable to headless rendering

Any automated composition path that renders HTML headlessly cannot load Cormorant
SC, Lora, Montserrat, DM Serif Display, EB Garamond or Inter. Verified 2026-09-13:
Google Fonts is blocked by the execution environment's egress policy and
`document.fonts` comes back empty, so the renderer silently substitutes a fallback
serif without erroring.

This means any headless rendering path will produce off-brand type and report
success. The fix is locally installed font files rather than a webfont link.

Until then, composition happens in Canva and Adobe, which have the fonts.

Owner: Codex.

---

## 8. Two Shopify content defects

**An empty blog exists.** Shopify carries `Letters from CFBL`, handle
`newsletter`, with sixteen articles, and alongside it `Letters From The Practice:
September 2026`, handle `letters-from-the-practice-september-2026`, with zero.
Article Intake routes by blog ID, so anything published into the new one is
invisible to it. Publish the September letter as an article inside
`Letters from CFBL` and retire the empty blog.

**Naming conventions are inconsistent in already-published files:**
`WTDIR_wk1_Herman` with no date, `SPOT_01_Serravalle_quote` numbering a series,
and `0911_CFBL_ADHDEvals` date-first. Use date-first going forward. **Do not
rename what is already published.** The matcher accepts all three patterns
instead.

Owner: Codex for the matcher, Niki for the blog.

---

## 9. Debris record in Brands and Asset Kits

An empty record with no name and no tag, left over from an intake test. It cannot
match anything, so it is harmless, but it is noise in a five-row table.

Owner: Codex.

---

## 10. One unidentified media file

`UNIDENTIFIED - is this wk2 van der Kolk film.mp4`, 110 MB, in the reading room
source library. Content Pipeline record `INST-0920-A` cannot finalize one line of
its caption until someone confirms which September film it is.

**Only Niki can answer this.** It is not a technical problem.

Owner: Niki.

---

## 11. The Buffer publisher has never run live

**Not a precondition for the first operating cycle.** Posts are placed into
Buffer manually after Niki's approval, and that is a supported path, not a
workaround. Marketing runs while engineering hardens the publisher. Do not hold a
cycle for this.

**Make scenario `6214861`.** Built, correct in structure, zero executions.

Before it runs, two things must be true. It must require Niki's explicit approval
on the specific piece, not Publish Guard alone, because Publish Guard means
technically ready and nothing more. And it must refuse to queue a post whose image
has not been confirmed registered, because a platform will accept and publish a
post without its picture while every status field reads success. The retired
connector's `metricool.js` was written to refuse rather than trust the success
flag; Buffer needs the same refusal.

Owner: Codex, on Niki's go-ahead.
