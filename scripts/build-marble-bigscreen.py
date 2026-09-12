#!/usr/bin/env python3
"""Big-screen marble preview. Renders the gold-flecked marble as a FULL PAGE
background with real CFBL hero + cards on top, at three subtlety levels, so it
can be judged at true scale (not as a swatch). Output: preview/CFBL-marble-bigscreen.html
"""
import base64, os

def svg_marble(base_freq, octaves, gamma, vein_rgb, vein_alpha, tint):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="900" viewBox="0 0 900 900">
  <defs>
    <filter id="m" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="{base_freq}" numOctaves="{octaves}" seed="11" result="noise"/>
      <feColorMatrix in="noise" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 {vein_alpha} 0" result="veins"/>
      <feComponentTransfer in="veins" result="veins2">
        <feFuncA type="gamma" amplitude="1" exponent="{gamma}" offset="0"/>
      </feComponentTransfer>
      <feFlood flood-color="rgb({vein_rgb})" result="vc"/>
      <feComposite in="vc" in2="veins2" operator="in" result="vlines"/>
      <feMerge><feMergeNode in="vlines"/></feMerge>
    </filter>
  </defs>
  <rect width="900" height="900" fill="{tint}"/>
  <rect width="900" height="900" filter="url(#m)"/>
</svg>'''
    b64 = base64.b64encode(svg.encode()).decode()
    return f'url("data:image/svg+xml;base64,{b64}")'

levels = [
    ("Subtle", svg_marble("0.010 0.024", 5, 4.4, "180,146,92", 0.85, "#FBF7F1")),
    ("Medium", svg_marble("0.008 0.018", 5, 3.4, "170,135,82", 1.0, "#FAF6EE")),
    ("Bold",   svg_marble("0.006 0.013", 5, 2.6, "158,124,72", 1.0, "#F9F4EA")),
]

NAVY = "#2B5275"; TERRA = "#9D654E"; SAND = "#EED9C5"; TEXT = "#2A2724"

def page(label, bg):
    return f'''
<section style="background-image:{bg};background-size:680px 680px;padding:64px 48px;border-bottom:6px solid {NAVY};">
  <div style="max-width:1100px;margin:0 auto;">
    <p style="font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{TERRA};margin:0 0 28px;">{label} marble &mdash; full page</p>
    <p style="font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:{TERRA};font-weight:700;margin:0 0 8px;">Center for Balanced Living</p>
    <h1 style="font-family:Georgia,serif;font-size:46px;line-height:1.1;color:{NAVY};margin:0 0 16px;max-width:18ch;">Trauma-informed care for the whole person</h1>
    <p style="font-size:18px;line-height:1.6;color:{TEXT};max-width:60ch;margin:0 0 28px;">Psychological evaluation, individual therapy, and nature-based approaches in Townsend, Delaware.</p>
    <a href="#" style="display:inline-block;background:{NAVY};color:#fff;padding:14px 32px;border-radius:999px;text-decoration:none;font-weight:600;">Start the Conversation</a>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px;">
      {''.join(f'<div style="background:#fff;border:1px solid #E2D3C2;border-radius:16px;padding:28px;box-shadow:0 6px 24px rgba(43,82,117,.08);"><h3 style="font-family:Georgia,serif;color:{NAVY};margin:0 0 10px;font-size:22px;">{t}</h3><p style="margin:0;color:{TEXT};font-size:15px;line-height:1.6;">{d}</p></div>' for t,d in [("Clinical Care","Therapy and evaluation grounded in safety and trust."),("CFBL Institute","Training and consultation for clinicians."),("MUSA","Writing on psychology, relationships, and being human.")])}
    </div>
  </div>
</section>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CFBL Marble - big screen</title>
<style>body{{margin:0;font-family:-apple-system,Segoe UI,Roboto,sans-serif;}}</style></head>
<body>
<div style="background:{NAVY};color:#fff;padding:14px 48px;font-size:14px;">CFBL marble preview &mdash; three subtlety levels, full-page scale. Scroll to compare. Sand (no marble) is at the bottom for reference.</div>
{''.join(page(l,bg) for l,bg in levels)}
{page("None (current Sand)", f'linear-gradient(#FBF6F0,#FBF6F0)')}
</body></html>'''

os.makedirs('preview', exist_ok=True)
out = 'preview/CFBL-marble-bigscreen.html'
open(out,'w').write(html)
print("wrote", out, os.path.getsize(out), "bytes")
