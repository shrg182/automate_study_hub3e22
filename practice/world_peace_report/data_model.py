#!/usr/bin/env python3
"""Data models for the world peace PDF report."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Final


STATUS_TO_SCORE: Final[dict[str, int]] = {
    "Open window / high risk": 8,
    "Fragile / active": 7,
    "Exploratory / stalled": 6,
    "Active forum / limited enforcement": 5,
}


@dataclass(slots=True, frozen=True)
class NegotiationFront:
    """Represent one negotiation front in the report."""

    name: str
    status: str
    negotiating_picture: str
    near_term_read: str

    @property
    def risk_score(self) -> int:
        """Return a simple risk score for dashboard use."""
        return STATUS_TO_SCORE.get(self.status, 5)


@dataclass(slots=True, frozen=True)
class ReportMetadata:
    """Store top-level metadata for the PDF report."""

    title: str
    subtitle: str
    as_of_date: date
    prepared_for: str = "Situational awareness and discussion"


@dataclass(slots=True)
class ReportContent:
    """Store the body content for the PDF report."""

    metadata: ReportMetadata
    executive_summary: list[str] = field(default_factory=list)
    fronts: list[NegotiationFront] = field(default_factory=list)
    methodology_notes: list[str] = field(default_factory=list)


def build_sample_report() -> ReportContent:
    """Create sample report data for the PDF generator."""
    metadata = ReportMetadata(
        title="Current World Peace Negotiation Report",
        subtitle="A concise geopolitical negotiation dashboard",
        as_of_date=date.today(),
    )

    executive_summary = [
        "Global peace negotiations remain fragmented rather than unified.",
        "Gaza diplomacy is active but fragile, with implementation gaps and recurring violence.",
        "Russia-Ukraine contacts continue, but durable political convergence remains weak.",
        "The Hormuz front is volatile because military incidents can quickly outrun diplomacy.",
        "The UN remains central for coordination and legitimacy, but enforcement power is limited.",
    ]

    fronts = [
        NegotiationFront(
            name="Gaza / Israel-Hamas",
            status="Fragile / active",
            negotiating_picture=(
                "Ceasefire and hostage-related diplomacy remains active through mediators, "
                "but implementation is uneven and broader political settlement remains blocked."
            ),
            near_term_read=(
                "Limited transactional progress is possible, though a durable settlement is still unlikely "
                "without a wider political framework."
            ),
        ),
        NegotiationFront(
            name="Russia-Ukraine",
            status="Exploratory / stalled",
            negotiating_picture=(
                "Channels for negotiation still exist and humanitarian exchanges remain possible, "
                "but the two sides remain far apart on core war-termination terms."
            ),
            near_term_read=(
                "Talks are real, but most near-term outcomes are likely to remain partial, narrow, and reversible."
            ),
        ),
        NegotiationFront(
            name="U.S.-Iran / Hormuz crisis",
            status="Open window / high risk",
            negotiating_picture=(
                "The diplomatic opening is real, yet maritime incidents and military escalation risk can close it quickly."
            ),
            near_term_read=(
                "This front requires constant monitoring because a tactical clash could rapidly reshape the negotiation climate."
            ),
        ),
        NegotiationFront(
            name="UN peace and security diplomacy",
            status="Active forum / limited enforcement",
            negotiating_picture=(
                "The UN remains a central venue for pressure, coordination, humanitarian legitimacy, and public diplomacy."
            ),
            near_term_read=(
                "Expect continued resolutions, meetings, and mediation support, but limited capacity to impose outcomes alone."
            ),
        ),
    ]

    methodology_notes = [
        "This report uses concise qualitative judgments rather than predictive certainty.",
        "Risk scores are lightweight indicators intended for comparison across fronts.",
        "The report structure is designed for daily or weekly refreshes as negotiations evolve.",
    ]

    return ReportContent(
        metadata=metadata,
        executive_summary=executive_summary,
        fronts=fronts,
        methodology_notes=methodology_notes,
    )
