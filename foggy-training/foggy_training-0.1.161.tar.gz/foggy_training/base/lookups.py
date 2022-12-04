from typing import Union

from torch.nn import functional
from torchmetrics import Metric
import torchmetrics


def suggest_string(candidates, lookfor, typ):
    print(lookfor, f'is not a valid choice for {typ}. Possible choices are:', candidates)


def get_loss_fun(loss: Union[str, callable]):
    if loss is None:
        return

    if callable(loss):
        return loss
    try:
        return getattr(functional, loss)
    except AttributeError:
        raise ValueError(suggest_string(dir(functional), loss, typ='loss'))


def get_metric_fun(metric: Union[str, Metric]):
    if isinstance(metric, Metric):
        return metric
    try:
        return getattr(torchmetrics, metric)()
    except AttributeError:
        raise ValueError(suggest_string(dir(torchmetrics), metric, typ='metric'))
