"""Segmentation tasks."""

import warnings
from typing import Any, Dict, cast, Optional, Tuple

# import matplotlib.pyplot as plt
import pytorch_lightning as pl
import segmentation_models_pytorch as smp
import torch
import torch.nn as nn
from torch import Tensor
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch.utils.data import DataLoader
from torchmetrics import MetricCollection, Metric
from torchmetrics.classification import (  # type: ignore[attr-defined]
    BinaryAccuracy,
    BinaryJaccardIndex,
    BinaryRecall,
    BinarySpecificity,
    BinaryF1Score,
    BinaryPrecision
)

from odeon.core.types import OdnMetric
from odeon.models.change.arch.change_unet import FCSiamDiff, FCSiamConc


# https://github.com/pytorch/pytorch/issues/60979
# https://github.com/pytorch/pytorch/pull/61045
DataLoader.__module__ = "torch.utils.data"  # Sphinx bug


class ChangeUnet(pl.LightningModule):
    """

    """

    def configure_model(self,
                        model: str = 'fc_siam_conc',
                        model_params: Optional[Dict] = None) -> nn.Module:
        """
        Configures the task based on kwargs parameters passed to the constructor.
        Parameters
        ----------
        model
        model_params

        Returns
        -------

        """

        if model_params is None:
            model_params = {}
        if model == "fc_siam_diff":
            return FCSiamDiff(**model_params)
        elif model == "fc_siam_conc":
            return FCSiamConc(**model_params)
        else:
            raise ValueError(
                f"Model type '{model}' is not valid. "
                f"Currently, only supports 'unet'."
            )

    def configure_loss(self,
                       loss: str) -> nn.Module:
        if loss == "bce":
            ignore_value = -1000 if self.ignore_index is None else self.ignore_index
            return nn.BCEWithLogitsLoss()
        elif loss == "focal":
            return smp.losses.FocalLoss("binary", normalized=True)
        else:
            raise ValueError(f"Loss type '{loss}' is not valid. "
                             f"Currently, supports 'bce', or 'focal' loss.")

    def configure_learning(self):
        ...

    def configure_metrics(self, metric_params: Dict) -> Tuple[OdnMetric, OdnMetric, OdnMetric]:

        train_metrics = MetricCollection(
            [
                BinaryAccuracy(),
                BinaryJaccardIndex(),
                BinaryRecall(),
                BinarySpecificity(),
                BinaryPrecision(),
                BinaryF1Score()
            ],
            prefix="train_")
        val_metrics = self.train_metrics.clone(prefix="val_")
        test_metrics = self.train_metrics.clone(prefix="test_")
        return train_metrics, val_metrics, test_metrics

    def __init__(self,
                 model: str = 'fc_siam_conc',
                 model_params: Optional[Dict] = None,
                 loss: str = 'bce',
                 learning_rate: float = 0.0001,
                 **kwargs: Any) -> None:
        """Initialize the LightningModule with a model and loss function.

        Raises:
            ValueError: if kwargs arguments are invalid
        """
        super().__init__()
        self.model = self.configure_model(model=model, model_params=model_params)
        self.loss = self.configure_loss(loss=loss)
        self.train_metrics, self.val_metrics, self.test_metrics = self.configure_metrics()
        # Creates `self.hparams` from kwargs
        self.save_hyperparameters()  # type: ignore[operator]
        self.hyperparams = cast(Dict[str, Any], self.hparams)
        """"
        if not isinstance(kwargs["ignore_index"], (int, type(None))):
            raise ValueError("ignore_index must be an int or None")
        if (kwargs["ignore_index"] is not None) and (kwargs["loss"] == "jaccard"):
            warnings.warn(
                "ignore_index has no effect on training when loss='jaccard'",
                UserWarning,
            )
        self.ignore_index = kwargs["ignore_index"]
        """

    def forward(self, *args: Any, **kwargs: Any) -> Any:
        """Forward pass of the model.
        Args:
            x: tensor of data to run through the model
        Returns:
            output from the model
        """
        return self.model(*args, **kwargs)

    def training_step(self, *args: Any, **kwargs: Any) -> Tensor:
        """Compute and return the training loss.
        Args:
            batch: the output of your DataLoader
        Returns:
            training loss
        """
        batch = args[0]
        x = batch["image"]
        y = batch["mask"]
        y_hat = self(x)
        y_hat_hard = y_hat.argmax(dim=1)
        loss = self.loss(y_hat, y)
        # by default, the train step logs every `log_every_n_steps` steps where
        # `log_every_n_steps` is a parameter to the `Trainer` object
        self.log("train_loss", loss, on_step=True, on_epoch=False)
        self.train_metrics(y_hat_hard, y)
        return cast(Tensor, loss)

    def training_epoch_end(self, outputs: Any) -> None:
        """Logs epoch level training metrics.

        Parameters
        ----------
        outputs: list of items returned by training_step

        Returns
        -------

        """

        self.log_dict(self.train_metrics.compute())
        self.train_metrics.reset()

    def validation_step(self, *args: Any, **kwargs: Any) -> None:
        """Compute validation loss and log example predictions.
        Args:
            batch: the output of your DataLoader
            batch_idx: the index of this batch
        """
        batch = args[0]
        batch_idx = args[1]
        x = batch["image"]
        y = batch["mask"]
        y_hat = self(x)
        y_hat_hard = y_hat.argmax(dim=1)
        loss = self.loss(y_hat, y)
        self.log("val_loss", loss, on_step=False, on_epoch=True)
        self.val_metrics(y_hat_hard, y)
        """
        if batch_idx < 10:
            try:
                datamodule = self.trainer.datamodule  # type: ignore[attr-defined]
                batch["prediction"] = y_hat_hard
                for key in ["image", "mask", "prediction"]:
                    batch[key] = batch[key].cpu()
                sample = batch[0]
                fig = datamodule.plot(sample)
                summary_writer = self.logger.experiment  # type: ignore[union-attr]
                summary_writer.add_figure(
                    f"image/{batch_idx}", fig, global_step=self.global_step
                )
                plt.close()
            except AttributeError:
                pass
        """

    def validation_epoch_end(self, outputs: Any) -> None:
        """Logs epoch level validation metrics.
        Args:
            outputs: list of items returned by validation_step
        """
        self.log_dict(self.val_metrics.compute())
        self.val_metrics.reset()

    def test_step(self, *args: Any, **kwargs: Any) -> None:
        """Compute test loss.
        Args:
            batch: the output of your DataLoader
        """
        batch = args[0]
        x = batch["image"]
        y = batch["mask"]
        y_hat = self(x)
        y_hat_hard = y_hat.argmax(dim=1)
        loss = self.loss(y_hat, y)
        # by default, the test and validation steps only log per *epoch*
        self.log("test_loss", loss, on_step=False, on_epoch=True)
        self.test_metrics(y_hat_hard, y)

    def test_epoch_end(self, outputs: Any) -> None:
        """Logs epoch level test metrics.
        Args:
            outputs: list of items returned by test_step
        """
        self.log_dict(self.test_metrics.compute())
        self.test_metrics.reset()

    def configure_optimizers(self) -> Dict[str, Any]:
        """Initialize the optimizer and learning rate scheduler.
        Returns:
            a "lr dict" according to the pytorch lightning documentation --
            https://pytorch-lightning.readthedocs.io/en/latest/common/lightning_module.html#configure-optimizers
        """
        optimizer = torch.optim.Adam(
            self.model.parameters(), lr=self.lr
        )
        return {
            "optimizer": optimizer,
            "lr_scheduler": {
                "scheduler": ReduceLROnPlateau(
                    optimizer,
                    patience=self.hyperparams["learning_rate_schedule_patience"],
                ),
                "monitor": "val_loss",
            },
        }
