#!/usr/bin/env python3
"""
create_chapter_directories.py

A script to create chapter directories for a book project.
Usage:
    python3 create_chapter_directories.py
    python3 create_chapter_directories.py --base-dir chapters
    python3 create_chapter_directories.py --base-dir book_project
    python3 create_chapter_directories.py --base-dir tools/placeholders
"""

from __future__ import annotations

import argparse
from pathlib import Path

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHAPTERS_DIR = PROJECT_ROOT / "chapters"
TOOLS_DIR = PROJECT_ROOT / "tools"
OUTPUT_DIR = PROJECT_ROOT / "tools" / "placeholders" / "output"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Create chapter directories for a book project.")

    parser.add_argument(
        "--base-dir",
        type=Path,
        default=CHAPTERS_DIR,
        help="Base directory to create chapter directories (default: current directory)",
    )

    return parser.parse_args()


def create_chapter_directories(base_dir: Path) -> None:
    """Create chapter directories in the specified base directory."""
    for i in range(0, 24 + 1):
        chapter_dir = base_dir / f"Chapter_{i:02d}"
        chapter_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {chapter_dir}")


if __name__ == "__main__":
    args = parse_args()
    create_chapter_directories(args.base_dir)
