import contextlib
import typing as t

try:
    from typing import final
except ImportError:
    from typing_extensions import final

from abc import abstractmethod

from foxhelpers.distributed_helper import DistributedEnv

BASE = 'Metric' if t.TYPE_CHECKING else object
RETURN_TYPE = t.TypeVar("RETURN_TYPE")


class Metric(t.Generic[RETURN_TYPE]):
    _initialized = False

    def __init__(self, **kwargs) -> None:
        self._initialized = True

    @abstractmethod
    def reset(self):
        pass

    def add(self, *args, **kwargs):
        assert self._initialized, f"{self.__class__.__name__} must be initialized by overriding __init__"
        return self._add(*args, **kwargs)

    @abstractmethod
    def _add(self, *args, **kwargs):
        pass

    def summary(self) -> RETURN_TYPE:
        return self._summary()

    @abstractmethod
    def _summary(self) -> RETURN_TYPE:
        pass

    @final
    def join(self):
        return

    @final
    def close(self):
        return


class DistributedMixin(BASE):
    @abstractmethod
    def _synchronize(self):
        """Synchronize values across GPUs"""
        pass

    @final
    def synchronize(self):
        if self.is_distributed:
            self._synchronize()

    @property
    def is_distributed(self) -> bool:
        return DistributedEnv().is_distributed

    @property
    def process_num(self) -> int:
        return DistributedEnv().word_size

    def add(self, *args, **kwargs):
        super(DistributedMixin, self).add(*args, **kwargs)
        self.synchronize()

    @contextlib.contextmanager
    def synchronize_cmx(self):
        self.synchronize()
        yield
