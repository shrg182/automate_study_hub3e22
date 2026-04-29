#!/usr/bin/env python3
"""
read_toc_from_json.py

Read and display the ATBS 3e table of contents from a JSON file.

Usage:
    python3 read_toc_from_json.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict


JSON_FILE: Path = Path.cwd().resolve() / "out" / "atbs3e_toc.json"


def 