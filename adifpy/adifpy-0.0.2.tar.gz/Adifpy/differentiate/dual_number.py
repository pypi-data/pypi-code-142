from __future__ import annotations

import numpy as np


class DualNumber:
    """Tuple-like object for storing the value and directional derivatives during AD passes

    This class is our implementation of dual numbers that will be used
    to calculate function and first-order derivative values at a point specified
    by the user in our auto-differentiation program.

    >>> foo = DualNumber(1, 2)
    >>> bar = DualNumber(3, 4)
    >>> foo * bar
    3.0, 10.0
    """

    def __init__(self, real : float | int, dual: float = 1.0):
        self.real = real
        self.dual = dual

    def __str__(self):
        return f"Dual Number object: ({float(self.real)}, {float(self.dual)})"

    def __repr__(self):
        return f"{float(self.real)}, {float(self.dual)}"

    def __add__(self, other: DualNumber | int | float) -> DualNumber:
        """Add a scalar or another dual number"""
        if isinstance(other, DualNumber):
            return DualNumber(self.real + other.real, self.dual + other.dual)
        try:
            return DualNumber(self.real + float(other), self.dual)
        except ValueError:
            raise TypeError("Operand must be of type int, float, or DualNumber.")

    def __radd__(self, other: int | float) -> DualNumber:
        """Add this dual number to a scalar"""
        return self.__add__(other)

    def __sub__(self, other: DualNumber | int | float) -> DualNumber:
        """Subtract a scalar or another dual number from this dual number"""
        if isinstance(other, DualNumber):
            return DualNumber(self.real - other.real, self.dual - other.dual)
        try:
            return DualNumber(self.real - float(other), self.dual)
        except ValueError:
            raise TypeError("Operand must be of type int, float, or DualNumber.")

    def __rsub__(self, other: int | float) -> DualNumber:
        """Subtract a dual number from a scalar"""
        try:
            return DualNumber(float(other) - self.real, -self.dual)
        except ValueError:
            raise TypeError("Operand must be of type int, float, or DualNumber.")

    def __mul__(self, other: DualNumber | int | float) -> DualNumber:
        """Multiply this dual number by another dual number or a scalar"""
        if isinstance(other, DualNumber):
            return DualNumber(self.real * other.real, self.real * other.dual + self.dual * other.real)
        try:
            other = float(other)
            return DualNumber(self.real * other, self.dual * other)
        except ValueError:
            raise TypeError("Operand must be of type int, float, or DualNumber.")

    def __rmul__(self, other: int | float) -> DualNumber:
        """Multiply a scalar by this dual number"""
        return self.__mul__(other)

    def __truediv__(self, other: DualNumber | int | float) -> DualNumber:
        """Divide this dual number by another dual number or a scalar"""
        if isinstance(other, DualNumber):
            return(DualNumber(self.real / other.real, (self.dual * other.real - other.dual * self.real) / (other.real**2)))
        try:
            other = float(other)
            return(DualNumber(self.real / other, self.dual / other))
        except ValueError:
            raise TypeError("Operand must be of type int, float, or DualNumber.")

    def __rtruediv__(self, other: int | float) -> DualNumber:
        """Divide a scalar by a dual number"""
        try:
            other = float(other)
            return(DualNumber(other / self.real, - self.dual * other / pow(self.real, 2)))
        except ValueError:
            raise TypeError("Operand must be of type int, float, or DualNumber.")

    def __pow__(self, other: DualNumber | int | float) -> DualNumber:
        """Raise this dual number to the power of another dual number or a scalar"""
        if isinstance(other, DualNumber):
            return(DualNumber(pow(self.real, other.real), other.dual * np.log(self.real) * pow(self.real, other.real) + self.dual * other.real * pow(self.real, other.real - 1)))
        try:
            other = float(other)
            return(DualNumber(pow(self.real, other), self.dual * other * pow(self.real, other - 1)))
        except ValueError:
            raise TypeError("Operand must be of type int, float, or DualNumber.")

    def __rpow__(self, other: int | float) -> DualNumber:
        """Raise a scalar to a dual number"""
        try:
            other = float(other)
            return(DualNumber(pow(other, self.real), self.dual * np.log(other) * pow(other, self.real)))
        except ValueError:
            raise TypeError("Operand must be of type int, float, or DualNumber.")

    def __neg__(self: DualNumber) -> DualNumber:
        """Negate this dual number"""
        return -1 * self

    # Other functions
    def exp(self):
        """Exponential e^x"""
        return DualNumber(np.exp(self.real),
                          np.exp(self.real) * self.dual)

    def sqrt(self):
        "Square root"
        return self ** 0.5

    # Builtin log functions of multiple bases
    def log(self):
        "Natural log"
        return DualNumber(np.log(self.real),
                          (1.0 / self.real) * self.dual)

    def log10(self):
        """Log base 10"""
        return DualNumber(np.log10(self.real),
                          1.0 / self.real / np.log(10) * self.dual)

    def log2(self):
        """Log base 2"""
        return DualNumber(np.log2(self.real),
                          1.0 / self.real / np.log(2) * self.dual)

    # Trigonometric Functions
    def sin(self):
        return DualNumber(np.sin(self.real),
                          np.cos(self.real) * self.dual)

    def cos(self):
        return DualNumber(np.cos(self.real),
                          -np.sin(self.real) * self.dual)

    def tan(self):
        return DualNumber(np.tan(self.real),
                          (1 / pow(np.cos(self.real), 2)) * self.dual)

    # Inverse Trigonometric Functions
    def arcsin(self):
        return DualNumber(np.arcsin(self.real),
                          pow(1 - pow(self.real,2), -1 / 2) * self.dual)

    def arccos(self):
        return DualNumber(np.arccos(self.real),
                          -pow(1 - pow(self.real,2), -1 / 2) * self.dual)

    def arctan(self):
        return DualNumber(np.arctan(self.real),
                          1 / (1 + pow(self.real, 2)) * self.dual)

    # Hyperbolic Trigonometric Functions
    def sinh(self):
        return DualNumber(np.sinh(self.real),
                          np.cosh(self.real) * self.dual)

    def cosh(self):
        return DualNumber(np.cosh(self.real),
                          np.sinh(self.real) * self.dual)

    def tanh(self):
        return DualNumber(np.tanh(self.real),
                          (1 - pow(np.tanh(self.real), 2)) * self.dual)


    # Inverse Hyperbolic Trigonometric Functions
    def arcsinh(self):
        return DualNumber(np.arcsinh(self.real),
                          pow(pow(self.real, 2) + 1, -1 / 2) * self.dual)

    def arccosh(self):
        return DualNumber(np.arccosh(self.real),
                          pow(pow(self.real, 2) - 1, -1 / 2) * self.dual)

    def arctanh(self):
        return DualNumber(np.arctanh(self.real),
                          pow(1 - pow(self.real, 2), -1) * self.dual)


# Other functions
# NOTE: These functions will not be called through any instance of DualNumber:
# They will be called through the package via __init__.py

def sigmoid(z):
    """Sigmoid activation function"""
    try:
        return 1.0 / (1.0 + np.exp(-float(z)))
    except TypeError:
        real = 1.0 / (1.0 + np.exp(-z.real))
        return DualNumber(real,
                          real * (1.0 - real) * z.dual)

def logb(z, base: float):
    """Log with arbitrary base"""
    try:
        return np.log(float(z)) / np.log(base)
    except TypeError:
        return DualNumber(np.log(z.real) / np.log(base),
                          1 / z.real / np.log(base) * z.dual)
