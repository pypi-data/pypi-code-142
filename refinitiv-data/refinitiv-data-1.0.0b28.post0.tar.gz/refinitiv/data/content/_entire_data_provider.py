import abc
from datetime import timedelta
from typing import Callable, List, Tuple, Any, Optional, TYPE_CHECKING

from ._historical_join_responses import historical_join_responses
from .._content_type import ContentType
from .._tools import hp_datetime_adapter
from ..content._intervals import (
    interval_arg_parser,
    get_day_interval_type,
    DayIntervalType,
    Intervals,
)


if TYPE_CHECKING:
    from ..delivery._data._data_provider import Response


INTERVALS_BY_SECONDS = {
    Intervals.ONE_MINUTE.value: 59,
    Intervals.FIVE_MINUTES.value: 299,
    Intervals.TEN_MINUTES.value: 599,
    Intervals.THIRTY_MINUTES.value: 1799,
    Intervals.SIXTY_MINUTES.value: 3599,
    Intervals.HOURLY.value: 3599,
}

EVENTS_MAX_LIMIT = 10000


def remove_last_date_elements(data: List[List[Any]]) -> List[List[Any]]:
    end_date = data[-1][0]
    for index, item in enumerate(data[::-1]):
        if item[0] != end_date:
            data = data[:-index]
            return data

    return data


def create_raw(responses: List["Response"], entire_data: List[List[Any]]) -> dict:
    for response in responses:
        if response.is_success:
            raw = response.data.raw
            raw["data"] = entire_data
            return response.data.raw

    return {}


class EntireDataProvider(abc.ABC):
    @abc.abstractmethod
    def request_with_dates(self, *args) -> Tuple[List["Response"], List[List[Any]]]:
        pass

    @abc.abstractmethod
    def request_with_count(self, *args) -> Tuple[List["Response"], List[List[Any]]]:
        pass

    @abc.abstractmethod
    def get_request_function(self, **kwargs) -> Optional[Callable]:
        pass

    @abc.abstractmethod
    def get_request_function_async(self, **kwargs) -> Optional[Callable]:
        pass

    def get_data(self, provide_data: Callable, **kwargs) -> "Response":
        request_function = self.get_request_function(**kwargs)

        if request_function:
            responses, entire_data = request_function(provide_data, **kwargs)
            raw = create_raw(responses, entire_data)

        else:
            response = provide_data(**kwargs)
            responses = [response]
            raw = response.data.raw

        response = historical_join_responses(responses, raw)
        return response

    async def get_data_async(self, provide_data: Callable, **kwargs) -> "Response":
        request_function = self.get_request_function_async(**kwargs)

        if request_function:
            responses, entire_data = await request_function(provide_data, **kwargs)
            raw = create_raw(responses, entire_data)

        else:
            response = await provide_data(**kwargs)
            responses = [response]
            raw = response.data.raw

        response = historical_join_responses(responses, raw)
        return response


