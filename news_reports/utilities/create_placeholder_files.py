#!/usr/bin/env python3
"""
create_placeholder_files.py

Create placeholder files and starter scripts for the world peace PDF report.

This script:
- creates placeholder text files
- creates README.md files
- creates starter Python script files
- creates missing parent directories automatically
"""

from __future__ import annotations

from pathlib import Path


def create_empty_file(file_path: Path) -> None:
    """
    Create an empty file, along with any missing parent directories.

    Args:
        file_path: Full path to the file to create.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        print(f"Skipped existing file: {file_path.resolve()}")
        return

    file_path.touch()
    print(f"Created file: {file_path.resolve()}")


def write_text_file(file_path: Path, content: str, overwrite: bool = True) -> None:
    """
    Write text content to a file, creating parent directories if needed.

    Args:
        file_path: Full path to the file.
        content: Text content to write.
        overwrite: Whether to overwrite the file if it already exists.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists() and not overwrite:
        print(f"Skipped existing file: {file_path.resolve()}")
        return

    file_path.write_text(content, encoding="utf-8")
    print(f"Wrote file: {file_path.resolve()}")


def create_placeholder_files(base_path: Path) -> None:
    """
    Create placeholder text files and README files.

    Args:
        base_path: Base directory for the world peace report structure.
    """
    edited_dir = base_path / "world_peace_report_edited"
    generated_dir = base_path / "world_peace_report_generated"

    create_empty_file(edited_dir / "placeholder.txt")
    create_empty_file(generated_dir / "placeholder.txt")

    write_text_file(
        edited_dir / "README.md",
        (
            "# World Peace Report Edited\n\n"
            "This directory contains edited versions, notes, and draft "
            "materials for the world peace report.\n"
        ),
    )

    write_text_file(
        generated_dir / "README.md",
        (
            "# World Peace Report Generated\n\n"
            "This directory contains generated output files such as PDF "
            "reports and related exports.\n"
        ),
    )


def create_placeholder_python_scripts(base_path: Path) -> None:
    """
    Create starter Python script files for the edited report workflow.

    Args:
        base_path: Base directory for the world peace report structure.
    """
    edited_dir = base_path

    script_templates: dict[str, str] = {
        "placeholder.py": (
            "#!/usr/bin/env python3\n"
            "\"\"\"Placeholder Python script for the world peace report.\"\"\"\n\n"
            "from __future__ import annotations\n\n\n"
            "def main() -> None:\n"
            "    \"\"\"Run the placeholder script.\"\"\"\n"
            "    print(\"Placeholder script\")\n\n\n"
            "if __name__ == \"__main__\":\n"
            "    main()\n"
        ),
        "generator.py": (
            "#!/usr/bin/env python3\n"
            "\"\"\"PDF generator for the world peace report.\"\"\"\n\n"
            "from __future__ import annotations\n\n\n"
            "def main() -> None:\n"
            "    \"\"\"Run the PDF generator.\"\"\"\n"
            "    print(\"Generate report here.\")\n\n\n"
            "if __name__ == \"__main__\":\n"
            "    main()\n"
        ),
        "data_model.py": (
            "#!/usr/bin/env python3\n"
            "\"\"\"Data models for the world peace report.\"\"\"\n\n"
            "from __future__ import annotations\n"
        ),
        "cli.py": (
            "#!/usr/bin/env python3\n"
            "\"\"\"Command-line entry point for the world peace report.\"\"\"\n\n"
            "from __future__ import annotations\n\n\n"
            "def main() -> None:\n"
            "    \"\"\"Run the command-line interface.\"\"\"\n"
            "    print(\"CLI entry point\")\n\n\n"
            "if __name__ == \"__main__\":\n"
            "    main()\n"
        ),
        "styles.py": (
            "#!/usr/bin/env python3\n"
            "\"\"\"Styles for the world peace report.\"\"\"\n\n"
            "from __future__ import annotations\n\n\n"
            "def main() -> None:\n"
            "    \"\"\"Run the styles module.\"\"\"\n"
            "    print(\"Define styles here.\")\n\n\n"
            "if __name__ == \"__main__\":\n"
            "    main()\n"
        ),
    }

    for filename, content in script_templates.items():
        write_text_file(edited_dir / filename, content, overwrite=False)


def main() -> None:
    """
    Entry point for the script.
    """
    project_dir = Path(__file__).resolve().parent.parent
    target_path = project_dir / "white_house_dinner_security_incident"
    target_path.mkdir(parents=True, exist_ok=True)

    create_placeholder_files(target_path)
    create_placeholder_python_scripts(target_path)


if __name__ == "__main__":
    main()