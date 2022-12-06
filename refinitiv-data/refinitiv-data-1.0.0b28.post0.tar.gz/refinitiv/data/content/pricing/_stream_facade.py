from typing import TYPE_CHECKING, Any, Callable, List, Optional, Union

from ..._content_type import ContentType
from ..._core.session import get_valid_session
from ..._tools import (
    PRICING_DATETIME_PATTERN,
    cached_property,
    create_repr,
    make_callback,
)
from ..._tools._dataframe import convert_df_columns_to_datetime_re
from ..._types import OptBool, OptStr, Strings
from ...delivery._stream.base_stream import StreamOpenWithUpdatesMixin
from .._universe_streams import UniverseStreamFacade, _UniverseStreams

if TYPE_CHECKING:
    import pandas

    from ... import OpenState
    from ..._core.session import Session
    from ...delivery.omm_stream import ContribResponse, ContribType


class PricingStream(UniverseStreamFacade):
    pass


class Stream(StreamOpenWithUpdatesMixin):
    """
    Summary line of this class are used for requesting, processing and managing a set of
    streaming level 1 (MarketPrice domain) quotes and trades

    Extended description of this class:
        The object automatically manages a set of streaming caches available for access
        at any time. Your application can then reach into this cache and pull out
        real-time fields by just calling a simple access method.
        The object also emits a number of different events, your application can
        listen to in order to be notified of the latest field values in real-times.
        The object iterable.

    Parameters
    ----------
    session : Session, optional
        Means default session would be used
    universe : str or list of str, optional
        The single/multiple instrument/s name (e.g. "EUR=" or ["EUR=", "CAD=", "UAH="])
    fields : list, optional
        Specifies the specific fields to be delivered when messages arrive
    service : str, optional
        Name of the streaming service publishing the instruments
    api: str, optional
        Specifies the data source. It can be updated/added using config file
    extended_params : dict, optional
        If necessary other parameters

    Examples
    --------
    >>> from refinitiv.data.content import pricing
    >>> definition = pricing.Definition("EUR=")
    >>> stream = definition.get_stream()
    """

    def __init__(
        self,
        session: "Session" = None,
        universe: Union[str, List[str]] = None,
        fields: Optional[list] = None,
        service: OptStr = None,
        api: OptStr = None,
        extended_params: Optional[dict] = None,
    ) -> None:
        self._session = get_valid_session(session)
        self._always_use_default_session = session is None
        self._universe = universe or []
        self._fields = fields
        self._service = service
        self._api = api
        self._extended_params = extended_params

    @cached_property
    def _stream(self) -> _UniverseStreams:
        if self._api:
            content_type = ContentType.STREAMING_CUSTOM
        else:
            content_type = ContentType.STREAMING_PRICING

        return _UniverseStreams(
            content_type=content_type,
            item_facade_class=PricingStream,
            universe=self._universe,
            session=self._session,
            fields=self._fields,
            service=self._service,
            api=self._api,
            extended_params=self._extended_params,
        )

    def open(self, with_updates: bool = True) -> "OpenState":
        """
        Summary line of this func open the Pricing connection by sending corresponding
        requests for all requested instruments

        Extended description of this class:
             It will be opened once all the requested instruments are received
             either on_refresh, on_status or other method.
             Then the pricing.Stream can be used in order to retrieve data.

        Parameters
        ----------
        with_updates : bool, optional
            actions:
                True - the streaming will work as usual and the data will be received
                continuously.
                False - only one data snapshot will be received
                (single Refresh 'NonStreaming') and stream will be closed automatically.

            Default: True

        Returns
        -------
        OpenState

        Examples
        --------
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition("EUR=")
        >>> stream = definition.get_stream()
        >>> stream.open()
        """
        return super().open(with_updates=with_updates)

    def close(self) -> "OpenState":
        """
        Summary line of this func closes the pricing connection, releases resources

        Returns
        -------
        OpenState

        Examples
        --------
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition("EUR=")
        >>> stream = definition.get_stream()
        >>> stream.open()
        >>> stream.close()
        """
        return super().close()

    def _get_fields(self, universe: str, fields: Optional[list] = None) -> dict:
        """
        Returns a dict of the fields for a requested universe.

        Parameters
        ----------
        universe: str
            Name of the instrument (e.g. 'EUR=' ...).
        fields: list, optional
            The fields that are listed in the `fields` parameter.

        Returns
        -------
        dict

        Examples
        --------
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition(["AIRP.PA", "AIR.PA", "ALSO.PA"])
        >>> stream = definition.get_stream()
        >>> fields
        ... {'AIRP.PA': {'BID': 147.14, 'ASK': 147.16}}
        """
        _fields = {
            universe: {
                key: value
                for key, value in self._stream[universe].items()
                if fields is None or key in fields
            }
        }
        return _fields

    def get_snapshot(
        self,
        universe: Optional[Union[str, Strings]] = None,
        fields: Optional[Union[str, Strings]] = None,
        convert: OptBool = True,
    ) -> "pandas.DataFrame":
        """
        Returns a Dataframe filled with snapshot values for a list of instrument names
        and a list of fields.

        Parameters
        ----------
        universe: str, list of str, optional
            List of instruments to request snapshot data on.

        fields: str, list of str, optional
            List of fields to request.

        convert: bool, optional
            If True, force numeric conversion for all values.
            By default True.

        Returns
        -------
            pandas.DataFrame

            pandas.DataFrame content:
                - columns : instrument and fieled names
                - rows : instrument name and field values

        Raises
        ------
            Exception
                If request fails or if server returns an error

            ValueError
                If a parameter type or value is wrong

        Examples
        --------
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition(
        ...    ["MSFT.O", "GOOG.O", "IBM.N"],
        ...    fields=["BID", "ASK", "OPEN_PRC"]
        ...)
        >>> stream = definition.get_stream()
        >>> data = stream.get_snapshot(["MSFT.O", "GOOG.O"], ["BID", "ASK"])
        >>> data
        ... "      Instrument   BID         ASK      "
        ... "0     MSFT.O        150.9000   150.9500 "
        ... "1     GOOG.O        1323.9000  1327.7900"
        """
        df = self._stream.get_snapshot(
            universe=universe, fields=fields, convert=convert
        )
        convert_df_columns_to_datetime_re(df, PRICING_DATETIME_PATTERN)
        return df

    def on_refresh(self, func: Callable[[Any, str, "Stream"], Any]) -> "Stream":
        """
        Called when a stream on instrument_name was opened successfully or when the
        stream is refreshed by the server
        This callback is called with the reference to the steam object, the instrument
        name and the instrument full image

        Parameters
        ----------
        func : Callable
            Callable object to process retrieved data

        Returns
        -------
        current instance

        Examples
        --------
        >>> import datetime
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition("EUR=")
        >>> stream = definition.get_stream()
        >>> def on_refresh(message, ric, stream):
        ...    current_time = datetime.datetime.now().time()
        ...    print("\t{} | Receive refresh [{}] : {}".format(current_time, ric, message))  # noqa
        >>> stream.on_refresh(on_refresh)
        >>> stream.open()
        """
        self._stream.on_refresh(make_callback(func))
        return self

    def on_update(self, func: Callable[[Any, str, "Stream"], Any]) -> "Stream":
        """
        Called when an update is received for a instrument_name
        This callback is called with the reference to the stream object, the instrument
        name and the instrument update

        Parameters
        ----------
        func : Callable
            Callable object to process retrieved data

        Returns
        -------
        current instance

        Examples
        --------
        >>> import datetime
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition("EUR=")
        >>> stream = definition.get_stream()
        >>> def on_update(update, ric, stream):
        ...     current_time = datetime.datetime.now().time()
        ...     print("\t{} | Receive update [{}] : {}".format(current_time, ric, update))  # noqa
        >>> stream.on_update(on_update)
        >>> stream.open()
        """
        self._stream.on_update(make_callback(func))
        return self

    def on_status(self, func: Callable[[Any, str, "Stream"], Any]) -> "Stream":
        """
        Called when a status is received for a instrument_name
        This callback is called with the reference to the stream object, the instrument
        name and the instrument status

        Parameters
        ----------
        func : Callable
            Callable object to process retrieved data

        Returns
        -------
        current instance

        Examples
        --------
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition("EUR=")
        >>> stream = definition.get_stream()
        >>> def on_status(status, ric, stream):
        ...     print("\tReceive status [{}] : {}".format(ric, status))
        >>> stream.on_status(on_status)
        >>> stream.open()
        """
        self._stream.on_status(make_callback(func))
        return self

    def on_complete(self, func: Callable[["Stream"], Any]) -> "Stream":
        """
        Called when all subscriptions are completed
        This callback is called with the reference to the stream object

        Parameters
        ----------
        func : Callable
            Callable object to process retrieved data

        Returns
        -------
        current instance

        Examples
        --------
        >>> import datetime
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition("EUR=")
        >>> stream = definition.get_stream()
        >>> def on_complete(stream):
        ...    current_time = datetime.datetime.now().time()
        ...    print("\t{} | Receive complete".format(current_time))
        >>> stream.on_complete(on_complete)
        >>> stream.open()
        """
        self._stream.on_complete(func)
        return self

    def on_error(self, func: Callable) -> "Stream":
        self._stream.on_error(make_callback(func))
        return self

    def on_ack(self, func: Callable) -> "Stream":
        """
        This function called when the stream received an ack message after sending a contribution.

        Parameters
        ----------
        func : Callable, optional
             Callable object to process retrieved ack data

        Returns
        -------
        Stream
            current instance

        Examples
        --------
        Prerequisite: The default session must be opened.
        >>> from refinitiv.data.content import pricing
        >>>
        >>> definition = pricing.Definition("EUR=")
        >>> stream = definition.get_stream()
        >>> def on_ack(ack_msg, ric, stream):
        ...     print(f"\tReceive ack [{ric}] : {ack_msg}")
        >>> stream.on_ack(on_ack)
        >>> stream.open()
        >>> result = stream.contribute("EUR=", {"BID": 1.12})
        """
        self._stream.on_ack(make_callback(func))
        return self

    def contribute(
        self,
        name: str,
        fields: dict,
        contrib_type: Union[str, "ContribType", None] = None,
        post_user_info: Optional[dict] = None,
    ) -> "ContribResponse":
        """
        Function to send OnStream contribution request.

        Parameters
        ----------
        name: string
            RIC to contribute to.

        fields: dict{field:value}
            Specify fields and values to contribute.

        contrib_type: Union[str, ContribType], optional
            Define the contribution type.
            Default: "Update"

        post_user_info: dict, optional
            PostUserInfo object represents information about the posting user.
                Address: string, required
                    Dotted-decimal string representing the IP Address of the posting user.
                UserID: int, required
                    Specifies the ID of the posting user

        Returns
        -------
        ContribResponse

        Examples
        --------
        >>> import refinitiv.data as rd
        >>>
        >>> pricing_stream = rd.content.pricing.Definition(
        ...    ["MSFT.O", "GOOG.O", "IBM.N"],
        ...    fields=["BID", "ASK", "OPEN_PRC"]
        ...).get_stream()
        >>> response = pricing_stream.contribute("MSFT.O", {"BID": 240.83})
        """
        return self._stream.contribute(name, fields, contrib_type, post_user_info)

    async def contribute_async(
        self,
        name: str,
        fields: dict,
        contrib_type: Union[str, "ContribType", None] = None,
        post_user_info: Optional[dict] = None,
    ) -> "ContribResponse":
        """
        Function to send asynchronous OnStream contribution request.

        Parameters
        ----------
        name: string
            RIC to contribute to.

        fields: dict{field:value}
            Specify fields and values to contribute.

        contrib_type: Union[str, ContribType], optional
            Define the contribution type.
            Default: "Update"

        post_user_info: dict, optional
            PostUserInfo object represents information about the posting user.
                Address: string, required
                    Dotted-decimal string representing the IP Address of the posting user.
                UserID: int, required
                    Specifies the ID of the posting user

        Returns
        -------
        ContribResponse

        Examples
        --------
        >>> import refinitiv.data as rd
        >>>
        >>> pricing_stream = rd.content.pricing.Definition(
        ...    ["MSFT.O", "GOOG.O", "IBM.N"],
        ...    fields=["BID", "ASK", "OPEN_PRC"]
        ...).get_stream()
        >>> response = await pricing_stream.contribute_async("MSFT.O", {"BID": 240.83})
        """
        return await self._stream.contribute_async(
            name, fields, contrib_type, post_user_info
        )

    def add_instruments(self, instruments) -> None:
        """
        Add instruments to the stream universe.

        Parameters
        ----------
        instruments: str, list of str, optional
            List of instruments to add.

        Examples
        --------
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition(
        ...    ["MSFT.O", "GOOG.O", "IBM.N"],
        ...)
        >>> stream = definition.get_stream()
        >>> stream.add_instruments("VOD.L")
        """
        self._stream.add_instruments(instruments)

    def remove_instruments(self, instruments) -> None:
        """
        Remove instruments from the stream universe.

        Parameters
        ----------
        instruments: str, list of str, optional
            List of instruments to remove.

        Examples
        --------
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition(
        ...    ["MSFT.O", "GOOG.O", "IBM.N"],
        ...)
        >>> stream = definition.get_stream()
        >>> stream.remove_instruments("GOOG.O")
        """
        self._stream.remove_instruments(instruments)

    def add_fields(self, fields) -> None:
        """
        Add fields to the fields list.

        Parameters
        ----------
        fields: str, list of str, optional
            List of fields to add.

        Examples
        --------
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition(
        ...    ["MSFT.O", "GOOG.O", "IBM.N"],
        ...    fields=["BID", "ASK", "OPEN_PRC"]
        ...)
        >>> stream = definition.get_stream()
        >>> stream.add_fields("TRDPRC_1")
        """
        self._stream.add_fields(fields)

    def remove_fields(self, fields) -> None:
        """
        Remove fields from the fields list.

        Parameters
        ----------
        fields: str, list of str, optional
            List of fields to remove.

        Examples
        --------
        >>> from refinitiv.data.content import pricing
        >>> definition = pricing.Definition(
        ...    ["MSFT.O", "GOOG.O", "IBM.N"],
        ...    fields=["BID", "ASK", "OPEN_PRC"]
        ...)
        >>> stream = definition.get_stream()
        >>> stream.remove_fields("ASK")
        """
        self._stream.remove_fields(fields)

    def __iter__(self):
        return self._stream.__iter__()

    def __getitem__(self, item) -> "PricingStream":
        return self._stream.__getitem__(item)

    def __len__(self) -> int:
        return self._stream.__len__()

    def __repr__(self):
        return create_repr(
            self,
            class_name=self.__class__.__name__,
            content=f"{{name='{self._universe}'}}",
        )
