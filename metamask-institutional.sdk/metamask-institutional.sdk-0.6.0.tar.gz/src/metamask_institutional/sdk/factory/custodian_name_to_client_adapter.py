from metamask_institutional.sdk.adapters.bitgo_adapter import BitgoAdapter
from metamask_institutional.sdk.adapters.cactus_adapter import CactusAdapter
from metamask_institutional.sdk.adapters.jsonrpc_adapter import JsonRpcAdapter
from metamask_institutional.sdk.adapters.qredo_adapter import QredoAdapter
from metamask_institutional.sdk.bitgo.bitgo_client import BitgoClient
from metamask_institutional.sdk.cactus.cactus_client import CactusClient
from metamask_institutional.sdk.jsonrpc.jsonrpc_client import JsonRpcClient
from metamask_institutional.sdk.qredo.qredo_client import QredoClient

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
