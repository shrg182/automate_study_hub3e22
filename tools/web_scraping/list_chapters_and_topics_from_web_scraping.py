#!/usr/bin/env python3
"""
list_chapters_and_topics_from_web_scraping.py


"""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Final

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent[2]
DEFAULT_TOC_FILE: Final[Path] = (
    PROJECT_ROOT / "tools" / "web_scraping" / "out" / "atbs3e_chapter_topics.json"
)
DEFAULT_CHAPTER_DIR: Final[Path] = PROJECT_ROOT / "chapters"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="List chapters and topics from a CSV or JSON TOC file."
    )
