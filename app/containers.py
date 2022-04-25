from dependency_injector import containers, providers
from dependency_injector.providers import Singleton, Factory
from app.database import Database
from app.repositories import UserRepository, TodoRepository
from app.services import UserService, TodoService


def create_user_service(db: Singleton[Database]) -> Factory[UserService]:
    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )
    user_service = providers.Factory(
        UserService,
        user_repository=user_repository
    )
    return user_service


def create_todo_service(db: Singleton[Database]) -> Factory[TodoService]:
    todo_repository = providers.Factory(
        TodoRepository,
        session_factory=db.provided.session,
    )
    todo_service = providers.Factory(
        TodoService,
        todo_repository=todo_repository
    )
    return todo_service


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".api.v1.endpoints.users", ".api.v1.endpoints.todos"])
    config = providers.Configuration(yaml_files=["config.yml"])
    db = providers.Singleton(Database, db_url=config.db.url)
    todo_service = create_todo_service(db)
    user_service = create_user_service(db)
