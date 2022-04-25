from fastapi import APIRouter

from app.api.v1.endpoints.users import router as users_endpoint_router
from app.api.v1.endpoints.todos import router as todos_endpoint_router

api_router = APIRouter()

api_router.include_router(users_endpoint_router, prefix='/users', tags=['Users'])
api_router.include_router(todos_endpoint_router, prefix='/todos', tags=['Todos'])
