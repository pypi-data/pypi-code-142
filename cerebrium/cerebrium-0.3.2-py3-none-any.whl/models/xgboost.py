from xgboost import XGBClassifier, XGBRegressor
from torch import Tensor
from numpy import atleast_2d, ndarray
from typing import Union, List


class XGBClassfierModel:
    def __init__(self, model):
        self.model = model

    def predict(self, input: Union[Tensor, ndarray, List]) -> list:
        if not isinstance(input, ndarray):
            if isinstance(input, Tensor):
                input = input.detach().cpu().numpy()
            input = atleast_2d(input)
        return self.model.predict_proba(input)
