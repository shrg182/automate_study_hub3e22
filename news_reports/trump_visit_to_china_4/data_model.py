#!/usr/bin/env python3
"""
data_model

Data structures and current content for the Trump China Visit Report.
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
    breaking_news: str
    executive_summary: list[str]
    situation_analysis: list[str]
    latest_updates: list[str]
    risk_assessment: list[str]
    trump_remarks: list[str]
    key_events_timeline: list[str]
    comments: list[str]
    vocabulary: list[VocabularyItem]
    credits: str


def build_sample_report_content() -> ReportContent:
    """
    Build current sample report content.

    Returns:
        ReportContent instance.
    """
    vocabulary = []
    vocabulary.extend([
        VocabularyItem(
            "state visit",
            "An official visit by a national leader to another country."
        ),
        VocabularyItem(
            "summit",
            "A high-level meeting between government leaders."
        ),
        VocabularyItem(
            "delegation",
            "A group of representatives attending official meetings or negotiations."
        ),
        VocabularyItem(
            "Great Hall of the People",
            "The main political assembly building in Beijing used for major state events and diplomatic meetings."
        ),
        VocabularyItem(
            "Temple of Heaven",
            "A historic imperial ceremonial complex in Beijing, also known as Tiantan."
        ),
        VocabularyItem(
            "Tiantan Park",
            "The public park area surrounding the Temple of Heaven in Beijing."
        ),
        VocabularyItem(
            "state banquet",
            "A formal dinner hosted by a government for visiting leaders and delegations."
        ),
        VocabularyItem(
            "Zhongnanhai",
            "The central leadership compound of the Chinese government and Communist Party in Beijing."
        ),
        VocabularyItem(
            "ceremonial diplomacy",
            "The use of symbolic ceremonies and formal events in international relations."
        ),
        VocabularyItem(
            "bilateral relations",
            "Relations between two countries."
        ),
        VocabularyItem(
            "strategic stability",
            "A condition in which major powers avoid serious conflict and maintain balance."
        ),
        VocabularyItem(
            "trade truce",
            "A temporary reduction in trade conflict or tariffs."
        ),
        VocabularyItem(
            "tariffs",
            "Taxes imposed on imported goods."
        ),
        VocabularyItem(
            "rare earths",
            "Strategic minerals used in electronics, defense systems, and advanced technology."
        ),
        VocabularyItem(
            "semiconductor",
            "A material or microchip used in electronic and computing devices."
        ),
        VocabularyItem(
            "export controls",
            "Government restrictions on the export of sensitive technologies or products."
        ),
        VocabularyItem(
            "market access",
            "The ability to sell goods or services within a foreign market."
        ),
        VocabularyItem(
            "maritime security",
            "Security related to oceans, shipping routes, and naval activities."
        ),
        VocabularyItem(
            "Taiwan issue",
            "The political and security dispute concerning Taiwan's status and cross-strait relations."
        ),
        VocabularyItem(
            "Strait of Hormuz",
            "A strategically important waterway connecting the Persian Gulf to global shipping routes."
        ),
        VocabularyItem(
            "symbolic diplomacy",
            "Diplomatic actions designed mainly to convey political meaning or goodwill."
        ),
        VocabularyItem(
            "leader-level diplomacy",
            "Direct diplomatic engagement between national leaders."
        ),
        VocabularyItem(
            "commercial agreement",
            "A business or trade arrangement between companies or governments."
        ),
        VocabularyItem(
            "preliminary agreement",
            "An initial agreement reached before final negotiations are completed."
        ),
        VocabularyItem(
            "geopolitical rivalry",
            "Competition between countries for power, influence, or strategic advantage."
        ),
        VocabularyItem(
            "Indo-Pacific",
            "The geopolitical region spanning the Indian and Pacific Oceans."
        ),
        VocabularyItem(
            "supply chain",
            "The network used to produce and distribute goods."
        ),
        VocabularyItem(
            "diplomatic leverage",
            "Political or economic influence used during negotiations."
        ),
        VocabularyItem(
            "strategic competition",
            "Long-term rivalry between major powers across economic, military, and political areas."
        ),
    ])

    return ReportContent(
        title="Trump China Visit Report",
        author_line="By ChatGPT",
        as_of_date=date.today(),
        breaking_news=(
            "President Donald Trump conducted a state visit to Beijing from May 13 to May 15, 2026, "
            "marking his first trip to China since leaving office in 2021. The visit included high-level "
            "summit meetings with Chinese President Xi Jinping, ceremonial events, and discussions on "
            "trade, Taiwan, Iran, and regional security. Both leaders emphasized cooperation and stability, "
            "although major disagreements remain on key issues."
        ),
        executive_summary=[
            (
                "Trump's 2026 visit to China was a significant diplomatic event that combined symbolic ceremony, "
                "commercial negotiation, and strategic messaging during a period of continued U.S.-China rivalry."
            ),
        ],
        situation_analysis=[
            (
                "The visit emphasized personal leader-to-leader diplomacy, particularly through events at the "
                "Great Hall of the People, the Temple of Heaven, and Zhongnanhai."
            ),
        ],
        latest_updates=[
            (
                "Although both governments highlighted cooperation and stability, major disagreements remain over "
                "Taiwan, semiconductor restrictions, trade policy, maritime security, and geopolitical influence."
            ),
        ],
        risk_assessment=[
            (
                "The participation of major American corporate leaders demonstrated the importance of economic interests "
                "and supply-chain access in shaping modern U.S.-China relations."
            ),
        ],

        key_events_timeline=[
            (
                "May 11, 2026 — China officially confirmed that President Donald Trump "
                "would conduct a state visit to Beijing from May 13 to May 15."
            ),

            (
                "May 13, 2026 — Air Force One departed the United States for Beijing, "
                "accompanied by senior government officials, security personnel, and "
                "a large delegation of American business leaders."
            ),

            (
                "May 14, 2026 — Trump arrived in Beijing for his first China visit "
                "since 2017 and was formally welcomed by Chinese officials."
            ),

            (
                "May 14, 2026 — Trump and Xi Jinping held opening talks at the "
                "Great Hall of the People in Beijing, discussing trade, Taiwan, "
                "Iran, technology controls, rare earths, and regional security."
            ),

            (
                "May 14, 2026 — Xi Jinping warned that mishandling the Taiwan issue "
                "could lead to serious confrontation between the two countries."
            ),

            (
                "May 14, 2026 — Trump stated that U.S.-China relations could become "
                "'better than ever' if both sides pursue practical cooperation."
            ),

            (
                "May 14, 2026 — Trump and Xi jointly visited Beijing's Temple of Heaven "
                "(Tiantan Park), where the summit adopted a strong ceremonial and "
                "symbolic diplomatic atmosphere."
            ),

            (
                "May 14, 2026 — The two leaders attended a state banquet in Beijing "
                "featuring traditional Chinese state hospitality and formal diplomatic events."
            ),

            (
                "May 14, 2026 — Trump invited Xi Jinping to visit the White House "
                "on September 24, 2026, to continue leader-level diplomacy."
            ),

            (
                "May 15, 2026 — Trump and Xi held second-day summit discussions focused "
                "on tariffs, Boeing aircraft purchases, semiconductor export controls, "
                "agricultural trade, investment access, and maritime security."
            ),

            (
                "May 15, 2026 — Xi Jinping gave Trump a rare guided walk through "
                "Zhongnanhai, the central Chinese leadership compound, in what analysts "
                "described as a significant gesture of personal diplomacy."
            ),

            (
                "May 15, 2026 — Trump stated that China had agreed to purchase "
                "200 Boeing aircraft, with possible future purchases reaching "
                "up to 750 aircraft, although final details remained unclear."
            ),

            (
                "May 15, 2026 — Trump stated that China would purchase billions "
                "of dollars in American agricultural products under preliminary trade understandings."
            ),

            (
                "May 15, 2026 — Discussions also addressed Iran, with Trump stating "
                "that Iran must not obtain nuclear weapons and that the Strait of Hormuz "
                "should remain open."
            ),

            (
                "May 15, 2026 — Reuters reported that the summit produced warm rhetoric "
                "and symbolic diplomatic progress but only limited concrete breakthroughs."
            ),

            (
                "May 15, 2026 — Trump departed Beijing and returned to Washington "
                "following the conclusion of the two-day summit."
            ),

            (
                "May 16, 2026 — Chinese officials described several trade and investment "
                "understandings reached during the summit as 'preliminary' and subject "
                "to further negotiation."
            ),

            (
                "May 17, 2026 — Chinese aviation regulators reportedly met with "
                "executives from Boeing and GE Aerospace following Trump's visit, "
                "signaling continued commercial discussions after the summit."
            ),
        ],
        trump_remarks=[
            (
                "Trump described the U.S.-China relationship as "
                "'very strong' during his opening meeting with Xi Jinping in Beijing."
            ),
            (
                "Trump stated that he believes relations between the United States "
                "and China could become 'better than ever' if both sides pursue "
                "practical cooperation."
            ),
            (
                "During discussions on Taiwan, Trump reportedly said he remained "
                "undecided regarding future U.S. arms sales packages to Taiwan, "
                "calling the issue part of broader negotiations with Beijing."
            ),
            (
                "Trump said he and Xi Jinping discussed Boeing aircraft purchases, "
                "Taiwan, Iran, trade relations, and regional stability during the summit."
            ),
            (
                "Trump claimed China agreed to purchase 200 Boeing aircraft and "
                "possibly hundreds more in future agreements, although final details "
                "had not yet been publicly confirmed."
            ),
            (
                "Trump stated that China committed to purchasing at least "
                "$17 billion annually in U.S. agricultural products "
                "for multiple years."
            ),
            (
                "On Iran, Trump said he did not require Xi Jinping's assistance "
                "but welcomed China's role in maintaining stability and reopening "
                "the Strait of Hormuz."
            ),
            (
                "Trump praised the ceremonial arrangements in Beijing, including "
                "the Temple of Heaven visit and the Zhongnanhai leadership compound tour, "
                "calling the relationship with Xi Jinping 'warm' and respectful."
            ),
            (
                "Trump invited Xi Jinping to visit the White House later in 2026 "
                "to continue leader-level diplomacy."
            ),
            (
                "At the conclusion of the visit, Trump described the summit as "
                "productive and historic while acknowledging that negotiations "
                "on trade, tariffs, and technology issues would continue."
            ),
        ],
        comments=[
            (
                "Trump's 2026 Beijing visit combined symbolic diplomacy, commercial negotiation, "
                "and strategic messaging during a period of continued U.S.-China rivalry."
            ),

            (
                "The visit emphasized ceremony and personal leader-to-leader diplomacy, "
                "particularly through events at the Great Hall of the People, "
                "the Temple of Heaven, and Zhongnanhai."
            ),

            (
                "Although both governments highlighted cooperation and stability, "
                "major disagreements remain over Taiwan, semiconductor restrictions, "
                "trade policy, maritime security, and geopolitical influence."
            ),

            (
                "The participation of major American corporate leaders demonstrated the "
                "importance of economic interests and supply-chain access in shaping "
                "modern U.S.-China relations."
            ),

            (
                "Trump's public remarks focused heavily on trade, Boeing aircraft sales, "
                "agricultural exports, and economic opportunities for American companies."
            ),

            (
                "Xi Jinping placed greater emphasis on strategic stability, sovereignty, "
                "and Taiwan-related concerns during the summit discussions."
            ),

            (
                "The Temple of Heaven visit served as a highly symbolic diplomatic moment, "
                "designed to project historical continuity, mutual respect, and controlled "
                "stability between the two countries."
            ),

            (
                "Analysts generally viewed the summit as successful in reducing immediate "
                "tensions and improving communication, although few concrete long-term "
                "breakthroughs were announced."
            ),

            (
                "The summit reflected a broader international trend in which economic "
                "competition, technology policy, national security, and diplomacy are "
                "increasingly interconnected."
            ),

            (
                "Despite warm public rhetoric from both leaders, the long-term strategic "
                "competition between the United States and China is expected to continue."
            ),
        ],
        vocabulary=vocabulary,

        credits=(
            "This report combines AI-generated factual content from ChatGPT with analytical structuring "
            "designed for educational and informational purposes. Current-event details should be checked "
            "against primary or reputable news sources before publication."
        ),
    )
