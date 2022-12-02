from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.connection_definition_type import ConnectionDefinitionType
from emllib.dataclass.eml220.connection_type import ConnectionType
from emllib.dataclass.eml220.i18n_non_empty_string_type import I18NNonEmptyStringType
from emllib.dataclass.eml220.url_type import UrlType

__NAMESPACE__ = "https://eml.ecoinformatics.org/resource-2.2.0"


@dataclass
class OnlineType:
    online_description: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "onlineDescription",
            "type": "Element",
            "namespace": "",
        },
    )
    url: Optional[UrlType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection: Optional[ConnectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection_definition: Optional[ConnectionDefinitionType] = field(
        default=None,
        metadata={
            "name": "connectionDefinition",
            "type": "Element",
            "namespace": "",
        },
    )
