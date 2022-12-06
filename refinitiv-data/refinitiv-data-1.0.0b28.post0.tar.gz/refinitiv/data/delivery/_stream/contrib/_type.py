from enum import Enum

from ...._tools import (
    EnumArgsParser,
    make_parse_enum,
    make_convert_to_enum,
)


class ContribType(Enum):
    REFRESH = "Refresh"
    UPDATE = "Update"


contrib_type_enum_arg_parser = EnumArgsParser(
    parse=make_parse_enum(ContribType),
    parse_to_enum=make_convert_to_enum(ContribType),
)
