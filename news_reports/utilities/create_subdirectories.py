#!/usr/bin/env python3
"""
create_subdirectories.py

Utility to create subdirectories for the world peace PDF report.
This script sets up the necessary folder structure for storing
edited and generated report files.
"""

from __future__ import annotations

from pathlib import Path


def create_subdirectories(base_path: Path) -> None:
    """
    Create necessary subdirectories under the given base path.

    Args:
        base_path: The parent directory where subfolders will be created.
    """
    subdirs = ["world_peace_report_edited", "world_peace_report_generated"]

    for subdir in subdirs:
        dir_path = base_path / subdir
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path.resolve()}")


def main() -> None:
    """
    Entry point for the script.
    """
    # Correct Path usage
    project_dir = Path(__file__).parent.parent
    target_path = project_dir / "news_reports" / "world_peace_report"

    # Ensure base directory exists
    target_path.mkdir(parents=True, exist_ok=True)

    create_subdirectories(target_path)


if __name__ == "__main__":
    main()