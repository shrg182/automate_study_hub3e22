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
                    "Карибский кризис поставил Соединенные Штаты и Советский Союз "
                    "на грань ядерной войны в октябре 1962 года после того, как американские "
                    "разведывательные фотографии выявили строящиеся советские ядерные ракетные "
                    "объекты на Кубе."
                ),
                (
                    "President John F. Kennedy responded with a naval 'quarantine' of Cuba, "
                    "publicly demanding the removal of the missiles while his advisers debated "
                    "air strikes, invasion, diplomacy, and blockade enforcement."
                ),
                (
                    "Президент Джон Ф. Кеннеди ответил морским \"карантином\" Кубы, "
                    "публично требуя вывода ракет, в то время как его советники обсуждали "
                    "авиаудары, вторжение, дипломатию и обеспечение блокады."
                ),
                (
                    "The immediate crisis eased on October 28, 1962, when Soviet leader Nikita "
                    "Khrushchev agreed to remove the missiles from Cuba in exchange for a U.S. "
                    "pledge not to invade Cuba and a secret U.S. commitment to remove Jupiter "
                    "missiles from Turkey."
                ),
                (
                    "Непосредственный кризис ослаб 28 октября 1962 года, когда "
                    "советский лидер Никита Хрущев согласился убрать ракеты с Кубы в обмен "
                    "на обещание США не вторгаться на Кубу и тайное обязательство США вывести "
                    "ракеты \"Юпитер\" из Турции."
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
                    "Ядерная политика на грани войны: кризис показал, как быстро "
                    "разведданные, военные передвижения и политическое давление могли подтолкнуть "
                    "ядерные державы к войне."
                ),
                (
                    "Controlled escalation: Kennedy chose a quarantine before air strikes or "
                    "invasion, creating space for diplomacy while still applying pressure."
                ),
                (
                    "Контролируемая эскалация: Кеннеди выбрал карантин вместо "
                    "авиаударов или вторжения, оставив пространство для дипломатии и одновременно "
                    "сохранив давление."
                ),
                (
                    "Back-channel diplomacy: Public threats were paired with private messages "
                    "and secret concessions that gave both leaders a way to step back."
                ),
                (
                    "Закулисная дипломатия: публичные угрозы сочетались с частными "
                    "сообщениями и тайными уступками, которые дали обоим лидерам возможность "
                    "отступить."
                ),
                (
                    "Cuba's security dilemma: Fidel Castro's government wanted protection after "
                    "the Bay of Pigs invasion, but the settlement was largely negotiated by "
                    "Washington and Moscow."
                ),
                (
                    "Дилемма безопасности Кубы: правительство Фиделя Кастро стремилось "
                    "к защите после вторжения в заливе Свиней, но урегулирование в основном "
                    "согласовывали Вашингтон и Москва."
                ),
                (
                    "Cold War lessons: The near catastrophe encouraged later crisis-management "
                    "measures, including improved communication between Washington and Moscow."
                ),
                (
                    "Уроки холодной войны: близость катастрофы способствовала более "
                    "поздним мерам по управлению кризисами, включая улучшение связи между "
                    "Вашингтоном и Москвой."
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
                    "Карибский кризис был 13-дневным противостоянием в октябре "
                    "1962 года из-за советских ядерных ракет, размещенных на Кубе примерно "
                    "в 90 милях от Флориды. Он стал самым опасным прямым противостоянием "
                    "между США и СССР в годы холодной войны."
                ),
                (
                    "The United States discovered the missile sites through U-2 aerial photography "
                    "and announced a naval quarantine on October 22. Soviet ships approached the "
                    "quarantine line while both sides exchanged public warnings and private messages."
                ),
                (
                    "Соединенные Штаты обнаружили ракетные объекты с помощью "
                    "аэрофотосъемки самолетом U-2 и 22 октября объявили морской карантин. "
                    "Советские корабли приближались к линии карантина, пока обе стороны "
                    "обменивались публичными предупреждениями и частными сообщениями."
                ),
                (
                    "The crisis ended through a negotiated settlement: Soviet missiles would leave "
                    "Cuba, the United States would not invade Cuba, and U.S. Jupiter missiles in "
                    "Turkey would be removed quietly. The episode remains a core case study in "
                    "nuclear risk, intelligence, and crisis leadership."
                ),
                (
                    "Кризис завершился путем согласованного урегулирования: советские "
                    "ракеты должны были покинуть Кубу, Соединенные Штаты не должны были "
                    "вторгаться на Кубу, а американские ракеты \"Юпитер\" в Турции должны были "
                    "быть тихо удалены. Этот эпизод остается ключевым примером для изучения "
                    "ядерного риска, разведки и лидерства в кризисе."
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
                    "Кризис вырос из нескольких факторов давления: неудачного "
                    "вторжения в заливе Свиней в 1961 году, стремления Кубы к безопасности, "
                    "попыток СССР изменить стратегический баланс и опасений США, что "
                    "наступательное оружие на Кубе будет угрожать безопасности Западного "
                    "полушария и внутреннему политическому доверию."
                ),
                (
                    "On October 16, 1962, Kennedy was informed that reconnaissance photographs "
                    "showed Soviet missile installations. For nearly a week, the administration "
                    "deliberated in secret through the Executive Committee of the National Security "
                    "Council, known as ExComm."
                ),
                (
                    "16 октября 1962 года Кеннеди сообщили, что разведывательные "
                    "фотографии показывают советские ракетные установки. Почти неделю "
                    "администрация тайно обсуждала ситуацию через Исполнительный комитет "
                    "Совета национальной безопасности, известный как ExComm."
                ),
                (
                    "On October 22, Kennedy addressed the nation, announced the quarantine, and "
                    "warned that any nuclear missile launched from Cuba against the Western Hemisphere "
                    "would be treated as an attack by the Soviet Union."
                ),
                (
                    "22 октября Кеннеди обратился к нации, объявил карантин и "
                    "предупредил, что любая ядерная ракета, запущенная с Кубы против "
                    "Западного полушария, будет рассматриваться как нападение Советского Союза."
                ),
                (
                    "October 27 was the most dangerous day: a U-2 was shot down over Cuba, another "
                    "U-2 strayed over Soviet territory, and U.S. leaders received conflicting Soviet "
                    "messages. Restraint on both sides prevented rapid escalation."
                ),
                (
                    "27 октября было самым опасным днем: один U-2 был сбит над "
                    "Кубой, другой U-2 отклонился над советскую территорию, а лидеры США "
                    "получали противоречивые советские сообщения. Сдержанность обеих сторон "
                    "предотвратила быструю эскалацию."
                ),
                (
                    "The final settlement removed the immediate missile threat but left important "
                    "questions about alliance politics, Cuban sovereignty, nuclear deterrence, and "
                    "the hidden risks of military alerts."
                ),
                (
                    "Окончательное урегулирование устранило непосредственную ракетную "
                    "угрозу, но оставило важные вопросы о политике союзов, суверенитете Кубы, "
                    "ядерном сдерживании и скрытых рисках военных тревог."
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
                    "14 октября 1962 года: разведывательный полет U-2 сфотографировал "
                    "строящиеся советские ракетные объекты на Кубе."
                ),
                (
                    "October 16, 1962: Kennedy was briefed on the missile evidence, beginning "
                    "the intense decision period remembered as the 'thirteen days.'"
                ),
                (
                    "16 октября 1962 года: Кеннеди доложили о ракетных доказательствах, "
                    "и начался напряженный период принятия решений, известный как \"тринадцать дней\"."
                ),
                (
                    "October 22, 1962: Kennedy publicly announced the missile discovery and "
                    "ordered a naval quarantine of Cuba."
                ),
                (
                    "22 октября 1962 года: Кеннеди публично объявил об обнаружении "
                    "ракет и приказал установить морской карантин Кубы."
                ),
                (
                    "October 27, 1962: U.S. pilot Major Rudolf Anderson was killed when his U-2 "
                    "was shot down over Cuba, marking the crisis's deadliest moment."
                ),
                (
                    "27 октября 1962 года: американский пилот майор Рудольф Андерсон "
                    "погиб, когда его U-2 был сбит над Кубой, что стало самым смертоносным "
                    "моментом кризиса."
                ),
                (
                    "October 28, 1962: Khrushchev announced that Soviet missiles would be removed "
                    "from Cuba. The U.S. quarantine formally ended on November 20 after verification "
                    "and removal steps."
                ),
                (
                    "28 октября 1962 года: Хрущев объявил, что советские ракеты будут "
                    "убраны с Кубы. Карантин США официально завершился 20 ноября после проверки "
                    "и шагов по удалению ракет."
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
                    "Риск ядерной войны: кризис создал несколько путей к применению "
                    "ядерного оружия, включая неверно истолкованные военные передвижения, "
                    "несанкционированные местные действия и давление с требованием ответного "
                    "удара после уничтожения U-2."
                ),
                (
                    "Command-and-control risk: Leaders did not fully control every battlefield "
                    "event, and later evidence showed the danger of tactical nuclear weapons and "
                    "submarine encounters unknown to some decision-makers at the time."
                ),
                (
                    "Риск командования и управления: лидеры не полностью контролировали "
                    "каждое событие на поле боя, а более поздние данные показали опасность "
                    "тактического ядерного оружия и столкновений с подводными лодками, о которых "
                    "некоторые лица, принимавшие решения, тогда не знали."
                ),
                (
                    "Political risk: Kennedy faced pressure to appear firm, Khrushchev faced "
                    "pressure not to retreat humiliatingly, and Castro feared another U.S. invasion."
                ),
                (
                    "Политический риск: Кеннеди испытывал давление, чтобы выглядеть "
                    "твердым, Хрущев испытывал давление, чтобы не отступить унизительно, а "
                    "Кастро опасался нового вторжения США."
                ),
                (
                    "Alliance risk: NATO allies, Turkey, and Latin American governments were "
                    "affected by decisions that were partly public and partly secret."
                ),
                (
                    "Риск для союзов: союзники по НАТО, Турция и правительства "
                    "Латинской Америки были затронуты решениями, которые были частично публичными "
                    "и частично тайными."
                ),
                (
                    "Long-term risk: The crisis demonstrated that deterrence can prevent war but "
                    "also produce moments where errors or accidents could have catastrophic effects."
                ),
                (
                    "Долгосрочный риск: кризис показал, что сдерживание может "
                    "предотвращать войну, но также создавать моменты, когда ошибки или "
                    "случайности могут иметь катастрофические последствия."
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
                    "Позиция США: Кеннеди представил ракеты как неприемлемую "
                    "наступательную угрозу Западному полушарию и использовал карантин, чтобы "
                    "сочетать силу, право и дипломатию."
                ),
                (
                    "Soviet view: Khrushchev sought to protect Cuba, strengthen Soviet leverage, "
                    "and respond to U.S. strategic advantages, including U.S. missiles positioned "
                    "near the Soviet Union."
                ),
                (
                    "Советская позиция: Хрущев стремился защитить Кубу, усилить "
                    "советские рычаги влияния и ответить на стратегические преимущества США, "
                    "включая американские ракеты, размещенные рядом с Советским Союзом."
                ),
                (
                    "Cuban view: Castro's government saw the missiles through the lens of survival "
                    "after the Bay of Pigs and continuing U.S. hostility, but Cuba had limited control "
                    "over the final U.S.-Soviet settlement."
                ),
                (
                    "Кубинская позиция: правительство Кастро рассматривало ракеты "
                    "через призму выживания после залива Свиней и продолжающейся враждебности "
                    "США, но Куба имела ограниченный контроль над окончательным американо-"
                    "советским урегулированием."
                ),
                (
                    "Historical view: The crisis is now remembered as both a success of restraint "
                    "and a warning about how close nuclear-armed states can come to disaster."
                ),
                (
                    "Историческая оценка: сегодня кризис помнят и как успех "
                    "сдержанности, и как предупреждение о том, насколько близко ядерные державы "
                    "могут подойти к катастрофе."
                ),
            ],
        ),
        "New Vocabulary": ReportSection(title="New Vocabulary", paragraphs=[]),
        "Sources": ReportSection(title="Sources", paragraphs=[]),
        "Credits": ReportSection(title="Credits", paragraphs=[]),
    }

    vocabulary = [
        VocabularyItem(
            "quarantine / карантин",
            "The naval restriction Kennedy ordered around Cuba; the term avoided the legal implications of declaring a blockade.",
        ),
        VocabularyItem(
            "blockade / блокада",
            "A military action that prevents ships or goods from entering or leaving an area, often treated as an act of war.",
        ),
        VocabularyItem(
            "Executive Committee / Исполнительный комитет",
            "The Executive Committee of the National Security Council, Kennedy's core advisory group during the crisis.",
        ),
        VocabularyItem(
            "reconnaissance aircraft / самолет-разведчик",
            "A reconnaissance aircraft used to gather intelligence; in this crisis, U-2 planes photographed Soviet missile sites in Cuba.",
        ),
        VocabularyItem(
            "brinkmanship / балансирование на грани войны",
            "The practice of pushing a dangerous confrontation close to disaster to gain advantage or force concessions.",
        ),
        VocabularyItem(
            "deterrence / сдерживание",
            "The strategy of preventing attack by making the likely cost of attack too high.",
        ),
        VocabularyItem(
            "back channel / закулисный канал",
            "A private or unofficial communication path used alongside formal diplomacy.",
        ),
        VocabularyItem(
            "Jupiter missiles / ракеты \"Юпитер\"",
            "U.S. medium-range ballistic missiles deployed in Turkey and Italy during the Cold War.",
        ),
        VocabularyItem(
            "settlement / урегулирование",
            "A negotiated settlement or resolution of a dispute or crisis.",
        ),
        VocabularyItem(
            "sovereignty / суверенитет",
            "A state's independent authority to govern itself without outside control.",
        ),
        VocabularyItem(
            "escalation / эскалация",
            "An increase in the intensity or seriousness of a conflict.",
        ),
        VocabularyItem(
            "concession / уступка",
            "A concession: something given up or agreed to in order to reach a compromise.",
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
        author_line="By Codex and ChatGPT",
        as_of_date=date(2026, 5, 23),
        sections=sections,
        vocabulary=vocabulary,
        sources=sources,
        credits=(
            "This AI-generated educational report was prepared by Codex with ChatGPT "
            "involvement, using public historical sources and the section requirements "
            "listed in news_report_request_list.csv."
        ),
    )
