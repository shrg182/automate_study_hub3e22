#!/usr/bin/env python3
"""
data_model

Data structures and current contents for the Trump China Visit Report

TODO:
    - Add dataclasses, i.e. Vocabulary and ReportContent.
    - Add data model parts.
    - Add main program logic.
"""

from __future__ import annotations

from dataclasses import dataclass

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class VocabularyItem:
    """Represent one vocabulary item."""

    term: str
    definition: str


@dataclass(slots=True)
class ReportContent:
    """Store all report content."""

    title: str
    author_line: str
    as_of_date: date
    breaking_news: str
    executive_summary: list[str]
    situation_analysis: list[str]
