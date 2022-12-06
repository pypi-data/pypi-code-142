import asyncio
from abc import abstractmethod
from concurrent.futures import ThreadPoolExecutor, wait
from functools import partial
from typing import List, TYPE_CHECKING

from ._entire_data_provider import get_entire_data_provider
from ._historical_join_responses import historical_join_responses
from ._intervals import DayIntervalType, get_day_interval_type
from .._errors import RDError
from .._tools import fields_arg_parser
from ..delivery._data._data_provider import Data, DataProvider


if TYPE_CHECKING:
    from .._content_type import ContentType
    from ._df_build_type import DFBuildType
    from .._types import Strings
    from ..delivery._data._data_provider import Response
    from ._historical_df_builder import HistoricalBuilder


def copy_fields(fields: List[str]) -> List[str]:
    if fields is None:
        return []

    if not isinstance(fields, (list, str)):
        raise AttributeError(f"fields not support type {type(fields)}")
    fields = fields_arg_parser.get_list(fields)

    return fields[:]


def get_first_success_response(responses: List["Response"]) -> "Response":
    successful = (response for response in responses if response.is_success)
    first_successful = next(successful, None)
    return first_successful


def validate_responses(responses: List["Response"]):
    response = get_first_success_response(responses)

    if response is None:
        error_message = "ERROR: No successful response.\n"

        error_codes = set()

        for response in responses:
            if response.errors:
                error = response.errors[0]

                if error.code not in error_codes:
                    error_codes.add(error.code)
                    sub_error_message = error.message

                    if "." in error.message:
                        sub_error_message, _ = error.message.split(".", maxsplit=1)

                    error_message += f"({error.code}, {sub_error_message}), "

        error_message = error_message[:-2]
        error = RDError(1, f"No data to return, please check errors: {error_message}")
        error.response = responses
        raise error


class HistoricalDataProvider(DataProvider):
    @abstractmethod
    def _get_axis_name(self, interval, **kwargs) -> str:
        # for override
        pass

    def get_data(self, *args, **kwargs) -> "Response":
        universe: List[str] = kwargs.pop("universe", [])
        entire_data_provider = get_entire_data_provider(kwargs.get("__content_type__"))

        with ThreadPoolExecutor(thread_name_prefix="HistoricalRequestThread") as ex:
            futures = []
            for inst_name in universe:
                fut = ex.submit(
                    entire_data_provider.get_data,
                    partial(super().get_data, *args),
                    universe=inst_name,
                    **kwargs,
                )
                futures.append(fut)

            wait(futures)

            responses = []
            for fut in futures:
                exception = fut.exception()

                if exception:
                    raise exception

                responses.append(fut.result())

        validate_responses(responses)

        return self._process_responses(
            responses,
            universe,
            copy_fields(kwargs.get("fields")),
            kwargs.get("interval"),
            kwargs.get("__content_type__"),
            kwargs.get("__dfbuild_type__"),
        )

    async def get_data_async(self, *args, **kwargs) -> "Response":
        universe: List[str] = kwargs.pop("universe", [])
        entire_data_provider = get_entire_data_provider(kwargs.get("__content_type__"))

        tasks = []
        for inst_name in universe:
            tasks.append(
                entire_data_provider.get_data_async(
                    partial(super().get_data_async, *args), universe=inst_name, **kwargs
                )
            )

        responses = await asyncio.gather(*tasks)
        if len(responses) == 1 and get_first_success_response(responses) is None:
            return responses.pop()

        return self._process_responses(
            responses,
            universe,
            copy_fields(kwargs.get("fields")),
            kwargs.get("interval"),
            kwargs.get("__content_type__"),
            kwargs.get("__dfbuild_type__"),
        )

    def _process_responses(
        self,
        responses: List["Response"],
        universe: "Strings",
        fields: "Strings",
        interval,
        content_type: "ContentType",
        dfbuild_type: "DFBuildType",
    ) -> "Response":
        df_builder: "HistoricalBuilder" = self.response.get_dfbuilder(
            content_type, dfbuild_type
        )

        if len(responses) == 1:
            raw = responses[0].data.raw
            data = Data(
                raw,
                dfbuilder=partial(
                    df_builder.build_one,
                    fields=fields,
                    axis_name=self._get_axis_name(interval),
                ),
            )
        else:
            raws = [response.data.raw for response in responses]
            data = Data(
                raws,
                dfbuilder=partial(
                    df_builder.build,
                    universe=universe,
                    fields=fields,
                    axis_name=self._get_axis_name(interval),
                ),
            )

        response = historical_join_responses(responses, data)
        return response


field_timestamp_by_day_interval_type = {
    DayIntervalType.INTER: "DATE",
    DayIntervalType.INTRA: "DATE_TIME",
}

axis_by_day_interval_type = {
    DayIntervalType.INTRA: "Timestamp",
    DayIntervalType.INTER: "Date",
}


def get_fields_events(fields, **kwargs):
    fields = fields_arg_parser.get_list(fields)
    result = copy_fields(fields)
    field_timestamp = "DATE_TIME"

    if field_timestamp not in result:
        result.append(field_timestamp)
    return ",".join(result)


def get_fields_summaries(fields, **kwargs):
    fields = fields_arg_parser.get_list(fields)
    result = copy_fields(fields)
    interval = kwargs.get("interval")
    field_timestamp = field_timestamp_by_day_interval_type.get(
        get_day_interval_type(interval or DayIntervalType.INTER)
    )
    if field_timestamp not in result:
        result.append(field_timestamp)
    return ",".join(result)


class SummariesDataProvider(HistoricalDataProvider):
    def _get_axis_name(self, interval, **kwargs):
        axis_name = axis_by_day_interval_type.get(
            get_day_interval_type(interval or DayIntervalType.INTER)
        )
        return axis_name


class EventsDataProvider(HistoricalDataProvider):
    def _get_axis_name(self, interval, **kwargs):
        return "Timestamp"
