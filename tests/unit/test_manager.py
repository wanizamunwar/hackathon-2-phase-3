import pytest
from src.todo_app.manager import TaskManager
from src.todo_app.models import Task

@pytest.fixture
def task_manager():
    """Provides a fresh TaskManager instance for each test."""
    return TaskManager()

def test_add_task_valid_description(task_manager):
    """Test adding a task with a valid description."""
    task = task_manager.add_task("Buy groceries")
    assert isinstance(task, Task)
    assert task.id == 1
    assert task.description == "Buy groceries"
    assert not task.is_completed
    assert task_manager.get_task_by_id(1) == task
    assert task_manager.get_all_tasks() == [task]

def test_add_task_auto_increments_id(task_manager):
    """Test that task IDs are auto-incremented."""
    task1 = task_manager.add_task("Task one")
    task2 = task_manager.add_task("Task two")
    assert task1.id == 1
    assert task2.id == 2
    assert task_manager.get_all_tasks() == [task1, task2]

def test_add_task_empty_description_raises_error(task_manager):
    """Test that adding a task with an empty description raises ValueError."""
    with pytest.raises(ValueError, match="Task description cannot be empty."):
        task_manager.add_task("")
    with pytest.raises(ValueError, match="Task description cannot be empty."):
        task_manager.add_task("   ")

def test_get_all_tasks_empty(task_manager):
    """Test retrieving all tasks when no tasks have been added."""
    assert task_manager.get_all_tasks() == []

def test_get_all_tasks_multiple(task_manager):
    """Test retrieving all tasks when multiple tasks exist."""
    task1 = task_manager.add_task("Task A")
    task2 = task_manager.add_task("Task B")
    assert task_manager.get_all_tasks() == [task1, task2]

def test_get_task_by_id_exists(task_manager):
    """Test retrieving an existing task by ID."""
    task = task_manager.add_task("Find me")
    assert task_manager.get_task_by_id(task.id) == task

def test_get_task_by_id_not_exists(task_manager):
    """Test retrieving a non-existent task by ID."""
    task_manager.add_task("Existing task")
    assert task_manager.get_task_by_id(999) is None

def test_mark_task_complete_existing(task_manager):
    """Test marking an existing task as complete."""
    task = task_manager.add_task("To complete")
    completed_task = task_manager.mark_task_complete(task.id)
    assert completed_task.is_completed
    assert task_manager.get_task_by_id(task.id).is_completed

def test_mark_task_complete_non_existent_raises_error(task_manager):
    """Test marking a non-existent task as complete raises ValueError."""
    with pytest.raises(ValueError, match="Task with ID 999 not found."):
        task_manager.mark_task_complete(999)

def test_mark_task_complete_already_complete_raises_error(task_manager):
    """Test marking an already complete task as complete raises ValueError."""
    task = task_manager.add_task("Already done")
    task_manager.mark_task_complete(task.id)
    with pytest.raises(ValueError, match=f"Task with ID {task.id} is already complete."):
        task_manager.mark_task_complete(task.id)

def test_update_task_description_existing(task_manager):
    """Test updating the description of an existing task."""
    task = task_manager.add_task("Old description")
    updated_task = task_manager.update_task_description(task.id, "New description")
    assert updated_task.description == "New description"
    assert task_manager.get_task_by_id(task.id).description == "New description"

def test_update_task_description_non_existent_raises_error(task_manager):
    """Test updating a non-existent task raises ValueError."""
    with pytest.raises(ValueError, match="Task with ID 999 not found."):
        task_manager.update_task_description(999, "Some new text")

def test_update_task_description_empty_description_raises_error(task_manager):
    """Test updating a task with an empty new description raises ValueError."""
    task = task_manager.add_task("Existing")
    with pytest.raises(ValueError, match="New task description cannot be empty."):
        task_manager.update_task_description(task.id, "")
    with pytest.raises(ValueError, match="New task description cannot be empty."):
        task_manager.update_task_description(task.id, "   ")

def test_delete_task_existing(task_manager):
    """Test deleting an existing task."""
    task = task_manager.add_task("To delete")
    task_manager.delete_task(task.id)
    assert task_manager.get_task_by_id(task.id) is None
    assert task_manager.get_all_tasks() == []

def test_delete_task_non_existent_raises_error(task_manager):
    """Test deleting a non-existent task raises ValueError."""
    task_manager.add_task("Existing task")
    with pytest.raises(ValueError, match="Task with ID 999 not found."):
        task_manager.delete_task(999)
