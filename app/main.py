from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tasks

app = FastAPI(title="Task Manager API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router)