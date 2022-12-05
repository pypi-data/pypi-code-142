from abc import ABC

import numpy as np
import tensorflow as tf

from mlc.models.model import Model


class TfModel(Model, ABC):
    def load(self, path):
        self.model = tf.keras.models.load_model(path)

    def save(self, path):
        self.model.save(path)

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        """
        Only implemented for binary / multi-class-classification tasks.
        Returns the probability distribution over the classes C.
        (Save probabilities to self.prediction_probabilities)

        :param x: test data
        :return: probabilities for the classes (Shape N x C)
        """

        prediction_probabilities = self.model.predict(x)

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
