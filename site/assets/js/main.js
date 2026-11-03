// PTDL static site: mobile menu toggle only.
(function () {
  var root = document.documentElement;
  root.className += ' js';
  var btn = document.querySelector('.nav-toggle');
  var nav = document.getElementById('menu');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
