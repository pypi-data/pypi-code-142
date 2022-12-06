import abc
import dataclasses
from copy import deepcopy
from functools import partial
from itertools import product
from typing import List, Optional, Any, Set, Dict

import pandas as pd
from pandas.core.tools.datetimes import DatetimeScalarOrArrayConvertible

from .._tools._dataframe import convert_str_to_datetime, convert_dtypes


@dataclasses.dataclass
class CacheItem:
    """Data cache item."""

    fields_by_inst: Dict[str, List[Any]] = dataclasses.field(
        init=False, default_factory=dict
    )

    def add(self, inst: str, fields: List[Any]):
        """
        Add cache item as an instance:fields key-value pair.

        Parameters
        ----------
        inst : str
            Instance name.
        fields : List[Any]
            Instance fields.
        """
        self.fields_by_inst[inst] = fields

    def has(self, inst: str) -> bool:
        """
        Boolean that indicates is the instance stored in cache item or not.

        Parameters
        ----------
        inst : str
            Instance name.

        Returns
        -------
        bool
            True if instance is already stored, False otherwise.

        """
        return inst in self.fields_by_inst


@dataclasses.dataclass
class CacheItems:
    """Container for CacheItem instances."""

    _items: List[CacheItem] = dataclasses.field(init=False, default_factory=list)

    def add(self, inst: str, fields: List[Any]):
        """Add item as a key-value pair to CacheItems container.

        Parameters
        ----------
        inst : str
            Instance name.
        fields : List[Any]
            Instance fields.
        """
        item = CacheItem()
        item.add(inst, fields)
        self._items.append(item)

    def get_item_without(self, inst: str):
        """
        Gets cache item without particular instance.

        Parameters
        ----------
        inst : str
            Instance name.

        Returns
        -------
        item : CacheItem
            CacheItem that does not contain particular instance.

        """
        for item in self._items:
            if not item.has(inst):
                return item

        raise ValueError(f"Cannot get item without inst={inst}.")

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        if self._n < len(self._items):
            result = self._items[self._n]
            self._n += 1
            return result
        raise StopIteration


@dataclasses.dataclass
class DateCache:
    """
    Cache for data items that belong to particular date.

    DateCache has the following structure:

    Example
    -------
    DateCache {
        'date_1': CacheItems [
            CacheItem {
                dict {
                    'inst_A': [1, 2, 3],
                    'inst_B': [1, 2, 3]
                }
            },
            CacheItem {
                dict {
                    'inst_A': [1, 2, 3]
                }
            }
        ]
    }
    """

    _cache: Dict[str, CacheItems] = dataclasses.field(init=False, default_factory=dict)

    def can_update_fields(self, date: str, inst: str) -> bool:
        """
        Boolean that indicates can item fields be updated or not.

        Parameters
        ----------
        date : str
            Date string to retrieve a bunch of items that belong to this date.
        inst : str
            Instance name to check if CacheItems has this instance or not.

        Returns
        -------
        bool
            True if fields can be updated, False otherwise
        """
        for item in self._cache.get(date, CacheItems()):
            if not item.has(inst):
                return True

        return False

    def add(self, date: str, inst: str, fields: List[Any]):
        """Add items to CacheItems container in data cache during initialization.

        Parameters
        ----------
        date : str
            Date string.
        inst : str
            Instance name.
        fields : List[Any]
            Instance fields, filled according template.
        """
        items = self._cache.setdefault(date, CacheItems())
        items.add(inst, fields)

    def update_fields(
        self,
        date: str,
        inst: str,
        fields: List[Any],
        num_columns: int,
        unique_insts: List[str],
    ) -> List[Any]:
        """Updates fields in data cache and returns updated ones.

        Parameters
        ----------
        date : str
            Date string.
        inst : str
            Instance name.
        fields : List[Any]
            Fields list.
        num_columns : int
            Data columns quantity.
        unique_insts : List[str]
            List of unique instances across dataframe.

        Returns
        -------
        cache_fields : List[Any]
            List of updated fields.
        """
        fields_by_inst = self._cache[date].get_item_without(inst).fields_by_inst
        idx = max(unique_insts.index(inst) for inst in fields_by_inst.keys())
        cache_inst = unique_insts[idx]
        cache_fields = fields_by_inst[cache_inst]
        idx = unique_insts.index(inst)
        cache_idx = unique_insts.index(cache_inst)

        left_idx = cache_idx * num_columns + num_columns
        right_idx = idx * num_columns + num_columns

        for idx in range(left_idx, right_idx):
            cache_fields[idx] = fields[idx]

        fields_by_inst[inst] = cache_fields
        return cache_fields


