from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(title="Task Management API", version="1.0.0")

app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"status": "ok", "message": "FastAPI PostgreSQL Docker service is healthy."}