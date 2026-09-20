from contextlib import asynccontextmanager
from uuid import uuid4

from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import select

from app.models.base import Base
from app.db.session import engine

from app.api.routers.task import router as task_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Код при старте
    Base.metadata.create_all(bind=engine)
    yield
    # Код при выключении

# Передаем параметр именно lifespan (через s)
app = FastAPI(lifespan=lifespan)
app.include_router(router=task_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)






