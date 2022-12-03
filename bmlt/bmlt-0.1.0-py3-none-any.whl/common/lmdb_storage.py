import json
from typing import Any, Dict

from lmdbm import Lmdb


class JsonLmdb(Lmdb):
    """LMDB-based storage with dict-like interface."""

    def _pre_key(self, value: str) -> bytes:
        return value.encode("utf-8")

    def _post_key(self, value: bytes) -> str:
        return value.decode("utf-8")

    def _pre_value(self, value: Dict[str, Any]) -> bytes:
        return json.dumps(value).encode("utf-8")

    def _post_value(self, value: bytes) -> Dict[str, Any]:
        return json.loads(value.decode("utf-8"))
