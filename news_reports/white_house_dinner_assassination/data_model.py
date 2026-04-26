#!/usr/bin/env python3
"""
data_model.py

Data models for the report content, and a function to build sample content for testing and development.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class NewsItem:
    """
    Represent a breaking news item.
    """
    title: str
    content: str


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
    news: list[NewsItem]
    title: str
    subtitle: str
    author_line: str
    as_of_date: date
    executive_summary: list[str]
    comments: list[str]
    vocabulary: list[VocabularyItem]


def build_sample_report_content() -> ReportContent:
    """
    Build sample content for testing and development.
    """
    news = [
        NewsItem(
            title="Security Incident at Correspondents Dinner",
            content=(
                "A suspected assassination attempt disrupted a correspondents’ dinner "
                "attended by Donald Trump after an armed individual was intercepted by "
                "security personnel near the venue. The suspect was detained without "
                "injuring the former president, though the incident triggered emergency "
                "protocols and a temporary suspension of the event. Authorities are "
                "investigating the motives and security implications of the breach."
            ),
        )
    ]

    executive_summary = [
        "An armed individual was intercepted by security personnel near the venue of a correspondents’ dinner attended by Donald Trump.",
        "The suspect was detained without injuring the former president.",
        "The incident triggered emergency protocols and a temporary suspension of the event.",
        "Authorities are investigating the motives and security implications of the breach.",
    ]

    comments = [
        "This incident raises significant concerns about the security measures in place for high-profile events.",
        "The motives behind the suspect's actions are still unclear, and the investigation is ongoing.",
        "The temporary suspension of the event highlights the seriousness of the threat and the need for swift response protocols."
    ]

    vocabulary = [
        VocabularyItem(
            term="Assassination Attempt",
            definition="An act of trying to kill a prominent person, often for political reasons."
        ),
        VocabularyItem(
            term="Security Personnel",
            definition="Individuals responsible for ensuring the safety and security of people and property."
        ),
        VocabularyItem(
            term="Emergency Protocols",
            definition="Pre-established procedures to follow in case of an emergency situation."
        ),
        VocabularyItem(
            term="Detained",
            definition="To keep someone in custody, typically by law enforcement authorities."
        )
    ]

    return ReportContent(
        title="Breaking News: Security Incident at Correspondents Dinner",
        subtitle="An armed individual was intercepted near the venue of a correspondents’ dinner attended by Donald Trump.",
        author_line="By Jane Doe, Senior Security Correspondent",
        as_of_date=date.today(),
        news=news,
        executive_summary=executive_summary,
        comments=comments,
        vocabulary=vocabulary
    )
