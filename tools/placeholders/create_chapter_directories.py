#!/usr/bin/env python3
"""
create_chapter_directories.py

Create chapter directories from a CSV or JSON table-of-contents file.

This script only creates directories. It does not create README.md, USAGE.md,
utils.py, or any other utility files.

Usage:
    python3 tools/placeholders/create_chapter_directories.py
    python3 tools/placeholders/create_chapter_directories.py --dry-run
    python3 tools/placeholders/create_chapter_directories.py --toc-file tools/web_scraping/out/atbs3e_toc.csv
    python3 tools/placeholders/create_chapter_directories.py --chapters-dir chapters
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Final


PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[2]
DEFAULT_TOC_FILE: Final[Path] = (
    PROJECT_ROOT / "tools" / "web_scraping" / "out" / "atbs3e_toc.json"
)
DEFAULT_CHAPTERS_DIR: Final[Path] = PROJECT_ROOT / "chapters"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Create chapter directories from a CSV or JSON TOC file."
    )
    parser.add_argument(
        "--toc-file",
        type=Path,
        default=DEFAULT_TOC_FILE,
        help="CSV or JSON file containing chapter information.",
    )
    parser.add_argument(
        "--chapters-dir",
        type=Path,
        default=DEFAULT_CHAPTERS_DIR,
        help="Directory where chapter directories should be created.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show directories that would be created without creating them.",
    )
    return parser.parse_args()


def load_toc_items(toc_file: Path) -> list[dict[str, Any]]:
    """Load TOC items from a CSV or JSON file."""
    if not toc_file.is_file():
        raise FileNotFoundError(f"TOC file not found: {toc_file}")

    suffix = toc_file.suffix.lower()
    if suffix == ".json":
        data = json.loads(toc_file.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("chapters", data.get("items", []))
        if not isinstance(data, list):
            raise ValueError(f"Expected a list of TOC items in {toc_file}")
        return [item for item in data if isinstance(item, dict)]

    if suffix == ".csv":
        with toc_file.open("r", encoding="utf-8", newline="") as file:
            return list(csv.DictReader(file))

    raise ValueError(f"Unsupported TOC file type: {toc_file.suffix}")


def to_snake_case(text: str) -> str:
    """Convert text to snake_case suitable for directory names."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(
        char for char in normalized if not unicodedata.combining(char)
    )
    ascii_text = ascii_text.replace("&", " and ").replace("-", " ")
    ascii_text = re.sub(r"[^A-Za-z0-9 _]+", " ", ascii_text)
    snake = re.sub(r"\s+", "_", ascii_text).strip("_").lower()
    return re.sub(r"_+", "_", snake)


def extract_chapter_number(item: dict[str, Any]) -> int | None:
    """Extract a numeric chapter number from a TOC item."""
    for key in ("chapter_num", "chapter_number", "number"):
        value = item.get(key)
        if value in (None, ""):
            continue
        try:
            return int(value)
        except (TypeError, ValueError):
            pass

    text = f"{item.get('title', '')} {item.get('url', '')}"
    match = re.search(r"\bchapter[_\s-]*(\d+)\b", text, flags=re.IGNORECASE)
    if match:
        return int(match.group(1))

    match = re.search(r"\bchapter(\d+)\.html\b", text, flags=re.IGNORECASE)
    if match:
        return int(match.group(1))

    return None


def clean_chapter_title(title: str) -> str:
    """Remove leading chapter labels from a title."""
    cleaned = re.sub(
        r"^\s*chapter\s+\d+\s*[-:]\s*",
        "",
        title,
        flags=re.IGNORECASE,
    )
    return cleaned.strip() or title.strip()


def make_chapter_directory_name(item: dict[str, Any]) -> str | None:
    """Build the chapter directory name for one TOC item."""
    chapter_number = extract_chapter_number(item)
    if chapter_number is None:
        return None

    title = str(item.get("title", f"Chapter {chapter_number}"))
    clean_title = clean_chapter_title(title)
    slug = to_snake_case(clean_title)
    return f"chapter_{chapter_number:02d}_{slug}"


def create_chapter_directories(
    toc_items: list[dict[str, Any]],
    chapters_dir: Path,
    dry_run: bool,
) -> None:
    """Create chapter directories from TOC items."""
    if dry_run:
        print(f"Would ensure chapters directory exists: {chapters_dir}")
    else:
        chapters_dir.mkdir(parents=True, exist_ok=True)

    created_count = 0
    skipped_count = 0
    ignored_count = 0

    for item in toc_items:
        directory_name = make_chapter_directory_name(item)
        if directory_name is None:
            ignored_count += 1
            print(f"Ignored item without chapter number: {item.get('title', item)}")
            continue

        chapter_dir = chapters_dir / directory_name
        if chapter_dir.exists():
            skipped_count += 1
            print(f"Skipped existing directory: {chapter_dir}")
            continue

        created_count += 1
        if dry_run:
            print(f"Would create directory: {chapter_dir}")
        else:
            chapter_dir.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {chapter_dir}")

    print(
        "Summary: "
        f"created={created_count}, skipped={skipped_count}, ignored={ignored_count}"
    )


def main() -> None:
    """Run the chapter directory creation script."""
    args = parse_args()
    toc_file = args.toc_file.resolve()
    chapters_dir = args.chapters_dir.resolve()

    toc_items = load_toc_items(toc_file)
    create_chapter_directories(
        toc_items=toc_items,
        chapters_dir=chapters_dir,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
