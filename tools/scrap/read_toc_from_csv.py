#!/usr/bin/env python3
"""
read_toc_from_csv.py

Read and display the ATBS 3e table of contents from a CSV file.

Usage:
    python3 read_toc_from_csv.py
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Dict


CSV_FILE: Path = Path.cwd() / 'out' / "atbs3e_toc.csv"


def load_toc(csv_path: Path) -> List[Dict[str, str]]:
    """Load TOC data from a CSV file."""
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with csv_path.open(mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def display_toc(toc: List[Dict[str, str]]) -> None:
    """Print the table of contents in a readable format."""
    print("\n=== ATBS 3e Table of Contents (CSV) ===\n")

    for index, item in enumerate(toc, start=1):
        title: str = item.get("title", "N/A")
        link: str = item.get("link", "N/A")

        print(f"{index:02d}. {title}")
        print(f"     {link}\n")


def main() -> None:
    """Entry point."""
    toc_data = load_toc(CSV_FILE)
    display_toc(toc_data)


if __name__ == "__main__":
    main()