class SummariesEntireDataProvider(EntireDataProvider):
    def request_with_dates(
        self,
        provide_data: Callable,
        interval,
        start: str,
        end: str,
        count: Optional[int] = None,
        **kwargs,
    ) -> Tuple[List["Response"], List[List[Any]]]:
        interval_sec = INTERVALS_BY_SECONDS[interval_arg_parser.get_str(interval)]

        entire_data = []
        responses = []
        unique_data_count = set()

        finished_date = hp_datetime_adapter.get_localize(start)
        # need do ... while
        end_date = finished_date + timedelta(microseconds=1)

        while end_date > finished_date and len(unique_data_count) <= 1:
            response = provide_data(
                interval=interval,
                count=count,
                start=start,
                end=end,
                **kwargs,
            )
            responses.append(response)

            if not response.is_success:
                break

            raw = response.data.raw
            if len(raw) == 0 or not raw.get("data"):
                break

            data = raw["data"]
            entire_data.extend(data)

            if count is not None and len(entire_data) >= count:
                entire_data = entire_data[:count]
                break

            unique_data_count.add(len(data))

            end_date = data[-1][0]
            end = end_date
            end_date = hp_datetime_adapter.get_localize(end_date)

            if (end_date - finished_date).seconds < interval_sec:
                break

        return responses, entire_data

    async def request_with_dates_async(
        self,
        provide_data: Callable,
        interval,
        start: str,
        end: str,
        count: Optional[int] = None,
        **kwargs,
    ) -> Tuple[List["Response"], List[List[Any]]]:
        interval_sec = INTERVALS_BY_SECONDS[interval_arg_parser.get_str(interval)]

        entire_data = []
        responses = []
        unique_data_count = set()

        finished_date = hp_datetime_adapter.get_localize(start)
        # need do ... while
        end_date = finished_date + timedelta(microseconds=1)

        while end_date > finished_date and len(unique_data_count) <= 1:
            response = await provide_data(
                interval=interval,
                count=count,
                start=start,
                end=end,
                **kwargs,
            )
            responses.append(response)

            if not response.is_success:
                break

            raw = response.data.raw
            if len(raw) == 0 or not raw.get("data"):
                break

            data = raw["data"]
            entire_data.extend(data)

            if count is not None and len(entire_data) >= count:
                entire_data = entire_data[:count]
                break

            unique_data_count.add(len(data))

            end_date = data[-1][0]
            end = end_date
            end_date = hp_datetime_adapter.get_localize(end_date)

            if (end_date - finished_date).seconds < interval_sec:
                break

        return responses, entire_data

    def request_with_count(
        self,
        provide_data: Callable,
        interval,
        count: int,
        end: str,
        start: Optional[str] = None,
        **kwargs,
    ) -> Tuple[List["Response"], List[List[Any]]]:
        interval_sec = INTERVALS_BY_SECONDS[interval_arg_parser.get_str(interval)]

        c = count
        entire_data = []
        responses = []
        unique_data_count = set()

        finished_date = None
        if start:
            finished_date = hp_datetime_adapter.get_localize(start)

        while c > 0 and len(unique_data_count) <= 1:
            response = provide_data(
                interval=interval,
                count=count,
                start=start,
                end=end,
                **kwargs,
            )
            responses.append(response)

            if not response.is_success:
                break

            raw = response.data.raw
            if len(raw) == 0 or not raw.get("data"):
                break

            data = raw["data"]
            entire_data.extend(data)

            unique_data_count.add(len(data))

            c -= len(data)
            count = c
            end_date = data[-1][0]
            end = end_date

            if finished_date:
                end_date = hp_datetime_adapter.get_localize(end_date)

                if (end_date - finished_date).seconds < interval_sec:
                    break

        return responses, entire_data

    async def request_with_count_async(
        self,
        provide_data: Callable,
        interval,
        count: int,
        end: str,
        start: Optional[str] = None,
        **kwargs,
    ) -> Tuple[List["Response"], List[List[Any]]]:
        interval_sec = INTERVALS_BY_SECONDS[interval_arg_parser.get_str(interval)]

        c = count
        entire_data = []
        responses = []
        unique_data_count = set()

        finished_date = None
        if start:
            finished_date = hp_datetime_adapter.get_localize(start)

        while c > 0 and len(unique_data_count) <= 1:
            response = await provide_data(
                interval=interval,
                count=count,
                start=start,
                end=end,
                **kwargs,
            )
            responses.append(response)

            if not response.is_success:
                break

            raw = response.data.raw
            if len(raw) == 0 or not raw.get("data"):
                break

            data = raw["data"]
            entire_data.extend(data)

            unique_data_count.add(len(data))

            c -= len(data)
            count = c
            end_date = data[-1][0]
            end = end_date

            if finished_date:
                end_date = hp_datetime_adapter.get_localize(end_date)

                if (end_date - finished_date).seconds < interval_sec:
                    break

        return responses, entire_data

    def get_request_function(
        self,
        interval,
        count: Optional[int] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        **kwargs,
    ) -> Optional[Callable]:
        request_function = None

        if (
            interval is None
            or get_day_interval_type(interval) is not DayIntervalType.INTRA
        ):
            return request_function

        if start is not None and end is not None:
            request_function = self.request_with_dates

        elif count is not None and count > 0:
            request_function = self.request_with_count

        return request_function

    def get_request_function_async(
        self,
        interval,
        count: Optional[int] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        **kwargs,
    ) -> Optional[Callable]:
        request_function = None

        if (
            interval is None
            or get_day_interval_type(interval) is not DayIntervalType.INTRA
        ):
            return request_function

        if start is not None and end is not None:
            request_function = self.request_with_dates_async

        elif count is not None and count > 0:
            request_function = self.request_with_count_async

        return request_function


