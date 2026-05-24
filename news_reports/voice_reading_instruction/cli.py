#!/usr/bin/env python3
"""
Command line entry point for the voice reading instruction PDF.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from generator import DEFAULT_OUTPUT, build_instruction_pdf


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(
        description="Generate the voice reading instruction PDF."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output PDF path.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the PDF generator."""

    args = parse_args()
    output_path = build_instruction_pdf(args.output)
    print(f"Created {output_path}")


if __name__ == "__main__":
    main()
