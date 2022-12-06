from enum import Enum, unique
from typing import Optional, Union

from ..._tools import make_convert_to_enum, EnumArgsParser, make_parse_enum


@unique
class AssetState(Enum):
    """
    Asset state values for 'filter' parameter in request for SymbolConversion content object.
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"


OptAssetState = Optional[Union[str, AssetState]]

asset_state_enum_arg_parser = EnumArgsParser(
    parse=make_parse_enum(AssetState), parse_to_enum=make_convert_to_enum(AssetState)
)
