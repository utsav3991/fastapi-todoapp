from sqlalchemy.orm import Session

from app import schema, models


def create_todo(db:Session, todo: schema.TodoModel):
    new_todo = models.Todo(id=todo.id, title=todo.title, descritpion=todo.desc, created=todo.created)
    db.add(new_todo)
    try:
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
    # db.refresh(new_todo)
    return new_todo