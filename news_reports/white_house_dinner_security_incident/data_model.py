#!/usr/bin/env python3
"""
data_model.py

Data structures and content for the security incident report.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class NewsItem:
    title: str
    content: str


@dataclass(slots=True)
class VocabularyItem:
    term: str
    definition: str


@dataclass(slots=True)
class ReportContent:
    title: str
    author_line: str
    as_of_date: date
    news: list[NewsItem]
    executive_summary: list[str]
    risk_assessment: list[str]
    comments: list[str]
    vocabulary: list[VocabularyItem]


def build_sample_report_content() -> ReportContent:
    news = [
        NewsItem(
            title="Security Incident at Correspondents' Dinner",
            content=(
                "A suspected assassination attempt disrupted a correspondents’ dinner "
                "attended by Donald Trump. An armed individual was intercepted by "
                "security personnel near the venue and detained without injuries to "
                "Donald Trump.\n\n"
                "The incident triggered emergency protocols and a temporary suspension "
                "of the event. Authorities are currently investigating the suspect’s "
                "motives and the broader security implications."
            ),
        ),
        NewsItem(
            title="Authorities Respond to Security Breach",
            content=(
                "Following the incident, law enforcement agencies have increased security "
                "measures around high-profile events. The suspect is being questioned, "
                "and authorities are reviewing surveillance footage and security logs to "
                "assess how the breach occurred and whether it was an isolated attempt."
            ),
        ),
        NewsItem(
            title="Public Reaction and Security Concerns",
            content=(
                "The public has expressed concern over the security breach, with many "
                "calling for enhanced protective measures at political events. Security "
                "experts are analyzing the incident to identify potential vulnerabilities and "
                "recommend improvements to prevent future occurrences."
            ),
        ),
        NewsItem(
            title="Political Implications of the Incident",
            content=(
                "The incident has sparked political debate regarding the safety of public figures and "
                "the effectiveness of current security protocols. Some politicians are advocating for "
                "increased funding for security agencies, while others are calling for a review of event security strategies."
            ),
        ),
        NewsItem(
            title="Ongoing Investigation and Future Precautions",
            content=(
                "The investigation into the security incident is ongoing, with authorities seeking to determine the suspect’s motives and any potential connections to larger threats. Security agencies are also evaluating current protocols and considering additional measures to enhance protection at future events."
            ),
        ),
        NewsItem(
            title="Latest Updates",
            content=(
                "Authorities have identified the suspect as Cole Tomas Allen, 31, and investigators are examining writings reportedly sent to family members before the attack. According to Reuters, President Donald Trump and First Lady Melania Trump were rushed from the White House Correspondents’ Association dinner on April 25, 2026, after a man opened fire with a shotgun on security personnel; Reuters also reported that investigators are focused on how the weapon was brought into the Washington Hilton. The Washington Post reported that the suspect’s writings criticized the Trump administration and suggested an intent to target people connected to it. Trump has urged the WHCA to reschedule the dinner within 30 days, while the incident has intensified debate over security at large presidential events. "
            ),
        ),
    ]

    executive_summary = [
        "A security breach occurred near a high-profile political event.",
        "The suspect was intercepted before reaching the protected perimeter.",
        "No casualties were reported due to rapid security response.",
        "The incident highlights vulnerabilities in outer security layers.",
    ]

    risk_assessment = [
        "Risk level: Elevated",
        "Threat type: Suspected lone actor",
        "Security performance: Effective interception, no penetration",
        "Outlook: Continued risk of similar low-scale attempts",
    ]

    comments = [
        "This incident underscores the importance of layered security at high-profile events.",
        "The breach suggests potential gaps in early detection or perimeter control.",
        "Further investigation is needed to determine whether the suspect acted alone.",
    ]

    vocabulary = [
        VocabularyItem("assassination attempt", "An effort to kill an important public figure."),
        VocabularyItem("intercepted", "Stopped before reaching a target."),
        VocabularyItem("detained", "Held by authorities for investigation."),
        VocabularyItem("protocol", "An official security procedure."),
        VocabularyItem("breach", "A failure or gap in security."),
        VocabularyItem("perimeter", "The outer boundary of a protected area."),
        VocabularyItem("vulnerability", "A weakness that can be exploited."),
        VocabularyItem("lone actor", "An individual acting without support from a group."),
        VocabularyItem("elevated risk", "A higher-than-normal level of threat."),
        VocabularyItem("outlook", "An assessment of future conditions or risks."),
        VocabularyItem("layered security", "A system using multiple levels of protection."),
        VocabularyItem("surveillance", "Close monitoring for security purposes."),
        VocabularyItem("subdued", "Brought under control by force."),
        VocabularyItem("implication", "A possible consequence or effect."),
    ]

    return ReportContent(
        title="White House Dinner Security Incident Report",
        author_line="by ChatGPT",
        as_of_date=date(2026, 4, 27),
        news=news,
        executive_summary=executive_summary,
        risk_assessment=risk_assessment,
        comments=comments,
        vocabulary=vocabulary,
    )