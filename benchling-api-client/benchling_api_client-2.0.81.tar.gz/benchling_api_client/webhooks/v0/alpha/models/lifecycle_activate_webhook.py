from typing import Any, cast, Dict, List, Type, TypeVar

import attr

from ..extensions import NotPresentError
from ..types import UNSET, Unset

T = TypeVar("T", bound="LifecycleActivateWebhook")


@attr.s(auto_attribs=True, repr=False)
class LifecycleActivateWebhook:
    """ Sent when a user initiates app activation on a tenant """

    _client_id: str
    _client_secret: str
    _deprecated: bool
    _excluded_properties: List[str]
    _type: str

    def __repr__(self):
        fields = []
        fields.append("client_id={}".format(repr(self._client_id)))
        fields.append("client_secret={}".format(repr(self._client_secret)))
        fields.append("deprecated={}".format(repr(self._deprecated)))
        fields.append("excluded_properties={}".format(repr(self._excluded_properties)))
        fields.append("type={}".format(repr(self._type)))
        return "LifecycleActivateWebhook({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        client_id = self._client_id
        client_secret = self._client_secret
        deprecated = self._deprecated
        excluded_properties = self._excluded_properties

        type = self._type

        field_dict: Dict[str, Any] = {}
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if excluded_properties is not UNSET:
            field_dict["excludedProperties"] = excluded_properties
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_client_id() -> str:
            client_id = d.pop("clientId")
            return client_id

        try:
            client_id = get_client_id()
        except KeyError:
            if strict:
                raise
            client_id = cast(str, UNSET)

        def get_client_secret() -> str:
            client_secret = d.pop("clientSecret")
            return client_secret

        try:
            client_secret = get_client_secret()
        except KeyError:
            if strict:
                raise
            client_secret = cast(str, UNSET)

        def get_deprecated() -> bool:
            deprecated = d.pop("deprecated")
            return deprecated

        try:
            deprecated = get_deprecated()
        except KeyError:
            if strict:
                raise
            deprecated = cast(bool, UNSET)

        def get_excluded_properties() -> List[str]:
            excluded_properties = cast(List[str], d.pop("excludedProperties"))

            return excluded_properties

        try:
            excluded_properties = get_excluded_properties()
        except KeyError:
            if strict:
                raise
            excluded_properties = cast(List[str], UNSET)

        def get_type() -> str:
            type = d.pop("type")
            return type

        try:
            type = get_type()
        except KeyError:
            if strict:
                raise
            type = cast(str, UNSET)

        lifecycle_activate_webhook = cls(
            client_id=client_id,
            client_secret=client_secret,
            deprecated=deprecated,
            excluded_properties=excluded_properties,
            type=type,
        )

        return lifecycle_activate_webhook

    @property
    def client_id(self) -> str:
        if isinstance(self._client_id, Unset):
            raise NotPresentError(self, "client_id")
        return self._client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        self._client_id = value

    @property
    def client_secret(self) -> str:
        if isinstance(self._client_secret, Unset):
            raise NotPresentError(self, "client_secret")
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value: str) -> None:
        self._client_secret = value

    @property
    def deprecated(self) -> bool:
        if isinstance(self._deprecated, Unset):
            raise NotPresentError(self, "deprecated")
        return self._deprecated

    @deprecated.setter
    def deprecated(self, value: bool) -> None:
        self._deprecated = value

    @property
    def excluded_properties(self) -> List[str]:
        """These properties have been dropped from the payload due to size."""
        if isinstance(self._excluded_properties, Unset):
            raise NotPresentError(self, "excluded_properties")
        return self._excluded_properties

    @excluded_properties.setter
    def excluded_properties(self, value: List[str]) -> None:
        self._excluded_properties = value

    @property
    def type(self) -> str:
        if isinstance(self._type, Unset):
            raise NotPresentError(self, "type")
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        self._type = value
