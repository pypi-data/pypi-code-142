"""Automatic Differentiation object"""

from typing import Callable

import numpy as np

from Adifpy.differentiate.forward_mode import forward_mode
from Adifpy.differentiate.reverse_mode import reverse_mode
from Adifpy.differentiate.helpers import isscalar_or_array, isscalar


class Evaluator:
    """AD evaluation object

    >>> my_evaluator = Evaluator(lambda x: x * x)
    >>> my_evaluator(1)
    (1, 2)
    >>> my_evaluator(3)
    (9, 6)
    """

    def __init__(self, fn: Callable):
        self.fn = fn

        self.input_dim = None
        self.output_dim = None

    def __call__(self, pt, **kwargs):
        """Perform AD on this Evaluator's function, at this point

        Args:
            pt (float | iterable): the point or vector at which to evaluate the function
            seed_vector (iterable, optional): the seed vector, if the function has vector input
            force_mode (str, optional): either 'forward' or 'reverse' for forcing AD mode

        Returns:
            If the function's output space is R, a tuple of the value and directional derivative.
            Otherwise, a tuple of two lists: the values and directional derivatives for each component
        """
        if isinstance(pt, list):
            pt = np.array(pt)

        # Ensure the evaluation point is valid
        if not isscalar_or_array(pt):
            raise TypeError(f'Evaluation point must be a scalar or NumPy array, not {type(pt)}.')

        shape = np.shape(pt)
        pt_shape = 1 if shape == () else shape[0]

        if self.input_dim is None:
            self.input_dim = pt_shape
        elif self.input_dim != pt_shape:
            print(f'WARNING: Expected point in R{self.input_dim}, but got point in R{pt_shape}')

        # Ensure that a seed vector is provided for vector functions
        if self.input_dim > 1 and 'seed_vector' not in kwargs:
            raise AttributeError('For vector functions, `seed_vector` argument is required')
        elif 'seed_vector' not in kwargs:
            # Set the default seed vector for functions that map from R
            kwargs['seed_vector'] = 1
        elif self.input_dim > 1:
            # Ensure the seed vector is valid (and throw an error if it is not)
            kwargs['seed_vector'] = np.array(kwargs['seed_vector'])
        else:
            self.input_dim = None
            raise TypeError('seed_vector argument should not be provided for functions from R -> R')

        # Ensure the seed vector is of the expected dimensionality
        shape = np.shape(kwargs['seed_vector'])
        seed_dim = 1 if shape == () else shape[0]
        assert seed_dim == self.input_dim, \
            f'Evaluation point has {self.input_dim} dimensions, but seed vector has {seed_dim} dimensions'

        # Set the output dimension (and ensure the function is valid)
        try:
            fn_output = self.fn(pt)

            if not isscalar_or_array(fn_output):
                print(type(fn_output), fn_output)
                raise TypeError('Output must not be None')

            self.output_dim = 1 if isscalar(fn_output) else len(fn_output)
        except Exception as error:
            raise RuntimeError('Evaluator function failed') from error

        # Decide which AD mode to use, either depending on forced user input or optimized for performance
        differentiator = forward_mode
        if 'force_mode' in kwargs:
            match kwargs['force_mode']:
                case 'forward':
                    differentiator = forward_mode
                case 'reverse':
                    if self.input_dim != 1:
                        raise NotImplementedError('Reverse mode only supports functions from R -> R')
                    differentiator = reverse_mode
                case _:
                    raise ValueError('`force_mode` argument must be either `forward` or `reverse`')

        return differentiator(func=self.fn, pt=pt, seed_vector=kwargs['seed_vector'])
