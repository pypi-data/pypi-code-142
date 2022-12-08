import numpy as np
from inspect import signature

from src.autodiffpypi.base_derivatives import *
from src.autodiffpypi.dual_number import *

class Forward():
    def __init__(self, fn, num_of_inputs):
        """ Initialize Forward mode class

        Params:
            self: Forward
            fn: array, function: () -> DualNumber
        """
        if isinstance(fn, list):
            if len(fn) == 0:
                raise ValueError("Input to Forward class should be a function or a non-empty list of functions")
            for elt in fn:
                if not callable(elt):
                    raise ValueError("Input to Forward class should be a function or a non-empty list of functions")
            self.fn = np.array(fn)
        elif callable(fn):
            self.fn = np.array([fn])
        else:
            raise ValueError("Input to Forward class should be a function or a non-empty list of functions")
        self.num_of_inputs = num_of_inputs


    def evaluate(self, *args):
        """ Negate self
        Params:
            self: Forward

        Returns:
            value: int

        Example:
        >>> x = 2
        >>> f1 = lambda x: x ** 2
        >>> Forward(f1, 1).evaluate(x)
        4
        """

        # Check for number of inputs match
        if len(args) != self.num_of_inputs:
            raise ValueError("User must input values to find the derivative of the function")

        # Convert to dual
        duals = [DualNumber(x) for x in args]

        # Multiple functions
        if len(self.fn) > 1:
            return np.array([np.array([fun(*duals).real]) for fun in self.fn])
        # Single function
        else:
            return self.fn[0](*duals).real


    def derivative(self, index, *args):
        """ Compute derivative
        Params:
            self: Forward

        Returns:
            derivative: float

        Example:
        >>> x = 1
        >>> f1 = lambda x: x ** 2
        >>> Forward(f1, 1).derivative(x)
        2
        """

        # Check for number of inputs match
        if len(args) > self.num_of_inputs:
            raise ValueError("User must input values to find the derivative of the function")

        if len(args) == 0 and self.num_of_inputs == 1:
            args = [index]
            index = 0

        if len(self.fn) > 1:
            lst = self.jacobian(*args)[:, index]
            return np.array([[elt] for elt in lst])
        else:
            return self.jacobian(*args)[0][index]


    def jacobian(self, *args):
        """ Compute jacobian matrix of derivatives
        Params:
            self: Forward

        Returns:
            jacobian: np.array

        Example:
        >>> x = DualNumber(2,1)
        >>> f = lambda x : x ** 2
        >>> Forward(f, 1).jacobian()
        [4.0]
        """

        # Check for number of inputs match
        if len(args) != self.num_of_inputs:
            raise ValueError("User must input values to find the derivative of the function")

        duals_list = []
        # Convert to dual
        for ind in range(len(args)):
            lst = [DualNumber(x, 0.0) for x in args]
            lst[ind].dual = 1.0
            duals_list.append(lst)
        
        # Per function, we want to have a numpy list
        res = []
        for fun in self.fn:
            arr = []
            for ind, duals in enumerate(duals_list):
                fun_params = len(signature(fun).parameters)
                if len(duals) > fun_params:
                    arr.append(fun(*duals[0:fun_params]).dual)
                else:
                    arr.append(fun(*duals).dual)
            res.append(np.array(arr))
        return np.array(res)


x = 2
f = lambda x : x ** 2
j = Forward(f, 1).jacobian(x)
print(j)