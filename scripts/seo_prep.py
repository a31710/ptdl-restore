"""One-off source fixes for SEO: shorter titles, image sizes (stops layout shift), hero image priority.

Run with Pillow available: python scripts/seo_prep.py   (safe to re-run)
"""
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "site"

TITLES = {
    "index.html": "PTDL – Vận chuyển hàng hóa Bắc Nam | Xe tải, container",
    "dich-vu.html": "Dịch vụ vận tải Bắc Nam, liên tỉnh, nội thành | PTDL",
    "le-ban-giao-lo-xe-thaco.html": "Lễ bàn giao lô xe Thaco Linker cho PTDL",
    "huong-dan-gui-hang-di-uc-tai-binh-duong.html": "Hướng dẫn gửi hàng đi Úc tại Bình Dương | PTDL",
}

IMG_RE = re.compile(r"<img\b[^>]*>")


def add_size(tag: str) -> str:
    if "width=" in tag or "height=" in tag:
        return tag
    m = re.search(r'src="(assets/images/[^"]+)"', tag)
    if not m:
        return tag
    path = SRC / m.group(1)
    if not path.exists():
        return tag
    w, h = Image.open(path).size
    return tag[:-1] + f' width="{w}" height="{h}">'


for page in sorted(SRC.glob("*.html")):
    html = page.read_text(encoding="utf-8")
    new = html
    if page.name in TITLES:
        new = re.sub(r"<title>.*?</title>", f"<title>{TITLES[page.name]}</title>", new, count=1, flags=re.S)
    new = IMG_RE.sub(lambda m: add_size(m.group(0)), new)
    if page.name == "index.html" and 'fetchpriority' not in new:
        new = new.replace('<img class="hero-truck"', '<img class="hero-truck" fetchpriority="high"', 1)
    if new != html:
        page.write_text(new, encoding="utf-8", newline="\n")
        print("updated", page.name)
