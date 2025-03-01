from petisco.application.application_config import ApplicationConfig
from tests.integration.flask_app.toy_app.application.use_cases.create_user import (
    CreateUser,
)
from tests.integration.flask_app.toy_app.application.use_cases.get_user_name import (
    GetUserName,
)


class UseCaseBuilder:
    @staticmethod
    def create_user():

        config = ApplicationConfig.get_instance()
        user_repository = config.repositories_provider()["user"]
        return CreateUser(
            user_repository=user_repository, event_manager=config.event_manager
        )

    @staticmethod
    def get_user_name():
        config = ApplicationConfig.get_instance()
        user_repository = config.repositories_provider()["user"]

        return GetUserName(user_repository=user_repository)
