from typing import Optional, Callable, List

from b_lambda_layer_common.exceptions.container.not_found_error import NotFoundError
from faker import Faker
from pytest import fixture

from authelio_sdk.client import Client
from authelio_sdk.models.user import User


@fixture(scope='function')
def user_function(sdk_client: Client, faker: Faker) -> Callable[..., User]:
    """
    Fixture that returns a function.

    The function creates a user in Authelio.

    This fixture does automatic cleanup (deletes created users) after test run.

    :return: Returns a function that in Authelio and returns a user object.
    """
    user_ids = []

    def __create_user(
            group_ids: Optional[List[str]] = None,
            username: Optional[str] = None,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            email: Optional[str] = None,
            direct_permissions: Optional[List[str]] = None
    ) -> User:
        user = sdk_client.user.create(
            group_ids=group_ids,
            email=email or faker.email(),
            username=username or faker.user_name(),
            first_name=first_name or faker.first_name(),
            last_name=last_name or faker.last_name(),
            direct_permissions=direct_permissions
        )

        # Set a new password for a user.
        user.password = 'Welcome2AuthelioAPI!'
        # Confirm the new password in the system.
        sdk_client.user.confirm(user.user_id, user.tmp_password, user.password)

        user_id = user.user_id
        user_ids.append(user_id)

        return user

    yield __create_user

    for user_id in user_ids:
        try:
            sdk_client.user.delete(user_id)
        except NotFoundError:
            # User was not found, maybe deleted already, hence ignore this error.
            continue


@fixture(scope='function')
def user(user_function) -> User:
    """
    Fixture that creates a user in the Authelio
    and returns dictionary representation of that newly created user.

    This fixture does automatic cleanup (deletes created user in the Authelio) after test run.

    :return: Returns a dictionary representation of newly created and saved user.
    """

    return user_function()
