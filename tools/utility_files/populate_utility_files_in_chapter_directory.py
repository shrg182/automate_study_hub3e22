#!/usr/bin/env python3
"""
populate_utility_files_in_chapter_directory.py

Populate README.md and USAGE.md files in one chapter directory by using
independent template files.

The chapter information is provided inside this script.

Usage:
    python3 tools/utility_files/populate_utility_files_in_chapter_directory.py
    python3 tools/utility_files/populate_utility_files_in_chapter_directory.py --overwrite
    python3 tools/utility_files/populate_utility_files_in_chapter_directory.py --dry-run
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from typing import Final


PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[2]

TEMPLATE_DIR: Final[Path] = Path(__file__).resolve().parent / "templates"

README_TEMPLATE: Final[Path] = TEMPLATE_DIR / "README.md.template"
USAGE_TEMPLATE: Final[Path] = TEMPLATE_DIR / "USAGE.md.template"

PARENT_DIRECTORY_NAME: Final[str] = "chapters2"

CHAPTER_DIRECTORY_NAME: Final[str] = (
    "chapter_12_designing_and_deploying_command_line_programs"
)

CHAPTER_TITLE: Final[str] = (
    "Chapter 12 Designing And Deploying Command Line Programs"
)

CHAPTER_PAGE_URL: Final[str] = (
    "https://welib.org/md5/8f15563c16d2a98c4d3115150679b092"
)

ATBS_CHAPTER_URL: Final[str] = (
    "https://automatetheboringstuff.com/3e/chapter12.html"
)

CHAPTER_DIR: Final[Path] = (
    PROJECT_ROOT / PARENT_DIRECTORY_NAME / CHAPTER_DIRECTORY_NAME
)


def read_template(template_path: Path) -> str:
    """Read and return the contents of a template file."""
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    return template_path.read_text(encoding="utf-8")


def build_template_context() -> dict[str, str]:
    """Build the replacement values used by the template files."""
    generated_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")

    relative_chapter_directory = str(
        CHAPTER_DIR.relative_to(PROJECT_ROOT)
    )

    return {
        "chapter_title": CHAPTER_TITLE,
        "parent_directory_name": PARENT_DIRECTORY_NAME,
        "chapter_directory_name": CHAPTER_DIRECTORY_NAME,
        "chapter_page_url": CHAPTER_PAGE_URL,
        "atbs_chapter_url": ATBS_CHAPTER_URL,
        "generated_datetime": generated_datetime,
        "relative_chapter_directory": relative_chapter_directory,
    }


def render_template(template_text: str, context: dict[str, str]) -> str:
    """Render a template string using the provided context."""
    return template_text.format(**context)


def write_file(
    output_path: Path,
    content: str,
    overwrite: bool,
    dry_run: bool,
) -> None:
    """Write content to a file, respecting overwrite and dry-run options."""
    if output_path.exists() and not overwrite:
        print(f"Skipped existing file: {output_path}")
        return

    if dry_run:
        action = "Would overwrite" if output_path.exists() else "Would create"
        print(f"{action}: {output_path}")
        return

    output_path.write_text(content, encoding="utf-8")

    action = "Overwritten" if output_path.exists() else "Created"
    print(f"{action}: {output_path}")


def populate_utility_files(overwrite: bool, dry_run: bool) -> None:
    """Populate README.md and USAGE.md in the target chapter directory."""
    if not CHAPTER_DIR.exists():
        raise FileNotFoundError(f"Chapter directory not found: {CHAPTER_DIR}")

    context = build_template_context()

    readme_text = render_template(
        read_template(README_TEMPLATE),
        context,
    )

    usage_text = render_template(
        read_template(USAGE_TEMPLATE),
        context,
    )

    write_file(
        output_path=CHAPTER_DIR / "README.md",
        content=readme_text,
        overwrite=overwrite,
        dry_run=dry_run,
    )

    write_file(
        output_path=CHAPTER_DIR / "USAGE.md",
        content=usage_text,
        overwrite=overwrite,
        dry_run=dry_run,
    )


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Populate README.md and USAGE.md in a chapter directory "
            "from independent template files."
        )
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite README.md and USAGE.md if they already exist.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing files.",
    )

    return parser.parse_args()


def main() -> None:
    """Run the utility-file population script."""
    args = parse_args()

    populate_utility_files(
        overwrite=args.overwrite,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()