from fastapi import Depends, APIRouter, HTTPException, Path
from db import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from models import Todo
from pydantic import BaseModel, Field


router = APIRouter()


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=50)
    priority: int = Field(gt=0)
    complete: bool = Field(default=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/")
async def read_all(db: db_dependency):
    return db.query(Todo).all()


@router.get("/api/v1/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    print(todo_model)
    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code=404, detail="todo with this id not found")


@router.post("/api/todo/", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_body: TodoRequest):
    todo_dict = Todo(**todo_body.model_dump())
    db.add(todo_dict)
    db.commit()


@router.put("/api/todo/{todo_id}")
async def update_todo(
    db: db_dependency, todo_request: TodoRequest, todo_modify_id: int
):
    todo_model = db.query(Todo).filter(Todo.id == todo_modify_id).first()

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@router.delete("/api/todo/{delete_id}")
async def delete_todo(db: db_dependency, todo_delete_id: int):
    db.query(Todo).filter(Todo.id == todo_delete_id).delete()
    db.commit()
