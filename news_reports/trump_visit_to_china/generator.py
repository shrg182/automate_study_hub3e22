#!/usr/bin/env python3
"""
generator

Generate the Trump China Visit Report PDF.
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer, 
)

from data_model import build_sample_report_content
from styles import build_styles


def _format_date(d: date) -> str:
    """Format a date as "Month Day, Year"."""
    return d.strftime("%B %d, %Y")


def _build_title(report, styles) -> list:
    """Build the title section of the report."""
    elements = []
    elements.append(Paragraph(report.title, styles["title"]))
    elements.append(Paragraph(report.author_line, styles["author"]))
    elements.append(Paragraph(f"As of {report.as_of_date}", styles["author"]))
    elements.append(Spacer(1, 12))
    return elements


def _build_breaking_news(report, styles) -> list:
    """Build the breaking news section."""
    elements = []
    elements.append(Paragraph("Breaking News", styles["section_heading"]))
    elements.append(Paragraph(report.breaking_news, styles["body"]))
    return elements


def _build_bullet_section(title, items, styles) -> list:
    """Build a section with bullet points."""
    elements = []
    elements.append(Paragraph(title, styles["section_heading"]))
    for item in items:
        elements.append(Paragraph(f"• {item}", styles["bullet"]))
    return elements


def _build_text_section(title, text, styles) -> list:
    """Build a section with a single block of text."""
    elements = []
    elements.append(Paragraph(title, styles["section_heading"]))
    elements.append(Paragraph(text, styles["body"]))
    return elements


def _build_vocabulary_section(vocab_items, styles) -> list:
    """Build the vocabulary section."""
    elements = []
    elements.append(Paragraph("Vocabulary", styles["section_heading"]))
    for item in vocab_items:
        elements.append(Paragraph(f"{item.term}: {item.definition}", styles["vocabulary"]))
    return elements


def build_report(output_path: str | Path) -> None:
    """Build the report PDF."""
    output_path = Path(output_path)
    report = build_sample_report_content()
    styles = build_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
    )

    elements = []
    elements.extend(_build_title(report, styles))
    elements.extend(_build_breaking_news(report, styles))
    elements.extend(_build_bullet_section("Executive Summary", report.executive_summary, styles))
    elements.extend(_build_bullet_section("Situation Analysis", report.situation_analysis, styles))
    elements.extend(_build_bullet_section("Latest Updates", report.latest_updates, styles))
    elements.extend(_build_bullet_section("Risk Assessment", report.risk_assessment, styles))
    elements.extend(_build_text_section("Comments", "\n".join(report.comments), styles))
    elements.extend(_build_vocabulary_section(report.vocabulary, styles))
    elements.append(Spacer(1, 12))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=styles["credits"].textColor))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(report.credits, styles["credits"]))

    doc.build(elements)