from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import dependencies, crud
from app.schema import CreateTodoModel, UpdateTodoModel, TodoModel

router = APIRouter()


@router.post("/todo/add", response_model=List[CreateTodoModel])
def post_todo(todo: CreateTodoModel, db: Session = Depends(dependencies.get_db)):
    crud.create_todo(db, todo)
    return todo


@router.put("/todo/update/{id}", response_model=List[UpdateTodoModel])
def update_todo(id: int, todo: UpdateTodoModel, db: Session = Depends(dependencies.get_db)):
    crud.update_todo(db, todo, id)
    return todo


@router.delete("/todo/delete/{id}")
def delete_todo(id:int, db: Session = Depends(dependencies.get_db)):
    crud.delete(id, db)
    return
