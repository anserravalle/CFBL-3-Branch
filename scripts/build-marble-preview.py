#!/usr/bin/env python3
"""Marble-background comparison preview (gold vs grey), now with VISIBLE veining
at three intensities. CSS-only (no images). Output: preview/CFBL-marble-compare.html
"""
css = open('assets/base.css').read()

def marble(vein, fleck, strength):
    """vein/fleck = rgba color strings; strength scales opacity of veins."""
    v = strength
    return f"""
  background-color: #FBF7F1;
  background-image:
    /* diagonal marble veins (visible) */
    linear-gradient(115deg, transparent 0 14%, {vein.format(a=0.0)} 14%, {vein.format(a=v)} 15%, {vein.format(a=0.0)} 16%, transparent 16% 100%),
    linear-gradient(125deg, transparent 0 38%, {vein.format(a=0.0)} 38%, {vein.format(a=v*0.7)} 39.5%, {vein.format(a=0.0)} 41%, transparent 41% 100%),
    linear-gradient(100deg, transparent 0 62%, {vein.format(a=0.0)} 62%, {vein.format(a=v)} 63%, {vein.format(a=0.0)} 64.5%, transparent 65% 100%),
    linear-gradient(135deg, transparent 0 80%, {vein.format(a=0.0)} 80%, {vein.format(a=v*0.6)} 81%, {vein.format(a=0.0)} 82%, transparent 82% 100%),
    /* fine cross veins */
    linear-gradient(60deg, transparent 0 30%, {vein.format(a=v*0.4)} 31%, transparent 31.6% 100%),
    linear-gradient(70deg, transparent 0 70%, {vein.format(a=v*0.4)} 71%, transparent 71.6% 100%),
    /* scattered flecks */
    radial-gradient(2px 2px at 18% 26%, {fleck} 45%, transparent 47%),
    radial-gradient(2px 2px at 47% 64%, {fleck} 45%, transparent 47%),
    radial-gradient(2px 2px at 73% 34%, {fleck} 45%, transparent 47%),
    radial-gradient(2px 2px at 88% 72%, {fleck} 45%, transparent 47%),
    radial-gradient(2px 2px at 33% 88%, {fleck} 45%, transparent 47%),
    radial-gradient(2px 2px at 61% 14%, {fleck} 45%, transparent 47%);
  background-size: 100% 100%, 100% 100%, 100% 100%, 100% 100%, 100% 100%, 100% 100%, 320px 320px, 320px 320px, 320px 320px, 320px 320px, 320px 320px, 320px 320px;
"""

gold_v = "rgba(176,141,87,{a})"
gold_f = "rgba(193,165,114,0.7)"
grey_v = "rgba(110,110,110,{a})"
grey_f = "rgba(120,120,120,0.55)"

def block(label, marble_css):
    return f"""
<section style="{marble_css}">
  <div class="page-width" style="padding-block:56px;">
    <p style="text-align:center;font-family:var(--font-body);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#9D654E;margin-bottom:24px;font-weight:600;">{label}</p>
    <div class="hero__grid has-media" style="margin-bottom:40px;">
      <div class="hero__content">
        <p class="eyebrow hero__eyebrow">Trauma-Informed Psychological Care</p>
        <h1 class="hero__title">Your Path To Healing Begins Here</h1>
        <div class="hero__lead"><p>Therapy, evaluations, consultation, and education, grounded in trauma-informed care.</p></div>
        <div class="btn-row"><a href="#" class="btn btn--primary btn--lg">Start the Conversation</a><a href="#" class="btn btn--secondary">Explore Services</a></div>
      </div>
      <div class="hero__media hero__media--framed" style="--frame-color:#9D654E;"><div class="media media--4-3" style="display:grid;place-items:center;background:#e7d4c0;color:#2b5275;font-family:var(--font-heading);">Image</div></div>
    </div>
    <div style="max-width:760px;margin:0 auto 32px;text-align:center;">
      <h2>Text directly on the background</h2>
      <p style="color:var(--color-text);">Body copy sitting straight on the marble, no white card behind it. Check whether the veins make it harder to read.</p>
    </div>
    <div class="grid grid--3">
      <article class="card card--elevated"><h3 class="card__title">Begin Therapy</h3><div class="card__body"><p>Support for healing and change.</p></div></article>
      <article class="card card--elevated"><h3 class="card__title">Get an Evaluation</h3><div class="card__body"><p>Clarity for diagnosis and next steps.</p></div></article>
      <article class="card card--elevated"><h3 class="card__title">Learn With Us</h3><div class="card__body"><p>Training, supervision, consultation.</p></div></article>
    </div>
  </div>
</section>
"""

sections = ""
for name, v, f in [("GOLD", gold_v, gold_f), ("GREY", grey_v, grey_f)]:
    for lvl, s in [("subtle", 0.12), ("medium", 0.22), ("bold", 0.38)]:
        sections += block(f"{name} veins &mdash; {lvl}", marble(v, f, s))

sand_block = """
<section class="bg--sand"><div class="page-width" style="padding-block:48px;text-align:center;">
<p style="font-family:var(--font-body);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#9D654E;font-weight:600;margin-bottom:16px;">For comparison: current Sand (no texture)</p>
<h2>Your Path To Healing Begins Here</h2><p style="max-width:620px;margin:0 auto;color:var(--color-text);">The warm, untextured background the theme uses today.</p>
</div></section>
"""

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CFBL Marble Comparison</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500;600;700&family=Cormorant:ital,wght@0,500;1,400;1,500&family=Montserrat:wght@300;400;500;600&display=swap">
<style>{css}
.compare-note{{position:fixed;top:0;left:0;right:0;z-index:50;background:#1E3C57;color:#fff;font-family:Montserrat,sans-serif;font-size:13px;text-align:center;padding:8px;}}
body{{padding-top:36px;}}</style></head>
<body class="brand--cfbl">
<div class="compare-note">Marble comparison &middot; Gold (subtle/medium/bold), then Grey (subtle/medium/bold), then current Sand</div>
{sections}{sand_block}
</body></html>"""

open('preview/CFBL-marble-compare.html','w').write(html)
print("wrote", len(html), "bytes")
