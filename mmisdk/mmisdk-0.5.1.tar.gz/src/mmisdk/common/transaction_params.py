from typing import Optional

from pydantic import Field

from mmisdk.common.base_model import BaseModel
from mmisdk.common.dec_string import DecString
from mmisdk.common.ethereum_address import EthereumAddress
from mmisdk.common.hex_string import HexString


class BaseTxParams(BaseModel):
    from_: EthereumAddress = Field(None, alias="from")   # In Python, "from" is a reserved keyword
    to: EthereumAddress
    value: Optional[DecString]
    data: Optional[HexString]
    gas: Optional[DecString]  # Same as gasLimit
    nonce: Optional[DecString]


class LegacyTxParams(BaseTxParams):
    type = 1
    gasPrice: DecString


class EIP1559TxParams(BaseTxParams):
    type = 2
    maxPriorityFeePerGas: DecString
    maxFeePerGas: DecString
