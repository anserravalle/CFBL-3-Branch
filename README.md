# Center for Balanced Living — Shopify Online Store 2.0 Theme

A bespoke, clinically-polished Shopify **Online Store 2.0** theme for Center for
Balanced Living — a trauma-informed psychology practice in the MOT area of
Delaware. Built design-system-first for complete no-code customization, strong
SEO, accessibility, and performance.

> This theme is a ground-up rebuild migrated from the practice's previous
> **Impact (Maestrooo)** theme. See [`docs/MIGRATION_NOTES.md`](docs/MIGRATION_NOTES.md)
> for the content map and preserved business details, and
> [`docs/DESIGN_SYSTEM.md`](docs/DESIGN_SYSTEM.md) for the design system that
> governs every section.

---

## 1. File structure & where each file goes

```
.
├── layout/
│   └── theme.liquid                 # Master HTML shell: <head>, fonts, token seeding, section groups
├── config/
│   ├── settings_schema.json         # All global theme-editor settings
│   └── settings_data.json           # Saved values / brand defaults
├── locales/
│   └── en.default.json              # UI strings (translatable)
├── templates/                       # JSON templates (assign sections per page type)
│   ├── index.json                   # Homepage
│   ├── page.json                    # Default page
│   ├── page.contact.json            # Contact page (use template "contact")
│   ├── page.services.json           # Services overview (template "services")
│   ├── page.about.json              # About (template "about")
│   ├── page.workshops.json          # Groups & workshops (template "workshops")
│   ├── blog.json  article.json      # Blog list / single post
│   ├── product.json collection.json # Digital offerings (courses, programs)
│   ├── cart.json search.json list-collections.json
│   └── 404.json
├── sections/
│   ├── *-group.json                 # Section groups: announcement / header / footer
│   ├── header.liquid footer.liquid announcement-bar.liquid
│   ├── hero-brand.liquid            # Homepage hero (framed image)
│   ├── text-image.liquid service-card-grid.liquid featured-services.liquid
│   ├── testimonial-section.liquid credentials-section.liquid faq-section.liquid
│   ├── blog-feature.liquid newsletter-signup.liquid contact-cta.liquid
│   ├── rich-text-brand.liquid video-section.liquid image-banner.liquid
│   ├── resource-grid.liquid workshop-event-grid.liquid contact-form.liquid
│   ├── tabs.liquid                  # Tabbed types (e.g. Areas of Evaluation)
│   ├── images-with-text-scrolling.liquid  # Sticky "Meet the Team" scroller
│   └── main-*.liquid                # page/blog/article/product/collection/cart/search/404
├── snippets/
│   ├── button.liquid card-service.liquid responsive-image.liquid
│   ├── icon.liquid                  # Inline SVG icon set (no icon fonts)
│   └── seo-meta.liquid              # Meta tags + JSON-LD structured data
└── assets/
    ├── base.css                     # Design system implemented as CSS
    ├── theme.js                     # Drawer, FAQ accordion, video (≈3KB)
    └── section-animations.js        # Optional scroll-reveal (≈0.6KB)
```

Shopify requires this exact top-level folder layout. Keep folder names as-is.

---

## 2. How to upload / deploy

### Option A — Shopify CLI (recommended for developers)
```bash
# Install once: https://shopify.dev/docs/themes/tools/cli
shopify theme push --unpublished        # upload as a new unpublished theme
# or live-preview while editing:
shopify theme dev
```
Run from the repository root (the folder containing `layout/`, `config/`, etc.).

### Option B — Zip upload (no tools)
1. Zip the **contents** of this repo (so `layout/`, `config/`, `sections/`… are
   at the top level of the zip — not nested inside a folder).
   - `docs/`, `README.md`, and `.git/` aren't theme files; harmless if included.
2. Shopify admin → **Online Store → Themes → Add theme → Upload zip file**.
3. Click **Preview** to review, then **Publish** when ready.

### After uploading — one-time setup
- **Navigation:** Shopify menus aren't part of a theme export. In **Content →
  Menus**, ensure a `Main menu` and a `Footer` menu exist (the header/footer
  reference them). Point links at the real pages.
- **Pages:** Create/keep pages and assign templates: Contact → `contact`,
  Services → `services`, About → `about`, Workshops → `workshops`.
- **Images:** Re-link images in the editor (hero, about, clinician) via each
  section's image picker.
- **Blog:** Create a blog (e.g. "Resources") and select it in the homepage
  *Blog / resources* section and the *Blog* template.

---

## 3. Customizing from the Shopify theme editor

Everything visual is editable with **no code**. Open **Online Store → Themes →
Customize**.

### Global settings (Theme settings)
- **Brand colors** — primary (navy), secondary (sky), sand, accent (terracotta),
  background, text.
- **Typography** — brand fonts on by default (Cormorant SC + Montserrat); toggle
  off to pick Shopify fonts. Base font size + heading scale.
- **Layout & spacing** — page width, content width, global section spacing,
  button radius, card radius.
- **Header / Footer** — style, sticky header, logo + mobile logo, logo height.
- **Brand assets & SEO** — favicon, default social share image, business name,
  business type, phone, email, address, areas served (powers local SEO schema).
- **Social links**, **global CTAs**, **animations** on/off.

