# Codex maintenance

Technical infrastructure, automations, dependencies and known defects. What Codex
owns and what it does not.

## Division of responsibility

**Codex owns:** the repository, code, integrations, Make scenarios, Airtable
schema and formulas, connectors, crons, and repairs. Anything that breaks.

**ChatGPT/Work owns:** marketing strategy, content, creative direction, and the
editorial cycle. See `OPERATOR_SPEC.md`.

**Niki owns:** final approval on anything that publishes.

Codex does not decide brand rules, content, or what ships. Those live in
`CURRENT_SYSTEM.md`, in The Standard, and with Niki.

## Airtable

Base `appP8PQe3dvqxosjR`, CFBL 3-Brand Engine. Table and field IDs are in
`OPERATOR_SPEC.md`.

### Publish Guard

The single technical ship or no-ship computation. Eight nested conditions, eight
closing parens. It means *technically ready*, never *approved*.

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
what catches that. A comma separator does not work because array coercion supplies
no delimiter of its own. Do not "simplify" this.

### Tracked links

```
IF(ARRAYJOIN({Profile LinkedIn}, "") = "", "",
IF(AND({Landing URL} = "", ARRAYJOIN({Brand Base URL}, "") = ""), "",
IF({Landing URL} != "", {Landing URL}, ARRAYJOIN({Brand Base URL}, ""))
 & "?utm_source=linkedin&utm_medium=social&utm_campaign=" & ARRAYJOIN({Brand Key}, "")
 & "&utm_content=" & RECORD_ID()))
```

`utm_content` carries the Airtable record ID, which makes attribution post-level
rather than campaign-level. That is the entire reason for the formula.

### Send Queue

A formula, not a select. Reads the three venue checkboxes and only names a
platform when the linked brand actually holds a profile ID for it. A checkbox
alone does not queue a post.

## Make

Team `2907664`. Four scenarios, verified 2026-09-13.

| ID | Name | State | Notes |
|---|---|---|---|
| `6216427` | CFBL 1 Shopify Intake | **`isActive` false, `isinvalid` true, 14 errors / 20 executions** | Down. See `OPEN_ISSUES.md`. |
| `6219321` | CFBL 2 Article Intake | Active, on-demand only | No dedup. Do not put on a schedule until it has one. |
| `6214861` | CFBL 3 Buffer Publisher | Active, never run live | Router with IG, LinkedIn and TikTok branches, each filtered on Send Queue. |
| `6203896` | Website Activity Sync | `isActive` false, `nextExec` null | Retired, retained only for its blueprint. See `RETIRED_SYSTEMS.md`. |

**CFBL 1 Shopify Intake.** Webhook driven: Shopify pushes to Make rather than Make
polling Shopify, which sidesteps app scopes entirely. Flow is webhook, create the
Airtable record as Needs Manual Review, search Brands by tag, promote to Draft and
link the brand only if a brand matched. **Quarantine by default, promote on
match.** When the brand search returns nothing the branch halts and the record
stays in Needs Manual Review. That halt is the fail-safe, not a bug. Never make the
intake guess a brand.

**CFBL 2 Article Intake.** Routes by Shopify blog ID rather than by tag. This
proved correct when a Clinical article carried a stray `brand:musa` tag: the blog
an article lives in is a stronger signal than a tag someone typed.

**CFBL 3 Buffer Publisher.** Reads Content Pipeline rows and sends each cleared
channel to that brand's Buffer profile. Routing is inherited from Airtable, never
set in the scenario. **It has never run live, and per the approval gate it must
not run on Publish Guard alone.** Publish Guard means technically ready. Human
approval is a separate, required step.

Connections: Airtable read-only `10987115`, CFBL Airtable Write `10993299` which
is the one in use, Buffer `10987143`, Shopify `10989870`.

## Platform constraints already established

Do not re-investigate these.

**TikTok cannot publish through this stack.** Make's TikTok app is ads only.
Reauthorizing does not change it. Keep writing scripts if useful, post manually.

**Shopify allows one connection per store in Make.** Creating a new one replaces
the old one and silently breaks scenarios bound to the previous connection ID.

**Reauthorizing an OAuth connection replays the original grant.** It does not add
scopes. A new scope needs a new connection.

**Do OAuth connections on desktop.** Mobile Safari accepts the flow, shows the
connection in the dropdown, and never persists it server side. The symptom is
`Status Code Error 400, no access token specified`.

**Shopify MCP refuses `webhookSubscriptionCreate`** and classifies it as data
exfiltration. That is correct behavior. Create webhooks in the Shopify admin
Notifications UI.

**Airtable modules in Make nest field values under a `record` object.** Sending a
`fields` key returns 422, could not find field fields.

**Airtable search modules reject empty strings for optional parameters.** Sending
an empty `view`, `fields` or `sort` returns parameter validation failed. Omit them.

**Shopify numeric IDs fail into Airtable text fields even with typecast.** Use
`admin_graphql_api_id`, which is already a string GID.

**`scenarios_run` with a data payload against a webhook scenario reports SUCCESS
and does nothing.** Check the execution log, not the return value.

**The Airtable API rejects field names on create and update.** Use field IDs.

## Known defect classes

**A scheduled post can publish with the caption and no image while every status
field reads success.** From `metricool.js` in the retired operations connector: a
platform will not attach an image it has not registered, and skipping the
registration step does not error. The post is accepted and published without its
picture and nothing reports a failure. The old connector was written to refuse to
queue rather than trust the success flag. **Any publisher built here needs the same
refusal, Buffer included.**

**Filename parsing.** The old connector's parser, `api/_lib/naming.js` in
`cfbl-operations-connector`, accepts only stems beginning `CFBL-`, `DRS-` or
`MUSA-` followed by four digits and a letter, and has no `INST` account at all.
Not one of Niki's real design files parses, which is a sufficient explanation for
that system appearing to do nothing. Any matcher built must accept the code as a
prefix with arbitrary text after it, must know `INST`, and must accept the
`MMDD_ACCOUNT_Slug` pattern as well.

**Drive search scope.** Any automated matcher must be scoped to the marketing
folders and never allowed to search Drive generally. Searching for "Fisher" or
"Walker", who are book authors in the reading series, returns client evaluation
files with those surnames.

## Dependencies worth knowing

- Composed images live in **Shopify Files**, because Airtable attachment URLs
  expire and Buffer needs a permanent public address.
- **Canva brand kit IDs**: Niki Serravalle's Team `kAFyY1XTC7Y`, cfbl institute
  `kAHJ1YJ0bj4`, MUSA `kAHMFB7bPAs`, Center for Balanced Living `kAHNmLXRp04`.
- **Shopify blog IDs** are stored on the Brands and Asset Kits table and are what
  Article Intake routes on.
- Brand typefaces are **Cormorant SC, Montserrat, Lora, Inter / Source Sans Pro,
  DM Serif Display, EB Garamond**. Any headless rendering path needs these locally
  installed; see `OPEN_ISSUES.md`.

## Security constraints that bind code as well as people

- No protected health information or identifiable client information in any
  connected system, ever.
- No credential in a conversation. Tokens go from the issuing platform directly
  into the platform that needs them. A token that reaches a chat is compromised
  and must be rotated.
- No personnel-file access for marketing purposes.
- The repository carries identifiers, never keys. Base IDs, table IDs, field IDs,
  scenario IDs and connection IDs are addresses and require an authenticated
  connection to use.
