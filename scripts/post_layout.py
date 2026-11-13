"""One-off: move the four article pages to the new layout (header band, article + sticky sidebar, related posts).

The article body itself is kept exactly as it was; only the wrapper around it changes. Safe to re-run (skips converted pages).
"""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "site"
POSTS = [
    "le-ban-giao-lo-xe-thaco.html",
    "bao-hiem-hang-hoa.html",
    "huong-dan-gui-hang-di-uc-tai-binh-duong.html",
    "cach-chuyen-nha-duong-dai-o-ha-noi.html",
]
CARD_RE = re.compile(r'      <article class="card"[^>]*>\n(.*?)      </article>\n', re.S)
ICON = lambda name: f'<svg class="svg" aria-hidden="true"><use href="assets/images/icons.svg#{name}"/></svg>'

news = (SRC / "tin-tuc.html").read_text(encoding="utf-8")
cards = {}
for m in CARD_RE.finditer(news):
    block = m.group(1)
    href = re.search(r'<a class="card-media" href="([^"]+)">', block).group(1)
    cards[href] = m.group(0).replace('      <article class="card" ', '      <article class="card" ', 1)

for name in POSTS:
    path = SRC / name
    html = path.read_text(encoding="utf-8")
    if "post-head" in html:
        continue
    m = re.search(r'<article class="section post">\n  <div class="wrap narrow">\n(.*?)\n  </div>\n</article>\n', html, re.S)
    inner = m.group(1)
    crumbs = re.search(r'    <p class="crumbs">.*?</p>\n', inner).group(0)
    h1 = re.search(r"    <h1>.*?</h1>\n", inner).group(0).strip()
    meta = re.search(r'    <p class="meta">(.*?)</p>\n', inner)
    cat, time_tag = [x.strip() for x in meta.group(1).split("·", 1)]
    body = inner.replace(crumbs, "").replace("    " + h1 + "\n", "").replace(meta.group(0), "")
    back = re.search(r'    <p class="back">.*?</p>\n?', body)
    body = body.replace(back.group(0), "") if back else body
    # first real paragraph becomes the lead
    body = re.sub(r"(\n    )<p>", r"\1<p class=\"lead\">", body, count=1) if not body.lstrip().startswith("<!--") else body
    if 'class="lead"' not in body:
        body = body.replace("<p>", '<p class="lead">', 1)
    related = "".join(cards[h] for h in cards if h != name)
    new = f'''<div class="read-bar" aria-hidden="true"><span id="read-bar"></span></div>
<header class="post-head">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">{ICON("i-home")}Trang chủ</a><span aria-hidden="true">/</span><a href="tin-tuc.html">Tin tức</a><span aria-hidden="true">/</span><span aria-current="page">{cat}</span></p>
    <div class="post-meta"><span class="cat">{cat}</span><span class="when">{ICON("i-calendar")}{time_tag}</span></div>
    {h1}
  </div>
</header>

<section class="section post">
  <div class="wrap post-grid">
    <article class="post-body" id="post-body">
{body}
      <div class="post-foot">
        <a class="btn back-btn" href="tin-tuc.html">&larr; Quay lại tin tức</a>
        <button class="btn copy-link" type="button" data-copy-link>{ICON("i-link")}Sao chép liên kết</button>
      </div>
    </article>
    <aside class="post-side" aria-label="Thông tin thêm">
      <nav class="toc" aria-label="Mục lục bài viết" data-toc hidden>
        <h2>Mục lục bài viết</h2>
        <ol></ol>
      </nav>
      <div class="side-cta">
        <h2>Liên hệ PTDL</h2>
        <a class="side-phone" href="tel:02855555565">{ICON("i-phone")}<span>0285 5555 565</span></a>
        <a class="btn btn-light" href="lien-he.html">Gửi yêu cầu báo giá</a>
      </div>
    </aside>
  </div>
</section>

<section class="section sec-related">
  <div class="wrap">
    <div class="sec-head" data-anim="up">
      <p class="sub-title">Cẩm nang vận chuyển</p>
      <h2 class="sec-title">Bài viết liên quan</h2>
    </div>
    <div class="grid grid-3">
{related}    </div>
    <p class="news-more"><a class="btn btn-light" href="tin-tuc.html">Xem tất cả tin tức</a></p>
  </div>
</section>
<div class="toast" id="toast" role="status" aria-live="polite" hidden></div>
'''
    html = html[: m.start()] + new + html[m.end():]
    path.write_text(html, encoding="utf-8", newline="\n")
    print("converted", name)
