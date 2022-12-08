from torch import tensor, Tensor
from numpy import ndarray
from typing import Union, List


class TorchModel:
    def __init__(self, model):
        self.model = model

    def predict(self, input: Union[Tensor, ndarray, List]) -> list:
        if not isinstance(input, Tensor):
            input = tensor(input)
        return self.model(input)
