#!/usr/bin/env python3
"""
data_model.py

Current content for the Cuba Crisis news report.
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
    Build the report content.

    Returns:
        ReportContent instance.
    """

    sections = {
        "Breaking News / Leads": ReportSection(
            title="Breaking News / Leads",
            paragraphs=[
                (
                    "The Cuban Missile Crisis brought the United States and the Soviet Union "
                    "to the edge of nuclear war in October 1962 after U.S. reconnaissance "
                    "photographs revealed Soviet nuclear missile sites under construction in Cuba."
                ),
                (
                    "President John F. Kennedy responded with a naval 'quarantine' of Cuba, "
                    "publicly demanding the removal of the missiles while his advisers debated "
                    "air strikes, invasion, diplomacy, and blockade enforcement."
                ),
                (
                    "The immediate crisis eased on October 28, 1962, when Soviet leader Nikita "
                    "Khrushchev agreed to remove the missiles from Cuba in exchange for a U.S. "
                    "pledge not to invade Cuba and a secret U.S. commitment to remove Jupiter "
                    "missiles from Turkey."
                ),
            ],
        ),
        "Key Themes": ReportSection(
            title="Key Themes",
            paragraphs=[
                (
                    "Nuclear brinkmanship: The crisis showed how quickly intelligence, military "
                    "movement, and political pressure could push nuclear powers toward war."
                ),
                (
                    "Controlled escalation: Kennedy chose a quarantine before air strikes or "
                    "invasion, creating space for diplomacy while still applying pressure."
                ),
                (
                    "Back-channel diplomacy: Public threats were paired with private messages "
                    "and secret concessions that gave both leaders a way to step back."
                ),
                (
                    "Cuba's security dilemma: Fidel Castro's government wanted protection after "
                    "the Bay of Pigs invasion, but the settlement was largely negotiated by "
                    "Washington and Moscow."
                ),
                (
                    "Cold War lessons: The near catastrophe encouraged later crisis-management "
                    "measures, including improved communication between Washington and Moscow."
                ),
            ],
        ),
        "Executive Summary": ReportSection(
            title="Executive Summary",
            paragraphs=[
                (
                    "The Cuban Missile Crisis was a 13-day confrontation in October 1962 over "
                    "Soviet nuclear missiles deployed in Cuba, about 90 miles from Florida. It "
                    "became the most dangerous direct U.S.-Soviet confrontation of the Cold War."
                ),
                (
                    "The United States discovered the missile sites through U-2 aerial photography "
                    "and announced a naval quarantine on October 22. Soviet ships approached the "
                    "quarantine line while both sides exchanged public warnings and private messages."
                ),
                (
                    "The crisis ended through a negotiated settlement: Soviet missiles would leave "
                    "Cuba, the United States would not invade Cuba, and U.S. Jupiter missiles in "
                    "Turkey would be removed quietly. The episode remains a core case study in "
                    "nuclear risk, intelligence, and crisis leadership."
                ),
            ],
        ),
        "Situation Analysis": ReportSection(
            title="Situation Analysis",
            paragraphs=[
                (
                    "The crisis grew from several pressures: the failed 1961 Bay of Pigs invasion, "
                    "Cuba's search for security, Soviet efforts to alter the strategic balance, "
                    "and U.S. concern that offensive weapons in Cuba would threaten hemispheric "
                    "security and domestic political confidence."
                ),
                (
                    "On October 16, 1962, Kennedy was informed that reconnaissance photographs "
                    "showed Soviet missile installations. For nearly a week, the administration "
                    "deliberated in secret through the Executive Committee of the National Security "
                    "Council, known as ExComm."
                ),
                (
                    "On October 22, Kennedy addressed the nation, announced the quarantine, and "
                    "warned that any nuclear missile launched from Cuba against the Western Hemisphere "
                    "would be treated as an attack by the Soviet Union."
                ),
                (
                    "October 27 was the most dangerous day: a U-2 was shot down over Cuba, another "
                    "U-2 strayed over Soviet territory, and U.S. leaders received conflicting Soviet "
                    "messages. Restraint on both sides prevented rapid escalation."
                ),
                (
                    "The final settlement removed the immediate missile threat but left important "
                    "questions about alliance politics, Cuban sovereignty, nuclear deterrence, and "
                    "the hidden risks of military alerts."
                ),
            ],
        ),
        "Latest Updates": ReportSection(
            title="Latest Updates",
            paragraphs=[
                (
                    "October 14, 1962: A U-2 reconnaissance flight photographed Soviet missile "
                    "sites under construction in Cuba."
                ),
                (
                    "October 16, 1962: Kennedy was briefed on the missile evidence, beginning "
                    "the intense decision period remembered as the 'thirteen days.'"
                ),
                (
                    "October 22, 1962: Kennedy publicly announced the missile discovery and "
                    "ordered a naval quarantine of Cuba."
                ),
                (
                    "October 27, 1962: U.S. pilot Major Rudolf Anderson was killed when his U-2 "
                    "was shot down over Cuba, marking the crisis's deadliest moment."
                ),
                (
                    "October 28, 1962: Khrushchev announced that Soviet missiles would be removed "
                    "from Cuba. The U.S. quarantine formally ended on November 20 after verification "
                    "and removal steps."
                ),
            ],
        ),
        "Risk Assessment": ReportSection(
            title="Risk Assessment",
            paragraphs=[
                (
                    "Nuclear war risk: The crisis created multiple pathways to nuclear use, "
                    "including misread military movements, unauthorized local action, and pressure "
                    "for retaliation after the U-2 shootdown."
                ),
                (
                    "Command-and-control risk: Leaders did not fully control every battlefield "
                    "event, and later evidence showed the danger of tactical nuclear weapons and "
                    "submarine encounters unknown to some decision-makers at the time."
                ),
                (
                    "Political risk: Kennedy faced pressure to appear firm, Khrushchev faced "
                    "pressure not to retreat humiliatingly, and Castro feared another U.S. invasion."
                ),
                (
                    "Alliance risk: NATO allies, Turkey, and Latin American governments were "
                    "affected by decisions that were partly public and partly secret."
                ),
                (
                    "Long-term risk: The crisis demonstrated that deterrence can prevent war but "
                    "also produce moments where errors or accidents could have catastrophic effects."
                ),
            ],
        ),
        "Comments": ReportSection(
            title="Comments",
            paragraphs=[
                (
                    "U.S. view: Kennedy framed the missiles as an unacceptable offensive threat "
                    "to the Western Hemisphere and used the quarantine to combine force, law, and "
                    "diplomacy."
                ),
                (
                    "Soviet view: Khrushchev sought to protect Cuba, strengthen Soviet leverage, "
                    "and respond to U.S. strategic advantages, including U.S. missiles positioned "
                    "near the Soviet Union."
                ),
                (
                    "Cuban view: Castro's government saw the missiles through the lens of survival "
                    "after the Bay of Pigs and continuing U.S. hostility, but Cuba had limited control "
                    "over the final U.S.-Soviet settlement."
                ),
                (
                    "Historical view: The crisis is now remembered as both a success of restraint "
                    "and a warning about how close nuclear-armed states can come to disaster."
                ),
            ],
        ),
        "New Vocabulary": ReportSection(title="New Vocabulary", paragraphs=[]),
        "Sources": ReportSection(title="Sources", paragraphs=[]),
        "Credits": ReportSection(title="Credits", paragraphs=[]),
    }

    vocabulary = [
        VocabularyItem(
            "quarantine",
            "The term Kennedy used for the naval restriction around Cuba; it avoided the legal implications of declaring a blockade.",
        ),
        VocabularyItem(
            "blockade",
            "A military action that prevents ships or goods from entering or leaving an area, often treated as an act of war.",
        ),
        VocabularyItem(
            "ExComm",
            "The Executive Committee of the National Security Council, Kennedy's core advisory group during the crisis.",
        ),
        VocabularyItem(
            "U-2",
            "A high-altitude reconnaissance aircraft used by the United States to photograph Soviet missile sites in Cuba.",
        ),
        VocabularyItem(
            "brinkmanship",
            "The practice of pushing a dangerous confrontation close to disaster to gain advantage or force concessions.",
        ),
        VocabularyItem(
            "deterrence",
            "The strategy of preventing attack by making the likely cost of attack too high.",
        ),
        VocabularyItem(
            "back channel",
            "A private or unofficial communication path used alongside formal diplomacy.",
        ),
        VocabularyItem(
            "Jupiter missiles",
            "U.S. medium-range ballistic missiles deployed in Turkey and Italy during the Cold War.",
        ),
    ]

    sources = [
        SourceItem(
            "John F. Kennedy Presidential Library and Museum",
            "https://www.jfklibrary.org/learn/about-jfk/jfk-in-history/cuban-missile-crisis",
        ),
        SourceItem(
            "U.S. Department of State, Office of the Historian",
            "https://history.state.gov/milestones/1961-1968/cuban-missile-crisis",
        ),
        SourceItem(
            "National Archives",
            "https://www.archives.gov/publications/prologue/2002/fall/cuban-missiles.html",
        ),
        SourceItem(
            "Encyclopaedia Britannica",
            "https://www.britannica.com/event/Cuban-missile-crisis",
        ),
        SourceItem(
            "The National Archives, United Kingdom",
            "https://www.nationalarchives.gov.uk/education/resources/cold-war-on-file/khrushchev-on-cuban-crisis-1962/",
        ),
    ]

    return ReportContent(
        title="Cuba Crisis News Report",
        subtitle="The Cuban Missile Crisis, October-November 1962",
        author_line="By ChatGPT",
        as_of_date=date(2026, 5, 20),
        sections=sections,
        vocabulary=vocabulary,
        sources=sources,
        credits=(
            "This AI-generated educational report was prepared from public historical "
            "sources and follows the section requirements listed in news_report_request_list.csv."
        ),
    )

