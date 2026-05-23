# Cuba Crisis News Report

2026-05-23 3:57 PM by Codex

This folder generates an educational PDF news report about the Cuban Missile Crisis of October-November 1962. The report includes English paragraphs, Russian translations under each paragraph, English/Russian vocabulary with English definitions, sources, credits, and asset-based images.

## Files

- `cli.py`: Command-line entry point for creating the PDF.
- `generator.py`: Builds the report layout, sections, asset images, vocabulary, sources, and credits.
- `data_model.py`: Stores the report text, Russian translations, vocabulary, source list, and metadata.
- `styles.py`: Defines ReportLab text styles and registers a Unicode font for Russian text when available.
- `news_report_request_list.csv`: Controls which sections appear and their order.
- `assets/`: Stores the report images used in the PDF.

## Generate the PDF

Run the generator from this folder:

```bash
cd news_reports/cuba_crisis
python3 cli.py
```

The default output is:

```text
cuba_crisis_report_20260523.pdf
```

You can also choose a custom output path:

```bash
python3 cli.py --output my_cuba_crisis_report.pdf
```

## Images Included

The `Asset Images` section uses only files from `assets/`:

- `cuba_crisis_2.png`
- `cuba_crisis.jpeg`
- `P-2H_Neptune_over_Soviet_ship_Oct_1962.jpeg`

The previous generated maps, charts, and illustrations are not included in the report output.

## Customize Sections

Edit `news_report_request_list.csv` to change section order or hide a section. Set `include` to `yes` or `no`.

Example:

```csv
order,requirement,include,specific_requirements
4,Asset Images,yes,
```

Supported built-in sections include:

- `Breaking News / Leads`
- `Key Themes`
- `Executive Summary`
- `Asset Images`
- `Situation Analysis`
- `Latest Updates`
- `Risk Assessment`
- `Comments`
- `New Vocabulary`
- `Sources`
- `Credits`

## Notes

The report date and credits are stored in `data_model.py`. The current report is dated May 23, 2026, and credits Codex with ChatGPT involvement.
