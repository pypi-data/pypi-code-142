from typing import Callable

from authelio_sdk.client import Client
from authelio_sdk.models.group import Group
from authelio_sdk.models.user import User


def test_FUNC_client_group_users_WITH_users_in_group_EXPECT_group_users_returned(
        sdk_client: Client,
        group: Group,
        user_function: Callable[..., User]
) -> None:
    """
    Test whether group users function works as expected.

    :param sdk_client: Authelio SDK client.
    :param group: Group fixture.
    :param user_function: Function, that creates user entity.

    :return: No return.
    """
    user_ids = [user_function(group_ids=[group.group_id]).user_id for _ in range(5)]

    fetched_group_users = sdk_client.group.users(group.group_id)

    assert sorted(fetched_group_users) == sorted(user_ids)
