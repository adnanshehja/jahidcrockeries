/* =========================================================
   JAHID CROCKERIES — interactions
   One script for both pages: tableware (index.html) and
   kitchen appliances (appliances.html).
   ========================================================= */

(function () {
  'use strict';

  const doc = document;
  const body = doc.body;

  /* -------------------------------------------------------
     Header state
     ------------------------------------------------------- */
  const header = doc.getElementById('siteHead');
  const setHeader = () => {
    if (!header) return;
    header.classList.toggle('is-scrolled', window.scrollY > 12);
  };
  setHeader();
  window.addEventListener('scroll', setHeader, { passive: true });

  /* -------------------------------------------------------
     Mobile navigation
     ------------------------------------------------------- */
  const nav = doc.getElementById('primaryNav');
  const toggle = doc.getElementById('menuToggle');
  const navClose = doc.getElementById('navClose');
  const mobileMQ = window.matchMedia('(max-width: 1000px)');
  let menuOpen = false;

  const setInert = (el, value) => {
    if (!el) return;
    if ('inert' in el) el.inert = value;
  };

  function syncNavState() {
    if (!nav) return;
    if (mobileMQ.matches) {
      setInert(nav, !menuOpen);
      nav.setAttribute('aria-hidden', String(!menuOpen));
    } else {
      menuOpen = false;
      setInert(nav, false);
      nav.removeAttribute('aria-hidden');
      nav.classList.remove('is-open');
      body.classList.remove('menu-open');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    }
  }

  function openMenu() {
    if (!nav) return;
    menuOpen = true;
    nav.classList.add('is-open');
    body.classList.add('menu-open');
    setInert(nav, false);
    nav.setAttribute('aria-hidden', 'false');
    if (toggle) toggle.setAttribute('aria-expanded', 'true');
    window.setTimeout(() => {
      if (navClose) navClose.focus();
    }, 120);
  }

  function closeMenu(returnFocus) {
    if (!nav) return;
    menuOpen = false;
    nav.classList.remove('is-open');
    body.classList.remove('menu-open');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
    if (mobileMQ.matches) {
      setInert(nav, true);
      nav.setAttribute('aria-hidden', 'true');
    }
    if (returnFocus && toggle) toggle.focus();
  }

  if (toggle) {
    toggle.addEventListener('click', () => {
      if (menuOpen) closeMenu(true);
      else openMenu();
    });
  }
  if (navClose) navClose.addEventListener('click', () => closeMenu(true));

  if (nav) {
    nav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        if (mobileMQ.matches) closeMenu(false);
      });
    });
  }

  doc.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menuOpen) closeMenu(true);
  });

  if (mobileMQ.addEventListener) {
    mobileMQ.addEventListener('change', syncNavState);
  } else if (mobileMQ.addListener) {
    mobileMQ.addListener(syncNavState);
  }
  syncNavState();

  /* -------------------------------------------------------
     Reveal on scroll
     ------------------------------------------------------- */
  const revealItems = Array.from(doc.querySelectorAll('[data-reveal]'));
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function revealInView() {
    const viewport = window.innerHeight || doc.documentElement.clientHeight;
    revealItems.forEach((el) => {
      if (el.classList.contains('is-visible')) return;
      const rect = el.getBoundingClientRect();
      if (rect.top < viewport * 0.97 && rect.bottom > 0) {
        el.classList.add('is-visible');
      }
    });
  }

  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealItems.forEach((el) => el.classList.add('is-visible'));
  } else {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });

    revealItems.forEach((el) => revealObserver.observe(el));

    /* Fonts and images can shift the layout after first paint, moving
       elements into the viewport without a scroll event. Re-check. */
    revealInView();
    window.addEventListener('load', revealInView);
    window.addEventListener('resize', revealInView, { passive: true });
    if (doc.fonts && doc.fonts.ready) {
      doc.fonts.ready.then(revealInView).catch(() => {});
    }
    window.setTimeout(revealInView, 1400);
  }

  /* -------------------------------------------------------
     Active section in navigation
     ------------------------------------------------------- */
  const navLinks = nav ? Array.from(nav.querySelectorAll('a[href^="#"]')) : [];
  const sectionMap = new Map();

  navLinks.forEach((link) => {
    const id = link.getAttribute('href').slice(1);
    if (id) sectionMap.set(id, link);
  });

  if ('IntersectionObserver' in window && sectionMap.size) {
    const sectionObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const link = sectionMap.get(entry.target.id);
        if (!link) return;
        if (entry.isIntersecting) {
          sectionMap.forEach((l) => l.removeAttribute('aria-current'));
          link.setAttribute('aria-current', 'true');
        }
      });
    }, { rootMargin: '-42% 0px -52% 0px', threshold: 0 });

    sectionMap.forEach((_, id) => {
      const section = doc.getElementById(id);
      if (section) sectionObserver.observe(section);
    });
  }

  /* -------------------------------------------------------
     Catalogue — filters
     ------------------------------------------------------- */
  const allItems = Array.from(doc.querySelectorAll('.g-item'));
  const filterButtons = Array.from(doc.querySelectorAll('.filter'));
  const countEl = doc.getElementById('galleryCount');
  const emptyEl = doc.getElementById('galleryEmpty');

  const items = allItems.map((el) => ({
    el,
    cat: el.dataset.cat || '',
    title: el.dataset.title || '',
    meta: el.dataset.meta || '',
    desc: el.dataset.desc || '',
    image: el.dataset.image || '',
    sizes: el.dataset.sizes || ''
  }));

  // Track which items are visible so the lightbox only cycles the filtered set.
  let visibleItems = items.slice();
  let current = 0;

  function applyFilter(filter) {
    visibleItems = [];

    items.forEach((item) => {
      const matches = filter === 'all' || item.cat === filter;
      item.el.classList.toggle('is-hidden', !matches);
      if (matches) visibleItems.push(item);
    });

    filterButtons.forEach((btn) => {
      const active = (btn.dataset.filter || 'all') === filter;
      btn.classList.toggle('is-active', active);
      btn.setAttribute('aria-pressed', String(active));
    });

    if (countEl) {
      const n = visibleItems.length;
      countEl.textContent = n + (n === 1 ? ' piece' : ' pieces');
    }
    if (emptyEl) emptyEl.classList.toggle('is-shown', visibleItems.length === 0);

    // Reflect the filter in the URL without jumping the page. Guarded because
    // some browsers block history changes on file:// pages.
    try {
      const url = new URL(window.location.href);
      if (filter === 'all') url.searchParams.delete('filter');
      else url.searchParams.set('filter', filter);
      window.history.replaceState(null, '', url);
    } catch (err) {
      /* Filtering still works; only the shareable URL is skipped. */
    }
  }

  filterButtons.forEach((button) => {
    button.addEventListener('click', () => {
      applyFilter(button.dataset.filter || 'all');
    });
  });

  // Deep links such as appliances.html?filter=stove
  const initial = new URLSearchParams(window.location.search).get('filter');
  if (initial && filterButtons.some((b) => b.dataset.filter === initial)) {
    applyFilter(initial);
  } else {
    applyFilter('all');
  }

  /* -------------------------------------------------------
     Lightbox
     ------------------------------------------------------- */
  const lightbox = doc.getElementById('lightbox');
  const lbImage = doc.getElementById('lbImage');
  const lbTitle = doc.getElementById('lbTitle');
  const lbMeta = doc.getElementById('lbMeta');
  const lbDesc = doc.getElementById('lbDesc');
  const lbSizes = doc.getElementById('lbSizes');
  const lbEnquire = doc.getElementById('lbEnquire');
  const lbCount = doc.getElementById('lbCount');
  const lbClose = doc.getElementById('lbClose');
  const lbPrev = doc.getElementById('lbPrev');
  const lbNext = doc.getElementById('lbNext');

  let lastFocused = null;

  function whatsappLink(title) {
    return 'https://wa.me/8801400993386?text=' +
      encodeURIComponent('Hello Jahid Crockeries, I\'m interested in the ' + title + '.');
  }

  function renderItem(index) {
    if (!visibleItems.length) return;
    current = (index + visibleItems.length) % visibleItems.length;
    const item = visibleItems[current];

    lbImage.src = item.image;
    lbImage.alt = item.title + ' — Jahid Crockeries';
    lbTitle.innerHTML = item.title;
    lbMeta.innerHTML = item.meta;
    lbDesc.textContent = item.desc;
    lbEnquire.href = whatsappLink(item.title);
    lbCount.textContent =
      String(current + 1).padStart(2, '0') + ' / ' + String(visibleItems.length).padStart(2, '0');

    if (lbSizes) {
      lbSizes.textContent = item.sizes;
      lbSizes.style.display = item.sizes ? '' : 'none';
    }
  }

  function openLightbox(item) {
    if (!lightbox) return;
    const index = visibleItems.indexOf(item);
    lastFocused = doc.activeElement;
    renderItem(index < 0 ? 0 : index);
    lightbox.hidden = false;
    body.classList.add('menu-open');
    if (lbClose) lbClose.focus();
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.hidden = true;
    body.classList.remove('menu-open');
    lbImage.src = '';
    if (lastFocused && typeof lastFocused.focus === 'function') lastFocused.focus();
  }

  items.forEach((item) => {
    item.el.addEventListener('click', () => openLightbox(item));
  });

  if (lbClose) lbClose.addEventListener('click', closeLightbox);
  if (lbPrev) lbPrev.addEventListener('click', () => renderItem(current - 1));
  if (lbNext) lbNext.addEventListener('click', () => renderItem(current + 1));

  if (lightbox) {
    lightbox.addEventListener('click', (event) => {
      if (event.target === lightbox) closeLightbox();
    });
  }

  doc.addEventListener('keydown', (event) => {
    if (!lightbox || lightbox.hidden) return;

    if (event.key === 'Escape') {
      event.preventDefault();
      closeLightbox();
    } else if (event.key === 'ArrowLeft') {
      event.preventDefault();
      renderItem(current - 1);
    } else if (event.key === 'ArrowRight') {
      event.preventDefault();
      renderItem(current + 1);
    } else if (event.key === 'Tab') {
      const focusables = Array.from(lightbox.querySelectorAll('button, a[href]'))
        .filter((el) => el.offsetParent !== null);
      if (!focusables.length) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (event.shiftKey && doc.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && doc.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });

  /* -------------------------------------------------------
     FAQ accordion
     ------------------------------------------------------- */
  const faqItems = Array.from(doc.querySelectorAll('.faq__item'));

  faqItems.forEach((item) => {
    const button = item.querySelector('.faq__q');
    const panel = item.querySelector('.faq__a');
    if (!button || !panel) return;

    button.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');

      faqItems.forEach((other) => {
        other.classList.remove('is-open');
        const otherBtn = other.querySelector('.faq__q');
        const otherPanel = other.querySelector('.faq__a');
        if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
        if (otherPanel) otherPanel.style.maxHeight = null;
      });

      if (!isOpen) {
        item.classList.add('is-open');
        button.setAttribute('aria-expanded', 'true');
        panel.style.maxHeight = panel.scrollHeight + 'px';
      }
    });
  });

  /* -------------------------------------------------------
     Reading progress
     ------------------------------------------------------- */
  const progress = doc.createElement('div');
  progress.className = 'scroll-progress';
  progress.setAttribute('aria-hidden', 'true');
  const progressBar = doc.createElement('span');
  progress.appendChild(progressBar);
  body.appendChild(progress);

  let progressTick = false;
  function paintProgress() {
    const max = doc.documentElement.scrollHeight - window.innerHeight;
    const ratio = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
    progressBar.style.width = (ratio * 100) + '%';
    progress.classList.toggle('is-active', ratio > 0.004);
    progressTick = false;
  }
  function queueProgress() {
    if (progressTick) return;
    progressTick = true;
    window.requestAnimationFrame(paintProgress);
  }
  paintProgress();
  window.addEventListener('scroll', queueProgress, { passive: true });
  window.addEventListener('resize', queueProgress, { passive: true });
  window.addEventListener('load', paintProgress);

  /* -------------------------------------------------------
     Year
     ------------------------------------------------------- */
  const year = doc.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

})();
