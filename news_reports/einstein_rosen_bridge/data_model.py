#!/usr/bin/env python3
"""
data_model.py

Content model for the Einstein-Rosen Bridge introduction report.
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
class SourceItem:
    """Represent one source used in the report."""

    name: str
    note: str


@dataclass(slots=True)
class ReportSection:
    """Represent one report section."""

    title: str
    paragraphs: list[str]


@dataclass(slots=True)
class ReportContent:
    """Store all report content."""

    title: str
    subtitle: str
    author_line: str
    as_of_date: date
    sections: list[ReportSection]
    vocabulary: list[VocabularyItem]
    sources: list[SourceItem]
    credits: str


def build_report_content() -> ReportContent:
    """Build the Einstein-Rosen Bridge introduction content."""
    sections = [
        ReportSection(
            title="What Is an Einstein-Rosen Bridge?",
            paragraphs=[
                (
                    "The Einstein-Rosen bridge is a theoretical idea from general "
                    "relativity: a mathematical connection between two regions of "
                    "spacetime. It is often described as an early form of the modern "
                    "wormhole concept, though the original bridge was not proposed as "
                    "a practical travel route."
                ),
            ],
        ),
        ReportSection(
            title="The Historical Background: Einstein and Rosen in 1935",
            paragraphs=[
                (
                    "In 1935, Albert Einstein and Nathan Rosen studied whether a "
                    "particle-like structure could be represented without singularities "
                    "by connecting two sheets of spacetime. Their construction became "
                    "known as the Einstein-Rosen bridge."
                ),
            ],
        ),
        ReportSection(
            title="Basic Idea: A Bridge Through Spacetime",
            paragraphs=[
                (
                    "The basic picture is a geometric bridge, or throat, that connects "
                    "two separate regions in the mathematical description of spacetime. "
                    "This does not mean digging a tunnel through ordinary space; it means "
                    "describing a connection inside the structure of spacetime itself."
                ),
            ],
        ),
        ReportSection(
            title="Connection with General Relativity",
            paragraphs=[
                (
                    "The concept matters because it turns gravity from a force acting "
                    "inside space into geometry itself. Instead of picturing a bridge "
                    "as an object placed in the universe, the theory treats the bridge "
                    "as part of the shape of spacetime."
                ),
            ],
        ),
        ReportSection(
            title="Relationship Between Einstein-Rosen Bridges and Black Holes",
            paragraphs=[
                (
                    "The Einstein-Rosen bridge appears when the mathematics of an "
                    "idealized black hole is extended in a symmetric way. In that "
                    "extension, two exterior regions can be connected by a narrow "
                    "geometric throat."
                ),
            ],
        ),
        ReportSection(
            title="Wormholes: The Popular Name and Science-Fiction Image",
            paragraphs=[
                (
                    "In popular language, an Einstein-Rosen bridge is often called a "
                    "wormhole. Science fiction usually imagines wormholes as shortcuts "
                    "for fast travel, but that image is more speculative than the "
                    "original theory."
                ),
            ],
        ),
        ReportSection(
            title="Can Anything Travel Through an Einstein-Rosen Bridge?",
            paragraphs=[
                (
                    "In the original classical model, ordinary matter, light, and "
                    "travelers cannot use the bridge as a stable passageway. The bridge "
                    "is a mathematical connection, but it is not a usable route in the "
                    "simple 1935 form."
                ),
            ],
        ),
        ReportSection(
            title="Why the Original Einstein-Rosen Bridge Is Not Traversable",
            paragraphs=[
                (
                    "The original bridge closes too quickly for anything to cross from "
                    "one side to the other. In standard general relativity, this makes "
                    "it non-traversable: it can exist in the equations without acting "
                    "like an open doorway."
                ),
            ],
        ),
        ReportSection(
            title='Spacetime Curvature and the "Shortcut" Idea',
            paragraphs=[
                (
                    "The shortcut idea comes from curvature. If spacetime can bend, then "
                    "two distant regions might be connected by a shorter geometric path "
                    "in a larger mathematical description, even if they are far apart in "
                    "ordinary space."
                ),
            ],
        ),
        ReportSection(
            title="The Difference Between Mathematical Possibility and Physical Reality",
            paragraphs=[
                (
                    "A solution to Einstein's equations shows mathematical possibility, "
                    "not automatic physical reality. To be physically real, a bridge "
                    "would need conditions that can exist in the universe and survive "
                    "instabilities, quantum effects, and observational tests."
                ),
            ],
        ),
        ReportSection(
            title="Traversable Wormholes and Exotic Matter",
            paragraphs=[
                (
                    "Later theoretical work explored traversable wormholes, but these "
                    "usually require exotic matter or unusual energy conditions to hold "
                    "the throat open. These ideas are mathematically interesting, but "
                    "they remain speculative."
                ),
            ],
        ),
        ReportSection(
            title="Einstein-Rosen Bridges in Modern Physics",
            paragraphs=[
                (
                    "Einstein-Rosen bridges remain useful in modern physics because they "
                    "help researchers think about black holes, quantum gravity, spacetime "
                    "geometry, information, and possible links between gravity and "
                    "quantum entanglement."
                ),
            ],
        ),
        ReportSection(
            title="Einstein-Rosen Bridges in Movies and Popular Culture",
            paragraphs=[
                (
                    "Movies and novels often present wormholes as dramatic gateways "
                    "between stars, galaxies, or times. These stories can be helpful "
                    "for imagination, but they usually simplify or change the physics "
                    "behind the Einstein-Rosen bridge."
                ),
            ],
        ),
        ReportSection(
            title="Common Misunderstandings About Wormholes",
            paragraphs=[
                (
                    "A common misunderstanding is that every wormhole is a proven cosmic "
                    "tunnel. Another is that the Einstein-Rosen bridge automatically "
                    "allows faster-than-light travel. The original bridge is theoretical, "
                    "unstable, and non-traversable."
                ),
            ],
        ),
        ReportSection(
            title="Why Einstein-Rosen Bridges Still Matter",
            paragraphs=[
                (
                    "Einstein-Rosen bridges still matter because they show how strange "
                    "and powerful the geometric view of gravity can be. They connect "
                    "introductory ideas about curvature to deep questions about black "
                    "holes and the structure of the universe."
                ),
            ],
        ),
        ReportSection(
            title="Conclusion: A Fascinating but Unproven Idea",
            paragraphs=[
                (
                    "The Einstein-Rosen bridge is one of the most fascinating ideas to "
                    "come from general relativity. It is not a confirmed path for travel, "
                    "but it remains a valuable way to study how spacetime, black holes, "
                    "and theoretical physics can stretch ordinary intuition."
                ),
            ],
        ),
    ]

    vocabulary = [
        VocabularyItem(
            "general relativity",
            "Einstein's theory that describes gravity as curvature of spacetime.",
        ),
        VocabularyItem(
            "spacetime",
            "The combined four-dimensional framework of space and time.",
        ),
        VocabularyItem(
            "event horizon",
            "A boundary around a black hole beyond which signals cannot escape outward.",
        ),
        VocabularyItem(
            "singularity",
            "A place where a mathematical description predicts extreme or undefined curvature.",
        ),
        VocabularyItem(
            "wormhole",
            "A theoretical connection between separated regions of spacetime.",
        ),
        VocabularyItem(
            "traversable",
            "Able to be crossed by matter, light, or observers in principle.",
        ),
    ]

    sources = [
        SourceItem(
            "Einstein and Rosen, 1935",
            "Original paper introducing the bridge concept in general relativity.",
        ),
        SourceItem(
            "General relativity textbooks",
            "Background on black-hole solutions, horizons, and spacetime curvature.",
        ),
        SourceItem(
            "Modern wormhole literature",
            "Context for later distinctions between non-traversable and traversable wormholes.",
        ),
    ]

    return ReportContent(
        title="Einstein-Rosen Bridge",
        subtitle="An Introduction to the Theory",
        author_line="by Codex",
        as_of_date=date(2026, 5, 22),
        sections=sections,
        vocabulary=vocabulary,
        sources=sources,
        credits=(
            "This educational introduction was generated by Codex"
        ),
    )
