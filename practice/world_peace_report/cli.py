#!/usr/bin/env python3
"""Command-line entry point for the world peace PDF report."""

from __future__ import annotations

import argparse
from pathlib import Path

from data_model import build_sample_report
from generator import build_pdf


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate a world peace negotiation PDF report."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("world_peace_negotiation_report.pdf"),
        help="Output PDF path. Default: world_peace_negotiation_report.pdf",
    )
    return parser.parse_args()


def main() -> None:
    """Run the PDF report generator."""
    args = parse_args()
    report = build_sample_report()
    output_path = build_pdf(report, args.output)
    print(f"Created PDF: {output_path.resolve()}")


if __name__ == "__main__":
    main()
