/* ============================================================
   REENE MEDICAL DIAGNOSTICS — interaction layer
   Smooth scroll · magnetic buttons · scroll-linked motion
   ============================================================ */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var lerp = function (a, b, t) { return a + (b - a) * t; };
  var clamp = function (v, a, b) { return Math.min(b, Math.max(a, v)); };

  var scrollY = window.scrollY || 0;
  var raf = [];               // per-frame subscribers
  function onFrame(fn) { raf.push(fn); }

  /* ---------- smooth scroll (Lenis, progressive enhancement) ---------- */
  var lenis = null;
  function initScroll() {
    if (reduce || typeof window.Lenis !== 'function') return;
    lenis = new window.Lenis({
      duration: 1.15,
      easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      smoothWheel: true,
      touchMultiplier: 1.6
    });
    lenis.on('scroll', function (e) { scrollY = e.scroll; });
  }

  function tick(time) {
    if (lenis) lenis.raf(time);
    else scrollY = window.scrollY;
    for (var i = 0; i < raf.length; i++) raf[i](scrollY);
    requestAnimationFrame(tick);
  }

  /* ---------- reveal on enter ---------- */
  function initReveal() {
    var els = $$('.rv, .rv-clip, .rv-img, .line-mask, [data-reveal]');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        var delay = parseFloat(el.getAttribute('data-delay') || 0);
        if (delay) setTimeout(function () { el.classList.add('in'); }, delay);
        else el.classList.add('in');
        io.unobserve(el);
      });
    }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ---------- navbar state ---------- */
  function initNav() {
    var nav = $('.nav');
    if (!nav) return;

    var trigger = window.innerHeight * 0.72;
    var hero = $('.hero, .phero');
    if (hero) trigger = Math.max(120, hero.offsetHeight - 120);
    window.addEventListener('resize', function () {
      var h = $('.hero, .phero');
      trigger = h ? Math.max(120, h.offsetHeight - 120) : window.innerHeight * 0.72;
    });

    // hysteresis: separate on/off thresholds so the state can never flicker
    // while the scroll position sits right on the boundary.
    var GAP = 90;
    var solid = false;

    onFrame(function (y) {
      if (!solid && y > trigger) { solid = true; nav.classList.add('solid'); }
      else if (solid && y < trigger - GAP) { solid = false; nav.classList.remove('solid'); }
    });
  }

  /* ---------- full-screen menu ---------- */
  function initMenu() {
    var burger = $('#burger'), menu = $('#menu');
    if (!burger || !menu) return;
    function set(open) {
      burger.classList.toggle('x', open);
      menu.classList.toggle('open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
      if (lenis) open ? lenis.stop() : lenis.start();
    }
    burger.addEventListener('click', function () { set(!menu.classList.contains('open')); });
    $$('a', menu).forEach(function (a) { a.addEventListener('click', function () { set(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  }

  /* ---------- magnetic buttons + cursor-origin fill ---------- */
  function initMagnetic() {
    if (reduce) return;
    $$('.btn').forEach(function (btn) {
      var label = $('.btn__label', btn);
      var fill  = $('.btn__fill', btn);
      var box   = null;

      function origin(e) {
        if (!fill) return;
        var r = btn.getBoundingClientRect();
        fill.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        fill.style.setProperty('--my', (e.clientY - r.top) + 'px');
      }
      btn.addEventListener('mouseenter', function (e) { box = btn.getBoundingClientRect(); origin(e); });
      btn.addEventListener('mouseleave', function (e) {
        origin(e);
        btn.style.transform = '';
        if (label) label.style.transform = '';
      });
      btn.addEventListener('mousemove', function (e) {
        if (!box) box = btn.getBoundingClientRect();
        var x = e.clientX - box.left - box.width / 2;
        var y = e.clientY - box.top - box.height / 2;
        btn.style.transform = 'translate(' + (x * 0.22).toFixed(2) + 'px,' + (y * 0.32).toFixed(2) + 'px)';
        if (label) label.style.transform = 'translate(' + (x * 0.10).toFixed(2) + 'px,' + (y * 0.16).toFixed(2) + 'px)';
      });
    });
  }

  /* ---------- hero backdrop cycler (ken burns + crossfade) ---------- */
  function initHeroBg() {
    var wrap = $('.hero-bg');
    if (!wrap) return;
    var slides = $$('figure', wrap);
    var dots = $$('.hero-dots button');
    if (slides.length < 2) return;
    var i = 0, timer = null;
    var HOLD = 9000;

    function go(n) {
      slides[i].classList.remove('on');
      if (dots[i]) dots[i].classList.remove('on');
      i = (n + slides.length) % slides.length;
      // restart the ken-burns animation cleanly
      var img = $('img', slides[i]);
      if (img) { img.style.animation = 'none'; void img.offsetWidth; img.style.animation = ''; }
      slides[i].classList.add('on');
      if (dots[i]) {
        var d = dots[i];
        d.classList.remove('on'); void d.offsetWidth; d.classList.add('on');
      }
    }
    function play() { clearInterval(timer); if (!reduce) timer = setInterval(function () { go(i + 1); }, HOLD); }

    slides[0].classList.add('on');
    if (dots[0]) dots[0].classList.add('on');
    dots.forEach(function (d, n) { d.addEventListener('click', function () { go(n); play(); }); });
    play();

    document.addEventListener('visibilitychange', function () {
      if (document.hidden) clearInterval(timer); else play();
    });
  }

  /* ---------- scroll-linked word highlight ---------- */
  function initHighlight() {
    var blocks = $$('.hl-words');
    if (!blocks.length) return;

    blocks.forEach(function (b) {
      if (b.dataset.split) return;
      var words = b.textContent.trim().split(/\s+/);
      b.textContent = '';
      words.forEach(function (w, n) {
        var s = document.createElement('span');
        s.textContent = w + (n < words.length - 1 ? ' ' : '');
        s.className = 'off';
        b.appendChild(s);
      });
      b.dataset.split = '1';
    });

    if (reduce) return;
    onFrame(function () {
      blocks.forEach(function (b) {
        var r = b.getBoundingClientRect();
        var vh = window.innerHeight;
        // progress across the middle band of the viewport
        var p = clamp((vh * 0.82 - r.top) / (r.height + vh * 0.30), 0, 1);
        var spans = b.children;
        var cut = Math.round(p * spans.length);
        for (var n = 0; n < spans.length; n++) {
          spans[n].classList.toggle('off', n >= cut);
        }
      });
    });
  }

  /* ---------- parallax ---------- */
  function initParallax() {
    var els = $$('[data-par]');
    if (!els.length || reduce) return;
    var state = els.map(function () { return 0; });

    onFrame(function () {
      var vh = window.innerHeight;
      els.forEach(function (el, n) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var speed = parseFloat(el.getAttribute('data-par')) || 0.12;
        var mid = r.top + r.height / 2 - vh / 2;
        var target = -mid * speed;
        state[n] = lerp(state[n], target, 0.12);
        el.style.transform = 'translate3d(0,' + state[n].toFixed(2) + 'px,0)';
      });
    });
  }

  /* ---------- counters ---------- */
  function initCounters() {
    var els = $$('[data-count]');
    if (!els.length || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        io.unobserve(el);
        var raw = el.getAttribute('data-count');
        var target = parseFloat(raw);
        var suffix = raw.replace(/[\d.]/g, '');
        if (reduce || isNaN(target)) { el.textContent = raw; return; }
        var t0 = performance.now(), dur = 1500;
        (function step(now) {
          var p = clamp((now - t0) / dur, 0, 1);
          var e = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * e) + suffix;
          if (p < 1) requestAnimationFrame(step);
        })(t0);
      });
    }, { threshold: 0.5 });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ---------- service rows: cursor-following peek image ---------- */
  function initPeek() {
    var peek = $('#peek');
    var rows = $$('.svc[data-peek]');
    if (!peek || !rows.length || reduce) return;
    var img = $('img', peek);
    var tx = 0, ty = 0, cx = 0, cy = 0, active = false;

    rows.forEach(function (row) {
      row.addEventListener('mouseenter', function () {
        var src = row.getAttribute('data-peek');
        if (src && img.getAttribute('src') !== src) img.setAttribute('src', src);
        active = true; peek.classList.add('on');
      });
      row.addEventListener('mouseleave', function () { active = false; peek.classList.remove('on'); });
    });
    window.addEventListener('mousemove', function (e) { tx = e.clientX; ty = e.clientY; });
    onFrame(function () {
      if (!active) return;
      cx = lerp(cx, tx, 0.14);
      cy = lerp(cy, ty, 0.14);
      peek.style.left = cx + 'px';
      peek.style.top  = cy + 'px';
    });
  }

  /* ---------- anchor links through Lenis ---------- */
  function initAnchors() {
    $$('a[href^="#"]').forEach(function (a) {
      var id = a.getAttribute('href');
      if (!id || id === '#') return;
      a.addEventListener('click', function (e) {
        var t = document.querySelector(id);
        if (!t) return;
        e.preventDefault();
        if (lenis) lenis.scrollTo(t, { offset: -80 });
        else t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
      });
    });
  }

  /* ---------- filters (services / gallery) ---------- */
  function initFilters() {
    $$('[data-filter-group]').forEach(function (group) {
      var name = group.getAttribute('data-filter-group');
      var targets = $$('[data-filter-target="' + name + '"]');
      $$('.f-btn', group).forEach(function (btn) {
        btn.addEventListener('click', function () {
          $$('.f-btn', group).forEach(function (b) { b.classList.remove('on'); });
          btn.classList.add('on');
          var cat = btn.getAttribute('data-filter');
          targets.forEach(function (t) {
            var show = cat === 'all' || t.getAttribute('data-cat') === cat;
            t.style.display = show ? '' : 'none';
          });
        });
      });
    });
  }

  /* ---------- gallery lightbox ---------- */
  function initLightbox() {
    var lb = $('#lightbox');
    if (!lb) return;
    var img = $('#lbImg'), cap = $('#lbCap');
    var items = $$('.gal-item');
    var cur = 0;

    function show(n) {
      cur = (n + items.length) % items.length;
      var it = items[cur];
      var src = $('img', it);
      img.setAttribute('src', src.getAttribute('src'));
      img.setAttribute('alt', src.getAttribute('alt') || '');
      if (cap) cap.textContent = it.getAttribute('data-cap') || '';
    }
    function open(n) {
      show(n); lb.classList.add('on');
      document.body.style.overflow = 'hidden';
      if (lenis) lenis.stop();
    }
    function close() {
      lb.classList.remove('on');
      document.body.style.overflow = '';
      if (lenis) lenis.start();
    }
    items.forEach(function (it, n) {
      it.setAttribute('tabindex', '0');
      it.setAttribute('role', 'button');
      it.addEventListener('click', function () { open(n); });
      it.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(n); }
      });
    });
    var c = $('#lbClose'), p = $('#lbPrev'), nx = $('#lbNext');
    if (c) c.addEventListener('click', close);
    if (p) p.addEventListener('click', function () { show(cur - 1); });
    if (nx) nx.addEventListener('click', function () { show(cur + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('on')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(cur - 1);
      if (e.key === 'ArrowRight') show(cur + 1);
    });
  }

  /* ---------- contact form (mailto bridge — no backend) ---------- */
  function initContactForm() {
    var form = $('#contactForm');
    if (!form) return;
    var note = $('#formNote');

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = function (n) { return form[n] ? form[n].value.trim() : ''; };
      var ok = true;
      [['fullName', 1], ['phoneNumber', 1], ['message', 1]].forEach(function (pair) {
        var el = form[pair[0]];
        if (!el) return;
        var field = el.closest('.field');
        var bad = !el.value.trim();
        if (field) field.classList.toggle('err', bad);
        if (bad) ok = false;
      });
      if (!ok) return;

      var body = 'Name: ' + v('fullName') +
                 '\nPhone: ' + v('phoneNumber') +
                 (v('emailAddress') ? '\nEmail: ' + v('emailAddress') : '') +
                 (v('subject') ? '\nSubject: ' + v('subject') : '') +
                 '\n\n' + v('message');

      window.location.href = 'mailto:info@reenemedicaldiagnostics.com?subject=' +
        encodeURIComponent(v('subject') || 'Website enquiry — Reene Medical Diagnostics') +
        '&body=' + encodeURIComponent(body);

      if (note) {
        note.textContent = 'Opening your email app — press send to complete the enquiry. For an immediate reply, call or message us on WhatsApp.';
        note.classList.add('show');
      }
      form.reset();
    });
  }

  /* ---------- booking stepper ---------- */
  function initBooking() {
    var panel = $('#bookingPanel');
    if (!panel) return;

    var st = { service: '', label: '', date: '', time: '', name: '', phone: '', email: '', notes: '' };
    var steps = $$('.step-dot');
    var panes = $$('.step-pane');
    var idx = 0;

    function render() {
      steps.forEach(function (s, n) {
        s.classList.toggle('on', n === idx);
        s.classList.toggle('done', n < idx);
      });
      panes.forEach(function (p, n) { p.classList.toggle('on', n === idx); });
      var top = panel.getBoundingClientRect().top + (lenis ? scrollY : window.scrollY) - 120;
      if (lenis) lenis.scrollTo(top); else window.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
    }
    function err(n, msg) { var e = $('.step-err', panes[n]); if (e) e.textContent = msg || ''; }
    function valid(n) {
      err(n, '');
      if (n === 0 && !st.service) { err(n, 'Select a service to continue.'); return false; }
      if (n === 1 && !st.date)    { err(n, 'Choose a preferred date.'); return false; }
      if (n === 2 && !st.time)    { err(n, 'Choose a preferred time.'); return false; }
      if (n === 3) {
        st.name  = ($('#pName')  || {}).value ? $('#pName').value.trim()  : '';
        st.phone = ($('#pPhone') || {}).value ? $('#pPhone').value.trim() : '';
        st.email = ($('#pEmail') || {}).value ? $('#pEmail').value.trim() : '';
        st.notes = ($('#pNotes') || {}).value ? $('#pNotes').value.trim() : '';
        if (!st.name || !st.phone) { err(n, 'Your name and phone number are required.'); return false; }
      }
      return true;
    }
    function fmt(d) {
      if (!d) return '—';
      var p = d.split('-');
      return new Date(+p[0], +p[1] - 1, +p[2])
        .toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
    }
    function summary() {
      var set = function (id, val) { var e = $(id); if (e) e.textContent = val || '—'; };
      set('#sService', st.label); set('#sDate', fmt(st.date)); set('#sTime', st.time);
      set('#sName', st.name); set('#sPhone', st.phone);

      var body = 'Appointment request\n\n' +
        'Service: ' + st.label + '\nDate: ' + fmt(st.date) + '\nTime: ' + st.time +
        '\nName: ' + st.name + '\nPhone: ' + st.phone +
        (st.email ? '\nEmail: ' + st.email : '') +
        (st.notes ? '\nNotes: ' + st.notes : '');

      var m = $('#sendEmail'), w = $('#sendWa');
      if (m) m.href = 'mailto:info@reenemedicaldiagnostics.com?subject=' +
        encodeURIComponent('Appointment request — ' + st.label) + '&body=' + encodeURIComponent(body);
      if (w) w.href = 'https://wa.me/2348122190051?text=' + encodeURIComponent(body);
    }
    function go(n) {
      if (n > idx && !valid(idx)) return;
      if (n === panes.length - 1) summary();
      idx = clamp(n, 0, panes.length - 1);
      render();
    }

    $$('.pick').forEach(function (card) {
      card.addEventListener('click', function () {
        $$('.pick').forEach(function (c) { c.classList.remove('on'); });
        card.classList.add('on');
        st.service = card.getAttribute('data-service');
        st.label = card.getAttribute('data-label');
      });
    });
    var date = $('#bDate');
    if (date) {
      date.setAttribute('min', new Date().toISOString().split('T')[0]);
      date.addEventListener('change', function () { st.date = date.value; });
    }
    $$('.slot').forEach(function (s) {
      s.addEventListener('click', function () {
        $$('.slot').forEach(function (x) { x.classList.remove('on'); });
        s.classList.add('on');
        st.time = s.textContent.trim();
      });
    });
    $$('[data-next]').forEach(function (b) { b.addEventListener('click', function () { go(idx + 1); }); });
    $$('[data-back]').forEach(function (b) { b.addEventListener('click', function () { go(idx - 1); }); });
    steps.forEach(function (s, n) { s.addEventListener('click', function () { if (n < idx) go(n); }); });

    render();
  }

  /* ---------- year ---------- */
  function initYear() {
    $$('.js-year').forEach(function (e) { e.textContent = new Date().getFullYear(); });
  }

  /* ---------- boot ---------- */
  function boot() {
    initScroll();
    initNav();
    initMenu();
    initReveal();
    initMagnetic();
    initHeroBg();
    initHighlight();
    initParallax();
    initCounters();
    initPeek();
    initAnchors();
    initFilters();
    initLightbox();
    initContactForm();
    initBooking();
    initYear();
    requestAnimationFrame(tick);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
