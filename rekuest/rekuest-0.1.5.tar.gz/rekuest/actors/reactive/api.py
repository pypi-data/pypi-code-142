from rekuest.actors.vars import (
    get_current_assignation_helper,
    get_current_provision_helper,
)


def useUser() -> str:
    """Returns the user id of the current assignation"""
    return get_current_assignation_helper().user


def useGuardian() -> str:
    """Returns the guardian id of the current provision"""
    return get_current_provision_helper().guardian


def progress(percentage: int) -> None:
    """Progress

    Args:
        percentage (int): Percentage to progress to
    """

    helper = get_current_assignation_helper()
    helper.progress(percentage)


async def aprogress(percentage: int) -> None:
    """Progress

    Args:
        percentage (int): Percentage to progress to
    """

    helper = get_current_assignation_helper()
    await helper.aprogress(percentage)
