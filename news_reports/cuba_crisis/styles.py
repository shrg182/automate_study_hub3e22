#!/usr/bin/env python3
"""
styles.py

ReportLab styles for the Cuba Crisis news report.
"""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet


NAVY = colors.HexColor("#1F3A5F")
INK = colors.HexColor("#2F3437")
MUTED = colors.HexColor("#666666")


def build_styles() -> dict[str, ParagraphStyle]:
    """Build paragraph styles keyed by semantic name."""

    sample = getSampleStyleSheet()

    return {
        "title": ParagraphStyle(
            "title",
            parent=sample["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=27,
            alignment=TA_CENTER,
            textColor=NAVY,
            spaceAfter=6,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            textColor=INK,
            spaceAfter=6,
        ),
        "meta": ParagraphStyle(
            "meta",
            parent=sample["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            textColor=MUTED,
            spaceAfter=6,
        ),
        "section_heading": ParagraphStyle(
            "section_heading",
            parent=sample["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            alignment=TA_LEFT,
            textColor=NAVY,
            spaceBefore=12,
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
            textColor=INK,
            spaceAfter=5,
        ),
        "small": ParagraphStyle(
            "small",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=11,
            leftIndent=10,
            textColor=INK,
            spaceAfter=4,
        ),
        "credits": ParagraphStyle(
            "credits",
            parent=sample["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12,
            textColor=MUTED,
            spaceAfter=4,
        ),
    }

