import numpy as np

from ..typed import Model


class Polynomial(Model):
    @staticmethod
    def forward(
        t: float | np.ndarray, a: float, b: float, c: float
    ) -> float | np.ndarray:
        return 3 * a * t**2 + 2 * b * t + c
