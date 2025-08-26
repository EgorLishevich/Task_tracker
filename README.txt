# Task Manager API

FastAPI-приложение для управления задачами с полным CRUD функционалом.

## Запуск

### Локально
1. Установите зависимости: `pip install -r requirements.txt`
2. Запустите сервер: `uvicorn app.main:app --reload`

### В Docker
1. Соберите образ: `docker build -t task-manager .`
2. Запустите контейнер: `docker run -p 8000:8000 task-manager`

## API Endpoints

- `POST /tasks/` - Создать задачу
- `GET /tasks/` - Получить все задачи
- `GET /tasks/{id}` - Получить задачу по ID
- `PUT /tasks/{id}` - Обновить задачу
- `DELETE /tasks/{id}` - Удалить задачу

## Тестирование
Запустите тесты: `pytest --cov=app tests/`