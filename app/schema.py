from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoModel(BaseModel):
    id: int
    created: datetime = datetime.now()

    class Config:
        orm_mode = True

class CreateTodoModel(TodoModel):
    title: str
    desc: str

    class Config:
        orm_mode = True

class UpdateTodoModel(TodoModel):
    title: Optional[str]

    class Config:
        orm_mode = True