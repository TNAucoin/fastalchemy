from typing import Iterator

from app.models.todo_model import Todo
from app.models.user_model import User
from app.repositories.exceptions import UserNotFoundError


class UserRepository:

    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[User]:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, public_id: str) -> User:
        with self.session_factory() as session:
            user = session.query(User).filter(User.public_id == public_id).first()
            if not user:
                raise UserNotFoundError(public_id)
            return user

    def add(self, email: str, name: str, public_id: str, is_admin: bool = False) -> User:
        with self.session_factory() as session:
            user = User(email=email, name=name, public_id=public_id, is_admin=is_admin)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_by_id(self, user_id: int) -> None:
        with self.session_factory() as session:
            user: User = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(user_id)
            session.delete(user)
            session.commit()

    def get_user_todos(self, public_id: str) -> Iterator[Todo]:
        with self.session_factory() as session:
            user: User = session.query(User).filter(User.public_id == public_id).first()
            if not user:
                raise UserNotFoundError(public_id)
            return user.todos.all()
