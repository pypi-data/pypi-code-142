
from typing import Any

from metamask_institutional.sdksk-institutional.sdk.common.base_model import BaseModel


class JsonRpcError(BaseModel):
    code: int
    message: str
    data: Any
