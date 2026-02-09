import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from main import app
from models import Task  # noqa: F401 — needed for table registration

MOCK_USER = {"user_id": "test-user-123", "email": "test@example.com"}


def mock_get_current_user():
    return MOCK_USER


@pytest.fixture
def client():
    from auth import get_current_user
    from db import get_session

    engine = create_engine(
        "sqlite://",
        echo=False,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)

    def get_test_session():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_current_user] = mock_get_current_user
    app.dependency_overrides[get_session] = get_test_session

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()


USER_ID = "test-user-123"
OTHER_USER_ID = "other-user-456"


class TestHealthCheck:
    def test_health(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}


class TestCreateTask:
    def test_create_task_success(self, client):
        response = client.post(
            f"/api/{USER_ID}/tasks",
            json={"title": "Test task", "description": "A test task"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test task"
        assert data["description"] == "A test task"
        assert data["completed"] is False
        assert data["priority"] == "medium"
        assert data["tags"] == []
        assert data["user_id"] == USER_ID

    def test_create_task_with_priority_and_tags(self, client):
        response = client.post(
            f"/api/{USER_ID}/tasks",
            json={
                "title": "Priority task",
                "priority": "high",
                "tags": ["work", "urgent"],
            },
        )
        assert response.status_code == 201
        data = response.json()
        assert data["priority"] == "high"
        assert data["tags"] == ["work", "urgent"]

    def test_create_task_empty_title(self, client):
        response = client.post(
            f"/api/{USER_ID}/tasks",
            json={"title": "   "},
        )
        assert response.status_code == 400

    def test_create_task_invalid_priority(self, client):
        response = client.post(
            f"/api/{USER_ID}/tasks",
            json={"title": "Test", "priority": "critical"},
        )
        assert response.status_code == 400

    def test_create_task_wrong_user(self, client):
        response = client.post(
            f"/api/{OTHER_USER_ID}/tasks",
            json={"title": "Test"},
        )
        assert response.status_code == 403


class TestGetTasks:
    def test_get_tasks_empty(self, client):
        response = client.get(f"/api/{USER_ID}/tasks")
        assert response.status_code == 200
        assert response.json() == []

    def test_get_tasks_after_create(self, client):
        client.post(f"/api/{USER_ID}/tasks", json={"title": "Task 1"})
        client.post(f"/api/{USER_ID}/tasks", json={"title": "Task 2"})

        response = client.get(f"/api/{USER_ID}/tasks")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2

    def test_get_tasks_wrong_user(self, client):
        response = client.get(f"/api/{OTHER_USER_ID}/tasks")
        assert response.status_code == 403


class TestGetSingleTask:
    def test_get_task_success(self, client):
        create = client.post(f"/api/{USER_ID}/tasks", json={"title": "Single"})
        task_id = create.json()["id"]

        response = client.get(f"/api/{USER_ID}/tasks/{task_id}")
        assert response.status_code == 200
        assert response.json()["title"] == "Single"

    def test_get_task_not_found(self, client):
        response = client.get(f"/api/{USER_ID}/tasks/9999")
        assert response.status_code == 404


class TestUpdateTask:
    def test_update_task_success(self, client):
        create = client.post(f"/api/{USER_ID}/tasks", json={"title": "Original"})
        task_id = create.json()["id"]

        response = client.put(
            f"/api/{USER_ID}/tasks/{task_id}",
            json={"title": "Updated"},
        )
        assert response.status_code == 200
        assert response.json()["title"] == "Updated"

    def test_update_task_empty_title(self, client):
        create = client.post(f"/api/{USER_ID}/tasks", json={"title": "Original"})
        task_id = create.json()["id"]

        response = client.put(
            f"/api/{USER_ID}/tasks/{task_id}",
            json={"title": "   "},
        )
        assert response.status_code == 400

    def test_update_task_not_found(self, client):
        response = client.put(
            f"/api/{USER_ID}/tasks/9999",
            json={"title": "Updated"},
        )
        assert response.status_code == 404


class TestDeleteTask:
    def test_delete_task_success(self, client):
        create = client.post(f"/api/{USER_ID}/tasks", json={"title": "Delete me"})
        task_id = create.json()["id"]

        response = client.delete(f"/api/{USER_ID}/tasks/{task_id}")
        assert response.status_code == 204

        get_response = client.get(f"/api/{USER_ID}/tasks/{task_id}")
        assert get_response.status_code == 404

    def test_delete_task_not_found(self, client):
        response = client.delete(f"/api/{USER_ID}/tasks/9999")
        assert response.status_code == 404


class TestToggleComplete:
    def test_toggle_complete(self, client):
        create = client.post(f"/api/{USER_ID}/tasks", json={"title": "Toggle me"})
        task_id = create.json()["id"]
        assert create.json()["completed"] is False

        response = client.patch(f"/api/{USER_ID}/tasks/{task_id}/complete")
        assert response.status_code == 200
        assert response.json()["completed"] is True

        response = client.patch(f"/api/{USER_ID}/tasks/{task_id}/complete")
        assert response.status_code == 200
        assert response.json()["completed"] is False


class TestSearchAndFilter:
    def test_search_by_keyword(self, client):
        client.post(f"/api/{USER_ID}/tasks", json={"title": "Buy groceries"})
        client.post(f"/api/{USER_ID}/tasks", json={"title": "Read a book"})

        response = client.get(f"/api/{USER_ID}/tasks?search=groceries")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["title"] == "Buy groceries"

    def test_filter_by_status(self, client):
        create = client.post(f"/api/{USER_ID}/tasks", json={"title": "Task A"})
        task_id = create.json()["id"]
        client.patch(f"/api/{USER_ID}/tasks/{task_id}/complete")
        client.post(f"/api/{USER_ID}/tasks", json={"title": "Task B"})

        completed = client.get(f"/api/{USER_ID}/tasks?status=completed")
        assert len(completed.json()) == 1

        pending = client.get(f"/api/{USER_ID}/tasks?status=pending")
        assert len(pending.json()) == 1

    def test_filter_by_priority(self, client):
        client.post(f"/api/{USER_ID}/tasks", json={"title": "High", "priority": "high"})
        client.post(f"/api/{USER_ID}/tasks", json={"title": "Low", "priority": "low"})

        response = client.get(f"/api/{USER_ID}/tasks?priority=high")
        assert len(response.json()) == 1
        assert response.json()[0]["title"] == "High"

    def test_sort_by_title(self, client):
        client.post(f"/api/{USER_ID}/tasks", json={"title": "Banana"})
        client.post(f"/api/{USER_ID}/tasks", json={"title": "Apple"})

        response = client.get(f"/api/{USER_ID}/tasks?sort_by=title&sort_order=asc")
        data = response.json()
        assert data[0]["title"] == "Apple"
        assert data[1]["title"] == "Banana"
