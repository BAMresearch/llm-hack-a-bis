"""Build a static page, or preview it locally with rebuilds on refresh."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path
import shutil
import re

import markdown

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "dist"


def build():
    source = (ROOT / "content/index.md").read_text(encoding="utf-8")
    source = source.replace(
        "<!-- include tutorial -->",
        (ROOT / "content/tutorial.md").read_text(encoding="utf-8"),
    )
    content = markdown.markdown(
        source,
        extensions=["fenced_code", "tables", "toc", "attr_list"],
    )
    # Markdown stays editable; sections get consistent responsive wrappers.
    parts = re.split(r'(<h2\b[^>]*>.*?</h2>)', content, flags=re.DOTALL)
    hero = (
        '<section class="hero"><div class="hero-copy">'
        '<div class="eyebrow">BAM · openBIS · 12.11.2026</div>'
        + parts[0] + '</div><div class="hero-art" aria-hidden="true">'
        '<span class="data-node">{ }</span><span class="model-node">✳</span>'
        '<span class="art-caption">Learn → connect → build</span></div></section>'
    )
    sections = []
    for number, index in enumerate(range(1, len(parts), 2), start=1):
        sections.append(
            '<section class="content-section"><div class="section-heading">'
            f'<span class="eyebrow">{number:02d} / HACK A BIS</span>'
            + parts[index] + '</div><div class="section-body">'
            + parts[index + 1] + '</div></section>'
        )
    content = hero + ''.join(sections)
    template = (ROOT / "templates/index.html").read_text(encoding="utf-8")
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / "index.html").write_text(
        template.replace("{{ content }}", content), encoding="utf-8"
    )
    shutil.copytree(ROOT / "assets", OUTPUT / "assets", dirs_exist_ok=True)
    (OUTPUT / ".nojekyll").touch()


class PreviewHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?", 1)[0] in ("/", "/index.html"):
            build()
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serve", action="store_true", help="Rebuild on browser refresh")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    build()
    print(f"Built {OUTPUT / 'index.html'}", flush=True)
    if args.serve:
        handler = partial(PreviewHandler, directory=str(OUTPUT))
        with HTTPServer(("127.0.0.1", args.port), handler) as server:
            print(f"Preview: http://localhost:{args.port} (Ctrl+C to stop)", flush=True)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass


if __name__ == "__main__":
    main()
