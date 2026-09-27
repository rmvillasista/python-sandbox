import json
from pathlib import Path
from typing import List
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/tasks", tags=["Tasks"])
DATA_FILE = Path("web_tasks.json")

class TaskSchema(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: str

def read_db() -> List[dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_db(data: List[dict]):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@router.get("/", response_model=List[TaskSchema])
def list_tasks():
    return read_db()

@router.post("/", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    db = read_db()
    new_id = max([t["id"] for t in db], default=0) + 1
    new_task = {"id": new_id, "title": payload.title, "done": False}
    db.append(new_task)
    write_db(db)
    return new_task