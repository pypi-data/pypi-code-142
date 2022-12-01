import math
import uuid
from typing import List, Union, Tuple, Iterable, Callable, Sequence
import itertools
import datetime
from cooptools.typevalidation import date_tryParse

def flattened_list_of_lists(list_of_lists: List[List], unique: bool = False) -> List:
    flat = list(itertools.chain.from_iterable(list_of_lists))

    if unique:
        flat = list(set(flat))

    return flat

def all_indxs_in_lst(lst: List, value) -> List[int]:
    idxs = []
    idx = -1
    while True:
        try:
            idx = lst.index(value, idx + 1)
            idxs.append(idx)
        except ValueError as e:
            break
    return idxs

def next_perfect_square_rt(n: int) -> int:
    int_root_n = int(math.sqrt(n))
    if int_root_n == n:
        return n
    return int_root_n + 1

def last_day_of_month(any_day: datetime.date):
    # this will never fail
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month_first_day = (any_day.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month_first_day - datetime.timedelta(days=1)


def month_range(start_date, end_date) -> List[datetime.date]:
    date1 = date_tryParse(start_date).replace(day=1)
    date2 = last_day_of_month(date_tryParse(end_date))

    if date2 < date1:
        raise ValueError(f"invalid date range {start_date}->{end_date}")

    months = []
    while date1 < date2:
        month = date1.month
        year = date1.year
        months.append(last_day_of_month(date1))
        next_month = month + 1 if month != 12 else 1
        next_year = year + 1 if next_month == 1 else year
        date1 = date1.replace(month=next_month, year=next_year)

    return months

def date_range(start_date: datetime.date, end_date:datetime.date) -> List[datetime.date]:
    date1 = date_tryParse(start_date)
    date2 = date_tryParse(end_date)

    verify(lambda: date1 < date2, msg=f"invalid date range {date1}->{date2}", block=True)

    dates = []
    while date1 <= date2:
        dates.append(date1)
        date1 = date1 + datetime.timedelta(days=1)

    return dates

def date_to_condensed_string(date) -> str:
    date = date_tryParse(date)

    mo = str(date.month)
    if len(mo) == 1: mo = f"0{mo}"
    day = str(date.day)
    if len(day) == 1: day = f"0{day}"

    return f"{date.year}{mo}{day}"

def try_resolve_guid(id: str) -> Union[str, uuid.UUID]:

    try:
        return uuid.UUID(id)
    except:
        return id

def split_strip(txt: str):
    return [x.strip() for x in txt.split(',')]

def duplicates_in_list(lst: Iterable) -> List:
    res = list(set([ele for ele in lst
                    if list(lst).count(ele) > 1]))
    return res


def verify(verify_func: Callable, msg: str=None, msg_sub: str=None, block: bool=True):
    if msg_sub is not None:
        msg += f"\n\t{msg_sub}"

    result = verify_func()

    if not result and block:
        raise ValueError(msg)

    return result

def verify_val(val: Union[int, float],
               low: Union[int, float] = None,
               low_inc: Union[int, float] = None,
               hi: Union[int, float] = None,
               hi_inc: Union[int, float] = None,
               error_msg: str = None,
               block: bool = True) -> bool:

    if low_inc is not None:
        low_tst = lambda: val >= low_inc
        low_txt = f"{low_inc} <="
    elif low is not None:
        low_tst = lambda: val > low
        low_txt = f"{low} <"
    else:
        low_tst = lambda: True
        low_txt = f""

    if hi_inc is not None:
        hi_tst = lambda: val <= hi_inc
        hi_txt = f"<= {hi_inc}"
    elif hi is not None:
        hi_tst = lambda: val < hi
        hi_txt = f"< {hi}"
    else:
        hi_tst = lambda: True
        hi_txt = ""

    tst = lambda:  low_tst() and hi_tst()

    msg = f"invalid value: {low_txt} {val} {hi_txt} is not valid"
    return verify(tst, msg, msg_sub=error_msg, block=block)




def verify_unique(lst: Iterable, error_msg: str = None):
    dups = duplicates_in_list(lst)

    tst = lambda: len(dups) == 0
    msg = f"All the values are not unique. Dups: {dups}"
    verify(tst, msg, error_msg)

def verify_len_match(iterable1, iterable2, error_msg: str = None):
    msg = f"{iterable1} and {iterable2} do not have the same length ({len(iterable1)} vs {len(iterable2)})"

    tst = lambda: len(iterable1) == len(iterable2)
    verify(tst, msg, error_msg)


def verify_len(iterable, length: int, error_msg: str = None):
    msg = f"{iterable} does not have len {length} ({len(iterable)})"

    tst = lambda: len(iterable) == length
    verify(tst, msg, error_msg)

def degree_to_rads(degrees: float) -> float:
    return degrees * math.pi / 180

def rads_to_degrees(rads: float) -> float:
    return rads * 180 / math.pi


def bounding_box_of_points(pts: Sequence[Tuple[float, float]]) -> Tuple[float, float, float, float]:
    min_x = min([p[0] for p in pts])
    max_x = max([p[0] for p in pts])
    min_y = min([p[1] for p in pts])
    max_y = max([p[1] for p in pts])

    w = max_x - min_x
    h = max_y - min_y

    return (min_x, min_y, w, h)

def divided_length(inc: float,
                   start: float = None,
                   start_inc: float = None,
                   stop: float = None,
                   stop_inc: float = None,
                   force_to_ends: bool = False) -> List[float]:
    vals = []

    s = start or start_inc
    e = stop or stop_inc

    if s <= e:
        tst = lambda val: verify_val(val, low=start, low_inc=start_inc, hi=stop, hi_inc=stop_inc, block=False)
    else:
        tst = lambda val: verify_val(val, low=stop, low_inc=stop_inc, hi=start, hi_inc=start_inc, block=False)
        inc *= -1

    ii = s
    while tst(ii):
        vals.append(ii)
        ii += inc

    # force to ends
    if force_to_ends:
        remaining_delta = abs(e - vals[-1])
        vals = [x + remaining_delta / (len(vals) - 1) * (ii) for ii, x in enumerate(vals)]

    return vals

if __name__ == "__main__":
    from pprint import pprint

    # pprint(month_range('1/1/21', '8/9/22'))

    print(date_to_condensed_string('11/5/2022'))