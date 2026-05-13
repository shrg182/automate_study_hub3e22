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
        title="Trump China Visit Report",
        author_line="By Jane Doe, Senior Analyst",
        as_of_date=date(2026, 5, 12),
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
        latest_updates=[
        (
            "Reuters reported that Donald Trump is traveling to Beijing for a summit "
            "with Xi Jinping expected to begin Thursday and continue through Friday."
        ),
        (
            "The summit is expected to take place at Beijing's Temple of Heaven, "
            "giving the meeting strong diplomatic and symbolic significance."
        ),
        (
            "Key agenda items are expected to include trade, agriculture, Boeing aircraft, "
            "AI and semiconductor controls, rare earths, Taiwan, Iran, and maritime security."
        ),
        (
            "Trump stated that he does not need Xi Jinping's help regarding Iran, "
            "although the issue is still expected to be discussed during the visit."
        ),
        (
            "U.S. corporate leaders and global markets are closely monitoring the summit "
            "for signs of commercial agreements or easing of U.S.-China tensions."
        ),
    ]
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
        credits="Report compiled by Jane Doe, Senior Analyst. Data sourced from official statements and reputable news outlets.",
    )   