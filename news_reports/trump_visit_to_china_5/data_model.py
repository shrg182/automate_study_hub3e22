#!/usr/bin/env python3
"""
data_model

Data structures and current contents for the Trump China Visit Report

TODO:
    - Add dataclasses, i.e. Vocabulary and ReportContent.
    - Add data model parts.
    - Add main program logic.
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
class ReportContent:
    """Store all report content."""

    title: str
    author_line: str
    as_of_date: date
    international_comments: dict
    domestic_us_comments: dict
    vocabulary: list[VocabularyItem]


def build_sample_report_content() -> ReportContent:
    """
    Build current sample report content.

    Returns:
        ReportContent instance.
    """
    vocabulary = [
        VocabularyItem(
            "strategic stability",
            "A balance that helps major powers avoid serious conflict."
        ),
        VocabularyItem(
            "bilateral relations",
            "Political, economic, and security ties between two countries."
        ),
        VocabularyItem(
            "Indo-Pacific",
            "The region linking the Indian and Pacific Oceans."
        ),
        VocabularyItem(
            "strategic rivalry",
            "Long-term competition between countries for power and influence."
        ),
        VocabularyItem(
            "market access",
            "The ability to sell goods or services in another country's market."
        ),
        VocabularyItem(
            "maritime security",
            "Protection of sea routes, shipping, and naval activity."
        ),
        VocabularyItem(
            "diplomatic leverage",
            "Influence used to gain advantage in negotiations."
        ),
        VocabularyItem(
            "symbolic diplomacy",
            "Ceremonies or gestures used to send a political message."
        ),
        VocabularyItem(
            "cautious optimism",
            "Hopefulness mixed with concern about possible risks."
        ),
        VocabularyItem(
            "supply chain",
            "The network that produces, transports, and delivers goods."
        ),
    ]

    return ReportContent(
        title="Trump China Visit Report",
        author_line="By ChatGPT",
        as_of_date=date(2026, 5, 18),
        international_comments={
            "Asia": {
                "China": [
                    (
                        "Chinese officials described the summit as constructive and "
                        "emphasized the importance of strategic stability in "
                        "U.S.-China relations."
                    ),
                    (
                        "Chinese state media highlighted the symbolism of the Temple "
                        "of Heaven and Zhongnanhai events as signs of diplomatic respect "
                        "and continuity."
                    ),
                    (
                        "Beijing stressed that Taiwan remains the most sensitive issue "
                        "in bilateral relations."
                    ),
                ],

                "Taiwan": [
                    (
                        "Taiwanese officials expressed concern regarding Trump's remarks "
                        "on Taiwan arms sales and future U.S. policy."
                    ),
                    (
                        "Taiwan emphasized the importance of maintaining strong "
                        "security cooperation with the United States."
                    ),
                ],

                "Japan": [
                    (
                        "Japanese officials welcomed continued U.S.-Japan alliance "
                        "commitments following the Beijing summit."
                    ),
                    (
                        "Tokyo remained focused on Indo-Pacific security and regional stability."
                    ),
                ],
            },

            "Europe": {
                "European Union": [
                    (
                        "European analysts viewed the summit positively in terms of "
                        "short-term stability but remained cautious about long-term tensions."
                    ),
                    (
                        "European governments continue to monitor technology dependence "
                        "and trade exposure involving China."
                    ),
                ],

                "Germany": [
                    (
                        "German financial analysts viewed the summit as reducing "
                        "short-term geopolitical risk."
                    ),
                    (
                        "Investors cautiously welcomed the calmer diplomatic atmosphere."
                    ),
                ],

                "United Kingdom": [
                    (
                        "British commentators described the summit as an important "
                        "signal that Washington and Beijing continue to maintain "
                        "direct communication channels."
                    ),
                ],
            },

            "Middle East": {
                "Iran": [
                    (
                        "Iranian observers closely monitored discussions involving "
                        "sanctions, oil trade, and the Strait of Hormuz."
                    ),
                    (
                        "Some analysts argued that China gained diplomatic leverage "
                        "because of continuing Middle East instability."
                    ),
                ],

                "Saudi Arabia": [
                    (
                        "Gulf-region observers focused on energy markets, oil shipping routes, "
                        "and maritime security."
                    ),
                ],
            },

            "North America": {
                "Canada": [
                    (
                        "Canadian analysts viewed the summit as economically important "
                        "because of its impact on North American supply chains."
                    ),
                ],
            },
        },

        domestic_us_comments={
            "Republican Supporters": [
                (
                    "Republican allies praised Trump's direct diplomacy with Xi Jinping "
                    "and highlighted possible economic gains from the summit."
                ),
                (
                    "Supporters emphasized Boeing aircraft sales, agriculture exports, "
                    "and improved commercial opportunities."
                ),
            ],

            "Democratic Critics": [
                (
                    "Democratic critics argued that the summit produced symbolic gestures "
                    "without major strategic breakthroughs."
                ),
                (
                    "Some Democrats expressed concern regarding uncertainty over Taiwan policy."
                ),
            ],

            "Business Community": [
                (
                    "American corporate leaders welcomed the summit and hoped for "
                    "expanded market access in China."
                ),
                (
                    "Technology, aviation, finance, agriculture, and semiconductor sectors "
                    "closely monitored the negotiations."
                ),
            ],

            "Financial Markets": [
                (
                    "Global investors reacted with cautious optimism following the summit."
                ),
                (
                    "Markets welcomed reduced tensions but remained uncertain about "
                    "long-term strategic outcomes."
                ),
            ],

            "American Media": [
                (
                    "American media coverage emphasized the contrast between strong "
                    "ceremonial diplomacy and limited concrete breakthroughs."
                ),
                (
                    "Several commentators described the visit as symbolically successful "
                    "but strategically unresolved."
                ),
            ],
        },
        vocabulary=vocabulary,
    )
