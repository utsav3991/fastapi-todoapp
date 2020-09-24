from pydantic import BaseModel


class TodoModel(BaseModel):
    id: int
    title: str
    desc: str

    class Config:
        orm_mode = True
