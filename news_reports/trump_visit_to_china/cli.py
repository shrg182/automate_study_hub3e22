#!/usr/bin/env python3
"""
cli.py

Command-line interface for generating the PDF report.
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
        description="Generate Trump China Visit PDF report."
    )

    parser.add_argument(
        "--output",
        type=str,
        default="trump_china_visit_report.pdf",
        help="Output PDF filename.",
    )

    return parser.parse_args()


def main() -> None:
    """
    Run report generation.
    """

    args = parse_args()

    output_path = Path(args.output)

    generated_file = build_report(output_path)

    print("Generated report successfully.")
    print(f"Saved to: {generated_file}")


if __name__ == "__main__":
    main()