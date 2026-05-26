#!/usr/bin/env python3
"""
list_chapter_directories.py

Display a directory tree for a Python study project or chapter directory.

Usage:
    python3 list_chapter_directories.py
    python3 list_chapter_directories.py chapters
    python3 tools/utility_files/list_chapter_directories.py chapters
    python3 tools/utility_files/list_chapter_directories.py chapters --format True

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
    ".DS_Store"
}


def get_sorted_children(root: Path) -> list[Path]:
    """
    Return sorted child paths, excluding unwanted directories.

    Directories are listed before files.
    Items are sorted alphabetically, ignoring case.
    """
    try:
        children = [
            item
            for item in root.iterdir()
            if item.name not in EXCLUDE_DIRS
        ]
    except PermissionError:
        return []

    return sorted(
        children,
        key=lambda item: (not item.is_dir(), item.name.lower()),
    )


def build_tree(
    path: Path,
    prefix: str = "",
    is_last: bool = True,
) -> list[str]:
    """
    Recursively build a directory tree.

    Args:
        path: The path to display.
        prefix: Prefix string for formatting branches.
        is_last: Whether this path is the last child.

    Returns:
        A list of formatted tree lines.
    """
    connector = "└── " if is_last else "├── "
    display_name = f"{path.name}/" if path.is_dir() else path.name

    lines: list[str] = [f"{prefix}{connector}{display_name}"]

    if not path.is_dir():
        return lines

    children = get_sorted_children(path)

    next_prefix = prefix + ("    " if is_last else "│   ")

    for index, child in enumerate(children):
        is_last_child = index == len(children) - 1
        lines.extend(build_tree(child, next_prefix, is_last_child))

    return lines


def print_tree(root: Path) -> None:
    """
    Print the directory tree starting from root.

    Args:
        root: The root directory.
    """
    print(f"{root.name}/")

    children = get_sorted_children(root)

    for index, child in enumerate(children):
        is_last = index == len(children) - 1
        lines = build_tree(child, "", is_last)

        for line in lines:
            print(line)


def print_tree_format_1(root: Path) -> None:
    """
    Print the directory tree in a format like:
        directory 1, directory 2, ..., last directory,
        for use in the population of placeholder files.

    That is:
    python3 tools/utility_files/populate_utility_files_in_chapters.py --overwrite --exclude-overwrite-chapters chapter_00_introduction
    """
    children = get_sorted_children(root)

    for index, child in enumerate(children):
        line = f"{index} {child}, "
        print(line)


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Display a directory tree.",
    )

    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="Root directory to display. Default: current directory.",
    )
    parser.add_argument(
        "--format",
        type=str,
        default="exclude",
        help="a list of directory names for --overwrite exclude chapters, like chapter_00_introduction, chapter_01..."
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

    format = args.format

    if format:
        print_tree_format_1(root_path)
    else:
        print_tree(root_path)


if __name__ == "__main__":
    main()
