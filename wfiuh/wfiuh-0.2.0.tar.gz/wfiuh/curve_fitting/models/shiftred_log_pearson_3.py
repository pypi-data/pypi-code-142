import numpy as np
import scipy.special

from .typed import Model


class ShiftedLogPearson3(Model):
    @staticmethod
    def pdf(t: float | np.ndarray, a: float, b: float, c: float) -> float | np.ndarray:
        print("test")
        return (
            c**b
            * (np.log(t / a + 1)) ** (b - 1)
            / (a * scipy.special.gamma(b) * (t / a + 1) ** (c + 1))
        )
