/* ==========================================================================
   Center for Balanced Living — theme.js
   Lean, dependency-free interactivity: mobile drawer (with focus trap),
   accessible FAQ accordion, and click-to-load video. ~3KB.
   ========================================================================== */
(function () {
  'use strict';

  /* ----------------------------------------------------------------------
     Mobile navigation drawer
     ---------------------------------------------------------------------- */
  function initDrawer() {
    var drawer = document.getElementById('MobileDrawer');
    var overlay = document.querySelector('[data-drawer-overlay]');
    var openBtn = document.querySelector('[data-drawer-open]');
    var closeBtn = document.querySelector('[data-drawer-close]');
    if (!drawer || !openBtn) return;

    var lastFocused = null;

    function focusable() {
      return drawer.querySelectorAll('a[href], button:not([disabled]), input, select, [tabindex]:not([tabindex="-1"])');
    }

    function open() {
      lastFocused = document.activeElement;
      drawer.classList.add('is-open');
      drawer.setAttribute('aria-hidden', 'false');
      if (overlay) { overlay.hidden = false; requestAnimationFrame(function () { overlay.classList.add('is-open'); }); }
      openBtn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      var items = focusable();
      if (items.length) items[0].focus();
      document.addEventListener('keydown', onKeydown);
    }

    function close() {
      drawer.classList.remove('is-open');
      drawer.setAttribute('aria-hidden', 'true');
      if (overlay) { overlay.classList.remove('is-open'); setTimeout(function () { overlay.hidden = true; }, 300); }
      openBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      document.removeEventListener('keydown', onKeydown);
      if (lastFocused) lastFocused.focus();
    }

    function onKeydown(e) {
      if (e.key === 'Escape') { close(); return; }
      if (e.key !== 'Tab') return;
      var items = focusable();
      if (!items.length) return;
      var first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }

    openBtn.addEventListener('click', open);
    if (closeBtn) closeBtn.addEventListener('click', close);
    if (overlay) overlay.addEventListener('click', close);
  }

  /* ----------------------------------------------------------------------
     FAQ accordion (accessible, animates max-height)
     ---------------------------------------------------------------------- */
  function initFaq() {
    var groups = document.querySelectorAll('[data-faq]');
    groups.forEach(function (group) {
      var buttons = group.querySelectorAll('.faq__question');
      buttons.forEach(function (btn) {
        var panel = document.getElementById(btn.getAttribute('aria-controls'));
        if (!panel) return;
        btn.addEventListener('click', function () {
          var expanded = btn.getAttribute('aria-expanded') === 'true';
          btn.setAttribute('aria-expanded', String(!expanded));
          if (expanded) {
            panel.style.maxHeight = null;
          } else {
            panel.style.maxHeight = panel.scrollHeight + 'px';
          }
        });
      });
    });
    // Recalculate open panels on resize
    window.addEventListener('resize', function () {
      document.querySelectorAll('.faq__question[aria-expanded="true"]').forEach(function (btn) {
        var panel = document.getElementById(btn.getAttribute('aria-controls'));
        if (panel) panel.style.maxHeight = panel.scrollHeight + 'px';
      });
    });
  }

  /* ----------------------------------------------------------------------
     Click-to-load external video (keeps initial load light)
     ---------------------------------------------------------------------- */
  function initVideo() {
    document.querySelectorAll('[data-video-trigger]').forEach(function (trigger) {
      trigger.addEventListener('click', function () {
        var wrap = trigger.closest('[data-video-wrap]');
        var tpl = wrap && wrap.querySelector('[data-video-embed]');
        if (!tpl) return;
        var frame = tpl.content.cloneNode(true);
        trigger.replaceWith(frame);
      });
    });
  }

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    initDrawer();
    initFaq();
    initVideo();
  });
})();
