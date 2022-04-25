from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.services import TodoService

router = APIRouter()


@router.get('/')
@inject
def get_all_todos(todo_service: TodoService = Depends(Provide["todo_service"])):
    return todo_service.get_todos()
