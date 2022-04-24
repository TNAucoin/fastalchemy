from fastapi import FastAPI

from app.api.api_v1_router import api_router
from app.containers import Container


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(api_router, prefix='/v1', tags=['V1'])

    return app


app = create_app()
