#!/usr/bin/env python3
"""
export_atbs3e_chapter_topics_txt.py

Export scraped ATBS 3e chapter-topic items to a plain text file.

Usage:
    python3 tools/web_scraping/export_atbs3e_chapter_topics_txt.py 
    python3 tools/web_scraping/export_atbs3e_chapter_topics_txt.py --chapter-number 10
    python3 tools/web_scraping/export_atbs3e_chapter_topics_txt.py --chapter-number 10 --topic-heading 4
    python3 tools/web_scraping/export_atbs3e_chapter_topics_txt.py --chapter-number 10 --topic-heading 4 --show-url
"""

from __future__ import annotations

import argparse
import json
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

DEFAULT_OUTPUT_TXT = (
    PROJECT_ROOT
    / "tools"
    / "web_scraping"
    / "out"
    / "atbs3e_chapter_topics_list.txt"
)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Export scraped ATBS 3e chapter topics to a text file."
    )

    parser.add_argument(
        "--topics-file",
        type=Path,
        default=DEFAULT_TOPICS_JSON,
        help=f"Path to chapter topics JSON file. Default: {DEFAULT_TOPICS_JSON}"
    )
