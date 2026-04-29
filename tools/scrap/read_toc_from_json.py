#!/usr/bin/env python3
"""
read_toc_from_json.py

Read and display the ATBS 3e table of contents from a JSON file.

Usage:
    python3 read_toc_from_json.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict


JSON_FILE: Path = Path.cwd() / 'out' / "atbs3e_toc.json"


def load_toc(json_path: Path) -> List[Dict[str, str]]:
    """Load TOC data from a JSON file."""
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    with json_path.open(mode="r", encoding="utf-8") as file:
        return json.load(file)


def display_toc(toc: List[Dict[str, str]]) -> None:
    """Print the table of contents in a readable format."""
    print("\n=== ATBS 3e Table of Contents (JSON) ===\n")

    for index, item in enumerate(toc, start=1):
        title: str = item.get("title", "N/A")
        link: str = item.get("link", "N/A")

        print(f"{index:02d}. {title}")
        print(f"     {link}\n")


def main() -> None:
    """Entry point."""
    toc_data = load_toc(JSON_FILE)
    display_toc(toc_data)


if __name__ == "__main__":
    main()