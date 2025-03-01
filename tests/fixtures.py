import pytest

from petisco import CorrelationId, Event
from petisco.domain.entities.client_id import ClientId
from petisco.domain.entities.user_id import UserId


@pytest.fixture
def given_any_user_id():
    return UserId("user_id")


@pytest.fixture
def given_any_client_id():
    return ClientId("Any User")


@pytest.fixture
def given_any_first_name():
    return "Any User"


@pytest.fixture
def given_any_topic():
    return "topic"


@pytest.fixture
def given_any_correlation_id():
    return CorrelationId("correlation_id")


@pytest.fixture
def make_user_created_event(given_any_user_id):
    class UserCreated(Event):
        user_id: UserId

        def __init__(self, user_id: UserId):
            self.user_id = user_id
            super().__init__()

    def _make_any_user_created_event(user_id=given_any_user_id):
        return UserCreated(user_id=user_id)

    return _make_any_user_created_event


@pytest.fixture
def make_first_name_added_event(given_any_user_id, given_any_first_name):
    class FirstNameAdded(Event):
        user_id: UserId
        first_name: str

        def __init__(self, user_id: UserId, first_name: str):
            self.user_id = user_id
            self.first_name = first_name
            super().__init__()

    def _make_any_first_name_added_event(
        user_id=given_any_user_id, first_name=given_any_first_name
    ):
        return FirstNameAdded(user_id=user_id, first_name=first_name)

    return _make_any_first_name_added_event
