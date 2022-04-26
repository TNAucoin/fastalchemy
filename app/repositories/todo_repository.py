from typing import Iterator
from uuid import uuid4

from app.models.todo_model import Todo
from app.models.user_model import User
from app.repositories.exceptions import UserNotFoundError


class TodoRepository:

    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    def get_all_todos(self) -> Iterator[Todo]:
        with self.session_factory() as session:
            return session.query(Todo).all()

    def get_todo_by_id(self, public_id: str):
        with self.session_factory() as session:
            todo = session.query(Todo).filter_by(public_id=public_id).first()
            return todo

    def create_todo(self, name: str, user_email: str):
        with self.session_factory() as session:
            user = session.query(User).filter_by(email=user_email).first()
            if not user:
                raise UserNotFoundError(user_email)
            
            todo = Todo(name=name, user_id=user.id, is_completed=False, public_id=str(uuid4()))
            session.add(todo)
            session.commit()
            session.refresh(todo)
            return todo
