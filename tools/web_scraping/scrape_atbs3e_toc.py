#!/usr/bin/env python3
"""
scrape_atbs3e_toc.py

Scrape the Automate the Boring Stuff with Python, 3rd Edition
table of contents.

Output:
    tools/web_scraping/out/atbs3e_toc.csv
    tools/web_scraping/out/atbs3e_toc.json
"""

from __future__ import annotations

import csv
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup, Tag

BASE_URL = "https://automatetheboringstuff.com/3e/"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "tools" / "web_scraping" / "out"

CSV_OUTPUT = OUTPUT_DIR / "atbs3e_toc.csv"
JSON_OUTPUT = OUTPUT_DIR / "atbs3e_toc.json"


@dataclass(frozen=True)
class TocItem:
    """One table-of-contents item."""

    chapter_num: int
    title: str
    url: str


def clean_text(text: str) -> str:
    """Normalize whitespace."""
    return re.sub(r"\s+", " ", text).strip()


def fetch_html(url: str) -> str:
    """Fetch HTML from a webpage."""
    headers = {
        "User-Agent": "Mozilla/5.0 Python study scraping script"
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    return response.text


def extract_chapter_num(url: str) -> int | None:
    """Extract chapter number from a chapter URL."""
    parsed_url = urlparse(url)
    filename = Path(parsed_url.path).name

    match = re.fullmatch(r"chapter(\d+)\.html", filename)
    if not match:
        return None

    return int(match.group(1))


def parse_toc(html: str, base_url: str) -> list[TocItem]:
    """Parse TOC links from the ATBS 3e homepage."""
    soup = BeautifulSoup(html, "html.parser")
    items: list[TocItem] = []

    for a_tag in soup.find_all("a"):
        if not isinstance(a_tag, Tag):
            continue

        href = a_tag.get("href")
        if not isinstance(href, str):
            continue

        title = clean_text(a_tag.get_text(" ", strip=True))
        if not title:
            continue

        full_url = urljoin(base_url, href.strip())
        chapter_num = extract_chapter_num(full_url)

        if chapter_num is None:
            continue

        items.append(
            TocItem(
                chapter_num=chapter_num,
                title=title,
                url=full_url,
            )
        )

    items.sort(key=lambda item: item.chapter_num)

    return items


def save_to_csv(items: list[TocItem], output_path: Path) -> None:
    """Save TOC items to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["chapter_num", "title", "url"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for item in items:
            writer.writerow(asdict(item))


def save_to_json(items: list[TocItem], output_path: Path) -> None:
    """Save TOC items to JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as json_file:
        json.dump(
            [asdict(item) for item in items],
            json_file,
            indent=2,
            ensure_ascii=False,
        )


def main() -> None:
    """Scrape the ATBS 3e table of contents."""
    print(f"Fetching: {BASE_URL}")

    html = fetch_html(BASE_URL)
    toc_items = parse_toc(html, BASE_URL)

    save_to_csv(toc_items, CSV_OUTPUT)
    save_to_json(toc_items, JSON_OUTPUT)

    print(f"Saved {len(toc_items)} TOC items.")
    print(f"CSV:  {CSV_OUTPUT.resolve()}")
    print(f"JSON: {JSON_OUTPUT.resolve()}")


if __name__ == "__main__":
    main()
