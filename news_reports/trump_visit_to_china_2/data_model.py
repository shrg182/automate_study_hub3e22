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
    breaking_news: str
    executive_summary: list[str]
    situation_analysis: list[str]
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
        VocabularyItem("state visit", "An official visit by a head of state to another country."),
        VocabularyItem("bilateral relations", "Relations between two countries."),
        VocabularyItem("trade truce", "A temporary easing of trade conflict."),
        VocabularyItem("tariffs", "Taxes placed on imported goods."),
        VocabularyItem("rare earths", "Minerals used in electronics, defense systems, and clean technology."),
        VocabularyItem("strategic rivalry", "Competition for influence and power between states."),
        VocabularyItem("Taiwan issue", "The diplomatic and security dispute over Taiwan's status and future."),
        VocabularyItem("maritime security", "Security related to oceans, sea routes, and naval activity."),
        VocabularyItem("business delegation", "A group of business leaders traveling for official meetings."),
        VocabularyItem("diplomatic leverage", "Influence used to gain advantage in negotiations."),
    ]

    return ReportContent(
        title="Trump China Visit Report Update",
        author_line="By ChatGPT",
        as_of_date=date(2026, 5, 13),
        breaking_news="President Trump has arrived in Beijing for a state visit, marking a significant moment in US-China relations.",
        executive_summary=[
            "President Trump's visit to China is a critical opportunity to address key issues in the bilateral relationship.",
            "The visit is expected to focus on trade, security, and regional stability.",
            "Key topics include the trade truce, Taiwan issue, and maritime security.",
        ],
        situation_analysis=[
            "The US-China relationship has been marked by strategic rivalry and economic tensions in recent years.",
            "The trade truce has provided some relief but underlying issues remain unresolved.",
            "The Taiwan issue continues to be a major point of contention, with potential implications for regional security.",
        ],
latest_updates = [
    (
        "President Donald Trump is now airborne and traveling to Beijing "
        "for his May 13–15 state visit to China."
    ),
    (
        "Chinese authorities have finalized preparations for the summit, "
        "including ceremonial events and meetings expected at Beijing's "
        "Temple of Heaven."
    ),
    (
        "Trump is expected to hold high-level talks with Xi Jinping on "
        "trade, tariffs, artificial intelligence, semiconductor controls, "
        "rare earth exports, Taiwan, Iran, and maritime security."
    ),
    (
        "Major U.S. business leaders accompanying or linked to the trip "
        "include executives from Boeing, Apple, Tesla, Mastercard, "
        "BlackRock, and other major corporations."
    ),
    (
        "Financial markets and global investors are closely monitoring "
        "the summit for signs of new trade agreements, tariff relief, "
        "or expanded market access."
    ),
    (
        "Taiwan remains one of the most sensitive agenda items, with "
        "U.S. officials emphasizing that there should be no destabilizing "
        "change in the Indo-Pacific region."
    ),
    (
        "The Iran conflict is also expected to be discussed, although "
        "Trump has publicly stated that he does not require Xi Jinping's "
        "assistance regarding Iran."
    ),
    (
        "Analysts expect the summit to produce symbolic diplomatic progress "
        "and limited commercial agreements, while broader strategic rivalry "
        "between the United States and China is expected to continue."
    ),
],
        risk_assessment=[
            "The visit has the potential to ease tensions but also carries risks of miscommunication and unmet expectations.",
            "The trade truce may be fragile and could unravel if not supported by concrete actions.",
            "The Taiwan issue remains a flashpoint that could escalate if not managed carefully.",
        ],
        comments=[
            "The visit is a reminder of the complex and multifaceted nature of US-China relations.",
            "While there are opportunities for cooperation, significant challenges remain.",
            "The international community will be closely watching the outcomes of this visit.",
        ],
        vocabulary=vocabulary,
        credits=(
            "This report combines AI-generated factual content from ChatGPT with analytical structuring "
            "designed for educational and informational purposes. Current-event details should be checked "
            "against primary or reputable news sources before publication."
        ),
    )   