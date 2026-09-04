# Navigation & site map - setup guide

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

> Tip: a top-level item can be both a link **and** a dropdown - set its URL to
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
| individual-therapy         | `individual-therapy`    | CFBL        |
| psychological-evaluations  | `evaluations`           | CFBL        |
| wellness-groups            | `wellness-groups`       | CFBL        |
| workshops                  | `workshops`             | CFBL        |
| cfbl-institute             | `cfbl-institute`        | Institute   |
| professional-trainings     | `professional-trainings`| Institute   |
| courses-certification      | `service`               | Institute¹  |
| clinical-supervision       | `clinical-supervision`  | Institute¹  |
| emdr-consultation          | `emdr-consultation`     | Institute¹  |
| musa                       | `musa`                  | MUSA        |
| niki-serravalle (+ team)   | `team-member`           | CFBL        |

> Team bios: assign **`team-member`** to each clinician's page (niki-serravalle,
> amanda-foxwell, kirsten-lowe, brianna-patton, etc.). Edit each page's content
> for the long bio; set the hero image/heading and specialties in the editor.

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

---

## 6. Update: Career Development + footer menus + header signature

### Career Development (main menu)
Add a top-level **Career Development** item to the Main menu, linking to
`/pages/career-development`, with these children:

```
Career Development     -> /pages/career-development
  ├─ Clinical Supervision -> /pages/clinical-supervision
  ├─ EMDR Consultation    -> /pages/emdr-consultation
  └─ Join Our Team        -> /pages/join-our-team
```

Pages + templates to create:
| Page (handle)        | Theme template        | Scope     |
| -------------------- | --------------------- | --------- |
| career-development   | `career-development`  | Institute |
| join-our-team        | `join-our-team`       | CFBL/Inst |

(`career-development` auto-resolves to the Institute/Forest scope via its handle.)

### Footer menus
The footer uses three link menus plus an Office Hours text column (the hours
text is editable directly in the Footer section, no menu needed). Create these
menus in Content > Menus:

```
footer (Explore):            Contact Us, Privacy Practices, Newsletter, CFBL Institute
footer-for-clients:          Therapy, Evaluations, Wellness Groups, Client Portal, FAQ
footer-for-professionals:    Join Our Team, Workshops, Courses & Certification,
                             Professional Trainings, EMDR Consultation, Supervision
```

Office Hours (set in the Footer section's "Office Hours" text block):
```
Monday: 10 am-6 pm
Tuesday: 10 am-6 pm
Wednesday: 10 am-6 pm
Thursday: 10 am-6 pm
Friday: 10 am-4 pm
Saturday / Sunday: Closed
```

### Header signature image
In the theme editor, open the Header section and upload your **Signature image**
(top right). A transparent PNG works best; adjust its height with the slider.
It hides on mobile to keep the header compact.

---

## 7. Sub-evaluation & detail pages (added)

Create these pages and assign the matching template (all auto-scope to CFBL,
except courses which is Institute):

| Page (handle)              | Template                   |
| -------------------------- | -------------------------- |
| adhd-evaluation            | `adhd-evaluation`          |
| autism-evaluation          | `autism-evaluation`        |
| diagnostic-clarification   | `diagnostic-clarification` |
| personality-and-emotional  | `personality-and-emotional`|
| academic-and-learning      | `academic-and-learning`    |
| courses-certification      | `courses-certification`    |
| client-portal              | `client-portal` (set the real portal URL on the hero button) |

The Evaluations page tabs now link to these sub-pages. Workshops page has a
detail intro. Privacy Practices can use the default `page` template.
