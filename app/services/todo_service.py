from app.repositories import TodoRepository


class TodoService:

    def __init__(self, todo_repository: TodoRepository) -> None:
        self._repository: TodoRepository = todo_repository

    def get_todos(self):
        return self._repository.get_all()
