
from typing import Optional

from pydantic import Field

from mmisdk.common.base_model import BaseModel
from mmisdk.common.dec_string import DecString
from mmisdk.common.ethereum_address import EthereumAddress
from mmisdk.common.hex_string import HexString


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
