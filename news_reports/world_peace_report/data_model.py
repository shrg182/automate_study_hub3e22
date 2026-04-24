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
    """

    front: str
    status_label: str
    status_key: str
    negotiating_picture: str
    near_term_read: str


@dataclass(slots=True)
class VocabularyItem:
    """
    Represent one vocabulary item drawn from the report text.

    Attributes:
        term:
            The vocabulary word or phrase.
        definition:
            A short learner-friendly meaning.
    """

    term: str
    definition: str


@dataclass(slots=True)
class ReportContent:
    """
    Store the complete content needed to build the report.
    """

    title: str
    subtitle: str
    author_line: str
    as_of_date: date
    executive_summary: list[str]
    fronts: list[NegotiationFront]
    comments: list[str]
    vocabulary: list[VocabularyItem]


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
                "Negotiations remain active but unstable, with a temporary "
                "ceasefire extended amid mutual accusations and continued "
                "military pressure. Planned talks face delays as Iran rejects "
                "negotiations under pressure and demands easing of coercive "
                "measures before meaningful dialogue."
            ),
            near_term_read=(
                "Diplomacy is still possible, but the risk of rapid escalation "
                "remains high if talks stall or military incidents occur."
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

    vocabulary = [
        VocabularyItem(
            term="ceasefire",
            definition="An agreement to stop fighting for a period of time.",
        ),
        VocabularyItem(
            term="mediation",
            definition="The act of helping two sides negotiate and reach an agreement.",
        ),
        VocabularyItem(
            term="compliance",
            definition="Following rules, agreements, or required actions.",
        ),
        VocabularyItem(
            term="governance",
            definition="The system or process of governing and managing an area or institution.",
        ),
        VocabularyItem(
            term="logistics",
            definition="The practical organization of supplies, transport, and operations.",
        ),
        VocabularyItem(
            term="convergence",
            definition="Movement toward the same position or conclusion.",
        ),
        VocabularyItem(
            term="settlement",
            definition="A formal agreement that resolves a dispute or conflict.",
        ),
        VocabularyItem(
            term="coercive",
            definition="Using pressure or force to make someone do something.",
        ),
        VocabularyItem(
            term="escalation",
            definition="An increase in the intensity or seriousness of a conflict.",
        ),
        VocabularyItem(
            term="leverage",
            definition="Power or influence used to affect a situation or negotiation.",
        ),
    ]

    return ReportContent(
        title="Current World Peace Negotiation Report",
        subtitle="A concise geopolitical briefing on active negotiation fronts",
        author_line="by ChatGPT",
        as_of_date=date(2026, 4, 21),
        executive_summary=executive_summary,
        fronts=fronts,
        comments=comments,
        vocabulary=vocabulary,
    )