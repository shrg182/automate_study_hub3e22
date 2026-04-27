#!/usr/bin/env python3

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet


NAVY = colors.HexColor("#173A5E")
LIGHT_GRAY = colors.HexColor("#D9DDE3")
WHITE = colors.white


def build_styles() -> dict[str, ParagraphStyle]:
    sample = getSampleStyleSheet()

    return {
        "title": ParagraphStyle(
            "title", parent=sample["Title"], fontSize=20,
            alignment=TA_CENTER, textColor=NAVY, spaceAfter=10
        ),
        "author": ParagraphStyle(
            "author", parent=sample["BodyText"], fontSize=10,
            alignment=TA_CENTER, spaceAfter=10
        ),
        "section_heading": ParagraphStyle(
            "section_heading", parent=sample["Heading2"],
            textColor=NAVY, spaceBefore=10, spaceAfter=6
        ),
        "body": ParagraphStyle(
            "body", parent=sample["BodyText"], fontSize=10, spaceAfter=6
        ),
        "bullet": ParagraphStyle(
            "bullet", parent=sample["BodyText"],
            leftIndent=12, spaceAfter=4
        ),
        "vocabulary": ParagraphStyle(
            "vocabulary", parent=sample["BodyText"],
            leftIndent=10, spaceAfter=5
        ),
    }