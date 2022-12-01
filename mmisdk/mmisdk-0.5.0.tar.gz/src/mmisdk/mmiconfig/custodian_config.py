from typing import Optional

from pydantic import AnyHttpUrl
from pydantic import HttpUrl

from mmisdk.common.base_model import BaseModel


class CustodianConfig(BaseModel):
    name: str
    apiBaseUrl: Optional[AnyHttpUrl]
    refreshTokenUrl: Optional[AnyHttpUrl]
