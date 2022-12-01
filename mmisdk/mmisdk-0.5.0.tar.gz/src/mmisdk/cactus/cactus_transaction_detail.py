from typing import Optional
from typing import Union

from pydantic import Field

from mmisdk.common.base_model import BaseModel
from mmisdk.common.dec_string import DecString
from mmisdk.common.empty_string import EmptyString
from mmisdk.common.ethereum_address import EthereumAddress
from mmisdk.common.hex_string import HexString


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
