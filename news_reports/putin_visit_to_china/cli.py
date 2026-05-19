#!/usr/bin/env python3
"""
cli.py

Command-line interface for generating the PDF report.

Usage:
    python3 cli.py --output putin_china_visit_report_20260519.pdf
"""

from __future__ import annotations

import argparse
from pathlib import Path

from generator import build_report


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Generate Putin China Visit PDF report."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="putin_china_visit_report_20260519.pdf",
        help="Output PDF filename.",
    )

    return parser.parse_args()


def main() -> None:
    """Run report generation."""

    args = parse_args()
    generated_file = build_report(Path(args.output))

    print("Generated report successfully.")
    print(f"Saved to: {generated_file}")


if __name__ == "__main__":
    main()
