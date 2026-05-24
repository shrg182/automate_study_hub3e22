#!/usr/bin/env python3
"""
list_chapter_names.py

List chapter directory names only.

Usage:
    python3 tools/utility_files/list_chapter_names.py
    python3 tools/utility_files/list_chapter_names.py chapters
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


EXCLUDE_DIRS: set[str] = {
    ".git",
    ".idea",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
}


def get_chapter_directories(root: Path) -> list[Path]:
    """
    Get chapter directories from the root directory.

    Args:
        root: Directory that contains chapter folders.

    Returns:
        A sorted list of chapter directory paths.
    """
    return sorted(
        [
            item
            for item in root.iterdir()
            if item.is_dir()
            and item.name not in EXCLUDE_DIRS
            and item.name.startswith("chapter_")
        ],
        key=lambda item: item.name.lower(),
    )


def print_chapter_names(root: Path) -> None:
    """
    Print chapter directory names only.

    Args:
        root: Directory that contains chapter folders.
    """
    chapter_dirs = get_chapter_directories(root)

    if not chapter_dirs:
        print(f"No chapter directories found in: {root}")
        return

    for chapter_dir in chapter_dirs:
        print(chapter_dir.name)


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="List chapter directory names only.",
    )

    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path("chapters"),
        help="Directory that contains chapter folders. Default: chapters",
    )

    return parser.parse_args()


def main() -> None:
    """Run the script."""
    args = parse_args()
    root_path: Path = args.root.expanduser().resolve()

    if not root_path.exists():
        print(f"Error: Path does not exist: {root_path}", file=sys.stderr)
        sys.exit(1)

    if not root_path.is_dir():
        print(f"Error: Path is not a directory: {root_path}", file=sys.stderr)
        sys.exit(1)

    print_chapter_names(root_path)


if __name__ == "__main__":
    main()
