/* ==========================================================================
   Center for Balanced Living - theme.js
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

  /* ----------------------------------------------------------------------
     Tabs (ARIA tab pattern with arrow-key navigation)
     ---------------------------------------------------------------------- */
  function initTabs() {
    document.querySelectorAll('[data-tabs]').forEach(function (group) {
      var tabs = Array.prototype.slice.call(group.querySelectorAll('[role="tab"]'));
      if (!tabs.length) return;

      function select(tab) {
        tabs.forEach(function (t) {
          var selected = t === tab;
          t.setAttribute('aria-selected', String(selected));
          t.setAttribute('tabindex', selected ? '0' : '-1');
          var panel = document.getElementById(t.getAttribute('aria-controls'));
          if (panel) panel.hidden = !selected;
        });
      }

      tabs.forEach(function (tab, i) {
        tab.addEventListener('click', function () { select(tab); });
        tab.addEventListener('keydown', function (e) {
          var idx = null;
          if (e.key === 'ArrowRight' || e.key === 'ArrowDown') idx = (i + 1) % tabs.length;
          else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') idx = (i - 1 + tabs.length) % tabs.length;
          else if (e.key === 'Home') idx = 0;
          else if (e.key === 'End') idx = tabs.length - 1;
          if (idx !== null) { e.preventDefault(); select(tabs[idx]); tabs[idx].focus(); }
        });
      });
    });
  }

  /* ----------------------------------------------------------------------
     Scrolling images + text - sticky media swaps to the item in view
     ---------------------------------------------------------------------- */
  function initScroller() {
    var scrollers = document.querySelectorAll('[data-scroller]');
    if (!scrollers.length || !('IntersectionObserver' in window)) return;

    scrollers.forEach(function (scroller) {
      var items = scroller.querySelectorAll('[data-scroller-item]');
      var media = scroller.querySelectorAll('.scroller__media-item');
      if (!items.length || !media.length) return;

      function setActive(index) {
        media.forEach(function (m) {
          m.classList.toggle('is-active', m.getAttribute('data-media-index') === String(index));
        });
      }

      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) setActive(entry.target.getAttribute('data-index'));
        });
      }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });

      items.forEach(function (item) { io.observe(item); });
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
    initTabs();
    initScroller();
  });
})();
