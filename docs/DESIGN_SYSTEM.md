# Center for Balanced Living — Design System

This document defines the design system **before** any section styling. Every
section, block, and snippet in the theme inherits from these decisions. Do not
improvise section styling independently — extend the tokens and rules below.

---

## 1. Brand foundation

**Practice:** Center for Balanced Living — a trauma-informed clinical
psychology practice serving Middletown, Townsend, and the greater MOT area of
Delaware.

**Personality:** warm, grounded, polished, trustworthy, clinically
sophisticated. Never trendy, casual, influencer-like, wellness-generic, or
salesy.

**Voice:** an experienced licensed psychologist who is also a businesswoman —
warm, accessible, hopeful, research-informed, relational. Uses "we" for the
practice team. Avoids wellness clichés, "journey" language, and overpromising.

---

## 2. Color tokens

| Token              | Hex        | Role                                             |
| ------------------ | ---------- | ------------------------------------------------ |
| `--color-navy`     | `#2B5275`  | Primary. Headlines, primary buttons, key accents |
| `--color-sky`      | `#4E9FBF`  | Secondary. Links, secondary accents, hover       |
| `--color-sand`     | `#EED9C5`  | Warm background base, soft color fields           |
| `--color-terracotta`| `#9D654E` | Accent. Used sparingly — one accent at a time     |

**Derived / utility colors** (computed to maintain contrast):

| Token                  | Value        | Role                              |
| ---------------------- | ------------ | --------------------------------- |
| `--color-bg`           | `#FBF6F0`    | Page background (lightened sand)  |
| `--color-bg-sand`      | `#EED9C5`    | Section background (sand)         |
| `--color-surface`      | `#FFFFFF`    | Cards, elevated surfaces          |
| `--color-text`         | `#2A2724`    | Body text (warm near-black)       |
| `--color-heading`      | `#2B5275`    | Headings (navy)                   |
| `--color-muted`        | `#6B6258`    | Captions, meta, muted text        |
| `--color-border`       | `#E2D3C2`    | Hairlines, dividers               |
| `--color-navy-dark`    | `#1E3C57`    | Navy hover / footer               |
| `--color-on-dark`      | `#FBF6F0`    | Text on navy/dark surfaces        |

**Contrast rules (WCAG AA):**
- Body text `#2A2724` on `#FBF6F0` → ~13:1 (AAA).
- Navy `#2B5275` on sand `#EED9C5` → ~5.4:1 (AA for normal text).
- On-dark text `#FBF6F0` on navy `#2B5275` → ~8:1 (AAA).
- Never use Sky Blue for normal-size body text on light backgrounds (fails AA);
  reserve it for large text, borders, and UI accents, or darken to navy.
- Never rely on color alone to convey meaning — pair with text, icon, or shape.

---

## 3. Typography

**Families:**
- Headings / section titles: **Cormorant SC** (serif, small-caps display).
- Body, UI, nav, buttons, captions, forms: **Montserrat** (humanist sans).

Loaded via Google Fonts with `display=swap` and preconnect. Body font is also
available as Shopify `font_picker` settings so the owner can change them.

**Type scale** (modular, base 16px, ratio ≈ 1.25 — owner-adjustable via
`heading_scale`):

| Token        | rem    | Use                                    |
| ------------ | ------ | -------------------------------------- |
| `--fs-xs`    | 0.78   | Eyebrows, captions, legal              |
| `--fs-sm`    | 0.875  | Meta, small UI                         |
| `--fs-base`  | 1.0    | Body                                   |
| `--fs-md`    | 1.15   | Lead paragraphs, subheads              |
| `--fs-lg`    | 1.4    | H4 / card titles                       |
| `--fs-xl`    | 1.85   | H3                                     |
| `--fs-2xl`   | 2.4    | H2                                     |
| `--fs-3xl`   | 3.2    | H1 / hero                              |
| `--fs-4xl`   | 4.0    | Display hero (optional)                |

Headings scale fluidly with `clamp()` between mobile and desktop. The owner's
`heading_scale` setting multiplies heading sizes globally.

**Weights:** Cormorant SC 500/600/700; Montserrat 300/400/500/600.
**Line-height:** headings 1.1–1.2; body 1.65; tight UI 1.3.
**Letter-spacing:** eyebrows `0.14em` uppercase; Cormorant SC headings `0.01em`.

---

## 4. Spacing scale

8px base grid. Tokens:

| Token        | px   | Token        | px   |
| ------------ | ---- | ------------ | ---- |
| `--space-2`  | 2    | `--space-24` | 24   |
| `--space-4`  | 4    | `--space-32` | 32   |
| `--space-8`  | 8    | `--space-40` | 40   |
| `--space-12` | 12   | `--space-48` | 48   |
| `--space-16` | 16   | `--space-64` | 64   |
| `--space-20` | 20   | `--space-80` | 80   |

**Section rhythm:** vertical padding defaults to a global setting
(`--section-spacing`, default 80px desktop / scales down on mobile). Each section
can override top/bottom padding (0–160px) from the editor. Consecutive sections
of the same background color collapse rhythm naturally via consistent padding.

---

## 5. Layout & containers

- `--page-max-width`: default **1280px** (owner-adjustable).
- `--section-max-width`: default **1100px** content measure (owner-adjustable).
- Reading measure for long-form text: **68ch** max.
- Gutters: `clamp(20px, 5vw, 64px)`.
- Grid: 12-col conceptual; components use CSS grid with `auto-fit/minmax`.

---

## 6. Radius, borders, shadows