def partial_process_index(
    num_unique_insts: int,
    num_columns: int,
    date_cache: DateCache,
    index: List[DatetimeScalarOrArrayConvertible],
    unique_insts: List[str],
    inst: str,
    date: str,
    fields: List[Any],
):
    is_add = True

    if num_unique_insts > 1:
        total = num_unique_insts * num_columns
        template = [pd.NA] * total

        idx = unique_insts.index(inst)
        right_idx = idx * num_columns + num_columns
        left_idx = idx * num_columns
        for item, idx in zip(fields, range(left_idx, right_idx)):
            template[idx] = item
        fields = template

        if date_cache.can_update_fields(date, inst):
            is_add = False
            fields = date_cache.update_fields(
                date, inst, fields, num_columns, unique_insts
            )

        else:
            date_cache.add(date, inst, fields)
            index.append(convert_str_to_datetime(date))

    else:
        index.append(convert_str_to_datetime(date))

    return fields, is_add


class DFBuilder(abc.ABC):
    auto_headers: Optional[List] = None

    @abc.abstractmethod
    def get_headers(self, content_data: dict) -> List[dict]:
        # for override
        pass

    def get_date_idxs(self, columns: List[str]) -> Set[int]:
        return {idx for idx, col in enumerate(columns) if "date" in col.lower()}

    def build_index(
        self, content_data: dict, use_field_names_in_headers: bool = False, **kwargs
    ) -> pd.DataFrame:

        key = "name" if use_field_names_in_headers else "title"

        headers = self.get_headers(content_data)
        columns = [header[key] for header in headers]
        date_idxs = self.get_date_idxs(columns)

        data = []
        fields_list = content_data.get("data", [])
        for fields in fields_list:
            fields = list(fields)

            for idx, item in enumerate(fields):
                if item is None:
                    fields[idx] = pd.NA

            for idx in date_idxs:
                fields[idx] = convert_str_to_datetime(fields[idx])

            data.append(fields)

        df = pd.DataFrame(data=data, columns=columns)
        df = convert_dtypes(df)
        return df

    def build_date_as_index(
        self,
        content_data: dict,
        use_field_names_in_headers: bool = False,
        use_multiindex: bool = False,
        **kwargs,
    ) -> pd.DataFrame:
        key = "name" if use_field_names_in_headers else "title"

        headers = self.get_headers(content_data)
        columns = [header[key] for header in headers]

        inst_header, date_header = self.auto_headers
        inst_header = inst_header[key]
        date_header = date_header[key]

        data = []
        index = []
        inst_idx = columns.index(inst_header)
        date_idx = columns.index(date_header)
        columns.pop(date_idx)
        columns.pop(inst_idx)
        num_columns = len(columns)

        date_idxs = self.get_date_idxs(columns)
        date_cache = DateCache()
        fields_list = content_data.get("data", [])
        unique_insts = list(dict.fromkeys(fields[inst_idx] for fields in fields_list))
        num_unique_insts = len(unique_insts)
        process_index = partial(
            partial_process_index,
            num_unique_insts,
            num_columns,
            date_cache,
            index,
            unique_insts,
        )
        for fields in fields_list:
            fields = list(fields)
            date_str = fields[date_idx]

            if not date_str:
                continue

            inst = fields[inst_idx]
            fields.pop(date_idx)
            fields.pop(inst_idx)

            fields = [pd.NA if i is None else i for i in fields]

            for idx in date_idxs:
                fields[idx] = convert_str_to_datetime(fields[idx])

            fields, is_add = process_index(inst, date_str, fields)

            is_add and data.append(fields)

        if num_columns > 1 and num_unique_insts > 1 or use_multiindex:
            columns = pd.MultiIndex.from_tuples(product(unique_insts, columns))

        elif num_unique_insts == 1:
            columns = pd.Index(data=columns, name=unique_insts.pop())

        elif num_columns == 1:
            columns = pd.Index(data=unique_insts, name=columns.pop())

        index = pd.Index(data=index, name=date_header)
        df = pd.DataFrame(data=data, columns=columns, index=index)
        df = convert_dtypes(df)
        df.sort_index(ascending=False, inplace=True)
        return df


