import abc
import typing as tp
from abc import ABC

import numpy as np


class Model(ABC):
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.objective = kwargs["objective"]
        self.constructor_kwargs = kwargs
        self.model = None

    def predict(self, x: np.ndarray) -> tp.Tuple[np.ndarray, np.ndarray]:
        """
        Returns the regression value or the concrete classes of binary /
        multi-class-classification tasks.
        (Save predictions to self.predictions)

        :param x: test data
        :return: predicted values / classes of test data (Shape N x 1)
        """

        if self.constructor_kwargs["objective"] == "regression":
            predictions = self.model.predict(x)
        elif (
            self.constructor_kwargs["objective"] == "classification"
            or self.constructor_kwargs["objective"] == "binary"
        ):
            prediction_probabilities = self.predict_proba(x)
            predictions = np.argmax(prediction_probabilities, axis=1)

        return predictions

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        """
        Only implemented for binary / multi-class-classification tasks.
        Returns the probability distribution over the classes C.
        (Save probabilities to self.prediction_probabilities)

        :param x: test data
        :return: probabilities for the classes (Shape N x C)
        """

        prediction_probabilities = self.model.predict_proba(x)

        # If binary task returns only probability for the true class,
        # adapt it to return (N x 2)
        if prediction_probabilities.shape[1] == 1:
            prediction_probabilities = np.concatenate(
                (
                    1 - prediction_probabilities,
                    prediction_probabilities,
                ),
                1,
            )
        return prediction_probabilities

    def fit(
        self,
        x: np.ndarray,
        y: np.ndarray,
        x_val: tp.Union[None, np.ndarray] = None,
        y_val: tp.Union[None, np.ndarray] = None,
    ):
        self.model.fit(x, y)

    def clone(self):
        return self.__class__(**self.constructor_kwargs)

    @abc.abstractmethod
    def load(self, path):
        pass

    @abc.abstractmethod
    def save(self, path):
        pass
