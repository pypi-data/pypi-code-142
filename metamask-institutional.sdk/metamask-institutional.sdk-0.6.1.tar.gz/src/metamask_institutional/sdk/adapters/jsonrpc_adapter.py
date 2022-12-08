

from typing import Union

from metamask_institutional.sdk.common.custodian import Custodian
from metamask_institutional.sdk.common.transaction import Transaction
from metamask_institutional.sdk.common.transaction import TransactionStatus
from metamask_institutional.sdk.common.transaction_params import EIP1559TxParams
from metamask_institutional.sdk.common.transaction_params import LegacyTxParams
from metamask_institutional.sdk.jsonrpc.jsonrpc_client import JsonRpcClient
from metamask_institutional.sdk.jsonrpc.jsonrpc_create_transaction_metadata import JsonRpcCreateTransactionMetadata
from metamask_institutional.sdk.jsonrpc.jsonrpc_create_transaction_params import JsonRpcCreateTransactionParams
from metamask_institutional.sdk.jsonrpc.jsonrpc_get_transaction_result import JsonRpcGetTransactionResult
from metamask_institutional.sdk.utils.decify import decify
from metamask_institutional.sdk.utils.hexlify import hexlify


class JsonRpcAdapter(Custodian):

    def __init__(self, client: JsonRpcClient) -> None:
        self.client = client

    def get_transaction(self, transaction_id, chain_id=1) -> Transaction:
        get_tx_result = self.client.get_transaction_by_id(transaction_id)
        return self.__map_jsonrpc_transaction_to_transaction(get_tx_result)

    def create_transaction(self, tx_params: Union[LegacyTxParams, EIP1559TxParams], extra_params) -> Transaction:
        # Parse and type check params
        type_ = tx_params["type"] if 'type' in tx_params else '1'
        tx_params_parsed = EIP1559TxParams(**tx_params) if type_ == '2' else LegacyTxParams(**tx_params)
        extra_params_parsed = JsonRpcCreateTransactionMetadata(**extra_params)

        gasPrice = tx_params_parsed.gasPrice if type_ == '1' else None
        maxPriorityFeePerGas = tx_params_parsed.maxPriorityFeePerGas if type_ == '2' else None
        maxFeePerGas = tx_params_parsed.maxFeePerGas if type_ == '2' else None

        jsonrpc_create_tx_params = JsonRpcCreateTransactionParams(
            type=hexlify(tx_params_parsed.type),
            from_=tx_params_parsed.from_,
            to=tx_params_parsed.to,
            gas=hexlify(tx_params_parsed.gas),
            value=hexlify(tx_params_parsed.value),
            data=tx_params_parsed.data,
            maxPriorityFeePerGas=hexlify(maxPriorityFeePerGas),
            maxFeePerGas=hexlify(maxFeePerGas),
            gasPrice=hexlify(gasPrice)

        )

        tx_id = self.client.create_transaction(jsonrpc_create_tx_params, extra_params_parsed)
        transaction = self.client.get_transaction_by_id(tx_id)
        return self.__map_jsonrpc_transaction_to_transaction(transaction)

    def __map_jsonrpc_transaction_to_transaction(self, jsonrpc_transaction: JsonRpcGetTransactionResult) -> Transaction:
        return Transaction(
            id=jsonrpc_transaction.id,
            type=decify(jsonrpc_transaction.type),  # Convert from hex to decimal
            from_=jsonrpc_transaction.from_,
            to=jsonrpc_transaction.to,
            value=decify(jsonrpc_transaction.value),
            gas=decify(jsonrpc_transaction.gas),
            gasPrice=decify(jsonrpc_transaction.gasPrice),
            maxPriorityFeePerGas=decify(jsonrpc_transaction.maxPriorityFeePerGas),
            maxFeePerGas=decify(jsonrpc_transaction.maxFeePerGas),
            nonce=decify(jsonrpc_transaction.nonce),
            data=jsonrpc_transaction.data,
            hash=jsonrpc_transaction.hash,
            status=TransactionStatus(**jsonrpc_transaction.status.dict(by_alias=True))
        )
