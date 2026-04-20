#!/usr/bin/env python3
"""
world_peace_negotiation_report.py

Generate a PDF report summarizing the current state of major peace-related
negotiations as of April 20, 2026.

Requirements:
    pip install reportlab

Usage:
    python3 world_peace_negotiation_report.py
    python3 world_peace_negotiation_report.py --output current_world_peace_report.pdf
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, StyleSheet1, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
)

ACCENT = colors.HexColor("#1F4E79")
ACCENT_DARK = colors.HexColor("#15324B")
ACCENT_LIGHT = colors.HexColor("#DCEAF7")
TEXT = colors.HexColor("#1C1C1C")
MUTED = colors.HexColor("#666666")
SUCCESS = colors.HexColor("#2E7D32")
WARNING = colors.HexColor("#D97706")
DANGER = colors.HexColor("#B42318")
BORDER = colors.HexColor("#D0D7DE")


@dataclass(frozen=True)
class NegotiationFront:
    name: str
    status_label: str
    status_color: colors.Color
    progress_score: int
    snapshot: str
    sticking_points: list[str]
    near_term: str


FRONTS: list[NegotiationFront] = [
    NegotiationFront(
        name="Gaza / Israel-Hamas",
        status_label="Fragile / active",
        status_color=WARNING,
        progress_score=45,
        snapshot=(
            "A U.S.-brokered ceasefire that began in October 2025 remains in "
            "place formally, but Reuters reported on April 20, 2026 that "
            "implementation has stalled and violence continues."
        ),
        sticking_points=[
            "Disarmament of Hamas remains unresolved.",
            "Israeli force pullbacks are incomplete.",
            "Local violence and rival militias complicate stabilization.",
        ],
        near_term=(
            "Limited transactional progress is still possible, but the broader "
            "political settlement remains blocked."
        ),
    ),
    NegotiationFront(
        name="Russia-Ukraine",
        status_label="Exploratory / stalled",
        status_color=WARNING,
        progress_score=35,
        snapshot=(
            "Reuters reported on April 10, 2026 that negotiators were moving "
            "toward a potential deal, but the only concrete outcome this year "
            "has been prisoner-of-war exchanges."
        ),
        sticking_points=[
            "Territory remains the central impasse.",
            "Russia demands Ukrainian withdrawal from parts of Donbas.",
            "Ukraine rejects those terms despite pressure to negotiate."
        ],
        near_term=(
            "The talks appear real, but substantive convergence is still thin."
        ),
    ),
    NegotiationFront(
        name="U.S.-Iran / Hormuz crisis",
        status_label="Open window / high risk",
        status_color=DANGER,
        progress_score=40,
        snapshot=(
            "On April 20, 2026 Reuters reported that China urged all parties to "
            "maintain ceasefire and negotiation momentum after the U.S. seizure "
            "of an Iranian-flagged cargo ship."
        ),
        sticking_points=[
            "Maritime escalation threatens the diplomatic track.",
            "Normal transit through the Strait of Hormuz has not fully resumed.",
            "Retaliatory language raises the risk of derailment."
        ],
        near_term=(
            "The diplomatic opening is real, but any new clash could shut it quickly."
        ),
    ),
    NegotiationFront(
        name="UN peace and security diplomacy",
        status_label="Active forum / limited enforcement",
        status_color=SUCCESS,
        progress_score=55,
        snapshot=(
            "The UN Security Council's April 2026 programme includes multiple "
            "peace-and-security sessions, and the UN Secretary-General has "
            "continued to publicly support ongoing negotiations and ceasefires."
        ),
        sticking_points=[
            "UN diplomacy can convene and legitimize talks but cannot by itself impose deals.",
            "Major-power divisions continue to limit coercive enforcement.",
            "Breakthroughs still depend on political will by the direct parties."
        ],
        near_term=(
            "The UN remains an essential venue for pressure, coordination, and legitimacy."
        ),
    ),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a world peace negotiation PDF report.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("world_peace_negotiation_report.pdf"),
        help="Output PDF path.",
    )
    return parser.parse_args()


def build_styles() -> StyleSheet1:
    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="TitleReport",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=30,
            alignment=TA_CENTER,
            textColor=ACCENT_DARK,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubtitleReport",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            alignment=TA_CENTER,
            textColor=MUTED,
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionReport",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=19,
            textColor=ACCENT_DARK,
            spaceBefore=12,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyReport",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            textColor=TEXT,
            alignment=TA_JUSTIFY,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallReport",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=12,
            textColor=MUTED,
            alignment=TA_LEFT,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CardTitle",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=14,
            textColor=ACCENT_DARK,
            spaceAfter=4,
        )
    )
    return styles


class ReportTemplate(BaseDocTemplate):
    def __init__(self, filename: str | Path, **kwargs: object) -> None:
        super().__init__(str(filename), pagesize=LETTER, **kwargs)
        frame = Frame(
            0.7 * inch,
            0.72 * inch,
            LETTER[0] - 1.4 * inch,
            LETTER[1] - 1.35 * inch,
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        template = PageTemplate(id="report", frames=[frame], onPage=self.draw_page)
        self.addPageTemplates([template])

    @staticmethod
    def draw_page(canvas, doc) -> None:  # type: ignore[no-untyped-def]
        canvas.saveState()
        width, height = LETTER

        canvas.setStrokeColor(BORDER)
        canvas.setLineWidth(0.8)
        canvas.line(0.7 * inch, height - 0.62 * inch, width - 0.7 * inch, height - 0.62 * inch)

        canvas.setFillColor(ACCENT_DARK)
        canvas.setFont("Helvetica-Bold", 9)
        canvas.drawString(0.72 * inch, height - 0.48 * inch, "Current World Peace Negotiation Report")

        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 8.5)
        canvas.drawRightString(width - 0.72 * inch, height - 0.48 * inch, "As of April 20, 2026")

        canvas.setLineWidth(0.6)
        canvas.line(0.7 * inch, 0.58 * inch, width - 0.7 * inch, 0.58 * inch)
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(0.72 * inch, 0.38 * inch, "Prepared for situational awareness and discussion.")
        canvas.drawRightString(width - 0.72 * inch, 0.38 * inch, f"Page {doc.page}")
        canvas.restoreState()


def status_badge(text: str, fill_color: colors.Color) -> Table:
    badge = Table([[Paragraph(f"<b>{text}</b>", ParagraphStyle(
        name=f"badge_{text}",
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=10,
        textColor=colors.white,
        alignment=TA_CENTER,
    ))]], colWidths=[1.5 * inch])
    badge.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), fill_color),
                ("BOX", (0, 0), (-1, -1), 0, fill_color),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return badge


def progress_bar(score: int, width: float = 2.2 * inch, height: float = 0.18 * inch) -> Drawing:
    drawing = Drawing(width, 0.46 * inch)
    drawing.add(Rect(0, 10, width, height, fillColor=colors.HexColor("#E9EEF3"), strokeColor=None))
    drawing.add(Rect(0, 10, width * max(0, min(score, 100)) / 100.0, height, fillColor=ACCENT, strokeColor=None))
    drawing.add(String(0, 22, f"Momentum score: {score}/100", fontName="Helvetica", fontSize=8.5, fillColor=MUTED))
    return drawing


def info_box(styles: StyleSheet1) -> Table:
    content = [
        [Paragraph("<b>Assessment frame</b>", styles["CardTitle"])],
        [Paragraph(
            "This report does not assume a single global peace process. It tracks "
            "the most consequential active or semi-active negotiation fronts shaping "
            "international stability right now.",
            styles["BodyReport"],
        )],
        [Paragraph(
            "Scores in this report are editorial indicators designed to summarize "
            "current diplomatic momentum, not formal forecasts.",
            styles["BodyReport"],
        )],
    ]
    table = Table(content, colWidths=[6.6 * inch])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), ACCENT_LIGHT),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    return table


def summary_table(styles: StyleSheet1, fronts: Iterable[NegotiationFront]) -> Table:
    rows: list[list[object]] = [
        [
            Paragraph("<b>Front</b>", styles["SmallReport"]),
            Paragraph("<b>Status</b>", styles["SmallReport"]),
            Paragraph("<b>Negotiating picture</b>", styles["SmallReport"]),
            Paragraph("<b>Near-term read</b>", styles["SmallReport"]),
        ]
    ]

    for front in fronts:
        rows.append(
            [
                Paragraph(front.name, styles["BodyReport"]),
                status_badge(front.status_label, front.status_color),
                Paragraph(front.snapshot, styles["BodyReport"]),
                Paragraph(front.near_term, styles["BodyReport"]),
            ]
        )

    table = Table(rows, colWidths=[1.55 * inch, 1.4 * inch, 2.4 * inch, 1.45 * inch], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), ACCENT_DARK),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.6, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
            ]
        )
    )
    return table


def front_card(front: NegotiationFront, styles: StyleSheet1) -> Table:
    bullet_html = "".join(f"<br/>- {point}" for point in front.sticking_points)
    left_side = [
        Paragraph(front.name, styles["CardTitle"]),
        Spacer(1, 2),
        status_badge(front.status_label, front.status_color),
        Spacer(1, 6),
        progress_bar(front.progress_score),
    ]
    right_side = [
        Paragraph(f"<b>Snapshot.</b> {front.snapshot}", styles["BodyReport"]),
        Paragraph(f"<b>Main blockers.</b>{bullet_html}", styles["BodyReport"]),
        Paragraph(f"<b>Near-term outlook.</b> {front.near_term}", styles["BodyReport"]),
    ]

    table = Table(
        [[left_side, right_side]],
        colWidths=[2.2 * inch, 4.2 * inch],
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )
    return table


def source_table(styles: StyleSheet1) -> Table:
    entries = [
        ["1", "Reuters, April 20, 2026", "Gaza ceasefire implementation has stalled; violence and militia clashes continue."],
        ["2", "Reuters, April 5, 2026", "Hamas signaled it would not discuss disarmament without a full Israeli withdrawal from Gaza."],
        ["3", "Reuters, April 10, 2026", "Ukraine-Russia negotiators were described as moving toward a potential deal, but only POW swaps were concrete."],
        ["4", "Reuters, April 20, 2026", "China urged parties in the Hormuz crisis to maintain ceasefire and negotiation momentum after the ship seizure."],
        ["5", "UN Security Council / UN Secretariat, April 2026", "April programme materials show continued formal UN focus on international peace and security."],
    ]

    rows: list[list[object]] = [
        [
            Paragraph("<b>No.</b>", styles["SmallReport"]),
            Paragraph("<b>Source</b>", styles["SmallReport"]),
            Paragraph("<b>Why it matters</b>", styles["SmallReport"]),
        ]
    ]
    for num, source, note in entries:
        rows.append(
            [
                Paragraph(num, styles["BodyReport"]),
                Paragraph(source, styles["BodyReport"]),
                Paragraph(note, styles["BodyReport"]),
            ]
        )

    table = Table(rows, colWidths=[0.45 * inch, 2.1 * inch, 4.05 * inch], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), ACCENT_DARK),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.8, BORDER),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
            ]
        )
    )
    return table


def build_story(styles: StyleSheet1) -> list[object]:
    story: list[object] = []

    story.append(Spacer(1, 1.1 * inch))
    story.append(Paragraph("Current World Peace Negotiation Report", styles["TitleReport"]))
    story.append(
        Paragraph(
            "A concise diplomatic snapshot of the major negotiation fronts shaping international stability.",
            styles["SubtitleReport"],
        )
    )
    story.append(info_box(styles))
    story.append(Spacer(1, 18))
    story.append(
        Paragraph(
            "<b>Executive summary.</b> As of April 20, 2026, there is no single "
            "global peace conference capable of resolving the world's main conflicts at once. "
            "Instead, diplomacy is fragmented across several theaters. Gaza remains under a "
            "fragile ceasefire framework with implementation disputes; Russia-Ukraine talks show "
            "signs of movement but little hard convergence; the Hormuz crisis has reopened a narrow "
            "diplomatic window while remaining highly escalatory; and the United Nations continues "
            "to serve as a central convening forum even when enforcement is limited.",
            styles["BodyReport"],
        )
    )
    story.append(Spacer(1, 12))
    story.append(Paragraph("Negotiation dashboard", styles["SectionReport"]))
    story.append(summary_table(styles, FRONTS))

    story.append(PageBreak())
    story.append(Paragraph("Detailed front-by-front assessment", styles["SectionReport"]))
    story.append(
        Paragraph(
            "The sections below summarize the present diplomatic picture, the main blockers, "
            "and the most realistic near-term reading for each front.",
            styles["BodyReport"],
        )
    )

    for front in FRONTS:
        story.append(front_card(front, styles))
        story.append(Spacer(1, 10))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Key takeaways", styles["SectionReport"]))
    story.append(
        Paragraph(
            "1. The current system is producing conflict management more often than full settlement.<br/>"
            "2. Ceasefires are easier to negotiate than final political end states.<br/>"
            "3. Maritime and regional escalation risks can rapidly reverse diplomatic gains.<br/>"
            "4. External mediators can keep talks alive, but durable peace still depends on direct-party concessions.",
            styles["BodyReport"],
        )
    )

    story.append(Paragraph("Source notes", styles["SectionReport"]))
    story.append(source_table(styles))
    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            "This report is a synthesized briefing document. It is designed for readability and "
            "discussion, not as a substitute for direct source review or formal intelligence analysis.",
            styles["SmallReport"],
        )
    )
    return story


def generate_pdf(output_path: Path) -> Path:
    styles = build_styles()
    doc = ReportTemplate(
        output_path,
        title="Current World Peace Negotiation Report",
        author="OpenAI",
        subject="Diplomatic situation report",
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.8 * inch,
        bottomMargin=0.7 * inch,
    )
    story = build_story(styles)
    doc.build(story)
    return output_path


def main() -> None:
    args = parse_args()
    output_path = generate_pdf(args.output)
    print(f"Created PDF: {output_path.resolve()}")


if __name__ == "__main__":
    main()
