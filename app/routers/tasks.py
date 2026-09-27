from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import TaskModel

router = APIRouter(prefix="/tasks", tags=["Tasks"])


class TaskSchema(BaseModel):
    id: int
    title: str
    done: bool

    model_config = ConfigDict(from_attributes=True)


class TaskCreate(BaseModel):
    title: str


@router.get("/", response_model=List[TaskSchema])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(TaskModel).all()


@router.post("/", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    db_task = TaskModel(title=payload.title, done=False)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.patch("/{task_id}/complete", response_model=TaskSchema)
def complete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.done = True
    db.commit()
    db.refresh(task)
    return task