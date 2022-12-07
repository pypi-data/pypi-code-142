import torch
from abc import ABC
from abc import abstractmethod
from ailca.core.env import *


class Layer(ABC):
    """
    An abstract class to implement the network layers of the neural networks.
    """

    @abstractmethod
    def __init__(self):
        self._modules = list()
        self._dim_out = None

    @property
    def dim_out(self):
        return self._dim_out

    def tolist(self) -> list:
        return self._modules


def get_act_func(name_act_func: str) -> torch.nn.Module:
    """
    Generate an object of the activation function.
    It returns a ``torch.module.Module`` object of the activation functions.

    :param name_act_func: (*str*) A name of the activation function.
    :return: (*torch.nn.Module*) An object of the activation function.
    """

    if name_act_func == ACT_FUNC_SIGMOID:
        return torch.nn.Sigmoid()
    elif name_act_func == ACT_FUNC_TANH:
        return torch.nn.Tanh()
    elif name_act_func == ACT_FUNC_RELU:
        return torch.nn.ReLU()
    elif name_act_func == ACT_FUNC_SOFTPLUS:
        return torch.nn.Softplus()
    elif name_act_func == ACT_FUNC_PRELU:
        return torch.nn.PReLU()
    else:
        raise AssertionError('Unexpected type of the activation function: \'{}\'.'.format(name_act_func))


def layers_to_sequential(list_layers: list) -> torch.nn.Sequential:
    """
    Convert a list of the neural network layers into a ``torch.nn.Sequential`` object to construct ``PyTorchModel``.
    The list of layers must be converted into the ``torch.nn.Sequential`` objects by this function
    to fit their parameters based on PyTorch.

    :param list_layers: (*list*) A list of the neural network layers.
    :return: (*torch.nn.Sequential*) A trainable object of the layers.
    """

    listed_layers = list()

    for layer in list_layers:
        for module in layer.tolist():
            listed_layers.append(module)

    return torch.nn.Sequential(*listed_layers)
