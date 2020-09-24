from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from .database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, index=True)
    descritpion = Column(String, primary_key=True, index=True)
    created = Column(DateTime, default=datetime.now().date())
