#!/usr/bin/env python3
# File       : base_derivatives.py
# Description: Holds the base derivatives of functions

import numpy as np
from src.autodiffpypi.dual_number import DualNumber
from src.structures.graph import Node

_supported_types = (float, int)


# Trig functions - sin, cos, tan
def sin(x):
    """sin implementation - supports evaluation and derivative

    Args:
        x (DualNumber/Node/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/Node/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative sin(x) = cos(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (cos(x))
    """
    if isinstance(x, DualNumber):
        real = np.sin(x.real)
        dual = np.cos(x.real) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.sin(x.value), [(x, np.cos(x.value))])
    elif isinstance(x, _supported_types):
        return np.sin(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def cos(x):
    """cos implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative cos(x) = -sin(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (-sin(x))
    """
    if isinstance(x, DualNumber):
        real = np.cos(x.real)
        dual = -np.sin(x.real) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.cos(x.value), [(x, -np.sin(x.value))])
    elif isinstance(x, _supported_types):
        return np.cos(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def tan(x):
    """tan implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative tan(x) = 1 / cos^2(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1/cos^2(x))
    """
    if isinstance(x, DualNumber):
        real = np.tan(x.real)
        dual = (1 / (np.cos(x.real)) ** 2) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.tan(x.value), [ (x, 1 / (np.cos(x.value)) ** 2) ])
    elif isinstance(x, _supported_types):
        return np.tan(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


# Inverse trig functions
def arcsin(x):
    """arcsin implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        ValueError: x must be in the range -1 <= x <= 1
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative arcsin(x) = 1/√1-x² where -1 <= x <= 1, or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1/√1-x² where -1 <= x <= 1)
    """
    if isinstance(x, DualNumber):
        if not (-1 <= x.real and x.real <= 1):
            raise ValueError(f"x must be in the range -1 <= x <= 1")
        real = np.arcsin(x.real)
        dual = (1 / np.sqrt(1 - x.real**2)) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        if not (-1 <= x.value and x.value <= 1):
            raise ValueError(f"x must be in the range -1 <= x <= 1")
        return Node(np.arcsin(x.value), [(x, 1 / np.sqrt(1 - x.value**2)) ])
    elif isinstance(x, _supported_types):
        if not (-1 <= x.real and x.real <= 1):
            raise ValueError(f"x must be in the range -1 <= x <= 1")
        return np.arcsin(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def arccos(x):
    """arccos implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        ValueError: x must be in the range -1 <= x <= 1
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative arcsos(x) = -1/√(1-x^2) where -1 < x < 1, or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (-1/√(1-x^2) where -1 < x < 1)
    """
    if isinstance(x, DualNumber):
        if not (-1 <= x.real and x.real <= 1):
            raise ValueError(f"x must be in the range -1 <= x <= 1")
        real = np.arccos(x.real)
        dual = (-1 / np.sqrt(1 - x.real**2)) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        if not (-1 <= x.value and x.value <= 1):
            raise ValueError(f"x must be in the range -1 <= x <= 1")
        return Node(np.arccos(x.value), [ (x, -1 / np.sqrt(1 - x.value**2)) ])
    elif isinstance(x, _supported_types):
        if not (-1 <= x.real and x.real <= 1):
            raise ValueError(f"x must be in the range -1 <= x <= 1")
        return np.arccos(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def arctan(x):
    """arctan implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative arctan(x) = 1/(1+x^2), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1/(1+x^2))
    """
    if isinstance(x, DualNumber):
        real = np.arctan(x.real)
        dual = (1 / (1 + x.real**2)) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.arctan(x.value), [ (x, 1 / (1 + x.value**2)) ])
    elif isinstance(x, _supported_types):
        return np.arctan(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def exp(x):
    """exp implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative exp(x) = exp(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (exp(x))
    """
    # derivative of exp(x) = exp(x)
    if isinstance(x, DualNumber):
        real = np.exp(x.real)
        dual = np.exp(x.real) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.exp(x.value), [ (x, np.exp(x.value)) ])
    elif isinstance(x, _supported_types):
        return np.exp(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


# Hyperbolic functions
def sinh(x):
    """sinh implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative sinh(x) = cosh(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (cosh(x))
    """
    if isinstance(x, DualNumber):
        real = np.sinh(x.real)
        dual = np.cosh(x.real) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.sinh(x.value), [ (x, np.cosh(x.value)) ])
    elif isinstance(x, _supported_types):
        return np.sinh(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def cosh(x):
    """cosh implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative cosh(x) = sinh(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (sinh(x))
    """
    if isinstance(x, DualNumber):
        real = np.cosh(x.real)
        dual = np.sinh(x.real) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.cosh(x.value), [ (x, np.sinh(x.value)) ])
    elif isinstance(x, _supported_types):
        return np.cosh(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def tanh(x):
    """tanh implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative tanh(x) = 1 - tanh^2(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1 - tanh^2(x))
    """
    if isinstance(x, DualNumber):
        real = np.tanh(x.real)
        dual = (1 - (np.tanh(x.real))**2) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.tanh(x.value), [ (x, 1 - (np.tanh(x.value))**2) ])
    elif isinstance(x, _supported_types):
        return np.tanh(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def sqrt(x):
    """sqrt implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative sqrt(x) = 1 / 2*sqrt(x), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1 / 2*sqrt(x))
    """
    if isinstance(x, DualNumber):
        real = np.sqrt(x.real)
        dual = (1 / (2 * np.sqrt(x.real))) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.sqrt(x.value), [ (x, 1 / (2 * np.sqrt(x.value))) ])
    elif isinstance(x, _supported_types):
        return np.sqrt(x)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def pow(x, a):
    """pow implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated
        a (int): Exponent - must be a positive integer

    Raises:
        ValueError: a must be a positive integer
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative pow(x, a) = a * x**(a-1), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (a * x**(a-1))
    """
    if not isinstance(a, int) and a > 0:
        raise ValueError(f"Exponent must be a positive integer")
    if isinstance(x, DualNumber):
        real = x.real ** a
        dual = (a * x.real**(a-1)) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(x.value ** a, [ (x, a * x.value**(a-1)) ])
    elif isinstance(x, _supported_types):
        return x ** a
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def log(x, base=np.e):
    """log implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated
        base (int/float, optional): base of the log. Defaults to np.e.

    Raises:
        ValueError: base provided base must be a positive integer/float
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation and
        derivative log(x, base) = 1 / (x * np.log(base)), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (1 / (x * np.log(base))
    """
    # type checking for base
    if not (isinstance(base, _supported_types) and base > 0):
        raise ValueError(f"Provided base must be a positive integer/float")

    # derivative of log_a(x) = 1/x*ln(a)
    # default to base e (natural log) if no base provided
    if isinstance(x, DualNumber):
        real = np.log(x.real) / np.log(base)
        dual = (1 / (x.real * np.log(base))) * x.dual
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        return Node(np.log(x.value) / np.log(base), [ (x, 1 / (x.value * np.log(base))) ])
    elif isinstance(x, _supported_types):
        return np.log(x) / np.log(base)
    else:
        raise TypeError(f"Type error: `{type(x)}`")


def sigmoid(x):
    """sigmoid implementation - supports evaluation and derivative

    Args:
        x (DualNumber/int/float): input to be evaluated

    Raises:
        TypeError: x must be of type DualNumber/int/float

    Returns:
        DualNumber/float: DualNumber that contains evaluation sigmoid(x) = 1 / (1 + np.exp(-x))
        and derivative sigmoid(x) = (sigmoid(x) * (1 - sigmoid(x))), or just evaluation
        Node: Node that contains the evaluation and a tuple with 
        the parent node and the partial derivative with respect 
        to the parent node (sigmoid(x) * (1 - sigmoid(x)))
    """
    if isinstance(x, DualNumber):
        real = 1 / (1 + np.exp(-x.real))
        dual = x.dual * real * (1-real)
        return DualNumber(real, dual)
    elif isinstance(x, Node):
        node_val = 1 / (1 + np.exp(-x.value))
        return Node(node_val, [ (x, node_val * (1 - node_val)) ])
    elif isinstance(x, _supported_types):
        return 1 / (1 + np.exp(-x))
    else:
        raise TypeError(f"Type error: `{type(x)}`")
