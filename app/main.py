from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from .database import db
from .schemas import TaskCreate, TaskResponse, TaskUpdate
from .models import Task

app = FastAPI(title='Tasks Manager Api')


@app.get('/')
async def root():
    return RedirectResponse(url="/docs")


@app.post(
        '/tasks/',
        response_model=TaskResponse,
        summary='Создать задачу'
)
def create_task(task: TaskCreate):
    new_task = Task(**task.dict())
    return db.create(new_task)


@app.get(
        '/tasks/',
        response_model=list[TaskResponse],
        summary='Получить список задач'
)
def get_tasks():
    return db.get_all()


@app.get(
        '/tasks/{task_id}',
        response_model=TaskResponse,
        summary='Получить задачу'
)
def get_task(task_id: str):
    if task := db.get(task_id):
        return task
    raise HTTPException(status_code=404, detail='Task not found')


@app.put(
        '/tasks/{task_id}',
        response_model=TaskResponse,
        summary='Обновить задачу'
)
def update_task(task_id: str, task_data: TaskUpdate):
    if task := db.update(task_id, task_data.dict(exclude_unset=True)):
        return task
    raise HTTPException(status_code=404, detail='Task not found')


@app.delete(
        '/tasks/{task_id}',
        summary='Удалить задачу'
)
def delete_task(task_id: str):
    if db.delete(task_id):
        return {'detail': 'Task deleted'}
    raise HTTPException(status_code=404, detail='Task not found')
