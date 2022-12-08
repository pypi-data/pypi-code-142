from typing import Optional

from pydantic import Field

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.common.dec_string import DecString
from metamask_institutional.sdk.common.ethereum_address import EthereumAddress
from metamask_institutional.sdk.common.hex_string import HexString


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
