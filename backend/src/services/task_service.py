from sqlmodel import Session, select
from typing import List, Optional
from ..models.task import Task, TaskCreate, TaskUpdate, TaskToggleComplete
from ..models.user import User
from ..core.exceptions import TaskNotFoundException, InsufficientPermissionException, UserNotFoundException


class TaskService:
    """
    Service class to handle task-related business logic.
    """

    @staticmethod
    def create_task(session: Session, task_create: TaskCreate, user_id: int) -> Task:
        """
        Create a new task for the given user.
        """
        # Create a new task instance with the provided data and user_id
        db_task = Task(
            title=task_create.title,
            description=task_create.description,
            completed=task_create.completed,
            user_id=user_id
        )

        session.add(db_task)
        session.commit()
        session.refresh(db_task)

        return db_task

    @staticmethod
    def get_task_by_id(session: Session, task_id: int, user_id: int) -> Task:
        """
        Get a specific task by ID for the given user.
        """
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = session.exec(statement).first()

        if not task:
            raise TaskNotFoundException(task_id)

        return task

    @staticmethod
    def get_tasks_by_user(session: Session, user_id: int) -> List[Task]:
        """
        Get all tasks for the given user.
        """
        statement = select(Task).where(Task.user_id == user_id)
        tasks = session.exec(statement).all()

        return tasks

    @staticmethod
    def update_task(session: Session, task_id: int, task_update: TaskUpdate, user_id: int) -> Task:
        """
        Update a specific task for the given user.
        """
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        db_task = session.exec(statement).first()

        if not db_task:
            raise TaskNotFoundException(task_id)

        # Update only the fields that are provided
        for field, value in task_update.dict(exclude_unset=True).items():
            setattr(db_task, field, value)

        session.add(db_task)
        session.commit()
        session.refresh(db_task)

        return db_task

    @staticmethod
    def delete_task(session: Session, task_id: int, user_id: int) -> bool:
        """
        Delete a specific task for the given user.
        """
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        db_task = session.exec(statement).first()

        if not db_task:
            raise TaskNotFoundException(task_id)

        session.delete(db_task)
        session.commit()

        return True

    @staticmethod
    def toggle_task_completion(session: Session, task_id: int, user_id: int) -> Task:
        """
        Toggle the completion status of a specific task for the given user.
        """
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        db_task = session.exec(statement).first()

        if not db_task:
            raise TaskNotFoundException(task_id)

        # Toggle the completion status
        db_task.completed = not db_task.completed

        session.add(db_task)
        session.commit()
        session.refresh(db_task)

        return db_task