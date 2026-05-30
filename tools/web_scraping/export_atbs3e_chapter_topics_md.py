#!/usr/bin/env python3
"""
export_atbs3e_chapter_topics_md.py

Export scraped ATBS 3e chapter-topic items to a Markdown file.

Usage:
    python3 tools/web_scraping/export_atbs3e_chapter_topics_md.py
    python3 tools/web_scraping/export_atbs3e_chapter_topics_md.py --chapter-number 10
    python3 tools/web_scraping/export_atbs3e_chapter_topics_md.py --chapter-number 10 --topic-heading 4
    python3 tools/web_scraping/export_atbs3e_chapter_topics_md.py --chapter-number 10 --topic-heading 4 --show-url
"""

from __future__ import annotations

import argparse
import json
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

DEFAULT_OUTPUT_MD = (
    PROJECT_ROOT
    / "tools"
    / "web_scraping"
    / "out"
    / "atbs3e_chapter_topics_list.md"
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Export scraped ATBS 3e chapter topics to a Markdown file."
    )

    parser.add_argument(
        "--topics-file",
        type=Path,
        default=DEFAULT_TOPICS_JSON,
        help=f"Path to chapter topics JSON file. Default: {DEFAULT_TOPICS_JSON}",
    )

    parser.add_argument(
        "--output-file",
        type=Path,
        default=DEFAULT_OUTPUT_MD,
        help=f"Output Markdown file path. Default: {DEFAULT_OUTPUT_MD}",
    )

    parser.add_argument(
        "--chapter-number",
        type=int,
        default=None,
        help="Only export topics from this chapter number.",
    )

    parser.add_argument(
        "--topic-heading",
        type=int,
        choices=range(2, 7),
        metavar="{2,3,4,5,6}",
        default=None,
        help="Export topics up to this heading level. Example: 4 exports H2, H3, and H4.",
    )

    parser.add_argument(
        "--show-url",
        action="store_true",
        help="Include topic URLs as Markdown links.",
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

    return filtered_items


def build_markdown_output(
    items: list[dict[str, Any]],
    show_url: bool,
) -> str:
    """Build formatted Markdown output from topic items."""
    if not items:
        return "# ATBS 3e Chapter Topics\n\nNo matching topic items found.\n"

    lines: list[str] = ["# ATBS 3e Chapter Topics", ""]
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
            lines.append("")
            lines.append(f"## Chapter {chapter_num}: {chapter_title}")
            lines.append("")

        indent = "  " * max(0, heading_level - 2)

        if show_url and url:
            lines.append(f"{indent}- [{title}]({url})")
        else:
            lines.append(f"{indent}- {title}")

    lines.append("")
    lines.append(f"**Displayed topic items:** {len(items)}")
    lines.append("")

    return "\n".join(lines)


def export_markdown_file(
    content: str,
    output_path: Path,
) -> None:
    """Write Markdown content to a file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")


def main() -> None:
    """Export filtered chapter-topic items to a Markdown file."""
    args = parse_args()

    try:
        items = load_topic_items(args.topics_file)

        filtered_items = filter_topic_items(
            items=items,
            chapter_number=args.chapter_number,
            max_heading_level=args.topic_heading,
        )

        output_markdown = build_markdown_output(
            items=filtered_items,
            show_url=args.show_url,
        )

        export_markdown_file(
            content=output_markdown,
            output_path=args.output_file,
        )

    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}")
        raise SystemExit(1) from exc

    print(f"Exported {len(filtered_items)} topic items.")
    print(f"MD: {args.output_file.resolve()}")


if __name__ == "__main__":
    main()
