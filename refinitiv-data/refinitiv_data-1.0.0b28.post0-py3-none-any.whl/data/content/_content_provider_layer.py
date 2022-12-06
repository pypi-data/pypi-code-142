from typing import Generic, TypeVar, Optional, Callable, TYPE_CHECKING, Any

from ..delivery._data import _data_provider
from ..usage_collection._filter_types import FilterType
from ..usage_collection._logger import get_usage_logger
from ..usage_collection._utils import ModuleName

if TYPE_CHECKING:
    from .._core.session import Session

T = TypeVar("T")


class ContentUsageLoggerMixin(Generic[T]):
    _kwargs: dict
    # Should not change even if class name is changed, should be set by subclasses
    _USAGE_CLS_NAME: str

    def __init__(self, *args, **kwargs):
        get_usage_logger().log_func(
            name=f"{ModuleName.CONTENT}.{self._USAGE_CLS_NAME}.__init__",
            func_path=f"{self.__class__.__module__}."
            f"{self.__class__.__qualname__}."
            f"__init__",
            args=args,
            kwargs=kwargs,
            desc={FilterType.LAYER_CONTENT, FilterType.INIT},
        )
        super().__init__(*args, **kwargs)

    def get_data(
        self,
        session: Optional["Session"] = None,
        on_response: Optional[Callable] = None,
    ) -> T:
        # Library usage logging
        get_usage_logger().log_func(
            name=f"{ModuleName.CONTENT}.{self._USAGE_CLS_NAME}.get_data",
            func_path=f"{self.__class__.__module__}."
            f"{self.__class__.__qualname__}."
            f"get_data",
            kwargs={**self._kwargs},
            desc={FilterType.SYNC, FilterType.LAYER_CONTENT},
        )
        return super().get_data(session, on_response)

    async def get_data_async(
        self,
        session: Optional["Session"] = None,
        on_response: Optional[Callable] = None,
        closure: Optional[Any] = None,
    ) -> T:
        # Library usage logging
        self._kwargs["closure"] = closure
        get_usage_logger().log_func(
            name=f"{ModuleName.CONTENT}.{self._USAGE_CLS_NAME}.get_data_async",
            func_path=f"{self.__class__.__module__}."
            f"{self.__class__.__qualname__}."
            f"get_data_async",
            kwargs={**self._kwargs},
            desc={FilterType.ASYNC, FilterType.LAYER_CONTENT},
        )
        return await super().get_data_async(session, on_response)


class ContentProviderLayer(ContentUsageLoggerMixin, _data_provider.DataProviderLayer):
    def __init__(self, content_type, **kwargs):
        _data_provider.DataProviderLayer.__init__(
            self,
            data_type=content_type,
            **kwargs,
        )
