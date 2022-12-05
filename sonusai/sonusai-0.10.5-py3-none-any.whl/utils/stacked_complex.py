import numpy as np


def stack_complex(unstacked: np.ndarray) -> np.ndarray:
    """ Stack a complex array

    The input is an nD array (n > 1) containing complex data.

    Returns a stacked array where the last dimension is double the input last dimension:
        * first half is all the real data
        * second half is all the imaginary data

    """
    assert unstacked.ndim > 1

    shape = list(unstacked.shape)
    shape[-1] = shape[-1] * 2
    stacked = np.empty(shape, dtype=np.complex64)
    half = unstacked.shape[-1]
    stacked[..., :half] = np.real(unstacked)
    stacked[..., half:] = np.imag(unstacked)

    return stacked


def unstack_complex(stacked: np.ndarray) -> np.ndarray:
    """ Unstack a stacked complex array

    The input is an nD array (n > 1) where the last dimension contains stacked complex data:
        * first half is all the real data
        * second half is all the imaginary data

    Returns an unstacked complex array.

    """
    assert stacked.ndim > 1
    assert stacked.shape[-1] % 2 == 0

    half = stacked.shape[-1] // 2
    unstacked = 1j * stacked[..., half:]
    unstacked += stacked[..., :half]

    return unstacked


def stacked_complex_real(stacked: np.ndarray) -> np.ndarray:
    """ Get the real elements from a stacked complex array

    """
    assert stacked.ndim > 1
    assert stacked.shape[-1] % 2 == 0

    half = stacked.shape[-1] // 2
    return stacked[..., :half]


def stacked_complex_imag(stacked: np.ndarray) -> np.ndarray:
    """ Get the imaginary elements from a stacked complex array

    """
    assert stacked.ndim > 1
    assert stacked.shape[-1] % 2 == 0

    half = stacked.shape[-1] // 2
    return stacked[..., half:]
