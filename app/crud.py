from sqlalchemy.orm import Session

from app import schema, models


def create_todo(db:Session, todo: schema.CreateTodoModel):
    new_todo = models.Todo(id=todo.id, title=todo.title, descritpion=todo.desc, created=todo.created)
    db.add(new_todo)
    try:
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    return new_todo


def update_todo(db:Session, todo: schema.UpdateTodoModel, id:int):
    obj = db.query(models.Todo).filter(models.Todo.id == id).first()
    obj.title= todo.title
    obj.descritpion = todo.desc
    try:
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    return obj


def delete(id: int, db:Session):
    obj = db.query(models.Todo).filter(models.Todo.id==id)
    db.delete(obj)
