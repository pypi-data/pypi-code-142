import numpy as np
from .dualNum import DualNumber
from .node import Node


_supported_types = (int, float, np.int32,np.int64) 

def sin(x):
    """Calculates the sine of an int, float, DualNumber, or Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to a sine function

    Returns
    =======
    int, float, DualNumber, Node
        Sine of the input x

    Example
    =======
    >>> x = DualNumber(2,4)
    >>> y = sin(x)
    >>> print(y.real, y.dual)
    0.9092974268256817 -1.6645873461885696

    Raises
    =======
    TypeError: Type `[input type]` is not supported for sin
    """
    # Support dual number type 
    if isinstance(x, DualNumber):
        return DualNumber(np.sin(x.real), np.cos(x.real) * x.dual)
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.sin(x.value))
        x.children.append((np.cos(x.value), z))
        return z
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for cos"
            )
    # Support scalar types 
    else:
        return np.sin(x)

def cos(x):
    """Calculates the cosine of an int, float, DualNumber or Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to a cosine function

    Returns
    =======
    int, float, DualNumber, Node
        Cosine of the input x

    Example
    =======
    >>> x = DualNumber(2,4)
    >>> y = cos(x)
    >>> print(y.real, y.dual)
    -0.4161468365471424 -3.637189707302727

    Raises
    =======
    TypeError: Type `[input type]` is not supported for cos
    """
    # Support dual number type 
    if isinstance(x, DualNumber):
        return DualNumber(np.cos(x.real), -1 * np.sin(x.real) * x.dual)
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.cos(x.value))
        x.children.append((-np.sin(x.value), z))
        return z
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for cos"
            )
    # Support scalar types 
    else:
        return np.cos(x)

def tan(x):
    """Calculates the tangent of an int, float, DualNumber, or Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to a tangent function

    Returns
    =======
    int, float, DualNumber, Node
        Tangent of the input x

    Example
    =======
    >>> x = DualNumber(2,4)
    >>> y = tan(x)
    >>> print(y.real, y.dual)
    -2.185039863261519 23.09759681616767

    Raises
    =======
    TypeError: Type `[input type]` is not supported for tan
    """
    # Support dual number type
    if isinstance(x, DualNumber):
        return DualNumber(np.tan(x.real), x.dual / (np.cos(x.real)**2))
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.tan(x.value))
        x.children.append((1 / (np.cos(x.value) ** 2), z))
        return z
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for tan"
            )
    # Support scalar types 
    else:
        return np.tan(x)

def arcsin(x):
    """Calculates the arcsine of an int, float, DualNumber, Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to an arcsine function

    Returns
    =======
    int, float, DualNumber, Node
        Arcsine of the input x

    Example
    =======
    >>> x = DualNumber(0.5,0.5)
    >>> y = arcsin(x)
    >>> print(y.real, y.dual)
    0.5235987755982988 0.6666666666666666

    Raises
    =======
    TypeError: Type `[input type]` is not supported for arcsin
    """
    # Support dual number type
    if isinstance(x, DualNumber):
        return DualNumber(np.arcsin(x.real), x.dual / np.sqrt(1 - (x.real)**2))
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.arcsin(x.value))
        x.children.append((1 / np.sqrt(1 - x.value ** 2), z))
        return z
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for arcsin"
            )
    # Support scalar types 
    else:
        return np.arcsin(x)
        
def arccos(x):
    """Calculates the arccosine of an int, float, DualNumber, Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to an arccosine function

    Returns
    =======
    int, float, DualNumber, Node
        Arccosine of the input x

    Example
    =======
    >>> x = DualNumber(0.5,0.5)
    >>> y = arccos(x)
    >>> print(y.real, y.dual)
    1.0471975511965976 -0.6666666666666666

    Raises
    =======
    TypeError: Type `[input type]` is not supported for arccos
    """
    # Support dual number type
    if isinstance(x, DualNumber):
        return DualNumber(np.arccos(x.real), -1 * x.dual / np.sqrt(1-(x.real)**2))
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.arccos(x.value))
        x.children.append((-1 / np.sqrt(1 - x.value ** 2), z))
        return z
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for arccos"
            )
    # Support scalar types 
    else:
        return np.arccos(x)

def arctan(x):
    """Calculates the arctangent of an int, float, DualNumber, Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to an arctangent function

    Returns
    =======
    int, float, DualNumber, Node
        Arctangent of the input x

    Example
    =======
    >>> x = DualNumber(0.5,0.5)
    >>> y = arctan(x)
    >>> print(y.real, y.dual)
    0.46364760900080615 0.4

    Raises
    =======
    TypeError: Type `[input type]` is not supported for arctan
    """
    # Support dual number type
    if isinstance(x, DualNumber):
        return DualNumber(np.arctan(x.real), x.dual / (1+(x.real)**2))
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.arctan(x.value))
        x.children.append((1 / (1 + x.value ** 2), z))
        return z
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for arctan"
            )
    # Support scalar types 
    else:
        return np.arctan(x)

