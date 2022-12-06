from typing import TYPE_CHECKING, Union, Iterable, Tuple

from pandas import DataFrame

from ._containers import (
    FieldsContainer,
    UniverseContainer,
    ADCDataContainer,
    HPAndCustInstDataContainer,
)
from ._data_provider import DataProvider, convert_types
from .context_collection import get_adc_context
from .context_collection._context_factory import get_hp_and_custinst_context
from .._core.session import get_default, raise_if_closed
from .._errors import ScopeError
from .._tools import (
    DEBUG,
)
from .._tools._dataframe import (
    convert_dtypes,
)
from ..content import fundamental_and_reference
from ..content.fundamental_and_reference._data_grid_type import (
    get_data_grid_type_by_session,
)
from ..errors import RDError
from ..usage_collection._filter_types import FilterType
from ..usage_collection._logger import get_usage_logger
from ..usage_collection._utils import ModuleName

if TYPE_CHECKING:
    from logging import Logger


def get_log_string(fields, universe):
    return f"Fields: {fields} for {universe}"


def show_requests_in_log(logger: "Logger", response: "Response", universe, fields):
    request_messages = response.request_message
    statuses = response.http_status
    if not isinstance(response.request_message, list):
        request_messages = [response.request_message]
        statuses = [response.http_status]

    for request, status in zip(request_messages, statuses):
        path = request.url.path
        cur_universe = path.rsplit("/", 1)[-1]
        if cur_universe not in universe:
            cur_universe = universe
        logger.info(
            f"Request to {path} with {get_log_string(fields, cur_universe)}\n"
            f"status: {status}\n"
        )


def get_adc_data(
    params: dict, logger: "Logger", raise_if_error=False
) -> Tuple[dict, "DataFrame"]:
    fields = params.get("fields", "")
    universe = params["universe"]
    logger.info(f"Requesting {get_log_string(fields, universe)} \n")
    definition = fundamental_and_reference.Definition(**params)
    raw = {}
    df = DataFrame()
    try:
        response = definition.get_data()
        raw = response.data.raw
        df = response.data.df
    except ScopeError as e:
        if raise_if_error:
            raise e
        logger.error(str(e))
    except RDError as e:
        if raise_if_error:
            raise e
        logger.debug(f"Failure response into content layer: {str(e)}")
    except Exception as e:
        if DEBUG:
            raise e
        if raise_if_error:
            raise e
        logger.exception(f"Failure sending request with {definition}")
    else:
        show_requests_in_log(logger, response, universe, fields)
    return raw, df


def get_data_from_stream(universe, fields, logger):
    from . import Stream

    logger.info(f"Requesting pricing info for fields={fields} via websocket\n")
    stream = Stream(universe=universe, fields=fields)
    columns, data, df = None, None, DataFrame()

    try:
        stream.open(with_updates=False)
        columns, data = get_columns_and_data_from_stream(stream, fields)
        df = stream.get_snapshot(fields=fields)
        if len(df.columns) == 1 or not any([_stream.fields for _stream in stream]):
            df = DataFrame()
        else:
            df = convert_dtypes(df)
        stream.close()

    except Exception as e:
        logger.debug(f"Failure retrieving data for {stream._stream.universe}")

    return columns, data, df


def get_columns_from_stream(stream):
    columns = set()
    for _stream in stream:
        fields = _stream.fields or []
        columns.update(fields)
    return list(columns)


def get_columns_and_data_from_stream(stream, fields):
    stream_columns = get_columns_from_stream(stream)
    if fields:
        columns = [i for i in fields if i in stream_columns]
    else:
        columns = stream_columns
    data = {
        _stream.name: convert_types([_stream[column] for column in columns], columns)
        for _stream in stream
    }
    return columns, data


def update_universe(raw, _universe):
    index = 0  # instrument
    data = raw.get("data")
    if data and all(isinstance(i[index], str) for i in data):
        universe = [i[index] for i in data]
    else:
        universe = _universe
    return universe


def get_data(
    universe: Union[str, Iterable[str]],
    fields: Union[str, list, None] = None,
    parameters: Union[str, dict, None] = None,
    use_field_names_in_headers: bool = False,
) -> DataFrame:
    """
    With this tool you can request data from ADC, realtime pricing data or
    combination of both;

    Parameters
    ----------
    universe: str | list ,
        instruments to request.
    fields: str | list .
        fields to request.
    parameters: str | dict,
        Single global parameter key=value or dictionary
        of global parameters to request.
    use_field_names_in_headers: bool
        Return field name as column headers for data instead of title


    Returns
    -------
    pandas.DataFrame

    Examples
    --------
    >>> get_data(universe=['IBM.N', 'VOD.L'], fields=['BID', 'ASK'])
    >>> get_data(
    ...     universe=['GOOG.O', 'AAPL.O'],
    ...     fields=['TR.EV','TR.EVToSales'],
    ...     parameters = {'SDate': '0CY', 'Curn': 'CAD'}
    ...)
    """
    session = get_default()
    raise_if_closed(session)

    logger = session.logger()

    # Library usage logging
    get_usage_logger().log_func(
        name=f"{ModuleName.ACCESS}.get_data",
        func_path=f"{__name__}.get_data",
        kwargs=dict(
            universe=universe,
            fields=fields,
            parameters=parameters,
            use_field_names_in_headers=use_field_names_in_headers,
        ),
        desc={FilterType.SYNC, FilterType.LAYER_ACCESS},
    )

    universe = UniverseContainer(universe)
    fields = FieldsContainer(fields)
    data_grid_type = get_data_grid_type_by_session(session)
    adc = get_adc_context(data_grid_type, universe, fields)
    hp_and_cust_inst = get_hp_and_custinst_context(data_grid_type, universe, fields)

    adc_raw, adc_df = None, None
    if adc.can_get_data:
        adc_raw, adc_df = get_adc_data(
            params={
                "universe": universe.adc,
                "fields": fields.adc,
                "parameters": parameters,
                "use_field_names_in_headers": use_field_names_in_headers,
            },
            logger=logger,
        )

    adc_data = ADCDataContainer(adc_raw, adc_df, fields)
    universe.calc_hp(adc_raw)

    stream_columns, stream_data, stream_df = None, None, None
    if hp_and_cust_inst.can_get_data:
        stream_columns, stream_data, stream_df = get_data_from_stream(
            universe.hp_and_cust_inst, fields.hp, logger
        )

    hp_and_cust_inst_data = HPAndCustInstDataContainer(
        stream_columns, stream_data, stream_df
    )

    adc.set_data(adc_data, hp_and_cust_inst_data)
    hp_and_cust_inst.set_data(adc_data, hp_and_cust_inst_data)

    provider = DataProvider()
    return provider.get_df(
        adc,
        hp_and_cust_inst,
        adc_data,
        hp_and_cust_inst_data,
        use_field_names_in_headers,
    )
