#!/usr/bin/env python3
"""
move_files.py

Utility to move files from one directory to another. This script is designed to help organize files
by moving them to specified target directories. It can be used to clean up and manage file structures efficiently.
"""

from __future__ import annotations

from pathlib import Path
import shutil


def move_files(source_dir: Path, target_dir: Path, file_list: list[str]) -> None:
    """
    Move files from the source directory to the target directory.

    Args:
        source_dir: The directory containing the files to be moved.
        target_dir: The directory where the files will be moved to.
        file_list: A list of filenames to be moved.
    """
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Source directory {source_dir} does not exist or is not a directory.")
        return

    if not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created target directory: {target_dir.resolve()}")

    for item in source_dir.iterdir():
        if item.name in file_list:
            if item.is_file():
                shutil.move(str(item), str(target_dir / item.name))
                print(f"Moved file: {item.name} to {target_dir.resolve()}")
            

def main() -> None:
    """
    Entry point for the script.
    """
    # Example usage: Move files from 'source_folder' to 'target_folder'
    file_list: list[str] = [
        "create_placeholder_file.py",
        "create_report_workspace.py",
        "create_subdirectories.py",
    ]

    project_dir = Path(__file__).parent.parent
    source_folder = Path("tools")
    target_folder = Path("news_reports") / Path("utilities")
    source_folder = project_dir / source_folder
    target_folder = project_dir / target_folder

    move_files(source_folder, target_folder, file_list)

if __name__ == "__main__":
    main()