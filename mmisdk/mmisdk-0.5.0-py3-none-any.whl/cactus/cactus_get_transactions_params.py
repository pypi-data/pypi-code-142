from typing import Optional

from pydantic import Field

from mmisdk.common.base_model import BaseModel
from mmisdk.common.dec_string import DecString
from mmisdk.common.ethereum_address import EthereumAddress
from mmisdk.common.hex_string import HexString


class CactusGetTransactionsParams(BaseModel):
    """ Refer to ./custody-defi-api-4.yaml for more details """
    chainId: DecString
    from_: Optional[EthereumAddress] = Field(None, alias="from")
    transactionId: Optional[str]
    transactionHash: Optional[HexString]
