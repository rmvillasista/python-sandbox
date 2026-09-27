from fastapi import FastAPI
from app.database import Base, engine
from app.routers import tasks

# Create tables on application startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")


@app.get("/")
def health_check():
    return {"status": "ok"}


app.include_router(tasks.router)