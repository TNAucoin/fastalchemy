from fastapi import APIRouter

from app.api.v1.endpoints.users import router as users_endpoint_router

api_router = APIRouter()

api_router.include_router(users_endpoint_router, prefix='/users', tags=['Users'])
