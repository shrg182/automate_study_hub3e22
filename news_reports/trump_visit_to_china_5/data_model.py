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
    breaking_news: str
    executive_summary: list[str]
    situation_analysis: list[str]
    international_comments: dict
    domestic_us_comments: dict
    vocabulary: list[str]
    chatgpt_comments: list[str]
    appendices: list[dict]


def build_sample_report_content() -> ReportContent:
    """
    Build current sample report content.

    Returns:
        ReportContent instance.
    """
    vocabulary = []
    vocabulary.extend([
        VocabularyItem(
            "strategic stability",
            "A condition in which major powers avoid serious conflict and maintain balance."
        ),
        VocabularyItem(
            "bilateral relations",
            "Relations and interactions between two countries."
        ),
        VocabularyItem(
            "Indo-Pacific",
            "The geopolitical region spanning the Indian and Pacific Oceans."
        ),
        VocabularyItem(
            "geopolitical risk",
            "The possibility that international political events may affect economic or security conditions."
        ),
        VocabularyItem(
            "trade exposure",
            "The degree to which an economy or company depends on international trade."
        ),
        VocabularyItem(
            "supply chain",
            "The network used to produce, transport, and distribute goods."
        ),
        VocabularyItem(
            "market access",
            "The ability to sell products or services in a foreign market."
        ),
        VocabularyItem(
            "maritime security",
            "Security involving oceans, sea routes, shipping, and naval activity."
        ),
        VocabularyItem(
            "Strait of Hormuz",
            "A strategically important waterway connecting the Persian Gulf to global shipping routes."
        ),
        VocabularyItem(
            "diplomatic leverage",
            "Political or economic influence used during negotiations."
        ),
        VocabularyItem(
            "symbolic diplomacy",
            "Diplomatic actions intended mainly to convey political meaning or goodwill."
        ),
        VocabularyItem(
            "strategic breakthrough",
            "A major achievement that significantly changes geopolitical relations."
        ),
        VocabularyItem(
            "commercial opportunity",
            "A chance to expand business activity or economic gain."
        ),
        VocabularyItem(
            "financial market",
            "A system where financial assets such as stocks, bonds, and currencies are traded."
        ),
        VocabularyItem(
            "cautious optimism",
            "Hopefulness combined with careful concern about possible risks."
        ),
        VocabularyItem(
            "ceremonial diplomacy",
            "The use of formal ceremonies and symbolic events in international relations."
        ),
        VocabularyItem(
            "regional stability",
            "A stable political and security situation within a geographic region."
        ),
        VocabularyItem(
            "technology dependence",
            "Reliance on another country or company for important technologies."
        ),
        VocabularyItem(
            "strategic rivalry",
            "Long-term competition between countries for power and influence."
        ),
        VocabularyItem(
            "international commentary",
            "Public analysis or opinions expressed by foreign governments, analysts, or media."
        ),
    ])

    return ReportContent(
        title="Trump China Visit Report"
        author_line="By ChatGPT"
        as_of_date=date(2026, 5, 18)
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
        }

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
        }
        chatgpt_comments=[

            (
                "The 2026 Trump-China summit demonstrated that both Washington and Beijing "
                "remain willing to maintain direct leader-level communication despite "
                "continuing strategic rivalry."
            ),

            (
                "Much of the visit focused on symbolic diplomacy, including the Temple of Heaven "
                "and Zhongnanhai events, which projected stability and mutual respect while "
                "reducing immediate political tension."
            ),

            (
                "The participation of major American corporate leaders highlighted the growing "
                "connection between geopolitics, technology competition, finance, manufacturing, "
                "and global supply chains."
            ),

            (
                "Trade and commercial issues appeared to provide the most realistic area for "
                "short-term cooperation, particularly in aviation, agriculture, semiconductors, "
                "financial services, and market access."
            ),

            (
                "Taiwan remained the most sensitive and strategically dangerous issue discussed "
                "during the summit, with both governments attempting to avoid escalation while "
                "maintaining their core political positions."
            ),

            (
                "The summit suggested that the United States and China are entering a period "
                "of managed competition rather than direct confrontation or full strategic partnership."
            ),

            (
                "The discussions regarding Iran and the Strait of Hormuz demonstrated how "
                "U.S.-China relations are increasingly connected to broader global security issues "
                "beyond East Asia."
            ),

            (
                "The visit produced strong diplomatic imagery and warmer public rhetoric, "
                "but relatively few fully confirmed long-term agreements."
            ),

            (
                "International reactions generally viewed the summit as stabilizing in the "
                "short term, although most analysts do not expect deep structural disagreements "
                "between the two countries to disappear."
            ),

            (
                "Overall, the visit reflected the modern reality that economic competition, "
                "national security, advanced technology, and diplomacy are now deeply interconnected "
                "within global politics."
            ),
        ]
        appendices=[
            {
                "title": "Appendix A — Major Topics Discussed During the Summit",
                "content": [
                    "Trade and tariffs",
                    "Semiconductor export controls",
                    "Artificial intelligence and advanced technology",
                    "Rare earth exports and supply chains",
                    "Taiwan and Indo-Pacific security",
                    "Maritime security and naval stability",
                    "Iran and the Strait of Hormuz",
                    "Agricultural exports and Boeing aircraft purchases",
                    "Financial-market access and investment",
                    "Leader-level diplomacy and strategic stability",
                ],
            },

            {
                "title": "Appendix B — Major Locations Visited",
                "content": [
                    "Beijing Capital International Airport",
                    "Great Hall of the People",
                    "Temple of Heaven (Tiantan Park)",
                    "Zhongnanhai leadership compound",
                    "State banquet venues in Beijing",
                ],
            },

            {
                "title": "Appendix C — Major American Business Delegation Members",
                "content": [
                    "Elon Musk — Tesla and SpaceX",
                    "Tim Cook — Apple",
                    "Jensen Huang — Nvidia",
                    "Kelly Ortberg — Boeing",
                    "Larry Fink — BlackRock",
                    "Stephen Schwarzman — Blackstone",
                    "Jane Fraser — Citigroup",
                    "Michael Miebach — Mastercard",
                    "Ryan McInerney — Visa",
                    "Cristiano Amon — Qualcomm",
                    "Larry Culp — GE Aerospace",
                    "Brian Sikes — Cargill",
                ],
            },

            {
                "title": "Appendix D — Key Diplomatic Themes",
                "content": [
                    "Strategic stability",
                    "Managed competition",
                    "Economic interdependence",
                    "Technology rivalry",
                    "Supply-chain resilience",
                    "Symbolic diplomacy",
                    "Regional security",
                    "Market access negotiations",
                ],
            },

            {
                "title": "Appendix E — Frequently Referenced Terms",
                "content": [
                    "Indo-Pacific",
                    "Taiwan issue",
                    "Strategic rivalry",
                    "Trade truce",
                    "Export controls",
                    "Rare earths",
                    "Market access",
                    "Geopolitical risk",
                    "Leader-level diplomacy",
                    "Ceremonial diplomacy",
                ],
            },

            {
                "title": "Appendix F — Summary Assessment",
                "content": [
                    (
                        "The 2026 Trump-China summit reduced immediate diplomatic tensions "
                        "and improved communication channels between Washington and Beijing."
                    ),
                    (
                        "The visit achieved symbolic diplomatic success but produced "
                        "limited confirmed long-term strategic breakthroughs."
                    ),
                    (
                        "Economic cooperation remains possible in selected sectors despite "
                        "continuing geopolitical rivalry."
                    ),
                    (
                        "Taiwan remains the most sensitive issue affecting long-term "
                        "U.S.-China stability."
                    ),
                ],
            },
        ]
    )


def _build_appendices_section(report, styles) -> list:
    """
    Build appendices section.
    """
    story = [
        Paragraph()
    ]
