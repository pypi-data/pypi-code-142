from typing import Any, cast, Dict, List, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.session_message_create import SessionMessageCreate
from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionCreate")


@attr.s(auto_attribs=True, repr=False)
class SessionCreate:
    """  """

    _app_id: str
    _label: str
    _timeout_seconds: int
    _session_messages: Union[Unset, List[SessionMessageCreate]] = UNSET

    def __repr__(self):
        fields = []
        fields.append("app_id={}".format(repr(self._app_id)))
        fields.append("label={}".format(repr(self._label)))
        fields.append("timeout_seconds={}".format(repr(self._timeout_seconds)))
        fields.append("session_messages={}".format(repr(self._session_messages)))
        return "SessionCreate({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        app_id = self._app_id
        label = self._label
        timeout_seconds = self._timeout_seconds
        session_messages: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._session_messages, Unset):
            session_messages = []
            for session_messages_item_data in self._session_messages:
                session_messages_item = session_messages_item_data.to_dict()

                session_messages.append(session_messages_item)

        field_dict: Dict[str, Any] = {}
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if label is not UNSET:
            field_dict["label"] = label
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if session_messages is not UNSET:
            field_dict["sessionMessages"] = session_messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_app_id() -> str:
            app_id = d.pop("appId")
            return app_id

        try:
            app_id = get_app_id()
        except KeyError:
            if strict:
                raise
            app_id = cast(str, UNSET)

        def get_label() -> str:
            label = d.pop("label")
            return label

        try:
            label = get_label()
        except KeyError:
            if strict:
                raise
            label = cast(str, UNSET)

        def get_timeout_seconds() -> int:
            timeout_seconds = d.pop("timeoutSeconds")
            return timeout_seconds

        try:
            timeout_seconds = get_timeout_seconds()
        except KeyError:
            if strict:
                raise
            timeout_seconds = cast(int, UNSET)

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

        session_create = cls(
            app_id=app_id,
            label=label,
            timeout_seconds=timeout_seconds,
            session_messages=session_messages,
        )

        return session_create

    @property
    def app_id(self) -> str:
        if isinstance(self._app_id, Unset):
            raise NotPresentError(self, "app_id")
        return self._app_id

    @app_id.setter
    def app_id(self, value: str) -> None:
        self._app_id = value

    @property
    def label(self) -> str:
        """The name of the session. Length must be between 3-100 chars. Label must be set to a string if it's currently null. It becomes immutable once a value is set."""
        if isinstance(self._label, Unset):
            raise NotPresentError(self, "label")
        return self._label

    @label.setter
    def label(self, value: str) -> None:
        self._label = value

    @property
    def timeout_seconds(self) -> int:
        """Timeout in seconds, a value between 1 second and 30 days. Once set, it can only be increased, not decreased."""
        if isinstance(self._timeout_seconds, Unset):
            raise NotPresentError(self, "timeout_seconds")
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, value: int) -> None:
        self._timeout_seconds = value

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
