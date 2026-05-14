#!/usr/bin/env python3
"""
cli.py

Command-line interface for generating the PDF report.

Usage:
    python3 cli.py --output trump_china_visit_report_20260514.pdf
"""

from __future__ import annotations

import argparse
from pathlib import Path

from generator import build_report


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate PDF report for Trump's visit to China."
    )

    parser.add_argument(
        "--output", "-o",
        type=str or Path,
        default=Path("report.pdf"),
        help="Output file path.")

    return parser.parse_args()


def main() -> None:
    """Run report generation."""

    args = parse_args()

    output_path = args.output

    generated_file = build_report(output_path)

    print("Generated report successfully.")
    print(f"Saved to: {generated_file}")


if __name__ == "__main__":
    main()
