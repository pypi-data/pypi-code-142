from dataclasses import dataclass, field

from emllib.dataclass.eml220.function_type import FunctionType

__NAMESPACE__ = "https://eml.ecoinformatics.org/resource-2.2.0"


@dataclass
class UrlType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    function: FunctionType = field(
        default=FunctionType.DOWNLOAD,
        metadata={
            "type": "Attribute",
        },
    )
