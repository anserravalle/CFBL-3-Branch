#!/usr/bin/env python3
"""Regenerate the static browser preview from the live base.css + theme.js.
Run from repo root: python3 scripts/build-preview.py"""
import os
css = open('assets/base.css').read()
js = open('assets/theme.js').read()

def btn(l, s='primary', e=''):
    return f'<a href="#" class="btn btn--{s} {e}">{l}</a>'

def overlay_card(eyebrow, title, body, cta, bg):
    return f'''<a href="#" class="card card--overlay is-linked">
      <div class="card__overlay-media"><div class="media media--4-3" style="width:100%;height:100%;background:{bg};"></div></div>
      <div class="card__overlay-content"><p class="eyebrow" style="color:var(--color-sand)">{eyebrow}</p>
      <h3 class="card__title">{title}</h3><div class="card__body rte"><p>{body}</p></div>
      <span class="card__overlay-cta">{cta} &rarr;</span></div></a>'''

def field(label, inp):
    return f'<div class="field"><label>{label}</label>{inp}</div>'

sig = '<span class="header__signature" style="font-family:Cormorant SC,serif;font-size:1.6rem;font-style:italic;color:var(--color-navy);">Niki Serravalle</span>'

body = f'''
<div class="announcement"><div class="page-width"><p class="announcement__inner"><span>Now accepting new clients across the MOT area and throughout Delaware.</span><a href="#">Start the conversation</a></p></div></div>
<header class="site-header"><div class="page-width"><div class="site-header__inner">
  <div class="site-header__brand"><a href="#" class="site-header__logo"><span class="site-header__logo-text">Center for Balanced Living</span></a>{sig}</div>
  <nav class="nav"><ul class="nav__list">
    <li><a class="nav__link" href="#">For Clients</a></li><li><a class="nav__link" href="#">For Professionals</a></li>
    <li><a class="nav__link" href="#">Career Development</a></li><li><a class="nav__link" href="#">About Us</a></li>
    <li><a class="nav__link" href="#">MUSA</a></li><li><a class="nav__link" href="#">Contact</a></li>
  </ul></nav>
  <div class="header__actions">{btn('Start the Conversation','primary','btn--sm')}</div>
</div></div></header>
<main>
<section class="section hero bg--default hero--split" style="--section-pt:96px;--section-pb:96px;">
  <span class="brand-shape brand-shape--1"></span>
  <div class="page-width"><div class="hero__grid has-media">
    <div class="hero__content"><p class="eyebrow hero__eyebrow">Trauma-Informed Psychological Care</p>
      <h1 class="hero__title">Your Path To Healing Begins Here</h1>
      <div class="hero__lead"><p>Center for Balanced Living offers therapy, psychological evaluations, consultation, supervision, and educational services grounded in trauma-informed, research-based care.</p></div>
      <div class="btn-row">{btn('Start the Conversation','primary','btn--lg')}{btn('Explore Services','secondary')}</div></div>
    <div class="hero__media hero__media--framed" style="--frame-color:#9D654E;"><div class="media media--4-3" style="display:grid;place-items:center;background:#e7d4c0;color:#2b5275;font-family:var(--font-heading);font-size:1.4rem;">Image placeholder</div></div>
  </div></div>
</section>

<section class="section bg--default" style="--section-pt:80px;--section-pb:80px;"><div class="page-width"><div class="section__inner">
  <div class="section__header is-center"><p class="eyebrow">One Practice, Three Paths</p><h2>Choose Your Path</h2><p class="section__subheading">Clinical care, professional education, and writing, each with its own focus.</p></div>
  <div class="grid grid--3 cards--overlay">
    {overlay_card('For Clients','CFBL Clinical Services','Therapy, evaluation, groups, and workshops.','Explore Clinical Services','#2b5275')}
    {overlay_card('For Professionals','CFBL Institute','Continuing education, supervision, and consultation.','Visit the Institute','#3D5A52')}
    {overlay_card('Reading &amp; Essays','CFBL Writing (MUSA)','Books and essays on psychology and being human.','Read MUSA','#6E1F23')}
  </div>
</div></div></section>

<section class="section bg--sand" style="--section-pt:80px;--section-pb:80px;"><div class="page-width"><div class="section__inner">
  <div class="section__header"><p class="eyebrow">Our Models &amp; Approach</p><h2>Tabs With Media</h2><p class="section__subheading">Tabs can hold text, an image or video, and link to a full page.</p></div>
  <div class="tabs" data-tabs><div class="tabs__list" role="tablist" aria-label="Models">
    {''.join(f'<button type="button" role="tab" class="tabs__tab" id="t{i}" aria-controls="p{i}" aria-selected="{"true" if i==0 else "false"}" tabindex="{"0" if i==0 else "-1"}">{t}</button>' for i,t in enumerate(["ACT","CBT","DBT","EMDR","Trainings"]))}
  </div><div class="tabs__panels">
    {''.join(f"""<div role="tabpanel" class="tabs__panel tabs__panel--media" id="p{i}" aria-labelledby="t{i}" tabindex="0" {"" if i==0 else "hidden"}>
      <div class="tabs__panel-media"><div class="media media--4-3" style="background:#cdd9d2"></div></div>
      <div class="tabs__panel-body"><h3>{t}</h3><div class="rte"><p>{d}</p></div><p style="margin-top:20px"><a class="btn btn--secondary" href="#">Learn more</a></p></div></div>""" for i,(t,d) in enumerate([("Acceptance & Commitment Therapy","Make room for values-based action; change your relationship with difficult thoughts and feelings."),("Cognitive Behavioral Therapy","A structured, problem-focused approach linking thoughts, feelings, and behavior."),("Dialectical Behavior Therapy","Skills for emotion regulation, distress tolerance, and mindful awareness."),("EMDR","Reprocessing distressing memories to support trauma recovery."),("Trainings & Certifications","The advanced training behind our care, EMDR, IFS, somatic, DBT, ACT, and more.")]))}
  </div></div>
</div></div></section>

<section class="section bg--default" style="--section-pt:80px;--section-pb:80px;"><div class="page-width"><div class="section__inner">
  <div class="section__header is-center"><p class="eyebrow">Our Team</p><h2>Meet Our Team</h2></div>
  <div class="scroller scroller--media-start" data-scroller>
    <div class="scroller__media" aria-hidden="true">
      {''.join(f'<div class="scroller__media-item {"is-active" if i==0 else ""}" data-media-index="{i}"><div class="media media--4-3" style="display:grid;place-items:center;background:{bg};color:#fff;font-family:var(--font-heading);font-size:2rem;">{n.split()[0]}</div></div>' for i,(n,bg) in enumerate([('Dr. Niki Serravalle','#2b5275'),('Amanda Foxwell','#9D654E')]))}
    </div>
    <div class="scroller__text">
      <article class="scroller__item" data-scroller-item data-index="0"><h3 class="scroller__title">Dr. Niki Serravalle</h3><p class="scroller__role">Founder &middot; Licensed Psychologist</p><div class="rte scroller__content"><p>Founder of Center for Balanced Living with more than two decades of clinical experience.</p></div><ul class="person-contact"><li><a href="#">&#9993; drserravalle@gmail.com</a></li></ul></article>
      <article class="scroller__item" data-scroller-item data-index="1"><h3 class="scroller__title">Amanda Foxwell</h3><p class="scroller__role">Mental Health Counselor</p><div class="rte scroller__content"><p>Works with teens and adults navigating trauma and anxiety; EMDR-trained.</p></div><ul class="person-contact"><li><a href="#">&#9742; (302) 365-0610</a></li><li><a href="#">&#9993; amandaf@balancedlivingde.com</a></li></ul></article>
    </div>
  </div>
</div></div></section>

<section class="section bg--sand" style="--section-pt:80px;--section-pb:80px;"><div class="page-width"><div class="section__inner">
  <div class="section__header"><p class="eyebrow">Get in Touch</p><h2>Start the Conversation</h2></div>
  <div class="contact__grid">
    <div class="contact__info">
      <div class="rte"><p>Tell us a little about what you are looking for, and we will help you find the service, or the referral, that fits.</p></div>
      <div class="contact__details" style="margin-top:var(--space-24)"><p class="contact__detail">&#9742; (302) 608-3780</p><p class="contact__detail">&#9201; By appointment</p></div>
      <p class="contact__detail" style="margin-top:var(--space-24);font-weight:600;color:var(--color-heading)">We usually reach out within 24-48 hours.</p>
      <div class="form-note form-note--error" style="margin-top:var(--space-16);font-weight:500"><p>This form is not intended for emergencies or urgent mental health concerns. If you are experiencing an emergency, call 911 or go to your nearest emergency room.</p></div>
    </div>
    <div class="contact__form-wrap"><div class="form-grid">
      <div class="form-grid--2">{field('First name','<input type="text">')}{field('Last name','<input type="text">')}</div>
      <div class="form-grid--2">{field('Email','<input type="email">')}{field('Phone (optional)','<input type="tel">')}</div>
      {field('What are you reaching out about?','<select><option>Please select...</option><option>Therapy</option><option>Psychological Evaluation</option><option>Group or Workshop</option></select>')}
      {field('Preferred method of contact','<select><option>Email</option><option>Phone</option><option>Either</option></select>')}
      {field('How can we help?','<textarea></textarea>')}
      <button class="btn btn--primary btn--lg">Send Message</button>
    </div></div>
  </div>
</div></div></section>

<section class="section bg--navy" style="--section-pt:96px;--section-pb:96px;"><div class="page-width"><div class="section__inner section__header is-center" style="margin-bottom:0">
  <p class="eyebrow">Take the Next Step</p><h2>Healing happens in relationship</h2>
  <div class="rte section__subheading"><p>Whether you are seeking therapy, an evaluation, consultation, or training, we are here to help you take a clear next step.</p></div>
  <div class="btn-row is-center">{btn('Start the Conversation','primary','btn--lg')}{btn('Call (302) 608-3780','secondary')}</div>
</div></div></section>
</main>
<footer class="site-footer"><div class="page-width"><div class="footer__grid">
  <div class="footer__about"><span class="footer__logo">Center for Balanced Living</span><p>Trauma-informed therapy, psychological evaluation, groups, workshops, and consultation for the MOT area and throughout Delaware.</p></div>
  <nav class="footer__col"><h2 class="footer__heading">Explore</h2><ul class="footer__list"><li><a href="#">Contact Us</a></li><li><a href="#">Privacy Practices</a></li><li><a href="#">Newsletter</a></li><li><a href="#">CFBL Institute</a></li></ul></nav>
  <nav class="footer__col"><h2 class="footer__heading">For Clients</h2><ul class="footer__list"><li><a href="#">Therapy</a></li><li><a href="#">Evaluations</a></li><li><a href="#">Wellness Groups</a></li><li><a href="#">Client Portal</a></li><li><a href="#">FAQ</a></li></ul></nav>
  <nav class="footer__col"><h2 class="footer__heading">For Professionals</h2><ul class="footer__list"><li><a href="#">Join Our Team</a></li><li><a href="#">Workshops</a></li><li><a href="#">Courses &amp; Certification</a></li><li><a href="#">Professional Trainings</a></li><li><a href="#">EMDR Consultation</a></li><li><a href="#">Supervision</a></li></ul></nav>
  <div class="footer__col"><h2 class="footer__heading">Office Hours</h2><div class="rte footer__about"><p>Monday: 10 am-6 pm<br>Tuesday: 10 am-6 pm<br>Wednesday: 10 am-6 pm<br>Thursday: 10 am-6 pm<br>Friday: 10 am-4 pm<br>Saturday / Sunday: Closed</p></div></div>
</div><div class="footer__bottom"><p>&copy; 2026 Center for Balanced Living. All rights reserved.</p></div></div></footer>
'''

