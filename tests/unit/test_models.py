import pytest
from src.todo_app.models import Task

def test_task_creation_valid():
    """Test that a Task can be created with valid parameters."""
    task = Task(1, "Buy groceries")
    assert task.id == 1
    assert task.description == "Buy groceries"
    assert not task.is_completed

def test_task_creation_completed():
    """Test that a completed Task can be created."""
    task = Task(2, "Read a book", True)
    assert task.id == 2
    assert task.description == "Read a book"
    assert task.is_completed

def test_task_creation_empty_description_raises_error():
    """Test that creating a Task with an empty description raises ValueError."""
    with pytest.raises(ValueError, match="Task description cannot be empty."):
        Task(3, "")
    with pytest.raises(ValueError, match="Task description cannot be empty."):
        Task(4, "   ")

def test_task_creation_non_positive_id_raises_error():
    """Test that creating a Task with non-positive ID raises ValueError."""
    with pytest.raises(ValueError, match="Task ID must be a positive integer."):
        Task(0, "Invalid ID task")
    with pytest.raises(ValueError, match="Task ID must be a positive integer."):
        Task(-1, "Invalid ID task")

def test_task_creation_non_integer_id_raises_error():
    """Test that creating a Task with non-integer ID raises ValueError."""
    with pytest.raises(ValueError, match="Task ID must be a positive integer."):
        Task("a", "Invalid ID task")
    with pytest.raises(ValueError, match="Task ID must be a positive integer."):
        Task(1.5, "Invalid ID task")

def test_task_repr():
    """Test the string representation of a Task."""
    task_incomplete = Task(1, "Walk the dog")
    assert repr(task_incomplete) == "[❌] 1: Walk the dog"

    task_complete = Task(2, "Finish report", True)
    assert repr(task_complete) == "[✅] 2: Finish report"

def test_task_to_dict():
    """Test conversion of Task object to dictionary."""
    task = Task(1, "Test dict conversion", False)
    expected_dict = {"id": 1, "description": "Test dict conversion", "is_completed": False}
    assert task.to_dict() == expected_dict

def test_task_from_dict():
    """Test creation of Task object from dictionary."""
    data = {"id": 1, "description": "Test from dict", "is_completed": True}
    task = Task.from_dict(data)
    assert task.id == 1
    assert task.description == "Test from dict"
    assert task.is_completed
