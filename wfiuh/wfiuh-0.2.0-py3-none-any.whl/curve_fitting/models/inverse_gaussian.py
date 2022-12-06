import numpy as np
import scipy.stats

from .typed import Model


class InverseGaussian(Model):
    @staticmethod
    def cdf(t: float | np.ndarray, a: float, b: float) -> float | np.ndarray:
        return scipy.stats.invgauss.cdf(x=t, mu=b / a, scale=a)

    @staticmethod
    def pdf(t: float | np.ndarray, a: float, b: float) -> float | np.ndarray:
        return scipy.stats.invgauss.pdf(x=t, mu=b / a, scale=a)
