#!/usr/bin/env python3
"""Styling helpers for the world peace PDF report."""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, StyleSheet1, getSampleStyleSheet


PAGE_BACKGROUND = colors.whitesmoke
NAVY = colors.HexColor("#153A5B")
STEEL = colors.HexColor("#5A6B7A")
LIGHT_BORDER = colors.HexColor("#D5DCE3")
SOFT_BLUE = colors.HexColor("#EDF3F8")
SOFT_GREEN = colors.HexColor("#EAF4EA")
SOFT_ORANGE = colors.HexColor("#FFF1DD")
SOFT_RED = colors.HexColor("#F9E4E2")
WHITE = colors.white

STATUS_COLORS: dict[str, colors.Color] = {
    "Open window / high risk": colors.HexColor("#B3261E"),
    "Fragile / active": colors.HexColor("#C77700"),
    "Exploratory / stalled": colors.HexColor("#A66500"),
    "Active forum / limited enforcement": colors.HexColor("#2E7D32"),
}


def build_styles() -> StyleSheet1:
    """Return a reusable stylesheet for the report."""
    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="ReportTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            alignment=TA_CENTER,
            textColor=NAVY,
            spaceAfter=10,
        )
    )

    styles.add(
        ParagraphStyle(
            name="ReportSubtitle",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            alignment=TA_CENTER,
            textColor=STEEL,
            spaceAfter=14,
        )
    )

    styles.add(
        ParagraphStyle(
            name="SectionHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=NAVY,
            spaceBefore=8,
            spaceAfter=6,
        )
    )

    styles.add(
        ParagraphStyle(
            name="SummaryBullet",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            alignment=TA_LEFT,
            textColor=colors.black,
            leftIndent=14,
            bulletIndent=2,
            spaceAfter=4,
        )
    )

    styles.add(
        ParagraphStyle(
            name="BodyJustify",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=13,
            alignment=TA_JUSTIFY,
            textColor=colors.black,
        )
    )

    styles.add(
        ParagraphStyle(
            name="SmallMuted",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=10,
            textColor=STEEL,
        )
    )

    styles.add(
        ParagraphStyle(
            name="StatusCell",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=10,
            alignment=TA_CENTER,
            textColor=WHITE,
        )
    )

    return styles


def status_color(status: str) -> colors.Color:
    """Return the fill color used for a status label."""
    return STATUS_COLORS.get(status, STEEL)
