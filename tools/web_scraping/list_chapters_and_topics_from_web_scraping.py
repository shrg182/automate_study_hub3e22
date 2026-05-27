#!/usr/bin/env python3
"""
list_chapters_and_topics_from_web_scraping.py


"""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Final

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent[2]
DEFAULT_TOC_FILE: Final[Path] = (
    PROJECT_ROOT / "tools" / "web_scraping" / "out" / "atbs3e_chapter_topics.json"
)
DEFAULT_CHAPTER_DIR: Final[Path] = PROJECT_ROOT / "chapters"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="List chapters and topics from a CSV or JSON TOC file."
    )
    parser.add_argument(
        "--toc-file",
        type=Path,
        default=DEFAULT_TOC_FILE,
        help="CSV or JSON containing chapter information."
    )
    return parser.parse_args()


def load_toc_items(toc_file: Path) -> list[dict[str, Any]]:
    """Load TOC items from a CSV or JSON file."""
    if not toc_file.is_file():
        raise FileNotFoundError(f"TOC file not found: {toc_file}")

    suffix = toc_file.suffix.lower()
    if suffix == ".json":
        data = json.loads(toc_file.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("chapters", data.get("items", []))
        if not isinstance(data, list):
            raise ValueError(f"Expected a list of TOC items in {toc_file}")
        return [item for item in data if isinstance(item, dict)]

    if suffix == ".csv":
        with toc_file.open("r", encoding="utf-8", newline="") as file:
            return list(csv.DictReader(file))

    raise ValueError(f"Unsupported TOC file type: {toc_file.suffix}")
