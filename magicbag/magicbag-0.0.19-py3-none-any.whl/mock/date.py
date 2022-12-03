"""Date type generator for mock data."""
import random
from datetime import date, datetime

import pytz


def random_date(start_year=1970, end_year=2021):
    """Return a random date.

    Args:
        start_year (int): start year
        end_year (int): end year
    Returns:
        (datatime.date): datetime.date object
    """
    return date(
        random.randint(start_year, end_year),
        random.randint(1, 12),
        random.randint(1, 28),
    )


def random_datetime(start_year=1970, end_year=2021, timezone="UTC"):
    """Return a random datetime.

    Args:
        start_year (int): start year
        end_year (int): end year
        timezone (str): timezone
    Returns:
        (datatime.datetime): datetime.datetime object
    """
    timezone = pytz.timezone(timezone)

    return datetime(
        random.randint(start_year, end_year),
        random.randint(1, 12),
        random.randint(1, 28),
        random.randint(0, 23),
        random.randint(0, 59),
        random.randint(0, 59),
        tzinfo=timezone,
    )
