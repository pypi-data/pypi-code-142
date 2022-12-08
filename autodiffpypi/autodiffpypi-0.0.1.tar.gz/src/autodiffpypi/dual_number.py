#!/usr/bin/env python3
# File       : dual_number.py
# Description: Dual number with support for addition, multiplication, and other basic operations
import numpy as np


class DualNumber:
    _supported_types = (int, float)

    def __init__(self, real, dual=1.0, **kwargs):
        if not isinstance(real, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(real)}`")
        self.real = real
        self.dual = dual

    def __neg__(self):
        """ Negate self
        Params:
            self: DualNumber

        Returns:
            self: DualNumber

        Example:
        >>> dual = DualNumber(1,1)
        >>> dual = -dual
        >>> print(y)
        DualNumber(Real: -1, Dual: -1)
        """

        return DualNumber(-self.real, -self.dual)

    def __abs__(self):
        """ Negate self
        Params:
            self: DualNumber

        Returns:
            self: DualNumber

        Example:
        >>> dual = DualNumber(-1,-1)
        >>> dual = abs(dual)
        >>> print(y)
        DualNumber(Real: 1, Dual: 1)
        """
        real = abs(self.real)
        dual = abs(self.dual)
        return DualNumber(real, dual)

    # Dunder multiplication method
    def __mul__(self, x):
        """ Multiply self by int, float, or DualNumber
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual = DualNumber(1,1)
        >>> dual2 = DualNumber(2,1)
        >>> y = dual * dual2
        >>> print(y)
        DualNumber(Real: 2, Dual: 1)
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        if isinstance(x, self._supported_types):
            return DualNumber(x * self.real, self.dual * x.real)
        else:
            return DualNumber(self.real * x.real,
                              self.real * x.dual + self.dual * x.real)

    def __rmul__(self, x):
        """ Multiply self by int, float, or DualNumber
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual = DualNumber(1,1)
        >>> dual2 = DualNumber(2,1)
        >>> y = dual * dual2
        >>> print(y)
        DualNumber(Real: 2, Dual: 1)
        """

        return self.__mul__(x)

    # Dunder addition method
    def __add__(self, x):
        """ Add self to int, float, or DualNumber
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual = DualNumber(1,1)
        >>> dual2 = DualNumber(2,1)
        >>> y = dual + dual2
        >>> print(y)
        DualNumber(Real: 3, Dual: 2)
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        if isinstance(x, self._supported_types):
            return DualNumber(x + self.real, self.dual)
        else:
            return DualNumber(self.real + x.real, self.dual + x.dual)

    def __radd__(self, x):
        """ Add self to int, float, or DualNumber
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual = DualNumber(1,1)
        >>> dual2 = DualNumber(2,1)
        >>> y = dual + dual2
        >>> print(y)
        DualNumber(Real: 3, Dual: 2)
        """

        return self.__add__(x)

    # Dunder subtraction method
    def __sub__(self, x):
        """ Subtract int, float, or DualNumber from self
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual = DualNumber(4,2)
        >>> dual2 = DualNumber(2,1)
        >>> y = dual - dual2
        >>> print(y)
        DualNumber(Real: 2, Dual: 1)
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        if isinstance(x, self._supported_types):
            return DualNumber(self.real - x, self.dual)
        else:
            return DualNumber(self.real - x.real, self.dual - x.dual)
    
    def __rsub__(self, x):
        """ Subtract self from int, float, or DualNumber
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual = DualNumber(4,2)
        >>> int1 = 2
        >>> y = int1 - dual2
        >>> print(y)
        DualNumber(Real: 2, Dual: -2)
        """

        real = x - self.real
        dual = -self.dual
        return DualNumber(real, dual)

    # Dunder division method taken https://en.m.wikipedia.org/wiki/Dual_number
    def __truediv__(self, x):
        """ Divide self by int, float, or DualNumber
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual = DualNumber(4,2)
        >>> dual2 = DualNumber(2,1)
        >>> y = dual / dual2
        >>> print(y)
        DualNumber(Real: 2, Dual: 2)
        """

        if isinstance(x, (*self._supported_types, DualNumber)):
            try:
                real = self.real / x.real
                dual = ((self.dual * x.real - self.real * x.dual)/(x.real**2))
            except AttributeError:
                real = (self.real*x)/x**2
                dual = (self.dual*x)/x**2
        else:
            raise TypeError(f"Type error: `{type(x)}`")
        return DualNumber(real, dual)

    def __rtruediv__(self, x):
        """ Divide int, float, or DualNumber by self
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> int1 = 2
        >>> dual2 = DualNumber(2,1)
        >>> y = int1 / dual2
        >>> print(y)
        DualNumber(Real: 1, Dual: 2)
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        real = (self.real * x)/self.real**2
        dual = (self.dual * x)/self.real**2
        return DualNumber(real, dual)

    def __pow__(self, x):
        """ Take self to power of x
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual1 = DualNumber(2, 2)
        >>> int1 = 2
        >>> y = dual1 ** int1
        >>> print(y)
        DualNumber(Real: 4, Dual: 8)
        """

        if isinstance(x, (*self._supported_types, DualNumber)):
            try:
                real = self.real ** x.real
                dual_p1 = (self.real ** x.real) * x.dual * np.log(self.real)
                dual_p2 = (self.real ** x.real) * \
                          ((self.dual * x.real)/self.real)
                dual = dual_p1 + dual_p2
            except AttributeError:
                real = self.real ** x
                dual = (self.real ** x) * ((self.dual * x.real)/self.real)
        else:
            raise TypeError(f"Type error: `{type(x)}`")
        return DualNumber(real, dual)

    def __rpow__(self, x):
        """ Take int / float to power of self
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual1 = DualNumber(2, 2)
        >>> int1 = 2
        >>> y = int1 ** dual1
        >>> print(y)
        DualNumber(Real: 4, Dual: 5.545177444479562)
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        real = x ** self.real
        dual = np.log(x) * (x ** self.real) * self.dual
        return DualNumber(real, dual)

    def __eq__(self, x):
        """ Equal comparison between int / float / dual
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual1 = DualNumber(2, 2)
        >>> dual2 = DualNumber(2, 2)
        >>> y = dual2 == dual1
        >>> print(y)
        True
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        if isinstance(x, DualNumber):
            return (self.real == x.real and self.dual == x.dual)
        else:
            return self.real == x

    def __ne__(self, x):
        """ Equal comparison between int / float / dual
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual1 = DualNumber(2, 2)
        >>> dual2 = DualNumber(2, 2)
        >>> y = dual2 != dual1
        >>> print(y)
        False
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        else:
            return not self.__eq__(x)

    def __lt__(self, x):
        """ Less than comparison between int / float / dual
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual1 = DualNumber(2, 2)
        >>> dual2 = DualNumber(2, 2)
        >>> y = dual2 < dual1
        >>> print(y)
        False
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        if isinstance(x, DualNumber):
            return self.real < x.real
        else:
            return self.real < x

    def __gt__(self, x):
        """ Greater than comparison between int / float / dual
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual1 = DualNumber(3, 2)
        >>> dual2 = DualNumber(2, 2)
        >>> y = dual1 > dual2
        >>> print(y)
        True
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        if isinstance(x, DualNumber):
            return self.real > x.real
        else:
            return self.real > x
    
    def __le__(self, x):
        """ Less or equal than comparison between int / float / dual
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual1 = DualNumber(3, 2)
        >>> dual2 = DualNumber(2, 2)
        >>> y = dual2 <= dual1
        >>> print(y)
        True
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        if isinstance(x, DualNumber):
            return self.real < x.real or self.real == x.real
        else:
            return self.real < x or self.real == x

    def __ge__(self, x):
        """ Greater or equal than comparison between int / float / dual
        Params:
            self: DualNumber
            x: DualNumber, int, float

        Returns:
            y: DualNumber

        Example:
        >>> dual1 = DualNumber(2, 2)
        >>> dual2 = DualNumber(2, 2)
        >>> y = dual2 >= dual1
        >>> print(y)
        True
        """

        if not isinstance(x, (*self._supported_types, DualNumber)):
            raise TypeError(f"Type error: `{type(x)}`")
        if isinstance(x, DualNumber):
            return self.real > x.real or self.real == x.real
        else:
            return self.real > x or self.real == x

    def __repr__(self):
        return (f"DualNumber(Real: {self.real}, Dual: {self.dual})")
