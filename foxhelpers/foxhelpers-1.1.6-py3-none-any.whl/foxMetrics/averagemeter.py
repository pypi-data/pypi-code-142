import typing as t
from collections import defaultdict

import torch
from torch import Tensor
from torch import distributed as dist

from .metric import Metric, DistributedMixin

metric_result = Tensor
dictionary_metric_result = Metric[t.Union[str, metric_result]]


class AverageValueMeter(DistributedMixin, Metric[metric_result]):
    def __init__(self):
        super(AverageValueMeter, self).__init__()
        self.sum = torch.tensor(0.0)
        self.n = 0

    @t.overload
    def add(self, value: Tensor, n: int = 1):
        ...

    def add(self, *args, **kwargs):
        return super(AverageValueMeter, self).add(*args, **kwargs)

    def _add(self, value: Tensor, n=1):
        device, dtype = value.device, value.dtype
        self.sum = self.sum.to(device=device, dtype=dtype) + value.detach() * n
        self.n += n

    def _synchronize(self):
        dist.all_reduce(self.sum)
        self.sum /= self.process_num

    def reset(self):
        self.sum = torch.tensor(0.0)
        self.n = 0

    def _summary(self) -> metric_result:
        # this function returns a dict and tends to aggregate the historical results.
        return torch.nan if self.n == 0 else self.sum / self.n  # noqa


class AverageValueDictionaryMeter(DistributedMixin, Metric[dictionary_metric_result]):
    def _synchronize(self):
        for meters in self._meter_dicts.values():
            meters.synchronize()

    def __init__(self) -> None:
        super().__init__()
        self._meter_dicts: t.Dict[str, AverageValueMeter] = defaultdict(AverageValueMeter)

    def reset(self):
        for k, v in self._meter_dicts.items():
            v.reset()

    def _add(self, **kwargs):
        for k, v in kwargs.items():
            self._meter_dicts[k].add(v)

    def _summary(self):
        return {k: v.summary() for k, v in self._meter_dicts.items()}


class AverageValueListMeter(AverageValueDictionaryMeter):

    def _add(self, list_value: t.Iterable[float] = None, **kwargs):
        assert isinstance(list_value, t.Iterable)
        for i, v in enumerate(list_value):
            self._meter_dicts[str(i)].add(v)