### Page content (sections & blocks)
- **Add / remove / reorder sections**; drag to reorder.
- **Blocks** (service cards, FAQ items, testimonials, credentials, events,
  resources, footer columns) are individually addable, removable, reorderable.
- Each section exposes: heading, subheading/eyebrow, body, image + **alt text**,
  image position & ratio, text alignment, background scheme, **top/bottom
  padding**, button label/link/style, and mobile behavior.

### The homepage hero
Two columns — text (eyebrow + heading + paragraph + two CTAs) left, image right.
The image sits on an editable **offset frame/holder**: toggle "Show offset frame
behind image" and set the **Frame color** (defaults to terracotta/brown so it
reads as a holder behind the image on a tan background).

### SEO titles & descriptions
Per-page meta title/description are edited in admin: **page/product/blog/article
→ Search engine listing → Edit**. The theme outputs those plus Open Graph/Twitter
tags and JSON-LD automatically.

---

## 4. Structured data (SEO) included
- **Organization + LocalBusiness/Psychologist** (sitewide, from Theme settings)
- **WebSite** search action
- **BlogPosting** on articles, **Product** on products
- **FAQPage** wherever an FAQ section has questions

---

## 5. QA checklist

### Responsiveness
- [ ] Header collapses to the accessible drawer < 750px; drawer traps focus and
      closes on Esc / overlay click.
- [ ] Hero, text+image, and grids stack to one column on mobile; image-first vs
      text-first respected.
- [ ] Grids honor the "two columns on mobile" option where enabled.
- [ ] No horizontal scroll at 320px, 375px, 768px, 1024px, 1440px.
- [ ] Hero offset frame doesn't overflow its column on small screens.

### SEO
- [ ] Exactly one `<h1>` per page.
- [ ] Page titles and meta descriptions set per page in admin.
- [ ] Images have descriptive alt text.
- [ ] JSON-LD validates in Google's Rich Results Test (Org, FAQ, Article, Product).
- [ ] Canonical URLs and Open Graph image present.
- [ ] Local SEO line + areas-served populated.

### Accessibility (WCAG-informed)
- [ ] Keyboard-only: skip link, nav, drawer, FAQ, forms all operable.
- [ ] Visible focus rings everywhere.
- [ ] Contrast: navy on sand, text on background, on-dark text all pass AA.
- [ ] Forms have associated `<label>`s; required fields marked.
- [ ] `prefers-reduced-motion` disables animations and smooth scroll.
- [ ] Color is never the only signal.

### Editor customization
- [ ] Every section can be added, removed, reordered.
- [ ] Every repeatable item is a block.
- [ ] Colors, fonts, spacing, padding, radius all change from the editor.
- [ ] Buttons, images, videos, backgrounds all editable.
- [ ] Toggles (brand fonts, animations, hero frame) behave when off.

### Performance (Core Web Vitals)
- [ ] Hero image eager + `fetchpriority="high"`; all others lazy.
- [ ] Fonts use `display=swap` with preconnect.
- [ ] Only `base.css`, `theme.js`, and (optional) `section-animations.js` load.
- [ ] Lighthouse performance/SEO/accessibility/best-practices reviewed.

---

## 6. Brand family (CFBL · CFBL Institute · MUSA)

One theme renders all three brands, each in its own palette + typography +
logo — and they never mix on a page. The active look is decided **per page** by
the template you assign it (or a `custom.brand_scope` page metafield). See
`docs/DESIGN_SYSTEM.md` §13b.

| Brand | Palette / fonts | Landing | Assign these templates to pages |
| ----- | --------------- | ------- | ------------------------------- |
| **CFBL** | Navy/Sand · Cormorant SC + Montserrat | Home, `about`, `services` | `service` → therapy/supervision/EMDR/etc.; `evaluations` → psychological-evaluations; `workshops`; default `page` for the rest |
| **CFBL Institute** | Forest/Cream · Cormorant SC + Lora | `cfbl-institute` | `professional-trainings`; and assign Institute pages (courses-certification, clinical-supervision, emdr-consultation, professionals) the relevant template or set their `brand_scope` metafield to `institute` |
| **MUSA** | Oxblood/Bone · DM Serif + EB Garamond | `musa` | `author-page`; blog template `essays`; article template `musa` |

**How to assign a template to a page** (no code): in Shopify admin open the
page (or blog/article), and in the **Theme template** dropdown choose the
template (e.g. `service`, `evaluations`, `cfbl-institute`). The brand scope,
colors, fonts, and logo switch automatically.

**Make more service landing pages:** in the theme editor, duplicate the
`service` template (or any template) to create page-specific versions with their
own FAQ/CTA copy — e.g. one per high-value service.

**Reminder:** sections defined in a JSON template are **shared** by every page
using that template. A page's unique prose comes from the page's own content
(rendered by the page header section); the surrounding process/FAQ/CTA bands are
the shared shell. Duplicate the template when a page needs unique band copy.

---

## 7. Notes
- **Optional templates not included:** customer account, password, gift-card.
  Add Shopify defaults or port from the previous theme if customer accounts are
  enabled. Core flows (home, pages, blog, products, collections, cart, search,
  404) are covered.
- **Apps:** the previous store used Mailchimp, Cowlendar (booking), and the
  Google/YouTube widget via App embeds — re-enable under **Theme settings → App
  embeds** if still in use.
- **No external dependencies, no jQuery, no icon fonts, no animation libraries.**
