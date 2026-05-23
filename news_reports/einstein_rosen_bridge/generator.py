#!/usr/bin/env python3
"""
generator.py

Generate the Einstein-Rosen Bridge introduction PDF.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Image as ReportLabImage,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

from data_model import ReportContent, ReportSection, build_report_content
from styles import build_styles


MODULE_DIR = Path(__file__).resolve().parent
ASSET_DIR = MODULE_DIR / "assets"
IMAGE_WIDTH = 1600
IMAGE_HEIGHT = 900

SECTION_IMAGES = {
    "Basic Idea: A Bridge Through Spacetime": (
        "spacetime_bridge.png",
        "Illustration: two regions of spacetime connected by a curved bridge.",
    ),
    "Relationship Between Einstein-Rosen Bridges and Black Holes": (
        "black_hole_throat.png",
        "Illustration: black-hole exterior regions joined by a narrow throat.",
    ),
    "Why the Original Einstein-Rosen Bridge Is Not Traversable": (
        "traversability_comparison.png",
        "Illustration: the original bridge pinches closed, unlike a hypothetical held-open throat.",
    ),
}


def _font(size: int) -> ImageFont.ImageFont:
    """Return a readable default font."""
    try:
        return ImageFont.truetype("Arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


def _centered_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.ImageFont,
    fill: str,
) -> None:
    """Draw centered text."""
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    draw.text((xy[0] - width // 2, xy[1]), text, font=font, fill=fill)


def _draw_grid(draw: ImageDraw.ImageDraw, color: str = "#D8E5E8") -> None:
    """Draw a simple spacetime grid."""
    for x in range(80, IMAGE_WIDTH, 120):
        draw.line((x, 130, x - 180, 760), fill=color, width=2)
    for y in range(160, 780, 80):
        draw.arc((-80, y - 220, IMAGE_WIDTH + 80, y + 220), 8, 172, fill=color, width=2)


def _draw_spacetime_bridge(path: Path) -> None:
    """Create a spacetime bridge diagram."""
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "#F7FBFC")
    draw = ImageDraw.Draw(image)
    _draw_grid(draw)

    teal = "#006D77"
    ink = "#263238"
    coral = "#E76F51"

    draw.ellipse((220, 270, 620, 670), outline=teal, width=10)
    draw.ellipse((980, 270, 1380, 670), outline=teal, width=10)
    draw.arc((420, 250, 1180, 650), 180, 360, fill=coral, width=18)
    draw.arc((420, 290, 1180, 690), 0, 180, fill=coral, width=18)
    draw.line((620, 470, 980, 470), fill=coral, width=10)

    _centered_text(draw, (420, 690), "Region A", _font(42), ink)
    _centered_text(draw, (1180, 690), "Region B", _font(42), ink)
    _centered_text(draw, (800, 390), "Einstein-Rosen bridge", _font(44), ink)
    _centered_text(draw, (800, 70), "A geometric connection in spacetime", _font(50), teal)

    image.save(path)


def _draw_black_hole_throat(path: Path) -> None:
    """Create a black-hole throat diagram."""
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "#FBFAF7")
    draw = ImageDraw.Draw(image)
    ink = "#263238"
    teal = "#006D77"
    gray = "#5F6C72"
    gold = "#E9C46A"

    draw.rectangle((0, 0, IMAGE_WIDTH, IMAGE_HEIGHT), fill="#FBFAF7")
    draw.ellipse((150, 250, 550, 650), fill="#101820", outline=teal, width=12)
    draw.ellipse((1050, 250, 1450, 650), fill="#101820", outline=teal, width=12)
    draw.rounded_rectangle((500, 355, 1100, 545), radius=95, fill=gold, outline=teal, width=8)
    draw.ellipse((475, 330, 625, 570), fill="#FBFAF7", outline=teal, width=8)
    draw.ellipse((975, 330, 1125, 570), fill="#FBFAF7", outline=teal, width=8)

    for offset in range(0, 180, 30):
        draw.arc((120 + offset, 220 + offset // 3, 580 - offset, 680 - offset // 3), 205, 335, fill=gray, width=3)
        draw.arc((1020 + offset, 220 + offset // 3, 1480 - offset, 680 - offset // 3), 205, 335, fill=gray, width=3)

    _centered_text(draw, (350, 680), "black-hole exterior", _font(38), ink)
    _centered_text(draw, (1250, 680), "second exterior", _font(38), ink)
    _centered_text(draw, (800, 575), "narrow throat", _font(38), ink)
    _centered_text(draw, (800, 80), "Idealized black-hole geometry", _font(50), teal)

    image.save(path)


def _draw_traversability(path: Path) -> None:
    """Create a traversability comparison diagram."""
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "#F8FAFB")
    draw = ImageDraw.Draw(image)
    ink = "#263238"
    teal = "#006D77"
    red = "#D62828"
    green = "#2A9D8F"
    gray = "#D8E5E8"

    draw.line((120, 450, 680, 450), fill=gray, width=16)
    draw.polygon((360, 450, 480, 345, 480, 555), fill="#F8FAFB", outline=red)
    draw.line((120, 450, 350, 450), fill=red, width=12)
    draw.line((490, 450, 680, 450), fill=red, width=12)
    draw.line((240, 360, 530, 540), fill=red, width=10)
    draw.line((530, 360, 240, 540), fill=red, width=10)

    draw.rounded_rectangle((920, 340, 1480, 560), radius=105, fill="#DDF3F1", outline=green, width=10)
    draw.line((980, 450, 1420, 450), fill=green, width=14)
    draw.polygon((1420, 450, 1350, 405, 1350, 495), fill=green)

    _centered_text(draw, (400, 610), "Original bridge", _font(42), ink)
    _centered_text(draw, (400, 665), "pinches closed", _font(34), red)
    _centered_text(draw, (1200, 610), "Hypothetical traversable wormhole", _font(38), ink)
    _centered_text(draw, (1200, 665), "would need support to stay open", _font(32), green)
    _centered_text(draw, (800, 80), "Traversability is the key difference", _font(50), teal)

    image.save(path)


def ensure_illustrations() -> dict[str, Path]:
    """Create illustration PNGs used by the PDF."""
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    assets = {
        "spacetime_bridge.png": ASSET_DIR / "spacetime_bridge.png",
        "black_hole_throat.png": ASSET_DIR / "black_hole_throat.png",
        "traversability_comparison.png": ASSET_DIR / "traversability_comparison.png",
    }

    _draw_spacetime_bridge(assets["spacetime_bridge.png"])
    _draw_black_hole_throat(assets["black_hole_throat.png"])
    _draw_traversability(assets["traversability_comparison.png"])
    return assets


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


def _build_illustration(image_path: Path, caption: str, styles) -> list:
    """Build an illustration and caption."""
    return [
        Spacer(1, 4),
        ReportLabImage(str(image_path), width=150 * mm, height=84.375 * mm),
        Paragraph(escape(caption), styles["caption"]),
    ]


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
    illustrations = ensure_illustrations()

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
        image_info = SECTION_IMAGES.get(section.title)
        if image_info is not None:
            filename, caption = image_info
            story.extend(_build_illustration(illustrations[filename], caption, styles))

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
