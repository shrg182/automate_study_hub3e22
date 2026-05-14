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
        story.append(Paragraph(f"• {item}", styles["body"]))

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
        story.append(Paragraph(item, styles["body"]))

    return story


def _build_vocabulary_section(report, styles) -> list:
    story = [
        Paragraph("Vocabulary", styles["section_heading"])
    ]

    for item in report.vocabulary:
        story.append(
            Paragraph(f"{item.term}: {item.definition}", styles["body"])
        )

    return story


def _build_credits(report, styles) -> list:
    return [
        Paragraph("Credits", styles["section_heading"]),
        Paragraph(report.credits, styles["body"]),
    ]


def _build_report_content(report, styles) -> list:
    story = []
    story.extend(_build_title(report, styles))
    story.extend(_build_breaking_news(report, styles))
    story.append(HRFlowable(width="100%", thickness=1, color="black"))
    story.extend(_build_bullet_section(
        "Latest Updates", report.latest_updates, styles))
    story.append(Spacer(1, 10))
    story.extend(_build_text_section(
        "Participants", report.participants, styles))
    story.append(Spacer(1, 10))
    story.extend(_build_text_section(
        "Visit to Tiantan Park", report.visit_to_tiantan_park, styles))
    story.append(Spacer(1, 10))
    story.extend(_build_vocabulary_section(report, styles))
    story.append(Spacer(1, 10))
    story.extend(_build_credits(report, styles))

    return story


def build_report(output_path: Path) -> Path:
    """
    Build the PDF report.

    Args:
        output_path: Path to save the generated PDF.

    Returns:
        Path to the generated PDF file.
    """
    report = build_sample_report_content()

    styles = build_styles()

    story = []
    story.extend(_build_title(report, styles))
    story.append(HRFlowable(width="100%", thickness=1, color="black"))
    story.extend(_build_bullet_section(
        "Latest Updates", report.latest_updates, styles))
    story.append(Spacer(1, 10))
    story.extend(_build_bullet_section(
        "Participants", report.participants, styles))
    story.append(Spacer(1, 10))
    story.extend(_build_text_section(
        "Visit to Tiantan Park",
                 report.visit_to_tiantan_park, styles))
    story.append(Spacer(1, 10))
    story.extend(_build_vocabulary_section(report, styles))
    story.append(Spacer(1, 10))
    story.extend(_build_credits(report, styles))

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
    )

    doc.build(story)

    return output_path


def main() -> None:
    """Run the script."""
    print("This is a placeholder script for generator.")


if __name__ == "__main__":
    main()
