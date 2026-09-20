from fastapi import Depends

from app.db import session
from app.services.task import TaskService


def get_task_service(db: session = Depends(session.get_db)):
    """Функция для инъекции зависимости TaskService"""
    return TaskService(db)