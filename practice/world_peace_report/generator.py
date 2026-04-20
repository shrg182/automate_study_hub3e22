#!/usr/bin/env python3
"""PDF generator for the world peace negotiation report."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
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
)

from data_model import NegotiationFront, ReportContent
from styles import LIGHT_BORDER, NAVY, SOFT_BLUE, build_styles, status_color


class ReportDocTemplate(BaseDocTemplate):
    """Custom document template with header and footer."""

    def __init__(self, filename: str | Path, **kwargs: object) -> None:
        super().__init__(str(filename), **kwargs)
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="normal",
        )
        template = PageTemplate(id="report", frames=[frame], onPage=self._draw_header_footer)
        self.addPageTemplates([template])
        self.report_title: str = "World Peace Negotiation Report"
        self.prepared_for: str = "Situational awareness and discussion"

    def _draw_header_footer(self, canvas, doc) -> None:  # type: ignore[no-untyped-def]
        canvas.saveState()
        page_width, page_height = LETTER

        canvas.setFont("Helvetica-Bold", 10)
        canvas.setFillColor(NAVY)
        canvas.drawString(doc.leftMargin, page_height - 0.55 * inch, self.report_title.upper())

        canvas.setStrokeColor(LIGHT_BORDER)
        canvas.line(doc.leftMargin, page_height - 0.63 * inch, page_width - doc.rightMargin, page_height - 0.63 * inch)

        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.grey)
        canvas.drawString(doc.leftMargin, 0.45 * inch, self.prepared_for)
        canvas.drawRightString(page_width - doc.rightMargin, 0.45 * inch, f"Page {canvas.getPageNumber()}")
        canvas.restoreState()


def _paragraph(text: str, style_name: str, styles) -> Paragraph:  # type: ignore[no-untyped-def]
    """Create a paragraph from a text string."""
    return Paragraph(text, styles[style_name])


def build_dashboard_table(fronts: Iterable[NegotiationFront], styles) -> Table:  # type: ignore[no-untyped-def]
    """Build the main negotiation dashboard table."""
    rows: list[list[object]] = [
        [
            _paragraph("<b>Front</b>", "SmallMuted", styles),
            _paragraph("<b>Status</b>", "SmallMuted", styles),
            _paragraph("<b>Negotiating picture</b>", "SmallMuted", styles),
            _paragraph("<b>Near-term read</b>", "SmallMuted", styles),
            _paragraph("<b>Risk</b>", "SmallMuted", styles),
        ]
    ]

    for front in fronts:
        status_label = Table(
            [[_paragraph(front.status, "StatusCell", styles)]],
            colWidths=[1.35 * inch],
            rowHeights=[0.32 * inch],
        )
        status_label.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), status_color(front.status)),
                    ("BOX", (0, 0), (-1, -1), 0.4, status_color(front.status)),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 2),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ]
            )
        )

        rows.append(
            [
                _paragraph(front.name, "BodyJustify", styles),
                status_label,
                _paragraph(front.negotiating_picture, "BodyJustify", styles),
                _paragraph(front.near_term_read, "BodyJustify", styles),
                _paragraph(f"<b>{front.risk_score}/10</b>", "BodyJustify", styles),
            ]
        )

    table = Table(
        rows,
        colWidths=[1.35 * inch, 1.5 * inch, 2.45 * inch, 2.1 * inch, 0.65 * inch],
        repeatRows=1,
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 9),
                ("GRID", (0, 0), (-1, -1), 0.35, LIGHT_BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, SOFT_BLUE]),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def _build_executive_summary(report: ReportContent, styles) -> list[object]:  # type: ignore[no-untyped-def]
    """Build story elements for the executive summary."""
    story: list[object] = []
    story.append(_paragraph("Executive Summary", "SectionHeading", styles))
    for item in report.executive_summary:
        story.append(Paragraph(item, styles["SummaryBullet"], bulletText="•"))
    story.append(Spacer(1, 0.14 * inch))
    return story


def _build_methodology(report: ReportContent, styles) -> list[object]:  # type: ignore[no-untyped-def]
    """Build story elements for the methodology section."""
    story: list[object] = []
    story.append(_paragraph("Methodology Notes", "SectionHeading", styles))
    for note in report.methodology_notes:
        story.append(Paragraph(note, styles["SummaryBullet"], bulletText="–"))
    return story


def build_pdf(report: ReportContent, output_path: str | Path) -> Path:
    """Generate the PDF report and return the output path."""
    output = Path(output_path)
    styles = build_styles()

    doc = ReportDocTemplate(
        output,
        pagesize=LETTER,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.95 * inch,
        bottomMargin=0.7 * inch,
        title=report.metadata.title,
        author="OpenAI",
    )
    doc.report_title = report.metadata.title
    doc.prepared_for = report.metadata.prepared_for

    story: list[object] = [
        Spacer(1, 0.2 * inch),
        _paragraph(report.metadata.title, "ReportTitle", styles),
        _paragraph(report.metadata.subtitle, "ReportSubtitle", styles),
        _paragraph(
            f"<para align='center'><font color='#5A6B7A'>As of {report.metadata.as_of_date:%B %d, %Y}</font></para>",
            "BodyJustify",
            styles,
        ),
        Spacer(1, 0.18 * inch),
    ]

    story.extend(_build_executive_summary(report, styles))
    story.append(_paragraph("Negotiation Dashboard", "SectionHeading", styles))
    story.append(build_dashboard_table(report.fronts, styles))
    story.append(PageBreak())
    story.extend(_build_methodology(report, styles))

    doc.build(story)
    return output
