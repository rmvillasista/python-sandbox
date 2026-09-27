from typing import Optional
from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    done: bool = False
    priority: Optional[str] = "medium"


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None
    priority: Optional[str] = None


class TaskResponse(TaskBase):
    id: int

    model_config = ConfigDict(from_attributes=True)