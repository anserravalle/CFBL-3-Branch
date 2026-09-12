#!/usr/bin/env python3
"""Gold-subtle marble preview using SVG fractal-noise turbulence for organic,
wavy veining (real marble look, not lines). CSS-only data-URI, lightweight.
Shows 3 organic variations + current Sand. Output: preview/CFBL-marble-gold.html
"""
import base64
css = open('assets/base.css').read()

def svg_marble(base_freq, octaves, scale, vein_rgb, vein_alpha, tint):
    """Generate an SVG noise tile -> data URI. Wavy turbulence displaced + tinted."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
    <filter id="m" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="{base_freq}" numOctaves="{octaves}" seed="7" result="noise"/>
      <feColorMatrix in="noise" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 {vein_alpha} 0" result="veins"/>
      <feComponentTransfer in="veins" result="veins2">
        <feFuncA type="gamma" amplitude="1" exponent="{scale}" offset="0"/>
      </feComponentTransfer>
      <feFlood flood-color="rgb({vein_rgb})" result="vc"/>
      <feComposite in="vc" in2="veins2" operator="in" result="vlines"/>
      <feMerge>
        <feMergeNode in="vlines"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="600" height="600" fill="{tint}"/>
  <rect width="600" height="600" filter="url(#m)"/>
</svg>'''
    b64 = base64.b64encode(svg.encode()).decode()
    return f'url("data:image/svg+xml;base64,{b64}")'

# Three organic gold-marble variations (all subtle), differing in vein character.
variations = [
    ("Soft cloudy (fine veins)",  svg_marble("0.012 0.03", 4, 4.0, "176,141,87", 0.9, "#FBF7F1")),
    ("Wispy veins (medium)",      svg_marble("0.008 0.02", 5, 3.2, "168,133,80", 1.0, "#FBF6EF")),
    ("Open marble (few bold veins)", svg_marble("0.006 0.014", 5, 2.4, "160,126,74", 1.0, "#FAF5ED")),
]

def block(label, bg):
    return f"""
<section style="background-color:#FBF7F1;background-image:{bg};background-size:cover;">
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
      <p style="color:var(--color-text);">Body copy sitting straight on the marble. Check readability.</p>
    </div>
    <div class="grid grid--3">
      <article class="card card--elevated"><h3 class="card__title">Begin Therapy</h3><div class="card__body"><p>Support for healing and change.</p></div></article>
      <article class="card card--elevated"><h3 class="card__title">Get an Evaluation</h3><div class="card__body"><p>Clarity for diagnosis and next steps.</p></div></article>
      <article class="card card--elevated"><h3 class="card__title">Learn With Us</h3><div class="card__body"><p>Training, supervision, consultation.</p></div></article>
    </div>
  </div>
</section>
"""

sections = "".join(block(l, bg) for l, bg in variations)
sand = """<section class="bg--sand"><div class="page-width" style="padding-block:48px;text-align:center;">
<p style="font-family:var(--font-body);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#9D654E;font-weight:600;margin-bottom:16px;">For comparison: current Sand (no texture)</p>
<h2>Your Path To Healing Begins Here</h2><p style="max-width:620px;margin:0 auto;color:var(--color-text);">The warm, untextured background used today.</p></div></section>"""

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CFBL Gold Marble (organic)</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500;600;700&family=Cormorant:ital,wght@0,500;1,400;1,500&family=Montserrat:wght@300;400;500;600&display=swap">
<style>{css}
.note{{position:fixed;top:0;left:0;right:0;z-index:50;background:#1E3C57;color:#fff;font-family:Montserrat,sans-serif;font-size:13px;text-align:center;padding:8px;}}
body{{padding-top:36px;}}</style></head>
<body class="brand--cfbl">
<div class="note">Organic gold marble (SVG noise) &middot; three vein styles, then current Sand</div>
{sections}{sand}
</body></html>"""

open('preview/CFBL-marble-gold.html','w').write(html)
print("wrote preview/CFBL-marble-gold.html", len(html), "bytes")
