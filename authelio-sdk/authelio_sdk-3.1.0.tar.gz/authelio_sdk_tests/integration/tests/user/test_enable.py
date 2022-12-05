from time import sleep

from authelio_sdk.client import Client
from authelio_sdk.models.user import User


def test_FUNC_client_user_enable_WITH_valid_configuration_EXPECT_user_enabled(
        sdk_client: Client,
        user: User
) -> None:
    """
    Check whether the disabled user can be enabled.

    :param sdk_client: SDK client.
    :param user: User fixture.

    :return: No return.
    """
    # Get the created new user.
    refreshed_user = sdk_client.user.get(user.user_id)[user.user_id]

    # Check that the original data exists.
    assert refreshed_user.user_id == user.user_id
    assert refreshed_user.is_active

    sdk_client.user.disable(user.user_id)

    # Currently, the cache is set for 10 seconds. Therefore, sleep for at least
    # 10 seconds or more (+1 second) and try get new data.
    sleep(11)

    # Refresh data from the database.
    refreshed_user = sdk_client.user.get(user.user_id)[user.user_id]

    # Check that the user was indeed disabled.
    assert refreshed_user.user_id == user.user_id
    assert not refreshed_user.is_active

    sdk_client.user.enable(user.user_id)

    # Currently, the cache is set for 10 seconds. Therefore, sleep for at least
    # 10 seconds or more (+1 second) and try get new data.
    sleep(11)

    # Refresh data from the database.
    refreshed_user = sdk_client.user.get(user.user_id)[user.user_id]

    # Check that the user was indeed enabled.
    assert refreshed_user.user_id == user.user_id
    assert refreshed_user.is_active
