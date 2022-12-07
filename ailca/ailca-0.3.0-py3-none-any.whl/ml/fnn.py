"""
Feedforward Neural Networks
---------------------------
The ``ailca.ml.fnn`` module provides an implementation of the most essential feedforward neural network.
The algorithms in this module are used to predict target values from the feature vectors and the chemical formulas.
"""


import torch.utils.data
import torch.nn as nn
from typing import Union
from torch.utils.data import DataLoader
from ailca.core.sys import *
from ailca.data.base import Dataset
from ailca.ml.base import PyTorchModel
from ailca.ml.nn import *


class FCLayer(Layer):
    def __init__(self,
                 dim_in: int,
                 dim_out: int,
                 batch_norm: bool = False,
                 act_func: str = None):
        super(FCLayer, self).__init__()
        self._modules.append(nn.Linear(dim_in, dim_out))
        self._dim_in = dim_in
        self._dim_out = dim_out
        self._batch_norm = batch_norm
        self._act_func = act_func

        # Construct a batch normalization layer.
        if batch_norm:
            self._modules.append(nn.BatchNorm1d(dim_out))

        # Apply an activation function.
        if act_func is not None:
            self._modules.append(get_act_func(act_func))

    @property
    def dim_in(self):
        return self._dim_in

    @property
    def batch_norm(self):
        return self._batch_norm

    @property
    def act_func(self):
        return self._act_func


class FNN(PyTorchModel):
    """
    A base class of feedforward neural networks.
    """

    @abstractmethod
    def __init__(self,
                 alg_id: str,
                 layers: list):
        super(FNN, self).__init__(alg_id)
        self._layers = layers_to_sequential(layers)
        self._dim_out = layers[-1].dim_out

        layer_info = list()
        for layer in layers:
            layer_info.append({'dim_in': layer.dim_in,
                               'dim_out': layer.dim_out,
                               'batch_norm': layer.batch_norm,
                               'act_func': layer.act_func})

        self._model_info = {
            'alg_id': self.alg_id,
            'alg_name': self.alg_name,
            'alg_src': self.alg_src,
            'layers': layer_info,
            'dim_out': self.dim_out
        }

    @abstractmethod
    def forward(self,
                x: object) -> torch.Tensor:
        """
        Execute the forward process of the prediction model.

        :param x: (*object*) Input data of the model.
        :return: (*torch.Tensor*) Output of the model for the input data.
        """

        pass

    def fit(self,
            data_loader: DataLoader,
            optimizer: torch.optim.Optimizer,
            loss_func: torch.nn.Module) -> float:
        """
        Optimize the model parameters of the prediction model to minimize the given ``loss_func``.

        :param data_loader: (*DataLoader*) A data loader object for generating mini-batches from the training dataset.
        :param optimizer: (*torch.optim.Optimizer*) An optimization algorithm to fit the model parameters.
        :param loss_func: (*torch.nn.Module*) A loss function to fit the model parameters.
        :return: (*float*) Training loss.
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


class FCNN(FNN):
    """
    A neural network to predict target values from vector- or matrix-shaped input data.
    It is trained to minimize the prediction errors that is usually defined as a distance metric
    between the true and predicted target values.
    """

    def __init__(self,
                 layers: list = None,
                 dim_in: int = None,
                 dim_out: int = None):
        if layers is None:
            if dim_in is None or dim_out is None:
                raise AssertionError('For auto-configuration, dimensionalities of the input and target'
                                     'data must be provided by \'dim_in\' and \'dim_out\'.')
            layers = [
                FCLayer(dim_in, 256, batch_norm=True, act_func=ACT_FUNC_RELU),
                FCLayer(256, 256, batch_norm=True, act_func=ACT_FUNC_RELU),
                FCLayer(256, dim_out)
            ]

        super(FCNN, self).__init__(ALG_FCNN, layers)

    def forward(self,
                inputs: torch.Tensor):
        """
        A forward process of neural networks.
        For input data in ``data``, it returns predicted target values.

        :param inputs: (*torch.Tensor*) Input data of the model.
        :return: (*numpy.ndarray*) Predicted target values.
        """

        return self._layers(inputs)
