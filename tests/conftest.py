import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Database


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_db():
    original_db = app.db
    app.db = Database()
    yield
    app.db = original_db


@pytest.fixture
def sample_task_data():
    return {
        'title': 'Test Task',
        'description': 'Test Description'
    }


@pytest.fixture
def created_task(client, sample_task_data):
    response = client.post('/tasks/', json=sample_task_data)
    return response.json()
