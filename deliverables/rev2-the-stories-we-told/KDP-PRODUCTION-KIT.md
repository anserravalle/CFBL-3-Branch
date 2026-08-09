# The Stories We Told — KDP Print Cover Production Kit

**Why this exists:** the design comps in `comps/` are low-resolution direction built on a
flattened JPEG with the text baked into the art. They cannot be uploaded to KDP. A print
cover must be assembled at 300 DPI from **clean, high-resolution artwork** (the couple/smoke
image with no text on it). This kit has everything needed to build that file — the exact
dimensions, the finalized copy, and the specs — so it can be assembled cleanly once the
high-res art exists.

---

## The one blocker: high-resolution art

The cover art is AI-generated and low-resolution, with the title/subtitle already burned in.
To finish, we need the **base couple/smoke image, text-free, at print resolution.** Options,
best first:

1. **Regenerate** it in the same AI tool at its largest output (2K–4K), with **no text**, and
   framed a little loose so it can be cropped to trim + bleed.
2. **AI-upscale** the existing art (Topaz, Photoshop "Super Resolution," Canva enhancer, or a
   free upscaler) to at least the pixel sizes below. Atmospheric art upscales tolerably;
   text does not — which is why the text must be re-set fresh, not upscaled.

Once that art exists, the type below is dropped on top crisply and exported.

---

## Exact dimensions (300 DPI)

Full cover is **one wrap**: back + spine + front, plus 0.125" bleed on all four sides.

**Trim 6" × 9" (standard memoir):**
- Height: 9" + 0.25" bleed = **2775 px**
- Front (and back) width: 6" + 0.125" outer bleed = 6.125" = **1837 px** each
- Spine width depends on page count (below), added between them.

**Full-wrap width = 1837 (back) + spine + 1837 (front).**

**Spine width by page count** (black-and-white interior):
| Paper | Formula | 200 pg | 250 pg | 300 pg |
|---|---|---|---|---|
| White (60#) | pages × 0.002252" × 300 | 135 px | 169 px | 203 px |
| Cream (60#) | pages × 0.0025" × 300 | 150 px | 188 px | 225 px |

> Fill in your final page count and paper. Example: 6×9, 260 pages, cream →
> spine ≈ 195 px → full wrap ≈ 1837 + 195 + 1837 = **3869 × 2775 px**.

**Safe zone:** keep all text ≥ 0.25" (75 px) inside every trim edge and ≥ 0.0625" (19 px)
off the spine folds. Text on the spine only if page count ≥ 100.

---

## Finalized copy (paste-ready)

**Front**
- Title: **The Stories We Told**
- Subtitle (two lines, oxblood small caps): **THE DANCE BETWEEN A CODEPENDENT / AND A COMPULSIVE LIAR**
- Below subtitle (cream small caps, smaller, space above): **A MEMOIR**
- Author: **NIKI SERRAVALLE** (no credentials on the front)

**Spine:** The Stories We Told  ·  NIKI SERRAVALLE

**Back — description (first-person DRAFT; replace with the book's approved copy):**
> In *The Stories We Told*, I examine the intimate and disorienting bond between a codependent
> and a compulsive liar. Through a deeply personal memoir, I trace the emotional logic of
> attachment, the seduction of explanation, and the slow unraveling that occurs when love
> becomes organized around confusion, rescue, and self-betrayal.
>
> This is a story about longing, self-deception, trauma, and the narratives we build to survive
> what we cannot yet bear to name. With psychological insight and emotional precision, I invite
> you into the complicated dance between truth and illusion, and the cost of confusing being
> chosen with being loved.

**Back — author bio:**
> **NIKI SERRAVALLE, PSY.D., LPCMH, NCC** is a psychologist specializing in clinical
> psychological evaluation, and a trauma-informed therapist. She is the founder of the Center
> for Balanced Living in Delaware and a sought-after speaker and educator. Her work lives at the
> intersection of psychology, nature-based sciences, integrated trauma care, and the human
> stories that shape who we become.

**Back — website:** balancedlivingde.com
**Back — photo:** `comps/author-headshot_BW_natural.png` (or `_color_natural.png`) — high-res, ready.
**No em dashes anywhere in the cover copy.**

---

## Type & color specs

- **Title** — high-contrast Didone display serif (the comp uses one like *InstrumentSerif* or
  *Gloock*). Cream **#EEE5DA**. Stacked: "The / Stories / We / Told," with "Stories" and "Told"
  large and "The"/"We" smaller.
- **Subtitle / "A Memoir" / spine / bio heading** — classical serif small caps, generous
  letterspacing. Oxblood **#A56E6A** for the subtitle and headings; cream **#EEE5DA** for
  "A Memoir."
- **Body (back blurb + bio)** — old-style serif (e.g., a Garamond/Minion), warm off-white
  **#DAD6D0**, ~11–12 pt, left-aligned.
- **Threads / accents** — oxblood, carried in the art.
- **Tonal direction** — upper third and left edge lifted toward warm stone/bone; lower-right
  kept dark (see the two lift options in `comps/`).

---

## Two ways to finish

**A. I assemble it.** Send me: (1) the base art text-free at the pixel sizes above, and
(2) your trim size, final page count, and paper (white/cream). I'll build the full wrap to the
KDP template and export a print-ready PDF.

**B. You assemble it** in Canva (KDP cover template), Affinity/Photoshop, or Amazon's free KDP
Cover Creator, using this kit. I'll supply any element (crisp type as PNGs, the headshot,
color values) on request.
