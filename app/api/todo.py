from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import dependencies, crud
from app.schema import TodoModel as tm

router = APIRouter()


@router.post("/todo/add", response_model=List[tm])
def post_todo(todo: tm, db: Session = Depends(dependencies.get_db)):
    created_todo = crud.create_todo(db, todo)
    return todo
