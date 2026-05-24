#!/usr/bin/env python3
"""
ReportLab styles for the voice reading instruction PDF.
"""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet


DEEP_BLUE = colors.HexColor("#1F3A5F")
INK = colors.HexColor("#2F3437")
MUTED = colors.HexColor("#666666")
LIGHT_BLUE = colors.HexColor("#EAF2F8")
RULE = colors.HexColor("#C8D6E5")


def build_styles() -> dict[str, ParagraphStyle]:
    """Build paragraph styles keyed by semantic name."""

    sample = getSampleStyleSheet()

    return {
        "title": ParagraphStyle(
            "title",
            parent=sample["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=29,
            alignment=TA_CENTER,
            textColor=DEEP_BLUE,
            spaceAfter=8,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            alignment=TA_CENTER,
            textColor=MUTED,
            spaceAfter=14,
        ),
        "meta": ParagraphStyle(
            "meta",
            parent=sample["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=8.5,
            leading=11,
            alignment=TA_CENTER,
            textColor=MUTED,
            spaceAfter=3,
        ),
        "section_heading": ParagraphStyle(
            "section_heading",
            parent=sample["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=16,
            alignment=TA_LEFT,
            textColor=DEEP_BLUE,
            spaceBefore=10,
            spaceAfter=4,
        ),
        "list_item": ParagraphStyle(
            "list_item",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=INK,
            spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "body",
            parent=sample["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13,
            textColor=INK,
            spaceAfter=4,
        ),
        "code": ParagraphStyle(
            "code",
            parent=sample["Code"],
            fontName="Courier",
            fontSize=8.5,
            leading=11,
            leftIndent=14,
            rightIndent=14,
            backColor=LIGHT_BLUE,
            borderColor=RULE,
            borderWidth=0.5,
            borderPadding=4,
            textColor=INK,
            spaceBefore=2,
            spaceAfter=5,
        ),
        "note": ParagraphStyle(
            "note",
            parent=sample["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=8.5,
            leading=11,
            textColor=MUTED,
            spaceBefore=4,
            spaceAfter=4,
        ),
    }
