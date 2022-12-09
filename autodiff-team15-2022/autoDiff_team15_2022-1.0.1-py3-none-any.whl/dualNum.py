import numpy as np

class DualNumber():
    """Dual number object useful in the implementation of automatic differentiation packages.

    Attributes
    ======
    real: int, float, np.int32, np.int64
        Real part of a dual number
    dual: int, float, np.int32, np.int64
        Dual part of a dual number

    Methods
    ======
    __add__(other)
        Enables addition with DualNumbers
    __radd__(other)
        Enables addition with DualNumbers
    __sub__(other)
        Enables subtraction with DualNumbers
    __rsub__(other)
        Enables subtraction with DualNumbers
    __mul__(other)
        Enables multiplication with DualNumbers
    __rmul__(other)
        Enables multiplication with DualNumbers
    __truediv__(other)
        Enables division with DualNumbers
    __rtruediv__(other)
        Enables division with DualNumbers
    __pow__(other)
        Enables raising DualNumbers to a power
    __rpow__(other)
        Enables raising a float/int to a DualNumber power
    __neg__()
        Enables negation of a DualNumber
    """
    _supported_types = (int, float, np.int32,np.int64)

    def __init__(self, real, dual=1.0):
        """Constructor for the DualNumber class.

        Parameters
        ======
        real: int, float, np.int32, np.int64
            Real part of a dual number
        dual: int, float, np.int32, np.int64
            Dual part of a dual number
        """
        self.real = real
        self.dual = dual

    def __add__(self, other):
        """Calculates the addition of other to self.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z :  DualNumber
            Addition of other to self

        Example
        =======
        # Testing addition with integers
        >>> z = DualNumber(1,2)
        >>> z2 = z + 1
        >>> print(z2.real, z2.dual)
        2 2

        # Testing addition with float
        >>> z3 = z + 1.0
        >>> print(z3.real, z3.dual)
        2.0 2

        # Testing addition with another dual number
        >>> z4 = DualNumber(4,5)
        >>> z5 = z + z4
        >>> print(z5.real, z5.dual)
        5 7

        Raises
        =======
        TypeError: Type `[input type]` is not supported for addition
        """
        # Supported dual number type 
        if isinstance(other, DualNumber):
            return DualNumber(other.real + self.real, other.dual + self.dual)
        # Return error if not a supported type 
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for addition"
            )
        # Supported scalar types
        else:  
            return DualNumber(self.real + other, self.dual)

    def __radd__(self, other):
        """Calculates the addition of self to other.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z : DualNumber
            Addition of self to other

        Example
        =======
        # Testing reverse addition with integers
        >>> z = DualNumber(1,2)
        >>> z2 = 1 + z
        >>> print(z2.real, z2.dual)
        2 2

        # Testing reverse addition with float
        >>> z3 = 1.0 + z
        >>> print(z3.real, z3.dual)
        2.0 2

        Raises
        =======
        TypeError: Type `[input type]` is not supported for addition
        """

        return self.__add__(other)

    def __sub__(self, other):
        """Calculates the subtraction of other from self.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z : DualNumber
            Subtraction of other from self

        Example
        =======
        # Testing subtraction with integers
        >>> z = DualNumber(1,2)
        >>> z2 = z - 2
        >>> print(z2.real, z2.dual)
        -1 2

        # Testing subtraction with float
        >>> z3 = z - 2.0
        >>> print(z3.real, z3.dual)
        -1.0 2

        # Testing subtraction with another dual number
        >>> z4 = DualNumber(4,5)
        >>> z5 = z - z4
        >>> print(z5.real, z5.dual)
        -3 -3

        Raises
        =======
        TypeError: Type `[input type]` is not supported for subtraction
        """
        # Supported dual number type 
        if isinstance(other, DualNumber):
            return DualNumber(self.real - other.real, self.dual - other.dual)
        # Return error if not a supported type 
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for subtraction"
            )
        # Supported scalar types
        else:  
            return DualNumber(self.real - other, self.dual)
    
    def __rsub__(self, other):
        """Calculates the subtraction of self from other.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z : DualNumber
            Difference of self from other

        Example
        =======
        # Testing reverse subtraction with integers
        >>> z = DualNumber(1,2)
        >>> z2 = 2 - z
        >>> print(z2.real, z2.dual)
        1 -2

        # Testing subtraction with float
        >>> z3 = 2.0 - z
        >>> print(z3.real, z3.dual)
        1.0 -2

        Raises
        =======
        TypeError: Type `[input type]` is not supported for subtraction
        """

        return -1*self.__sub__(other)

    def __mul__(self, other):
        """Calculates the product of self and other.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z : DualNumber
            Product of self and other

        Example
        =======
        # Testing multiplication with integers
        >>> z = DualNumber(1,2)
        >>> z2 = z * np.negative(2)
        >>> print(z2.real, z2.dual)
        -2 -4

        # Testing multiplication with float
        >>> z3 = z * 2.0
        >>> print(z3.real, z3.dual)
        -2.0 -4.0

        # Testing multiplication with another dual number
        >>> z4 = DualNumber(np.negative(1),np.negative(2))
        >>> z5 = z * z4
        >>> print(z5.real, z5.dual)
        -1 -4

        Raises
        =======
        TypeError: Type `[input type]` is not supported for multiplication
        """
        # Supported dual number type 
        if isinstance(other, DualNumber):
            return DualNumber(other.real * self.real, other.real * self.dual + other.dual * self.real)
        # Return error if not a supported type 
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for multiplication"
            )
        # Supported scalar types
        else:  
            return DualNumber(self.real*other, self.dual*other)
    
    def __rmul__(self, other):
        """Calculates the product of other and self.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z : DualNumber
            Product of other and self

        Example
        =======
        # Testing reverse multiplication with integers
        >>> z = DualNumber(1,2)
        >>> z2 = -2 * z
        >>> print(z2.real, z2.dual)
        -2 -4

        # Testing reverse multiplication with float
        >>> z3 = 2.0 * z
        >>> print(z3.real, z3.dual)
        2.0 4.0

        Raises
        =======
        TypeError: Type `[input type]` is not supported for multiplication
        """

        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Calculates the division of self by other.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z : DualNumber
            Division of self by other

        Example
        =======
        # Testing division with integers
        >>> z = DualNumber(1,2)
        >>> z2 = z / 2
        >>> print(z2.real, z2.dual)
        0.5 1

        # Testing division with float
        >>> z3 = z / 2.0
        >>> print(z3.real, z3.dual)
        0.5 1.0

        # Testing division with another dual number
        >>> z4 = DualNumber(-1,-2)
        >>> z5 = z / z4
        >>> print(z5.real, z5.dual)
        -1.0 0.0

        Raises
        =======
        TypeError: Type `[input type]` is not supported for division
        """
        # Supported dual number type 
        if isinstance(other, DualNumber):
            return DualNumber(self.real / other.real, (self.dual * other.real - self.real * other.dual)/(other.real**2))
        # Return error if not a supported type 
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for division"
            )
        # Supported scalar types
        else:
            return DualNumber(self.real / other, self.dual / other)

    def __rtruediv__(self, other):
        """Calculates the division of other by self.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z : DualNumber
            Division of other by self

        Example
        =======
        # Testing reverse division with integers
        >>> z = DualNumber(1,2)
        >>> z2 = 2 / z
        >>> print(z2.real, z2.dual)
        2 -4

        # Testing reverse division with float
        >>> z3 = 2.0 / z
        >>> print(z3.real, z3.dual)
        2.0 -4.0

        Raises
        =======
        TypeError: Type `[input type]` is not supported for division
        """
        # Supported dual number type 
        if isinstance(other, DualNumber):
            return other.__truediv__(self)
        # Return error if not a supported type
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for division"
            )
        # Supported scalar types
        else:
            return DualNumber(other / self.real, -other * self.dual / (self.real**2))

    def __pow__(self, other):
        """Calculation of self to the power of other.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z : DualNumber
            Self raised to the power of other

        Example
        =======
        # Testing raising dual number to integers power
        >>> z = DualNumber(2,2)
        >>> z2 = z**3
        >>> print(z2.real, z2.dual)
        8 24

        # Testing raising dual number to float power
        >>> z3 = z**3.0
        >>> print(z3.real, z3.dual)
        8 24

        # Testing raising dual number to another dual number
        >>> z4 = DualNumber(-1,-2)
        >>> z5 = z**z4
        >>> print(z5.real, z5.dual)
        0.5 -1.1931471805599454

        Raises
        =======
        TypeError: Type `[input type]` is not supported for powers
        """
        # Supported dual number type
        if isinstance(other, DualNumber):
            return DualNumber(self.real**other.real, 
                             other.real*self.real**(other.real-1) * self.dual + np.log(self.real) * self.real ** other.real * other.dual)
                             #(self.real**other.real) * (other.dual * np.log(self.real) + (self.dual*(other.real / self.real))))
        # Return error if not a supported type
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for powers"
            )
        # Supported scalar types
        else:
            return DualNumber(self.real**other, 
                            self.real**(other-1) * other * self.dual)
                             #(self.real**other) * ((self.dual*other) / self.real))

    def __rpow__(self, other):
        """Calculation of a number raised to the power of a DualNumber.

        Parameters
        ======
        self : DualNumber
        other : int, float, DualNumber

        Returns
        =======
        z : DualNumber
            Number raised to the power of a DualNumber

        Example
        =======
        # Testing raising dual number to integers power
        >>> z = DualNumber(2,2)
        >>> z2 = 3**z
        >>> print(z2.real, z2.dual)
        8 25.775021196025975

        # Testing raising dual number to float power
        >>> z3 = 3.0**z
        >>> print(z3.real, z3.dual)
        8 25.775021196025975

        # Testing raising float to a dual power
        >>> z4 = DualNumber(2,2)
        >>> z5 = 3.0**z
        >>> print(z5.real, z5.dual)
        9 25.775021196025975

        Raises
        =======
        TypeError: Type `[input type]` is not supported for powers
        """

        # Supported dual number type
        if isinstance(other, DualNumber):
            return other.__pow__(self)
        # Return error if not a supported type
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for powers"
            )
        # Supported scalar types
        else:
            return DualNumber(other**self.real, 
                             np.log(other) * other ** self.real * self.dual)

    def __neg__(self):
        """Calculation of the negative of a DualNumber.

        Parameters
        ======
        self : DualNumber

        Returns
        =======
        z : DualNumber
            Negative of a DualNumber

        Example
        =======
        # Testing negative of integer
        >>> z = DualNumber(1,2)
        >>> z2 = -z
        >>> print(z2.real, z2.dual)
        -1 -2
        """
        return DualNumber(self.real * (-1), self.dual * (-1))
