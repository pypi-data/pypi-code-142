# coding: utf-8
import enum
import re
import traceback
from collections.abc import Callable
from typing import TYPE_CHECKING, Optional

from ..._content_type import ContentType
from ..._tools import cached_property, make_enum_arg_parser
from ...delivery._stream import StreamStateEvent, StreamStateManager
from ...delivery._stream._stream_factory import create_rdp_stream

if TYPE_CHECKING:
    from ..._types import ExtendedParams, Strings, OptStr, OptStrStrs, OptCall
    from ..._core.session import Session
    from ...delivery._stream import _RDPStream

QUEUE_SIZE_PATTERN = re.compile(r"^queueSize=(?P<queue_size>[0-9]+)")


class Events(enum.Enum):
    """Events"""

    No = "None"
    Full = "Full"


class FinalizedOrders(enum.Enum):
    """Finalized order in cached"""

    No = "None"
    P1D = "P1D"


class UniverseTypes(enum.Enum):
    """Universe Types"""

    RIC = "RIC"
    Symbol = "Symbol"
    UserID = "UserID"


universe_type_arg_parser = make_enum_arg_parser(UniverseTypes, can_be_lower=True)
finalized_orders_arg_parser = make_enum_arg_parser(FinalizedOrders, can_be_lower=True)
events_arg_parser = make_enum_arg_parser(Events, can_be_lower=True)


class TradeDataStream(StreamStateManager):
    """
    Open a streaming trading analytics subscription.

    Parameters
    ----------
    universe: list
        a list of RIC or symbol or user's id for retrieving trading analytics data.

    fields: list
        a list of enumerate fields.
        Default: None

    universe_type: enum
        a type of given universe can be RIC, Symbol or UserID.
        Default: UniverseTypes.RIC

    finalized_orders: bool
        enable/disable the cached of finalized order of current day in the streaming.
        Default: False

    filters: list
        set the condition of subset of trading streaming data
        Default: None

    """

    def __init__(
        self,
        session: "Session",
        universe: "OptStrStrs" = None,
        universe_type: Optional["UniverseTypes"] = None,
        fields: "OptStrStrs" = None,
        events: Optional["Events"] = None,
        finalized_orders: Optional["FinalizedOrders"] = None,
        filters: "OptStrStrs" = None,
        api: "OptStr" = None,
        extended_params: "ExtendedParams" = None,
    ):
        self._session = session

        StreamStateManager.__init__(self, logger=self._session.logger())

        self._universe = universe
        self._universe_type = universe_type
        self._fields = fields
        self._event_details = events
        self._finalized_orders = finalized_orders
        self._filters = filters
        self._api = api
        self._extended_params = extended_params

        self.on_update: "OptCall" = None
        self.on_complete: "OptCall" = None
        self.on_add: "OptCall" = None
        self.on_remove: "OptCall" = None
        self.on_event: "OptCall" = None
        self.on_state: "OptCall" = None

        self._headers_ids: "Strings" = []

        self._is_completed: bool = False

    @property
    def session(self) -> "Session":
        return self._session

    @session.setter
    def session(self, session: "Session"):
        if self._session != session and not self.is_open:
            self._session = session
            StreamStateManager.init_logger(self, self._session.logger())
            self._stream.session = self._session

    @cached_property
    def _stream(self) -> "_RDPStream":
        parameters = {
            "universeType": self._universe_type,
            "events": self._event_details,
            "finalizedOrders": self._finalized_orders,
        }
        if self._filters is not None:
            parameters["filters"] = self._filters

        view = None
        if self._fields:
            view = self._fields.copy()

        content_type = ContentType.STREAMING_TRADING
        if self._api:
            content_type = ContentType.STREAMING_CUSTOM

        stream = create_rdp_stream(
            content_type=content_type,
            session=self._session,
            universe=self._universe,
            view=view,
            parameters=parameters,
            api=self._api,
            extended_params=self._extended_params,
        )
        stream.on_response(self._do_on_response)
        stream.on_update(self._do_on_update)
        stream.on(StreamStateEvent.CLOSED, self.close)
        return stream

    def _do_open(self, *args, **kwargs):
        self._debug(f"{self._classname} Open stream for {self._universe}")
        self._stream.open()

    def _do_close(self, *args, **kwargs):
        self._debug(f"{self._classname} Close stream for {self._universe}")
        self._stream.close()

    def _do_on_response(self, stream: "_RDPStream", message: dict):
        """
        Extract the response order summaries, order events and state

        Parameters
        ----------
        stream: _RDPStream
        message: dict
            {
                'streamID': '5',
                'type': 'Response',
                'headers': [
                            {'id': 'OrderKey', 'type': 'String'},
                            {'id': 'OrderTime', 'type': 'String', 'format': 'datetime'},
                            {'id': 'OrderStatus', 'type': 'String'},
                ],
                'state': {
                    'code': 200,
                    'status': 'Ok',
                    'stream': 'Open',
                    'message': 'queueSize=133'
                }
            }

        Returns
        -------
        None
        """
        self._headers_ids = [hdr["id"] for hdr in message.get("headers", [])]

        self._process_data(message)

        messages_data = message.get("messages", [])
        for datum in messages_data:
            self._callback(self.on_event, datum)

        self._process_state(message)

    def _do_on_update(self, stream: "_RDPStream", message: dict):
        """
        Extract the update (add/update/remove) order summaries and new order status.

        Parameters
        ----------
        stream: _RDPStream
        message: dict

        Returns
        -------
        None
        """
        self._process_data(message)

        update_data = message.get("update", [])
        for datum in update_data:
            self._callback(self.on_update, datum)

        removed_data = message.get("remove", [])
        for datum in removed_data:
            self._callback(self.on_remove, datum)

        messages_data = message.get("messages", [])
        for datum in messages_data:
            self._callback(self.on_event, datum)

        self._process_state(message)

    def _process_data(self, message: dict) -> None:
        data = message.get("data", [])
        for datum in data:
            self._callback(self.on_add, dict(zip(self._headers_ids, datum)))

    def _process_state(self, message: dict) -> None:
        state = message.get("state", {})

        if "message" in state:
            matched = QUEUE_SIZE_PATTERN.match(state["message"])

            if matched is not None:
                group = matched.groupdict()
                queue_size = group.get("queue_size", -1)
                queue_size = int(queue_size)

                if queue_size == 0 and not self._is_completed:
                    self._is_completed = True
                    self._callback(self.on_complete)

        if state:
            self._callback(self.on_state, state)

    def _callback(self, func: Callable, message: dict = None):
        if func:
            try:
                if message:
                    func(self, message)
                else:
                    func(self)
            except Exception as e:
                self._error(f"{self._classname} {func} callback raised exception:{e!r}")
                self._debug(f"{traceback.format_exc()}")
