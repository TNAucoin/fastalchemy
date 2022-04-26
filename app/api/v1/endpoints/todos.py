from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services import TodoService

router = APIRouter()


class CreateTodo(BaseModel):
    todo_name: str
    user_email: str


@router.get('/')
@inject
def get_all_todos(todo_service: TodoService = Depends(Provide["todo_service"])):
    return todo_service.get_todos()


@router.get('/{public_id}')
@inject
def get_todo_by_id(public_id: str, todo_service: TodoService = Depends(Provide["todo_service"])):
    return todo_service.get_todo_by_id(public_id)


@router.post('/')
@inject
def create_todo(todo: CreateTodo, todo_service: TodoService = Depends(Provide["todo_service"])):
    return todo_service.create_todo(todo.todo_name, todo.user_email)
