from typing import Generic
from typing import List
from typing import TypeVar

from pydantic.generics import GenericModel

from metamask_institutional.sdk.bitgo.bitgo_response_meta import BitgoResponseMeta

T = TypeVar("T")


class BitgoListResponse(GenericModel, Generic[T]):
    data: List[T]
    meta: BitgoResponseMeta
