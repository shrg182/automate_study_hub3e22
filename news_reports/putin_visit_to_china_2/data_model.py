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


def build_report_content() -> ReportContent:
    """
    Build the current report content.

    Returns:
        ReportContent instance.
    """

    vocabulary = [
        VocabularyItem(
            "comprehensive strategic coordination",
            "China and Russia's official term for close diplomatic, economic, and security cooperation.",
        ),
        VocabularyItem(
            "Good-Neighborliness Treaty",
            "The 2001 China-Russia friendship treaty that frames long-term cooperation between the two countries.",
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
            "secondary sanctions",
            "Penalties aimed at third parties that help a sanctioned country or entity evade restrictions.",
        ),
        VocabularyItem(
            "supply-chain stability",
            "The ability of trade and industrial networks to keep goods and inputs moving during shocks.",
        ),
        VocabularyItem(
            "geopolitical signal",
            "A public action meant to show political alignment or influence.",
        ),
    ]

    sources = [
        SourceItem(
            "AP News, May 20, 2026",
            "https://apnews.com/article/china-russia-putin-xi-5b7304bc1604cbb7135cb96f217b8b3e",
        ),
        SourceItem(
            "Chinese State Council / Xinhua, May 20, 2026",
            "https://english.www.gov.cn/news/202605/20/content_WS6a0d3e8fc6d00ca5f9a0b1de.html",
        ),
        SourceItem(
            "Chinese State Council / Xinhua, May 20, 2026",
            "https://english.www.gov.cn/news/202605/20/content_WS6a0d280fc6d00ca5f9a0b1c9.html",
        ),
        SourceItem(
            "Chinese State Council / Xinhua, May 19, 2026",
            "https://english.www.gov.cn/news/202605/19/content_WS6a0c8342c6d00ca5f9a0b1b8.html",
        ),
    ]

    return ReportContent(
        title="Putin China Visit Report",
        author_line="By ChatGPT",
        as_of_date=date(2026, 5, 20),
        lead=(
            "Russian President Vladimir Putin met Chinese President Xi Jinping in Beijing "
            "on May 20, 2026, during a May 19-20 state visit. The talks highlighted the "
            "strength of China-Russia ties only days after President Donald Trump's visit "
            "to China, placing Beijing at the center of overlapping U.S., Russian, and "
            "Chinese diplomacy."
        ),
        latest_updates=[
            (
                "Xi hosted a welcome ceremony for Putin outside the Great Hall of the People "
                "on Wednesday morning before formal talks in Beijing."
            ),
            (
                "AP reported that the two leaders oversaw more than 40 cooperation agreements "
                "covering areas including trade, technology, and media exchanges."
            ),
            (
                "The two sides agreed to extend the 2001 Treaty of Good-Neighborliness and "
                "Friendly Cooperation, a core legal framework for the bilateral relationship."
            ),
            (
                "Energy remained the clearest economic pillar: Russian officials said oil "
                "exports to China rose 35% in the first quarter of 2026, while no visible "
                "breakthrough was reported on the proposed Power of Siberia 2 gas pipeline."
            ),
            (
                "Xi used the meeting to criticize unilateralism and call for a more just "
                "global governance system, while also calling for an immediate end to Middle "
                "East hostilities because of risks to energy supplies and trade."
            ),
        ],
        key_themes={
            "China-Russia Alignment": [
                (
                    "The visit reinforced a durable partnership built around opposition to "
                    "Western pressure, support for a more multipolar order, and leader-level "
                    "coordination."
                ),
                (
                    "Official Chinese messaging tied the meeting to the 30th anniversary of "
                    "the China-Russia strategic partnership of coordination and the 25th "
                    "anniversary of the 2001 friendship treaty."
                ),
            ],
            "China's Diplomatic Balancing": [
                (
                    "The timing keeps Beijing in a delicate position: it is maintaining close "
                    "ties with Moscow while also trying to preserve a more stable channel with "
                    "Washington after Trump's state visit."
                ),
                (
                    "Hosting both the American and Russian presidents within days lets China "
                    "project itself as a central diplomatic platform, but it also sharpens "
                    "outside scrutiny of how Beijing manages competing relationships."
                ),
            ],
            "Energy And Trade": [
                (
                    "China is Russia's top trading partner, and Russian oil and gas remain "
                    "important to China's energy mix while Western sanctions limit Moscow's "
                    "other options."
                ),
                (
                    "The absence of visible progress on Power of Siberia 2 suggests that the "
                    "energy partnership is strong but still shaped by pricing, infrastructure, "
                    "and bargaining-power questions."
                ),
            ],
            "Ukraine And Sanctions Context": [
                (
                    "The war in Ukraine remains the central backdrop to Western concern about "
                    "China-Russia cooperation, especially any support that could weaken "
                    "sanctions pressure."
                ),
                (
                    "China continues to present itself as neutral on Ukraine while deepening "
                    "trade and diplomatic coordination with Moscow."
                ),
            ],
            "Middle East Crisis": [
                (
                    "The leaders linked their talks to the wider global security environment, "
                    "including energy and supply-chain risks from the Middle East conflict."
                ),
                (
                    "This framing helps both governments portray China-Russia coordination as "
                    "a stabilizing force, even as Western governments view the partnership "
                    "with suspicion."
                ),
            ],
        },
        international_comments={
            "China": [
                (
                    "Chinese official messaging emphasized high-level strategic coordination, "
                    "long-term treaty ties, and the need for a more just global governance system."
                ),
                (
                    "Beijing is likely to frame the visit as normal major-power diplomacy and "
                    "as evidence that China can maintain relationships with rival powers."
                ),
            ],
            "Russia": [
                (
                    "Moscow can use the visit to show that Russia is not isolated and still "
                    "has a powerful economic and diplomatic partner."
                ),
                (
                    "Russian messaging is likely to highlight energy sales, trade resilience, "
                    "and foreign-policy coordination at a time of sanctions pressure."
                ),
            ],
            "United States": [
                (
                    "Washington will likely watch for signs that China is helping Russia gain "
                    "access to technology, finance, or trade channels restricted by sanctions."
                ),
                (
                    "The meeting tests whether the recent Xi-Trump diplomatic thaw can coexist "
                    "with Beijing's continued partnership with Moscow."
                ),
            ],
            "Europe": [
                (
                    "European governments are likely to interpret the summit through Ukraine, "
                    "sanctions enforcement, energy markets, and NATO security."
                ),
                (
                    "Many European analysts see the relationship as increasingly unequal, with "
                    "Moscow needing Beijing more than Beijing needs Moscow."
                ),
            ],
            "Global South": [
                (
                    "Some non-Western governments may see the visit as another signal that "
                    "China and Russia are trying to build alternatives to Western-led systems."
                ),
                (
                    "Others may welcome calls for stability while remaining cautious about "
                    "being drawn into great-power competition."
                ),
            ],
        },
        vocabulary=vocabulary,
        sources=sources,
        credits=(
            "This report is an AI-generated educational summary based on public reporting "
            "available as of May 20, 2026. Current-event details should be checked against "
            "primary or reputable news sources before publication."
        ),
    )


def build_sample_report_content() -> ReportContent:
    """Backward-compatible alias for older generator code."""

    return build_report_content()

