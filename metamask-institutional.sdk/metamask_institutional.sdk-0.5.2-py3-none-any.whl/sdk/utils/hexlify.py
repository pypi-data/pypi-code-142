from typing import Optional

from metamask_institutional.sdk.common.dec_string import DecString
from metamask_institutional.sdk.common.hex_string import HexString


def hexlify(dec_string: Optional[DecString]) -> Optional[HexString]:
    """
    Converts a decimal string to its hexadecimal representation. Support None input.
    """
    return hex(int(dec_string)) if dec_string is not None else None
