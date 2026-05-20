#!/usr/bin/env python3
"""
data_model.py

Current content for the Putin visit to China news report.
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
    sections: dict[str, ReportSection]
    vocabulary: list[VocabularyItem]
    sources: list[SourceItem]
    credits: str


def build_report_content() -> ReportContent:
    """
    Build current report content.

    Returns:
        ReportContent instance.
    """

    sections = {
        "Breaking News / Leads": ReportSection(
            title="Breaking News / Leads",
            paragraphs=[
                (
                    "Russian President Vladimir Putin met Chinese President Xi Jinping "
                    "at the Great Hall of the People in Beijing on May 20, 2026, during "
                    "a two-day state visit that began the night before."
                ),
                (
                    "The summit came only days after U.S. President Donald Trump's visit "
                    "to China, putting Beijing at the center of a rapid sequence of major "
                    "power diplomacy."
                ),
                (
                    "Xi and Putin oversaw more than 40 cooperation agreements, agreed to "
                    "extend the 2001 China-Russia Treaty of Good-Neighborliness and "
                    "Friendly Cooperation, and highlighted growing trade and energy ties."
                ),
            ],
        ),
        "Key Themes": ReportSection(
            title="Key Themes",
            paragraphs=[
                (
                    "Strategic alignment: China and Russia used the visit to present a "
                    "united front against Western pressure and to promote a more multipolar "
                    "international order."
                ),
                (
                    "Energy dependence: Russia needs Chinese demand for oil and gas while "
                    "sanctions restrict its access to many Western markets. China benefits "
                    "from Russian energy supplies but retains bargaining leverage."
                ),
                (
                    "Diplomatic balancing: Beijing is trying to preserve its partnership "
                    "with Moscow while also keeping U.S.-China communication channels stable "
                    "after Trump's Beijing trip."
                ),
                (
                    "Treaty continuity: The extension of the 2001 friendship treaty signals "
                    "that both governments want the relationship framed as long-term and "
                    "institutional, not merely tactical."
                ),
            ],
        ),
        "Executive Summary": ReportSection(
            title="Executive Summary",
            paragraphs=[
                (
                    "Putin's May 19-20 visit to China strengthened the public image of a "
                    "close China-Russia partnership at a moment of global instability. The "
                    "leaders emphasized strategic trust, trade, energy cooperation, and "
                    "shared criticism of unilateralism."
                ),
                (
                    "The meeting produced symbolic and practical outcomes: a treaty extension, "
                    "a joint statement on strategic coordination, and more than 40 cooperation "
                    "documents. The most important economic theme remained energy, especially "
                    "Russian oil and gas exports to China."
                ),
                (
                    "The visit does not remove underlying asymmetry. Russia has fewer major "
                    "economic options because of the Ukraine war and Western sanctions, while "
                    "China can deepen ties with Moscow without fully sacrificing other global "
                    "trade and diplomatic priorities."
                ),
            ],
        ),
        "Situation Analysis": ReportSection(
            title="Situation Analysis",
            paragraphs=[
                (
                    "China and Russia framed the summit around anniversaries: 30 years since "
                    "the establishment of their strategic partnership of coordination and 25 "
                    "years since the 2001 Good-Neighborliness treaty. This gave the meeting a "
                    "formal historical frame and helped both sides present continuity."
                ),
                (
                    "Economic cooperation is substantial. AP cited Xinhua data that bilateral "
                    "trade reached about $228 billion in 2025, and Russian officials said oil "
                    "exports to China rose 35% in the first quarter of 2026."
                ),
                (
                    "There was no visible breakthrough on the proposed Power of Siberia 2 gas "
                    "pipeline, a reminder that China-Russia energy cooperation still depends "
                    "on price, route, financing, and bargaining power."
                ),
                (
                    "The Ukraine war remains the main external pressure point. China says it "
                    "is neutral, but Western governments continue to scrutinize Chinese trade "
                    "and technology flows that may help Russia withstand sanctions."
                ),
            ],
        ),
        "Latest Updates": ReportSection(
            title="Latest Updates",
            paragraphs=[
                (
                    "Xi hosted Putin with a welcome ceremony and formal talks at the Great "
                    "Hall of the People on Wednesday, May 20."
                ),
                (
                    "The two leaders signed or witnessed documents on strategic coordination, "
                    "good-neighborly cooperation, trade, technology, media, and people-to-people "
                    "exchanges."
                ),
                (
                    "Chinese official statements said the two sides would pursue higher-quality "
                    "coordination and make the global governance system more just and reasonable."
                ),
                (
                    "Xi called for an early end to Middle East hostilities, citing risks to "
                    "energy supply, supply chains, and international trade."
                ),
                (
                    "Putin departed after the meetings, and he invited Xi to visit Russia in "
                    "2027 while saying he would attend the APEC summit in southern China in "
                    "November."
                ),
            ],
        ),
        "Risk Assessment": ReportSection(
            title="Risk Assessment",
            paragraphs=[
                (
                    "Sanctions risk: Expanded Russia-China trade may attract more Western "
                    "scrutiny, especially if goods, finance, or technology are seen as helping "
                    "Russia's military-industrial base."
                ),
                (
                    "Energy risk: Middle East instability could increase demand for Russian "
                    "energy, but pipeline delays and price disputes may limit how quickly the "
                    "relationship can expand."
                ),
                (
                    "Diplomatic risk: Beijing's simultaneous engagement with Washington and "
                    "Moscow may become harder to balance if the United States or Europe imposes "
                    "new restrictions related to Russia."
                ),
                (
                    "Strategic risk: A tighter China-Russia front can deepen bloc politics, "
                    "make Ukraine diplomacy more difficult, and sharpen pressure on countries "
                    "trying to avoid choosing sides."
                ),
            ],
        ),
        "Comments": ReportSection(
            title="Comments",
            paragraphs=[
                (
                    "China's comment: Official Chinese messaging described the relationship "
                    "as high-level, stable, and based on political trust, non-alliance, "
                    "non-confrontation, and not targeting any third party."
                ),
                (
                    "Russia's comment: Putin portrayed energy cooperation as a driving force "
                    "of the relationship and emphasized that China-Russia coordination is a "
                    "stabilizing factor internationally."
                ),
                (
                    "Western view: U.S. and European policymakers are likely to focus less on "
                    "ceremony and more on whether Chinese trade helps Russia evade sanctions "
                    "or sustain the war in Ukraine."
                ),
                (
                    "Analyst view: The summit strengthened symbolism, but the lack of visible "
                    "Power of Siberia 2 progress shows that the partnership still contains "
                    "hard bargaining beneath the friendly rhetoric."
                ),
            ],
        ),
        "New Vocabulary": ReportSection(
            title="New Vocabulary",
            paragraphs=[],
        ),
        "Sources": ReportSection(
            title="Sources",
            paragraphs=[],
        ),
        "Credits": ReportSection(
            title="Credits",
            paragraphs=[],
        ),
    }

    vocabulary = [
        VocabularyItem(
            "comprehensive strategic coordination",
            "China and Russia's phrase for close political, diplomatic, economic, and security cooperation.",
        ),
        VocabularyItem(
            "Good-Neighborliness Treaty",
            "The 2001 treaty that provides a long-term legal and diplomatic basis for China-Russia relations.",
        ),
        VocabularyItem(
            "multipolar world",
            "A global order in which power is distributed among several major states or blocs.",
        ),
        VocabularyItem(
            "unilateralism",
            "A policy approach in which one country acts on its own rather than through shared rules or institutions.",
        ),
        VocabularyItem(
            "secondary sanctions",
            "Penalties placed on third parties that help a sanctioned country evade restrictions.",
        ),
        VocabularyItem(
            "Power of Siberia 2",
            "A proposed natural gas pipeline intended to carry more Russian gas to China.",
        ),
        VocabularyItem(
            "supply-chain stability",
            "The ability of production and shipping networks to keep goods moving during shocks.",
        ),
        VocabularyItem(
            "geopolitical signal",
            "A public diplomatic action meant to show alignment, influence, or resolve.",
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
            "Xinhua, May 20, 2026",
            "https://english.news.cn/20260520/e179fde59cdc4d2dbe36d2e9bcd08c85/c.html",
        ),
        SourceItem(
            "Chinese Ministry of Foreign Affairs, May 20, 2026",
            "https://www.fmprc.gov.cn/mfa_eng/xw/zyxw/202605/t20260520_11914662.html",
        ),
    ]

    return ReportContent(
        title="Putin Visit to China News Report",
        subtitle="State visit to Beijing, May 19-20, 2026",
        author_line="By ChatGPT",
        as_of_date=date(2026, 5, 20),
        sections=sections,
        vocabulary=vocabulary,
        sources=sources,
        credits=(
            "This AI-generated educational news report was prepared from public reporting "
            "and official statements available as of May 20, 2026. It follows the section "
            "requirements listed in news_report_request_list.csv."
        ),
    )

