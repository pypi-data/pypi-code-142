
from typing import Any

from mmisdk.common.base_model import BaseModel


class JsonRpcError(BaseModel):
    code: int
    message: str
    data: Any
