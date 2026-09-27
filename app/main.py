from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(title="Task Manager API")


@app.get("/")
def health_check():
    return {"status": "ok"}


app.include_router(tasks.router)