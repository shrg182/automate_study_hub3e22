#!/usr/bin/env python3
"""
cli.py

Command-line entry point for generating the World Peace Negotiation Report.

Usage:
    python3 cli.py
    python3 cli.py --output my_world_peace_report.pdf
"""

from __future__ import annotations

import argparse
from pathlib import Path

from generator import build_report


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate a PDF world peace negotiation report."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="world_peace_negotiation_report.pdf",
        help="Output PDF filename or path.",
    )
    return parser.parse_args()


def main() -> None:
    """
    Generate the PDF report from command-line input.
    """
    args = parse_args()
    output_path = Path(args.output)

    created_file = build_report(output_path)

    print("Generated report successfully.")
    print("Author: ChatGPT")
    print(f"Saved to: {created_file}")


if __name__ == "__main__":
    main()