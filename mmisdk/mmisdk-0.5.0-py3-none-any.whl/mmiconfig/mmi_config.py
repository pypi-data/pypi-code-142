from typing import Any
from typing import List

from mmisdk.common.base_model import BaseModel
from mmisdk.mmiconfig.custodian_config import CustodianConfig


class MMIConfig(BaseModel):
    custodians: List[CustodianConfig]
    portfolio: Any
