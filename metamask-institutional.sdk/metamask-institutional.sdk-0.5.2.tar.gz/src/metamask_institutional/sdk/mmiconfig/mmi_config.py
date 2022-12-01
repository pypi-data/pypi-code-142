from typing import Any
from typing import List

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.mmiconfig.custodian_config import CustodianConfig


class MMIConfig(BaseModel):
    custodians: List[CustodianConfig]
    portfolio: Any
