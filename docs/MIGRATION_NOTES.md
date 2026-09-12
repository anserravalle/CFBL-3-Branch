# Migration notes - from "Impact" (Maestrooo) to the CFBL custom theme

The previous store ran **Impact v5.2.0** by Maestrooo. This theme is a ground-up
rebuild on a bespoke design system, preserving real content, links, and brand
details. Source content was extracted from the old `templates/index.json`,
page templates, and `config/settings_data.json`.

## Preserved business details
- **Practice owner / clinician:** Dr. Angela (Niki) Serravalle, PsyD, LPCMH, NCC
- **Phone:** (302) 608-3780
- **Instagram:** https://www.instagram.com/centerforbalancedlivingde
- **Facebook:** https://www.facebook.com/Dr.Serravalle
- **LinkedIn:** https://www.linkedin.com/in/dr-niki-serravalle-87103376
- **Service area:** Middletown, Townsend, MOT, plus Wilmington, Newark, Dover (DE)

## Homepage content map (old → new)
| Old (Impact)                         | New section                |
| ------------------------------------ | -------------------------- |
| two-col-layout hero                  | `hero-brand`               |
| slideshow "ABOUT US"                 | `text-image`               |
| rich-text local-SEO line             | `rich-text-brand`          |
| ai_gen "Choose Your Path" 3 cards    | `service-card-grid`        |
| press / clinician quote              | `testimonial-section`      |
| contact form                         | `contact-cta` + contact    |

## Preserved page handles (link targets kept intact)
about-us, services, contact, faq, credentials, individual-therapy,
psychological-evaluations, adhd-evaluation, autism-evaluation,
diagnostic-clarification, personality-and-emotional, academic-and-learning,
clinical-supervision, emdr-consultation, professional-trainings,
courses-certification, cfbl-institute, musa, wellness-groups, workshops,
careers, client-portal, professionals, newsletter, event-calendar.

Local landing pages also preserved: therapy-middletown-delaware,
therapy-newark-delaware, therapy-dover-delaware, and the Wilmington page.

## Collections preserved
courses, educational-programs, groups, workshops, services-collection.

## Apps in use on the old store (re-add via App embeds / blocks if still used)
- Mailchimp Email/SMS
- Cowlendar booking
- Google & YouTube channel widget

## Not carried over (intentionally)
- Impact's `theme.js`/`sections.js` (200KB+), PhotoSwipe, country-flags assets,
  and the heavy custom CSS - replaced by a lean `base.css` + `theme.js`.
- Per-section inline `custom_css` font hacks (e.g. `h2 {font-size:70px}`) -
  replaced by the design-system type scale and editor settings.
