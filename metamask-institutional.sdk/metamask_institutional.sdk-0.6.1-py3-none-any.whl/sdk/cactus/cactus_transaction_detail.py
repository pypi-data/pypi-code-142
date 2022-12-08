from typing import Optional
from typing import Union

from pydantic import Field

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.common.dec_string import DecString
from metamask_institutional.sdk.common.empty_string import EmptyString
from metamask_institutional.sdk.common.ethereum_address import EthereumAddress
from metamask_institutional.sdk.common.hex_string import HexString


class CactusTransactionDetail(BaseModel):
    """ Refer to ./custody-defi-api-4.yaml for more details """
    transactionStatus: str
    transactionHash: Optional[HexString]
    custodian_transactionId: Optional[str]
    gasPrice: Optional[DecString]
    maxFeePerGas: Optional[DecString]
    maxPriorityFeePerGas: Optional[DecString]
    gasLimit: Optional[DecString]
    nonce: Union[DecString, EmptyString, None]
    from_: Optional[EthereumAddress] = Field(None, alias="from")
    signature: Optional[str]