class EventsEntireDataProvider(EntireDataProvider):
    def request_with_dates(
        self,
        provide_data: Callable,
        start: str,
        end: str,
        count: Optional[int] = None,
        **kwargs,
    ) -> Tuple[List["Response"], List[List[Any]]]:
        entire_data = []
        responses = []

        finished_date = hp_datetime_adapter.get_localize(start)
        # need do ... while
        end_date = finished_date + timedelta(microseconds=1)
        response_count = EVENTS_MAX_LIMIT

        while end_date > finished_date and response_count >= EVENTS_MAX_LIMIT:
            response = provide_data(count=count, start=start, end=end, **kwargs)
            responses.append(response)

            if not response.is_success:
                break

            raw = response.data.raw
            if len(raw) == 0 or not raw.get("data"):
                break

            data = raw["data"]

            response_count = len(data)
            if response_count >= EVENTS_MAX_LIMIT:
                data = remove_last_date_elements(data)

            entire_data.extend(data)

            end_date = data[-1][0]
            end = end_date
            end_date = hp_datetime_adapter.get_localize(end_date)

            if count is not None and len(entire_data) >= count:
                entire_data = entire_data[:count]
                break

        return responses, entire_data

    async def request_with_dates_async(
        self,
        provide_data: Callable,
        start: str,
        end: str,
        count: Optional[int] = None,
        **kwargs,
    ) -> Tuple[List["Response"], List[List[Any]]]:
        entire_data = []
        responses = []

        finished_date = hp_datetime_adapter.get_localize(start)
        # need do ... while
        end_date = finished_date + timedelta(microseconds=1)
        response_count = EVENTS_MAX_LIMIT

        while end_date > finished_date and response_count >= EVENTS_MAX_LIMIT:
            response = await provide_data(count=count, start=start, end=end, **kwargs)
            responses.append(response)

            if not response.is_success:
                break

            raw = response.data.raw
            if len(raw) == 0 or not raw.get("data"):
                break

            data = raw["data"]

            response_count = len(data)
            if response_count >= EVENTS_MAX_LIMIT:
                data = remove_last_date_elements(data)

            entire_data.extend(data)

            end_date = data[-1][0]
            end = end_date
            end_date = hp_datetime_adapter.get_localize(end_date)

            if count is not None and len(entire_data) >= count:
                entire_data = entire_data[:count]
                break

        return responses, entire_data

    def request_with_count(
        self, provide_data: Callable, count: int, start: str, end: str, **kwargs
    ) -> Tuple[List["Response"], List[List[Any]]]:
        entire_data = []
        responses = []
        c = count
        response_count = EVENTS_MAX_LIMIT

        while c > 0 and response_count >= EVENTS_MAX_LIMIT:
            response = provide_data(count=count, start=start, end=end, **kwargs)
            responses.append(response)

            if not response.is_success:
                break

            raw = response.data.raw
            if len(raw) == 0 or not raw.get("data"):
                break

            data = raw["data"]

            response_count = len(data)
            if response_count >= EVENTS_MAX_LIMIT:
                data = remove_last_date_elements(data)

            entire_data.extend(data)

            c -= len(data)
            count = c
            end_date = data[-1][0]
            end = end_date

        return responses, entire_data

    async def request_with_count_async(
        self, provide_data: Callable, count: int, start: str, end: str, **kwargs
    ) -> Tuple[List["Response"], List[List[Any]]]:
        entire_data = []
        responses = []
        c = count
        response_count = EVENTS_MAX_LIMIT

        while c > 0 and response_count >= EVENTS_MAX_LIMIT:
            response = await provide_data(count=count, start=start, end=end, **kwargs)
            responses.append(response)

            if not response.is_success:
                break

            raw = response.data.raw
            if len(raw) == 0 or not raw.get("data"):
                break

            data = raw["data"]

            response_count = len(data)
            if response_count >= EVENTS_MAX_LIMIT:
                data = remove_last_date_elements(data)

            entire_data.extend(data)

            c -= len(data)
            count = c
            end_date = data[-1][0]
            end = end_date

        return responses, entire_data

    def get_request_function(
        self,
        count: Optional[int] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        **kwargs,
    ) -> Optional[Callable]:
        request_function = None

        if start is not None and end is not None:
            request_function = self.request_with_dates

        elif count is not None and count > EVENTS_MAX_LIMIT:
            request_function = self.request_with_count

        return request_function

    def get_request_function_async(
        self,
        count: Optional[int] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        **kwargs,
    ) -> Optional[Callable]:
        request_function = None

        if start is not None and end is not None:
            request_function = self.request_with_dates_async

        elif count is not None and count > EVENTS_MAX_LIMIT:
            request_function = self.request_with_count_async

        return request_function


entire_data_provider_by_content_type = {
    ContentType.HISTORICAL_PRICING_EVENTS: EventsEntireDataProvider(),
    ContentType.CUSTOM_INSTRUMENTS_EVENTS: EventsEntireDataProvider(),
    ContentType.HISTORICAL_PRICING_INTERDAY_SUMMARIES: SummariesEntireDataProvider(),
    ContentType.HISTORICAL_PRICING_INTRADAY_SUMMARIES: SummariesEntireDataProvider(),
    ContentType.CUSTOM_INSTRUMENTS_INTERDAY_SUMMARIES: SummariesEntireDataProvider(),
    ContentType.CUSTOM_INSTRUMENTS_INTRADAY_SUMMARIES: SummariesEntireDataProvider(),
}


def get_entire_data_provider(content_type: ContentType) -> EntireDataProvider:
    entire_data_provider = entire_data_provider_by_content_type.get(content_type)

    if not entire_data_provider:
        raise ValueError(f"Cannot find entire data provider for {content_type}")

    return entire_data_provider
