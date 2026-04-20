#!/usr/bin/env python3
"""
create_placeholder_files.py

Create placeholder files for the world peace PDF report.
"""

from __future__ import annotations

from pathlib import Path


def create_placeholder_file(file_path: Path) -> None:
    """
    Create one placeholder file, along with any missing parent folders.

    Args:
        file_path: The full path to the placeholder file.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.touch(exist_ok=True)
    print(f"Created placeholder file: {file_path.resolve()}")


def create_readme(readme_path: Path, content: str) -> None:
    """
    Create or overwrite a README file.

    Args:
        readme_path: Path to the README file.
        content: Content to write into the README.
    """
    readme_path.parent.mkdir(parents=True, exist_ok=True)
    readme_path.write_text(content, encoding="utf-8")
    print(f"Created README file: {readme_path.resolve()}")


def create_placeholder_files(base_path: Path) -> None:
    """
    Create placeholder files in the specified base path.

    Args:
        base_path: The directory where placeholder files will be created.
    """
    edited_placeholder = (
        base_path / "world_peace_report_edited" / "placeholder.txt"
    )
    generated_placeholder = (
        base_path / "world_peace_report_generated" / "placeholder.txt"
    )
    edited_readme = base_path / "world_peace_report_edited" / "README.md"

    create_placeholder_file(edited_placeholder)
    create_placeholder_file(generated_placeholder)

    create_readme(
        edited_readme,
        (
            "# World Peace Report Edited\n\n"
            "This directory contains edited versions of the world peace report.\n"
        ),
    )


def main() -> None:
    """
    Entry point for the script.
    """
    project_dir = Path(__file__).resolve().parent.parent
    target_path = project_dir / "news_reports" / "world_peace_report"
    target_path.mkdir(parents=True, exist_ok=True)

    create_placeholder_files(target_path)


if __name__ == "__main__":
    main()