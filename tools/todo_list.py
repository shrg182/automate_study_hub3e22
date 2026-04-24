#!/usr/bin/env python3
"""
todo_list.py

A simple command-line to-do list manager.
Save and load tasks from a text file.

Usage:
    python3 todo_list.py add "Buy groceries"
    python3 todo_list.py list
    python3 todo_list.py remove 1
"""

from __future__ import annotations

import argparse
from pathlib import Path

TODO_FILE = Path("todo_list.txt")


def load_tasks() -> list[str]:
    """Load tasks from the to-do list file."""
    if not TODO_FILE.exists():
        return []
    with TODO_FILE.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
    

def save_tasks(tasks: list[str]) -> None:
    """Save tasks to the to-do list file."""
    with TODO_FILE.open("w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task(tasks: list[str]) -> None:
    """Add a new task to the to-do list."""
    task: str = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f'Added task: "{task}"')
    else:
        print("No task entered. Nothing added.")


def list_tasks() -> None:
    """List all tasks in the to-do list."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks in the to-do list.")
        return
    print("To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")


def remove_task(task_number: int) -> None:
    """Remove a task by its number from the to-do list."""
    tasks = load_tasks()
   
    try:
        task_number: int = int(input("Enter the number of the task to remove: ").strip())
        if 1 <= task_number <= len(tasks):
            removed_task: str = tasks.pop(task_number - 1)
            print(f'Removed task: "{removed_task}"')
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def edit_task(tasks: list[str]) -> None:
    """Edit an existing task in the to-do list."""
    list_tasks()
    try:
        task_number: int = int(input("Enter the number of the task to edit: ").strip())
        if 1 <= task_number <= len(tasks):
            new_task: str = input("Enter the new task description: ").strip()
            if new_task:
                old_task: str = tasks[task_number - 1]
                tasks[task_number - 1] = new_task
                save_tasks(tasks)
                print(f'Updated task {task_number}: "{old_task}" -> "{new_task}"')
            else:
                print("No new description entered. Task not updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def clear_tasks() -> None:
    """Clear all tasks from the to-do list."""
    if TODO_FILE.exists():
        TODO_FILE.unlink()
        print("All tasks cleared.")
    else:
        print("No tasks to clear.")

def main() -> None:
    """Run the to-do list manager."""
    tasks: list[str] = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Edit Task")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice: str = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            remove_task(task_number)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            clear_tasks()
            tasks.clear()
        elif choice == "6":
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()