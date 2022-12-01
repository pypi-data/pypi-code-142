
from typing import Optional

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.common.hex_string import HexString


class JsonRpcCreateTransactionMetadata(BaseModel):
    chainId: HexString
    originUrl: Optional[str]  # The web page/dapp where the transaction originated
    transactionCategory: Optional[str]  # The category of transaction, as best can be determined by the wallet
    note: Optional[str]  # A note to be attached to the transaction which can be specified by the user
