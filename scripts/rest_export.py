"""Export public content of ptdl.com.vn through the WordPress REST API.

The front end returns HTTP 500, but /wp-json still serves published posts, pages
and media. Only public, unauthenticated endpoints are read. TLS verification is on
by default; the site's certificate is currently expired, so the export only works
once it is renewed, or when the user explicitly passes --insecure.
Output goes to backup/live/ (gitignored).
"""
import json
import ssl
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

BASE = "https://ptdl.com.vn/wp-json/wp/v2"
OUT = Path(__file__).resolve().parent.parent / "backup" / "live"
ENDPOINTS = ["posts", "pages", "media", "categories", "tags", "comments"]
CTX = ssl.create_default_context()
if "--insecure" in sys.argv:
    CTX.check_hostname = False
    CTX.verify_mode = ssl.CERT_NONE


def get(url: str) -> tuple[bytes, dict]:
    req = Request(url, headers={"User-Agent": "ptdl-restore/1.0"})
    for attempt in range(1, 4):
        try:
            with urlopen(req, timeout=60, context=CTX) as resp:
                return resp.read(), dict(resp.headers)
        except HTTPError:
            raise
        except (URLError, TimeoutError) as exc:
            print(f"  RETRY {attempt}/3 {url}: {exc}")
            time.sleep(3 * attempt)
    raise RuntimeError(f"giving up on {url}")


def export_endpoint(name: str) -> list:
    items: list = []
    page = 1
    while True:
        url = f"{BASE}/{name}?per_page=100&page={page}"
        try:
            body, headers = get(url)
        except HTTPError as exc:
            print(f"{name}: HTTP {exc.code} (stopping)")
            break
        batch = json.loads(body)
        items.extend(batch)
        pages = int(headers.get("X-WP-TotalPages", headers.get("x-wp-totalpages", "1")))
        print(f"{name}: page {page}/{pages}, {len(batch)} items")
        if page >= pages:
            break
        page += 1
        time.sleep(1)
    return items


def download_media(media: list) -> None:
    folder = OUT / "media"
    for item in media:
        src = item.get("source_url")
        if not src or not item.get("mime_type", "").startswith("image/"):
            continue
        target = folder / urlparse(src).path.lstrip("/").replace("wp-content/uploads/", "")
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            body, _ = get(src)
        except (HTTPError, RuntimeError) as exc:
            print(f"  media FAIL {src}: {exc}")
            continue
        target.write_bytes(body)
        print(f"  media {target.name}")
        time.sleep(0.3)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    skip_media = "--no-media" in sys.argv
    for name in ENDPOINTS:
        items = export_endpoint(name)
        (OUT / f"{name}.json").write_text(
            json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8"
        )
        if name == "media" and not skip_media:
            download_media(items)
    print(f"Done. Saved to {OUT}")


if __name__ == "__main__":
    main()
