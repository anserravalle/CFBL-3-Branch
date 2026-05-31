#!/usr/bin/env python3
"""Standalone marble-background comparison preview (gold flecks vs grey flecks).
Pulls the real base.css so colors/typography match the live theme. Output:
preview/CFBL-marble-compare.html
"""
import os
css = open('assets/base.css').read()

# Two CSS-only marble textures. A soft off-white base (layered radial "veining")
# plus scattered flecks via multiple tiny radial-gradients. Lightweight, no images.
def marble(fleck, vein):
    return f"""
  background-color: #FBF7F1;
  background-image:
    radial-gradient(1.5px 1.5px at 12% 22%, {fleck} 40%, transparent 42%),
    radial-gradient(1.2px 1.2px at 28% 64%, {fleck} 40%, transparent 42%),
    radial-gradient(1.6px 1.6px at 45% 35%, {fleck} 40%, transparent 42%),
    radial-gradient(1.1px 1.1px at 61% 78%, {fleck} 40%, transparent 42%),
    radial-gradient(1.7px 1.7px at 74% 18%, {fleck} 40%, transparent 42%),
    radial-gradient(1.2px 1.2px at 83% 52%, {fleck} 40%, transparent 42%),
    radial-gradient(1.4px 1.4px at 92% 88%, {fleck} 40%, transparent 42%),
    radial-gradient(1.1px 1.1px at 38% 92%, {fleck} 40%, transparent 42%),
    radial-gradient(1.3px 1.3px at 6% 80%, {fleck} 40%, transparent 42%),
    radial-gradient(1.5px 1.5px at 54% 12%, {fleck} 40%, transparent 42%),
    radial-gradient(ellipse 60% 40% at 20% 30%, {vein} 0%, transparent 60%),
    radial-gradient(ellipse 50% 35% at 80% 70%, {vein} 0%, transparent 60%),
    radial-gradient(ellipse 70% 50% at 60% 20%, {vein} 0%, transparent 55%);
  background-size: 240px 240px, 240px 240px, 240px 240px, 240px 240px, 240px 240px, 240px 240px, 240px 240px, 240px 240px, 240px 240px, 240px 240px, 100% 100%, 100% 100%, 100% 100%;
"""

gold = marble("rgba(193,165,114,0.55)", "rgba(193,165,114,0.06)")   # champagne gold flecks
grey = marble("rgba(120,120,120,0.40)", "rgba(120,120,120,0.05)")   # soft grey flecks

def block(label, marble_css):
    return f"""
<section style="{marble_css}">
  <div class="page-width" style="padding-block:64px;">
    <p style="text-align:center;font-family:var(--font-body);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#9D654E;margin-bottom:28px;font-weight:600;">{label}</p>

    <!-- Hero-style on the marble -->
    <div class="hero__grid has-media" style="margin-bottom:48px;">
      <div class="hero__content">
        <p class="eyebrow hero__eyebrow">Trauma-Informed Psychological Care</p>
        <h1 class="hero__title">Your Path To Healing Begins Here</h1>
        <div class="hero__lead"><p>Center for Balanced Living offers therapy, psychological evaluations, consultation, supervision, and educational services grounded in trauma-informed, research-based care.</p></div>
        <div class="btn-row"><a href="#" class="btn btn--primary btn--lg">Start the Conversation</a><a href="#" class="btn btn--secondary">Explore Services</a></div>
      </div>
      <div class="hero__media hero__media--framed" style="--frame-color:#9D654E;"><div class="media media--4-3" style="display:grid;place-items:center;background:#e7d4c0;color:#2b5275;font-family:var(--font-heading);font-size:1.3rem;">Image placeholder</div></div>
    </div>

    <!-- A heading + paragraph directly on the marble (readability test) -->
    <div style="max-width:760px;margin:0 auto;text-align:center;">
      <h2>Text directly on the background</h2>
      <p style="color:var(--color-text);">This shows how body copy reads when it sits straight on the marble surface, with no white card behind it. Notice whether the flecks and veining make the words harder to read.</p>
    </div>

    <!-- White cards on the marble (how sections with cards would look) -->
    <div class="grid grid--3" style="margin-top:40px;">
      <article class="card card--elevated"><span class="card__icon">&#9679;</span><h3 class="card__title">Begin Therapy</h3><div class="card__body"><p>Support for healing and change.</p></div></article>
      <article class="card card--elevated"><span class="card__icon">&#9679;</span><h3 class="card__title">Get an Evaluation</h3><div class="card__body"><p>Clarity for diagnosis and next steps.</p></div></article>
      <article class="card card--elevated"><span class="card__icon">&#9679;</span><h3 class="card__title">Learn With Us</h3><div class="card__body"><p>Training, supervision, and consultation.</p></div></article>
    </div>
  </div>
</section>
"""

# A plain sand band between the two for honest comparison to what you have now
sand_block = """
<section class="bg--sand">
  <div class="page-width" style="padding-block:48px;text-align:center;">
    <p style="font-family:var(--font-body);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#9D654E;font-weight:600;margin-bottom:16px;">For comparison: your current Sand background (no texture)</p>
    <h2>Your Path To Healing Begins Here</h2>
    <p style="max-width:620px;margin:0 auto;color:var(--color-text);">This is the warm, untextured background the theme uses today.</p>
  </div>
</section>
"""

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CFBL Marble Background Comparison</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500;600;700&family=Cormorant:ital,wght@0,500;1,400;1,500&family=Montserrat:wght@300;400;500;600&display=swap">
<style>{css}
.compare-note{{position:fixed;top:0;left:0;right:0;z-index:50;background:#1E3C57;color:#fff;font-family:Montserrat,sans-serif;font-size:13px;text-align:center;padding:8px;}}
body{{padding-top:36px;}}
</style></head>
<body class="brand--cfbl">
<div class="compare-note">Marble background comparison &middot; scroll to see Gold flecks, Grey flecks, and your current Sand</div>
{block("Option A &mdash; Gold flecks (champagne)", gold)}
{block("Option B &mdash; Grey flecks (soft stone)", grey)}
{sand_block}
</body></html>"""

open('preview/CFBL-marble-compare.html','w').write(html)
print("wrote preview/CFBL-marble-compare.html", len(html), "bytes")
