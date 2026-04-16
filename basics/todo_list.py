#!/usr/bin/env python3
"""
todo_list.py

A simple command-line to-do list manager.
Saves tasks to a text file.

Usage:
    python3 todo_list.py
"""

from pathlib import Path

TODO_FILE: Path = Path("todo_list.txt")


def load_tasks() -> list[str]:
    """Load tasks from the file."""
    if not TODO_FILE.exists():
        return []

    with TODO_FILE.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def save_tasks(tasks: list[str]) -> None:
    """Save tasks to the file."""
    with TODO_FILE.open("w", encoding="utf-8") as file:
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


def add_task(tasks: list[str]) -> None:
    """Add a new task."""
    task: str = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Task cannot be empty.")


def remove_task(tasks: list[str]) -> None:
    """Remove a task by its number."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_number: int = int(input("Enter the task number to remove: ").strip())
        if 1 <= task_number <= len(tasks):
            removed_task: str = tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def edit_task(tasks: list[str]) -> None:
    """Edit a task by its number."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_number: int = int(input("Enter the task number to edit: ").strip())
        if 1 <= task_number <= len(tasks):
            new_task: str = input("Enter the new task description: ").strip()
            if new_task:
                tasks[task_number - 1] = new_task
                print("Task updated.")
            else:
                print("Task description cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def erase_all_tasks(tasks: list[str]) -> None:
    """Erase all tasks from memory and delete the file."""
    print("Warning: This will permanently delete all tasks.")

    confirmation: str = input("Type 'YES' to confirm: ").strip()
    if confirmation != "YES":
        print("Operation cancelled.")
        return

    tasks.clear()

    if TODO_FILE.exists():
        TODO_FILE.unlink()

    print("All tasks have been erased.")


def main() -> None:
    """Run the main program loop."""
    tasks: list[str] = load_tasks()

    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Edit task")
        print("5. Save and exit")
        print("6. Erase all tasks")

        choice: str = input("Choose an option: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        elif choice == "6":
            erase_all_tasks(tasks)
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()