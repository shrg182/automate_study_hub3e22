#!/usr/bin/env python3
"""
list_chapter_directories.py

Get chapters' directory tree and list it.

Usage:
    python3 list_chapter_directories.py
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

    connector: str = "|-" if is_last else "--"

    if root.is_dir():
        children: List[Path] = sorted(
            [
                item for item in root.iterdir()
                if item.name not in EXCLUDE_DIRS
            ],
            key=lambda x:
        )
