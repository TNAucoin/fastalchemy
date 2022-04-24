from typing import Iterator
from uuid import uuid4

from app.models import User
from app.repositories import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self, email: str, name: str, is_admin: bool = False) -> User:
        uid = str(uuid4())
        return self._repository.add(email=email, name=name, is_admin=is_admin, public_id=uid)

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
