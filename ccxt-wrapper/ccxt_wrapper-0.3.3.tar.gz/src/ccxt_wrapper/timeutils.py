import asyncio
import warnings
from datetime import datetime, timedelta
from math import ceil

from tqdm import tqdm


def round_time(t: datetime, interval: timedelta) -> datetime:
    if isinstance(t, datetime) and all(
        "pandas" not in type(x).__module__ for x in (t, interval)
    ):
        return t - (t - datetime.min.replace(tzinfo=t.tzinfo)) % interval
    try:
        from pandas import Timedelta, Timestamp

        if isinstance(interval, Timedelta):
            interval = interval.to_pytimedelta()
        if isinstance(t, Timestamp):
            return Timestamp(round_time(t.to_pydatetime(), interval))
        else:
            return round_time(t, interval)
    except ImportError:
        pass
    raise TypeError(f"Unsupported type: {type(t)}")


async def wait_until(t: datetime, enable_tqdm: bool = False) -> None:
    """Wait until the given time.

    Parameters
    ----------
    t : datetime
        The time to wait until
    enable_tqdm : bool, optional
        Whether to enable the tqdm progress bar, by default False
    """

    if t.utcnow() > t:
        warnings.warn(
            RuntimeWarning(
                f"Time is in the past, now:{t.utcnow()}, t:{t}, delta:{t.utcnow() - t}"
            )
        )

    pbar = tqdm(
        total=ceil((t - t.utcnow()).total_seconds()),
        disable=not enable_tqdm,
        bar_format="|{bar}| {percentage:.2f}% [{elapsed}<{remaining}]",
    )
    last_update = t.utcnow()
    while t.utcnow() < t:
        await asyncio.sleep(min((t - t.utcnow()).total_seconds(), 0.1))
        pbar.update((t.utcnow() - last_update).total_seconds())
        last_update = t.utcnow()
    pbar.n = pbar.total


if __name__ == "__main__":
    from pandas import Timedelta, Timestamp

    asyncio.run(
        wait_until(
            round_time(Timestamp.utcnow(), Timedelta(seconds=1))
            + Timedelta(seconds=10),
            enable_tqdm=True,
        )
    )
