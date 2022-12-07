import torch
import torch.nn.functional as F
import torchvision.models.resnet as resnet
import torchvision.models.densenet as densenet
from abc import ABCMeta, abstractmethod
from typing import Union
from torch.utils.data import DataLoader
from ailca.core.env import *
from ailca.core.sys import is_gpu_runnable
from ailca.ml.base import PyTorchModel
from ailca.data.base import Dataset


class CNN(PyTorchModel):
    @abstractmethod
    def __init__(self,
                 alg_id: str,
                 dim_out: int):
        super(CNN, self).__init__(alg_id)
        self._dim_out = dim_out

        self._model_info = {
            'alg_id': self.alg_id,
            'alg_name': self.alg_name,
            'alg_src': self.alg_src,
            'dim_out': self.dim_out
        }

    def fit(self,
            data_loader: DataLoader,
            optimizer: torch.optim.Optimizer,
            loss_func: torch.nn.Module):
        """
        Optimize the model parameters of the prediction model to minimize the given ``loss_func``.

        :param data_loader: (*DataLoader*) A data loader object for generating mini-batches from the training dataset.
        :param optimizer: (*torch.optim.Optimizer*) An optimization algorithm to fit the model parameters.
        :param loss_func: (*torch.nn.Module*) A loss function to fit the model parameters.
        """

        # Initialize training loss.
        train_loss = 0

        # Set the model to the training mode.
        self.train()

        # Train the machine learning model for each mini-batch.
        for x, y in data_loader:
            # Move the data from CPU to GPU if GPU is runnable.
            if is_gpu_runnable():
                x = x.cuda()
                y = y.cuda()

            # Predict target values for the input data.
            y_p = self(x)

            # Calculate the training loss for the mini-batch.
            loss = loss_func(y_p, y)

            # Optimize the model parameters.
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Accumulate the training loss.
            train_loss += loss.item()

        return train_loss / len(data_loader)

    def predict(self,
                x: Union[torch.Tensor, Dataset]) -> torch.Tensor:
        """
        Predict the target values for the input data ``x``.

        :param x: (*Union[torch.Tensor, Dataset]*) A single input or dataset object containing multiple inputs.
        :return: (*torch.Tensor*) Predicted values for the input dataset.
        """

        # Set the model to the evaluation model.
        self.eval()

        # Take actual input data.
        if isinstance(x, torch.Tensor):
            # Predict target value for single input data.
            with torch.no_grad():
                if is_gpu_runnable():
                    return self(torch.stack([x, x]).cuda()).cpu()[0].view(1, -1)
                else:
                    return self(torch.stack([x, x])).cpu()[0].view(1, -1)

        else:
            # Predict target values for a set of input data.
            with torch.no_grad():
                if is_gpu_runnable():
                    return self(x.x.cuda()).cpu()
                else:
                    return self(x.x).cpu()


class ResNet(CNN, resnet.ResNet, metaclass=ABCMeta):
    def forward(self,
                x: torch.Tensor) -> torch.Tensor:
        """
        Execute the forward process of the prediction model.

        :param x: (*torch.Tensor*) Input data of the model.
        :return: (*torch.Tensor*) Output of the model for the input data.
        """

        return self._forward_impl(x)


class ResNet18(ResNet):
    def __init__(self, dim_out, **kwargs):
        CNN.__init__(self, ALG_RESNET18, dim_out)
        resnet.ResNet.__init__(self, resnet.BasicBlock, [2, 2, 2, 2], num_classes=dim_out, **kwargs)


class ResNet34(ResNet):
    def __init__(self, dim_out, **kwargs):
        CNN.__init__(self, ALG_RESNET34, dim_out)
        resnet.ResNet.__init__(self, resnet.BasicBlock, [3, 4, 6, 3], num_classes=dim_out, **kwargs)


class ResNet101(ResNet):
    def __init__(self, dim_out, **kwargs):
        CNN.__init__(self, ALG_RESNET101, dim_out)
        resnet.ResNet.__init__(self, resnet.BasicBlock, [3, 4, 23, 3], num_classes=dim_out, **kwargs)


class DenseNet(CNN, densenet.DenseNet, metaclass=ABCMeta):
    def forward(self,
                x: torch.Tensor) -> torch.Tensor:
        """
        Execute the forward process of the prediction model.

        :param x: (*torch.Tensor*) Input data of the model.
        :return: (*torch.Tensor*) Output of the model for the input data.
        """

        features = self.features(x)
        out = F.relu(features, inplace=True)
        out = F.adaptive_avg_pool2d(out, (1, 1))
        out = torch.flatten(out, 1)
        out = self.classifier(out)

        return out


class DenseNet121(DenseNet):
    def __init__(self, dim_out, **kwargs):
        CNN.__init__(self, ALG_DENSENET121, dim_out)
        densenet.DenseNet.__init__(self, 32, (6, 12, 24, 16), 64, num_classes=dim_out, **kwargs)
