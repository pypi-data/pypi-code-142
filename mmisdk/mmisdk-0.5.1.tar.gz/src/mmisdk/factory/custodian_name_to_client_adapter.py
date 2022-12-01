from mmisdk.adapters.bitgo_adapter import BitgoAdapter
from mmisdk.adapters.cactus_adapter import CactusAdapter
from mmisdk.adapters.jsonrpc_adapter import JsonRpcAdapter
from mmisdk.adapters.qredo_adapter import QredoAdapter
from mmisdk.bitgo.bitgo_client import BitgoClient
from mmisdk.cactus.cactus_client import CactusClient
from mmisdk.jsonrpc.jsonrpc_client import JsonRpcClient
from mmisdk.qredo.qredo_client import QredoClient

"""
Map each custodian name to its appropriate Client class, and to its appropriate Adapter class.
"""

CUSTODIAN_NAME_TO_CLIENT_ADAPTER = {
    "qredo": {
        "client": QredoClient,
        "adapter": QredoAdapter
    },
    "qredo-dev": {
        "client": QredoClient,
        "adapter": QredoAdapter
    },
    "cactus": {
        "client": CactusClient,
        "adapter": CactusAdapter
    },
    "cactus-dev": {
        "client": CactusClient,
        "adapter": CactusAdapter
    },
    "bitgo": {
        "client": BitgoClient,
        "adapter": BitgoAdapter
    },
    "bitgo-test": {
        "client": BitgoClient,
        "adapter": BitgoAdapter
    },
    "default": {
        "client": JsonRpcClient,
        "adapter": JsonRpcAdapter
    }
}
