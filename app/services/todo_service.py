from app.repositories import TodoRepository


class TodoService:

    def __init__(self, todo_repository: TodoRepository) -> None:
        self._repository: TodoRepository = todo_repository
