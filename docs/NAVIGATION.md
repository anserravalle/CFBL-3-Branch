# Navigation & site map — setup guide

Shopify **menus are created in the admin** (Content → Menus), not in theme files,
so this guide gives you the exact menu tree to build plus the Pages, Blogs, and
**theme templates** to assign to each link. Once these exist, the header,
footer, blog, and brand-scope all work automatically.

---

## 1. Main menu (header)

Create / edit **Content → Menus → Main menu** with these top-level items and
sub-items (Shopify shows children as dropdowns):

```
For Clients            → /pages/services
  ├─ About Us          → /pages/about-us
  ├─ Our Credentials   → /pages/credentials
  ├─ FAQ               → /pages/faq
  ├─ Individual Therapy→ /pages/individual-therapy
  ├─ Evaluations       → /pages/psychological-evaluations
  └─ Wellness Groups   → /pages/wellness-groups

For Professionals      → /pages/cfbl-institute
  ├─ Professional Trainings → /pages/professional-trainings
  ├─ Workshops         → /pages/workshops
  ├─ Courses           → /pages/courses-certification
  └─ FAQ               → /pages/faq

About Us               → /pages/about-us
  └─ (individual bio pages, e.g. /pages/niki-serravalle, /pages/amanda-foxwell …)

MUSA                   → /pages/musa
  ├─ Why I Write       → /pages/musa#why
  └─ Essays            → /blogs/essays

Newsletter             → /blogs/newsletter
Make It Make Sense     → /blogs/make-it-make-sense
```

> Tip: a top-level item can be both a link **and** a dropdown — set its URL to
> the landing page and add children beneath it.

---

## 2. Pages to create & the template to assign each

In **admin → Content → Pages**, create each page and set its **Theme template**
(the dropdown on the page editor). The template drives the design *and* the
brand scope (Institute = Forest, MUSA = Oxblood).

| Page (handle)              | Theme template          | Brand scope |
| -------------------------- | ----------------------- | ----------- |
| services                   | `services`              | CFBL        |
| about-us                   | `about`                 | CFBL        |
| credentials                | `page` (or `service`)   | CFBL        |
| faq                        | `faq`                   | CFBL        |
| contact                    | `contact`               | CFBL        |
| individual-therapy         | `service`               | CFBL        |
| psychological-evaluations  | `evaluations`           | CFBL        |
| wellness-groups            | `service`               | CFBL        |
| workshops                  | `workshops`             | CFBL        |
| cfbl-institute             | `cfbl-institute`        | Institute   |
| professional-trainings     | `professional-trainings`| Institute   |
| courses-certification      | `service`               | Institute¹  |
| clinical-supervision       | `service`               | Institute¹  |
| emdr-consultation          | `service`               | Institute¹  |
| musa                       | `musa`                  | MUSA        |
| niki-serravalle (+ team)   | `service` or `page`     | CFBL        |

¹ These handles auto-resolve to the Institute scope via `brand-scope`. If you
use a different handle, either assign an Institute template or set the page's
`custom.brand_scope` metafield to `institute`.

---

## 3. Blogs to create & the template to assign each

In **admin → Content → Blog posts → Manage blogs**, create:

| Blog (handle)        | Theme template (blog) | Article template | Scope |
| -------------------- | --------------------- | ---------------- | ----- |
| make-it-make-sense   | `make-it-make-sense`  | (default)        | CFBL  |
| newsletter           | `newsletter`          | (default)        | CFBL  |
| essays               | `essays`              | `musa`           | MUSA  |

Assign the template under the blog's (or article's) **Theme template** dropdown.

**Make It Make Sense tags:** tag posts with any of
`The Field`, `On Therapy`, `On Diagnostics`, `The Cultural Moment`, `Being Human`.
The theme cards on the blog landing link to `/.../tagged/<tag>` and the listing
below filters to that tag automatically. Edit the cards (titles/tags/icons) in
the theme editor on the *Make It Make Sense* blog template.

**Newsletter ("Letters From the Practice"):** each post is an issue. The landing
features the current (latest) issue and lists past issues below.

---

## 4. Footer menu
Create **Content → Menus → Footer** (referenced by the footer's menu columns).
A simple set works well:
```
Explore: About Us, Services, FAQ, Contact
Practice: Individual Therapy, Evaluations, Workshops, CFBL Institute
```
Then in the theme editor (Footer section) point each footer column at the menu
you want, and set the contact column's phone/hours.

---

## 5. Quick checklist
- [ ] Main menu built with the tree above
- [ ] Footer menu built
- [ ] All Pages created with the right **Theme template** assigned
- [ ] Blogs `make-it-make-sense`, `newsletter`, `essays` created + templates assigned
- [ ] Make It Make Sense posts tagged with the five themes
- [ ] MUSA pages confirm Oxblood; Institute pages confirm Forest
- [ ] Header CTA + sub-brand logos set in Theme settings
