
from typing import Optional

from pydantic import Field

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.common.ethereum_address import EthereumAddress
from metamask_institutional.sdk.common.hex_string import HexString


class JsonRpcCreateTransactionParams(BaseModel):
    type: Optional[HexString]
    from_: EthereumAddress = Field(None, alias="from")  # In Python, "from" is a reserved keyword
    to: EthereumAddress
    gas: HexString  # Gas limit
    value: HexString
    data: Optional[HexString]
    maxPriorityFeePerGas: Optional[HexString]  # Maximum fee per gas the sender is willing to pay miners in wei
    # The maximum total fee per gas the sender is willing to pay (includes the network / base fee and miner / priority fee) in wei
    maxFeePerGas: Optional[HexString]
    # The maximum total fee per gas the sender is willing to pay (includes the network / base fee and miner / priority fee) in wei
    gasPrice: Optional[HexString]
