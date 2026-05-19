#!/usr/bin/env python3
"""
generator.py

Generate the Trump China Visit Report PDF.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

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


def _build_breaking_news(report, styles) -> list:
    return [
        _paragraph("Breaking News", styles["section_heading"]),
        _paragraph(report.breaking_news, styles["body"]),
    ]


def _build_nested_comments(title: str, comment_groups: dict, styles) -> list:
    story = [_paragraph(title, styles["section_heading"])]

    for group_name, group_value in comment_groups.items():
        story.append(_paragraph(str(group_name), styles["subsection_heading"]))

        if isinstance(group_value, dict):
            for source_name, comments in group_value.items():
                story.append(
                    Paragraph(
                        f"<b>{escape(str(source_name))}</b>",
                        styles["body"],
                    )
                )
                for comment in comments:
                    story.append(Paragraph(f"&#8226; {escape(comment)}", styles["bullet"]))
        else:
            for comment in group_value:
                story.append(Paragraph(f"&#8226; {escape(comment)}", styles["bullet"]))

    return story


def _build_vocabulary(report, styles) -> list:
    story = [_paragraph("New Vocabulary", styles["section_heading"])]

    for item in report.vocabulary:
        story.append(
            Paragraph(
                f"<b>{escape(item.term)}</b>: {escape(item.definition)}",
                styles["vocabulary"],
            )
        )

    return story


def _build_appendices(report, styles) -> list:
    story = [_paragraph("Appendices", styles["section_heading"])]

    for appendix in report.appendices:
        story.append(_paragraph(appendix["title"], styles["subsection_heading"]))
        for item in appendix["content"]:
            story.append(Paragraph(f"&#8226; {escape(item)}", styles["bullet"]))

    return story


def _build_credits(styles) -> list:
    return [
        _paragraph("Credits", styles["section_heading"]),
        _paragraph(
            "Generated with ReportLab from the local study-hub data model.",
            styles["credits"],
        ),
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
    output_file.parent.mkdir(parents=True, exist_ok=True)

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
    story.extend(_build_breaking_news(report, styles))
    story.extend(
        _build_bullet_section(
            "Executive Summary",
            report.executive_summary,
            styles,
        )
    )
    story.extend(
        _build_text_section(
            "Situation Analysis",
            report.situation_analysis,
            styles,
        )
    )
    story.extend(
        _build_nested_comments(
            "International Comments",
            report.international_comments,
            styles,
        )
    )
    story.extend(
        _build_nested_comments(
            "Domestic U.S. Comments",
            report.domestic_us_comments,
            styles,
        )
    )
    story.extend(
        _build_text_section(
            "ChatGPT Comments",
            report.chatgpt_comments,
            styles,
        )
    )
    story.extend(_build_vocabulary(report, styles))
    story.extend(_build_appendices(report, styles))
    story.extend(_build_credits(styles))

    doc.build(story)

    return output_file


def main() -> None:
    """Generate the default PDF when this file is run directly."""
    generated_file = build_report("trump_china_visit_report_20260518.pdf")
    print(f"Generated report: {generated_file}")


if __name__ == "__main__":
    main()
