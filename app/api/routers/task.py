from fastapi import APIRouter

from app.api.routers.dependencies import get_task_service
from app.schemas.task import CreateTask, TaskSchema, TaskUpdate
from app.services.task import TaskNotFound, TaskService



router = APIRouter(prefix="/tasks")


from contextlib import asynccontextmanager
from uuid import uuid4

from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session


@router.get("")
def get_tasks(task_service: TaskService = Depends(get_task_service)) -> list[TaskSchema]:
    return task_service.list_tasks()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_task(payload: CreateTask, task_service: TaskService = Depends(get_task_service)) -> TaskSchema:
    return task_service.create_task(task_create=payload)

@router.patch("/{task_id}")
def update_task(
    task_id: str,
    payload: TaskUpdate,
    task_service: TaskService = Depends(get_task_service)
) -> TaskSchema:
    try:
        return task_service.update_task(task_id=task_id, task_update=payload)
    except TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, task_service: TaskService = Depends(get_task_service)):
    try:
        return task_service.delete_task(task_id=task_id)
    except TaskNotFound:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
