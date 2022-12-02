from typing import Any, Sequence, Set, Type, Union

from pydantic import BaseModel

from chalk.utils import AnyDataclass


class StreamResolverParam(BaseModel):
    name: str


class StreamResolverParamMessage(StreamResolverParam):
    typ: Union[Type[str], Type[bytes], Type[BaseModel], AnyDataclass]


class StreamResolverParamMessageWindow(StreamResolverParam):
    item_typ: Union[Type[str], Type[bytes], Type[BaseModel], AnyDataclass]


class StreamResolverSignature(BaseModel):
    params: Sequence[StreamResolverParam]
    output_feature_fqns: Set[str]


class StreamResolverParamKeyedState(StreamResolverParam):
    typ: Union[Type[BaseModel], Type[AnyDataclass]]
    default_value: Any
