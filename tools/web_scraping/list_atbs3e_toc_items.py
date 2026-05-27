#!/usr/bin/env python3
"""
list_atbs3e_toc_items.py

List scraped ATBS 3e table-of-contents items.

Usage:
    python3 tools/web_scraping/list_atbs3e_toc_items.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TOC_JSON = PROJECT_ROOT / "tools" / "web_scraping" / "out" / "atbs3e_toc.json"


def load_toc_items(json_path: Path) -> list[dict[str, Any]]:
    """Load TOC items from a JSON file."""
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    with json_path.open("r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    if not isinstance(data, list):
        raise ValueError("Expected JSON data to be a list.")

    return data


def print_toc_items(items: list[dict[str, Any]]) -> None:
    """Print TOC items in a readable format."""
    for item in items:
        chapter_num = item.get("chapter_num")
        title = item.get("title", "")
        url = item.get("url", "")

        print(f"{chapter_num:>2}. {title}")
        print(f"    {url}")


def main() -> None:
    """Load and print scraped TOC items."""
    items = load_toc_items(TOC_JSON)
    print_toc_items(items)

    print(f"\nTotal items: {len(items)}")


if __name__ == "__main__":
    main()
