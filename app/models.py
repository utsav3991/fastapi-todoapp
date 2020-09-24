from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from .database import Base

class Todo(Base):
    __table__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    descritpion = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime, default=datetime.now())
    updated = Column(DateTime)
