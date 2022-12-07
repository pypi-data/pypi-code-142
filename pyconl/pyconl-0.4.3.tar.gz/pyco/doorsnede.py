from typing import Union
import math

#import numpy as np
#import matplotlib.pyplot as plt

import pyco.model as pycom

class Doorsnede(pycom.BasisObject):
    """Betreft een samenstelling van vormen met materiaaleigenschappen.

    AANMAKEN DOORSNEDE
        d1 = Doorsnede(Lijn)            invoeren van vorm objecten

    """

    AFRONDEN_NAAR_NUL = 1e-13

    def __init__(self, onderdelen:dict):
        super().__init__()

    def _float(self, waarde):
        """Zet object om naar een float en rond hele kleine waarden af naar nul."""
        f = float(waarde)
        if f > -1*self.AFRONDEN_NAAR_NUL and f < 1*self.AFRONDEN_NAAR_NUL:
            f = 0.0
        return f


if __name__ == '__main__':
    pass
