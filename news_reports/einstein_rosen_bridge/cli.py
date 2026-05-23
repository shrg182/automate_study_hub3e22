#!/usr/bin/env python3
"""
cli.py

Command-line entry point for the Einstein-Rosen Bridge introduction report.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from generator import build_report


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate the Einstein-Rosen Bridge introduction PDF."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("einstein_rosen_bridge_introduction.pdf"),
        help="Output PDF filename.",
    )
    return parser.parse_args()


def main() -> None:
    """Run report generation."""
    args = parse_args()
    generated_file = build_report(args.output)

    print("Generated report successfully.")
    print(f"Saved to: {generated_file}")


if __name__ == "__main__":
    main()
