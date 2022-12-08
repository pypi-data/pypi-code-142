import time
from datetime import date, datetime
from typing import Any, Dict, List, Union

from tabulate import tabulate


def get_public_vars(obj: Any) -> Dict[str, Any]:
    return {k: v for k, v in vars(obj).items() if not k.startswith("_")}


def datetime_to_millis(timestamp: Union[date, datetime]) -> int:
    return int(time.mktime(timestamp.timetuple()) * 1000)


def millis_to_datetime(millis: int) -> datetime:
    return datetime.fromtimestamp(millis / 1000)


def millis_to_date(millis: int) -> date:
    return date.fromtimestamp(millis / 1000)


def tabulate_dict(obj: List[Dict[str, Any]]) -> str:
    return tabulate(headers="keys", tabular_data=obj)
