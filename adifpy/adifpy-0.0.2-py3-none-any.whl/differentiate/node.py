from __future__ import annotations

import numpy as np

from Adifpy.differentiate.helpers import isscalar


class Node:
    """Object for storing weights and adjoint values during reverse mode AD

    This class is our implementation of nodes that will be passed through a
    user's input function in reverse mode AD.

    >>> foo = Node(3)
    >>> bar = Node(2)
    >>> foo * bar
    6.0, 0
    """
    def __init__(self, value: int | float):
        self.value = value
        self.children = []
        self.node_adjoint = None

    def __str__(self):
        return f"Node object of value {float(self.value)}, with {len(self.children)} child nodes."

    def __repr__(self):
        return f"{float(self.value)}, {len(self.children)}"

    def reverse_pass(self):
        # Check if node has been visited already
        if not self.node_adjoint:
            self.node_adjoint = 0

            # Iterate over child nodes, summing together the weights and child node adjoint values
            for weight, node in self.children:
                self.node_adjoint += weight * node.reverse_pass()

        return self.node_adjoint

    def __add__(self, other: Node | float | int) -> Node:
        """Add a scalar or a node to a node"""
        if isinstance(other, Node):
            z = Node(self.value + other.value)
            self.children.append([1.0, z])
            other.children.append([1.0, z])
            return z
        elif isscalar(other):
            z = Node(self.value + other)
            self.children.append([1.0, z])
            return z
        raise TypeError("Operand must be of type int, float, or node.")

    def __radd__(self, other: float | int) -> Node:
        """Add a node to a scalar"""
        return self.__add__(other)

    def __sub__(self, other: Node | float | int) -> Node:
        """Subtract a scalar or node from a node"""
        if isinstance(other, Node):
            z = Node(self.value - other.value)
            self.children.append([1.0, z])
            other.children.append([-1.0, z])
            return z
        elif isscalar(other):
            z = Node(self.value - other)
            self.children.append([1.0, z])
            return z
        raise TypeError("Operand must be of type int, float, or node.")

    def __rsub__(self, other: float | int) -> Node:
        """Subtract a node from a scalar"""
        if isscalar(other):
            z = Node(other - self.value)
            self.children.append([-1.0, z])
            return z
        raise TypeError("Operand must be of type int, float, or DualNumber.")

    def __mul__(self, other: Node | float | int) -> Node:
        """Multiply a node by another node or a scalar"""
        if isinstance(other, Node):
            z = Node(self.value * other.value)
            self.children.append([other.value, z])
            other.children.append([self.value, z])
            return z
        elif isscalar(other):
            z = Node(self.value * other)
            self.children.append([other, z])
            return z
        raise TypeError("Operand must be of type int, float, or node.")

    def __rmul__(self, other: float | int) -> Node:
        """Multiply a scalar by a node"""
        return self.__mul__(other)

    def __truediv__(self, other: Node | float | int) -> Node:
        """Divide a node by another node or a scalar"""
        if isinstance(other, Node):
            z = Node(self.value / other.value)
            self.children.append([1 / other.value, z])
            other.children.append([-self.value / pow(other.value, 2), z])
            return z
        elif isscalar(other):
            z = Node(self.value / other)
            self.children.append([1 / other, z])
            return z
        raise TypeError("Operand must be of type int, float, or node.")

    def __rtruediv__(self, other: float | int) -> Node:
        """Divide a scalar by a node"""
        if isscalar(other):
            z = Node(other / self.value)
            self.children.append([-other / pow(self.value, 2), z])
            return z
        raise TypeError("Operand must be of type int, float, or node.")

    def __pow__(self, other: Node | float | int) -> Node:
        """Raise a node to the power of another node or a scalar"""
        if isinstance(other, Node):
            z = Node(pow(self.value, other.value))
            self.children.append([other.value * pow(self.value, other.value - 1), z])
            other.children.append([pow(self.value, other.value) * np.log(self.value), z])
            return z
        elif isscalar(other):
            z = Node(pow(self.value, other))
            self.children.append([other * pow(self.value, other - 1), z])
            return z
        raise TypeError("Operand must be of type int, float, or node.")

    def __rpow__(self, other: float | int) -> Node:
        """Raise a scalar to the power of a node"""
        if isscalar(other):
            z = Node(pow(other, self.value))
            self.children.append([pow(other, self.value) * np.log(other), z])
            return z
        raise TypeError("Operand must be of type int, float, or node.")

    def __neg__(self: Node) -> Node:
        """Negate a node"""
        return -1 * self

# Other functions
    def exp(self):
        """Exponential e^x"""
        z = Node(np.exp(self.value))
        self.children.append([np.exp(self.value), z])
        return z

    def sqrt(self):
        "Square root"
        return self ** 0.5

    # Builtin log functions of multiple bases
    def log(self):
        "Natural log"
        z = Node(np.log(self.value))
        self.children.append([1.0 / self.value, z])
        return z

    def log10(self):
        """Log base 10"""
        z = Node(np.log10(self.value))
        self.children.append([1.0 / self.value / np.log(10), z])
        return z

    def log2(self):
        """Log base 2"""
        z = Node(np.log2(self.value))
        self.children.append([1.0 / self.value / np.log(2), z])
        return z

    # Trigonometric functions
    def sin(self):
        z = Node(np.sin(self.value))
        self.children.append([np.cos(self.value), z])
        return z

    def cos(self):
        z = Node(np.cos(self.value))
        self.children.append([-np.sin(self.value), z])
        return z

    def tan(self):
        z = Node(np.tan(self.value))
        self.children.append([1 / pow(np.cos(self.value), 2), z])
        return z

    # Inverse trigonometric functions
    def arcsin(self):
        z = Node(np.arcsin(self.value))
        self.children.append([pow(1 - pow(self.value, 2), -1 / 2), z])
        return z

    def arccos(self):
        z = Node(np.arccos(self.value))
        self.children.append([-pow(1 - pow(self.value, 2), -1 / 2), z])
        return z

    def arctan(self):
        z = Node(np.arctan(self.value))
        self.children.append([pow(1 + pow(self.value, 2), -1), z])
        return z

    # Hyperbolic functions
    def sinh(self):
        z = Node(np.sinh(self.value))
        self.children.append([np.cosh(self.value), z])
        return z

    def cosh(self):
        z = Node(np.cosh(self.value))
        self.children.append([np.sinh(self.value), z])
        return z

    def tanh(self):
        z = Node(np.tanh(self.value))
        self.children.append([pow(np.cosh(self.value), -2), z])
        return z

    # Inverse hyperbolic functions
    def arcsinh(self):
        z = Node(np.arcsinh(self.value))
        self.children.append([pow(pow(self.value, 2) + 1, -1/2), z])
        return z

    def arccosh(self):
        z = Node(np.arccosh(self.value))
        self.children.append([pow(pow(self.value, 2) - 1, -1/2), z])
        return z

    def arctanh(self):
        z = Node(np.arctanh(self.value))
        self.children.append([pow(1 - pow(self.value, 2), -1), z])
        return z
