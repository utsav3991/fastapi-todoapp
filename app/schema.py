from datetime import datetime

from pydantic import BaseModel


class TodoModel(BaseModel):
    id: int
    title: str
    desc: str
    created: datetime = datetime.now()

    class Config:
        orm_mode = True
