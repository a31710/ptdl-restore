"""Tiny local server that reproduces the WordPress-style URLs of ptdl.com.vn.

Run:  python serve.py [port]      (default port 8080, then open http://localhost:8080)

  /gioi-thieu            -> gioi-thieu.html
  /services/chuyen-hang-bac-nam -> services/chuyen-hang-bac-nam.html
  /<slug>.htm            -> <slug>.htm
  /gioi-thieu/           -> 301 to /gioi-thieu (WordPress redirects the same way)
  anything else          -> 404.html with a real 404 status
"""
import mimetypes
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
ALIASES = {"/home": "/", "/track-form": "/tracking"}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def resolve(self, path: str):
        """Return (file, status, redirect_to)."""
        path = ALIASES.get(path, path)
        if path == "/":
            return ROOT / "index.html", 200, None
        if path.endswith("/"):
            return None, 301, path.rstrip("/")
        rel = path.lstrip("/")
        target = (ROOT / rel).resolve()
        if ROOT not in target.parents and target != ROOT:
            return ROOT / "404.html", 404, None
        if target.is_file():
            return target, 200, None
        page = target.with_name(target.name + ".html")
        if page.is_file():
            return page, 200, None
        return ROOT / "404.html", 404, None

    def respond(self, send_body: bool):
        parts = urlsplit(self.path)
        file, status, redirect = self.resolve(unquote(parts.path))
        if redirect is not None:
            self.send_response(301)
            self.send_header("Location", redirect + (("?" + parts.query) if parts.query else ""))
            self.end_headers()
            return
        data = file.read_bytes()
        ctype = mimetypes.guess_type(file.name)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype in ("application/xml", "application/javascript"):
            ctype += "; charset=utf-8"
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        if send_body:
            self.wfile.write(data)

    def do_GET(self):
        self.respond(True)

    def do_HEAD(self):
        self.respond(False)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    # ASCII only: the Windows console code page (cp1258, cp1252...) cannot print Vietnamese diacritics.
    print(f"PTDL preview: http://localhost:{port}   (link list: http://localhost:{port}/_links)")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
