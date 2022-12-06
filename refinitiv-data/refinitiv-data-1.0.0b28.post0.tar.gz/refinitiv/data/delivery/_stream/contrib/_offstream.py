from typing import Union, Optional, Callable, TYPE_CHECKING

from ._type import contrib_type_enum_arg_parser
from ..stream_connection import LOGIN_STREAM_ID
from ..._stream import _OMMStream
from ...._tools import cached_property, OrEvent

if TYPE_CHECKING:
    from ._type import ContribType
    from .._stream_factory import StreamDetails
    from ...._core.session import Session


class _OffStreamContrib(_OMMStream):
    def __init__(
        self,
        post_id: int,
        session: "Session",
        name: str,
        details: "StreamDetails",
        service: str,
        domain: str,
        on_ack: Optional[Callable] = None,
        on_error: Optional[Callable] = None,
    ) -> None:
        super().__init__(
            stream_id=post_id,
            session=session,
            name=name,
            details=details,
            domain=domain,
            service=service,
            on_error=on_error,
            on_ack=on_ack,
        )
        self._post_id = post_id

    @cached_property
    def _contributed(self) -> OrEvent:
        return OrEvent(self._error_event, self._ack_event)

    def get_next_post_id(self) -> int:
        return self.post_id

    def get_contrib_message(
        self, fields: dict, contrib_type: Union[str, "ContribType", None]
    ) -> dict:
        return {
            "Ack": True,
            "ID": LOGIN_STREAM_ID,
            "Message": {
                "Fields": fields,
                "ID": 0,
                "Type": contrib_type_enum_arg_parser.get_str(
                    contrib_type if contrib_type else "Update"
                ),
                "Domain": self.domain,
            },
            "PostID": self.post_id,
            "Type": "Post",
            "Key": {"Name": self.name, "Service": self.service},
            "Domain": self.domain,
        }

    def _do_open(self, *args, **kwargs):
        self._initialize_cxn()
        self._cxn.on(self._event.ack_by_id, self._on_stream_ack)
        self._cxn.on(self._event.error_by_id, self._on_stream_error)

    def _do_close(self, *args, **kwargs):
        self._dispose()

    def _dispose(self):
        self._debug(f"{self._classname} disposing [d]")
        self._cxn.remove_listener(self._event.error_by_id, self._on_stream_error)
        self._cxn.remove_listener(self._event.ack_by_id, self._on_stream_ack)
        self._release_cxn()
        self._debug(f"{self._classname} disposed [D]")
