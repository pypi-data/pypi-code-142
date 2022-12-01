
from typing import Optional

from metamask_institutional.sdk.common.base_model import BaseModel


class JsonRpcTransactionStatus(BaseModel):
    finished: bool  # Whether the transaction has finised, e.g. it is completed, failed or cancelled
    signed: bool  # Whether the transaction has been signed
    submitted: Optional[bool]  # Whether the transaction was submitted to the blockchain
    success: Optional[bool]  # Whether the transaction was successful, i.e. it was included in a block and not reverted
    displayText: str  # Short text to display to the user
    reason: Optional[str]  # The reason for the transaction status
