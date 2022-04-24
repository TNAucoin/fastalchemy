from dependency_injector import containers, providers

from app.api.v1.endpoints import users
from app.database import Database
from app.repositories import UserRepository, TodoRepository
from app.services import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[users])
    config = providers.Configuration(yaml_files=["config.yml"])
    db = providers.Singleton(Database, db_url=config.db.url)
    todo_repository = providers.Factory(
        TodoRepository,
        session_factory=db.provided.session,
    )
    todo_service = providers.Factory(
        UserService,
        todo_repository=todo_repository
    )
    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )
    user_service = providers.Factory(
        UserService,
        user_repository=user_repository
    )
