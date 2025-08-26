import pytest

from app.main import app
from app.database import Database
from app.models import TaskStatus


@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_db():
    app.db = Database()
    yield


def test_create_task(client):
    response = client.post('/tasks/', json={
        'title': 'Test Task',
        'description': 'Test Description'
    })
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'Test Task'
    assert data['status'] == TaskStatus.CREATED


def test_get_tasks(client):
    client.post('/tasks/', json={'title': 'Task 1'})
    response = client.get('/tasks/')
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_task(client):
    create_resp = client.post('/tasks/', json={
        'title': 'Test', 'description': 'Test'
    })
    assert create_resp.status_code == 200
    task_id = create_resp.json()['id']
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    assert response.json()['title'] == 'Test'


def test_update_task(client):
    create_resp = client.post('/tasks/', json={
        'title': 'Test', 'description': 'Test'
    })
    assert create_resp.status_code == 200
    task_id = create_resp.json()['id']
    current_status = create_resp.json()['status']
    upd_resp = client.put(f'/tasks/{task_id}', json={
        'title': 'Updated',
        'description': 'Updated',
        'status': current_status
    })
    assert upd_resp.status_code == 200, (
        f"Update failed with status {upd_resp.status_code}: {upd_resp.text}"
    )
    assert upd_resp.json()['title'] == 'Updated'
    assert upd_resp.json()['description'] == 'Updated'
    assert upd_resp.json()['status'] == current_status


def test_delete_task(client):
    create_resp = client.post('/tasks/', json={
        'title': 'Test', 'description': 'Test'
    })
    assert create_resp.status_code == 200
    task_id = create_resp.json()['id']
    delete_resp = client.delete(f'/tasks/{task_id}')
    assert delete_resp.status_code == 200
    assert client.get(f'/tasks/{task_id}').status_code == 404
