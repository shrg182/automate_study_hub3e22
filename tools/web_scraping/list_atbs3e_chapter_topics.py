#!/usr/bin/env python3
"""
list_atbs3e_chapter_topics.py

List scraped ATBS 3e chapter-topic items or print the chapters tree.

Usage:
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --chapter-number 10
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --topic-heading 3
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --chapter-number 10 --topic-heading 4
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --chapter-number 10 --topic-heading 4 --show-url
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --tree-view
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from directory_tree import print_tree

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TOPICS_JSON = (
    PROJECT_ROOT
    / "tools"
    / "web_scraping"
    / "out"
    / "atbs3e_chapter_topics.json"
)
DEFAULT_TREE_ROOT = PROJECT_ROOT / "chapters"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="List scraped ATBS 3e chapter topics."
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
        help="Only show topics from this chapter number.",
    )

    parser.add_argument(
        "--topic-heading",
        type=int,
        choices=range(2, 7),
        metavar="{2,3,4,5,6}",
        default=None,
        help="Show topics up to this heading level. Example: 4 shows H2, H3, and H4.",
    )

    parser.add_argument(
        "--show-url",
        action="store_true",
        help="Show topic URLs in the listing.",
    )

    parser.add_argument(
        "--tree-view",
        action="store_true",
        help="Print the chapters directory tree instead of listing topics.",
    )

    parser.add_argument(
        "--tree-root",
        type=Path,
        default=DEFAULT_TREE_ROOT,
        help=f"Directory root for --tree-view. Default: {DEFAULT_TREE_ROOT}",
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


def filter_topic_items(
    items: list[dict[str, Any]],
    chapter_number: int | None,
    max_heading_level: int | None,
) -> list[dict[str, Any]]:
    """Filter topic items by chapter number and maximum heading level."""
    filtered_items: list[dict[str, Any]] = []

    for item in items:
        item_chapter_num = item.get("chapter_num")
        item_heading_level = item.get("heading_level")

        if chapter_number is not None and item_chapter_num != chapter_number:
            continue

        if max_heading_level is not None:
            if not isinstance(item_heading_level, int):
                continue

            if item_heading_level > max_heading_level:
                continue

        filtered_items.append(item)

    return sorted(
        filtered_items,
        key=lambda item: (
            item.get("chapter_num", 999),
            item.get("heading_level", 999),
            item.get("title", ""),
        ),
    )


def print_topic_items(
    items: list[dict[str, Any]],
    show_url: bool,
) -> None:
    """Print chapter-topic items in a readable format."""
    if not items:
        print("No matching topic items found.")
        return

    current_chapter: int | None = None

    for item in items:
        chapter_num = item.get("chapter_num")
        chapter_title = item.get("chapter_title", "Untitled Chapter")
        heading_level = item.get("heading_level")
        title = item.get("title", "Untitled Topic")
        url = item.get("url", "")

        if not isinstance(heading_level, int):
            continue

        if chapter_num != current_chapter:
            current_chapter = chapter_num
            print()
            print(f"Chapter {chapter_num}: {chapter_title}")
            print("=" * 72)

        indent = "  " * max(0, heading_level - 2)
        print(f"{indent}* H{heading_level} {title}")

        if show_url and url:
            print(f"{indent}  {url}")


def run_tree_view(tree_root: Path) -> None:
    """Print the chapters directory tree."""
    if not tree_root.exists():
        raise FileNotFoundError(f"Tree root not found: {tree_root}")

    if not tree_root.is_dir():
        raise NotADirectoryError(f"Tree root is not a directory: {tree_root}")

    print_tree(tree_root)


def main() -> None:
    """Run the chapter-topic lister."""
    args = parse_args()

    try:
        if args.tree_view:
            run_tree_view(args.tree_root)
            return

        items = load_topic_items(args.topics_file)

        filtered_items = filter_topic_items(
            items=items,
            chapter_number=args.chapter_number,
            max_heading_level=args.topic_heading,
        )

        print_topic_items(
            items=filtered_items,
            show_url=args.show_url,
        )

        print()
        print(f"Displayed topic items: {len(filtered_items)}")
        print(f"Total topic items in file: {len(items)}")

    except (
        FileNotFoundError,
        NotADirectoryError,
        ValueError,
        json.JSONDecodeError,
    ) as exc:
        print(f"Error: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
