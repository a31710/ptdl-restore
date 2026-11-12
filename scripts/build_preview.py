"""Build preview/ from site/ with the same URLs the WordPress site used.

Real permalinks (from the WordPress REST data):
  pages  : /gioi-thieu, /services, /services/chuyen-hang-bac-nam, /lien-he, /blog  (no trailing slash)
  posts  : /<slug>.htm
  category: /category/cam-nang-van-chuyen
site/ stays the flat, hand-edited source; preview/ is generated, so rerun this script after editing site/.
"""
import importlib.util
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "site"
OUT = ROOT / "preview"
DOMAIN = "https://ptdl.com.vn"

# source file -> (public URL, output file relative to preview/)
PAGES = {
    "index.html": ("/", "index.html"),
    "gioi-thieu.html": ("/gioi-thieu", "gioi-thieu.html"),
    "dich-vu.html": ("/services", "services.html"),
    "chuyen-hang-bac-nam.html": ("/services/chuyen-hang-bac-nam", "services/chuyen-hang-bac-nam.html"),
    "tin-tuc.html": ("/blog", "blog.html"),
    "lien-he.html": ("/lien-he", "lien-he.html"),
    "le-ban-giao-lo-xe-thaco.html": ("/le-ban-giao-lo-xe-thaco.htm", "le-ban-giao-lo-xe-thaco.htm"),
    "huong-dan-gui-hang-di-uc-tai-binh-duong.html": (
        "/huong-dan-gui-hang-di-uc-tai-binh-duong-an-toan-va-nhanh-chong.htm",
        "huong-dan-gui-hang-di-uc-tai-binh-duong-an-toan-va-nhanh-chong.htm"),
    "cach-chuyen-nha-duong-dai-o-ha-noi.html": ("/cach-chuyen-nha-duong-dai-o-ha-noi.htm", "cach-chuyen-nha-duong-dai-o-ha-noi.htm"),
    "bao-hiem-hang-hoa.html": (
        "/bao-hiem-hang-hoa-la-gi-tai-sao-doanh-nghiep-nen-mua.htm",
        "bao-hiem-hang-hoa-la-gi-tai-sao-doanh-nghiep-nen-mua.htm"),
}
URL_BAC_NAM = "/services/chuyen-hang-bac-nam"
URL_CATEGORY = "/category/cam-nang-van-chuyen"
LINK_RE = re.compile(r'(href|src|poster)="([^"]*)"')


def rewrite_links(html: str) -> str:
    def fix(m: re.Match) -> str:
        attr, value = m.group(1), m.group(2)
        if value.startswith(("http:", "https:", "mailto:", "tel:", "#", "data:", "/")) or not value:
            return m.group(0)
        path, _, frag = value.partition("#")
        if path in PAGES:
            new = PAGES[path][0] + ("#" + frag if frag else "")
        elif path.startswith("assets/"):
            new = "/" + value
        else:
            return m.group(0)
        return f'{attr}="{new}"'
    return LINK_RE.sub(fix, html)


def add_canonical(html: str, url: str) -> str:
    canonical = f'<link rel="canonical" href="{DOMAIN}{url if url != "/" else "/"}">\n'
    return html.replace('<link rel="icon"', canonical + '<link rel="icon"', 1)


def write(out_rel: str, html: str) -> None:
    target = OUT / out_rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


def make_category_page(blog_html: str) -> str:
    page = re.sub(r"<title>.*?</title>", "<title>Chuyên mục: Cẩm nang vận chuyển | PTDL</title>", blog_html, flags=re.S)
    page = page.replace("<h1>Tin tức</h1>", "<h1>Cẩm nang vận chuyển</h1>", 1)
    page = page.replace("<p>Cẩm nang vận chuyển</p>", "<p>Chuyên mục</p>", 1)
    return page


def main() -> None:
    OUT.mkdir(exist_ok=True)
    # Empty the folder instead of deleting it: Windows refuses to remove a directory that a shell or server is using.
    for child in OUT.iterdir():
        shutil.rmtree(child) if child.is_dir() else child.unlink()
    spec = importlib.util.spec_from_file_location("search_index", ROOT / "scripts" / "search_index.py")
    search_index = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(search_index)
    search_index.main()
    shutil.copytree(SRC / "assets", OUT / "assets")
    index_js = OUT / "assets" / "js" / "search-index.js"
    text = index_js.read_text(encoding="utf-8")
    for name, (url, _) in PAGES.items():
        text = text.replace(f'"u":"{name}', f'"u":"{url}')
    index_js.write_text(text, encoding="utf-8")
    for extra in (ROOT / "scripts" / "preview_files").iterdir():
        shutil.copy(extra, OUT / extra.name)

    sources = {name: (SRC / name).read_text(encoding="utf-8") for name in PAGES}
    sources["__category__"] = make_category_page(sources["tin-tuc.html"])

    targets = dict(PAGES)
    targets["__category__"] = (URL_CATEGORY, "category/cam-nang-van-chuyen.html")
    for name, html in sources.items():
        url, out_rel = targets[name]
        html = rewrite_links(html)
        write(out_rel, add_canonical(html, url))

    not_found = rewrite_links((SRC / "404.html").read_text(encoding="utf-8"))
    write("404.html", not_found)

    urls = [u for u, _ in targets.values()]
    sitemap = "".join(f"  <url><loc>{DOMAIN}{u if u != '/' else '/'}</loc></url>\n" for u in urls)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + sitemap + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")

    labels = {
        "/": "Trang chủ", "/gioi-thieu": "Giới thiệu", "/services": "Dịch vụ", URL_BAC_NAM: "Chuyển hàng Bắc – Nam",
        "/blog": "Tin tức (trang blog)", URL_CATEGORY: "Chuyên mục Cẩm nang vận chuyển", "/lien-he": "Liên hệ",
    }
    rows = []
    for u in urls:
        label = labels.get(u, "Bài viết: " + u.strip("/").removesuffix(".htm").replace("-", " "))
        rows.append(f'<tr><td>{label}</td><td><a href="{u}">{u}</a></td></tr>')
    rows.append('<tr><td>Trang 404</td><td><a href="/khong-ton-tai">/khong-ton-tai</a></td></tr>')
    write("_links.html", f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>Danh sách liên kết xem trước | PTDL</title>
<style>body{{font:16px/1.5 system-ui,sans-serif;max-width:820px;margin:2rem auto;padding:0 1rem;color:#222}}
table{{border-collapse:collapse;width:100%}}td,th{{border-bottom:1px solid #ddd;padding:.5rem;text-align:left}}a{{color:#3f6a14}}</style></head>
<body><h1>Danh sách liên kết xem trước</h1>
<p>Các đường dẫn giống cấu trúc đường dẫn cố định (permalink) của WordPress cũ: trang không có dấu gạch chéo cuối, bài viết kết thúc bằng <code>.htm</code>.</p>
<table><tr><th>Trang</th><th>Đường dẫn</th></tr>
{chr(10).join(rows)}
</table></body></html>
""")
    print(f"Built {len(targets)} pages + 404 + _links.html into {OUT}")


if __name__ == "__main__":
    main()
