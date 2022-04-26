from app.repositories import TodoRepository


class TodoService:

    def __init__(self, todo_repository: TodoRepository) -> None:
        self._repository: TodoRepository = todo_repository

    def get_todos(self):
        return self._repository.get_all_todos()

    def get_todo_by_id(self, public_id: str):
        return self._repository.get_todo_by_id(public_id)

    def create_todo(self, todo_name: str, user_email: str):
        return self._repository.create_todo(name=todo_name, user_email=user_email)
