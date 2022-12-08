from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union

from pydantic.generics import GenericModel

from metamask_institutional.sdk.jsonrpc.jsonrpc_error import JsonRpcError

T = TypeVar("T")


class JsonRpcResponse(GenericModel, Generic[T]):
    jsonrpc = "2.0"
    result: Optional[T]
    error: Optional[JsonRpcError]
    id: Optional[Union[str, int]]
