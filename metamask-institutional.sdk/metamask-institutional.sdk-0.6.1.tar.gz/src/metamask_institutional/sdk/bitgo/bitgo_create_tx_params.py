
from typing import Optional

from pydantic import Field

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.common.dec_string import DecString
from metamask_institutional.sdk.common.ethereum_address import EthereumAddress
from metamask_institutional.sdk.common.hex_string import HexString


class BitgoCreateTxParamsInner(BaseModel):
    from_: EthereumAddress = Field(None, alias="from")
    to: EthereumAddress
    value: DecString
    gasLimit: DecString
    gasPrice: Optional[DecString]
    maxPriorityFeePerGas: Optional[DecString]
    maxFeePerGas: Optional[DecString]
    data: HexString


class BitgoCreateTxParams(BaseModel):
    txParams: BitgoCreateTxParamsInner
