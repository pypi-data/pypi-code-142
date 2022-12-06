from typing import Union, TYPE_CHECKING

from .._intervals import DayIntervalType, Intervals, get_day_interval_type
from ..._tools import hp_universe_parser, validate_types, try_copy_to_list
from ...delivery._data._data_provider import BaseResponse, Data, DataProviderLayer
from ._historical_pricing_request_factory import get_content_type_by_interval

if TYPE_CHECKING:
    from ._enums import OptAdjustments, OptMarketSession
    from ..._types import (
        OptInt,
        ExtendedParams,
        OptDateTime,
        StrStrings,
        StrStrings,
    )


class Definition(DataProviderLayer[BaseResponse[Data]]):
    """
    Summary line of this class that defines parameters for requesting summaries from historical pricing

    Parameters
    ----------
    universe : str or list of str
        The entity universe
    interval : str or Intervals, optional
        The consolidation interval in ISO8601
    start : str or date or datetime or timedelta, optional
        The start date and timestamp of the query in ISO8601 with UTC only
    end : str or date or datetime or timedelta, optional
        The end date and timestamp of the query in ISO8601 with UTC only
    adjustments : list of Adjustments or Adjustments or str, optional
        The adjustment list or Adjustments type
    sessions : list of MarketSession or MarketSession or str, optional
        The list of market session classification or str
    count : int, optional
        The maximum number of data returned. Values range: 1 - 10000
    fields : list, optional
        The list of fields that are to be returned in the response
    extended_params : dict, optional
        If necessary other parameters

    Examples
    --------
    >>> from refinitiv.data.content.historical_pricing import summaries
    >>> definition_summaries = summaries.Definition("EUR")
    >>> response = definition_summaries.get_data()

    """

    def __init__(
        self,
        universe: "StrStrings",
        interval: Union[str, Intervals] = None,
        start: "OptDateTime" = None,
        end: "OptDateTime" = None,
        adjustments: "OptAdjustments" = None,
        sessions: "OptMarketSession" = None,
        count: "OptInt" = None,
        fields: "StrStrings" = None,
        extended_params: "ExtendedParams" = None,
    ) -> None:
        # By default, if interval is not defined, interday default value is requested
        day_interval_type = get_day_interval_type(interval or DayIntervalType.INTER)
        content_type = get_content_type_by_interval(day_interval_type)
        validate_types(count, [int, type(None)], "count")
        universe = try_copy_to_list(universe)
        universe = hp_universe_parser.get_list(universe)
        adjustments = try_copy_to_list(adjustments)
        sessions = try_copy_to_list(sessions)
        fields = try_copy_to_list(fields)

        super().__init__(
            data_type=content_type,
            universe=universe,
            interval=interval,
            start=start,
            end=end,
            adjustments=adjustments,
            sessions=sessions,
            count=count,
            fields=fields,
            extended_params=extended_params,
        )
