#!/usr/bin/env python3
"""
todo_list.py

A menu-based to-do list manager with completion status.
Tasks are saved to a text file.

Usage:
    python3 todo_list.py
"""

from __future__ import annotations

from pathlib import Path

TODO_FILE: Path = Path("todo_list.txt")


def load_tasks() -> list[str]:
    """Load tasks from the to-do list file."""
    if not TODO_FILE.exists():
        return []

    with TODO_FILE.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def save_tasks(tasks: list[str]) -> None:
    """Save tasks to the to-do list file."""
    with TODO_FILE.open("w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")


def display_tasks(tasks: list[str]) -> None:
    """Display all tasks."""
    if not tasks:
        print("No tasks in the to-do list.")
        return

    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks: list[str]) -> None:
    """Add a new task with an incomplete status."""
    task: str = input("Enter a new task: ").strip()

    if not task:
        print("No task entered. Nothing added.")
        return

    formatted_task: str = f"[ ] {task}"
    tasks.append(formatted_task)
    save_tasks(tasks)

    print(f'Added task: "{task}"')


def mark_task_completed(tasks: list[str]) -> None:
    """Mark a task as completed."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_number: int = int(
            input("Enter the task number to mark complete: ").strip()
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 1 <= task_number <= len(tasks):
        print("Invalid task number.")
        return

    task: str = tasks[task_number - 1]

    if task.startswith("[x] "):
        print("That task is already completed.")
        return

    if task.startswith("[ ] "):
        tasks[task_number - 1] = task.replace("[ ] ", "[x] ", 1)
    else:
        tasks[task_number - 1] = f"[x] {task}"

    save_tasks(tasks)
    print("Task marked as completed.")


def remove_task(tasks: list[str]) -> None:
    """Remove a task by its number."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_number: int = int(
            input("Enter the number of the task to remove: ").strip()
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 1 <= task_number <= len(tasks):
        print("Invalid task number.")
        return

    removed_task: str = tasks.pop(task_number - 1)
    save_tasks(tasks)

    print(f'Removed task: "{removed_task}"')


def edit_task(tasks: list[str]) -> None:
    """Edit an existing task while preserving its completion status."""
    display_tasks(tasks)

    if not tasks:
        return

    try:
        task_number: int = int(
            input("Enter the number of the task to edit: ").strip()
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 1 <= task_number <= len(tasks):
        print("Invalid task number.")
        return

    old_task: str = tasks[task_number - 1]
    status: str = "[ ]"

    if old_task.startswith("[x] "):
        status = "[x]"
        old_description = old_task[4:]
    elif old_task.startswith("[ ] "):
        old_description = old_task[4:]
    else:
        old_description = old_task

    new_description: str = input("Enter the new task description: ").strip()

    if not new_description:
        print("No new description entered. Task not updated.")
        return

    tasks[task_number - 1] = f"{status} {new_description}"
    save_tasks(tasks)

    print(f'Updated task: "{old_description}" -> "{new_description}"')


def clear_tasks(tasks: list[str]) -> None:
    """Clear all tasks from memory and from the file."""
    if not tasks and not TODO_FILE.exists():
        print("No tasks to clear.")
        return

    confirmation: str = input("Type YES to clear all tasks: ").strip()

    if confirmation != "YES":
        print("Clear operation cancelled.")
        return

    tasks.clear()

    if TODO_FILE.exists():
        TODO_FILE.unlink()

    print("All tasks cleared.")


def main() -> None:
    """Run the to-do list manager."""
    tasks: list[str] = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Completed")
        print("4. Remove Task")
        print("5. Edit Task")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice: str = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            clear_tasks(tasks)
        elif choice == "7":
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 7.")


if __name__ == "__main__":
    main()