from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class ChainInfo:
    chain_name: str
    chain_id: int
    node_uri: str
    faucet_uri: Optional[str] = None

    def json(self) -> dict:
        return asdict(self)
