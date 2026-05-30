#!/usr/bin/env python3
"""
generate_atbs3e_chapter_summaries.py

Generate simple Markdown summaries from scraped ATBS 3e chapter-topic items.

The script creates deterministic summaries from topic headings in the scraped JSON file. It does not use AI. It goups toics by chapter and summaries the main H2 topics with optional supporting subtopics.

Usage:
    python3 tools/web_scraping/generate_atbs3e_chapter_summaries.py
    python3 tools/web_scraping/generate_atbs3e_chapter_summaries.py --chapter-number 10
    python3 tools/web_scraping/generate_atbs3e_chapter_summaries.py --chapter-number 10 --topic-heading 4
    python3 tools/web_scraping/generate_atbs3e_chapter_summaries.py --chapter-number 10 --show-url

"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_TOPICS_JSON = (
    PROJECT_ROOT
    / "tools"
    / "web_scraping"
    / "out"
    / "atbs3e_chapter_topics.json"
)

DEFAULT_OUTPUT_MD = (
    PROJECT_ROOT
    / "tools"
    / "web_scraping"
    / "out"
    / "atbs3e_chapter_summaries.md"
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate Markdown summaries from ATBS 3e chapter topics."
    )

    parser.add_argument(
        "--topics-file",
        type=Path,
        default=DEFAULT_TOPICS_JSON,
        help=f"Path to chapter topics JSON file. Default: {DEFAULT_TOPICS_JSON}",
    )

    parser.add_argument(
        "--output-file",
        type=Path,
        default=DEFAULT_OUTPUT_MD,
        help=f"Output Markdown file path. Default: {DEFAULT_OUTPUT_MD}",
    )

    parser.add_argument(
        "--chapter-number",
        type=int,
        default=None,
        help="Only generate a summary for this chapter number",
    )

    parser.add_argument(
        "--topic-heading",
        choices=range(2, 7),
        metavar="{2,3,4,5,6}",
        default=4,
        help=(
            "Include topics up to this heading level. "
            "Example: 4 includes H2, H3, and H4. Default: 4."
        )
    )

    parser.add_argument(
        "--show-url",
        action="store_true",
        help="Include topic URLs in the generated summary file."
    )

    return parser.parse_args()
