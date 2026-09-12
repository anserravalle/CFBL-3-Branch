# Deploying the CFBL theme to Shopify

## A. Get the theme onto your computer
The theme lives in this repo. Either:
- Download the repo as a ZIP from GitHub (Code > Download ZIP), or
- `git clone` the branch.

## B. Make an uploadable ZIP (important structure)
Shopify needs the theme folders at the TOP LEVEL of the zip:
`assets/ config/ layout/ locales/ sections/ snippets/ templates/`

If you downloaded GitHub's zip, open it, go INSIDE the project folder, select
those folders, and compress THOSE into a new zip. You can leave out `docs/`,
`scripts/`, `preview/`, and `README.md` (harmless if included).

CLI alternative (recommended for devs):
```
shopify theme push --unpublished      # uploads as a preview/unpublished theme
shopify theme dev                     # live local preview at localhost:9292
```

## C. Upload (no-code)
Shopify admin > Online Store > Themes > Add theme > Upload zip file.
Click Preview to review safely; your live theme is untouched until you Publish.

## D. One-time setup after upload
1. Menus (Content > Menus): create `main-menu`, `footer`, `footer-for-clients`,
   `footer-for-professionals` per docs/NAVIGATION.md.
2. Pages (Content > Pages): create each page and set its Theme template
   (dropdown) per docs/NAVIGATION.md (e.g. Evaluations -> `evaluations`,
   CFBL Institute -> `cfbl-institute`, ADHD -> `adhd-evaluation`, etc.).
3. Blogs (Content > Blogs): create `make-it-make-sense`, `newsletter`, `essays`
   and assign their templates; tag Make It Make Sense posts with the five themes.
4. Theme settings: upload Logo, CFBL Institute logo, MUSA logo, Favicon, default
   social image; set the cursive Signature image (Header section); confirm phone,
   socials, address.
5. Images: re-pick hero/about/team/eval images in the editor.
6. Products (optional): create a product per workshop/course/training and link
   it in the Workshops & events section for registration (docs/REGISTRATION.md).
7. Customer accounts / password / gift card: Shopify's defaults handle these.

## E. Go live
Preview thoroughly, then Online Store > Themes > Publish.
