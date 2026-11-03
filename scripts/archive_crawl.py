"""Crawl the Wayback Machine snapshot of ptdl.com.vn and save raw HTML.

Uses the "id_" form of Wayback URLs so the archived HTML comes back unmodified.
Only same-site links are followed. Output goes to backup/archive/.
"""
import gzip
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

TIMESTAMP = "20250320022357"
SITE = "ptdl.com.vn"
START = f"https://{SITE}/"
OUT = Path(__file__).resolve().parent.parent / "backup" / "archive"
MAX_PAGES = int(sys.argv[1]) if len(sys.argv) > 1 else 300
DELAY = 2.0

HREF_RE = re.compile(r"""href=["']([^"'#]+)["']""", re.IGNORECASE)
IMG_RE = re.compile(r"""src=["'](https?://[^"']+/wp-content/uploads/[^"']+)["']""", re.IGNORECASE)
RETRIES = 3


def wb_url(url: str) -> str:
    return f"https://web.archive.org/web/{TIMESTAMP}id_/{url}"


def fetch(url: str) -> bytes | None:
    req = Request(wb_url(url), headers={"User-Agent": "ptdl-restore/1.0"})
    for attempt in range(1, RETRIES + 1):
        try:
            with urlopen(req, timeout=60) as resp:
                data = resp.read()
            break
        except HTTPError as exc:
            print(f"  FAIL {url}: HTTP {exc.code}")
            return None
        except (URLError, TimeoutError) as exc:
            print(f"  RETRY {attempt}/{RETRIES} {url}: {exc}")
            time.sleep(5 * attempt)
    else:
        return None
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    return data


def local_path(url: str) -> Path:
    parts = urlparse(url)
    path = parts.path.strip("/") or "index"
    if path.endswith("/"):
        path += "index"
    if not Path(path).suffix:
        path += ".html"
    return OUT / parts.netloc / path


def same_site(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return host == SITE or host == f"www.{SITE}"


def main() -> None:
    seen: set[str] = set()
    queue = [START]
    saved = 0

    while queue and saved < MAX_PAGES:
        url = queue.pop(0).split("#")[0]
        if url in seen:
            continue
        seen.add(url)

        body = fetch(url)
        if body is None:
            continue

        target = local_path(url)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)
        saved += 1
        print(f"[{saved}] {url} -> {target.name}")

        if target.suffix == ".html":
            text = body.decode("utf-8", errors="ignore")
            for link in HREF_RE.findall(text):
                absolute = urljoin(url, link)
                if same_site(absolute) and absolute not in seen:
                    queue.append(absolute)
            for image in IMG_RE.findall(text):
                if same_site(image) and image not in seen:
                    queue.append(image)

        time.sleep(DELAY)

    print(f"Done. Saved {saved} files to {OUT}")


if __name__ == "__main__":
    main()
