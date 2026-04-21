#!/usr/bin/env python3
"""
generator.py

Build the World Peace Negotiation Report PDF.

This module handles:
- document creation
- title section
- executive summary
- negotiation dashboard table
- analyst comments
- page header and footer
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from data_model import ReportContent, build_sample_report_content
from styles import (
    LIGHT_GRAY,
    LIGHT_NAVY,
    NAVY,
    STATUS_COLOR_MAP,
    VERY_LIGHT_GRAY,
    WHITE,
    build_styles,
)


PAGE_WIDTH, PAGE_HEIGHT = A4


def _format_report_date(report_content: ReportContent) -> str:
    """
    Format the report date for display.

    Args:
        report_content: The report content object.

    Returns:
        A human-readable date string.
    """
    return report_content.as_of_date.strftime("%B %d, %Y")


def add_header_footer(canvas, doc) -> None:
    """
    Draw the page header and footer on each page.

    Args:
        canvas: ReportLab canvas object.
        doc: ReportLab document object.
    """
    canvas.saveState()

    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(0.7)
    canvas.line(
        20 * mm,
        PAGE_HEIGHT - 18 * mm,
        PAGE_WIDTH - 20 * mm,
        PAGE_HEIGHT - 18 * mm,
    )

    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(
        20 * mm,
        PAGE_HEIGHT - 14 * mm,
        "Current World Peace Negotiation Report",
    )

    canvas.setFont("Helvetica-Oblique", 8)
    canvas.drawRightString(PAGE_WIDTH - 20 * mm, PAGE_HEIGHT - 14 * mm, "by ChatGPT")

    canvas.setStrokeColor(LIGHT_GRAY)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 18 * mm, PAGE_WIDTH - 20 * mm, 18 * mm)

    canvas.setFillColor(colors.black)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(
        20 * mm,
        12 * mm,
        "Prepared for situational awareness and discussion.",
    )
    canvas.drawRightString(PAGE_WIDTH - 20 * mm, 12 * mm, f"Page {doc.page}")

    canvas.restoreState()


def _build_title_section(report_content: ReportContent, styles: dict) -> list:
    """
    Build the title section for the report.

    Args:
        report_content: Data for the report.
        styles: Dictionary of paragraph styles.

    Returns:
        A list of flowables.
    """
    story = []

    story.append(Spacer(1, 40))
    story.append(Paragraph(report_content.title, styles["title"]))
    story.append(Paragraph(report_content.subtitle, styles["subtitle"]))
    story.append(Paragraph(report_content.author_line, styles["author"]))
    story.append(
        Paragraph(
            f"As of {_format_report_date(report_content)}",
            styles["subtitle"],
        )
    )
    story.append(Spacer(1, 18))

    return story


def _build_executive_summary(report_content: ReportContent, styles: dict) -> list:
    """
    Build the executive summary section.

    Args:
        report_content: Data for the report.
        styles: Dictionary of paragraph styles.

    Returns:
        A list of flowables.
    """
    story = []

    story.append(Paragraph("Executive Summary", styles["section_heading"]))

    for item in report_content.executive_summary:
        story.append(Paragraph(f"• {item}", styles["bullet"]))

    story.append(Spacer(1, 8))
    return story


def _build_dashboard_table(report_content: ReportContent, styles: dict) -> Table:
    """
    Build the main negotiation dashboard table with improved styling.

    Args:
        report_content: Data for the report.
        styles: Dictionary of paragraph styles.

    Returns:
        A styled Table object.
    """
    rows = [
        [
            Paragraph("Front", styles["table_header"]),
            Paragraph("Status", styles["table_header"]),
            Paragraph("Negotiating picture", styles["table_header"]),
            Paragraph("Near-term read", styles["table_header"]),
        ]
    ]

    status_row_colors: list[tuple[int, colors.Color]] = []

    for row_index, front in enumerate(report_content.fronts, start=1):
        rows.append(
            [
                Paragraph(front.front, styles["table_cell"]),
                Paragraph(front.status_label, styles["status_label"]),
                Paragraph(front.negotiating_picture, styles["table_cell"]),
                Paragraph(front.near_term_read, styles["table_cell"]),
            ]
        )
        status_row_colors.append(
            (row_index, STATUS_COLOR_MAP.get(front.status_key, colors.grey))
        )

    table = Table(
        rows,
        colWidths=[110, 95, 190, 130],
        repeatRows=1,
        hAlign="LEFT",
    )

    table_style = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, LIGHT_GRAY),
        ("LINEBELOW", (0, 0), (-1, 0), 1, NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, VERY_LIGHT_GRAY]),
    ]

    for row_index, status_color in status_row_colors:
        table_style.extend(
            [
                ("BACKGROUND", (1, row_index), (1, row_index), status_color),
                ("TEXTCOLOR", (1, row_index), (1, row_index), WHITE),
                ("ALIGN", (1, row_index), (1, row_index), "CENTER"),
                ("FONTNAME", (1, row_index), (1, row_index), "Helvetica-Bold"),
                ("VALIGN", (1, row_index), (1, row_index), "MIDDLE"),
            ]
        )

    table.setStyle(TableStyle(table_style))
    return table


def _build_comments_section(report_content: ReportContent, styles: dict) -> list:
    """
    Build the comments section.

    Args:
        report_content: Data for the report.
        styles: Dictionary of paragraph styles.

    Returns:
        A list of flowables.
    """
    story = []

    story.append(Paragraph("Comments", styles["section_heading"]))

    for comment in report_content.comments:
        story.append(Paragraph(comment, styles["comment"]))

    return story


def build_report(output_path: str | Path) -> Path:
    """
    Generate the PDF report and save it to disk.

    Args:
        output_path: Output path for the generated PDF.

    Returns:
        The resolved Path to the PDF file.
    """
    output_file = Path(output_path).expanduser().resolve()
    styles = build_styles()
    report_content = build_sample_report_content()

    doc = SimpleDocTemplate(
        str(output_file),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=24 * mm,
        bottomMargin=24 * mm,
        title=report_content.title,
        author="ChatGPT",
        subject="World peace negotiation briefing",
    )

    story = []

    story.extend(_build_title_section(report_content, styles))
    story.append(HRFlowable(width="100%", thickness=1, color=LIGHT_NAVY))
    story.append(Spacer(1, 10))
    story.extend(_build_executive_summary(report_content, styles))
    story.append(Paragraph("Negotiation Dashboard", styles["section_heading"]))
    story.append(_build_dashboard_table(report_content, styles))
    story.append(Spacer(1, 14))
    story.extend(_build_comments_section(report_content, styles))

    doc.build(
        story,
        onFirstPage=add_header_footer,
        onLaterPages=add_header_footer,
    )

    return output_file