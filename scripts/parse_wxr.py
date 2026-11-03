"""Split a WordPress WXR export into Elementor data and site configuration.

Reads the first .xml in backup/live/wp-export/ and writes:
  docs/elementor/<slug>.json   Elementor layout data of the genuine pages and templates
  docs/config/*.json|css|html  menus, forms, custom CSS and other site settings

Pages and posts matching the attacker's spam pattern are skipped, and so are
the demo pages that ship with the theme.
"""
import glob
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
}
SPAM = re.compile(r"cox|-htm|htm$|^[0-9a-f]{12}")
DEMO_PAGES = {
    "home-two", "home-three", "blog-grid", "team", "team-single",
    "project-single", "project-masonry", "faq-page", "sample-page",
    "my-account", "track-form-2",
}
LAYOUT_TYPES = {"page", "elementor_library", "transpi_template"}


def item_meta(item: ET.Element) -> dict:
    return {
        m.findtext("wp:meta_key", namespaces=NS): m.findtext("wp:meta_value", namespaces=NS)
        for m in item.findall("wp:postmeta", NS)
    }


def main() -> None:
    export = glob.glob(str(ROOT / "backup" / "live" / "wp-export" / "*.xml"))[0]
    elementor_dir = ROOT / "docs" / "elementor"
    config_dir = ROOT / "docs" / "config"
    elementor_dir.mkdir(parents=True, exist_ok=True)
    config_dir.mkdir(parents=True, exist_ok=True)

    menus: list[dict] = []
    forms: list[dict] = []
    for item in ET.parse(export).getroot().iter("item"):
        kind = item.findtext("wp:post_type", namespaces=NS)
        slug = item.findtext("wp:post_name", namespaces=NS) or ""
        status = item.findtext("wp:status", namespaces=NS)
        title = item.findtext("title") or ""
        body = item.findtext("content:encoded", namespaces=NS) or ""
        meta = item_meta(item)

        if kind in ("page", "post") and (SPAM.search(slug) or slug in DEMO_PAGES):
            continue

        if kind in LAYOUT_TYPES and status == "publish" and meta.get("_elementor_data"):
            data = json.loads(meta["_elementor_data"])
            out = {
                "type": kind,
                "slug": slug,
                "title": title,
                "template": meta.get("_wp_page_template"),
                "elementor_data": data,
                "page_settings": meta.get("_elementor_page_settings"),
            }
            (elementor_dir / f"{kind}-{slug}.json").write_text(
                json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8"
            )
        elif kind == "nav_menu_item" and status == "publish":
            menus.append({
                "title": title,
                "slug": slug,
                "menu_order": item.findtext("wp:menu_order", namespaces=NS),
                "parent": meta.get("_menu_item_menu_item_parent"),
                "type": meta.get("_menu_item_type"),
                "object": meta.get("_menu_item_object"),
                "url": meta.get("_menu_item_url"),
            })
        elif kind == "wpcf7_contact_form":
            forms.append({
                "slug": slug,
                "title": title,
                "form": meta.get("_form"),
                "messages": meta.get("_messages"),
            })
        elif kind == "custom_css":
            (config_dir / f"custom-css-{slug}.css").write_text(body, encoding="utf-8")
        elif kind == "mc4wp-form":
            (config_dir / f"mc4wp-form-{slug}.html").write_text(body, encoding="utf-8")

    (config_dir / "menus.json").write_text(json.dumps(menus, ensure_ascii=False, indent=1), encoding="utf-8")
    (config_dir / "contact-forms.json").write_text(json.dumps(forms, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Elementor files: {len(list(elementor_dir.glob('*.json')))}, menu items: {len(menus)}, forms: {len(forms)}")


if __name__ == "__main__":
    main()
