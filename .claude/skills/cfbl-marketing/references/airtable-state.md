# Airtable state

Base `appP8PQe3dvqxosjR`, CFBL 3-Brand Engine. Airtable is the operational
database. Shopify remains the source of truth for anything public: products,
prices, availability, pages and articles. Where the two disagree, Shopify is
right.

This file replaced an earlier Notion-backed equivalent. Notion is retired; see
`RETIRED_SYSTEMS.md`.

## Tables

| Table | Id | Holds |
|---|---|---|
| The Standard | `tbleatoO3KDm2VZbS` | The living standard. Read first, every time. |
| Content Pipeline | `tbl4AGvnuD3YjS1n2` | One row per piece |
| Brands & Asset Kits | `tbl93bjxUvFkMhYDd` | Brand routing, kits, profiles, voice |
| Curriculum Vault | `tbldTobI99OtH0DRe` | Course and training material |

## Brands

| Brand | Record | Tag key | Account |
|---|---|---|---|
| CFBL Clinical | `reccomuvFnOj8ZRh2` | `cfbl-clinical` | Center for Balanced Living |
| CFBL Institute | `recMEt3EqbugUYnVp` | `cfbl-institute` | Dr. Niki Serravalle |
| MUSA | `rec6rhNGbkMOzUcof` | `musa` | Dr. Niki Serravalle |

Two accounts, three brands. Brand governs voice and visual grammar. Account
governs where it posts. Institute and MUSA share the Dr. Niki Serravalle account,
which is why only one of them posts on any given day.

There is a fourth, empty record in Brands with no name and no tag. It is debris
from an intake test. It cannot match anything. Ignore it or delete it.

## Content Pipeline field ids

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

## The Standard field ids

| Field | Id |
|---|---|
| Principle | `fldjOmKv7ci6fe9qI` |
| Kind | `fldAplH5BD1tk24Oo` |
| Detail | `fldmJEYfoPerke27f` |
| Date established | `fldaInnGkJ3OXg7qn` |
| Source | `fldVNeMHgZ6adzR3F` |
| Provenance | `fldrPFOjxYV6YEgBb` |

Kind is one of: Do not repeat, What performed, Standing rule, Verification
failure, System defect.

Write the knowledge, not the adjective. Every row carries its evidence in Detail,
because a principle with no story behind it gets argued with six months later by
someone who was not there.

## Writing through the API

The MCP tools take **field ids, not field names**. Passing a name returns a
validation error saying the field id must start with `fld` and be 17 characters.

`create_records_for_table` and `update_records_for_table` both nest values under a
`fields` key per record. `update_records_for_table` also needs `id` on each record.

`list_records_for_table` returns `cellValuesByFieldId`, not `fields`.

Sorting is `sort: [{fieldId, direction}]`, not `sortFieldId`.

## Publish Guard

A readiness check, not an approval. It reads:

- no brand linked, more than one brand linked, no destination, no asset kit, or a
  brand tag that contradicts the linked brand, and it blocks
- no Asset Code, and it reads Not scheduled
- an Asset Code with no attached file, and it reads Waiting on that code
- no copy at all, and it reads Waiting on copy
- otherwise READY

READY means the row is complete. It does not mean Niki approved it. See the
approval gate in the skill.

## Asset codes

`ACCOUNT-MMDD-LETTER`, accounts `CFBL`, `INST`, `DRS`, `MUSA`. The code goes at
the front and a descriptive slug may follow it, so `INST-0920-A_WTDIR_Hinshaw.png`
is correct and preferred.

Niki's own design files are named `MMDD_ACCOUNT_Slug.png`. The old connector's
parser only accepted a stem beginning `CFBL-`, `DRS-` or `MUSA-` and had no `INST`
account, so none of her real files ever parsed and the publisher silently matched
nothing. Any matcher built here must accept the code as a prefix with arbitrary
text after it, and must know `INST`.

## Make scenarios

Team 2907664.

| Scenario | Id | State |
|---|---|---|
| CFBL 1 Shopify Intake | 6216427 | Active, webhook driven |
| CFBL 2 Article Intake | 6219321 | On demand only, no dedup yet |
| CFBL 3 Buffer Publisher | 6214861 | Built, never run live |
| Website Activity Sync | 6203896 | Deactivated 2026-09-10, do not repair or delete |

Intake quarantines by default and promotes only on an exact brand match. When the
brand search returns nothing the branch halts and the row stays in Needs Manual
Review. That halt is the fail-safe. Never make the intake guess a brand.
