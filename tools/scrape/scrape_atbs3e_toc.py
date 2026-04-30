#!/usr/bin/env python3
"""
scrapee_atbs3e_toc.py

scrapee the table of contents from the ATBS3e website and save it to a file.

This script uses BeautifulSoup to parse the HTML content of the ATBS3e website and extract the table of contents. The extracted data is then saved to a text file for further use.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

BASE_URL = "https://automatetheboringstuff.com/3e/"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "tools" / "scrape" / "out"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CSV_OUTPUT = OUTPUT_DIR / "atbs3e_toc.csv"
JSON_OUTPUT = OUTPUT_DIR / "atbs3e_toc.json"


@dataclass(frozen=True)
class TocItem:
    """One table-of-contents item."""

    title: str
    url: str


def fetch_html(url: str) -> str:
    """Fetch the HTML content of a webpage."""
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.text


def find_toc_heading(soup: BeautifulSoup) -> Tag | None:
    """Find the heading that contains the table of contents."""
    heading = soup.find(
        lambda tag: tag.name in ["h1", "h2", "h3", "h4", "h5", "h6"] 
        and "Table of Contents" in tag.text
    )

    if not isinstance(heading, Tag):
        raise ValueError("Could not find the table of contents heading.")
    
    return heading


def parse_toc(html: str, base_url: str) -> list[TocItem]:
    """Parse the table of contents from the HTML content."""
    soup = BeautifulSoup(html, "html.parser")
    toc_heading = find_toc_heading(soup)

    toc_list = toc_heading.find_next("ul")
    if not isinstance(toc_list, Tag):
        raise ValueError("Could not find the table of contents list.")
    
    toc_items: list[TocItem] = []

    for link in toc_list.find_all("a", href=True):
        title = link.get_text(" ", strip=True)
        href = str(link["href"])
        full_url = urljoin(base_url, href)

        toc_items.append(TocItem(title=title, url=full_url))

    return toc_items


def save_csv(items: list[TocItem], output_path: Path) -> None:
    """Save the table of contents items to a CSV file."""
    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["title", "url"])
        writer.writeheader()

        for item in items:
            writer.writerow(asdict(item))

    
def save_json(items: list[TocItem], output_path: Path) -> None:
    """Save the table of contents items to a JSON file."""
    data = [asdict(item) for item in items]

    with output_path.open("w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=2)


def main() -> None:
    """Run the scrapeing process."""
    html = fetch_html(BASE_URL)
    toc_items = parse_toc(html, BASE_URL)

    save_csv(toc_items, CSV_OUTPUT)
    save_json(toc_items, JSON_OUTPUT)

    print(f"Saved {len(toc_items)} items to {CSV_OUTPUT} and {JSON_OUTPUT}.")
    print(f"CSV: {CSV_OUTPUT.resolve()}")
    print(f"JSON: {JSON_OUTPUT.resolve()}")


if __name__ == "__main__":
    main()