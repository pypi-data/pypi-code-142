
from typing import Optional

from mmisdk.common.base_model import BaseModel
from mmisdk.common.hex_string import HexString


class JsonRpcCreateTransactionMetadata(BaseModel):
    chainId: HexString
    originUrl: Optional[str]  # The web page/dapp where the transaction originated
    transactionCategory: Optional[str]  # The category of transaction, as best can be determined by the wallet
    note: Optional[str]  # A note to be attached to the transaction which can be specified by the user
