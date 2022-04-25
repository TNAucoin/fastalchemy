from typing import Iterator

from app.models.todo_model import Todo


class TodoRepository:

    def __init__(self, session_factory) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator[Todo]:
        with self.session_factory() as session:
            return session.query(Todo).all()
