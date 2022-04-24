from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, status, Depends
from pydantic import BaseModel

from app.containers import Container
from app.services import UserService

router = APIRouter()


class User(BaseModel):
    email: str
    password: str


@router.get('/')
@inject
async def get_all_users(user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.get_users()


@router.get('/{user_id}')
def get_user_by_id(user_id: str):
    pass


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
def create_user(user: User, user_service: UserService = Depends(Provide[Container.user_service])):
    user_dict = user.dict()
    return user_service.create_user(**user_dict)
