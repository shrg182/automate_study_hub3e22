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
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --stats
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --stats --color
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --export-txt
    python3 tools/web_scraping/list_atbs3e_chapter_topics.py --chapter-number 10 --color
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from directory_tree import print_tree
from show_atbs3e_chapter_topic_stats import print_chapter_stats, print_summary_stats
from export_atbs3e_chapter_topics_txt import (
    DEFAULT_OUTPUT_TXT,
    build_text_output,
    export_text_file,
    filter_topic_items,
    load_topic_items,
)
from export_atbs3e_chapter_topics_md import (
    DEFAULT_OUTPUT_MD,
    build_markdown_output,
    export_markdown_file,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TOPICS_JSON = (
    PROJECT_ROOT
    / "tools"
    / "web_scraping"
    / "out"
    / "atbs3e_chapter_topics.json"
)

DEFAULT_TREE_ROOT = PROJECT_ROOT / "chapters"

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"

HEADING_COLORS = {
    2: GREEN,
    3: BLUE,
    4: YELLOW,
    5: MAGENTA,
    6: DIM,
}


def color_text(text: str, color_code: str, use_color: bool) -> str:
    """Return colored text when color output is enabled."""
    if not use_color or not color_code:
        return text

    return f"{color_code}{text}{RESET}"


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

    parser.add_argument(  # tree view
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

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show topic statistics by chapter.",
    )

    parser.add_argument(
        "--export-txt",
        action="store_true",
        help="Export the topic listing to a TXT file.",
    )

    parser.add_argument(
        "--output-file",
        type=Path,
        default=DEFAULT_OUTPUT_TXT,
        help=f"Output text file path. Default: {DEFAULT_OUTPUT_TXT}",
    )

    parser.add_argument(
        "--export-md",
        action="store_true",
        help="Export the topic listing to a Markdown file.",
    )

    parser.add_argument(
        "--output-markdown",
        type=Path,
        default=DEFAULT_OUTPUT_MD,
        help=f"Output markdown file path. Default: {DEFAULT_OUTPUT_MD}"
    )

    parser.add_argument(
        "--color",
        action="store_true",
        help="Use colored terminal output.",
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
    use_color: bool,
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
            chapter_line = f"Chapter {chapter_num}: {chapter_title}"

            print()
            print(color_text(chapter_line, BOLD + CYAN, use_color))
            print(color_text("=" * 72, CYAN, use_color))

        indent = "  " * max(0, heading_level - 2)
        heading_color = HEADING_COLORS.get(heading_level, "")

        heading_label = color_text(
            f"H{heading_level}",
            heading_color,
            use_color,
        )
        topic_title = color_text(title, heading_color, use_color)

        print(f"{indent}* {heading_label} {topic_title}")

        if show_url and url:
            print(f"{indent}  {color_text(url, DIM, use_color)}")


def run_tree_view(tree_root: Path) -> None:
    """Print the chapters directory tree."""
    if not tree_root.exists():
        raise FileNotFoundError(f"Tree root not found: {tree_root}")

    if not tree_root.is_dir():
        raise NotADirectoryError(f"Tree root is not a directory: {tree_root}")

    print_tree(tree_root)


def run_export_txt(
    topics_file: Path,
    output_path: Path,
    chapter_number: int | None,
    topic_heading: int | None,
    show_url: bool,
) -> None:
    """Export chapter-topic items to a plain text file."""
    items = load_topic_items(topics_file)

    filtered_items = filter_topic_items(
        items=items,
        chapter_number=chapter_number,
        max_heading_level=topic_heading,
    )

    output_text = build_text_output(
        items=filtered_items,
        show_url=show_url,
    )

    export_text_file(
        content=output_text,
        output_path=output_path,
    )

    print(f"Exported {len(filtered_items)} topic items.")
    print(f"TXT: {output_path.resolve()}")


def run_export_md(
    topics_file: Path,
    output_path: Path,
    chapter_number: int | None,
    topic_heading: int | None,
    show_url: bool,
) -> None:
    """Export chapter-topic items to a plain text file."""
    items = load_topic_items(topics_file)

    filtered_items = filter_topic_items(
        items=items,
        chapter_number=chapter_number,
        max_heading_level=topic_heading,
    )

    output_text = build_markdown_output(
        items=filtered_items,
        show_url=show_url,
    )

    export_text_file(
        content=output_text,
        output_path=output_path,
    )

    print(f"Exported {len(filtered_items)} topic items.")
    print(f"TXT: {output_path.resolve()}")


def main() -> None:
    """Run the chapter-topic lister."""
    args = parse_args()

    try:
        if args.tree_view:
            run_tree_view(args.tree_root)
            return

        if args.export_txt:
            run_export_txt(
                topics_file=args.topics_file,
                output_path=args.output_file,
                chapter_number=args.chapter_number,
                topic_heading=args.topic_heading,
                show_url=args.show_url,
            )
            return

        if args.export_md:
            run_export_md(
                topics_file=args.topics_file,
                output_path=args.output_markdown,
                chapter_number=args.chapter_number,
                topic_heading=args.topic_heading,
                show_url=args.show_url,
            )
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
            use_color=args.color,
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
