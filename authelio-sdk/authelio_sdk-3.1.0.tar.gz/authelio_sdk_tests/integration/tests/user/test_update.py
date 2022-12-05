from time import sleep
from typing import Callable

from faker import Faker

from authelio_sdk.client import Client
from authelio_sdk.models.group import Group
from authelio_sdk.models.user import User


def test_FUNC_client_user_update_WITH_existing_user_EXPECT_user_updated(
        sdk_client: Client,
        group_function: Callable[..., Group],
        user: User,
        faker: Faker
) -> None:
    """
    Test whether the existing user can be updated.

    :param sdk_client: SDK client.
    :param group_function: Group fixture.
    :param user: User fixture.
    :param faker: Faker fixture.

    :return: No return.
    """
    new_first_name = faker.first_name()
    new_email = faker.email()
    new_permissions = ['CREATE', 'GET']
    new_groups = [group_function().group_id for _ in range(2)]

    # Get the created new user.
    retrieved_user = sdk_client.user.get(user.user_id)[user.user_id]

    # Check that the original data exists.
    assert retrieved_user.user_id == user.user_id
    assert retrieved_user.first_name == user.first_name
    assert retrieved_user.email == user.email

    # Update with some random data.
    sdk_client.user.update(
        user_id=user.user_id,
        first_name=new_first_name,
        email=new_email,
        direct_permissions=new_permissions,
        group_ids=new_groups
    )

    # Currently, the cache is set for 10 seconds. Therefore, sleep for at least
    # 10 seconds or more (+1 second) and try get new data.
    sleep(11)

    # Refresh data from the database.
    refreshed_user = sdk_client.user.get(user.user_id)[user.user_id]

    # Check that the user data was indeed updated.
    assert refreshed_user.user_id == user.user_id
    assert refreshed_user.first_name == new_first_name
    assert refreshed_user.email == new_email
    assert sorted(refreshed_user.direct_permissions) == sorted(new_permissions)
    assert sorted(refreshed_user.group_ids) == sorted(new_groups)
