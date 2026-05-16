#!/usr/bin/env python3
"""
populate_utility_files_in_chapter_directory.py

Populate utility files in chapter directories for an ATBS-style book project.

Expected chapter directory names:
    chapter_01_python_basics
    chapter_02_if_else_and_flow_control
    ...

Default behavior:
- Reads TOC from: tools/web_scraping/out/atbs3e_toc.json
- Create utility files in matching chapter directories.
- Does not overwrite existing files unless --override flag is used.

Usage:
    python3 populate_utility_files_in_chapter_directory.py
    python3 populate_utility_files_in_chapter_directory.py 
        --toc-file tools/web_scraping/out/atbs3e_toc.json 
        --chapters-dir chapters

    python3 populate_utility_files_in_chapter_directory.py --dry-run

    python3 populate_utility_files_in_chapter_directory.py --override
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import unicodedata
from pathlib import Path
from typing import Any


DEFAULT_UTITLITY_FILES: dict[str, str] = {
    "README.md": "# {title}\n\nThis directory contains utility files for {title}.\n\nReview and utility notes for **{title}**.\n",
    "USAGE.md": "# Usage Instructions for {title}\n\nThis file provides usage instructions for the utilities: {title}\n\nAnd command examples here.\n",
    "utils.py": '''#!/usr/bin/env python3
"""
utils.py

Utility helpers for {title}.
"""

''',
}


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Populate utility files in chapter directories for an ATBS-style book project."
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path.cwd(),
        help="Base directory to search for chapter directories (default: current working directory)"
    )
    parser.add_argument(
        "--toc-file",
        type=Path,
        default=None,
        help=(
            "Path to the JSON file containing the table of contents (default: tools/web_scraping/out/atbs3e_toc.json)"
            "<based-dir>/tools/web_scraping/out/atbs3e_toc.json"
        )
    )
    parser.add_argument(
        "--chapters-dir",
        type=Path,
        default=None,
        help=(
            "Directory containing chapter subdirectories (default: <base-dir>/chpaters)"
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without creating any files"
    )
    parser.add_argument(
        "--override",
        action="store_true",
        help="Override existing files if they already exist"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    return parser.parse_args()


def to_snake_case(text: str) -> str:
    """Convert a string to snake_case."""
    normalized = unicodedata.normalize('NFKD', text)
    ascii_only = "".join(
        ch for ch in normalized if not unicodedata.combining(ch)
    )
    ascii_only = ascii_only.replace("&", "and").replace("-", " ")
    ascii_only = re.sub(r'[^A-Za-z0-9 _]+', '', ascii_only)
    snake = re.sub(r'\s+', '_', ascii_only).lower()
    return re.sub(r"_+", "_", snake)


def load_json(path: Path) -> Any:
    """Load JSON data from a file."""
    try:
        with path.open('r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error loading JSON from '{path}': {e}")
        return None


def extract_chapter_items(toc_data: Any) -> list[dict[str, str]]:
    """Extract chapter items from the TOC data.

    Supports:
      {
        "title": "Introduction",
        "url": "https://automatetheboringstuff.com/3e/chapter0.html"
        },

    Args:
        toc_data (Any): The loaded TOC data.


    Returns:
        list[dict[str, str]]: A list of chapter items with 'title' and 'url'.
    """
    if isinstance(toc_data, dict):
        raw_items = toc_data.get("chapters", [])
    elif isinstance(toc_data, list):
        raw_items = toc_data
    else:
        logging.error(
            "Unexpected TOC data format: expected dict with 'chapters' or list of items.")
        return []

    chapter_items: list[dict[str, Any]] = []

    for item in raw_items:
        if not isinstance(item, dict):
            logging.warning(f"Skipping non-dict item in TOC: {item}")
            continue

        chapter_label = str(item.get("chapter", "")).split()
        title = str(item.get("title", "")).strip()
        url = str(item.get("url", "")).strip()

        if not chapter_label.lower().startswith("chapter"):
            logging.warning(f"Skipping item without 'chapter' label: {item}")
            continue

        match = re.search(r'(\d+)', chapter_label)
        if not match:
            logging.warning(
                f"Skipping item with invalid chapter label: {item}")
            continue

        number = int(match.group(1))
        slug = to_snake_case(title)
        dirname = f"chapter_{number:02d}" + (f"_{slug}" if slug else "")

        chapter_items.append(
            {
                "number": number,
                "title": title,
                "url": url,
                "dirname": dirname,
            }
        )

    return chapter_items


def write_file(
        path: Path,
        content: str,
        dry_run: bool,
        override: bool
) -> bool:
    """Write file if allowed. Return True if file was created, False otherwise."""
    if path.exists() and not override:
        logging.info(
            f"File '{path}' already exists. Skipping (use --override to overwrite).")
        return False

    if dry_run:
        logging.info(f"[Dry Run] Would create file: '{path}'")
        return True

    try:
        with path.open('w', encoding='utf-8') as file:
            file.write(content)
        logging.info(f"Created file: '{path}'")
        return True
    except Exception as e:
        logging.error(f"Error writing file '{path}': {e}")
        return False


def populate_utility_files(
        base_dir: Path,
        toc_file: Path,
        chapters_dir: Path,
        dry_run: bool,
        override: bool
) -> None:
    """Populate utility files in chapter directories based on TOC data."""
    if not toc_file.is_file():
        logging.error(
            f"TOC file '{toc_file}' does not exist or is not a file.")
        return

    toc_data = load_json(toc_file)
    chapter_items = extract_chapter_items(toc_data)

    if not chapter_items:
        logging.warning("No valid chapter items found in TOC.")
        return

    files_written = 0

    for chapter in chapter_items:
        chapter_dir = chapters_dir / chapter["dirname"]

        if not chapter_dir.is_dir():
            logging.warning(
                f"Chapter directory '{chapter_dir}' does not exist. Skipping.")
            continue

        for filename, template in DEFAULT_UTITLITY_FILES.items():
            content = template.format(title=chapter["title"])
            target_file = chapter_dir / filename

            if write_file(
                path=target_file,
                content=content,
                dry_run=dry_run,
                override=override
            ):
                files_written += 1

    logging.info(
        f"Finished populating utility files. Total files created: {files_written}")


def main() -> None:
    """Main function to execute the script."""
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format='[%(levelname)s] %(message)s'
    )

    base_dir = args.base_dir

    toc_file = (
        args.toc_file.resolve()
        if args.toc_file
        else base_dir / "tools" / "web_scraping" / "out" / "atbs3e_toc.json"
    )

    chapters_dir = (
        args.chapters_dir.resolve()
        if args.chapters_dir
        else base_dir / "chapters"
    )

    populate_utility_files(
        base_dir=base_dir,
        toc_file=toc_file,
        chapters_dir=chapters_dir,
        dry_run=args.dry_run,
        override=args.override
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
