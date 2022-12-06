from .chain_info import ChainInfo


class BaseCommunication:
    """Communication class with a blockchain node according to the input chain info"""

    def __init__(self, chain_info: ChainInfo, *, use_sdk: bool = False) -> None:
        self.chain_info = chain_info
        self.use_sdk = use_sdk

    @property
    def chain_name(self) -> str:
        return self.chain_info.chain_name

    @property
    def chain_id(self) -> int:
        return self.chain_info.chain_id
