#!/usr/bin/env python3
"""
show_atbs3e_chapter_topic_stats.py

Show statistics for scraped ATBS 3e chapter-topic items.

Usage:
    python3 tools/web_scraping/show_atbs3e_chapter_topic_stats.py
    python3 tools/web_scraping/show_atbs3e_chapter_topic_stats.py --chapter-number 10
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TOPICS_JSON = (
    PROJECT_ROOT
    / "tools"
    / "web_scraping"
    / "out"
    / "atbs3e_chapter_topics.json"
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Show statistics for scraped ATBS 3e chapter topics."
    )

    parser.add_argument(
        "--topics-file",
        type=Path,
        default=DEFAULT_TOPICS_JSON,
        help=f"Path to chapter topics JSON file. Default: {DEFAULT_TOPICS_JSON}",
    )

    parser.add_argument(
        "--chapter-number",
        type=int,
        default=None,
        help="Only show statistics for this chapter number.",
    )

    return parser.parse_args()


def load_topic_items(json_path: Path) -> list[dict[str, Any]]:
    """Load chapter-topic items from a JSON file."""
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    with json_path.open("r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    if not isinstance(data, list):
        raise ValueError("Expected JSON data to be a list of topic items.")

    return data


def filter_by_chapter(
    items: list[dict[str, Any]],
    chapter_number: int | None,
) -> list[dict[str, Any]]:
    """Return items for one chapter, or all items if no chapter is selected."""
    if chapter_number is None:
        return items

    return [
        item
        for item in items
        if item.get("chapter_num") == chapter_number
    ]


def get_chapter_title(item: dict[str, Any]) -> str:
    """Return a safe chapter title."""
    title = item.get("chapter_title", "Untitled Chapter")
    return str(title)


def print_heading_level_stats(items: list[dict[str, Any]]) -> None:
    """Print topic counts by heading level."""
    heading_counts: Counter[int] = Counter()

    for item in items:
        heading_level = item.get("heading_level")
        if isinstance(heading_level, int):
            heading_counts[heading_level] += 1

    print("Heading Level Statistics")
    print("=" * 72)

    for heading_level in sorted(heading_counts):
        print(f"H{heading_level}: {heading_counts[heading_level]}")

    print()


def print_chapter_stats(items: list[dict[str, Any]]) -> None:
    """Print topic counts by chapter."""
    chapter_counts: dict[int, int] = defaultdict(int)
    chapter_titles: dict[int, str] = {}

    for item in items:
        chapter_num = item.get("chapter_num")
        if not isinstance(chapter_num, int):
            continue

        chapter_counts[chapter_num] += 1
        chapter_titles[chapter_num] = get_chapter_title(item)

    print("Chapter Statistics")
    print("=" * 72)

    for chapter_num in sorted(chapter_counts):
        title = chapter_titles.get(chapter_num, "Untitled Chapter")
        count = chapter_counts[chapter_num]
        print(f"Chapter {chapter_num:>2}: {count:>3} topics  |  {title}")

    print()


def print_summary_stats(items: list[dict[str, Any]]) -> None:
    """Print overall summary statistics."""
    chapter_numbers = {
        item.get("chapter_num")
        for item in items
        if isinstance(item.get("chapter_num"), int)
    }

    heading_levels = [
        item.get("heading_level")
        for item in items
        if isinstance(item.get("heading_level"), int)
    ]

    print("Summary")
    print("=" * 72)
    print(f"Total topic items: {len(items)}")
    print(f"Chapters included: {len(chapter_numbers)}")

    if heading_levels:
        print(f"Smallest heading level: H{min(heading_levels)}")
        print(f"Largest heading level:  H{max(heading_levels)}")

    print()


def main() -> None:
    """Load topic items and print statistics."""
    args = parse_args()

    try:
        all_items = load_topic_items(args.topics_file)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}")
        raise SystemExit(1) from exc

    items = filter_by_chapter(
        items=all_items,
        chapter_number=args.chapter_number,
    )

    if not items:
        print("No matching topic items found.")
        raise SystemExit(0)

    print_summary_stats(items)
    print_heading_level_stats(items)
    print_chapter_stats(items)


if __name__ == "__main__":
    main()
