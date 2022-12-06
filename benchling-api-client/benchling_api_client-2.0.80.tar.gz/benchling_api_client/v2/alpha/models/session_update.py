from typing import Any, cast, Dict, List, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.session_message_create import SessionMessageCreate
from ..models.session_update_status import SessionUpdateStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionUpdate")


@attr.s(auto_attribs=True, repr=False)
class SessionUpdate:
    """ Update a session to set its label (if null), or increase timeoutSeconds. """

    _session_messages: Union[Unset, List[SessionMessageCreate]] = UNSET
    _status: Union[Unset, SessionUpdateStatus] = UNSET
    _timeout_seconds: Union[Unset, int] = UNSET

    def __repr__(self):
        fields = []
        fields.append("session_messages={}".format(repr(self._session_messages)))
        fields.append("status={}".format(repr(self._status)))
        fields.append("timeout_seconds={}".format(repr(self._timeout_seconds)))
        return "SessionUpdate({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        session_messages: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._session_messages, Unset):
            session_messages = []
            for session_messages_item_data in self._session_messages:
                session_messages_item = session_messages_item_data.to_dict()

                session_messages.append(session_messages_item)

        status: Union[Unset, int] = UNSET
        if not isinstance(self._status, Unset):
            status = self._status.value

        timeout_seconds = self._timeout_seconds

        field_dict: Dict[str, Any] = {}
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if session_messages is not UNSET:
            field_dict["sessionMessages"] = session_messages
        if status is not UNSET:
            field_dict["status"] = status
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_session_messages() -> Union[Unset, List[SessionMessageCreate]]:
            session_messages = []
            _session_messages = d.pop("sessionMessages")
            for session_messages_item_data in _session_messages or []:
                session_messages_item = SessionMessageCreate.from_dict(
                    session_messages_item_data, strict=False
                )

                session_messages.append(session_messages_item)

            return session_messages

        try:
            session_messages = get_session_messages()
        except KeyError:
            if strict:
                raise
            session_messages = cast(Union[Unset, List[SessionMessageCreate]], UNSET)

        def get_status() -> Union[Unset, SessionUpdateStatus]:
            status = UNSET
            _status = d.pop("status")
            if _status is not None and _status is not UNSET:
                try:
                    status = SessionUpdateStatus(_status)
                except ValueError:
                    status = SessionUpdateStatus.of_unknown(_status)

            return status

        try:
            status = get_status()
        except KeyError:
            if strict:
                raise
            status = cast(Union[Unset, SessionUpdateStatus], UNSET)

        def get_timeout_seconds() -> Union[Unset, int]:
            timeout_seconds = d.pop("timeoutSeconds")
            return timeout_seconds

        try:
            timeout_seconds = get_timeout_seconds()
        except KeyError:
            if strict:
                raise
            timeout_seconds = cast(Union[Unset, int], UNSET)

        session_update = cls(
            session_messages=session_messages,
            status=status,
            timeout_seconds=timeout_seconds,
        )

        return session_update

    @property
    def session_messages(self) -> List[SessionMessageCreate]:
        """An array of `SessionMessage` describing the current session state."""
        if isinstance(self._session_messages, Unset):
            raise NotPresentError(self, "session_messages")
        return self._session_messages

    @session_messages.setter
    def session_messages(self, value: List[SessionMessageCreate]) -> None:
        self._session_messages = value

    @session_messages.deleter
    def session_messages(self) -> None:
        self._session_messages = UNSET

    @property
    def status(self) -> SessionUpdateStatus:
        """ Values that can be specified when updating the status of a Session """
        if isinstance(self._status, Unset):
            raise NotPresentError(self, "status")
        return self._status

    @status.setter
    def status(self, value: SessionUpdateStatus) -> None:
        self._status = value

    @status.deleter
    def status(self) -> None:
        self._status = UNSET

    @property
    def timeout_seconds(self) -> int:
        """Timeout in seconds, a value between 1 second and 30 days. Once set, it can only be increased, not decreased."""
        if isinstance(self._timeout_seconds, Unset):
            raise NotPresentError(self, "timeout_seconds")
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, value: int) -> None:
        self._timeout_seconds = value

    @timeout_seconds.deleter
    def timeout_seconds(self) -> None:
        self._timeout_seconds = UNSET
