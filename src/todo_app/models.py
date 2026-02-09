"""
models.py - Defines the Task entity for the Todo application.
"""

class Task:
    """
    Represents a single todo item.
    """
    def __init__(self, id: int, description: str, is_completed: bool = False):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Task ID must be a positive integer.")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Task description cannot be empty.")
        if not isinstance(is_completed, bool):
            raise ValueError("is_completed must be a boolean.")

        self.id = id
        self.description = description.strip()
        self.is_completed = is_completed

    def __repr__(self):
        status = "✅" if self.is_completed else "❌"
        return f"[{status}] {self.id}: {self.description}"

    def to_dict(self):
        """Converts the Task object to a dictionary."""
        return {
            "id": self.id,
            "description": self.description,
            "is_completed": self.is_completed
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates a Task object from a dictionary."""
        return cls(data["id"], data["description"], data["is_completed"])
