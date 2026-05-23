#!/usr/bin/env python3
"""
generator.py

Generate the Einstein-Rosen Bridge introduction PDF.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

from data_model import ReportContent, ReportSection, build_report_content
from styles import build_styles


def _format_date(report: ReportContent) -> str:
    """Format the report date."""
    return report.as_of_date.strftime("%B %d, %Y")


def _build_title(report: ReportContent, styles) -> list:
    """Build the report title block."""
    return [
        Paragraph(escape(report.title), styles["title"]),
        Paragraph(escape(report.subtitle), styles["subtitle"]),
        Paragraph(escape(report.author_line), styles["author"]),
        Paragraph(f"As of {_format_date(report)}", styles["author"]),
        Spacer(1, 8),
        HRFlowable(width="100%"),
        Spacer(1, 8),
    ]


def _build_section(section: ReportSection, styles) -> list:
    """Build a text section."""
    story = [Paragraph(escape(section.title), styles["section_heading"])]
    for paragraph in section.paragraphs:
        story.append(Paragraph(escape(paragraph), styles["body"]))
    return story


def _build_vocabulary(report: ReportContent, styles) -> list:
    """Build the vocabulary section."""
    story = [Paragraph("New Vocabulary", styles["section_heading"])]
    for item in report.vocabulary:
        text = f"<b>{escape(item.term)}</b>: {escape(item.definition)}"
        story.append(Paragraph(text, styles["vocabulary"]))
    return story


def _build_sources(report: ReportContent, styles) -> list:
    """Build the sources section."""
    story = [Paragraph("Sources", styles["section_heading"])]
    for item in report.sources:
        text = f"<b>{escape(item.name)}</b>: {escape(item.note)}"
        story.append(Paragraph(text, styles["vocabulary"]))
    return story


def build_report(output_path: str | Path) -> Path:
    """Build the PDF report and return the output path."""
    output_file = Path(output_path).resolve()
    output_file.parent.mkdir(parents=True, exist_ok=True)

    styles = build_styles()
    report = build_report_content()

    doc = SimpleDocTemplate(
        str(output_file),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        title=report.title,
        author="Codex",
    )

    story = []
    story.extend(_build_title(report, styles))

    for section in report.sections:
        story.extend(_build_section(section, styles))

    story.extend(_build_vocabulary(report, styles))
    story.extend(_build_sources(report, styles))
    story.append(Paragraph("Credits", styles["section_heading"]))
    story.append(Paragraph(escape(report.credits), styles["credits"]))

    doc.build(story)
    return output_file


def main() -> None:
    """Generate the default report."""
    build_report("einstein_rosen_bridge_introduction.pdf")


if __name__ == "__main__":
    main()
