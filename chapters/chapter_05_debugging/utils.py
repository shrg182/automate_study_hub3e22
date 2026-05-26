#!/usr/bin/env python3
"""
utils.py

Utility helper functions for chapter_05_debugging.

Chapter:
    Chapter 5 - Debugging

Chapter page:
    https://automatetheboringstuff.com/3e/chapter5.html

Auto-generated on:
    2026-05-26 00:26:45
"""

from __future__ import annotations

from pathlib import Path


CHAPTER_DIR: Path = Path(__file__).resolve().parent
PROJECT_ROOT: Path = CHAPTER_DIR.parents[1]


def get_chapter_dir() -> Path:
    """Return the absolute path of this chapter directory."""
    return CHAPTER_DIR


def get_project_root() -> Path:
    """Return the absolute path of the project root directory."""
    return PROJECT_ROOT


def get_data_dir() -> Path:
    """
    Return the chapter data directory.

    The directory is created if it does not already exist.
    """
    data_dir = CHAPTER_DIR / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def get_output_dir() -> Path:
    """
    Return the chapter output directory.

    The directory is created if it does not already exist.
    """
    output_dir = CHAPTER_DIR / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def chapter_info() -> dict[str, str]:
    """Return basic chapter information."""
    return {
        "chapter_number": "5",
        "chapter_title": "Chapter 5 - Debugging",
        "clean_chapter_title": "Debugging",
        "chapter_url": "https://automatetheboringstuff.com/3e/chapter5.html",
        "chapter_dir_name": "chapter_05_debugging",
    }


def main() -> None:
    """Display chapter utility information."""
    info = chapter_info()

    print("Chapter utility information")
    print("-" * 32)
    print(f"Chapter number: {{info['chapter_number']}}")
    print(f"Chapter title:  {{info['chapter_title']}}")
    print(f"Chapter URL:    {{info['chapter_url']}}")
    print(f"Chapter dir:    {{get_chapter_dir()}}")
    print(f"Project root:   {{get_project_root()}}")
    print(f"Data dir:       {{get_data_dir()}}")
    print(f"Output dir:     {{get_output_dir()}}")


if __name__ == "__main__":
    main()