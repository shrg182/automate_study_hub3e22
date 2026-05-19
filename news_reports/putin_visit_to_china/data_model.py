#!/usr/bin/env python3
"""
data_model.py

Data structures and current content for the Putin China Visit Report.
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
    url: str


@dataclass(slots=True)
class ReportContent:
    """Store all report content."""

    title: str
    author_line: str
    as_of_date: date
    lead: str
    latest_updates: list[str]
    key_themes: dict[str, list[str]]
    international_comments: dict[str, list[str]]
    vocabulary: list[VocabularyItem]
    sources: list[SourceItem]
    credits: str


def build_sample_report_content() -> ReportContent:
    """
    Build current sample report content.

    Returns:
        ReportContent instance.
    """

    vocabulary = [
        VocabularyItem(
            "strategic partnership",
            "A close long-term relationship based on shared diplomatic, economic, and security goals.",
        ),
        VocabularyItem(
            "multipolar world",
            "A global order in which power is spread among several major countries or blocs.",
        ),
        VocabularyItem(
            "Western sanctions",
            "Restrictions imposed by Western governments to pressure another country.",
        ),
        VocabularyItem(
            "energy exports",
            "Oil, gas, and related products sold to another country.",
        ),
        VocabularyItem(
            "diplomatic balancing",
            "Managing ties with competing powers without fully choosing one side.",
        ),
        VocabularyItem(
            "trade dependence",
            "A situation in which one country relies heavily on another for imports, exports, or markets.",
        ),
        VocabularyItem(
            "geopolitical signal",
            "A public action meant to show political alignment or influence.",
        ),
        VocabularyItem(
            "strategic stability",
            "A condition in which major powers try to reduce the risk of direct conflict.",
        ),
    ]

    sources = [
        SourceItem(
            "AP News, May 19, 2026",
            "https://apnews.com/article/0c0086341e9694122a49fb7054b41d97",
        ),
        SourceItem(
            "Chinese State Council / Xinhua, May 19, 2026",
            "https://english.www.gov.cn/news/202605/19/content_WS6a0c8342c6d00ca5f9a0b1b8.html",
        ),
        SourceItem(
            "Le Monde, May 19, 2026",
            "https://www.lemonde.fr/en/international/article/2026/05/19/putin-meets-with-xi-to-strengthen-deeply-unbalanced-relations_6753593_4.html",
        ),
    ]

    return ReportContent(
        title="Putin China Visit Report",
        author_line="By ChatGPT",
        as_of_date=date(2026, 5, 19),
        lead=(
            "Russian President Vladimir Putin arrived in Beijing on May 19, 2026, "
            "for a two-day state visit with Chinese President Xi Jinping. The visit "
            "comes less than a week after President Donald Trump's Beijing summit, "
            "making China the center of overlapping U.S., Russian, and Chinese diplomacy."
        ),
        latest_updates=[
            (
                "Chinese state media reported that Putin arrived in Beijing on Tuesday night "
                "and is visiting China from May 19 to 20 at Xi's invitation."
            ),
            (
                "AP reported that the trip is being watched for how Beijing preserves its "
                "close relationship with Moscow while also seeking stable relations with Washington."
            ),
            (
                "Russian officials described the trip as focused on strengthening the "
                "comprehensive partnership and strategic cooperation between Russia and China."
            ),
            (
                "Energy and trade are central topics, with Russia remaining an important "
                "supplier of oil and gas to China under continuing Western sanctions."
            ),
        ],
        key_themes={
            "China-Russia Alignment": [
                (
                    "The visit reinforces the image of a durable China-Russia partnership "
                    "built around opposition to Western pressure and support for a more multipolar order."
                ),
                (
                    "Both governments are likely to emphasize sovereignty, strategic trust, "
                    "and leader-level coordination."
                ),
            ],
            "China's Diplomatic Balancing": [
                (
                    "The timing places Beijing in a delicate position: it wants useful ties "
                    "with Moscow without undermining recent efforts to stabilize U.S.-China relations."
                ),
                (
                    "China can present itself as a major diplomatic platform by hosting "
                    "the American and Russian presidents within the same week."
                ),
            ],
            "Economic Dependence": [
                (
                    "Russia relies heavily on Chinese markets, technology channels, and "
                    "energy demand as sanctions limit its access to many Western economies."
                ),
                (
                    "China benefits from Russian energy supplies but remains careful about "
                    "secondary-sanctions risk and its broader global trade interests."
                ),
            ],
            "Ukraine War Context": [
                (
                    "The war in Ukraine remains the central backdrop to Western concerns "
                    "about China-Russia cooperation."
                ),
                (
                    "The visit is unlikely to remove the structural divide between Russia "
                    "and Western governments over Ukraine, sanctions, and European security."
                ),
            ],
        },
        international_comments={
            "China": [
                (
                    "Chinese official messaging emphasized the state-visit format and the "
                    "importance of high-level China-Russia engagement."
                ),
                (
                    "Beijing is likely to frame the visit as normal major-power diplomacy "
                    "rather than a move aimed at any third country."
                ),
            ],
            "Russia": [
                (
                    "Moscow views the visit as proof that Russia is not isolated and still "
                    "has a powerful diplomatic and economic partner."
                ),
                (
                    "Russian officials are expected to highlight energy sales, trade growth, "
                    "and strategic coordination."
                ),
            ],
            "United States": [
                (
                    "Washington will likely watch for signs that China is giving Russia "
                    "economic or technological support that weakens sanctions pressure."
                ),
                (
                    "The visit also tests whether China can separate its Russia policy from "
                    "recent efforts to keep U.S.-China communication channels open."
                ),
            ],
            "Europe": [
                (
                    "European governments are likely to interpret the summit through the "
                    "lens of Ukraine, sanctions enforcement, energy markets, and NATO security."
                ),
                (
                    "Some European analysts see the relationship as increasingly unequal, "
                    "with Moscow needing Beijing more than Beijing needs Moscow."
                ),
            ],
        },
        vocabulary=vocabulary,
        sources=sources,
        credits=(
            "This report is an AI-generated educational summary based on public reporting "
            "available as of May 19, 2026. Current-event details should be checked against "
            "primary or reputable news sources before publication."
        ),
    )
