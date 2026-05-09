#!/usr/bin/env python3
"""
data_model

Data structures and content for the Trump China Visit Report.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class VocabularyItem:
    """A single item in the report's vocabulary."""


    term: str
    definition: str


@dataclass(slots=True)
class ReportContent:
    """
    Store all report content.
    """

    title: str
    author_line: str
    as_of_date: date
    breaking_news: str
    executive_summary: list[str]
    situation_analysis: list[str]
    latest_updates: list[str]
    risk_assessment: list[str]
    comments: list[str] 
    vocabulary: list[VocabularyItem]
    credits: str


def build_sample_report_content() -> ReportContent:
    """
    Build a sample report content instance.
    
    Returns:

        ReportContent: A sample report content instance.
    """

    vocabulary = [
        VocabularyItem(
            "bilateral relations",
            "Relations between two countries."
        ),
        VocabularyItem(
            "trade negotiations",
            "Discussions aimed at reaching agreements on trade policies."
        ),
        VocabularyItem(
            "economic sanctions",
            "Penalties imposed on a country to influence its behavior."
        ),
        VocabularyItem(
            "geopolitical",
            "Related to international politics and global power"
        ),
        VocabularyItem(
            "strategic rivalry",
            "Competition for influence and power between states.complex"
        ),
        VocabularyItem(
            "supply chain",
            "The system used to produce and distribute goods."
        ),
        VocabularyItem(
            "Indo-Pacific",
            "The region spanning the Indian and Pacific Oceans."
        ),
        VocabularyItem(
            "diplomatic engagement",
            "Efforts to communicate and negotiate with other countries."
        ),
        VocabularyItem(
            "stabilize",
            "To make a situation more steady or less tense."
        ),
        VocabularyItem(
            "maritime security",
            "Security related to oceans and sea routes."
        )
    ]

    return ReportContent(
        title="Trump China Visit Report",
        author_line="By ChatGPT",
        as_of_date=date(2026, 5, 9),
        breaking_news=(
            "Donald Trump is expected to visit China next week for high-level talks with Chinese leaders. This visit comes amid ongoing tensions between the two countries over trade, technology, and geopolitical issues."
            "The visit is seen as an opportunity to ease tensions and explore potential areas of cooperation, but it also carries risks given the current state of bilateral relations."
            "Key topics likely to be discussed include trade negotiations, economic sanctions, and regional security in the Indo-Pacific. Both sides will be looking to stabilize relations while also addressing their strategic rivalry."
            "The outcome of this visit could have significant implications for global geopolitics and the future of US-China relations."
        )
        executive_summary=[
            "Trump's visit to China is a significant diplomatic event that could reshape US-China relations.",
            "The visit comes at a time of heightened tensions, with ongoing disputes over trade, technology, and regional security.",
            "Key issues on the agenda include trade negotiations, economic sanctions, and geopolitical competition in the Indo-Pacific.",
            "While there are opportunities for cooperation, there are also risks that the visit could exacerbate tensions if not handled carefully.",
            "The outcome of this visit will be closely watched by global leaders and could have far-reaching implications for international relations."
        ],
        situation_analysis=[
            (
                "Analysts view the potential visit as an attempt to stabilize "
                "bilateral relations amid ongoing tensions. However, the success of the visit will depend on the willingness of both sides to engage in constructive dialogue and make concessions on key issues."  
            )
            (
                "The talks are expected to focus on economic cooperation, "
                "Technology policy, and military communication mechanisms."
            )
            (
                "There is also speculation that the visit could lead to a temporary easing of economic sanctions, but this will likely be contingent on progress in trade negotiations and other areas of cooperation."
            )
        ],
        risk_assessment=[
            "The visit carries risks, including the possibility of increased tensions if the talks do not go well or if there are disagreements on key issues. There is also a risk that the visit could be used for domestic political purposes by either side, which could further complicate the situation."
            "However, if handled successfully, the visit could lead to a thaw in relations and open the door for future cooperation on global issues such as climate change, public health, and regional security."
            "Overall, the visit is a high-stakes diplomatic event that will require careful navigation of complex issues and competing interests."
        ],
        comments=[
            "This visit is a critical moment for US-China relations and will be closely watched by the international community. It has the potential to either ease tensions or exacerbate them, depending on how the talks unfold and the willingness of both sides to find common ground."
        ],
        vocabulary=vocabulary,
        credits=(
            "Report generated by ChatGPT, a language model developed by OpenAI. "
            "Data and analysis are based on publicly available information as of May 9, 2026."  
        )
    )