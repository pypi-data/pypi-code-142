from abc import abstractmethod

import numpy as np


class Metric:
    @abstractmethod
    def compute(self, y_true: np.ndarray, y_score: np.ndarray) -> np.ndarray:
        pass
