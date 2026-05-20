#!/usr/bin/env python3
"""
styles.py

Styles for the Putin China Visit Report PDF.
"""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet


DEEP_RED = colors.HexColor("#7A1F2B")
CHARCOAL = colors.HexColor("#30343B")
GRAY = colors.HexColor("#666666")


def build_styles() -> dict[str, ParagraphStyle]:
    """
    Build PDF paragraph styles.

    Returns:
        Dictionary of styles keyed by semantic name.
    """

    sample = getSampleStyleSheet()

    return {
        "title": ParagraphStyle(
            "title",
            parent=sample["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=28,
            alignment=TA_CENTER,
            textColor=DEEP_RED,
            spaceAfter=10,
        ),
        "author": ParagraphStyle(
            "author",
            parent=sample["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=10,
            alignment=TA_CENTER,
            textColor=GRAY,
            spaceAfter=8,
        ),
        "section_heading": ParagraphStyle(
            "section_heading",
            parent=sample["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=DEEP_RED,
            alignment=TA_LEFT,
            spaceBefore=12,
            spaceAfter=6,
        ),
        "subsection_heading": ParagraphStyle(
            "subsection_heading",
            parent=sample["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=CHARCOAL,
            alignment=TA_LEFT,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=15,
            alignment=TA_LEFT,
            spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            leftIndent=14,
            firstLineIndent=-8,
            spaceAfter=4,
        ),
        "vocabulary": ParagraphStyle(
            "vocabulary",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            leftIndent=10,
            spaceAfter=5,
        ),
        "source": ParagraphStyle(
            "source",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=11,
            leftIndent=10,
            spaceAfter=4,
            textColor=CHARCOAL,
        ),
        "credits": ParagraphStyle(
            "credits",
            parent=sample["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12,
            textColor=GRAY,
            spaceBefore=10,
        ),
    }

