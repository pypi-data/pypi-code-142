import numpy as np

from .typed import Model


class Polynomial(Model):
    @staticmethod
    def cdf(t: float | np.ndarray, a: float, b: float, c: float) -> float | np.ndarray:
        return a * t**3 + b * t**2 + c * t

    @staticmethod
    def pdf(t: float | np.ndarray, a: float, b: float, c: float) -> float | np.ndarray:
        return 3 * a * t**2 + 2 * b * t + c
