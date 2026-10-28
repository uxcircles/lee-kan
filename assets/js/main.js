(function () {
  document.documentElement.classList.remove('no-js');

  // Sticky header shadow
  var header = document.querySelector('.site-header');
  var bar = document.querySelector('.concept-bar');
  function onScroll() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 8);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') !== 'true';
      // The menu sits under the header; account for the concept bar if it's still on screen
      var barH = bar ? Math.max(0, bar.offsetHeight - window.scrollY) : 0;
      document.documentElement.style.setProperty('--bar-h', barH + 'px');
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('open', open);
      document.body.classList.toggle('nav-open', open);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) toggle.click();
    });
  }

  // Reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Fees page: highlight the section in view
  var tocLinks = document.querySelectorAll('.toc a');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove('active'); });
          var a = map[en.target.id];
          if (a) a.classList.add('active');
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) spy.observe(el);
    });
  }

  // Services: "Ask about this" pre-selects the matter on the contact form
  var matter = document.getElementById('matter');
  if (matter) {
    var q = new URLSearchParams(location.search).get('matter');
    if (q) {
      for (var i = 0; i < matter.options.length; i++) {
        if (matter.options[i].value === q) { matter.selectedIndex = i; break; }
      }
    }
  }

  // Enquiry form opens a pre-filled email (no backend needed)
  var form = document.getElementById('enquiry-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var f = form.elements;
      var matterText = f.matter.options[f.matter.selectedIndex].text;
      var subject = 'Website enquiry: ' + matterText + ' (' + f.name.value + ')';
      var body = [
        'Name: ' + f.name.value,
        'Phone: ' + (f.phone.value || '-'),
        'Email: ' + f.email.value,
        'Matter: ' + matterText,
        '',
        f.message.value
      ].join('\n');
      location.href = 'mailto:info@lee-kan.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
  }
})();
