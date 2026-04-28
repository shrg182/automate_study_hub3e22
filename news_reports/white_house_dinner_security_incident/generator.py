#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (
    Paragraph, SimpleDocTemplate, Spacer, HRFlowable
)

from data_model import build_sample_report_content
from styles import build_styles


PAGE_WIDTH, PAGE_HEIGHT = A4


def _format_date(d):
    return d.strftime("%B %d, %Y")


def _build_title(report, styles):
    return [
        Paragraph(report.title, styles["title"]),
        Paragraph(report.author_line, styles["author"]),
        Paragraph(f"As of {_format_date(report.as_of_date)}", styles["author"]),
        Spacer(1, 10),
    ]


def _build_news(report, styles):
    story = [Paragraph("Breaking News", styles["section_heading"])]

    for n in report.news:
        story.append(Paragraph(f"<b>{n.title}</b>", styles["body"]))
        story.append(Paragraph(n.content, styles["body"]))

    return story


def _build_summary(report, styles):
    story = [Paragraph("Executive Summary", styles["section_heading"])]

    for item in report.executive_summary:
        story.append(Paragraph(f"• {item}", styles["bullet"]))

    return story


def _build_risk(report, styles):
    story = [Paragraph("Risk Assessment", styles["section_heading"])]

    for item in report.risk_assessment:
        story.append(Paragraph(f"• {item}", styles["bullet"]))

    return story


def _build_comments(report, styles):
    story = [Paragraph("Comments", styles["section_heading"])]

    for c in report.comments:
        story.append(Paragraph(c, styles["body"]))

    return story


def _build_editorial(report, styles):
    story = [Paragraph("Editor Note", styles["section_heading"])]

    # Placeholder for editorial content
    story.append(Paragraph(
        "This report combines AI-generated factual content from ChatGPT with analytical insights provided by Anthropic.",
        styles["body"]
    ))

    return story


def _build_vocab(report, styles):
    story = [Paragraph("New Vocabulary", styles["section_heading"])]

    for v in report.vocabulary:
        story.append(
            Paragraph(f"<b>{v.term}</b>: {v.definition}", styles["vocabulary"])
        )

    return story


def _build_credits_section(styles: dict) -> list:
    """
    Build the attribution / credits section.
    """
    story = []

    story.append(Paragraph("Credits", styles["section_heading"]))

    story.append(
        Paragraph(
            "This report combines AI-generated factual content from ChatGPT "
            "with analytical insights provided by Anthropic, an AI-powered "
            "analysis platform.",
            styles["credits"],
        )
    )

    return story


def build_report(output_path: str | Path) -> Path:
    output = Path(output_path).resolve()

    styles = build_styles()
    report = build_sample_report_content()

    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
    )

    story = []

    story.extend(_build_title(report, styles))
    story.append(HRFlowable(width="100%"))
    story.append(Spacer(1, 10))

    story.extend(_build_news(report, styles))
    story.extend(_build_summary(report, styles))
    story.extend(_build_risk(report, styles))
    story.extend(_build_comments(report, styles))
    story.extend(_build_vocab(report, styles))
    story.append(Spacer(1, 12))
    story.extend(_build_credits_section(styles))

    doc.build(story)

    return output