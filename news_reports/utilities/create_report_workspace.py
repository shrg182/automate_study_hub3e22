#!/usr/bin/env python3
"""
create_report_workspace.py

Create a starter workspace for the world peace PDF report.

This script builds a small report workflow directory structure and
adds placeholder files so the folders are ready for editing, output,
logging, and asset storage.
"""

from __future__ import annotations

import json
from pathlib import Path

# Directory names and their descriptions for README files
# Replace white_house_dinner_assassination with white_house_dinner
DIRECTORY_DESCRIPTIONS: dict[str, str] = { # Directory names and their descriptions for README files
    "white_house_dinner_assassination": (
        "This directory stores edited source material, notes, draft text, "
        "and manually revised report content."
    ),
    "white_house_dinner_assassination_generated": (
        "This directory stores generated PDF reports and other output files."
    ),
    "white_house_dinner_assassination_logs": (
        "This directory stores log files, execution notes, and processing history."
    ),
    "white_house_dinner_assassination_assets": (
        "This directory stores supporting assets such as images, charts, "
        "icons, and reference materials."
    ),
}


def create_directory(path: Path) -> None:
    """
    Create a directory and any missing parent directories.

    Args:
        path: The directory path to create.
    """
    path.mkdir(parents=True, exist_ok=True)
    print(f"Ready directory: {path.resolve()}")


def write_file_if_missing(path: Path, content: str) -> None:
    """
    Create a text file only if it does not already exist.

    Args:
        path: File path to create.
        content: File content to write.
    """
    if path.exists():
        print(f"Skipped existing file: {path.resolve()}")
        return

    path.write_text(content, encoding="utf-8")
    print(f"Created file: {path.resolve()}")


def create_gitkeep(path: Path) -> None:
    """
    Create an empty .gitkeep file if it does not already exist.

    Args:
        path: Full path to the .gitkeep file.
    """
    if path.exists():
        print(f"Skipped existing file: {path.resolve()}")
        return

    path.touch()
    print(f"Created file: {path.resolve()}")


def create_readme(directory: Path, description: str) -> None:
    """
    Create a README.md file for a directory if missing.

    Args:
        directory: The target directory.
        description: Description text for the directory.
    """
    readme_path = directory / "README.md"
    content = f"# {directory.name}\n\n{description}\n"
    write_file_if_missing(readme_path, content)


def create_notes_file(directory: Path) -> None:
    """
    Create a starter notes.md file in the edited directory.

    Args:
        directory: The edited directory path.
    """
    notes_path = directory / "notes.md"
    content = (
        "# Report Notes\n\n"
        "Use this file to store:\n\n"
        "- draft summary points\n"
        "- revision notes\n"
        "- section ideas\n"
        "- references to check\n"
    )
    write_file_if_missing(notes_path, content)


def create_metadata_file(directory: Path) -> None:
    """
    Create a starter JSON metadata file in the edited directory.

    Args:
        directory: The edited directory path.
    """
    metadata_path = directory / "report_metadata.json"

    metadata = {
        "title": "Current World Peace Negotiation Report",
        "author": "ChatGPT",
        "status": "draft",
        "version": "1.0",
        "tags": ["world peace", "negotiation", "pdf report"],
        "notes": "Update fields as the report evolves.",
    }

    if metadata_path.exists():
        print(f"Skipped existing file: {metadata_path.resolve()}")
        return

    metadata_path.write_text(
        json.dumps(metadata, indent=4, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Created file: {metadata_path.resolve()}")


def create_log_file(directory: Path) -> None:
    """
    Create a starter run.log file in the logs directory.

    Args:
        directory: The logs directory path.
    """
    log_path = directory / "run.log"
    content = "Log initialized.\n"
    write_file_if_missing(log_path, content)


def create_placeholder_file(directory: Path, filename: str) -> None:
    """
    Create a placeholder file in a directory if missing.

    Args:
        directory: The target directory.
        filename: Placeholder filename.
    """
    placeholder_path = directory / filename
    write_file_if_missing(
        placeholder_path,
        "This is a placeholder file.\n",
    )


def build_workspace(base_path: Path) -> None:
    """
    Build the full report workspace under the base path.

    Args:
        base_path: Base directory for the report workspace.
    """
    create_directory(base_path)

    for folder_name, description in DIRECTORY_DESCRIPTIONS.items():
        directory = base_path / folder_name
        create_directory(directory)
        create_readme(directory, description)

    edited_dir = base_path / "white_house_dinner_assassination"
    generated_dir = base_path / "white_house_dinner_assassination_generated"
    logs_dir = base_path / "white_house_dinner_assassination_logs"
    assets_dir = base_path / "white_house_dinner_assassination_assets"

    create_notes_file(edited_dir)
    create_metadata_file(edited_dir)

    create_placeholder_file(generated_dir, "placeholder.txt")
    create_log_file(logs_dir)
    create_gitkeep(assets_dir / ".gitkeep")


def main() -> None:
    """
    Entry point for the script.
    """
    project_dir = Path(__file__).resolve().parent.parent
    target_path = project_dir / "white_house_dinner_assassination"

    build_workspace(target_path)


if __name__ == "__main__":
    main()