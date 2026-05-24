# Voice Reading Instruction PDF

Date: May 24, 2026  
Credit: Created by ChatGPT/Codex for the Automate Study Hub news report materials.

This folder generates a PDF instruction document about reading PDFs aloud. The README documents the PDF generation workflow only; the instructional handout text is maintained in `generator.py` and exported to `voice_reading_instruction.pdf`.

## Output

The generated PDF is:

```text
voice_reading_instruction.pdf
```

## Files

- `cli.py`: Command-line entry point for generating the PDF.
- `generator.py`: Defines the PDF content, page structure, and build function.
- `styles.py`: Defines ReportLab paragraph styles used by the PDF.
- `voice_reading_instruction.pdf`: Generated instruction document.
- `data_model.py`: Placeholder file reserved for future structured content models.

## Requirements

The generator uses Python 3 and ReportLab.

Check that ReportLab is available:

```bash
python3 -c "import reportlab; print(reportlab.Version)"
```

## Generate the PDF

From the repository root, run:

```bash
python3 news_reports/voice_reading_instruction/cli.py
```

This writes the default output file to:

```text
news_reports/voice_reading_instruction/voice_reading_instruction.pdf
```

## Generate to a Custom Path

Use `--output` to write the PDF somewhere else:

```bash
python3 news_reports/voice_reading_instruction/cli.py --output /tmp/voice_reading_instruction.pdf
```

## Edit the PDF Content

To change the instructional handout text, edit the `SECTIONS` list in:

```text
generator.py
```

Then regenerate the PDF with the CLI command above.

## Edit the PDF Styling

To change typography, spacing, colors, or metadata styling, edit:

```text
styles.py
```

Then regenerate the PDF.

## Verification

After generation, verify that the PDF exists:

```bash
ls -lh news_reports/voice_reading_instruction/voice_reading_instruction.pdf
```

Optionally verify the Python files compile:

```bash
python3 -m py_compile \
  news_reports/voice_reading_instruction/cli.py \
  news_reports/voice_reading_instruction/generator.py \
  news_reports/voice_reading_instruction/styles.py
```
