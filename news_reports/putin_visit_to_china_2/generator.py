#!/usr/bin/env python3
"""
generator.py

Generate the Putin China Visit Report PDF.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

from data_model import build_report_content
from styles import build_styles


DEFAULT_OUTPUT = "putin_china_visit_report_20260520.pdf"


def _format_date(d) -> str:
    """Format report date."""

    return d.strftime("%B %d, %Y")


def _paragraph(text: str, style) -> Paragraph:
    """Create a paragraph with escaped text."""

    return Paragraph(escape(text), style)


def _build_title(report, styles) -> list:
    return [
        _paragraph(report.title, styles["title"]),
        _paragraph(report.author_line, styles["author"]),
        _paragraph(f"As of {_format_date(report.as_of_date)}", styles["author"]),
        Spacer(1, 10),
    ]


def _build_text_section(title: str, items: list[str], styles) -> list:
    story = [_paragraph(title, styles["section_heading"])]

    for item in items:
        story.append(_paragraph(item, styles["body"]))

    return story


def _build_bullet_section(title: str, items: list[str], styles) -> list:
    story = [_paragraph(title, styles["section_heading"])]

    for item in items:
        story.append(Paragraph(f"&#8226; {escape(item)}", styles["bullet"]))

    return story


def _build_grouped_section(title: str, groups: dict[str, list[str]], styles) -> list:
    story = [_paragraph(title, styles["section_heading"])]

    for group_name, items in groups.items():
        story.append(_paragraph(group_name, styles["subsection_heading"]))
        for item in items:
            story.append(Paragraph(f"&#8226; {escape(item)}", styles["bullet"]))

    return story


def _build_vocabulary(report, styles) -> list:
    story = [_paragraph("Vocabulary", styles["section_heading"])]

    for item in report.vocabulary:
        story.append(
            Paragraph(
                f"<b>{escape(item.term)}</b>: {escape(item.definition)}",
                styles["vocabulary"],
            )
        )

    return story


def _build_sources(report, styles) -> list:
    story = [_paragraph("Sources", styles["section_heading"])]

    for source in report.sources:
        story.append(
            Paragraph(
                f"<b>{escape(source.name)}</b>: {escape(source.url)}",
                styles["source"],
            )
        )

    return story


def _build_credits(report, styles) -> list:
    return [
        _paragraph("Credits", styles["section_heading"]),
        _paragraph(report.credits, styles["credits"]),
    ]


def build_report(output_path: str | Path = DEFAULT_OUTPUT) -> Path:
    """
    Build the PDF report.

    Args:
        output_path: Output PDF path.

    Returns:
        Resolved output path.
    """

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
        author="ChatGPT",
    )

    story = []
    story.extend(_build_title(report, styles))
    story.append(HRFlowable(width="100%"))
    story.append(Spacer(1, 10))
    story.extend(_build_text_section("Lead", [report.lead], styles))
    story.extend(_build_bullet_section("Latest Updates", report.latest_updates, styles))
    story.extend(_build_grouped_section("Key Themes", report.key_themes, styles))
    story.extend(
        _build_grouped_section(
            "International Comments",
            report.international_comments,
            styles,
        )
    )
    story.extend(_build_vocabulary(report, styles))
    story.extend(_build_sources(report, styles))
    story.extend(_build_credits(report, styles))

    doc.build(story)

    return output_file


def main() -> None:
    """Generate the default PDF when this file is run directly."""

    generated_file = build_report(DEFAULT_OUTPUT)
    print(f"Generated report: {generated_file}")


if __name__ == "__main__":
    main()

