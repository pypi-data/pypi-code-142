from typing import Optional

from mmisdk.common.base_model import BaseModel
from mmisdk.common.dec_string import DecString


class CactusCreateTxExtraParams(BaseModel):
    chainId: DecString
    note: Optional[str]
