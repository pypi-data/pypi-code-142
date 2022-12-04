# Description: Implementation examples of forward mode AD
# Copyright 2022 Harvard University. All Rights Reserved.

# starting with sample code from PP7 solutions
import numpy as np

class derivative:
    """Functor for function decoration adding derivatives
    """

    def __init__(self, Dpf=None):
        self.Dpf = Dpf 

    def __call__(self, f):
        """Outer function of closure takes wrapped function f as an argument.
        """

        def closure(x, p=None):
            # check if dimensions are good
            if p is None:
                p = np.zeros(x.shape)
            else:
                assert len(p) == len(
                    x
                ), f"Seed vector must have same dimension as input vector"

            if self.Dpf is not None:
                return np.array([f(x), self.Dpf(x, p)])
            else:
                for z, s in zip(x, p):
                    assert isinstance(z, DualNumber)
                    z.dual = s
                return f(x)

        return closure

class DualNumber():
    """Simple dual number class"""

    def __init__(self, real, dual=0.0):
        self.real = real
        self.dual = dual

    def __add__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real + other.real, self.dual + other.dual)
        elif isinstance(other, (int, float)):
            return DualNumber(self.real + other, self.dual)
        else:
            raise TypeError(f"Cannot add DualNumber with {type(other)}")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real - other.real, self.dual - other.dual)
        elif isinstance(other, (int, float)):
            return DualNumber(self.real - other, self.dual)
        else:
            raise TypeError(f"Cannot subtract DualNumber with {type(other)}")

    def __rsub__(self, other):
        return DualNumber(other - self.real, -self.dual)

    def __mul__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self.real * other.real,
                              self.real * other.dual + self.dual * other.real)
        elif isinstance(other, (int, float)):
            return DualNumber(self.real * other, self.dual * other)
        else:
            raise TypeError(f"Cannot multiply DualNumber with {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance (other, DualNumber):
            return DualNumber(self.real/other.real, (self.dual * other.real - self.real*other.dual)/(other.real*other.real))
        elif isinstance(other, (int, float, np.ndarray)):
            return DualNumber(self.real/other, self.dual/other)
        else: 
            raise TypeError(f"Cannot divide DualNumber with {type(other)}")
            
    def __rtruediv__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(other.real/self.real, (self.real*other.dual-self.dual*other.real)/(self.real**2))
        elif isinstance(other, (int, float, np.ndarray)):
            return DualNumber(other/self.real, (-1*other*self.dual)/(self.real**2))
        else:
            raise TypeError(f"Cannot divide DualNumber with {type(other)}")
    
    def __neg__(self):
        return -1 * self

    def __pow__(self, other):
        # exponent is an int/flost
        if isinstance(other, (int, float)):
            return DualNumber(self.real**other, other * self.real**(other - 1) * self.dual)
        # exponent is a DualNumber
        elif isinstance(other, DualNumber):
            if self.real <= 0:
                raise ArithmeticError("Invalid base")  
            return DualNumber(self.real**other.real, other.real*self.real**(other.real-1)*self.dual + np.log(self.real)*self.real**other.real*other.dual)
        raise TypeError(f"Cannot raise DualNumber with {type(other)}")

    def __rpow__(self, other):
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ArithmeticError("Invalid base")
            return DualNumber(other**self.real, other**self.real * np.log(other) * self.dual)
        raise TypeError(f"Cannot raise {type(other)} with DualNumber")

    def __repr__(self):
        return f"DualNumber(real={self.real:e}, dual={self.dual:e})"
