"""
cli.py - Command Line Interface (CLI) related functions for the Todo application.
"""

from .models import Task

def display_tasks(tasks: list[Task]):
    """Displays a list of tasks in a formatted table."""
    if not tasks:
        print("Your todo list is empty!")
        return

    print("\n--- Your Todo List ---")
    print("ID | Status | Description")
    print("---|--------|------------")
    for task in tasks:
        status_char = "Done" if task.is_completed else "X"
        print(f"{task.id:<2} | {status_char:<6} | {task.description}")
    print("----------------------\n")

def get_user_input(prompt: str) -> str:
    """Gets string input from the user."""
    return input(prompt).strip()

def get_task_id_input(prompt: str) -> int:
    """Gets and validates an integer task ID from the user."""
    while True:
        try:
            task_id_str = input(prompt).strip()
            task_id = int(task_id_str)
            if task_id <= 0:
                print("Error: Task ID must be a positive integer.")
            else:
                return task_id
        except ValueError:
            print("Error: Invalid input. Please enter a number for the task ID.")
