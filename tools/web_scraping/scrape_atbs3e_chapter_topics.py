#!/usr/bin/env python3
"""
scrape_atbs3e_chapter_topics.py

Scrape subtitle headings from each ATBS 3e chapter page.

Output:
    tools/scrape/atbs3e_chapter_topics.csv
    tools/scrape/atbs3e_chapter_topics.json
"""

from __future__ import annotations

import csv
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag

CHAPTER_URL_TEMPLATE = "https://automatetheboringstuff.com/3e/chapter{num}.html"
CHAPTER_RANGE = range(25)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "tools" / "web_scraping" / "out"

CSV_OUTPUT = OUTPUT_DIR / "atbs3e_chapter_topics.csv"
JSON_OUTPUT = OUTPUT_DIR / "atbs3e_chapter_topics.json"

HEADING_TAGS = ("h2", "h3", "h4", "h5", "h6")


@dataclass(frozen=True)
class TopicItem:
    """One scraped chapter topic."""

    chapter_num: int
    chapter_title: str
    heading_level: int
    title: str
    url: str


def clean_text(text: str) -> str:
    """Normalize whitespace in scraped text."""
    return re.sub(r"\s+", " ", text).strip()


def fetch_html(url: str) -> str:
    """Fetch HTML from a webpage."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 scraping script for Python study; "
            "contact: local"
        )
    }
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.text


def get_chapter_title(soup: BeautifulSoup) -> str:
    """Return the chapter title from the first h1 or h2 heading."""
    heading = soup.find(["h1", "h2"])
    if not isinstance(heading, Tag):
        return ""

    return clean_text(heading.get_text(" ", strip=True))


def make_heading_url(base_url: str, heading: Tag) -> str:
    """Build a URL for a heading, including its id anchor if available."""
    heading_id = heading.get("id")
    if isinstance(heading_id, str) and heading_id.strip():
        return urljoin(base_url, f"#{heading_id.strip()}")

    return base_url


def parse_topics(
    html: str,
    base_url: str,
    chapter_num: int,
) -> list[TopicItem]:
    """Parse subtitle headings from one chapter page."""
    soup = BeautifulSoup(html, "html.parser")
    chapter_title = get_chapter_title(soup)

    topics: list[TopicItem] = []

    for heading in soup.find_all(HEADING_TAGS):
        if not isinstance(heading, Tag):
            continue

        title = clean_text(heading.get_text(" ", strip=True))
        if not title:
            continue

        heading_level = int(heading.name[1])

        topics.append(
            TopicItem(
                chapter_num=chapter_num,
                chapter_title=chapter_title,
                heading_level=heading_level,
                title=title,
                url=make_heading_url(base_url, heading),
            )
        )

    return topics


def save_to_csv(items: list[TopicItem], output_path: Path) -> None:
    """Save topic items to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        fieldnames = [
            "chapter_num",
            "chapter_title",
            "heading_level",
            "title",
            "url",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for item in items:
            writer.writerow(asdict(item))


def save_to_json(items: list[TopicItem], output_path: Path) -> None:
    """Save topic items to JSON."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as json_file:
        json.dump(
            [asdict(item) for item in items],
            json_file,
            indent=2,
            ensure_ascii=False,
        )


def main() -> None:
    """Scrape all chapter topics and save them."""
    all_topics: list[TopicItem] = []

    for chapter_num in CHAPTER_RANGE:
        chapter_url = CHAPTER_URL_TEMPLATE.format(num=chapter_num)
        print(f"Fetching chapter {chapter_num}: {chapter_url}")

        try:
            html = fetch_html(chapter_url)
            topics = parse_topics(html, chapter_url, chapter_num)
        except requests.RequestException as exc:
            print(f"[ERROR] Could not fetch chapter {chapter_num}: {exc}")
            continue

        print(f"  Found {len(topics)} topics.")
        all_topics.extend(topics)

    save_to_csv(all_topics, CSV_OUTPUT)
    save_to_json(all_topics, JSON_OUTPUT)

    print(f"\nSaved {len(all_topics)} topics.")
    print(f"CSV:  {CSV_OUTPUT.resolve()}")
    print(f"JSON: {JSON_OUTPUT.resolve()}")


if __name__ == "__main__":
    main()
