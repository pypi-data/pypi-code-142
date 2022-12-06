from typing import (
    TYPE_CHECKING,
)

from ._content_data import Data
from ._parsed_data import ParsedData
from ._response import Response
from ..._content_type import ContentType

if TYPE_CHECKING:
    from ..._core.session import Session


class ResponseFactory:
    def __init__(self, response_class=Response, data_class=Data):
        super().__init__()
        self.data_class = data_class
        self.response_class = response_class

    def get_raw(self, data: ParsedData):
        return data.content_data

    def get_dfbuilder(self, content_type=None, dfbuild_type=None, **kwargs):
        from ...content._df_builder_factory import get_dfbuilder, DFBuildType

        content_type = content_type or kwargs.get(
            "__content_type__", ContentType.DEFAULT
        )
        dfbuild_type = dfbuild_type or kwargs.get(
            "__dfbuild_type__", DFBuildType.DATE_AS_INDEX
        )
        return get_dfbuilder(content_type, dfbuild_type)

    def create_success(self, data: ParsedData, session: "Session" = None, **kwargs):
        inst = self.response_class(True, data)
        raw = self.get_raw(data)
        dfbuilder = self.get_dfbuilder(**kwargs)
        inst.data = self.data_class(raw, dfbuilder=dfbuilder, **kwargs)
        inst.data._owner = inst
        return inst

    def create_fail(self, data: ParsedData, **kwargs):
        inst = self.response_class(False, data)
        inst.data = self.data_class(data.content_data)
        inst.data._owner = inst
        return inst
