from typing import Optional

from mmisdk.common.dec_string import DecString
from mmisdk.common.hex_string import HexString


def hexlify(dec_string: Optional[DecString]) -> Optional[HexString]:
    """
    Converts a decimal string to its hexadecimal representation. Support None input.
    """
    return hex(int(dec_string)) if dec_string is not None else None