def sinh(x):
    """Calculates the hyperbolic sine of an int, float, DualNumber, Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to a hyperbolic sine function

    Returns
    =======
    int, float, DualNumber, Node
        Hyperbolic sine of the input x

    Example
    =======
    >>> x = DualNumber(0.5,0.5)
    >>> y = sinh(x)
    >>> print(y.real, y.dual)
    0.5210953054937474 0.5638129826031903

    Raises
    =======
    TypeError: Type `[input type]` is not supported for sinh
    """
    # Support dual number type
    if isinstance(x, DualNumber):
        return DualNumber(np.sinh(x.real), x.dual * np.cosh(x.real))
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.sinh(x.value))
        x.children.append((np.cosh(x.value), z))
        return z 
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for sinh"
            )
    # Support scalar types 
    else:
        return np.sinh(x)

def cosh(x):
    """Calculates the hyperbolic cosine of an int, float, DualNumber, Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to a hyperbolic cosine function

    Returns
    =======
    int, float, DualNumber, Node
        Hyperbolic cosine of the input x

    Example
    =======
    >>> x = DualNumber(0.5,0.5)
    >>> y = cosh(x)
    >>> print(y.real, y.dual)
    >>> 1.1276259652063807 0.2605476527468737

    Raises
    =======
    TypeError: Type `[input type]` is not supported for cosh
    """
    # Support dual number type 
    if isinstance(x, DualNumber):
        return DualNumber(np.cosh(x.real), x.dual * np.sinh(x.real))
    # Support node type 
    elif isinstance(x, Node):
        z = Node(np.cosh(x.value))
        x.children.append((np.sinh(x.value), z))
        return z  
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for cosh"
            )
    # Support scalar types 
    else:
        return np.cosh(x)

def tanh(x):
    """Calculates the hyperbolic tangent of an int, float, DualNumber, Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to a hyperbolic tangent function

    Returns
    =======
    int, float, DualNumber, Node
        Hyperbolic tangent of the input x

    Example
    =======
    >>> x = DualNumber(0.5,0.5)
    >>> y = tanh(x)
    >>> print(y.real, y.dual)
    0.46211715726000974 0.3932238664829637

    Raises
    =======
    TypeError: Type `[input type]` is not supported for tanh
    """
    # Support dual number type
    if isinstance(x, DualNumber):
        return DualNumber(np.tanh(x.real), x.dual * (1 - np.tanh(x.real) ** 2)) 
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.tanh(x.value))
        x.children.append((1 / np.cosh(x.value)**2, z))
        return z 
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for tanh"
            )
    # Support scalar types 
    else: 
        return np.tanh(x)

def exp(x):
    """Calculates the exponential of an int, float, DualNumber, Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to an exponential function

    Returns
    =======
    int, float, DualNumber, Node
        Exponential of the input x

    Example
    =======
    >>> x = DualNumber(0,0)
    >>> y = exp(x)
    >>> print(y.real, y.dual)
    1.0 0.0

    Raises
    =======
    TypeError: Type `[input type]` is not supported for exponents
    """
    # Support dual number type
    if isinstance(x, DualNumber):
        return DualNumber(np.exp(x.real), np.exp(x.real) * x.dual)
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.exp(x.value))
        x.children.append((np.exp(x.value), z)) 
        return z 
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for exponents"
            )
    # Support scalar types 
    else:
        return np.exp(x)

def log(x, base = 10):
    """Calculates the logarithm of an int, float, DualNumber, Node input with default base of 10.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to a logarithmic function

    Returns
    =======
    int, float, DualNumber, Node
        Logarithm of the input x

    Example
    =======
    >>> x = DualNumber(1,1)
    >>> y = log(x)
    >>> print(y.real, y.dual)
    0.0 0.43429448190325176

    Raises
    =======
    TypeError: Type `[input type]` is not supported for logs
    """
    # Support dual number type
    if isinstance(x, DualNumber):
        return DualNumber(np.log(x.real)/np.log(base), x.dual/(x.real*np.log(base)))
    # Support node type
    elif isinstance(x, Node):
        z = Node(np.log(x.value)/np.log(base))
        x.children.append((1 / (x.value * np.log(base)), z))
        return z
    # Return error if not a supported type
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for logs"
            )
    # Support scalar types 
    else:
        return np.log(x)/np.log(base)

def logistic(x):
    """Calculates the logistic of an int, float, DualNumber, Node input.

    Parameters
    ======
    x : int, float, DualNumber, Node
        The input to a logistic function

    Returns
    =======
    int, float, DualNumber, Node
        Logistic of the input x
        
    Example
    =======
    >>> x = DualNumber(1,1)
    >>> y = logistic(x)
    >>> print(y.real, y.dual)
    0.7310585786300049 0.19661193324148185

    Raises
    =======
    TypeError: Type `[input type]` is not supported for logistics
    """
    # Support dual number type
    if isinstance(x, DualNumber):
        return DualNumber(1 / (1 + np.exp(-x.real)),
                         np.exp(x.real) / ((1 + np.exp(x.real)) ** 2))
    # Support node type
    elif isinstance(x, Node):
        z = Node(1 / (1 + np.exp(-x.value))) 
        x.children.append((np.exp(x.value) / (1 + np.exp(x.value)) ** 2, z))
        return z 
    # Return error if not a supported type 
    elif not isinstance(x, _supported_types):
        raise TypeError(
            f"Type `{type(x)}` is not supported for logistic"
            )
    # Support scalar types 
    else: 
        return 1 / (1 + np.exp(-x))