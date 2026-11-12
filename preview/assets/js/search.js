/* PTDL site search: original script, no libraries. Needs assets/js/search-index.js (window.PTDL_SEARCH).
   Opens from any [data-search-open] button, from "/" and from Ctrl/Cmd+K. Matching ignores case and Vietnamese
   diacritics, so "bao hiem" finds "Bảo hiểm". Without JavaScript the search buttons simply stay inert. */
(function () {
  "use strict";
  var DATA = window.PTDL_SEARCH || [];
  var RECENT_KEY = "ptdl_recent_search";
  var POPULAR = ["Bảng giá", "Bảo hiểm hàng hóa", "Chuyển nhà", "Vận tải Bắc Nam", "Container", "Liên hệ"];
  var KIND_LABEL = { "Trang": "Trang và dịch vụ", "Tin tức": "Tin tức" };
  var MAX_PER_PAGE = 4, MAX_RESULTS = 30;

  var dlg, input, list, meta, clearBtn, body;
  var trigger = null, items = [], active = -1, timer = null, cache = null;

  /* ---------- text helpers ---------- */
  /* One output character for every input character, so positions in the folded text line up with the original. */
  function fold(s) {
    s = String(s || "");
    var out = "";
    for (var i = 0; i < s.length; i++) {
      var c = s.charAt(i);
      if (c === "đ" || c === "Đ") { out += "d"; continue; }
      var b = c.normalize("NFD").replace(/[̀-ͯ]/g, "");
      b = b.length ? b.charAt(0).toLowerCase() : " ";
      out += /[a-z0-9]/.test(b) ? b : " ";
    }
    return out;
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; });
  }
  function tokens(q) { return fold(q).split(/\s+/).filter(Boolean); }
  function wordStart(hay, t) { return hay.indexOf(" " + t) !== -1 || hay.indexOf(t) === 0; }
  function wholeWord(hay, t) { return (" " + hay + " ").indexOf(" " + t + " ") !== -1; }

  function prepare() {
    if (cache) { return cache; }
    cache = DATA.map(function (d) { return { d: d, nt: fold(d.t), nh: fold(d.h), nx: fold(d.x) }; });
    return cache;
  }

  /* ---------- searching and scoring ---------- */
  function run(q) {
    var toks = tokens(q), phrase = toks.join(" ");
    if (!toks.length) { return []; }
    var scored = [];
    prepare().forEach(function (e) {
      var score = 0, ok = true;
      for (var i = 0; i < toks.length; i++) {
        var t = toks[i], s = 0, longTok = t.length >= 4;
        /* a word has to start with the typed text; matches inside a word count only for longer terms */
        if (wordStart(e.nt, t)) { s += 30 + (wholeWord(e.nt, t) ? 12 : 0); } else if (longTok && e.nt.indexOf(t) !== -1) { s += 8; }
        if (wordStart(e.nh, t)) { s += 18 + (wholeWord(e.nh, t) ? 8 : 0); } else if (longTok && e.nh.indexOf(t) !== -1) { s += 5; }
        if (wordStart(e.nx, t)) { s += 4 + (wholeWord(e.nx, t) ? 2 : 0); } else if (longTok && e.nx.indexOf(t) !== -1) { s += 1; }
        if (!s) { ok = false; break; }
        score += s;
      }
      if (!ok) { return; }
      if (toks.length > 1) {
        if (e.nt.indexOf(phrase) !== -1) { score += 60; }
        if (e.nh.indexOf(phrase) !== -1) { score += 40; }
        if (e.nx.indexOf(phrase) !== -1) { score += 15; }
      }
      if (!e.d.h) { score += 6; }
      scored.push({ e: e, score: score });
    });
    scored.sort(function (a, b) { return b.score - a.score || a.e.d.x.length - b.e.d.x.length; });
    var perPage = {}, out = [];
    for (var k = 0; k < scored.length && out.length < MAX_RESULTS; k++) {
      var file = scored[k].e.d.u.split("#")[0];
      perPage[file] = (perPage[file] || 0) + 1;
      if (perPage[file] <= MAX_PER_PAGE) { out.push(scored[k].e); }
    }
    return out;
  }

  function highlight(text, toks) {
    var f = fold(text), marks = [];
    toks.forEach(function (t) {
      var from = 0, at;
      while ((at = f.indexOf(t, from)) !== -1) { marks.push([at, at + t.length]); from = at + t.length; }
    });
    if (!marks.length) { return esc(text); }
    marks.sort(function (a, b) { return a[0] - b[0]; });
    var merged = [marks[0]];
    for (var i = 1; i < marks.length; i++) {
      var last = merged[merged.length - 1];
      if (marks[i][0] <= last[1]) { last[1] = Math.max(last[1], marks[i][1]); } else { merged.push(marks[i]); }
    }
    var html = "", pos = 0;
    merged.forEach(function (m) {
      html += esc(text.slice(pos, m[0])) + "<mark>" + esc(text.slice(m[0], m[1])) + "</mark>";
      pos = m[1];
    });
    return html + esc(text.slice(pos));
  }

  function snippet(text, toks) {
    if (!text) { return ""; }
    var f = fold(text), first = -1;
    toks.forEach(function (t) { var i = f.indexOf(t); if (i !== -1 && (first === -1 || i < first)) { first = i; } });
    if (first === -1) { return highlight(text.slice(0, 150) + (text.length > 150 ? "…" : ""), toks); }
    var start = Math.max(0, first - 70), end = Math.min(text.length, first + 130);
    var piece = text.slice(start, end);
    return (start > 0 ? "…" : "") + highlight(piece, toks) + (end < text.length ? "…" : "");
  }

  /* ---------- recent searches ---------- */
  function recent() {
    try { var v = JSON.parse(localStorage.getItem(RECENT_KEY) || "[]"); return Array.isArray(v) ? v : []; } catch (e) { return []; }
  }
  function saveRecent(q) {
    q = q.trim();
    if (q.length < 2) { return; }
    var r = recent().filter(function (x) { return fold(x) !== fold(q); });
    r.unshift(q);
    try { localStorage.setItem(RECENT_KEY, JSON.stringify(r.slice(0, 6))); } catch (e) { /* private mode: ignore */ }
  }
  function clearRecent() { try { localStorage.removeItem(RECENT_KEY); } catch (e) { /* ignore */ } }

  /* ---------- rendering ---------- */
  function chips(arr) {
    return '<div class="sr-chips">' + arr.map(function (t) { return '<button type="button" class="sr-chip" data-q="' + esc(t) + '">' + esc(t) + "</button>"; }).join("") + "</div>";
  }
  function quickLinks() {
    var links = [].slice.call(document.querySelectorAll("#menu > ul > li > a"));
    if (!links.length) { return ""; }
    return '<div class="sr-quick">' + links.map(function (a) { return '<a href="' + esc(a.getAttribute("href")) + '">' + esc(a.textContent.trim()) + "</a>"; }).join("") + "</div>";
  }

  function renderEmpty() {
    items = []; active = -1;
    input.setAttribute("aria-expanded", "false");
    input.removeAttribute("aria-activedescendant");
    var r = recent(), html = "";
    if (r.length) {
      html += '<div class="sr-block"><div class="sr-label">Tìm kiếm gần đây <button type="button" class="sr-link" data-clear-recent>Xóa</button></div>' + chips(r) + "</div>";
    }
    html += '<div class="sr-block"><div class="sr-label">Gợi ý phổ biến</div>' + chips(POPULAR) + "</div>";
    var q = quickLinks();
    if (q) { html += '<div class="sr-block"><div class="sr-label">Đi nhanh tới</div>' + q + "</div>"; }
    list.innerHTML = html;
    list.removeAttribute("role");
    meta.textContent = "Nhập từ khóa để tìm trong website PTDL.";
  }

  function renderResults(q) {
    var toks = tokens(q), res = run(q);
    list.setAttribute("role", "listbox");
    if (!res.length) {
      items = []; active = -1;
      input.setAttribute("aria-expanded", "false");
      list.innerHTML = '<div class="sr-none"><b>Không tìm thấy kết quả cho “' + esc(q.trim()) + '”.</b>' +
        "<p>Thử từ khóa ngắn hơn, bỏ dấu hoặc chọn một gợi ý bên dưới. Cần hỗ trợ ngay? Gọi <a href=\"tel:02855555565\">0285 5555 565</a>.</p>" +
        chips(POPULAR) + "</div>";
      list.removeAttribute("role");
      meta.textContent = "Không có kết quả.";
      return;
    }
    var html = "", n = 0, groups = {}, order = [];
    res.forEach(function (e) {
      if (!groups[e.d.k]) { groups[e.d.k] = []; order.push(e.d.k); }
      groups[e.d.k].push(e);
    });
    order.forEach(function (k) {
      html += '<div class="sr-group" role="presentation">' + esc(KIND_LABEL[k] || k) + "</div>";
      groups[k].forEach(function (e) {
        var d = e.d, path = d.h ? esc(d.t) + " › " + esc(d.h) : esc(d.t);
        var title = d.h ? highlight(d.h, toks) : highlight(d.t, toks);
        html += '<div class="sr-item" role="option" id="sr-opt-' + n + '" data-i="' + n + '" aria-selected="false">' +
          '<a href="' + esc(d.u) + '"><span class="sr-title">' + title + '</span><span class="sr-path">' + path + "</span>" +
          '<span class="sr-snip">' + snippet(d.x, toks) + "</span></a></div>";
        n++;
      });
    });
    list.innerHTML = html;
    items = [].slice.call(list.querySelectorAll(".sr-item"));
    input.setAttribute("aria-expanded", "true");
    meta.textContent = "Tìm thấy " + res.length + " kết quả cho “" + q.trim() + "”.";
    setActive(0, false);
  }

  function setActive(i, scroll) {
    if (!items.length) { return; }
    active = (i + items.length) % items.length;
    items.forEach(function (el, k) { el.setAttribute("aria-selected", k === active ? "true" : "false"); });
    input.setAttribute("aria-activedescendant", items[active].id);
    if (scroll !== false) { items[active].scrollIntoView({ block: "nearest" }); }
  }

  function update() {
    var q = input.value;
    clearBtn.hidden = !q;
    if (!q.trim()) { renderEmpty(); } else { renderResults(q); }
    body.scrollTop = 0;
  }

  /* ---------- dialog ---------- */
  function build() {
    if (dlg) { return; }
    dlg = document.createElement("dialog");
    dlg.className = "search-dialog";
    dlg.setAttribute("aria-label", "Tìm kiếm trên website");
    dlg.innerHTML =
      '<div class="sr-head">' +
      '<svg class="svg" aria-hidden="true"><use href="' + iconHref() + '"/></svg>' +
      '<input class="sr-input" type="search" placeholder="Tìm dịch vụ, bảng giá, tin tức…" autocomplete="off" spellcheck="false" ' +
      'role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="sr-list" aria-label="Từ khóa tìm kiếm">' +
      '<button type="button" class="sr-clear" aria-label="Xóa từ khóa" hidden>×</button>' +
      '<button type="button" class="sr-close" aria-label="Đóng tìm kiếm"><span>Esc</span></button>' +
      "</div>" +
      '<div class="sr-meta" role="status" aria-live="polite"></div>' +
      '<div class="sr-body"><div id="sr-list" class="sr-list"></div></div>' +
      '<div class="sr-foot"><span><kbd>↑</kbd><kbd>↓</kbd> chọn</span><span><kbd>Enter</kbd> mở</span><span><kbd>Esc</kbd> đóng</span></div>';
    document.body.appendChild(dlg);
    input = dlg.querySelector(".sr-input");
    list = dlg.querySelector("#sr-list");
    meta = dlg.querySelector(".sr-meta");
    clearBtn = dlg.querySelector(".sr-clear");
    body = dlg.querySelector(".sr-body");

    input.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(update, 60); });
    input.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); setActive(active + 1); }
      else if (e.key === "ArrowUp") { e.preventDefault(); setActive(active - 1); }
      else if (e.key === "Home" && items.length) { e.preventDefault(); setActive(0); }
      else if (e.key === "End" && items.length) { e.preventDefault(); setActive(items.length - 1); }
      else if (e.key === "Enter") {
        e.preventDefault();
        var a = items[active >= 0 ? active : 0];
        if (a) { choose(a.querySelector("a")); }
      }
    });
    clearBtn.addEventListener("click", function () { input.value = ""; update(); input.focus(); });
    dlg.querySelector(".sr-close").addEventListener("click", close);
    dlg.addEventListener("click", function (e) {
      if (e.target === dlg) { close(); return; }
      var chip = e.target.closest(".sr-chip");
      if (chip) { input.value = chip.getAttribute("data-q"); update(); input.focus(); return; }
      if (e.target.closest("[data-clear-recent]")) { clearRecent(); renderEmpty(); return; }
      var row = e.target.closest(".sr-item a");
      if (row) { saveRecent(input.value); close(); return; }
      if (e.target.closest(".sr-quick a, .sr-none a")) { close(); }
    });
    list.addEventListener("mousemove", function (e) {
      var row = e.target.closest(".sr-item");
      if (row) { var i = +row.getAttribute("data-i"); if (i !== active) { setActive(i, false); } }
    });
    dlg.addEventListener("close", function () {
      document.documentElement.classList.remove("search-open");
      if (trigger && document.contains(trigger)) { trigger.focus(); }
    });
  }

  function iconHref() {
    var u = document.querySelector('use[href*="icons.svg"]');
    var base = u ? u.getAttribute("href").split("#")[0] : "assets/images/icons.svg";
    return base + "#i-search";
  }

  function choose(a) {
    if (!a) { return; }
    saveRecent(input.value);
    var href = a.getAttribute("href");
    close();
    window.location.href = href;
  }

  function open(prefill) {
    build();
    if (!dlg.open) {
      if (typeof dlg.showModal === "function") { dlg.showModal(); } else { dlg.setAttribute("open", ""); }
    }
    document.documentElement.classList.add("search-open");
    if (typeof prefill === "string") { input.value = prefill; }
    update();
    input.focus();
    input.select();
  }
  function close() {
    if (!dlg || !dlg.open) { return; }
    if (typeof dlg.close === "function") { dlg.close(); } else { dlg.removeAttribute("open"); document.documentElement.classList.remove("search-open"); }
  }

  /* ---------- triggers ---------- */
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-search-open]");
    if (t) { e.preventDefault(); trigger = t; open(); }
  });
  document.addEventListener("keydown", function (e) {
    var el = e.target, typing = el && (/^(input|textarea|select)$/i.test(el.tagName) || el.isContentEditable);
    var isK = (e.key === "k" || e.key === "K") && (e.ctrlKey || e.metaKey);
    if ((e.key === "/" && !typing && !e.ctrlKey && !e.metaKey && !e.altKey) || isK) {
      e.preventDefault();
      trigger = document.activeElement;
      open();
    }
  });
})();
