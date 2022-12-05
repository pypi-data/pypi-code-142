from typing import Callable

from authelio_sdk.client import Client
from authelio_sdk.models.group import Group


def test_FUNC_client_group_filter_WITH_new_group_EXPECT_new_group_found(
        sdk_client: Client,
        group_function: Callable[..., Group]
) -> None:
    """
    Test whether filter function works as expected.

    :param sdk_client: Authelio SDK client.
    :param group_function: Function, that creates group entity.

    :return: No return.
    """
    # Create some groups for filtering.
    group_ids = [group_function().group_id for _ in range(5)]

    filtered_groups, next_page_id = sdk_client.group.filter()

    filtered_group_ids = list(filtered_groups.keys())

    assert all(group_id in filtered_group_ids for group_id in group_ids)
