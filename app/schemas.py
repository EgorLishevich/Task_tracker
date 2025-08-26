from pydantic import BaseModel

from .models import Task, TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskResponse(Task):
    pass


class TaskUpdate(BaseModel):
    title: str
    description: str
    status: TaskStatus
