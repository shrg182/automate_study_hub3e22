#!/usr/bin/env python3
"""
styles.py

ReportLab styles for the Cuba Crisis news report.
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


NAVY = colors.HexColor("#1F3A5F")
INK = colors.HexColor("#2F3437")
MUTED = colors.HexColor("#666666")
RUSSIAN_BLUE = colors.HexColor("#2B6CB0")
FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"


def _register_unicode_fonts() -> None:
    """Register fonts that can render Cyrillic text when available."""

    global FONT_REGULAR, FONT_BOLD, FONT_ITALIC

    font_paths = {
        "StudyHubArial": Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        "StudyHubArial-Bold": Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
        "StudyHubArial-Italic": Path("/System/Library/Fonts/Supplemental/Arial Italic.ttf"),
    }
    if not all(font_path.exists() for font_path in font_paths.values()):
        return

    for font_name, font_path in font_paths.items():
        if font_name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(font_name, str(font_path)))

    pdfmetrics.registerFontFamily(
        "StudyHubArial",
        normal="StudyHubArial",
        bold="StudyHubArial-Bold",
        italic="StudyHubArial-Italic",
        boldItalic="StudyHubArial-Bold",
    )
    FONT_REGULAR = "StudyHubArial"
    FONT_BOLD = "StudyHubArial-Bold"
    FONT_ITALIC = "StudyHubArial-Italic"


def build_styles() -> dict[str, ParagraphStyle]:
    """Build paragraph styles keyed by semantic name."""

    _register_unicode_fonts()
    sample = getSampleStyleSheet()

    return {
        "title": ParagraphStyle(
            "title",
            parent=sample["Title"],
            fontName=FONT_BOLD,
            fontSize=22,
            leading=27,
            alignment=TA_CENTER,
            textColor=NAVY,
            spaceAfter=6,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=sample["BodyText"],
            fontName=FONT_REGULAR,
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            textColor=INK,
            spaceAfter=6,
        ),
        "meta": ParagraphStyle(
            "meta",
            parent=sample["BodyText"],
            fontName=FONT_ITALIC,
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            textColor=MUTED,
            spaceAfter=6,
        ),
        "section_heading": ParagraphStyle(
            "section_heading",
            parent=sample["Heading2"],
            fontName=FONT_BOLD,
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
            fontName=FONT_REGULAR,
            fontSize=10,
            leading=14,
            leftIndent=14,
            firstLineIndent=-8,
            textColor=INK,
            spaceAfter=5,
        ),
        "russian_bullet": ParagraphStyle(
            "russian_bullet",
            parent=sample["BodyText"],
            fontName=FONT_REGULAR,
            fontSize=10,
            leading=14,
            leftIndent=14,
            firstLineIndent=-8,
            textColor=RUSSIAN_BLUE,
            spaceAfter=7,
        ),
        "small": ParagraphStyle(
            "small",
            parent=sample["BodyText"],
            fontName=FONT_REGULAR,
            fontSize=8,
            leading=11,
            leftIndent=10,
            textColor=INK,
            spaceAfter=4,
        ),
        "caption": ParagraphStyle(
            "caption",
            parent=sample["BodyText"],
            fontName=FONT_ITALIC,
            fontSize=8,
            leading=11,
            alignment=TA_CENTER,
            textColor=MUTED,
            spaceAfter=6,
        ),
        "credits": ParagraphStyle(
            "credits",
            parent=sample["BodyText"],
            fontName=FONT_ITALIC,
            fontSize=9,
            leading=12,
            textColor=MUTED,
            spaceAfter=4,
        ),
    }
