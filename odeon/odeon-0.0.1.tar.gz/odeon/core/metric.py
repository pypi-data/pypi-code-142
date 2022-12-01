from typing import Type, Dict, List

from torchmetrics import Metric, MetricCollection
from torchmetrics.classification import BinaryAccuracy, BinarySpecificity, BinaryRecall, BinaryPrecision
from torchmetrics.classification import BinaryF1Score, BinaryJaccardIndex, BinaryROC, BinaryCalibrationError
from torchmetrics.classification import BinaryConfusionMatrix, BinaryAUROC
from torchmetrics.classification import MulticlassAccuracy, MulticlassPrecision, MulticlassRecall, MulticlassROC
from torchmetrics.classification import MulticlassF1Score, MulticlassJaccardIndex, MulticlassAUROC
from torchmetrics.classification import MulticlassConfusionMatrix, MulticlassCalibrationError
from torchmetrics.classification import MultilabelAccuracy, MultilabelPrecision, MultilabelRecall, MultilabelF1Score
from torchmetrics.classification import MultilabelROC, MultilabelAUROC

from odeon.core.registry import GenericRegistry
from odeon.core.types import OdnMetric


@GenericRegistry.register('MetricRegistry', aliases=['metricReg'])
class MetricRegistry(GenericRegistry[Type[OdnMetric]]):
    @classmethod
    def register_fn(cls, cl: Type[OdnMetric], name: str):
        assert issubclass(cl, Metric) or issubclass(cl, MetricCollection)
        cls._registry[name] = cl


def build_metrics(metrics: List[Dict]):
    for metric in metrics:
        name = metric['name']
        if 'params' in metric:
            params: Dict = metric['params']
            MetricRegistry.create(name=name, **params)
        else:
            MetricRegistry.create(name=name)
