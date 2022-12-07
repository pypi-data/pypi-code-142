from .dual_numbers import DualNumber
import numpy as np

# Useful variables
pi = np.pi
e = np.e

def sin(x):

    """Evaluates trigonometric function sin() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns sin(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """
    
    if isinstance(x, (float, int)):
        return np.sin(x)
    elif isinstance(x, DualNumber):
        return DualNumber._sin(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def sinh(x):

    """Evaluates hyperbolic trigonometric function sinh() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns sinh(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """
    
    if isinstance(x, (float, int)):
        return np.sinh(x)
    elif isinstance(x, DualNumber):
        return DualNumber._sinh(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def asin(x):

    """Evaluates arcsin, asin() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns asin(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """
    
    if isinstance(x, (float, int)):
        return np.arcsin(x)
    elif isinstance(x, DualNumber):
        return DualNumber._asin(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def cos(x):

    """Evaluates trigonometric function cos() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns cos(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """

    if isinstance(x, (float, int)):
        return np.cos(x)
    elif isinstance(x, DualNumber):
        return DualNumber._cos(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def cosh(x):

    """Evaluates hyperbolic trigonometric function cosh() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns cosh(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """
    
    if isinstance(x, (float, int)):
        return np.cosh(x)
    elif isinstance(x, DualNumber):
        return DualNumber._cosh(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def acos(x):

    """Evaluates arccos, acos() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns acos(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """
    
    if isinstance(x, (float, int)):
        return np.arccos(x)
    elif isinstance(x, DualNumber):
        return DualNumber._acos(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def exp(x):

    """Evaluates function exp() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns exp(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """

    if isinstance(x, (float, int)):
        return np.exp(x)
    elif isinstance(x, DualNumber):
        return DualNumber._exp(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def tan(x):

    """Evaluates function tan() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns exp(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """

    if isinstance(x, (float, int)):
        return np.tan(x)
    elif isinstance(x, DualNumber):
        return DualNumber._tan(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def tanh(x):

    """Evaluates hyperbolic trigonometric function cosh() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns cosh(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """
    
    if isinstance(x, (float, int)):
        return np.tanh(x)
    elif isinstance(x, DualNumber):
        return DualNumber._tanh(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def atan(x):

    """Evaluates arctan, atan() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns atan(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """
    
    if isinstance(x, (float, int)):
        return np.arctan(x)
    elif isinstance(x, DualNumber):
        return DualNumber._atan(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def sqrt(x):

    """Evaluates function sqrt() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns sqrt(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """
    if isinstance(x, (float, int)):
        return np.sqrt(x)
    elif isinstance(x, DualNumber):
        return DualNumber._sqrt(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def ln(x):

    """Evaluates function ln() for given input.

    Args:
        x (int, float or dual number): Argument to evaluate

    Returns:
        Float or DualNumber: Returns ln(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """

    if isinstance(x, (float, int)):
        return np.log(x)
    elif isinstance(x, DualNumber):
        return DualNumber._ln(x)
    else:
        raise TypeError(f"{x} is of type {type(x)}; expected float, int, or Dual")

def log(x, y = e):

    """Evaluates function log(x, y) for the logarithm of x with base y.

    Args:
        x (int, float or dual number): Argument to evaluate
        y (int, float or dual number): Argument use as base

    Returns:
        Float or DualNumber: Returns log(input) as float if input was int/float or DualNumber if input was DualNumber.
    
    """

    if isinstance(x, (float, int)) and isinstance(y, (float, int)):
        return np.log(x) / np.log(y)
    elif isinstance(x, DualNumber) or isinstance(y, DualNumber):
        return DualNumber._log(x, y)
    else:
        raise TypeError(f"{x} is of type {type(x)} and {y} is of type {type(y)}; expected floats, ints, or Duals")


def pow(x, y):

    """Evaluates the mathematical power function pow() as x^y.

    Args:
        x (int, float or dual number): Argument as coefficient
        y (int, float or dual number): Argument use as exponent

    Returns:
        Float or DualNumber: Returns pow(x, y) as float if inputs were int/float or DualNumber if any input was DualNumber.
    
    """

    if isinstance(x, (float, int)) and isinstance(y, (float, int)):
        return np.power(x, y)
    elif isinstance(x, DualNumber) or isinstance(y, DualNumber):
        return DualNumber._pow(x, y)
    else:
        raise TypeError(f"{x} is of type {type(x)} and {y} is of type {type(y)}; expected floats, ints, or Duals")

def div(x, y):

    """Evaluates the mathematical division function dix() as x/y.

    Args:
        x (int, float or dual number): Argument as coefficient
        y (int, float or dual number): Argument use as exponent

    Returns:
        Float or DualNumber: Returns div(x, y) as float if inputs were int/float or DualNumber if any input was DualNumber.
    
    """

    if isinstance(x, (float, int)) and isinstance(y, (float, int)):
        return x / y
    elif isinstance(x, DualNumber) or isinstance(y, DualNumber):
        return DualNumber._div(x, y)
    else:
        raise TypeError(f"{x} is of type {type(x)} and {y} is of type {type(y)}; expected floats, ints, or Duals")

def mul(x, y):

    """Evaluates the mathematical division function mul() as x*y.

    Args:
        x (int, float or dual number): Argument as coefficient
        y (int, float or dual number): Argument use as exponent

    Returns:
        Float or DualNumber: Returns mul(x, y) as float if inputs were int/float or DualNumber if any input was DualNumber.
    
    """

    if isinstance(x, (float, int)) and isinstance(y, (float, int)):
        return x * y
    elif isinstance(x, DualNumber) or isinstance(y, DualNumber):
        return DualNumber._mul(x, y)
    else:
        raise TypeError(f"{x} is of type {type(x)} and {y} is of type {type(y)}; expected floats, ints, or Duals")




