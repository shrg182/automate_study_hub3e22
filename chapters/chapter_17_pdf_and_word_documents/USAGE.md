# Usage Guide

### Chapter 17 Pdf And Word Documents

_Auto-generated on 2026-05-25 17:15:02_

> 📖 **Chapter Page:**   
> 🔗 **ATBS Chapter Link:** 

**Directory:** `chapter_17_pdf_and_word_documents`
**Relative path:** `chapters/chapter_17_pdf_and_word_documents`

---

## Overview

This file explains how to run scripts in this directory.

---

## Directory Tree

```text
chapter_17_pdf_and_word_documents/
|-- README.md
|-- USAGE.md
`-- utils.py
```

---

## Before Running Scripts

From the project root, activate the virtual environment:

```bash
source .venv/bin/activate
```

Check that Python is using the project virtual environment:

```bash
which python
python --version
```

---

## Run Scripts

Run a script from the project root:

```bash
python chapters/chapter_17_pdf_and_word_documents/example_01.py
```

Or change into this directory first:

```bash
cd chapters/chapter_17_pdf_and_word_documents
python example_01.py
```

---

## Common Commands

List files:

```bash
ls
```

Show current directory:

```bash
pwd
```

Run a Python file:

```bash
python filename.py
```

Run with help option, if supported:

```bash
python filename.py --help
```

---

## Script Examples

### `example_01.py`

```bash
python example_01.py
```

Description:

```text
Add description later.
```

### `example_02.py`

```bash
python example_02.py
```

Description:

```text
Add description later.
```

### `example_03.py`

```bash
python example_03.py
```

Description:

```text
Add description later.
```

---

## Troubleshooting

### Problem: `python: command not found`

Try:

```bash
python3 filename.py
```

### Problem: wrong Python environment

Check:

```bash
which python
```

Expected result should point to the project `.venv`.

### Problem: module not found

Install missing packages inside the virtual environment:

```bash
pip install package_name
```

Or install all project requirements:

```bash
pip install -r requirements.txt
```

---

## Ask questions

Use this section to collect questions about running scripts.

- Which script should be tested first?
- Does this script need command-line arguments?
- Should the output be saved to a file?