- `--radius-button`: default 999px (pill) — owner-adjustable.
- `--radius-card`: default 16px — owner-adjustable.
- `--radius-image`: inherits card radius; ratio-controlled.
- Borders: 1px `--color-border` hairlines.
- Shadows (soft, low, no harsh): 
  - `--shadow-sm`: `0 1px 2px rgba(43,82,117,.06)`
  - `--shadow-md`: `0 6px 24px rgba(43,82,117,.08)`
  - `--shadow-lg`: `0 18px 48px rgba(43,82,117,.10)`
- No harsh gradients. Optional single soft radial "brand shape" field only when
  it supports hierarchy.

---

## 7. Button hierarchy

| Level         | Style                                                        |
| ------------- | ----------------------------------------------------------- |
| **Primary**   | Navy fill, on-dark text, pill radius. Main CTA per section.  |
| **Secondary** | Navy outline, navy text, transparent fill.                  |
| **Tertiary**  | Text link with underline-on-hover + arrow. Low emphasis.    |
| **On-dark**   | Sand fill / navy text, OR sand outline on navy backgrounds.  |

Rules: one primary button per section. Min target 44×44px. Visible focus ring
(2px sky outline + offset). Button text, link, and style are all editor fields.

---

## 8. Card rules

- Surface white, `--radius-card`, `--shadow-md`, 1px border optional.
- Padding `--space-32`. Internal rhythm: eyebrow → title (H3) → body → CTA.
- Hover: lift `translateY(-4px)` + shadow-lg (disabled under reduced-motion).
- Service cards: optional icon/image (1:1 or 4:3), title, 1–2 line body, link.
- Equal-height via grid; content top-aligned, CTA bottom-aligned.

---

## 9. Image ratios

| Context             | Ratio          |
| ------------------- | -------------- |
| Hero                | 4:3 / 16:9 / natural (editor option) |
| Text + image        | 4:3 (default), 1:1, 3:2, natural     |
| Service card icon   | 1:1            |
| Card / resource     | 3:2            |
| Testimonial avatar  | 1:1 (circle)   |
| Blog thumbnail      | 3:2            |
| Banner              | 16:9 / 21:9    |

All images responsive (`srcset`/`sizes`), lazy-loaded except LCP/hero (eager).
Focal point honored via Shopify `image.presentation.focal_point`. Every image
setting has a paired `alt` text field.

---

## 10. Section rhythm & composition

A section = optional eyebrow → heading (H2) → optional subheading/body →
content → optional CTA row. Alignment (left/center) is an editor option;
default left for editorial feel, center for hero and CTA bands.

Background options per section: Background (bg), Sand, White (surface), Navy
(dark), Terracotta-tint. Text color auto-pairs but is overridable. Only one
graphic accent per section.

---

## 11. Mobile behavior

- Breakpoints: `--bp-sm: 480px`, `--bp-md: 750px`, `--bp-lg: 990px`,
  `--bp-xl: 1200px`.
- Multi-column grids collapse to 1 col < 750px (owner can choose 1 or 2 for
  some grids via "mobile columns").
- Two-column text+image stacks; owner chooses image-first or text-first on
  mobile.
- Heading sizes scale down via `clamp()`. Section padding scales ~0.6×.
- Nav collapses to an accessible slide-in drawer with focus trap.
- Touch targets ≥ 44px; no hover-only interactions.

---

## 12. Motion

- Subtle only: fade/translate ≤ 12px, 400–600ms ease-out, on scroll-in.
- Globally toggleable (`enable_animations`).
- Always wrapped in `@media (prefers-reduced-motion: no-preference)`.
- No animation libraries; ~1KB IntersectionObserver in `section-animations.js`.

---

## 13. Accessibility commitments

- One H1 per page; logical H2/H3 nesting.
- Semantic landmarks: `header`, `nav`, `main`, `section`, `footer`.
- Visible focus states; skip-to-content link.
- Keyboard-operable menu/drawer/accordion with ARIA.
- Form inputs always have associated `<label>`.
- Color never the sole signal.
- `prefers-reduced-motion` respected.

---

## 13b. Sub-brand scopes (CFBL · Institute · MUSA)

The brand family shares an author and a clinical sensibility but **must not mix
palettes, fonts, or voice within a single page**. The theme supports three
scopes via a `body` class set by `layout/theme.liquid` (resolved in
`snippets/brand-scope.liquid`):

| Scope         | Primary anchor | Ground         | Headline           | Body          |
| ------------- | -------------- | -------------- | ------------------ | ------------- |
| `cfbl` (default) | Deep Navy `#2B5275` | Sand `#EED9C5` | Cormorant SC | Montserrat |
| `institute`   | Forest `#3D5A52` | Cream `#EAE2D0` | Cormorant SC | Lora |
| `musa`        | Oxblood `#6E1F23` | Bone `#F1E8D8` | DM Serif Display | EB Garamond |

**How scope is chosen** (priority): page metafield `custom.brand_scope` →
page template suffix (e.g. a page using template `page.cfbl-institute` →
`institute`; `page.musa` / `page.author-page` → `musa`) → default `cfbl`.

Because every component references design tokens only, applying `.brand--*`
re-maps the entire page (header, sections, footer) automatically. The header
and footer also swap to the matching logo (CFBL rainbow tree / Institute /
MUSA) from theme settings. Fonts for the active scope are the only ones loaded,
keeping each page lean. Voice differences (warm vs. peer-to-peer vs. literary,
and the absence of marketing CTAs on MUSA) live in each scoped template's copy.

## 14. Performance commitments

- System/Google fonts with `swap`; preconnect.
- Single `base.css`; minimal `theme.js`; optional tiny animation file.
- Responsive `srcset` + `sizes`; `loading="lazy"` + `decoding="async"` for
  non-critical images; hero eager + `fetchpriority="high"`.
- No jQuery, no heavy frameworks, no per-feature apps.
- CSS custom properties set once on `:root` from theme settings.
