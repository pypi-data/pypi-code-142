import numpy as np


def isscalar(x):
    try:
        float(x)
        return True
    except (ValueError, TypeError):
        return False

def isscalar_or_array(x):
    return isinstance(x, (np.ndarray, list)) or isscalar(x)