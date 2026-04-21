#!/usr/bin/env python3
"""
styles.py

Centralized styles, colors, and table formatting helpers for the
World Peace Report module.
"""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet


# Core color palette
NAVY = colors.HexColor("#173A5E")
LIGHT_NAVY = colors.HexColor("#EAF0F6")
MID_GRAY = colors.HexColor("#666666")
LIGHT_GRAY = colors.HexColor("#D9DDE3")
VERY_LIGHT_GRAY = colors.HexColor("#F6F7F9")
WHITE = colors.white

# Status colors
STATUS_COLOR_MAP = {
    "fragile": colors.HexColor("#C97A00"),
    "stalled": colors.HexColor("#A66300"),
    "high_risk": colors.HexColor("#B22222"),
    "active": colors.HexColor("#2E7D32"),
}


def build_styles() -> dict[str, ParagraphStyle]:
    """
    Build and return all paragraph styles used in the PDF.

    Returns:
        A dictionary mapping style names to ParagraphStyle objects.
    """
    sample = getSampleStyleSheet()

    title_style = ParagraphStyle(
        name="ReportTitle",
        parent=sample["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=NAVY,
        alignment=TA_CENTER,
        spaceAfter=10,
    )

    subtitle_style = ParagraphStyle(
        name="ReportSubtitle",
        parent=sample["BodyText"],
        fontName="Helvetica",
        fontSize=11,
        leading=14,
        textColor=MID_GRAY,
        alignment=TA_CENTER,
        spaceAfter=6,
    )

    author_style = ParagraphStyle(
        name="AuthorLine",
        parent=sample["BodyText"],
        fontName="Helvetica-Oblique",
        fontSize=10,
        leading=12,
        textColor=MID_GRAY,
        alignment=TA_CENTER,
        spaceAfter=16,
    )

    section_heading_style = ParagraphStyle(
        name="SectionHeading",
        parent=sample["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=17,
        textColor=NAVY,
        alignment=TA_LEFT,
        spaceBefore=10,
        spaceAfter=8,
    )

    body_style = ParagraphStyle(
        name="BodyStyle",
        parent=sample["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.black,
        alignment=TA_LEFT,
        spaceAfter=6,
    )

    bullet_style = ParagraphStyle(
        name="BulletStyle",
        parent=sample["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        leftIndent=14,
        firstLineIndent=-8,
        bulletIndent=0,
        spaceAfter=4,
    )

    table_header_style = ParagraphStyle(
        name="TableHeaderStyle",
        parent=sample["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=WHITE,
        alignment=TA_LEFT,
    )

    table_cell_style = ParagraphStyle(
        name="TableCellStyle",
        parent=sample["BodyText"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=colors.black,
        alignment=TA_LEFT,
    )

    status_label_style = ParagraphStyle(
        name="StatusLabelStyle",
        parent=sample["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=9,
        textColor=WHITE,
        alignment=TA_CENTER,
    )

    comment_style = ParagraphStyle(
        name="CommentStyle",
        parent=sample["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.black,
        leftIndent=10,
        borderPadding=6,
        spaceAfter=8,
    )

    return {
        "title": title_style,
        "subtitle": subtitle_style,
        "author": author_style,
        "section_heading": section_heading_style,
        "body": body_style,
        "bullet": bullet_style,
        "table_header": table_header_style,
        "table_cell": table_cell_style,
        "status_label": status_label_style,
        "comment": comment_style,
    }