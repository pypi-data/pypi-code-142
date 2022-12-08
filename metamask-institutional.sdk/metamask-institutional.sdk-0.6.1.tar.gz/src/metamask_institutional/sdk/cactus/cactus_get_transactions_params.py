from typing import Optional

from pydantic import Field

from metamask_institutional.sdk.common.base_model import BaseModel
from metamask_institutional.sdk.common.dec_string import DecString
from metamask_institutional.sdk.common.ethereum_address import EthereumAddress
from metamask_institutional.sdk.common.hex_string import HexString


class CactusGetTransactionsParams(BaseModel):
    """ Refer to ./custody-defi-api-4.yaml for more details """
    chainId: DecString
    from_: Optional[EthereumAddress] = Field(None, alias="from")
    transactionId: Optional[str]
    transactionHash: Optional[HexString]
