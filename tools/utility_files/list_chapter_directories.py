#!/usr/bin/env python3
"""
list_chapter_directories.py

Get chapters' directory tree and list it.

Usage:
    python3 list_chapter_directories.py
    python3 tools/utility_files/list_chapter_directories.py chapters
"""

from pathlib import Path
from typing import Iterable, List
import sys

# Folders to ignore (customize as needed)
EXCLUDE_DIRS: set[str] = {".venv", "__pycache__"}


def build_tree(
    root: Path,
    prefix: str = "",
    is_last: bool = True,
) -> List[str]:
    """
    Recursively build a directory tree.

    Args:
        root: The root path to display.
        prefix: Prefix string for formating branches.
        is_last: Whether this node is the last child.

    Returns:
        A list of formatted tree lines.
    """
    lines: List[str] = []

    connector: str = "└── " if is_last else "├── "
    lines.append(f"{prefix}{connector}{root.name}")

    if root.is_dir():
        children: List[Path] = sorted(
            [
                item for item in root.iterdir()
                if item.name not in EXCLUDE_DIRS
            ],
            key=lambda x: (not x.is_dir(), x.name.lower())
        )

        new_prefix: str = prefix + ("   " if is_last else "|   ")

        for index, child in enumerate(children):
            is_last_child: bool = index == len(children) - 1
            lines.extend(
                build_tree(child, new_prefix, is_last_child)
            )

    return lines


def print_tree(root: Path) -> None:
    """
    Print the directory tree starting from root.

    Args:
        root: The root directory.
    """
    print(f"{root.name}/")

    children: List[Path] = sorted(
        [
            item for item in root.iterdir()
            if item.name not in EXCLUDE_DIRS
        ],
        key=lambda x: (not x.is_dir(), x.name.lower())
    )

    for index, child in enumerate(children):
        is_last: bool = index == len(children) - 1
        lines: List[str] = build_tree(child, "", is_last)
        for line in lines:
            print(line)


def main() -> None:
    """Entry point."""
    if len(sys.argv) > 1:
        root_path: Path = Path(sys.argv[1])
    else:
        root_path = Path.cwd()

    if not root_path.exists():
        print(f"Error: Path '{root_path}' does not exist.")

    print_tree(root_path)


if __name__ == "__main__":
    main()
