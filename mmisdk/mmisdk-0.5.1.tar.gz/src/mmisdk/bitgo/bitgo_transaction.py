from typing import Dict
from typing import Optional

from pydantic import Field

from mmisdk.common.base_model import BaseModel
from mmisdk.common.dec_string import DecString
from mmisdk.common.ethereum_address import EthereumAddress
from mmisdk.common.hex_string import HexString

# Using "Optional" on all fields as we're missing specific API docs for BitGo


class BitgoTransaction(BaseModel):
    transactionStatus: Optional[str]
    custodianTransactionId: Optional[str]
    from_: Optional[EthereumAddress] = Field(None, alias="from")
    to: Optional[EthereumAddress]
    coin: Optional[str]
    value: Optional[DecString]
    gasLimit: Optional[DecString]
    userId: Optional[str]
    createdTime: Optional[str]
    data: Optional[HexString]
    decodedData: Optional[Dict]
    transactionHash: Optional[HexString]
