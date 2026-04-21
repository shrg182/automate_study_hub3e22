#!/usr/bin/env python3
"""
data_model.py

Data models and current sample content for the World Peace Report module.
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
            Style key used to color the status cell.
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
            Short summary bullets.
        fronts:
            Negotiation fronts shown in the dashboard table.
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

    Returns:
        A ReportContent instance with current sample negotiation data.
    """
    fronts = [
        NegotiationFront(
            front="Gaza / Israel-Hamas",
            status_label="Fragile / active",
            status_key="fragile",
            negotiating_picture=(
                "Fighting and implementation disputes continue, but diplomacy "
                "has widened beyond ceasefire mechanics to include governance, "
                "humanitarian access, reconstruction logistics, and postwar "
                "administrative arrangements."
            ),
            near_term_read=(
                "Short-term progress is still possible, but the track remains "
                "fragile and heavily dependent on sequencing, compliance, and "
                "outside mediation."
            ),
        ),
        NegotiationFront(
            front="Russia-Ukraine",
            status_label="Exploratory / constrained",
            status_key="stalled",
            negotiating_picture=(
                "Negotiation signals still exist, but there is little public "
                "evidence of strong convergence on a final political settlement. "
                "The war context continues to limit diplomatic momentum."
            ),
            near_term_read=(
                "The channel is real, but near-term outcomes still appear narrow "
                "and more tactical than transformative."
            ),
        ),
        NegotiationFront(
            front="U.S.-Iran / Hormuz",
            status_label="Open channel / high risk",
            status_key="high_risk",
            negotiating_picture=(
                "Talks remain active, but the ceasefire timeline, distrust, and "
                "competing regional interests keep the situation unstable. Gulf "
                "states are openly concerned that talks could validate Iranian "
                "Hormuz leverage without resolving wider security threats."
            ),
            near_term_read=(
                "Diplomacy remains possible, but one maritime or regional shock "
                "could sharply narrow the negotiating space."
            ),
        ),
        NegotiationFront(
            front="UN peace diplomacy",
            status_label="Active forum / limited leverage",
            status_key="active",
            negotiating_picture=(
                "The UN continues to support ceasefires and negotiations across "
                "multiple fronts, stressing that there is no military solution, "
                "but it still relies on member-state political will for outcomes."
            ),
            near_term_read=(
                "The UN remains important for legitimacy, pressure, and process, "
                "but not decisive by itself."
            ),
        ),
    ]

    executive_summary = [
        "Global peace diplomacy remains fragmented and crisis-specific rather than unified.",
        "The Gaza track is still the most operationally active, with negotiation now extending into reconstruction and governance questions.",
        "Russia-Ukraine diplomacy continues, but visible movement toward a final settlement remains limited.",
        "U.S.-Iran talks remain open, yet Hormuz-related risk and regional distrust continue to constrain confidence.",
    ]

    comments = [
        "This report is a situational-awareness briefing and not a prediction model.",
        "Status labels are qualitative and designed for fast comparison across fronts.",
        "A strong next improvement would be to separate live news input from layout code so the report can refresh itself automatically.",
    ]

    return ReportContent(
        title="Current World Peace Negotiation Report",
        subtitle="A concise geopolitical briefing on active negotiation fronts",
        author_line="by ChatGPT",
        as_of_date=date(2026, 4, 21),
        executive_summary=executive_summary,
        fronts=fronts,
        comments=comments,
    )