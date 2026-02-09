from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select

from auth import get_current_user, verify_user_access
from db import get_session
from models import Task, TaskCreate, TaskRead, TaskUpdate

router = APIRouter(prefix="/api", tags=["tasks"])


@router.post(
    "/{user_id}/tasks",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    user_id: str,
    task_data: TaskCreate,
    session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user),
):
    verify_user_access(user_id, current_user)

    title = task_data.title.strip()
    if not title:
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    if task_data.priority not in ("high", "medium", "low"):
        raise HTTPException(status_code=400, detail="Priority must be high, medium, or low")

    task = Task(
        user_id=user_id,
        title=title,
        description=task_data.description,
        completed=task_data.completed,
        priority=task_data.priority,
        tags=task_data.tags,
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.get("/{user_id}/tasks", response_model=list[TaskRead])
async def get_tasks(
    user_id: str,
    session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user),
    search: str | None = Query(None),
    task_status: str | None = Query(None, alias="status"),
    priority: str | None = Query(None),
    tag: str | None = Query(None),
    sort_by: str = Query("created_at"),
    sort_order: str = Query("desc"),
):
    verify_user_access(user_id, current_user)

    statement = select(Task).where(Task.user_id == user_id)

    if search:
        statement = statement.where(
            Task.title.contains(search) | Task.description.contains(search)  # type: ignore
        )

    if task_status == "completed":
        statement = statement.where(Task.completed == True)  # noqa: E712
    elif task_status == "pending":
        statement = statement.where(Task.completed == False)  # noqa: E712

    if priority and priority in ("high", "medium", "low"):
        statement = statement.where(Task.priority == priority)

    # Sort
    sort_column = {
        "created_at": Task.created_at,
        "priority": Task.priority,
        "title": Task.title,
    }.get(sort_by, Task.created_at)

    if sort_order == "asc":
        statement = statement.order_by(sort_column.asc())  # type: ignore
    else:
        statement = statement.order_by(sort_column.desc())  # type: ignore

    tasks = session.exec(statement).all()

    # Filter by tag in Python (JSON array column)
    if tag:
        tasks = [t for t in tasks if tag in t.tags]

    return tasks


@router.get("/{user_id}/tasks/{task_id}", response_model=TaskRead)
async def get_task(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user),
):
    verify_user_access(user_id, current_user)

    task = session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/{user_id}/tasks/{task_id}", response_model=TaskRead)
async def update_task(
    user_id: str,
    task_id: int,
    task_data: TaskUpdate,
    session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user),
):
    verify_user_access(user_id, current_user)

    task = session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = task_data.model_dump(exclude_unset=True)

    if "title" in update_data:
        title = update_data["title"].strip()
        if not title:
            raise HTTPException(status_code=400, detail="Title cannot be empty")
        update_data["title"] = title

    if "priority" in update_data and update_data["priority"] not in ("high", "medium", "low"):
        raise HTTPException(status_code=400, detail="Priority must be high, medium, or low")

    for key, value in update_data.items():
        setattr(task, key, value)

    task.updated_at = datetime.now(timezone.utc)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.delete("/{user_id}/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user),
):
    verify_user_access(user_id, current_user)

    task = session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(task)
    session.commit()


@router.patch("/{user_id}/tasks/{task_id}/complete", response_model=TaskRead)
async def toggle_complete(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session),
    current_user: dict = Depends(get_current_user),
):
    verify_user_access(user_id, current_user)

    task = session.get(Task, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")

    task.completed = not task.completed
    task.updated_at = datetime.now(timezone.utc)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
