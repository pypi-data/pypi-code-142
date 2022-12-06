import itertools
from dataclasses import dataclass, field
from typing import Optional

from ._endpoint_data import RequestMethod

_id_iterator = itertools.count()


@dataclass
class Request:
    url: str
    method: str = RequestMethod.GET
    headers: dict = field(default_factory=dict)
    data: Optional[dict] = None
    params: Optional[dict] = None
    json: Optional[dict] = None
    closure: Optional[str] = None
    auto_retry: bool = False
    timeout: Optional[int] = None
    id: int = field(init=False, default_factory=lambda: next(_id_iterator))
