import numpy as np
import scipy.special
import scipy.stats

from ..typed import Model


class NormalGaussian(Model):
    @staticmethod
    def forward(t: float | np.ndarray, a: float, b: float) -> float | np.ndarray:
        return scipy.stats.norm.pdf(x=t, loc=a, scale=b)
