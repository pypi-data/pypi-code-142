from typing import Union

import pytorch_lightning as pl
from attr import define, field
from torch import optim
from torchinfo import summary
from torchmetrics import MetricCollection

from foggy_training.base.lookups import get_loss_fun, get_metric_fun


@define
class ForwardResult:
    pred = field()
    true = field(default=None)
    loss = field(default=None)


class LightningExtended(pl.LightningModule):

    """

    The Lightning Extended Modules provides some defaults for training and validation sets. You may do the following:

    ```python
    from foggy_training import models
    x = [[1., 1.], [2., 2.], [3., 3.]]
    y = [1., 2., 3.]
    data = {'x': x, 'y': y}
    model = models.LinearRegression(n_inputs=2)
    model.fit(data, epochs=20)
    ```

    """
    def __init__(self, loss_fun: Union[str, callable] = None, lr: float = None, metrics=None):
        """

        loss: string or callable. if string, must match the name of torch.nn.functional losses
        lr: float, learning rate
        metrics: list of torchmetrics

        """
        super(LightningExtended, self).__init__()
        self.loss_fun = get_loss_fun(loss_fun)
        self.loss = None
        self.lr = lr if lr is not None else 1e-3
        metrics = [] if metrics is None else metrics
        assert isinstance(metrics, list), 'metrics must be list of metrics'
        metrics = [get_metric_fun(m) for m in metrics]
        metrics = MetricCollection(metrics)
        self.train_metrics = metrics.clone(prefix='train_')
        self.val_metrics = metrics.clone(prefix='val_')

        if self.loss_fun is None:
            print('loss_fun is None. Make sure you provide loss using self.loss in forward. '
                  'Otherwise, training will fail and MisconfigurationException will be raised py PL.')

    def shared_step(self, batch) -> ForwardResult:
        result = self(batch)
        return result

    def get_loss(self, result):
        if self.loss_fun is not None:
            loss = self.loss_fun(result.pred, result.true)
        else:
            loss = 0

        if self.loss is not None:
            loss = self.loss + loss
            self.loss = None

        return loss

    def training_step(self, batch, batch_idx):
        result = self.shared_step(batch)
        loss = self.get_loss(result)
        logs = dict(loss=loss)
        metrics = self.train_metrics(result.pred, result.true)
        logs = {**logs, **metrics}
        self.log_dict(logs, prog_bar=True, on_epoch=True)
        return loss

    def validation_step(self, batch, batch_idx):
        result = self.shared_step(batch)
        loss = self.get_loss(result)
        logs = dict(val_loss=loss)
        metrics = self.val_metrics(result.pred, result.true)
        logs = {**logs, **metrics}
        self.log_dict(logs, prog_bar=True, on_step=False, on_epoch=True)

    def predict_step(self, batch, batch_idx, dataloader_idx=0):
        return self.shared_step(batch).pred

    def configure_optimizers(self):
        return optim.AdamW(filter(lambda p: p.requires_grad, self.parameters()), lr=self.lr)

    def summary(self, depth: int = 3,
                col_names=('num_params', 'trainable'),
                row_settings=('var_names', ), **kwargs):
        print(summary(self, depth=depth,
                      col_names=col_names,
                      row_settings=row_settings,
                      **kwargs))
