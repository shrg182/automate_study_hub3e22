#!/usr/bin/env python3
"""
cli.py

Command-line interface for generating the Cuba Crisis news report.

Usage:
    python3 cli.py
    python3 cli.py --request-csv news_report_request_list.csv --output report.pdf
"""

from __future__ import annotations

import argparse
from pathlib import Path

from generator import DEFAULT_OUTPUT, DEFAULT_REQUEST_CSV, build_report


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Generate a Cuba Crisis PDF report from a request CSV."
    )
    parser.add_argument(
        "--request-csv",
        type=Path,
        default=Path(DEFAULT_REQUEST_CSV),
        help="CSV file listing requested report sections.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(DEFAULT_OUTPUT),
        help="Output PDF filename.",
    )
    return parser.parse_args()


def main() -> None:
    """Run report generation."""

    args = parse_args()
    generated_file = build_report(args.output, args.request_csv)
    print("Generated report successfully.")
    print(f"Saved to: {generated_file}")


if __name__ == "__main__":
    main()
