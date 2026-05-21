#!/usr/bin/env python3
"""
generator.py

Generate the Cuba Crisis news report PDF.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

from data_model import ReportContent, build_report_content
from styles import build_styles


DEFAULT_REQUEST_CSV = "news_report_request_list.csv"
DEFAULT_OUTPUT = "cuba_crisis_report_20260520.pdf"


@dataclass(slots=True)
class RequestRow:
    """Represent one CSV request row."""

    order: int
    requirement: str
    include: bool
    specific_requirements: str


def _format_date(report_date) -> str:
    """Format a report date for display."""

    return report_date.strftime("%B %d, %Y")


def _paragraph(text: str, style) -> Paragraph:
    """Create an escaped ReportLab paragraph."""

    return Paragraph(escape(text), style)


def _bullet(text: str, style) -> Paragraph:
    """Create a bullet paragraph."""

    return Paragraph(f"&#8226; {escape(text)}", style)


def _parse_include(value: str) -> bool:
    """Parse the include column from the request CSV."""

    return value.strip().lower() in {"1", "true", "yes", "y", "include"}


def load_request_rows(csv_path: Path) -> list[RequestRow]:
    """Load requested sections from the CSV file."""

    with csv_path.open("r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [
            RequestRow(
                order=int(row.get("order") or index),
                requirement=row.get("requirement", "").strip(),
                include=_parse_include(row.get("include", "yes")),
                specific_requirements=row.get("specific_requirements", "").strip(),
            )
            for index, row in enumerate(reader, start=1)
            if row.get("requirement", "").strip()
        ]

    return sorted(rows, key=lambda row: row.order)


def _build_title(report: ReportContent, styles) -> list:
    """Build title elements."""

    return [
        _paragraph(report.title, styles["title"]),
        _paragraph(report.subtitle, styles["subtitle"]),
        _paragraph(report.author_line, styles["meta"]),
        _paragraph(f"As of {_format_date(report.as_of_date)}", styles["meta"]),
        Spacer(1, 10),
        HRFlowable(width="100%"),
        Spacer(1, 10),
    ]


def _build_standard_section(title: str, paragraphs: list[str], styles) -> list:
    """Build a normal text section."""

    story = [_paragraph(title, styles["section_heading"])]
    for paragraph in paragraphs:
        story.append(_bullet(paragraph, styles["bullet"]))
    return story


def _build_vocabulary(report: ReportContent, styles) -> list:
    """Build the vocabulary section."""

    story = [_paragraph("New Vocabulary", styles["section_heading"])]
    for item in report.vocabulary:
        story.append(
            Paragraph(
                f"<b>{escape(item.term)}</b>: {escape(item.definition)}",
                styles["small"],
            )
        )
    return story


def _build_sources(report: ReportContent, styles) -> list:
    """Build the sources section."""

    story = [_paragraph("Sources", styles["section_heading"])]
    for source in report.sources:
        story.append(
            Paragraph(
                f"<b>{escape(source.name)}</b>: {escape(source.url)}",
                styles["small"],
            )
        )
    return story


def _build_credits(report: ReportContent, styles) -> list:
    """Build the credits section."""

    return [
        _paragraph("Credits", styles["section_heading"]),
        _paragraph(report.credits, styles["credits"]),
    ]


def _build_requested_section(
    request: RequestRow,
    report: ReportContent,
    styles,
) -> list:
    """Build one requested section."""

    if request.requirement == "New Vocabulary":
        story = _build_vocabulary(report, styles)
    elif request.requirement == "Sources":
        story = _build_sources(report, styles)
    elif request.requirement == "Credits":
        story = _build_credits(report, styles)
    else:
        section = report.sections.get(request.requirement)
        if section is None:
            story = _build_standard_section(
                request.requirement,
                [f"Custom requested section: {request.requirement}."],
                styles,
            )
        else:
            story = _build_standard_section(section.title, section.paragraphs, styles)

    if request.specific_requirements:
        story.append(
            Paragraph(
                f"<b>Specific request:</b> {escape(request.specific_requirements)}",
                styles["small"],
            )
        )

    return story


def build_report(
    output_path: str | Path = DEFAULT_OUTPUT,
    request_csv_path: str | Path = DEFAULT_REQUEST_CSV,
) -> Path:
    """
    Build the PDF report according to the request CSV.

    Args:
        output_path: Output PDF path.
        request_csv_path: CSV file describing section order and inclusion.

    Returns:
        Resolved output path.
    """

    output_file = Path(output_path).resolve()
    request_file = Path(request_csv_path).resolve()
    output_file.parent.mkdir(parents=True, exist_ok=True)

    report = build_report_content()
    request_rows = [row for row in load_request_rows(request_file) if row.include]
    styles = build_styles()

    doc = SimpleDocTemplate(
        str(output_file),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        title=report.title,
        author="ChatGPT",
    )

    story = []
    story.extend(_build_title(report, styles))

    for request in request_rows:
        story.extend(_build_requested_section(request, report, styles))

    doc.build(story)
    return output_file


def main() -> None:
    """Generate the default PDF when this file is run directly."""

    generated_file = build_report(DEFAULT_OUTPUT, DEFAULT_REQUEST_CSV)
    print(f"Generated report: {generated_file}")


if __name__ == "__main__":
    main()

