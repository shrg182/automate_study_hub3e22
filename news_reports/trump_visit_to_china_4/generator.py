#!/usr/bin/env python3
"""
generator.py

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


def _format_date(d) -> str:
    """
    Format report date.
    """
    return d.strftime("%B %d, %Y")


def _build_title(report, styles) -> list:
    return [
        Paragraph(report.title, styles["title"]),
        Paragraph(report.author_line, styles["author"]),
        Paragraph(
            f"As of {_format_date(report.as_of_date)}",
            styles["author"],
        ),
        Spacer(1, 10),
    ]


def _build_breaking_news(report, styles) -> list:
    return [
        Paragraph("Breaking News", styles["section_heading"]),
        Paragraph(report.breaking_news, styles["body"]),
    ]


def _build_bullet_section(
    title: str,
    items: list[str],
    styles,
) -> list:
    story = [
        Paragraph(title, styles["section_heading"])
    ]

    for item in items:
        story.append(
            Paragraph(f"• {item}", styles["bullet"])
        )

    return story


def _build_text_section(
    title: str,
    items: list[str],
    styles,
) -> list:
    story = [
        Paragraph(title, styles["section_heading"])
    ]

    for item in items:
        story.append(
            Paragraph(item, styles["body"])
        )

    return story


def _build_vocabulary(report, styles) -> list:
    story = [
        Paragraph("New Vocabulary", styles["section_heading"])
    ]

    for item in report.vocabulary:
        story.append(
            Paragraph(
                f"<b>{item.term}</b>: {item.definition}",
                styles["vocabulary"],
            )
        )

    return story


def _build_credits(report, styles) -> list:
    return [
        Paragraph("Credits", styles["section_heading"]),
        Paragraph(report.credits, styles["credits"]),
    ]


def build_report(output_path: str | Path) -> Path:
    """
    Build the PDF report.

    Args:
        output_path: Output PDF path.

    Returns:
        Resolved output path.
    """

    output_file = Path(output_path).resolve()

    styles = build_styles()
    report = build_sample_report_content()

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

    story.extend(
        _build_text_section(
            "Key Events Timeline",
            report.key_events_timeline,
            styles,
        )
    )

    story.extend(
        _build_bullet_section(
            "Trump's Remarks",
            report.trump_remarks,
            styles,
        )
    )

    story.extend(
        _build_text_section(
            "Comments",
            report.comments,
            styles,
        )
    )

    story.extend(_build_vocabulary(report, styles))

    story.extend(_build_credits(report, styles))

    doc.build(story)

    return output_file
