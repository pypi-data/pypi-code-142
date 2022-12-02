"""Time mock."""

from .date import random_datetime


def random_timestamp(
    unit="s", timezone="Asia/Shanghai", start_year=1970, end_year=2021
):
    """Return a random timestamp.

    Args:
        unit (str): unit. "s" or "ms" or "us"
        timezone (str): timezone str. default "Asia/Shanghai"
        start_year (int): start year
        end_year (int): end year
    Returns:
        (int): timestamp
    """
    # return as second count
    second_result = random_datetime(start_year, end_year, timezone).timestamp()

    if unit == "ms":
        return int(second_result * 1000)

    if unit == "us":
        return int(second_result * 1000000)

    return int(second_result)
