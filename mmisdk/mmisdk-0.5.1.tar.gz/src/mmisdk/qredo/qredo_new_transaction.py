from typing import Optional

from pydantic import Field

from mmisdk.common.base_model import BaseModel
from mmisdk.common.dec_string import DecString
from mmisdk.common.ethereum_address import EthereumAddress


class QredoNewTransaction(BaseModel):
    from_: EthereumAddress = Field(None, alias="from")
    to: EthereumAddress
    value: DecString
    gasPrice: Optional[DecString]
    maxPriorityFeePerGas:  Optional[DecString]
    maxFeePerGas:  Optional[DecString]
    gasLimit: DecString
    data: str
    chainID: DecString
