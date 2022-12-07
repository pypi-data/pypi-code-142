"""
Measurements
"""

from typing import List, Tuple

from numpy import uint64

def measurement_creator(
    qidx: int,
    offset: int = 0,
    status: int = 0,
    value: int = 0
) -> uint64:
    """Helper function to pack data into a 64-bit HAL measurement status result.
    Converts this:
    (QUBIT_INDEX, STATUS, VALUE)
    to this:
    QUBIT INDEX [63-52] | OFFSET [51-12] | STATUS [11-7] | PADDING [6-1] | VALUE [0]

    Parameters
    ----------
    qidx : int
        Qubit index.
    offset : int, optional
        index offset, by default 0.
    status : int, optional
        Status code, by default 0.
    value : int, optional
        Measurement value, by default 0.

    Returns
    -------
    unit64
        64-bit measurement status from HAL.
    """

    return qidx << 52 | offset << 12 | status << 7 | value


def measurement_unpacker(bitcode: uint64) -> Tuple[int, int, int, int]:
    """Helper function to decode 64-bit measurement status result from HAL.
    Converts this:
    QUBIT INDEX [63-52] | OFFSET [51-12] | STATUS [11-7] | PADDING [6-1] | VALUE [0]
    to this:
    (QUBIT_INDEX, OFFSET, STATUS, VALUE)

    Parameters
    ----------
    bitcode : uint64
        64-bit measurement status from HAL.
    Returns
    -------
    Tuple[int, int, int, int]
        Tuple of decoded qubit index, index offset, status, and readout value.
    """

    return (
        (bitcode >> 52),
        (bitcode >> 12) & 1023,
        (bitcode & 3968) >> 7,
        bitcode & 1
    )
