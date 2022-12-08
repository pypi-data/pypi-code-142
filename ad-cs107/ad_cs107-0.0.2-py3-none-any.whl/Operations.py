import numpy as np
from project.Function import DualNumber

# Add all function names below to this list
# It is a list of strings defining what symbols in a module will be exported
# when from Operations import * is used on the module in another file
__all__ = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot', 'log', 'logb', 'ln', 'exp', 'sqrt']
supported_types = (int, float)

# sin, cos, tan 

def sin(x):
    if isinstance(x, DualNumber):
        return DualNumber(
            np.sin(x.real),
            (np.cos(x.real)) * x.dual)
    
    if isinstance(x, supported_types):
        return np.sin(x)

    raise TypeError("Error: Unsupported type passed")
    
 
def cos(x):
    if isinstance(x, DualNumber):
        return DualNumber(
            np.cos(x.real),
            (-np.sin(x.real)) * x.dual)
    
    if isinstance(x, supported_types):
        return np.cos(x)
    
    raise TypeError("Error: Unsupported type passed")
    

def tan(x):
    MP_zero = np.sin(np.pi)
    if abs(cos(x.real)) <= MP_zero:
        raise ArithmeticError("Error: zero-division in tan(x) calculation")

    if isinstance(x, DualNumber):
        return DualNumber(
            np.tan(x.real),
            (1 / np.cos(x.real)) * (1 / np.cos(x.real)) * x.dual)
    
    if isinstance(x, supported_types):
        return np.tan(x)
   
    raise TypeError("Error: Unsupported type passed")

# csc, sec, cot 
    
def csc(x):
    MP_zero = np.sin(np.pi)
    if isinstance(x, DualNumber):
        if abs(np.sin(x.real)) > MP_zero:
            return DualNumber(
                1 / np.sin(x.real),
                (-1 / np.sin(x.real)) * (1 / np.tan(x.real)) * x.dual)
        else:
            raise ArithmeticError("Error: zero-division in csc(x) calculation")

    if isinstance(x, supported_types):
        if abs(np.sin(x)) > MP_zero:
            return 1 / np.sin(x)
        else:
            raise ArithmeticError("Error: zero-division in csc(x) calculation")

    raise TypeError("Error: Unsupported type passed")


def sec(x):
    MP_zero = np.sin(np.pi)
    if isinstance(x, DualNumber):
        if abs(np.cos(x.real)) > MP_zero:
            return DualNumber(
                1 / np.cos(x.real),
                (1 / np.cos(x.real)) * np.tan(x.real) * x.dual)
        else:
            raise ArithmeticError("Error: zero-division in sec(x) calculation")

    if isinstance(x, supported_types):
        if abs(np.cos(x)) > MP_zero:
            return 1 / np.cos(x)
        else:
            raise ArithmeticError("Error: zero-division in sec(x) calculation")

    raise TypeError("Error: Unsupported type passed")


def cot(x):
    MP_zero = np.sin(np.pi)
    if isinstance(x, DualNumber):
        if abs(np.sin(x.real)) > MP_zero:
            return DualNumber(
                1 / np.tan(x.real),
                -1 * (1 / np.sin(x.real)) * (1 / np.sin(x.real)) * x.dual)
        else:
            raise ArithmeticError("Error: zero-division in cot(x) calculation")
    
    if isinstance(x, supported_types):
        if abs(np.sin(x)) > MP_zero:
            return 1 / np.tan(x)
        else:
            raise ArithmeticError("Error: zero-division in cot(x) calculation")

    raise TypeError("Error: Unsupported type passed")
    

# EXAMPLE OF FUNCTION WITH DOMAIN RESTRICTION
def ln(x):
    if isinstance(x, DualNumber):
        if x.real > 0:
            return DualNumber(np.log(x.real), x.dual * (1/x.real))
        else:
            raise ArithmeticError("ERROR: negative x value passed to ln")
        
    if isinstance(x, supported_types):
        if x > 0:
            return np.log(x)
        else:
            raise ArithmeticError("ERROR: negative x value passed to ln")

    raise TypeError("Error: Unsupported type passed")
    

def logb(x, b):
    if isinstance(b, supported_types):
        if b > 0:
        
            if isinstance(x, DualNumber):
                if x.real > 0:
                    return DualNumber(np.log(x.real, b), x.dual * 1/x.real * 1/np.log(b))
                else:
                    raise ArithmeticError("ERROR: negative x value passed to log")

            if isinstance(x, supported_types):
                if x > 0:
                    return np.log(x, b)
                else:
                    raise ArithmeticError("ERROR: negative x value passed to log")

            raise TypeError("Error: Unsupported type passed")
        
        else:
            raise ArithmeticError("ERROR: negative b value passed to logb")
     
    raise TypeError("Error: Unsupported type passed")
     
 
def log(x):
    if isinstance(x, DualNumber):
        if x.real > 0:
            return logb(x,10)
        else:
            raise ArithmeticError("ERROR: negative x value passed to log")
        
    if isinstance(x, supported_types):
        if x > 0:
            return np.log10(x)
        else:
            raise ArithmeticError("ERROR: negative x value passed to log")

    raise TypeError("Error: Unsupported type passed")


def exp(x):
    if isinstance(x, DualNumber):
        return DualNumber(np.exp(x.real), np.exp(x.real) * x.dual)
    elif isinstance(x, supported_types):
        return np.exp(x)
    raise TypeError("Error: Unsupported type passed")
    

def sqrt(x):
    if isinstance(x, DualNumber):
        if x.real >= 0:
            return x ** 0.5
        else:
            raise ArithmeticError("ERROR: negative x value passed to sqrt") 
    elif isinstance(x, supported_types):
        if x >= 0:
            return np.sqrt(x)
        else:
            raise ArithmeticError("ERROR: negative x value passed to sqrt")
