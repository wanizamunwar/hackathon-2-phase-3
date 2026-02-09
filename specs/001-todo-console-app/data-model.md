# Data Model: In-Memory Python Console Todo App

## Entity: Task

Represents a single todo item within the application. Tasks are stored in memory only and are identified by a unique integer ID.

### Attributes

*   **`id`**:
    *   **Type**: Integer
    *   **Description**: A unique identifier for the task. Automatically assigned sequentially when a task is added.
    *   **Constraints**: Must be unique, positive integer.
*   **`description`**:
    *   **Type**: String
    *   **Description**: The textual content or description of the todo item.
    *   **Constraints**: Cannot be empty.
*   **`is_completed`**:
    *   **Type**: Boolean
    *   **Description**: Indicates whether the task has been marked as complete.
    *   **Default**: `False` (tasks are incomplete when created).

### Relationships
No explicit relationships with other entities in this phase.

### Validation Rules
*   `description` must not be an empty string.
*   `id` must correspond to an existing task for update, deletion, or marking as complete operations.
*   Input for `id` must be a valid integer.

### Example (Conceptual)
```python
class Task:
    def __init__(self, id, description, is_completed=False):
        self.id = id
        self.description = description
        self.is_completed = is_completed

    def __repr__(self):
        status = "✅" if self.is_completed else "❌"
        return f"[{status}] {self.id}: {self.description}"
```