switcher = '''<div style="position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;gap:8px;justify-content:center;align-items:center;background:#1E3C57;color:#fff;font-family:Montserrat,sans-serif;font-size:13px;padding:6px">
<span style="opacity:.8">Brand preview:</span>
<button onclick="setBrand('cfbl',this)" style="cursor:pointer;border:0;border-radius:999px;padding:5px 14px;font-weight:600;background:#fff;color:#2b5275">CFBL</button>
<button onclick="setBrand('institute',this)" style="cursor:pointer;border:0;border-radius:999px;padding:5px 14px;font-weight:600;background:transparent;color:#fff">Institute</button>
<button onclick="setBrand('musa',this)" style="cursor:pointer;border:0;border-radius:999px;padding:5px 14px;font-weight:600;background:transparent;color:#fff">MUSA</button></div>
<script>function setBrand(b,btn){document.body.className='brand--'+b+' animations-on';[].forEach.call(btn.parentNode.querySelectorAll('button'),function(x){x.style.background='transparent';x.style.color='#fff'});btn.style.background='#fff';btn.style.color='#2b5275'}</script>'''

html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>CFBL Theme Preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@500;600;700&family=Montserrat:wght@300;400;500;600&family=Lora:wght@400;500;600&family=DM+Serif+Display&family=EB+Garamond:wght@400;500&display=swap">
<style>{css}
.preview-flag{{position:fixed;bottom:12px;right:12px;z-index:999;background:#2b5275;color:#fff;font-family:var(--font-body);font-size:12px;padding:8px 14px;border-radius:999px;box-shadow:var(--shadow-md);opacity:.92}}</style>
</head><body class="brand--cfbl animations-on" style="padding-top:34px">{switcher}{body}<div class="preview-flag">CFBL theme preview &middot; static</div><script>{js}</script></body></html>'''

os.makedirs('preview', exist_ok=True)
open('preview/CFBL-theme-preview.html', 'w').write(html)
print("wrote preview/CFBL-theme-preview.html", len(html), "bytes")
