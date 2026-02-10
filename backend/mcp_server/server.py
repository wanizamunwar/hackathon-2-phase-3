import json
import os

from dotenv import load_dotenv

load_dotenv()

from mcp.server.fastmcp import FastMCP
from sqlmodel import Session, create_engine, select

from models import Task

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite://")
engine = create_engine(DATABASE_URL, echo=False)

mcp = FastMCP("Todo MCP Server")

@mcp.tool()
def add_task(user_id: str, title: str, description: str = "") -> str:
    """Create a new task for the user.

    Args:
        user_id: The authenticated user's ID
        title: The task title (required)
        description: Optional task description
    """
    with Session(engine) as session:
        task = Task(user_id=user_id, title=title, description=description or None)
        session.add(task)
        session.commit()
        session.refresh(task)
        return json.dumps({"task_id": task.id, "status": "created", "title": task.title})


@mcp.tool()
def list_tasks(user_id: str, status: str = "all") -> str:
    """Retrieve tasks for the user, optionally filtered by status.

    Args:
        user_id: The authenticated user's ID
        status: Filter by status - "all", "pending", or "completed" (default: "all")
    """
    with Session(engine) as session:
        statement = select(Task).where(Task.user_id == user_id)
        if status == "pending":
            statement = statement.where(Task.completed == False)  # noqa: E712
        elif status == "completed":
            statement = statement.where(Task.completed == True)  # noqa: E712
        tasks = session.exec(statement).all()
        return json.dumps([
            {"id": t.id, "title": t.title, "completed": t.completed}
            for t in tasks
        ])


@mcp.tool()
def complete_task(user_id: str, task_id: int) -> str:
    """Mark a task as complete.

    Args:
        user_id: The authenticated user's ID
        task_id: The ID of the task to complete
    """
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task or task.user_id != user_id:
            return json.dumps({"error": "Task not found"})
        task.completed = True
        session.add(task)
        session.commit()
        return json.dumps({"task_id": task.id, "status": "completed", "title": task.title})


@mcp.tool()
def delete_task(user_id: str, task_id: int) -> str:
    """Delete a task from the list.

    Args:
        user_id: The authenticated user's ID
        task_id: The ID of the task to delete
    """
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task or task.user_id != user_id:
            return json.dumps({"error": "Task not found"})
        title = task.title
        session.delete(task)
        session.commit()
        return json.dumps({"task_id": task_id, "status": "deleted", "title": title})


@mcp.tool()
def update_task(user_id: str, task_id: int, title: str = "", description: str = "") -> str:
    """Update a task's title or description.

    Args:
        user_id: The authenticated user's ID
        task_id: The ID of the task to update
        title: New title for the task (leave empty to keep current)
        description: New description for the task (leave empty to keep current)
    """
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task or task.user_id != user_id:
            return json.dumps({"error": "Task not found"})
        if title:
            task.title = title
        if description:
            task.description = description
        session.add(task)
        session.commit()
        session.refresh(task)
        return json.dumps({"task_id": task.id, "status": "updated", "title": task.title})


if __name__ == "__main__":
    mcp.run(transport="stdio")
