from typing import Optional

from . import chain_info as aptos_chain_info
from .. import comms, exceptions


class AptosComm(comms.BaseCommunication):
    def __init__(
        self,
        *,
        is_mainnet: bool = False,
        is_testnet: bool = False,
        is_devnet: bool = False,
        node_uri: Optional[str] = None,
        faucet_uri: Optional[str] = None,
        use_sdk: bool = False,
    ) -> None:
        chain_info: Optional[aptos_chain_info.AptosChainInfo]
        if is_mainnet:
            chain_info = aptos_chain_info.APTOS_CHAIN_INFO_MAINNET
        elif is_testnet:
            chain_info = aptos_chain_info.APTOS_CHAIN_INFO_TESTNET
        elif is_devnet:
            chain_info = aptos_chain_info.APTOS_CHAIN_INFO_DEVNET
        else:
            chain_info = None

        if node_uri is None:
            node_uri = chain_info.node_uri

        if use_sdk:  # use `aptos-sdk`
            try:
                from aptos_sdk.client import RestClient
            except (ModuleNotFoundError, ImportError) as e:
                raise exceptions.SdkNotFoundError(
                    "Cannot find the `aptos_sdk` module.\n"
                    "Please install SDK first: https://aptos.dev/sdks/python-sdk"
                ) from e
            else:
                self.aptos_client = RestClient(node_uri)

                if chain_info is None:
                    chain_info = aptos_chain_info.AptosChainInfo(
                        "Unknown", self.aptos_client.chain_id, node_uri
                    )
                    for info in aptos_chain_info.pre_defined_chain_info_list:
                        if info.chain_id == chain_info.chain_id:
                            chain_info = info
                            break
                else:
                    if chain_info.chain_id != self.aptos_client.chain_id:
                        raise exceptions.DifferentChainInfoError(
                            f"The remote chain node is not {chain_info.chain_name}"
                            f" (Chain ID: {chain_info.chain_id}):"
                            f" remote node's chain ID is {self.aptos_client.chain_id}"
                        )
        else:  # use `wasd3r REST server`
            # TODO: need to implement REST API client.
            self.aptos_client = None
            assert False

        chain_info.faucet_uri = faucet_uri

        super().__init__(chain_info, use_sdk=use_sdk)
