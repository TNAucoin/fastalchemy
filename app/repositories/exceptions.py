class NotFoundError(Exception):
    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, {entity_id}")


class UserNotFoundError(NotFoundError):
    entity_name: str = "User"


class TodoNotFoundError(NotFoundError):
    entity_name = str = "Todo"
