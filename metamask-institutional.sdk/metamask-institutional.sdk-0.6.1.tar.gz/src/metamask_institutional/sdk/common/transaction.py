from typing import Optional

from pydantic import Field

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.common.dec_string import DecString
from metamask_institutional.sdk.common.ethereum_address import EthereumAddress
from metamask_institutional.sdk.common.hex_string import HexString


class TransactionStatus(BaseModel):
    finished: bool  # Whether the transaction has finised, e.g. it is completed, failed or cancelled
    signed: bool  # Whether the transaction has been signed
    submitted: Optional[bool]  # Whether the transaction was submitted to the blockchain
    success: Optional[bool]  # Whether the transaction was successful, i.e. it was included in a block and not reverted
    displayText: str  # Short text to display to the user
    reason: Optional[str]  # The reason for the transaction status


class Transaction(BaseModel):
    id: str
    type: DecString
    from_: EthereumAddress = Field(None, alias="from")
    to: Optional[EthereumAddress]
    value: Optional[DecString]  # In Wei
    gas: Optional[DecString]  # Same as gasLimit
    gasPrice: Optional[DecString]
    maxPriorityFeePerGas: Optional[DecString]
    maxFeePerGas: Optional[DecString]
    nonce: Optional[DecString]
    data: Optional[HexString]
    hash: Optional[HexString]
    status: TransactionStatus
