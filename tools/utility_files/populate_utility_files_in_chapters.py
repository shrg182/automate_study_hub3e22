#!/usr/bin/env python3
"""
populate_utility_files_in_chapters.py

Populate README.md, USAGE.md, and utils.py files in chapter directories and
their subdirectories.

The script discovers the chapter tree from the filesystem, optionally enriches
chapter metadata from the ATBS table-of-contents JSON file, renders the utility
templates, and writes the rendered files into each discovered directory.

Usage:
    python3 tools/utility_files/populate_utility_files_in_chapters.py
    python3 tools/utility_files/populate_utility_files_in_chapters.py --dry-run
    python3 tools/utility_files/populate_utility_files_in_chapters.py --overwrite
    python3 tools/utility_files/populate_utility_files_in_chapters.py --overwrite --exclude-overwrite-chapters chapter_00_introduction
    python3 tools/utility_files/populate_utility_files_in_chapters.py --include-root
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Final


PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[2]
DEFAULT_CHAPTERS_DIR: Final[Path] = PROJECT_ROOT / "chapters"
DEFAULT_TEMPLATE_DIR: Final[Path] = PROJECT_ROOT / "tools" / "utility_files" / "templates"
DEFAULT_TOC_FILE: Final[Path] = (
    PROJECT_ROOT / "tools" / "web_scraping" / "out" / "atbs3e_toc.json"
)

TEMPLATE_TO_OUTPUT: Final[dict[str, str]] = {
    "README.md.template": "README.md",
    "USAGE.md.template": "USAGE.md",
    "utils.py.template": "utils.py",
}

SKIPPED_DIRECTORY_NAMES: Final[set[str]] = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    "data",
    "output",
}


@dataclass(frozen=True)
class ChapterMetadata:
    """Metadata used to render utility file templates."""

    chapter_number: int | None
    chapter_title: str
    chapter_url: str


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Populate README.md, USAGE.md, and utils.py in chapter directories "
            "and subdirectories."
        )
    )
    parser.add_argument(
        "--chapters-dir",
        type=Path,
        default=DEFAULT_CHAPTERS_DIR,
        help="Directory containing chapter directories (default: chapters).",
    )
    parser.add_argument(
        "--template-dir",
        type=Path,
        default=DEFAULT_TEMPLATE_DIR,
        help="Directory containing template files (default: tools/utility_files/templates).",
    )
    parser.add_argument(
        "--toc-file",
        type=Path,
        default=DEFAULT_TOC_FILE,
        help="Optional JSON table-of-contents file with chapter metadata.",
    )
    parser.add_argument(
        "--include-root",
        action="store_true",
        help="Also populate utility files directly in the chapters directory.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing README.md, USAGE.md, and utils.py files.",
    )
    parser.add_argument(
        "--exclude-overwrite-chapters",
        nargs="*",
        default=[],
        metavar="CHAPTER_DIR",
        help=(
            "Chapter directory names to protect from overwriting, even when "
            "--overwrite is used. Values may be space-separated or comma-separated."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show intended actions without writing files.",
    )
    return parser.parse_args()


def load_toc_metadata(toc_file: Path) -> dict[int, ChapterMetadata]:
    """Load chapter metadata from a TOC JSON file if it exists."""
    if not toc_file.is_file():
        return {}

    data = json.loads(toc_file.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected a list of chapter records in {toc_file}")

    metadata: dict[int, ChapterMetadata] = {}
    for item in data:
        if not isinstance(item, dict):
            continue

        chapter_number = item.get("chapter_num")
        if not isinstance(chapter_number, int):
            chapter_number = extract_chapter_number(
                str(item.get("title", "")),
                str(item.get("url", "")),
            )

        if chapter_number is None:
            continue

        metadata[chapter_number] = ChapterMetadata(
            chapter_number=chapter_number,
            chapter_title=str(item.get("title", f"Chapter {chapter_number}")),
            chapter_url=str(item.get("url", "")),
        )

    return metadata


def extract_chapter_number(title: str, url: str = "") -> int | None:
    """Extract a chapter number from a title, URL, or directory name."""
    patterns = (
        r"\bchapter[_\s-]*(\d+)\b",
        r"\bchapter(\d+)\.html\b",
    )
    haystack = f"{title} {url}"
    for pattern in patterns:
        match = re.search(pattern, haystack, flags=re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def clean_chapter_title(title: str) -> str:
    """Return a display title without a leading chapter prefix."""
    cleaned = re.sub(
        r"^\s*chapter\s+\d+\s*[-:]\s*",
        "",
        title,
        flags=re.IGNORECASE,
    )
    return cleaned.strip() or title.strip()


def prettify_directory_name(directory_name: str) -> str:
    """Convert a snake-case directory name to title case."""
    return directory_name.replace("_", " ").replace("-", " ").title()


def should_skip_directory(path: Path) -> bool:
    """Return True when a directory should not receive utility files."""
    return path.name.startswith(".") or path.name in SKIPPED_DIRECTORY_NAMES


def discover_target_directories(chapters_dir: Path, include_root: bool) -> list[Path]:
    """Discover chapter directories and subdirectories from the filesystem."""
    if not chapters_dir.is_dir():
        raise FileNotFoundError(f"Chapters directory not found: {chapters_dir}")

    targets: list[Path] = []
    if include_root:
        targets.append(chapters_dir)

    for path in sorted(chapters_dir.rglob("*")):
        if not path.is_dir() or should_skip_directory(path):
            continue
        relative_parents = path.relative_to(chapters_dir).parents
        if any(
            parent != Path(".") and should_skip_directory(parent)
            for parent in relative_parents
        ):
            continue
        targets.append(path)

    return targets


def parse_excluded_chapter_names(raw_values: list[str]) -> set[str]:
    """Normalize chapter directory names that should be protected."""
    excluded_names: set[str] = set()
    for raw_value in raw_values:
        for value in raw_value.split(","):
            normalized = value.strip().rstrip("/")
            if normalized:
                excluded_names.add(Path(normalized).name)
    return excluded_names


def is_overwrite_protected(
    target_dir: Path,
    chapters_dir: Path,
    excluded_chapter_names: set[str],
) -> bool:
    """Return True when target_dir is inside a protected chapter directory."""
    if not excluded_chapter_names:
        return False

    relative_parts = target_dir.relative_to(chapters_dir).parts
    if not relative_parts:
        return chapters_dir.name in excluded_chapter_names

    chapter_dir_name = relative_parts[0]
    return chapter_dir_name in excluded_chapter_names


def make_directory_tree(root: Path) -> str:
    """Build a simple text tree for a directory."""
    lines = [root.name + "/"]
    visible_children = sorted(
        child for child in root.iterdir() if not child.name.startswith(".")
    )

    for index, child in enumerate(visible_children):
        connector = "`-- " if index == len(visible_children) - 1 else "|-- "
        suffix = "/" if child.is_dir() else ""
        lines.append(f"{connector}{child.name}{suffix}")

    return "\n".join(lines)


def load_templates(template_dir: Path) -> dict[str, str]:
    """Load all configured template files."""
    templates: dict[str, str] = {}
    for template_name in TEMPLATE_TO_OUTPUT:
        template_path = template_dir / template_name
        if not template_path.is_file():
            raise FileNotFoundError(f"Template file not found: {template_path}")
        templates[template_name] = template_path.read_text(encoding="utf-8")
    return templates


def render_template(template: str, context: dict[str, str]) -> str:
    """Render simple {placeholder_name} tokens in a template.

    The utility templates can include Python code with literal braces. Replacing
    only identifier-like placeholders keeps those braces intact.
    """

    def replace_match(match: re.Match[str]) -> str:
        placeholder = match.group(1)
        return context.get(placeholder, match.group(0))

    return re.sub(r"\{([A-Za-z_][A-Za-z0-9_]*)\}", replace_match, template)


def find_chapter_directory(path: Path, chapters_dir: Path) -> Path:
    """Return the top-level chapter directory for a target path."""
    relative_parts = path.relative_to(chapters_dir).parts
    if not relative_parts:
        return chapters_dir
    return chapters_dir / relative_parts[0]


def build_context(
    target_dir: Path,
    chapters_dir: Path,
    toc_metadata: dict[int, ChapterMetadata],
) -> dict[str, str]:
    """Build template values for a target directory."""
    chapter_dir = find_chapter_directory(target_dir, chapters_dir)
    chapter_number = extract_chapter_number(chapter_dir.name)
    metadata = toc_metadata.get(chapter_number) if chapter_number is not None else None

    chapter_title = (
        metadata.chapter_title
        if metadata is not None
        else prettify_directory_name(chapter_dir.name)
    )
    chapter_url = metadata.chapter_url if metadata is not None else ""
    generated_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    relative_target = target_dir.relative_to(PROJECT_ROOT)
    relative_chapter = chapter_dir.relative_to(PROJECT_ROOT)
    clean_title = clean_chapter_title(chapter_title)

    context = {
        "atbs_chapter_url": chapter_url,
        "chapter_clean_title": clean_title,
        "chapter_dir_name": chapter_dir.name,
        "chapter_directory_name": target_dir.name,
        "chapter_number": "" if chapter_number is None else str(chapter_number),
        "chapter_page_url": chapter_url,
        "chapter_title": chapter_title,
        "chapter_url": chapter_url,
        "clean_chapter_title": clean_title,
        "directory_name": target_dir.name,
        "directory_title": prettify_directory_name(target_dir.name),
        "directory_tree": make_directory_tree(target_dir),
        "generated_at": generated_datetime,
        "generated_datetime": generated_datetime,
        "parent_directory_name": target_dir.parent.name,
        "project_root": str(PROJECT_ROOT),
        "relative_chapter_directory": str(relative_chapter),
        "relative_directory": str(relative_target),
    }
    return context


def write_rendered_file(
    output_path: Path,
    content: str,
    overwrite: bool,
    overwrite_protected: bool,
    dry_run: bool,
) -> str:
    """Write a rendered file and return a status string."""
    if output_path.exists() and overwrite and overwrite_protected:
        return "protected"

    if output_path.exists() and not overwrite:
        return "skipped"

    if dry_run:
        return "would overwrite" if output_path.exists() else "would create"

    existed = output_path.exists()
    output_path.write_text(content, encoding="utf-8")
    return "overwritten" if existed else "created"


def populate_directory(
    target_dir: Path,
    chapters_dir: Path,
    templates: dict[str, str],
    toc_metadata: dict[int, ChapterMetadata],
    overwrite: bool,
    overwrite_protected: bool,
    dry_run: bool,
) -> dict[str, str]:
    """Populate all utility files for one target directory."""
    context = build_context(target_dir, chapters_dir, toc_metadata)
    results: dict[str, str] = {}

    for template_name, output_name in TEMPLATE_TO_OUTPUT.items():
        rendered = render_template(templates[template_name], context)
        output_path = target_dir / output_name
        results[output_name] = write_rendered_file(
            output_path=output_path,
            content=rendered,
            overwrite=overwrite,
            overwrite_protected=overwrite_protected,
            dry_run=dry_run,
        )

    return results


def main() -> None:
    """Populate utility files in discovered chapter directories."""
    args = parse_args()
    chapters_dir = args.chapters_dir.resolve()
    template_dir = args.template_dir.resolve()
    toc_file = args.toc_file.resolve()

    templates = load_templates(template_dir)
    toc_metadata = load_toc_metadata(toc_file)
    excluded_chapter_names = parse_excluded_chapter_names(
        args.exclude_overwrite_chapters
    )
    target_dirs = discover_target_directories(chapters_dir, args.include_root)

    print(f"Discovered {len(target_dirs)} target directories under {chapters_dir}")
    if excluded_chapter_names:
        protected_text = ", ".join(sorted(excluded_chapter_names))
        print(f"Overwrite-protected chapters: {protected_text}")

    status_counts: dict[str, int] = {}
    for target_dir in target_dirs:
        overwrite_protected = is_overwrite_protected(
            target_dir=target_dir,
            chapters_dir=chapters_dir,
            excluded_chapter_names=excluded_chapter_names,
        )
        results = populate_directory(
            target_dir=target_dir,
            chapters_dir=chapters_dir,
            templates=templates,
            toc_metadata=toc_metadata,
            overwrite=args.overwrite,
            overwrite_protected=overwrite_protected,
            dry_run=args.dry_run,
        )
        relative_target = target_dir.relative_to(PROJECT_ROOT)
        result_text = ", ".join(f"{name}: {status}" for name, status in results.items())
        print(f"{relative_target}: {result_text}")

        for status in results.values():
            status_counts[status] = status_counts.get(status, 0) + 1

    summary = ", ".join(
        f"{status}: {count}" for status, count in sorted(status_counts.items())
    )
    print(f"Summary: {summary}")


if __name__ == "__main__":
    main()
