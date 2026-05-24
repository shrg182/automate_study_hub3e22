#!/usr/bin/env python3
"""
Generate a PDF instruction document for reading PDFs aloud.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import HRFlowable, ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer

from styles import build_styles


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT = BASE_DIR / "voice_reading_instruction.pdf"


@dataclass(frozen=True, slots=True)
class InstructionSection:
    """One section in the instruction PDF."""

    title: str
    intro: str = ""
    steps: list[str] = field(default_factory=list)
    code_blocks: list[str] = field(default_factory=list)
    bullets: list[str] = field(default_factory=list)
    tip: str = ""


SECTIONS = [
    InstructionSection(
        title="Before You Start",
        intro="Check whether the PDF has selectable text before choosing a read-aloud tool.",
        steps=[
            "Check whether the PDF has selectable text.",
            "Try selecting one sentence with your mouse or finger.",
            "If you can select the words, most read-aloud tools should work.",
            "If you cannot select the words, the PDF is probably scanned as images. Use OCR first to convert the pages into searchable, selectable text.",
        ],
    ),
    InstructionSection(
        title="Option 1: Microsoft Edge",
        intro="Best for Windows users who already have Edge installed.",
        steps=[
            "Open the PDF with Microsoft Edge.",
            "Select Read aloud in the PDF toolbar.",
            "If the toolbar is hidden, right-click the PDF page and choose Read aloud.",
            "Use the toolbar to pause, resume, change voice, or change speed.",
        ],
        code_blocks=["Ctrl + Shift + U"],
    ),
    InstructionSection(
        title="Option 2: Adobe Acrobat Reader",
        intro="Best when Acrobat Reader is already installed.",
        steps=[
            "Open the PDF in Adobe Acrobat Reader.",
            "Go to View > Read Out Loud > Activate Read Out Loud.",
            "Choose Read This Page Only or Read To End of Document.",
        ],
        code_blocks=[
            "View > Read Out Loud > Activate Read Out Loud",
            "View > Read Out Loud > Read This Page Only",
            "View > Read Out Loud > Read To End of Document",
        ],
    ),
    InstructionSection(
        title="Option 3: Windows Built-In Narrator",
        intro="Best when you cannot install another PDF reader.",
        steps=[
            "Open the PDF in a reader that lets you select or search text.",
            "Start Narrator with Windows logo key + Ctrl + Enter.",
            "Use the keyboard to move through the document.",
            "Stop Narrator with the same shortcut.",
        ],
        code_blocks=["Windows logo key + Ctrl + Enter"],
        tip="Windows Narrator is built into Windows, so it does not require a separate download.",
    ),
    InstructionSection(
        title="Option 4: macOS Built-In Spoken Content",
        intro="Best for Mac users who want a system-level option.",
        steps=[
            "Open the PDF.",
            "Select the text you want to hear.",
            "Press the system speech shortcut.",
            "To set it up, open System Settings > Accessibility > Spoken Content > Speak selection. Then choose a shortcut, voice, and speaking speed.",
        ],
        code_blocks=["System Settings > Accessibility > Spoken Content > Speak selection"],
    ),
    InstructionSection(
        title="Option 5: iPhone or iPad Speak Screen",
        intro="Best for reading a PDF on an Apple mobile device.",
        steps=[
            "Open Settings.",
            "Go to Accessibility > Read & Speak.",
            "Turn on Speak Selection or Speak Screen.",
            "Open the PDF.",
            "Select text and tap Speak, or swipe down with two fingers from the top of the screen to read the screen.",
        ],
        code_blocks=["Accessibility > Read & Speak"],
    ),
    InstructionSection(
        title="Option 6: Android Select to Speak or Built-In Screen Reader",
        intro="Best for reading on an Android phone or tablet.",
        steps=[
            "Open Settings.",
            "Go to Accessibility > Select to Speak.",
            "Turn on the feature.",
            "Open the PDF and select the text or area to read.",
        ],
        code_blocks=["Accessibility > Select to Speak"],
        tip="If Select to Speak is not available, look for your device's built-in screen reader or text-to-speech settings. The exact name may vary by phone brand and Android version.",
    ),
    InstructionSection(
        title="Option 7: Local PDF Readers or Office Apps",
        intro="Best when Edge, Acrobat, Google services, or cloud features are not available.",
        bullets=[
            "Foxit PDF Reader",
            "WPS Office",
            "PDF-XChange Editor",
            "Look for menu items named Read Aloud, Read Out Loud, Speech, Text to Speech, or Accessibility.",
        ],
        tip="Availability and menu names vary by country, device, and version. Install PDF readers only from official or trusted local sources.",
    ),
    InstructionSection(
        title="Option 8: Copy Text into a Local Text-to-Speech Tool",
        intro="Best as a fallback when the PDF reader cannot read aloud.",
        steps=[
            "Select and copy the text from the PDF.",
            "Paste it into a local app that supports text-to-speech, such as a word processor, notes app, or operating-system speech tool.",
            "Use the app's read-aloud or speech command.",
        ],
        tip="Do not upload private, school, medical, legal, or work documents to unknown online text-to-speech websites.",
    ),
    InstructionSection(
        title="If You Are in a Restricted-Access Region",
        intro="Some tools, app stores, browser extensions, cloud voices, or online text-to-speech services may not be reachable in every country or network environment.",
        steps=[
            "Prefer built-in operating system tools first: Windows Narrator, macOS Spoken Content, iPhone/iPad Speak Screen, or Android accessibility speech.",
            "Use local/offline voices installed on the device when available.",
            "Install PDF readers only from official or trusted local sources.",
            "Avoid workflows that require uploading the PDF to a website.",
            "If the file is scanned, use an offline OCR tool when privacy or internet access is a concern.",
        ],
    ),
    InstructionSection(
        title="Troubleshooting",
        bullets=[
            "If nothing is read aloud, check that the PDF text is selectable.",
            "If the reading order is wrong, the PDF may need accessibility tags or OCR cleanup.",
            "If the voice sounds unnatural, install another system voice or choose a different voice in the tool's settings.",
            "If a shortcut does not work, check whether another app is using the same shortcut.",
            "If a tool is unavailable, use a built-in system option or a local PDF reader instead.",
        ],
    ),
    InstructionSection(
        title="References",
        bullets=[
            "Microsoft Edge: Read Aloud for PDFs",
            "Adobe Acrobat Reader: Read Out Loud",
            "Microsoft Windows: Narrator",
            "Apple macOS: Spoken Content",
            "Apple iPhone/iPad: Speak Screen and Speak Selection",
            "Android: Select to Speak",
        ],
    ),
]


def _paragraph(text: str, style) -> Paragraph:
    """Create an escaped paragraph."""

    return Paragraph(escape(text), style)


def _code(text: str, style) -> Paragraph:
    """Create a code-style paragraph."""

    return Paragraph(escape(text), style)


def _numbered_list(items: list[str], style) -> ListFlowable:
    """Create a numbered list."""

    return ListFlowable(
        [ListItem(_paragraph(item, style)) for item in items],
        bulletType="1",
        start="1",
        leftIndent=16,
        bulletFontName="Helvetica",
        bulletFontSize=9,
        bulletOffsetY=1,
    )


def _bullet_list(items: list[str], style) -> ListFlowable:
    """Create a bullet list."""

    return ListFlowable(
        [ListItem(_paragraph(item, style)) for item in items],
        bulletType="bullet",
        leftIndent=14,
        bulletFontName="Helvetica",
        bulletFontSize=8,
        bulletOffsetY=1,
    )


def _build_section(section: InstructionSection, styles) -> list:
    """Build one instruction section."""

    story = [_paragraph(section.title, styles["section_heading"])]
    if section.intro:
        story.append(_paragraph(section.intro, styles["body"]))
    if section.steps:
        story.append(_numbered_list(section.steps, styles["list_item"]))
    for code_block in section.code_blocks:
        story.append(_code(code_block, styles["code"]))
    if section.bullets:
        story.append(_bullet_list(section.bullets, styles["list_item"]))
    if section.tip:
        story.append(_paragraph(section.tip, styles["note"]))
    return story


def build_instruction_pdf(output_path: str | Path = DEFAULT_OUTPUT) -> Path:
    """Build the voice reading instruction PDF and return its resolved path."""

    output_file = Path(output_path).resolve()
    output_file.parent.mkdir(parents=True, exist_ok=True)
    styles = build_styles()

    doc = SimpleDocTemplate(
        str(output_file),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="How to Read a PDF Aloud",
        author="Codex and ChatGPT",
    )

    story = [
        _paragraph("How to Read a PDF Aloud", styles["title"]),
        _paragraph("Date: May 24, 2026", styles["meta"]),
        _paragraph(
            "Credit: Created by ChatGPT/Codex for the Automate Study Hub news report materials.",
            styles["meta"],
        ),
        _paragraph(
            "Several practical ways to hear a PDF read aloud, including built-in and offline options for limited-access environments.",
            styles["subtitle"],
        ),
        HRFlowable(width="100%", color="#C8D6E5", thickness=1),
        Spacer(1, 6),
    ]

    for index, section in enumerate(SECTIONS):
        if section.title == "Option 6: Android Select to Speak or Built-In Screen Reader":
            story.append(PageBreak())
        elif index > 0:
            story.append(Spacer(1, 2))
        story.extend(_build_section(section, styles))

    doc.build(story)
    return output_file


def main() -> None:
    """Generate the default instruction PDF."""

    print(build_instruction_pdf())


if __name__ == "__main__":
    main()
