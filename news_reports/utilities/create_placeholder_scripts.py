#!/usr/bin/env python3
"""
create_placeholder_scripts.py

This script generates placeholder scripts for the Trump visit to China news report. It creates a directory called "trump_visit_to_china" and populates it with empty Python files for each of the specified modules.
"""

from __future__ import annotations

from pathlib import Path
from typing_extensions import Final


PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "news_reports" / "putin_visit_to_china"

SCRIPT_NAMES = [
    "data_model",
    "styles",
    "generator",
    "cli"
]


PLACEHOLDER_TEMPLATE: str = '''#!/usr/bin/env python3
"""
{filename}

Placeholder script.

TODO:
    - Add description.
    - Add functionality.
    - Add main program logic.
"""

from __future__ import annotations


def main() -> None:
    """Run the script."""
    print("This is a placeholder script for {filename}.")

if __name__ == "__main__":
    main()
'''


def create_placeholder_scripts(output_dir: Path, filename: str) -> None:
    """Create a placeholder script with the given filename in the specified output directory."""

    output_dir.mkdir(parents=True, exist_ok=True)

    script_path = output_dir / f"{filename}.py"

    if script_path.exists():
        print(f"Script {script_path} already exists. Skipping.")
        return

    script_path.write_text(PLACEHOLDER_TEMPLATE.format(filename=filename))
    print(f"Created placeholder script: {script_path}")


def main() -> None:
    """Main function to create placeholder scripts."""
    for script_name in SCRIPT_NAMES:
        create_placeholder_scripts(OUTPUT_DIR, script_name)


if __name__ == "__main__":
    main()
