from enum import Enum
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pydantic import Field

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.common.dec_string import DecString
from metamask_institutional.sdk.common.empty_string import EmptyString
from metamask_institutional.sdk.common.ethereum_address import EthereumAddress
from metamask_institutional.sdk.common.hex_string import HexString


class QredoTransactionEvent(BaseModel):
    id: str
    timestamp: int
    status: str
    message: str


class QredoTransactionStatus(str, Enum):
    PENDING = "pending"
    CREATED = "created"
    AUTHORIZED = "authorized"
    APPROVED = "approved"
    EXPIRED = "expired"
    CANCELLED = "cancelled"
    REJECTED = "rejected"
    SIGNED = "signed"
    SCHEDULED = "scheduled"
    PUSHED = "pushed"
    CONFIRMED = "confirmed"
    MINED = "mined"
    FAILED = "failed"


class QredoTransactionInfo(BaseModel):
    txID: str
    txHash: Union[HexString, EmptyString]
    status: QredoTransactionStatus
    nonce: int
    from_:  EthereumAddress = Field(None, alias="from")
    to: EthereumAddress
    value: DecString
    gasLimit: DecString
    maxPriorityFeePerGas: Optional[DecString]
    maxFeePerGas: Optional[DecString]
    gasPrice: Optional[DecString]
    data: Union[HexString, EmptyString]
    rawTX: str
    createdBy: str
    network: str
    chainID: DecString
    timestamps: Dict
    events: List[QredoTransactionEvent]
