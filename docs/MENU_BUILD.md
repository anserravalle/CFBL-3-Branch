# Menu build guide (Content > Menus)

How to add an item: Content > Menus > open the menu > **Add menu item** > type the
**Name** > click the **Link** box and PICK the page/blog from the search list
(this guarantees the right URL) > to make a dropdown child, drag it slightly
right under its parent > **Save**.

Tip: link by picking from the list, not by typing URLs. Your page titles are long
(e.g. "Services at Center for Balanced Living"), so the search picker avoids
broken links.

### Known handle quirks (from your URL Redirects)
Your live page handles do NOT all match their short names. Shopify is already
redirecting the old short links to these, so old bookmarks and Google results
keep working. You do not need to create or rename any pages. When the picker
shows a page, these are the real handles behind the titles:

- About  ->  `about-us-1`  (old `/pages/about` redirects here)
- MUSA  ->  `musa-writing`  (old `/pages/musa` redirects here)
- Career Development  ->  `career-development`  (old `/pages/careers` redirects here)
- Professional Clinical Trainings  ->  `professional-clinical-trainings`
  (there is also a typo'd `clinicial-trainings` redirect; ignore it, pick the
  correctly spelled page)
- Individual Therapy  ->  `therapy-bear-delaware`
- Our Approach  ->  `our-approach`

Because these differ, ALWAYS pick from the search list. Do not hand-type
`/pages/about` etc., or you will hit a redirect chain instead of the page.

---

## Main menu (header)

- **For Clients**  -> Services page
  - About Us  -> About Us page
  - Our Credentials  -> Credentials page
  - Individual Therapy  -> Individual Therapy page
  - Psychological Evaluations  -> Psychological Evaluations page
  - Wellness Groups  -> Welcome To Our Wellness Groups page
  - FAQ  -> FAQ page
- **For Professionals**  -> CFBL Institute page
  - Professional Clinical Trainings  -> Professional Clinical Trainings page
  - Workshops  -> Workshops page
  - Courses & Certification  -> Courses & Certification page
- **Career Development**  -> Clinical Supervision page (or its own landing)
  - Clinical Supervision  -> Clinical Supervision page
  - EMDR Consultation  -> EMDR Consultation page
  - Join Our Team  -> Join Our Team page
- **About Us**  -> About Us page
  - Meet the Team  -> About Us page
  - (optional) individual clinician bio pages
- **MUSA**  -> Musa page
  - Essays  -> Essays blog
  - (Books - add later when ready)
- **Letters from the Practice**  -> Letters from CFBL blog
- **Make It Make Sense**  -> Make It Make Sense blog
- **Contact**  -> Start The Conversation page

---

## Footer menus

**footer** (Explore column)
- Contact  -> Start The Conversation page
- Privacy Practices  -> Privacy Practices page
- Letters from the Practice  -> Letters from CFBL blog
- CFBL Institute  -> CFBL Institute page

**footer-for-clients**
- Therapy  -> Individual Therapy page
- Evaluations  -> Psychological Evaluations page
- Wellness Groups  -> Welcome To Our Wellness Groups page
- Client Portal  -> Client Portal page (or the SimplePractice URL)
- FAQ  -> FAQ page

**footer-for-professionals**
- Join Our Team  -> Join Our Team page
- Workshops  -> Workshops page
- Courses & Certification  -> Courses & Certification page
- Professional Clinical Trainings  -> Professional Clinical Trainings page
- EMDR Consultation  -> EMDR Consultation page
- Clinical Supervision  -> Clinical Supervision page

---

## Blog templates (Content > Blog posts > Manage blogs > each blog > Theme template)
- Make It Make Sense  -> `make-it-make-sense`
- Letters from CFBL    -> `newsletter`
- Essays               -> `essays` (and set its article template to `musa`)

---

## MUSA note
MUSA covers psychology, relationships, the moment, and the fragility of being
human. "Books" gets added to the MUSA dropdown later when there is a books page.

---

## Final pre-publish checklist
- [ ] Blog templates set (3)
- [ ] Main menu built and saved
- [ ] Footer menus built and saved
- [ ] Preview the theme; click every nav item; confirm none 404
- [ ] Logo, sub-brand logos, signature, favicon set in Theme settings
- [ ] Publish (Online Store > Themes > Publish)