class DFBuilderRDP(DFBuilder):
    """
    {
        "links": {"count": 2},
        "variability": "",
        "universe": [
            {
                "Instrument": "GOOG.O",
                "Company Common Name": "Alphabet Inc",
                "Organization PermID": "5030853586",
                "Reporting Currency": "USD",
            }
        ],
        "data": [
            ["GOOG.O", "2022-01-26T00:00:00", "USD", None],
            ["GOOG.O", "2020-12-31T00:00:00", None, "2020-12-31T00:00:00"],
        ],
        "messages": {
            "codes": [[-1, -1, -1, -2], [-1, -1, -2, -1]],
            "descriptions": [
                {"code": -2, "description": "empty"},
                {"code": -1, "description": "ok"},
            ],
        },
        "headers": [
            {
                "name": "instrument",
                "title": "Instrument",
                "type": "string",
                "description": "The requested Instrument as defined by the user.",
            },
            {
                "name": "date",
                "title": "Date",
                "type": "datetime",
                "description": "Date associated with the returned data.",
            },
            {
                "name": "TR.RevenueMean",
                "title": "Currency",
                "type": "string",
                "description": "The statistical average of all broker ...",
            },
            {
                "name": "TR.Revenue",
                "title": "Date",
                "type": "datetime",
                "description": "Is used for industrial and utility companies. ...",
            },
        ],
    }
    """

    auto_headers = [
        {"name": "instrument", "title": "Instrument"},
        {"name": "date", "title": "Date"},
    ]

    def get_headers(self, content_data) -> List[dict]:
        return content_data.get("headers", [])


class DFBuilderUDF(DFBuilder):
    """
    {
        "columnHeadersCount": 1,
        "data": [
            ["GOOG.O", "2022-01-26T00:00:00Z", "USD", ""],
            ["GOOG.O", "2020-12-31T00:00:00Z", "", "2020-12-31T00:00:00Z"],
        ],
        "headerOrientation": "horizontal",
        "headers": [
            [
                {"displayName": "Instrument"},
                {"displayName": "Date"},
                {"displayName": "Currency", "field": "TR.REVENUEMEAN.currency"},
                {"displayName": "Date", "field": "TR.REVENUE.DATE"},
            ]
        ],
        "rowHeadersCount": 2,
        "totalColumnsCount": 4,
        "totalRowsCount": 3,
    }
    """

    auto_headers = [
        {"name": "Instrument", "title": "Instrument"},
        {"name": "Date", "title": "Date"},
    ]

    def get_headers(self, content_data) -> List[dict]:
        headers = content_data["headers"]
        headers = headers[0]
        return [
            {
                "name": header.get("field") or header.get("displayName"),
                "title": header.get("displayName"),
            }
            for header in headers
        ]


def build_dates_calendars_df(raw: Any, **kwargs):
    raw = deepcopy(raw)
    add_periods_data = []

    clean_request_items = []
    for item in raw:
        if not item.get("error"):
            clean_request_items.append(item)

    for request_item in clean_request_items:
        if request_item.get("date"):
            request_item["date"] = convert_str_to_datetime(request_item["date"])

        request_item.pop("holidays", None)
        add_periods_data.append(request_item)

    _df = pd.DataFrame(add_periods_data)

    return _df


def build_dates_calendars_holidays_df(raw: Any, **kwargs):
    holidays_data = _dates_calendars_prepare_holidays_data(raw)
    holidays_df = pd.DataFrame(holidays_data)
    return holidays_df


def _dates_calendars_prepare_holidays_data(raw):
    raw = deepcopy(raw)
    holidays_data = []

    for request_item_holiday in raw:
        for holiday in request_item_holiday.get("holidays", []):
            if holiday.get("names"):
                for holiday_name in holiday["names"]:
                    holiday_name["tag"] = request_item_holiday.get("tag")
                    holiday_name["date"] = convert_str_to_datetime(holiday.get("date"))
                    holidays_data.append(holiday_name)
            else:
                holiday["tag"] = request_item_holiday.get("tag")
                holidays_data.append(holiday)
    return holidays_data


def default_build_df(raw: Any, **kwargs) -> pd.DataFrame:
    df = pd.DataFrame(raw)
    df = convert_dtypes(df)
    return df


def build_dates_calendars_date_schedule_df(raw: Any, **kwargs) -> pd.DataFrame:
    raw = deepcopy(raw)

    _dates = []
    for date in raw.get("dates"):
        _dates.append(convert_str_to_datetime(date))

    raw["dates"] = _dates
    df = pd.DataFrame(raw)
    return df


def build_empty_df(*args, **kwargs) -> pd.DataFrame:
    return pd.DataFrame()


dfbuilder_rdp = DFBuilderRDP()
dfbuilder_udf = DFBuilderUDF()
