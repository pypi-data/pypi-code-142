import numpy as np
import scipy.special

from .typed import Model


class Gamma(Model):
    @staticmethod
    def cdf(t: float | np.ndarray, a: float, b: float) -> float | np.ndarray:
        raise NotImplementedError()

    @staticmethod
    def pdf(t: float | np.ndarray, a: float, b: float) -> float | np.ndarray:
        return (t / a) ** (b - 1) * np.exp(-t / a) / (a * scipy.special.gamma(b))
