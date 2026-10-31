/* BetterHealth preview. Progressive enhancement only: every piece of content is readable without this file. */
(function () {
  var doc = document;

  // Header border after scroll
  var header = doc.querySelector('.site-header');
  function onScroll() { header.classList.toggle('scrolled', window.scrollY > 8); }
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu
  var btn = doc.querySelector('.menu-btn'), nav = doc.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? btn.dataset.close : btn.dataset.open;
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && nav.classList.contains('open')) { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.textContent = btn.dataset.open; }
    });
  }

  // Map: layer nodes update the caption and highlight the matching row in the layers list
  var caption = doc.getElementById('map-caption');
  var layers = [].slice.call(doc.querySelectorAll('.layer'));
  var nodes = [].slice.call(doc.querySelectorAll('.map-node'));
  function selectLayer(i) {
    nodes.forEach(function (n) { n.classList.toggle('active', n.getAttribute('data-layer') === String(i)); });
    layers.forEach(function (l, idx) { l.classList.toggle('active', idx === i); });
    var l = layers[i];
    if (l && caption) caption.textContent = l.querySelector('h3').textContent + ' – ' + l.querySelector('p').textContent;
  }
  nodes.forEach(function (n) {
    var i = parseInt(n.getAttribute('data-layer'), 10);
    n.addEventListener('click', function () { selectLayer(i); });
    n.addEventListener('focus', function () { selectLayer(i); });
    n.addEventListener('mouseenter', function () { selectLayer(i); });
    n.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); selectLayer(i); } });
  });

  // Concerns selector (tabs). Without JavaScript every panel stays visible.
  var tabs = [].slice.call(doc.querySelectorAll('.sel-btn')), panels = [].slice.call(doc.querySelectorAll('.sel-panel'));
  function showTab(i, focus) {
    tabs.forEach(function (t, idx) { var on = idx === i; t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1; });
    panels.forEach(function (p, idx) { p.hidden = idx !== i; });
    if (focus) tabs[i].focus();
  }
  if (tabs.length) {
    showTab(0, false);
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { showTab(i, false); });
      t.addEventListener('keydown', function (e) {
        var k = e.key, n = tabs.length;
        if (k === 'ArrowDown' || k === 'ArrowRight') { e.preventDefault(); showTab((i + 1) % n, true); }
        else if (k === 'ArrowUp' || k === 'ArrowLeft') { e.preventDefault(); showTab((i - 1 + n) % n, true); }
        else if (k === 'Home') { e.preventDefault(); showTab(0, true); }
        else if (k === 'End') { e.preventDefault(); showTab(n - 1, true); }
      });
    });
  }

  // Contact form: validation and a preview notice. No data is sent anywhere until an endpoint is chosen.
  var form = doc.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.elements.name, contact = form.elements.contact, ok = true;
      [[name, 'e-name', form.dataset.errName], [contact, 'e-contact', form.dataset.errContact]].forEach(function (r) {
        var el = doc.getElementById(r[1]); var bad = !r[0].value.trim();
        el.hidden = !bad; el.textContent = bad ? r[2] : ''; r[0].setAttribute('aria-invalid', bad ? 'true' : 'false'); if (bad) ok = false;
      });
      var status = doc.getElementById('form-status');
      if (!ok) { status.hidden = true; var first = form.querySelector('[aria-invalid="true"]'); if (first) first.focus(); return; }
      status.hidden = false;
      var endpoint = form.dataset.endpoint;
      if (!endpoint) { status.textContent = form.dataset.preview; return; }
      fetch(endpoint, { method: 'POST', body: new FormData(form) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); status.textContent = form.dataset.sent; form.reset(); })
        .catch(function () { status.textContent = form.dataset.failed; });
    });
  }
})();
