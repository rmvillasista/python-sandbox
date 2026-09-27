from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.routers.tasks import router

test_app = FastAPI()
test_app.include_router(router)
client = TestClient(test_app)

def test_complete_task():
    client.post("/tasks/", json={"title": "Complete me"})
    response = client.patch("/tasks/1/complete")
    assert response.status_code == 200

def test_complete_nonexistent_task():
    response = client.patch("/tasks/999/complete")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"