from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union

from pydantic.generics import GenericModel

T = TypeVar("T")


class JsonRpcRequest(GenericModel, Generic[T]):
    jsonrpc = "2.0"
    method: str
    params: Optional[T]
    id: Optional[Union[str, int]]
