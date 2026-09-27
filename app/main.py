# app/main.py
from fastapi import FastAPI
from app.routers import tasks

app = FastAPI()

# Root health check endpoint required by test_read_main_health
@app.get("/")
def health_check():
    return {"status": "ok"}

# Mount tasks router without duplicating prefix="/tasks"
app.include_router(tasks.router)