

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.common.dec_string import DecString


class QredoCreateTxExtraParams(BaseModel):
    chainID: DecString
