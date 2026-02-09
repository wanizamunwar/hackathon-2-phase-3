"""
manager.py - Manages the collection of Todo tasks.
"""

from .models import Task

class TaskManager:
    """
    Manages the creation, retrieval, updating, and deletion of tasks.
    """
    def __init__(self):
        self._tasks = {} # Stores tasks as {id: Task_object}
        self._next_id = 1

    def _generate_id(self):
        """Generates a unique ID for a new task."""
        task_id = self._next_id
        self._next_id += 1
        return task_id

    def add_task(self, description: str) -> Task:
        """Adds a new task to the manager."""
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty.")
        
        task_id = self._generate_id()
        new_task = Task(id=task_id, description=description)
        self._tasks[task_id] = new_task
        return new_task

    def get_all_tasks(self) -> list[Task]:
        """Returns a list of all tasks."""
        return list(self._tasks.values())

    def get_task_by_id(self, task_id: int) -> Task | None:
        """Returns a task by its ID."""
        return self._tasks.get(task_id)
    
    def mark_task_complete(self, task_id: int) -> Task:
        """Marks a task as complete."""
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")
        if task.is_completed:
            raise ValueError(f"Task with ID {task_id} is already complete.")
        task.is_completed = True
        return task

    def update_task_description(self, task_id: int, new_description: str) -> Task:
        """Updates the description of an existing task."""
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")
        if not new_description or not new_description.strip():
            raise ValueError("New task description cannot be empty.")
        task.description = new_description.strip()
        return task

    def delete_task(self, task_id: int) -> None:
        """Deletes a task by its ID."""
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} not found.")
        del self._tasks[task_id]
