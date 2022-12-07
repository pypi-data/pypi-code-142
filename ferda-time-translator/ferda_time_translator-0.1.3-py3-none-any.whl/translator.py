import json
from bisect import bisect_right
from datetime import datetime

from .constants import ferda_time


def low_bound_bisect(a, x):
    i = bisect_right(a, x)
    if i == 0:
        return 0
    else:
        return i - 1


def get_ferda_time(dt: datetime, tmz=None) -> str:
    time = int(dt.astimezone(tmz).strftime("%H%M"))
    keys = list(ferda_time.keys())
    return ferda_time[keys[low_bound_bisect(keys, time)]]


def get_current_ferda_time() -> str:
    return get_ferda_time(datetime.now())


def pretty_print_ferda_time(dt: datetime, tmz=None) -> None:
    print(f"{dt.astimezone(tmz).strftime('%I:%M %p')} | {get_ferda_time(dt)}")


def get_all_ferda_times():
    str_times = dict((key_to_time(str(k)), v) for k, v in ferda_time.items())
    return json.dumps(str_times, indent=4, sort_keys=True)


def key_to_time(time: str):
    if time == "0":
        time = "0000"
    return datetime.strptime(time, "%H%M").strftime("%H:%M")
