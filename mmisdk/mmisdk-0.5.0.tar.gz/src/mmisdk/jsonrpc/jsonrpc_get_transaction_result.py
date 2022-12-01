
from typing import Optional

from pydantic import Field

from mmisdk.common.base_model import BaseModel
from mmisdk.common.ethereum_address import EthereumAddress
from mmisdk.common.hex_string import HexString
from mmisdk.jsonrpc.jsonrpc_transaction_status import JsonRpcTransactionStatus


class JsonRpcGetTransactionResult(BaseModel):
    id: str
    nonce: Optional[HexString]  # hex encoded unsigned integer
    hash: Optional[HexString]  # Keccak 256 Hash of the RLP encoding of a transaction
    status: JsonRpcTransactionStatus
    type: Optional[HexString]
    from_: EthereumAddress = Field(None, alias="from")
    to: EthereumAddress
    gas: Optional[HexString]  # Gas limit
    value: HexString
    data: Optional[HexString]
    maxPriorityFeePerGas: Optional[HexString]  # Maximum fee per gas the sender is willing to pay miners in wei
    # The maximum total fee per gas the sender is willing to pay (includes the network / base fee and miner / priority fee) in wei
    maxFeePerGas: Optional[HexString]
    gasPrice: Optional[HexString]  # The gas price willing to be paid by the sender in wei
