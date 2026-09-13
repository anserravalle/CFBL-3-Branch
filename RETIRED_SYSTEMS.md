# Retired systems and superseded rules

Nothing in this file governs current execution. It exists so that a future
operator who finds a reference to one of these knows it is dead, and so that the
technically useful parts are not lost.

**If anything here contradicts `CURRENT_SYSTEM.md` or `OPERATOR_SPEC.md`, those
files win.**

## Notion. Retired.

Notion was the home of the living standard, on a page called Marketing & Content
Engine. It was emptied and deleted on or before 2026-09-10, taking the accumulated
what-not-to-repeat log, the visual standard and the learning loop with it. One
fragment survived only because a skill file happened to quote it.

**Verified dead 2026-09-13:** the Notion API returns `401 unauthorized, API token
is invalid`. The workspace is not reachable.

**Replaced by** The Standard, Airtable table `tbleatoO3KDm2VZbS`. The replacement
was deliberate: durable architecture belongs in a repository under version
control, and anything that changes belongs where Niki already works. A file she
does not edit is a file that will be wrong within a month.

**One Notion artifact still exists.** Make scenario `6203896`, Website Activity
Sync, is still in the account with three Notion modules and a daily 06:00 schedule
definition. It is off: `isActive` false, `nextExec` null, verified three times.

It never worked. Module 3 carries a filter named `TEST LOCK - Notion writes
disabled` whose condition is `READ_ONLY_TEST` equals `ENABLE_NOTION_SYNC`, which
can never be true. Every Notion write in the scenario sits downstream of that
filter, so it never wrote anything in its life: two executions, two operations.

**It is retained for one reason only.** Its create-or-update router is the dedup
pattern CFBL 2 Article Intake still needs: query the destination by a natural key,
then branch on whether the result count is 1 or 0. Port that pattern rather than
inventing one. Export the blueprint before deleting the scenario.

**One caution.** It was deactivated on 2026-09-10 and by that evening was
`isActive` true again with a next run scheduled, without having been edited.
Deactivated a second time and verified off, and still off on 2026-09-13. If an
error email arrives from it, delete the scenario rather than deactivating a third
time, after exporting the blueprint.

## Metricool. Retired.

Metricool was the previous scheduling and publishing platform, and the
predecessor skill delivered to it as a bulk CSV.

**Replaced by Buffer**, which is the active publishing platform.

**Verified 2026-09-13:** no Metricool scenario exists in Make, and no Metricool
reference exists anywhere in the operating skill or its four reference files. The
rewritten skill delivers files to Niki directly. The "skill delivers to Metricool
vs this build delivers to Buffer" conflict that was recorded as live was already
resolved when the skill was rewritten on 2026-09-10; the record simply never
caught up.

**One live dependency remains, and it is a data-preservation issue, not a
workflow one.** Metricool holds every caption the old system published, for
blogIds `6760980` Center for Balanced Living and `6760856` Dr Serravalle, with
MUSA interleaved on the Dr Serravalle account. **That history has not been
exported.** Do not cancel the Metricool account, delete the Vercel project, or
rotate its token until it is out. See `OPEN_ISSUES.md`.

## The Vercel operations connector. Retired, not yet decommissioned.

`cfbl-operations-connector` ran an hourly publish cron and a Monday analytics cron
against Notion. Notion is gone, so those crons now fire against a dead endpoint.

It holds `listScheduledPosts(blogId, start, end)` and a live Metricool token,
which is the mechanism for the export above. Retire the crons, export the history,
then decommission. Not before.

Its `api/_lib/naming.js` parser is documented as a defect class in
`CODEX_MAINTENANCE.md`.

## Superseded operating rules

Each of these was a real rule at one point. None of them governs now.

**The Sunday-through-Saturday week, planned Thursday to Saturday of the week
before.** Set 2026-08-16, retired by Niki 2026-09-10. **Replaced by** the blog as
the cadence anchor and an eight-week editorial horizon. There is no fixed planning
weekday and no Thursday approval or Saturday audit step.

**Thirty percent marketing, thirty percent brand building, thirty percent
community building, counted rather than estimated.** **Replaced by** three
strategic jobs evaluated across the editorial cycle rather than forced into any
single week. The three jobs survive; the arithmetic does not.

**Roughly three parts value to one part promotion, counted not estimated.** Same
supersession. Judge the balance over the cycle.

**Three co-equal public brands with three print traditions**, editorial for
Clinical, scholarly for Institute, literary for MUSA. Corrected 2026-09-10. The
Operating Manual lists "third-brand explanation" under Stop and says explicitly
not to treat CFBL Institute or MUSA as equal public identities. **The internal
visual systems are real and preserved.** Only the claim that they are public
identities is retired. The three traditions still describe how each system feels;
they were never a license to set flat type on a color ground.

**CFBL Institute as a layout-led scholarly system**, using plates, figure numbers
and ruled tables without photography. Retired 2026-08-16 when photography-led work
measurably outperformed it. A predecessor skill carried the stale rule, the work
came back wrong, and a Sunday went into re-teaching it. **Do not restate it.** A
plate is still correct, but a plate is a photograph with a caption.

**Books + Essays as a type-led, image-sparse system.** Retired around 2026-08-11.
It had reached a live shot note before being corrected. The current rule is
image-oblique, never image-absent. A type-only page is the retired layout.

**Oxblood `#5A0C11`.** Wrong color. The correct value is `#6E1F23`. The wrong one
survived in two places at once, which is why the current rule is that a brief
carries palette hex values inline even when the renderer already knows them.

**The Institute Review**, as a series name. It was the discarded first name for
What the Doctor Is Reading, made on 2 September 2026 as one month / one theme /
one book, and superseded roughly twenty hours later by a book a week. Nothing was
made under the old name afterwards. One series, not two.

**Four competing approval surfaces.** The iteration before this one carried a
Stage field with nine options, a Publication Approval field with five, an
Automation Status field with five, and thirty-three properties in total. They
could each disagree with the others, and that is what killed it. **The lesson is
load-bearing and is repeated in `OPERATOR_SPEC.md`:** do not add a second approval
surface.

**Stale account-level skill copies.** `cfbl-content-creator` and
`cfbl-weekly-marketing` pointed at Notion and were retired by their own successor.
They no longer appear in the skill list.

## Things that were investigated and settled

Recorded so nobody spends a second session on them.

- TikTok cannot publish through this stack. Make's TikTok app is ads only.
- Shopify allows one connection per store in Make; a new one replaces the old.
- Reauthorizing an OAuth connection replays the original grant and adds no scopes.
- Mobile Safari accepts an OAuth flow and never persists the connection.
- Shopify MCP correctly refuses `webhookSubscriptionCreate`.
