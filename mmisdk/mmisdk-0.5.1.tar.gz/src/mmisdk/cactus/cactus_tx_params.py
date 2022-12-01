from typing import Optional

from pydantic import Field

from mmisdk.common.base_model import BaseModel
from mmisdk.common.dec_string import DecString
from mmisdk.common.ethereum_address import EthereumAddress
from mmisdk.common.hex_string import HexString


class CactusTXParams(BaseModel):
    """ Refer to ./custody-defi-api-4.yaml for more details """
    from_: EthereumAddress = Field(None, alias="from")
    to: EthereumAddress
    gasLimit: DecString
    value: DecString
    data: Optional[HexString]  # In practice it is indeed optional, contrary to what custody-defi-api-4.yaml says
    gasPrice: Optional[DecString]
    maxFeePerGas: Optional[DecString]
    maxPriorityFeePerGas: Optional[DecString]
