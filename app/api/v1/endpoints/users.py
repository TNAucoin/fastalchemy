from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, status, Depends
from pydantic import BaseModel

from app.containers import Container
from app.services import UserService

router = APIRouter()


class User(BaseModel):
    email: str
    name: str
    is_admin: bool = False


@router.get('/')
@inject
def get_all_users(user_service: UserService = Depends(Provide["user_service"])):
    return user_service.get_users()


@router.get('/{public_id}')
@inject
def get_user_by_id(public_id: str, user_service: UserService = Depends(Provide["user_service"])):
    return user_service.get_user_by_id(public_id)


@router.get('/{public_id}/todos/')
@inject
def get_user_todos(public_id: str, user_service: UserService = Depends(Provide["user_service"])):
    return user_service.get_user_todos(public_id)


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
def create_user(user: User, user_service: UserService = Depends(Provide["user_service"])):
    user_dict = user.dict()
    return user_service.create_user(**user_dict)
