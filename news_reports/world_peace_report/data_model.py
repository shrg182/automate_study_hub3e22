#!/usr/bin/env python3
"""
data_model.py

Data models and sample report content for the World Peace Report module.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class NegotiationFront:
    """
    Represent one negotiation front in the report.

    Attributes:
        front:
            Name of the conflict, diplomatic front, or negotiation area.
        status_label:
            Human-readable status label shown in the dashboard table.
        status_key:
            Style key used to color the status label.
            Expected values include:
            - "fragile"
            - "stalled"
            - "high_risk"
            - "active"
        negotiating_picture:
            Brief description of the current negotiation situation.
        near_term_read:
            Short forward-looking analyst comment.
    """

    front: str
    status_label: str
    status_key: str
    negotiating_picture: str
    near_term_read: str


@dataclass(slots=True)
class ReportContent:
    """
    Store the complete content needed to build the report.

    Attributes:
        title:
            Main report title.
        subtitle:
            Secondary title line.
        author_line:
            Attribution line shown beneath the title.
        as_of_date:
            Report date.
        executive_summary:
            Short summary bullets or paragraphs.
        fronts:
            List of negotiation fronts shown in the main dashboard.
        comments:
            Additional analyst comments shown near the end of the report.
    """

    title: str
    subtitle: str
    author_line: str
    as_of_date: date
    executive_summary: list[str]
    fronts: list[NegotiationFront]
    comments: list[str]


def build_sample_report_content() -> ReportContent:
    """
    Return sample report content for PDF generation.

    This sample content matches the type of report you were building:
    a concise geopolitical briefing with a negotiation dashboard and
    short analyst comments.

    Returns:
        A ReportContent instance with sample negotiation data.
    """
    fronts = [
        NegotiationFront(
            front="Gaza / Israel-Hamas",
            status_label="Fragile / active",
            status_key="fragile",
            negotiating_picture=(
                "A ceasefire framework remains diplomatically relevant, "
                "but implementation gaps, renewed violence, and disputes "
                "over sequencing continue to limit durable progress."
            ),
            near_term_read=(
                "Limited transactional progress is still possible, but a "
                "broader political settlement remains blocked."
            ),
        ),
        NegotiationFront(
            front="Russia-Ukraine",
            status_label="Exploratory / stalled",
            status_key="stalled",
            negotiating_picture=(
                "Talks and diplomatic signals continue, but there is still "
                "little evidence of substantive convergence on end-state terms."
            ),
            near_term_read=(
                "The diplomatic track appears real, but concrete outcomes "
                "remain thin in the near term."
            ),
        ),
        NegotiationFront(
            front="U.S.-Iran / Hormuz crisis",
            status_label="Open window / high risk",
            status_key="high_risk",
            negotiating_picture=(
                "A diplomatic opening exists, but escalation pressure remains "
                "high and any new maritime or regional security incident could "
                "sharply reduce negotiation space."
            ),
            near_term_read=(
                "The opening is meaningful, but also vulnerable. One clash "
                "could shut the window quickly."
            ),
        ),
        NegotiationFront(
            front="UN peace and security diplomacy",
            status_label="Active forum / limited enforcement",
            status_key="active",
            negotiating_picture=(
                "The UN remains central for legitimacy, messaging, and "
                "coordination, but enforcement power continues to lag behind "
                "the scale of active crises."
            ),
            near_term_read=(
                "The UN remains important for pressure, coordination, and "
                "process support, even when it cannot impose outcomes."
            ),
        ),
    ]

    executive_summary = [
        "Global peace negotiations remain fragmented rather than unified.",
        "The most active diplomacy is still issue-specific and region-specific.",
        "Ceasefire efforts can produce temporary relief, but durable political "
        "settlements remain difficult.",
        "Negotiation windows currently exist, yet trust deficits and battlefield "
        "or regional escalation risks continue to constrain progress.",
    ]

    comments = [
        (
            "This report is designed as a situational-awareness briefing rather "
            "than a definitive forecast. It summarizes negotiation dynamics in "
            "a compact format for study and discussion."
        ),
        (
            "The status labels are qualitative. They are meant to help readers "
            "compare negotiation fronts quickly, not replace detailed country- "
            "or conflict-level analysis."
        ),
        (
            "A practical next step for this module would be to separate the "
            "sample data from the presentation layer so the report can later "
            "pull live data from APIs, feeds, or manually maintained JSON files."
        ),
    ]

    return ReportContent(
        title="Current World Peace Negotiation Report",
        subtitle="A concise geopolitical briefing on active negotiation fronts",
        author_line="by ChatGPT",
        as_of_date=date.today(),
        executive_summary=executive_summary,
        fronts=fronts,
        comments=comments,
    )