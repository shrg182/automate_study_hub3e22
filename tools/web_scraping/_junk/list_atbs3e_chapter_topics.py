#!/usr/bin/env python3
"""
list_atbs3e_chapter_topics.py

List scraped ATBS 3e chapter-topic items.

Usage:
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --chapter-number 10 --topic-heading 3
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TOPICS_JSON = (
    PROJECT_ROOT
    / "tools"
    / "web_scraping"
    / "out"
    / "atbs3e_chapter_topics.json"
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="List chapters and topics from CSV or JSON files."
    )
    parser.add_argument(
        "--toc-file",
        type=Path,
        default=TOPICS_JSON,
        help="CSV or JSON containing chapter information."
    )
    parser.add_argument(
        "--chapter-number",
        type=int,
        default=None,
        help="Chapter number to list the information of this chapter."
    )
    parser.add_argument(
        "--topic-heading",
        type=int,
        default=None,
        help="Topic levels from heading lever 2 to 6."
    )

    return parser.parse_args()


def load_topic_items(json_path: Path) -> list[dict[str, Any]]:
    """Load chapter-topic items from a JSON file."""
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    with json_path.open("r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    if not isinstance(data, list):
        raise ValueError("Expected JSON data to be a list.")

    return data


def print_topic_items(items: list[dict[str, Any]], chapter_number: int, topic_heading: int) -> None:
    """Print chapter-topic items in a readable format."""
    current_chapter = None

    for item in items:
        chapter_num = item.get("chapter_num")
        if chapter_num == chapter_number:

            chapter_title = item.get("chapter_title", "")
            heading_level = item.get("heading_level", "")
            title = item.get("title", "")
            url = item.get("url", "")

            if chapter_num != current_chapter:
                current_chapter = chapter_num
                print()
                print(f"Chapter {chapter_num}: {chapter_title}")
                print("-" * 60)

            if topic_heading and heading_level == topic_heading:
                print(f"  H{heading_level} - {title}")
                print(f"      {url}")

    print(f"\nTotal topic items: {len(items)}")


def main() -> None:
    """Load and print scraped chapter-topic items."""
    args = parse_args()
    chapter_number = args.chapter_number
    topic_heading = args.topic_heading
    items = load_topic_items(TOPICS_JSON)
    print_topic_items(items, chapter_number, topic_heading)


if __name__ == "__main__":
    main()
