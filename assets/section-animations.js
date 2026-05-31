/* ==========================================================================
   section-animations.js - subtle scroll-reveal via IntersectionObserver.
   Only loaded when "Enable animations" is on. Respects reduced-motion: if the
   user prefers reduced motion, elements are shown immediately with no movement.

   Editor-safe: in the Shopify theme editor (Shopify.designMode), and whenever a
   section is re-rendered/added (shopify:section:load), elements are revealed
   immediately so a section never appears blank while editing. ~1KB.
   ========================================================================== */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var inEditor = window.Shopify && window.Shopify.designMode;
  var supported = 'IntersectionObserver' in window;

  function showAll(root) {
    (root || document).querySelectorAll('.reveal').forEach(function (el) {
      el.classList.add('is-visible');
    });
  }

  // In the editor, with reduced motion, or without IO support: just show
  // everything. This guarantees sections are never left invisible.
  if (inEditor || reduce || !supported) {
    showAll();
    // In the editor, also reveal any section that gets re-rendered on edit.
    if (inEditor) {
      document.addEventListener('shopify:section:load', function (e) { showAll(e.target); });
    }
    return;
  }

  var io = new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  function observe(root) {
    (root || document).querySelectorAll('.reveal:not(.is-visible)').forEach(function (el) {
      io.observe(el);
    });
  }

  observe();

  // Re-scan when sections are dynamically added/reordered (storefront + editor).
  document.addEventListener('shopify:section:load', function (e) { observe(e.target); });
})();
