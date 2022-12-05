import numpy as np
import scipy.special

from ..typed import Model


class Beta(Model):
    @staticmethod
    def forward(t: float | np.ndarray, a: float, b: float) -> float | np.ndarray:
        u = t ** (a - 1) * (1 - t) ** (b - 1) / scipy.special.beta(a, b)
        if isinstance(u, np.ndarray):
            u[~np.isnan(u)] = 0
        else:
            u = 0 if np.isnan(u) else u
        return u
