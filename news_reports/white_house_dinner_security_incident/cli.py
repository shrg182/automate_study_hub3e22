#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from generator import build_report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="report.pdf")
    args = parser.parse_args()

    path = Path(args.output)

    file = build_report(path)

    print("Generated report successfully.")
    print(f"Saved to: {file}")


if __name__ == "__main__":
    main()