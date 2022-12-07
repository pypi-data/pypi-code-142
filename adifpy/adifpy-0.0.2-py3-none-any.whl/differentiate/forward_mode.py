import numpy as np

from Adifpy.differentiate.dual_number import DualNumber
from Adifpy.differentiate.helpers import isscalar


def forward_mode(func, pt, seed_vector):
    """Compute the value and directional derivative at a point, for a given function.

    Forward mode AD calculates the derivative of a function at point
    with respect to some seed vector, at machine precision.

    Args:
        func (Callable): the function on which to evaluate
        pt (float | ndarray): the point at which to evaluate
        seed_vector (ndarray): the direction in which to evaluate
          defaults to 1 when the function's input space is R

    Returns:
        If the function's output space is R, a tuple of the value and directional derivative
        Otherwise, a tuple of two lists: the values and directional derivatives for each component

    >>> f = lambda x: x**2 + 3*x
    >>> forward_mode(f, 1, seed_vector=1)
    (4, 5)
    >>> f = lambda x: [np.sin(x[0]), np.cos(x[1])]

    NOTE: We expect a -0.0 here, since the derivative of cos is -sin
    >>> forward_mode(f, [0, 0], [1, 0])
    ([0.0, 1.0], [1.0, -0.0])
    """

    if isinstance(seed_vector, np.ndarray) or type(seed_vector) == list:
        # Create a list of dual numbers to pass through the function
        array_pt = np.array([DualNumber(p, seed) for p, seed in zip(pt, seed_vector)])
        passed = func(array_pt)
    else:
        passed = func(DualNumber(pt, seed_vector))

    if isscalar(passed):
        return (passed, 0)
    elif isinstance(passed, DualNumber):
        return (passed.real, passed.dual)
    else:
        # Some outputs may be scalars (for functions that map to constants)
        reals = [d if not isinstance(d, DualNumber) else d.real for d in passed]
        duals = [0 if not isinstance(d, DualNumber) else d.dual for d in passed]

        return reals, duals
