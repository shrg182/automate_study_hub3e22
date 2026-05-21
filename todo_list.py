#!/usr/bin/env python3
"""
todo_list.py

A menu-based to-do list manager with completion status.
The to-do list file can be saved in a target directory.

Usage:
    python3 todo_list.py
    python3 todo_list.py --todo-dir work_tasks
    python3 todo_list.py --todo-dir personal_tasks
    python3 todo_list.py --todo-dir tools/placeholders
    python3 todo_list.py --todo-dir tools/utility_files
"""

from __future__ import annotations

import argparse
from pathlib import Path

from basics.todo_list import TODO_FILE

TODO_FILENAME: str = "todo_list.txt"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="A simple command-line to-do list manager.")

    parser.add_argument(
        "--todo-dir",
        type=Path,
        default=Path.cwd(),
        help="Directory to save the to-do list file (default: current directory)",
    )

    return parser.parse_args()


def get_tod_file(todo_dir: Path) -> Path:
    """Return the full path to the to-do list file."""
    todo_dir.mkdir(parents=True, exist_ok=True)
    return todo_dir / TODO_FILENAME


def load_tasks(todo_file: Path) -> list[str]:
    """Load tasks from the to-do list file."""
    if not todo_file.exists():
        return []

    with todo_file.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def save_tasks(tasks: list[str], todo_file: Path) -> None:
    """Save tasks to the to-do list file."""
    with todo_file.open("w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def display_tasks(tasks: list[str]) -> None:
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks: list[str], todo_file: Path) -> None:
    """Add a new task with an incomplete status."""
    task: str = input("Enter a new task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(f"[ ] {task}")
    save_tasks(tasks, todo_file)
    print(f"Added task: {task}")


def mark_task_completed(tasks: list[str], todo_file: Path) -> None:
    """Mark a task as completed."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_number: int = int(
            input("Enter the task number to mark as completed: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return

    if not 1 <= task_number <= len(tasks):
        print("Invalid task number.")
        return

    task = tasks[task_number - 1]

    if task.startswith("[x] "):
        print("Task is already marked as completed.")
        return

    if task.startswith("[ ] "):
        tasks[task_number - 1] = task.replace("[ ] ", "[x] ", 1)
    else:
        tasks[task_number - 1] = f"[x] {task}"

    save_tasks(tasks, todo_file)
    print(f"Marked task as completed: {task[4:]}")


def remove_task(tasks: list[str], todo_file: Path) -> None:
    """Remove a task by its number."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_number: int = int(
            input("Enter the task number to remove: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return

    if not 1 <= task_number <= len(tasks):
        print("Invalid task number.")
        return

    removed_task: str = tasks.pop(task_number - 1)
    save_tasks(tasks, todo_file)
    print(f"Removed task: {removed_task[4:]}")


def edit_task(tasks: list[str], todo_file: Path) -> None:
    """Edit an existing task while preserving its completion status."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_number: int = int(
            input("Enter the task number to edit: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return

    if not 1 <= task_number <= len(tasks):
        print("Invalid task number.")
        return

    old_task: str = tasks[task_number - 1]

    if old_task.startswith("[x] "):
        status: str = "[x] "
        task_description: str = old_task[4:]
    elif old_task.startswith("[ ]"):
        status: str = "[ ] "
        task_description: str = old_task[4:]
    else:
        status = "[ ]"
        old_description = old_task

    new_description: str = input("Enter the new task description: ").strip()

    if not new_description:
        print("Task description cannot be empty.")
        return

    tasks[task_number - 1] = f"{status}{new_description}"
    save_tasks(tasks, todo_file)

    print(f"Updated task: {new_description}")


def clear_tasks(tasks: list[str], todo_file: Path) -> None:
    """Clear all tasks from the to-do list."""
    if not tasks and not todo_file.exists():
        print("No tasks to clear.")
        return

    confirmation = input(
        "Are you sure you want to clear all tasks? This action cannot be undone. (yes/no): ").strip().lower()

    if confirmation != "yes":
        print("Clear operation cancelled.")
        return

    tasks.clear()

    if todo_file.exists():
        todo_file.unlink()

    print("All tasks have been cleared.")


def main() -> None:
    """Main function to run the to-do list manager."""
    args = parse_args()
    todo_file = get_tod_file(args.todo_dir)
    tasks = load_tasks(todo_file)

    while True:
        print("\nMenu:")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Edit a task")
        print("6. Clear all tasks")
        print("7. Exit")

        choice: str = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks, todo_file)
        elif choice == "3":
            mark_task_completed(tasks, todo_file)
        elif choice == "4":
            remove_task(tasks, todo_file)
        elif choice == "5":
            edit_task(tasks, todo_file)
        elif choice == "6":
            clear_tasks(tasks, todo_file)
        elif choice == "7":
            print("Exiting the to-do list manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
