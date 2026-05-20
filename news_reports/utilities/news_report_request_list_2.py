#!/usr/bin/env python3
"""news_report_request_list.py

Create a folder for the news report and write a list of default report requirements.
The generated CSV can be used as instructions for future news report generation.

Usage:
    python3 news_report_request_list.py
    python3 news_report_request_list.py --report-folder putin_visit_to_china_3
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

DEFAULT_REQUIREMENTS = (
    "Title",
    "Breaking News",
    "Leads",
    "Key Themes",
    "Executive Summary",
    "Situation Analysis",
    "Latest Updates",
    "Risk Assessment",
    "Comments",
    "New Vocabulary",
    "Sources",
    "Credits",
)
DEFAULT_CSV_NAME = "news_report_request_list.csv"
CSV_FIELDNAMES = ["order", "requirement", "include", "specific_requirements"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a news report request CSV."
    )
    parser.add_argument(
        "--report-folder",
        default="news_report_request",
        help="Folder name under news_reports.",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_CSV_NAME,
        help="CSV filename to create inside the report folder.",
    )
    return parser.parse_args()


def normalize_folder_name(folder_name: str) -> str:
    return "".join(
        char for char in folder_name.strip().replace(" ", "_")
        if char.isalnum() or char in "-_"
    ).lower() or "news_report_request"


def default_rows() -> list[dict[str, str]]:
    return [
        {
            "order": str(index),
            "requirement": requirement,
            "include": "yes",
            "specific_requirements": "",
        }
        for index, requirement in enumerate(DEFAULT_REQUIREMENTS, start=1)
    ]


def save_csv(csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()
        writer.writerows(default_rows())
    print(f"Saved CSV: {csv_path.resolve()}")


def main() -> None:
    args = parse_args()
    folder_name = normalize_folder_name(args.report_folder)
    report_dir = Path(__file__).resolve().parent.parent / folder_name
    save_csv(report_dir / args.output)


if __name__ == "__main__":
    main()
