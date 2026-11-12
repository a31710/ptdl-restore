/* PTDL static site: original scripts (no libraries). Every effect is optional: without JS the content stays visible. */
(function () {
  "use strict";
  var root = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* preloader: hide when the page has loaded (never longer than 1.5 s) */
  var pre = $("#preloader");
  function hidePre() { if (pre) { pre.classList.add("done"); } }
  if (document.readyState === "complete") { hidePre(); } else { window.addEventListener("load", hidePre); setTimeout(hidePre, 1500); }

  /* sticky header shadow */
  var header = $(".site-header");
  function onScroll() { if (header) { header.classList.toggle("scrolled", window.scrollY > 40); } }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* mobile menu (slide-in panel) */
  var toggle = $(".nav-toggle"), nav = $("#menu");
  if (toggle && nav) {
    var overlay = document.createElement("div");
    overlay.className = "nav-overlay";
    document.body.appendChild(overlay);
    var close = document.createElement("button");
    close.type = "button"; close.className = "nav-close"; close.setAttribute("aria-label", "Đóng menu"); close.textContent = "×";
    nav.insertBefore(close, nav.firstChild);
    var setOpen = function (open) {
      document.body.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      if (open) { close.focus(); } else { toggle.focus(); }
    };
    toggle.addEventListener("click", function () { setOpen(!document.body.classList.contains("nav-open")); });
    close.addEventListener("click", function () { setOpen(false); });
    overlay.addEventListener("click", function () { setOpen(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && document.body.classList.contains("nav-open")) { setOpen(false); } });
    $$("a", nav).forEach(function (a) { a.addEventListener("click", function () { if (document.body.classList.contains("nav-open")) { setOpen(false); } }); });
  }

  /* services dropdown: on touch screens the first tap opens the card, a second tap follows the link; Esc or an outside tap closes it */
  var sub = $(".has-sub");
  if (sub) {
    var parentLink = $(":scope > a", sub);
    var closeSub = function () { sub.classList.remove("dropdown-open"); };
    if (parentLink) {
      parentLink.addEventListener("click", function (e) {
        var wide = window.matchMedia("(min-width: 1024px)").matches, touch = window.matchMedia("(hover: none)").matches;
        if (wide && touch && !sub.classList.contains("dropdown-open")) { e.preventDefault(); sub.classList.add("dropdown-open"); }
      });
    }
    document.addEventListener("click", function (e) { if (!sub.contains(e.target)) { closeSub(); } });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") { closeSub(); } });
  }

  /* split headings into words so they can slide in one by one */
  $$(".words").forEach(function (el) {
    var words = el.textContent.trim().split(/\s+/);
    el.setAttribute("aria-label", el.textContent.trim());
    el.innerHTML = words.map(function (w, i) { return '<span class="w" aria-hidden="true" style="--i:' + i + '">' + w + "</span> "; }).join("");
  });

  /* reveal on scroll */
  var revealTargets = $$("[data-anim], .words");
  if (!("IntersectionObserver" in window) || reduce) {
    revealTargets.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { threshold: 0.15, rootMargin: "0px 0px -6% 0px" });
    revealTargets.forEach(function (el) {
      var d = el.getAttribute("data-delay"); if (d) { el.style.setProperty("--d", d + "ms"); }
      io.observe(el);
    });
  }

  /* counters count up when they scroll into view */
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, "."); }
  function runCount(el) {
    /* the number count-up is short and carries information, so it still runs when the system asks for reduced motion (just faster) */
    var target = parseInt(el.getAttribute("data-count"), 10) || 0, dur = reduce ? 900 : 1800, t0 = null;
    function step(ts) {
      if (t0 === null) { t0 = ts; }
      var p = Math.min((ts - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(Math.round(target * eased));
      if (p < 1) { requestAnimationFrame(step); }
    }
    requestAnimationFrame(step);
    setTimeout(function () { el.textContent = fmt(target); }, dur + 150);   /* safety net if frames are throttled (background tab) */
  }
  var counters = $$("[data-count]");
  if (counters.length) {
    if ("IntersectionObserver" in window) {
      var co = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { runCount(en.target); co.unobserve(en.target); } });
      }, { threshold: 0.4 });
      counters.forEach(function (el) { el.textContent = "0"; co.observe(el); });
    } else { counters.forEach(function (el) { el.textContent = fmt(el.getAttribute("data-count")); }); }
  }

  /* carousels: autoplay 5 s, loop, buttons, dots, swipe, pause on hover and focus */
  $$("[data-carousel]").forEach(function (car) {
    var track = $(".slide-track", car), slides = $$(".slide", track), dotsBox = $(".dots", car);
    if (!track || slides.length < 2) { return; }
    var i = 0, timer = null, startX = null;
    var dots = slides.map(function (_, n) {
      var b = document.createElement("button");
      b.type = "button"; b.setAttribute("aria-label", "Nhận xét " + (n + 1));
      b.addEventListener("click", function () { go(n); restart(); });
      if (dotsBox) { dotsBox.appendChild(b); }
      return b;
    });
    function go(n) {
      i = (n + slides.length) % slides.length;
      track.style.transform = "translateX(" + (-100 * i) + "%)";
      slides.forEach(function (s, k) { s.setAttribute("aria-hidden", k === i ? "false" : "true"); });
      dots.forEach(function (d, k) { d.setAttribute("aria-current", k === i ? "true" : "false"); });
    }
    function restart() { clearInterval(timer); if (!reduce) { timer = setInterval(function () { go(i + 1); }, 5000); } }
    var prev = $("[data-prev]", car), next = $("[data-next]", car);
    if (prev) { prev.addEventListener("click", function () { go(i - 1); restart(); }); }
    if (next) { next.addEventListener("click", function () { go(i + 1); restart(); }); }
    car.addEventListener("mouseenter", function () { clearInterval(timer); });
    car.addEventListener("mouseleave", restart);
    car.addEventListener("focusin", function () { clearInterval(timer); });
    car.addEventListener("focusout", restart);
    track.addEventListener("pointerdown", function (e) { startX = e.clientX; });
    track.addEventListener("pointerup", function (e) {
      if (startX !== null && Math.abs(e.clientX - startX) > 40) { go(i + (e.clientX < startX ? 1 : -1)); restart(); }
      startX = null;
    });
    car.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") { go(i - 1); restart(); } else if (e.key === "ArrowRight") { go(i + 1); restart(); }
    });
    go(0); restart();
  });

  /* partner logos: duplicate the list once so the marquee loops without a gap */
  $$(".brands").forEach(function (ul) {
    if (reduce) { return; }
    $$("li", ul).forEach(function (li) { var c = li.cloneNode(true); c.setAttribute("aria-hidden", "true"); ul.appendChild(c); });
  });

  /* business lines: hover and keyboard focus are pure CSS; on touch screens the first tap previews a row, the second tap follows its link */
  var rows = $$(".row-item");
  if (rows.length) {
    var touchMode = function () { return window.matchMedia("(hover: none)").matches || window.innerWidth < 900; };
    rows.forEach(function (row) {
      row.addEventListener("click", function (e) {
        if (!touchMode() || e.target.closest(".go")) { return; }
        var was = row.classList.contains("active");
        rows.forEach(function (r) { r.classList.remove("active"); });
        if (!was) { row.classList.add("active"); } else { window.location.href = $(".go", row).getAttribute("href"); }
      });
    });
    document.addEventListener("click", function (e) { if (!e.target.closest(".row-item")) { rows.forEach(function (r) { r.classList.remove("active"); }); } });
  }

  /* news: filter pills and the "show all" toggle (the 4th article stays hidden until asked for) */
  $$("[data-news]").forEach(function (sec) {
    var cards = $$(".card", sec), pills = $$("[data-filter]", sec), toggle = $("[data-news-toggle]", sec);
    var filter = "all", open = false;
    function render() {
      cards.forEach(function (c) {
        var show = filter === "all" ? (!c.hasAttribute("data-extra") || open) : c.getAttribute("data-cat") === filter;
        c.hidden = !show;
      });
      if (toggle) {
        toggle.parentNode.hidden = filter !== "all";
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        toggle.textContent = open ? "Thu gọn danh sách" : "Xem tất cả tin tức";
      }
    }
    pills.forEach(function (b) {
      b.addEventListener("click", function () {
        filter = b.getAttribute("data-filter");
        pills.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        render();
      });
    });
    if (toggle) { toggle.addEventListener("click", function () { open = !open; render(); }); }
    render();
  });

  /* km slider shows its value */
  $$("input[type=range][data-output]").forEach(function (r) {
    var out = document.getElementById(r.getAttribute("data-output"));
    var show = function () {
      if (out) { out.textContent = r.value + " km"; }
      r.style.setProperty("--p", (100 * (r.value - r.min) / (r.max - r.min)) + "%");
    };
    r.addEventListener("input", show); show();
  });

  /* video: open YouTube in a dialog (the request to YouTube only happens after the click) */
  $$("[data-video]").forEach(function (link) {
    link.addEventListener("click", function (e) {
      var id = link.getAttribute("data-video");
      if (!id || typeof HTMLDialogElement === "undefined") { return; }
      e.preventDefault();
      var dlg = document.createElement("dialog");
      dlg.className = "video-dialog";
      var x = document.createElement("button");
      x.type = "button"; x.className = "x"; x.setAttribute("aria-label", "Đóng video"); x.textContent = "×";
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) + "?autoplay=1&rel=0";
      f.title = "Video giới thiệu PTDL"; f.allow = "autoplay; encrypted-media; picture-in-picture"; f.allowFullscreen = true;
      dlg.appendChild(x); dlg.appendChild(f); document.body.appendChild(dlg);
      var shut = function () { dlg.close(); };
      x.addEventListener("click", shut);
      dlg.addEventListener("click", function (ev) { if (ev.target === dlg) { shut(); } });
      dlg.addEventListener("close", function () { dlg.remove(); link.focus(); });
      dlg.showModal();
    });
  });
})();
