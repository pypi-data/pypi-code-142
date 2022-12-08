#!/usr/bin/env python3
# File       : reverse_mode.py
# Description: Computes Reverse AD

import numpy as np

from src.autodiffpypi.base_derivatives import *
from src.structures.graph import Node

class Reverse():

    # def __init__(self, fn, nodes):
    def __init__(self, fn, num_inputs):
        """ Initialize Reverse mode class

        Params:
            self: Reverse
            fn: array, function: () -> Node
            num_inputs: number of inputs
        """
        self.fn = np.array(fn) if isinstance(fn, list) else np.array([fn])
        self.num_inputs = num_inputs
    
    def build_nodes(self, inputs):
        """ Helper function to build node variables
        Params:
            self: Reverse
            inputs: List of integers

        Returns:
            value: List of nodes

        Example:
        >>> x = 2
        >>> y = 5
        >>> def f1(x, y):
        >>>     return x ** y
        >>> def f2(x, y):
        >>>     return x + y
        >>> reverse_ex = Reverse([f1, f2], 2)
        >>> value = reverse_ex.build_nodes()
        >>> print(value)
        [Node(2), Node(5)]
        """
        if len(inputs) != self.num_inputs:
            raise IndexError

        # build nodes out of input variables
        node_list = []
        for var in inputs:
            node_list.append(Node(var))
        
        return node_list

    def evaluate(self, inputs):
        """ Evaluate input functions
        Params:
            self: Reverse
            inputs: List of integers

        Returns:
            value: List of integers

        Example:
        >>> x = 2
        >>> y = 5
        >>> def f1(x, y):
        >>>     return x ** y
        >>> def f2(x, y):
        >>>     return x + y
        >>> reverse_ex = Reverse([f1, f2], 2)
        >>> value = reverse_ex.evaluate([x, y])
        >>> print(value)
        [32, 7]
        """
        # build nodes out of input variables
        node_list = self.build_nodes(inputs)

        # evaluate all functions at those variables
        res_arr = []
        for func in self.fn:
            res_arr.append(func(*node_list).value)

        return res_arr

    def derivative(self, inputs, index = None):
        """ Compute derivative
        Params:
            self: Reverse
            inputs: List of integers
            index: Integer

        Returns:
            derivative: List of integers

        Example:
        >>> x = 2
        >>> y = 5
        >>> def f1(x, y):
        >>>     return x ** y
        >>> def f2(x, y):
        >>>     return x + y
        >>> reverse_ex = Reverse([f1, f2], 2)
        >>> value = reverse_ex.derivative([x, y], 2)
        >>> print(value)
        [32log(2), 1]
        """
        if type(inputs) == int:
            inputs = [inputs]

        if len(inputs) == 1 and index is None:
            index = 1

        # build jacobian
        jacobian = np.array(self.jacobian(inputs))
        # get specified column
        return jacobian[:, index - 1]

    def jacobian(self, inputs):
        """ Compute jacobian matrix of derivatives
        Params:
            self: Reverse

        Returns:
            jacobian: List of ints

        Example:
        >>> x = 2
        >>> y = 3
        >>> def f1(x, y):
        >>>     return x ** y
        >>> def f2(x, y):
        >>>     return x + y
        >>> reverse_ex = Reverse([f1, f2], 2)
        >>> value = reverse_ex.jacobian([x, y])
        >>> print(value)
        [ [12, 8log(2)], [1, 1] ]
        """
        # build nodes out of input variables
        node_list = self.build_nodes(inputs)

        m = []
        for func in self.fn:
            row = []
            for node in node_list:
                row.append(func(*node_list).get_gradients()[node])
            m.append(row)
        return m