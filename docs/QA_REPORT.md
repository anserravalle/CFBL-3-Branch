# QA Report

Last run against the full theme. All automated checks pass.

## SEO / structure
- One H1 per template: PASS (39 templates audited; accounts for dynamic heading
  tags and show_title/use_h1 toggles).
- JSON templates / section schemas: all valid.
- No orphan section references in any template `order`.
- Structured data: Organization + LocalBusiness/Psychologist (sitewide), WebSite
  search, BlogPosting (articles), Product (products), FAQPage (FAQ sections).
- Canonical + Open Graph/Twitter meta in `snippets/seo-meta.liquid`.

## Accessibility (WCAG-informed)
- Skip-to-content link present.
- Visible focus states via `:focus-visible` (token `--color-focus`).
- `prefers-reduced-motion` respected (animations + smooth scroll).
- Contact form: 7 labels for 7 visible fields (all inputs labeled).
- Mobile drawer: focus trap + Esc close; tabs: arrow-key nav; FAQ: aria-expanded.
- Contrast: body/headings/eyebrows/links/focus all meet AA on every brand scope
  (eyebrow and link-hover use darkened tokens; Sky Blue never used as body text).

## Performance
- Single base.css, lean theme.js (~5KB), optional section-animations.js (~0.6KB).
- Responsive images via `image_tag` (srcset/sizes); hero eager + fetchpriority;
  others lazy + async. Logo is eager by design (LCP).
- Google Fonts: preconnect + display=swap. No jQuery, icon fonts, or libraries.

## Typography
- Zero em dashes and zero en dashes across the entire repo.

## Mobile
- Breakpoints at 990 / 749 / 480px. Grids collapse to 1 col (2-up option),
  hero/text-image/contact stack, team scroller stacks, tabs list scrolls,
  signature + nav collapse to the drawer.

## Manual checks to do in Shopify after upload
- [ ] Preview each template with real content and images.
- [ ] Run Google Rich Results Test on home, an article, a product, the FAQ page.
- [ ] Lighthouse (mobile + desktop) on home, a service page, a blog post.
- [ ] Tab through every page with the keyboard only.
- [ ] Submit each contact form and confirm it lands in Settings > Notifications.
