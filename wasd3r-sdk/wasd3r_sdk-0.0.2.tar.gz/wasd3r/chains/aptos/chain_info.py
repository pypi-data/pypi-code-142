from itertools import chain
from .. import chain_info


class AptosChainInfo(chain_info.ChainInfo):
    """Aptos chain info."""


APTOS_CHAIN_INFO_MAINNET = AptosChainInfo(
    "Mainnet",
    1,
    "https://fullnode.mainnet.aptoslabs.com/v1",
)

APTOS_CHAIN_INFO_TESTNET = AptosChainInfo(
    "Testnet",
    2,
    "https://fullnode.mainnet.aptoslabs.com/v1",
    "https://faucet.testnet.aptoslabs.com",
)

APTOS_CHAIN_INFO_DEVNET = AptosChainInfo(
    "Devnet",
    39,
    "https://fullnode.devnet.aptoslabs.com/v1",
    "https://tap.devnet.prod.gcp.aptosdev.com",
)

pre_defined_chain_info_list = [
    APTOS_CHAIN_INFO_MAINNET,
    APTOS_CHAIN_INFO_TESTNET,
    APTOS_CHAIN_INFO_DEVNET,
]
