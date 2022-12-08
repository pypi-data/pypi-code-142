import time


def current_time() -> int:
    """Return the current time as milliseconds since epoch.

    Returns:
        int: Current time.
    """
    return int(time.time() * 1000)
