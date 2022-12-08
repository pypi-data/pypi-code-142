#!/usr/bin/env python3
# File       : graph.py
# Description: Node Class for Reverse AD

from collections import defaultdict
from itertools import count
import numpy as np

class Node:
    _supported_types = (int, float)

    def __init__(self, value, parent_gradients = [], name = "", derivative = 1):
        """ Initialize Node class

        Params:
            self: Node
            value: int or float
            parent_gradients: array of tuples
                type: (Node parent_node, int local_gradient)
                    parent_node is a parent node of self
                    local_gradient is the derivative of self with respect to parent_node
            derivate: int or float
                default: 1

        """
        if not isinstance(value, (*self._supported_types, Node)):
            raise TypeError(f"Type error: `{type(value)}`")

        self.value = value
        self.derivative = derivative
        self.parent_gradients = parent_gradients
        self.name = name
    
    def __repr__(self):
        return (f"(Node name: {self.name}, value: {self.value}, parent gradients: {self.parent_gradients}, derivative: {self.derivative})")

    def __hash__(self):
        return hash((self.value, self.derivative, str(self.parent_gradients)))

    def get_gradients(self):
        """ Return derivatives of self with respect to parent nodes
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Dictionary of Nodes

        Example:
        >>> x = Node(2)
        >>> y = Node(5)
        >>> f = x ** y
        >>> x_deriv = f.get_gradients()[x]
        >>> print(x_deriv)
        3   
        >>> y_deriv = f.get_gradients()[y]
        >>> print(y_deriv)
        5

        """        
        # dictionary that lets us hash Nodes
        gradient_list = defaultdict(lambda: 0)

        # recursively calculate gradients
        def calc_grads(node, weight):

            for parent, gradient in node.parent_gradients:
                path_value = weight * gradient
                if parent is None:
                    return
                else:
                    gradient_list[parent] += path_value
                calc_grads(parent, path_value)
        
        calc_grads(self, weight = 1)

        return gradient_list

    def __neg__(self):
        """ Negate node's value
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(2)
        >>> node1 = -node1
        >>> print(node1.value)
        -2
        """
        return Node(-self.value, [(self, -1)])

    def __add__(self, x):
        """ Add node and input node / int / float
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(2)
        >>> node2 = Node(3)
        >>> y = node1 + node2
        >>> print(y)
        Node(5)
        """
        if type(x) == Node:
            node_sum = Node(self.value + x.value, [(self, 1), (x, 1)])
        elif type(x) == float or type(x) == int:
            node_sum = Node(self.value + x, [(self, 1)])
        else:
            raise TypeError
        
        return node_sum

    def __radd__(self, x):
        """ Add node and input node / int / float
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(2)
        >>> node2 = Node(5)
        >>> y = node2 + node1
        >>> print(y)
        Node(7)
        """
        return self.__add__(x)

    def __sub__(self, x):
        """ Subtract node by input node / int / float
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(5)
        >>> node2 = Node(2)
        >>> y = node1 - node2
        >>> print(y)
        Node(3)
        """
        if type(x) == Node:
            node_diff = Node(self.value - x.value, [(self, 1), (x, -1)])
        elif type(x) == float or type(x) == int:
            node_diff = Node(self.value - x, [(self, 1)])
        else:
            raise TypeError
                
        return node_diff
    
    def __rsub__(self, x):
        """ Subtract node by input node / int / float
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(4)
        >>> int1 = 2
        >>> y = int1 - node1
        >>> print(y)
        Node(-2)
        """

        if type(x) == float or type(x) == int:
            return Node(x - self.value, [(self, -1)])
        else:
            raise TypeError

    def __mul__(self, x):
        """ Multiply node by input node / int / float
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(2)
        >>> node2 = Node(5)
        >>> y = node1 * node2
        >>> print(y)
        Node(10)
        """
        if type(x) == Node:
            node_prod = Node(self.value * x.value, [(self, x.value), (x, self.value)])
        elif type(x) == float or type(x) == int:
            node_prod = Node(self.value * x, [(self, x)])
        else:
            raise TypeError

        return node_prod

    def __rmul__(self, x):
        """ Multiply node by input node / int / float
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(2)
        >>> node2 = Node(4)
        >>> y = node2 * node1
        >>> print(y)
        Node(8)
        """
        return self.__mul__(x)

    def __truediv__(self, x):
        """ Divide node by input node / int / float
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(20)
        >>> node2 = Node(5)
        >>> y = node1 / node2
        >>> print(y)
        Node(4)
        """
        if type(x) == Node:
            node_div = Node(self.value / x.value, [(self, 1/x.value), (x, -self.value / (x.value ** 2))])
        elif type(x) == float or type(x) == int:
            node_div = Node(self.value / x, [(self, 1/x)])
        else:
            raise TypeError
        return node_div

    def __rtruediv__(self, x):
        """ Divide node by input node / int / float
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(2)
        >>> node2 = Node(10)
        >>> y = node2 / node1
        >>> print(y)
        Node(5)
        """
        if type(x) == int or type(x) == float:
            return Node(x / self.value, [(self, -self.value / (x ** 2))])
        else:
            raise TypeError

    def __pow__(self, x):
        """ Raise node to power of input int / float / node
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(5)
        >>> node2 = Node(2)
        >>> y = node1 ^ node2
        >>> print(y)
        Node(25)
        """
        if type(x) == Node:
            node_pow = Node(self.value ** x.value, [(self, x.value * (self.value ** (x.value - 1))), (x, (self.value ** x.value) * np.log(self.value))])
        elif type(x) == float or type(x) == int:
            node_pow = Node(self.value ** x, [(self, x * (self.value ** (x - 1)))])
        else:
            raise TypeError
        
        return node_pow

    def __rpow__(self, x):
        """ Raise node to power of input int / float / node
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(2)
        >>> node2 = Node(5)
        >>> y = node2 ^ node1
        >>> print(y)
        Node(25)
        """
        if type(x) == float or type(x) == int:
            return Node(x ** self.value, [ (self, (self.value ** x) * np.log(self.value)) ])
        else:
            raise TypeError

    def __eq__(self, x):
        """ Equal comparison between node or node / int / float

        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Boolean
        
        Example:
        >>> node1 = Node(2)
        >>> node2 = Node(5)
        >>> y = (node1 == node2)
        >>> print(y)
        Ture

        """
        if type(x) == Node:
            return self.value == x.value and self.parent_gradients == x.parent_gradients and self.name == x.name
        elif type(x) == int or type(x) == float:
            return self.value == x
        else:
            raise TypeError

    def __ne__(self, x):
        """ Unequal comparison between nodes and node / int / float
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Boolean

        Example:
        >>> node1 = Node(2)
        >>> node2 = Node(2)
        >>> y = (node2 != node1)
        >>> print(y)
        False
        """
        if type(x) == Node:
            return self.value != x.value or self.parent_gradients != x.parent_gradients or self.name != x.name
        elif type(x) == int or type(x) == float:
            return self.value != x
        else:
            raise TypeError

    def __lt__(self, x):
        """ Strictly less than comparison between int / float / node
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Boolean

        Example:
        >>> node1 = Node(2)
        >>> node2 = Node(3)
        >>> y = (node2 < node1)
        >>> print(y)
        False
        """
        if type(x) == Node:
            return self.value < x.value
        elif type(x) == int or type(x) == float:
            return self.value < x
        else:
            raise TypeError

    def __gt__(self, x):
        """ Strictly greater than comparison between node and int / float / node
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Boolean

        Example:
        >>> node1 = Node(3)
        >>> node2 = Node(2)
        >>> y = (node1 > node2)
        >>> print(y)
        True
        """
        if type(x) == Node:
            return self.value > x.value
        elif type(x) == int or type(x) == float:
            return self.value > x
        else:
            raise TypeError

    def __le__(self, x):
        """ Less or equal than comparison between node and int / float / node
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Boolean

        Example:
        >>> node1 = Node(3)
        >>> node2 = Node(2)
        >>> y = (node1 <= node2)
        >>> print(y)
        False
        """
        if type(x) == Node:
            return self.value <= x.value
        elif type(x) == int or type(x) == float:
            return self.value <= x
        else:
            raise TypeError

    def __ge__(self, x):
        """ Greater or equal than comparison between node or int / float / node
        Params:
            self: Node
            x: Node, int, float

        Returns:
            y: Node

        Example:
        >>> node1 = Node(10)
        >>> node2 = Node(1)
        >>> y = (node2 >= node1)
        >>> print(y)
        True
        """
        if type(x) == Node:
            return self.value >= x.value
        elif type(x) == int or type(x) == float:
            return self.value >= x
        else:
            raise TypeError