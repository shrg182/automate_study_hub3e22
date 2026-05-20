#!/usr/bin/env python3
"""
news_report_request_list.py

1. Create a folder for the news report
2. Write a list of the requirements for the report:
    Breaking News / Leads
    Key Themes
    Executive Summary
    Situation Analysis
    Latest Updates
    Risk Assessment
    Comments
    New Vocabulary
    Sources
    Credits

3. Option to add items in the requirement list
4. Each requirement has an option to add specific requirements.

In general, this script produces a CSV file by user's inputs. This CSV file
will be used as the instruction for future news report generation.

Usage:
    python3 news_report_request_list.py
    python3 news_report_request_list.py --report-folder putin_visit_to_china_3
    python3 news_report_request_list.py --report-folder putin_visit_to_china_3 --defaults-only
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


DEFAULT_REQUIREMENTS: tuple[str, ...] = (
    "Breaking News / Leads",
    "Key Themes",
    "Executive Summary",
    "Situation Analysis",
    "Latest Updates",
    "Risk Assessment",
    "Comments",
    "New Vocabulary",
    "Sources",
    "Credits",
)
DEFAULT_CSV_NAME = "news_report_request_list.csv"
CSV_FIELDNAMES = [
    "order",
    "requirement",
    "include",
    "specific_requirements",
]


@dataclass(slots=True)
class ReportRequirement:
    """Represent one requested report section."""

    order: int
    requirement: str
    include: bool = True
    specific_requirements: str = ""

    def to_csv_row(self) -> dict[str, str]:
        """Convert the requirement to a CSV row."""

        return {
            "order": str(self.order),
            "requirement": self.requirement,
            "include": "yes" if self.include else "no",
            "specific_requirements": self.specific_requirements,
        }


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Create and edit a CSV request list for a news report."
    )
    parser.add_argument(
        "--report-folder",
        type=str,
        default="",
        help="Folder name to create under news_reports.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=DEFAULT_CSV_NAME,
        help=f"CSV filename to create inside the report folder (default: {DEFAULT_CSV_NAME}).",
    )
    parser.add_argument(
        "--defaults-only",
        action="store_true",
        help="Create the CSV with default requirements and skip the interactive menu.",
    )

    return parser.parse_args()


def project_news_reports_dir() -> Path:
    """Return the repository news_reports directory."""

    return Path(__file__).resolve().parent.parent


def normalize_folder_name(folder_name: str) -> str:
    """Normalize a user-provided folder name for filesystem use."""

    cleaned = folder_name.strip().replace(" ", "_")
    cleaned = "".join(char for char in cleaned if char.isalnum() or char in "-_")
    return cleaned.lower()


def prompt_report_folder(default_name: str = "news_report_request") -> str:
    """Prompt for the news report folder name."""

    raw_name = input(f"News report folder [{default_name}]: ").strip()
    return normalize_folder_name(raw_name or default_name)


def build_default_requirements() -> list[ReportRequirement]:
    """Create default report requirements."""

    return [
        ReportRequirement(order=index, requirement=requirement)
        for index, requirement in enumerate(DEFAULT_REQUIREMENTS, start=1)
    ]


def renumber_requirements(requirements: list[ReportRequirement]) -> None:
    """Keep requirement order values in list order."""

    for index, requirement in enumerate(requirements, start=1):
        requirement.order = index


def parse_include(value: str) -> bool:
    """Parse the CSV include column."""

    return value.strip().lower() in {"1", "true", "yes", "y", "include"}


def load_requirements(csv_path: Path) -> list[ReportRequirement]:
    """Load existing requirements from a CSV file."""

    if not csv_path.exists():
        return build_default_requirements()

    with csv_path.open("r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        requirements = [
            ReportRequirement(
                order=int(row.get("order") or index),
                requirement=row.get("requirement", "").strip(),
                include=parse_include(row.get("include", "yes")),
                specific_requirements=row.get("specific_requirements", "").strip(),
            )
            for index, row in enumerate(reader, start=1)
            if row.get("requirement", "").strip()
        ]

    renumber_requirements(requirements)
    return requirements or build_default_requirements()


def save_requirements(requirements: list[ReportRequirement], csv_path: Path) -> None:
    """Save requirements to CSV."""

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    renumber_requirements(requirements)

    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()
        writer.writerows(requirement.to_csv_row() for requirement in requirements)

    print(f"Saved CSV: {csv_path.resolve()}")


def display_requirements(requirements: list[ReportRequirement]) -> None:
    """Display current requirements."""

    if not requirements:
        print("No requirements found.")
        return

    print("\nNews Report Request List:")
    for item in requirements:
        status = "yes" if item.include else "no"
        details = item.specific_requirements or "(default)"
        print(f"{item.order}. [{status}] {item.requirement} - {details}")


def prompt_requirement_number(requirements: list[ReportRequirement], action: str) -> int | None:
    """Prompt for a requirement number and return its zero-based index."""

    display_requirements(requirements)

    if not requirements:
        return None

    try:
        number = int(input(f"Enter requirement number to {action}: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    if not 1 <= number <= len(requirements):
        print("Invalid requirement number.")
        return None

    return number - 1


def add_requirement(requirements: list[ReportRequirement]) -> None:
    """Add a new report requirement."""

    requirement = input("New requirement name: ").strip()
    if not requirement:
        print("Requirement name cannot be empty.")
        return

    specifics = input("Specific requirements (optional): ").strip()
    requirements.append(
        ReportRequirement(
            order=len(requirements) + 1,
            requirement=requirement,
            specific_requirements=specifics,
        )
    )
    print(f"Added requirement: {requirement}")


def edit_specific_requirements(requirements: list[ReportRequirement]) -> None:
    """Edit details for a selected requirement."""

    index = prompt_requirement_number(requirements, "edit")
    if index is None:
        return

    selected = requirements[index]
    print(f"Current details: {selected.specific_requirements or '(default)'}")
    specifics = input("New specific requirements: ").strip()
    selected.specific_requirements = specifics
    print(f"Updated: {selected.requirement}")


def rename_requirement(requirements: list[ReportRequirement]) -> None:
    """Rename a selected requirement."""

    index = prompt_requirement_number(requirements, "rename")
    if index is None:
        return

    selected = requirements[index]
    new_name = input(f"New name for '{selected.requirement}': ").strip()
    if not new_name:
        print("Requirement name cannot be empty.")
        return

    selected.requirement = new_name
    print(f"Renamed requirement to: {new_name}")


def toggle_requirement(requirements: list[ReportRequirement]) -> None:
    """Toggle whether a requirement should be included."""

    index = prompt_requirement_number(requirements, "toggle")
    if index is None:
        return

    selected = requirements[index]
    selected.include = not selected.include
    status = "included" if selected.include else "excluded"
    print(f"{selected.requirement} is now {status}.")


def remove_requirement(requirements: list[ReportRequirement]) -> None:
    """Remove a selected requirement."""

    index = prompt_requirement_number(requirements, "remove")
    if index is None:
        return

    removed = requirements.pop(index)
    renumber_requirements(requirements)
    print(f"Removed requirement: {removed.requirement}")


def reset_to_defaults(requirements: list[ReportRequirement]) -> None:
    """Reset the list to default requirements."""

    confirmation = input("Type YES to reset all requirements to defaults: ").strip()
    if confirmation != "YES":
        print("Reset cancelled.")
        return

    requirements.clear()
    requirements.extend(build_default_requirements())
    print("Requirement list reset to defaults.")


def run_menu(requirements: list[ReportRequirement], csv_path: Path) -> None:
    """Run the interactive request-list editor."""

    while True:
        print("\nNews Report Request CSV Builder")
        print("1. Display requirements")
        print("2. Add requirement")
        print("3. Add or edit specific requirements")
        print("4. Rename requirement")
        print("5. Include or exclude requirement")
        print("6. Remove requirement")
        print("7. Reset to defaults")
        print("8. Save CSV")
        print("9. Save and exit")
        print("10. Exit without saving")

        choice = input("Choose an option (1-10): ").strip()

        if choice == "1":
            display_requirements(requirements)
        elif choice == "2":
            add_requirement(requirements)
        elif choice == "3":
            edit_specific_requirements(requirements)
        elif choice == "4":
            rename_requirement(requirements)
        elif choice == "5":
            toggle_requirement(requirements)
        elif choice == "6":
            remove_requirement(requirements)
        elif choice == "7":
            reset_to_defaults(requirements)
        elif choice == "8":
            save_requirements(requirements, csv_path)
        elif choice == "9":
            save_requirements(requirements, csv_path)
            print("Exiting request CSV builder.")
            break
        elif choice == "10":
            print("Exiting without saving.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


def main() -> None:
    """Run the news report request CSV builder."""

    args = parse_args()
    folder_name = normalize_folder_name(args.report_folder) if args.report_folder else ""
    if not folder_name:
        folder_name = prompt_report_folder()

    report_dir = project_news_reports_dir() / folder_name
    csv_path = report_dir / args.output
    report_dir.mkdir(parents=True, exist_ok=True)

    requirements = load_requirements(csv_path)

    if args.defaults_only:
        save_requirements(requirements, csv_path)
        return

    print(f"Report folder: {report_dir.resolve()}")
    print(f"CSV file: {csv_path.resolve()}")
    run_menu(requirements, csv_path)


if __name__ == "__main__":
    main()
