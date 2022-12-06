# coding: utf-8
import asyncio
import json
import os
import socket
from functools import partial
from threading import Event
from typing import Callable, Optional, TYPE_CHECKING, Any, Union

from ._protocol_type import ProtocolType
from ._stream_listener import OMMStreamListener, StreamEvent
from .contrib import ContribResponse
from .contrib import contrib_type_enum_arg_parser
from .stream import (
    Stream,
    update_message_with_extended_params,
)
from ..._tools import cached_property, OrEvent

if TYPE_CHECKING:
    from .contrib import ContribType
    from ..._types import OptStr, ExtendedParams, Strings
    from ._stream_factory import StreamDetails
    from . import StreamConnection
    from ..._core.session import Session


class _OMMStream(Stream, OMMStreamListener["_OMMStream"]):
    def __init__(
        self,
        stream_id: int,
        session: "Session",
        name: str,
        details: "StreamDetails",
        domain: "OptStr" = "MarketPrice",
        service: "OptStr" = None,
        fields: Optional["Strings"] = None,
        key: Optional[dict] = None,
        extended_params: "ExtendedParams" = None,
        on_refresh: Optional[Callable] = None,
        on_status: Optional[Callable] = None,
        on_update: Optional[Callable] = None,
        on_complete: Optional[Callable] = None,
        on_error: Optional[Callable] = None,
        on_ack: Optional[Callable] = None,
    ) -> None:
        Stream.__init__(self, stream_id, session, details)
        OMMStreamListener.__init__(
            self,
            logger=session.logger(),
            on_refresh=on_refresh,
            on_status=on_status,
            on_update=on_update,
            on_complete=on_complete,
            on_error=on_error,
            on_ack=on_ack,
        )
        self._name = name
        self._service = service
        self._fields = fields or []
        self._domain = domain
        self._key = key
        self._extended_params = extended_params

        self._with_updates: bool = True
        self._refresh_message = None
        self._status_message = None
        self._error_message = None
        self._ack_message = None

        self._error_event = Event()
        self._ack_event = Event()
        self._update_event = Event()

        self._contrib_message = None
        self._is_contributing = False
        self._post_id = None
        self._post_user_info = None

    @cached_property
    def _contributed(self) -> OrEvent:
        return OrEvent(self._error_event, self._update_event)

    @property
    def post_id(self) -> int:
        return self._post_id

    def get_next_post_id(self) -> int:
        return next(self.session._contrib_post_id_counter)

    @property
    def post_user_info(self) -> dict:
        return self._post_user_info

    @property
    def name(self) -> str:
        return self._name

    @property
    def protocol_type(self) -> ProtocolType:
        return ProtocolType.OMM

    @property
    def domain(self) -> str:
        return self._domain

    @property
    def stream_state(self) -> str:
        return self._stream_state

    @property
    def message_state(self) -> str:
        return self._message_state

    @property
    def service(self):
        return self._service

    @property
    def is_contributing(self):
        return self._is_contributing

    @property
    def open_message(self):
        msg = {
            "ID": self.id,
            "Domain": self._domain,
            "Streaming": self._with_updates,
            "Key": {},
        }

        if self._key:
            msg["Key"] = self._key

        msg["Key"]["Name"] = self.name

        if self.service:
            msg["Key"]["Service"] = self.service

        if self._fields:
            msg["View"] = self._fields

        if self._extended_params:
            msg = update_message_with_extended_params(msg, self._extended_params)

        return msg

    @cached_property
    def close_message(self):
        return {"ID": self.id, "Type": "Close"}

    def _do_open(self, *args, **kwargs):
        self._with_updates = kwargs.get("with_updates", True)
        self._initialize_cxn()
        self._cxn.on(self._event.refresh_by_id, self._on_stream_refresh)
        self._cxn.on(self._event.update_by_id, self._on_stream_update)
        self._cxn.on(self._event.status_by_id, self._on_stream_status)
        self._cxn.on(self._event.complete_by_id, self._on_stream_complete)
        self._cxn.on(self._event.error_by_id, self._on_stream_error)
        self._cxn.on(self._event.ack_by_id, self._on_stream_ack)
        super()._do_open(*args, **kwargs)

    def _dispose(self):
        self._debug(f"{self._classname} disposing [d]")
        self._cxn.remove_listener(self._event.refresh_by_id, self._on_stream_refresh)
        self._cxn.remove_listener(self._event.update_by_id, self._on_stream_update)
        self._cxn.remove_listener(self._event.status_by_id, self._on_stream_status)
        self._cxn.remove_listener(self._event.complete_by_id, self._on_stream_complete)
        self._cxn.remove_listener(self._event.error_by_id, self._on_stream_error)
        self._cxn.remove_listener(self._event.ack_by_id, self._on_stream_ack)
        self._release_cxn()
        self._debug(f"{self._classname} disposed [D]")

    def _do_on_stream_refresh(self, cxn: "StreamConnection", message: dict, *_) -> Any:
        self._refresh_message = message
        message_state = message.get("State", {})
        self._stream_state = message_state.get("Stream", "")
        self._message_state = message_state.get("Text", "")
        return message

    def _on_stream_update(self, originator, *args) -> None:
        self._propagate_event(StreamEvent.UPDATE, originator, *args)

        if self.is_contributing:
            self._update_event.set()

    def _on_stream_status(self, originator, *args) -> None:
        self._propagate_event(StreamEvent.STATUS, originator, *args)

        if self.is_open:
            self.dispatch_complete(originator, *args)

    def _do_on_stream_status(self, cxn: "StreamConnection", message: dict, *_) -> Any:
        self._status_message = message
        message_state = message.get("State", {})
        stream_state = message_state.get("Stream", "")
        self._stream_state = stream_state
        self._message_state = message_state.get("Text", "")

        if stream_state == "Closed":
            self._debug(
                f"{self._classname} received a closing message, "
                f"message_state={message_state}, state={self.state}"
            )

            if self.is_opening:
                self._opened.set()

        return message

    def _on_stream_complete(self, originator, *args) -> None:
        self._propagate_event(StreamEvent.COMPLETE, originator, *args)

        if self.is_opening:
            self._opened.set()

    def _do_on_stream_error(
        self, originator: "StreamConnection", message: dict, *args
    ) -> Any:
        self._error_message = message

        if self.is_contributing:
            if message.get("Type") == "Error":
                debug_message = message.get("Debug", {}).get("Message")
                if debug_message:
                    try:
                        debug_dict = json.loads(debug_message)
                        if debug_dict.get("PostID"):
                            self._contrib_message = message
                    except json.decoder.JSONDecodeError:
                        self._error(
                            f"Cannot decode Debug message as JSON: {debug_message}"
                        )

            self._error_event.set()
            return (message, *args)

        else:
            return super()._do_on_stream_error(originator, message, *args)

    def _do_on_stream_ack(
        self, originator: "StreamConnection", message: dict, *args
    ) -> Any:
        self._ack_message = message

        if self.is_contributing:
            self._contrib_message = message
            ack_id = message.get("AckID")
            nack_code = message.get("NakCode")

            if ack_id != self.post_id:
                # Received Ack message with wrong ack_id
                self._error(
                    f"{self._classname} Received Ack message "
                    f"with wrong ack_id={ack_id} != post_id={self.post_id}"
                )
            else:
                if nack_code:
                    reason = message.get("Text")
                    self._error(
                        f"{self._classname} received Nack message, "
                        f"ackID={ack_id}, NackCode={nack_code}, reason={reason}"
                    )

                else:
                    self._debug(
                        f"{self._classname} received Ack message, "
                        f"ackID={ack_id}, state={self.state}"
                    )

            self._ack_event.set()
            return (message, *args)

        else:
            return super()._do_on_stream_ack(originator, message, *args)

    def send_open_message(self):
        self.send(self.open_message)

    def get_contrib_message(
        self, fields: dict, contrib_type: Union[str, "ContribType", None]
    ) -> dict:
        message = {
            "Ack": True,
            "ID": self.id,
            "Message": {
                "Fields": fields,
                "ID": self.id,
                "Type": contrib_type_enum_arg_parser.get_str(
                    contrib_type if contrib_type else "Update"
                ),
                "Domain": self.domain,
            },
            "PostID": self.post_id,
            "Type": "Post",
            "Domain": self.domain,
        }

        post_user_info = self._post_user_info
        if not post_user_info:
            hostname = socket.gethostname()
            ip_addr = socket.gethostbyname(hostname)
            post_user_info = {"Address": ip_addr, "UserID": os.getpid()}

        message["PostUserInfo"] = post_user_info

        return message

    def contribute(
        self,
        fields: dict,
        contrib_type: Union[str, "ContribType", None] = None,
        post_user_info: Optional[dict] = None,
    ) -> ContribResponse:
        self._is_contributing = True
        self._post_id = self.get_next_post_id()
        self._post_user_info = post_user_info

        self._error_event.clear()
        self._ack_event.clear()
        self._update_event.clear()

        sent = self.send(self.get_contrib_message(fields, contrib_type))

        if sent:
            self._contributed.wait()
            response = ContribResponse(self._contrib_message)

        else:
            response = ContribResponse({})

        self._is_contributing = False
        return response

    async def contribute_async(
        self,
        fields: dict,
        contrib_type: Union[str, "ContribType", None] = None,
        post_user_info: Optional[dict] = None,
    ) -> ContribResponse:
        return await asyncio.get_event_loop().run_in_executor(
            None, partial(self.contribute, fields, contrib_type, post_user_info)
        )
