from typing import Dict

__contracts__ = ["soft_fail"]


async def base64encode(hub, data: str) -> Dict:
    """
    Applies Base64 encoding to a string.
    """
    hub.log.warning(
        "core.encoding.base64encode Deprecated, use 'core.encoder.base64.encode'"
    )
    return hub.exec.core.encoder.base64.encode(data)


async def base64decode(hub, encoded_data: str) -> Dict:
    """
    Decode string containing a Base64 character sequence to the original string.
    """
    hub.log.warning(
        "core.encoding.base64decode Deprecated, use 'core.encoder.base64.decode'"
    )
    return hub.exec.core.encoder.base64.decode(encoded_data)
