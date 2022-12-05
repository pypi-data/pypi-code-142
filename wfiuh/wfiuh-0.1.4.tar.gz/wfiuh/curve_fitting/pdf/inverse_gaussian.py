import numpy as np
import scipy.stats

from ..typed import Model


class InverseGaussian(Model):
    @staticmethod
    def forward(t: float | np.ndarray, a: float, b: float) -> float | np.ndarray:
        return scipy.stats.invgauss.pdf(x=t, mu=b / a, scale=a)
