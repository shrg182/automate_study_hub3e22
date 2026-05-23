#!/usr/bin/env python3
"""
styles.py

PDF styles for the Einstein-Rosen Bridge introduction report.
"""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet


INK = colors.HexColor("#263238")
TEAL = colors.HexColor("#006D77")
GRAY = colors.HexColor("#5F6C72")


def build_styles() -> dict[str, ParagraphStyle]:
    """Build PDF paragraph styles."""
    sample = getSampleStyleSheet()

    return {
        "title": ParagraphStyle(
            "title",
            parent=sample["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=30,
            alignment=TA_CENTER,
            textColor=TEAL,
            spaceAfter=6,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=12,
            leading=16,
            alignment=TA_CENTER,
            textColor=INK,
            spaceAfter=8,
        ),
        "author": ParagraphStyle(
            "author",
            parent=sample["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12,
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
            alignment=TA_LEFT,
            textColor=TEAL,
            spaceBefore=12,
            spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "body",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=10,
            leading=15,
            alignment=TA_LEFT,
            textColor=INK,
            spaceAfter=7,
        ),
        "vocabulary": ParagraphStyle(
            "vocabulary",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=13,
            leftIndent=10,
            textColor=INK,
            spaceAfter=5,
        ),
        "caption": ParagraphStyle(
            "caption",
            parent=sample["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=8,
            leading=11,
            alignment=TA_CENTER,
            textColor=GRAY,
            spaceAfter=8,
        ),
        "credits": ParagraphStyle(
            "credits",
            parent=sample["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=8,
            leading=11,
            textColor=GRAY,
            spaceBefore=10,
        ),
    }
