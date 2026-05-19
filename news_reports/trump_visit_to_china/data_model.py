#!/usr/bin/env python3
"""
data_model.py

Data structures and current content for the Trump China Visit Report.
"""

from __future__ import annotations

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
    latest_updates: list[str]
    risk_assessment: list[str]
    comments: list[str]
    vocabulary: list[VocabularyItem]
    credits: str


def build_sample_report_content() -> ReportContent:
    """
    Build current sample report content.

    Returns:
        ReportContent instance.
    """
    vocabulary = [
        VocabularyItem(
            "state visit", "An official visit by a head of state to another country."),
        VocabularyItem("bilateral relations",
                       "Relations between two countries."),
        VocabularyItem("trade truce", "A temporary easing of trade conflict."),
        VocabularyItem("tariffs", "Taxes placed on imported goods."),
        VocabularyItem(
            "rare earths", "Minerals used in electronics, defense systems, and clean technology."),
        VocabularyItem("strategic rivalry",
                       "Competition for influence and power between states."),
        VocabularyItem(
            "Taiwan issue", "The diplomatic and security dispute over Taiwan's status and future."),
        VocabularyItem("maritime security",
                       "Security related to oceans, sea routes, and naval activity."),
        VocabularyItem("business delegation",
                       "A group of business leaders traveling for official meetings."),
        VocabularyItem("diplomatic leverage",
                       "Influence used to gain advantage in negotiations."),
    ]

    return ReportContent(
        title="Trump China Visit Report",
        author_line="by ChatGPT",
        as_of_date=date(2026, 5, 9),
        latest_updates=[
            (
                "Reuters reported that Trump is preparing to visit Beijing on May 14 and 15, "
                "with Taiwan, trade, technology, and rare earths among the major issues expected to shape the agenda."
            ),
            (
                "Reuters also reported that the Trump administration invited business leaders, including executives "
                "from Nvidia and Boeing, to join the China trip."
            ),
            (
                "Taiwanese officials said China may try to maneuver over the Taiwan issue during the meeting, "
                "while the U.S. side has stated that its Taiwan policy has not changed."
            ),
            (
                "Financial-market attention is focused on whether the summit produces concrete trade steps "
                "or merely extends the current fragile pause in tensions."
            ),
        ],
        risk_assessment=[
            "Risk level: Moderate to elevated",
            "Diplomatic outlook: Active but uncertain",
            "Economic outlook: Possible short-term stabilization, limited long-term reset",
            "Security outlook: Taiwan and maritime issues remain sensitive flashpoints",
            "Business outlook: Corporate participation may support deal-making but could draw political scrutiny",
        ],
        comments=[
            (
                "The visit is likely to produce symbolic progress if both sides emphasize stability, "
                "but structural competition between the United States and China will remain."
            ),
            (
                "A limited trade or investment package is more plausible than a broad strategic reset."
            ),
            (
                "The Taiwan issue remains the most politically sensitive item because any perceived shift "
                "in language or commitment could trigger regional concern."
            ),
        ],
        vocabulary=vocabulary,
        credits=(
            "This report combines AI-generated factual content from ChatGPT with analytical structuring "
            "designed for educational and informational purposes. Current-event details should be checked "
            "against primary or reputable news sources before publication."
        ),
    )
