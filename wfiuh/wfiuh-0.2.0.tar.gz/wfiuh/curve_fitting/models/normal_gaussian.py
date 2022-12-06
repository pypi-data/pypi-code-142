import numpy as np
import scipy.stats

from .typed import Model


class NormalGaussian(Model):
    @staticmethod
    def cdf(t: float | np.ndarray, a: float, b: float) -> float | np.ndarray:
        return scipy.stats.norm.cdf(x=t, loc=a, scale=b)

    @staticmethod
    def pdf(t: float | np.ndarray, a: float, b: float) -> float | np.ndarray:
        return scipy.stats.norm.pdf(x=t, loc=a, scale=b)
