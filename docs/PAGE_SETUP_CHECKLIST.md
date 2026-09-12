# Page setup checklist (assign templates / create pages)

How Shopify works: a **template** is a layout; a **page** is the real thing at a
URL. A template does nothing until a Page uses it. For each row below:

1. Content > Pages. If the page already exists (from the old site), open it.
   If not, click **Add page** and give it the Title shown.
2. On the right, set **Theme template** to the template in the second column.
3. Save. Then add/swap images and copy in the theme editor (Customize).
4. Add it to the right menu (see the bottom section).

Tip: many of these pages already exist from your old site, so it's often just a
**template dropdown change**, not a new page. Only the ones marked NEW are likely
missing.

---

## For Clients (CFBL)

- [ ] Services                  -> template `services`
- [ ] About Us                  -> template `about`
- [ ] Contact                   -> template `contact`
- [ ] FAQ                        -> template `faq`
- [ ] Our Credentials           -> template `credentials`
- [ ] Individual Therapy        -> template `individual-therapy`
- [ ] Psychological Evaluations -> template `evaluations`
- [ ] Wellness Groups           -> template `wellness-groups`
- [ ] Client Portal             -> template `client-portal`  (set the real portal URL on the hero button)
- [ ] Privacy Practices  (NEW)  -> template `privacy-practices`  (paste your Notice text into the page body)

### Evaluation detail pages (linked from the Evaluations tabs)
- [ ] ADHD Evaluation           -> template `adhd-evaluation`
- [ ] Autism Evaluation         -> template `autism-evaluation`
- [ ] Diagnostic Clarification  -> template `diagnostic-clarification`
- [ ] Personality & Emotional   -> template `personality-and-emotional`
- [ ] Academic & Learning       -> template `academic-and-learning`

---

## For Professionals / Career Development (Institute, Forest look)

- [ ] CFBL Institute            -> template `cfbl-institute`
- [ ] Professional Trainings    -> template `professional-trainings`
- [ ] Courses & Certification   -> template `courses-certification`
- [ ] Career Development  (NEW) -> template `career-development`
- [ ] Clinical Supervision      -> template `clinical-supervision`
- [ ] EMDR Consultation         -> template `emdr-consultation`
- [ ] Join Our Team       (NEW) -> template `join-our-team`

---

## About Us / team bios

- [ ] Each clinician's bio page (Niki, Amanda, Kirsten, Brianna, etc.)
      -> template `team-member`   (add photo, role, phone, email, bio per person)

The reusable `service` template is also available if you want a quick designed
landing for any other service not listed above.

---

## MUSA (Oxblood look)

- [ ] MUSA                      -> template `musa`

---

## Blogs (Content > Blogs > Manage blogs)

Create the blog, then set its Theme template:

- [ ] Make It Make Sense (handle `make-it-make-sense`) -> blog template `make-it-make-sense`
      Tag posts: The Field, On Therapy, On Diagnostics, The Cultural Moment, Being Human
- [ ] Newsletter (handle `newsletter`)                 -> blog template `newsletter`
- [ ] Essays (handle `essays`)                         -> blog template `essays`
      Set its article template to `musa`

---

## Menus (Content > Menus)

**Main menu** (header):
- For Clients -> /pages/services
  - About Us, Our Credentials, FAQ, Individual Therapy, Evaluations, Wellness Groups
- For Professionals -> /pages/cfbl-institute
  - Professional Trainings, Workshops, Courses & Certification, FAQ
- Career Development -> /pages/career-development
  - Clinical Supervision, EMDR Consultation, Join Our Team
- About Us -> /pages/about-us  (+ individual bio pages)
- MUSA -> /pages/musa
- Newsletter -> /blogs/newsletter
- Make It Make Sense -> /blogs/make-it-make-sense
- Contact Us -> /pages/contact

**footer**: Contact Us, Privacy Practices, Newsletter, CFBL Institute
**footer-for-clients**: Therapy, Evaluations, Wellness Groups, Client Portal, FAQ
**footer-for-professionals**: Join Our Team, Workshops, Courses & Certification,
  Professional Trainings, EMDR Consultation, Supervision

---

## Quick way to verify a page is live
Visit yourstore.com/pages/<handle> (e.g. /pages/career-development).
- Designed layout shows -> template assigned correctly.
- 404 or plain text -> page not created or template not set yet.
