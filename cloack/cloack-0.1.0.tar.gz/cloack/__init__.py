from datetime import datetime, timedelta

from .constants import RESOLUTIONS


# https://delorean.readthedocs.io/en/latest/quickstart.html#truncation
# The week starts on Monday: https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday
def truncate_dt(dt: datetime, discretization: str) -> datetime:
    if discretization in RESOLUTIONS:
        return dt.replace(**RESOLUTIONS[discretization])
    elif discretization == "week":
        return dt.replace(**RESOLUTIONS["day"]) - timedelta(days=dt.isoweekday() - 1)
    else:
        available_discretizations = ", ".join(
            [*map(repr, RESOLUTIONS.keys()), repr("week")]
        )

        raise ValueError(
            f"{repr(discretization)} is not supported. Available discretizations: {available_discretizations}."
        )
