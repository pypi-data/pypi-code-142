from typing import Callable

from faker import Faker

from authelio_sdk.client import Client
from authelio_sdk.models.user import User


def test_FUNC_client_user_filter_WITH_many_users_to_filter_all_EXPECT_users_found(
        sdk_client: Client,
        user_function: Callable[..., User],
        faker: Faker
) -> None:
    """
    Check whether all users can be retrieved.

    :param sdk_client: SDK client.
    :param user_function: User fixture.

    :return: No return.
    """
    # Create some random users.
    direct_permissions = [faker.unique.word() for _ in range(3)]
    users = [user_function(direct_permissions=direct_permissions).user_id for _ in range(5)]

    # Try to filter all users.
    user_data, next_page_id = sdk_client.user.filter()

    # Check that all users were found.
    for username in users:
        assert user_data[username].user_id == username
        assert sorted(user_data[username].direct_permissions) == sorted(direct_permissions)
