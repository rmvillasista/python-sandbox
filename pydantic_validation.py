from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

class ItemCreate(BaseModel):
    title: str = Field(..., min_length=3)
    priority: int = Field(default=1, ge=1, le=5)

class ItemResponse(ItemCreate):
    id: int
    completed: bool = False

items_db = {}

@app.post("/items/create", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    item_id = len(items_db) + 1
    new_item = ItemResponse(id=item_id, **item.model_dump())
    items_db[item_id] = new_item
    return new_item

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]