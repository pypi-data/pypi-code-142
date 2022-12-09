# -*- coding: utf-8 -*-
"""

This module implements DualNumber class, a key component 
for forward mode automatic differentiation.

"""
import numpy as np

class DualNumber(object):
    '''
    Create a dual number

    Attributes
    ----------
    _supported_scalars : tuple
        Description of supported numerical types.    
    '''

    _supported_scalars = (int, float)
    
    def __init__(self,real,dual = None):
        """
        Specify the real and dual part of a dual number.

        Parameters
        ----------
        real : float
            Real part of dual number.
        dual : float
            Dual part of dual number, default to 1 if not specified.
        
        Note
        ----
        Dual part is typically only set to 1 through external function
        when finding derivative with respect to that dual number.
        
        """
        self.real = real
        if dual == None:
            self.dual = 1.0
        else:
            self.dual = dual

    def __repr__(self):
        """
        Nice string representation of dual number.

        Returns
        ----------
        str

        Examples
        --------
        Print DualNumber

        >>> x = DualNumber(1.0)
        >>> x
        DualNumber(real=1.0, dual=None)

        """
        args = f"real={repr(self.real)}, dual={repr(self.dual)}"
        return f"{type(self).__name__}({args})"

    def __add__(self, other):
        '''
        Compute addition with dual number or regular number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number being added.
        
        Returns
        ----------
        DualNumber
        
        Raises
        ------
        TypeError
        If the other number inputted is not of any supported numeric format. 
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        if isinstance(other, self._supported_scalars):
            return DualNumber(self.real+other, self.dual)
        else:
            return DualNumber(self.real + other.real, self.dual + other.dual)
    
    def __radd__(self, other):
        '''
        Compute reflective addition with regular number.

        Parameters
        ----------
        other : int or float
            Other number being added to.
        
        Returns
        ----------
        DualNumber
        
        '''
        return self.__add__(other)
    
    def __sub__(self, other):
        '''
        Compute Subtraction of dual number or regular number from dual number or regular number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number being subtracted.
        
        Returns
        ----------
        DualNumber
        
        Raises
        ------
        TypeError
        If the other is not of any supported numeric format.       
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        if isinstance(other, self._supported_scalars):
            return DualNumber(self.real - other, self.dual)
        else:
            return DualNumber(self.real - other.real, self.dual - other.dual)

    def __rsub__(self, other):
        '''
        Compute Subtraction of dual number from regular number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number being subtracted from.
        
        Returns
        ----------
        DualNumber
        
        Raises
        ------
        TypeError
        If the other is not of any supported numeric format.        
        
        '''
        if not isinstance(other, self._supported_scalars):
            raise TypeError(f"Unsupported type '{type(other)}'")
        else:
            return DualNumber(other - self. real, - self.dual)

    def __mul__(self, other):
        '''
        Compute Multiplication with dual number or regular number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number being multiplied.
        
        Returns
        -------
        DualNumber
        
        Raises
        ------
        TypeError
        If the other number inputted is not of any supported numeric format.      

        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        if isinstance(other, self._supported_scalars):
            return DualNumber(self.real * other, self.dual * other)
        else:
            return DualNumber(self.real * other.real, self.real * other.dual + self.dual * other.real)
    
    def __rmul__(self, other):
        '''
        Compute reflective multiplication with regular number.

        Parameters
        ----------
        other : int or float
            Other number being multiplied.
        
        Returns
        -------
        DualNumber
        
        Raises
        ------
        TypeError
        If the other number input is not of any supported numeric format.    
        
        '''
        return self.__mul__(other)

    def __pow__(self,other):
        '''
        Compute power raised to input regular number or dual number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number as the power a dual number is being raised to.
        
        Returns
        -------
        DualNumber
        
        Raises
        ------
        TypeError
        If the other number input is not of any supported numeric format.   
        
        Notes
        ----------
        Since we delegate power to NumPy and NumPy return integer or nothing when power 
        is a negative integer when a mathematically correct answer should be a float number, 
        e.g. print([10**c for c in np.arange(-5,5)]) will raise a ValueError in Numpy
        saying ValueError: Integers to negative integer powers are not allowed.
        As such we convert the power numeric terms to float to avoid such issues.
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            return DualNumber(self.real**float(other), other*self.real**float(other-1)*self.dual)
        else:
            return DualNumber(self.real**float(other.real),self.real**float(other.real)*(other.real*self.dual/self.real+other.dual*np.log(self.real)))
    
    def __rpow__(self,other):
        '''
        Compute input int or float number raised to the power of dual number.

        Parameters
        ----------
        other : int or float
            Other number as the base to which is raised to the power of a dual number.
        
        Returns
        -------
        DualNumber
        
        Raises
        ------
        TypeError
        If the other number input is not of any supported numeric format.    
        
        '''
        if not isinstance(other, self._supported_scalars):
            raise TypeError(f"Unsupported type '{type(other)}'")
        other = DualNumber(other,0)
        return other.__pow__(self)
        
    def __neg__(self):
        '''
        Flip the sign of input dual number by negating its dual part and real part respectively.
        
        Returns
        -------
        DualNumber 
        
        '''
        return DualNumber(- self.real , - self.dual)
    
    def __eq__(self, other):
        '''
        Compare the real part of two numbers.

        Parameters
        ----------
        other: int or float or DualNumber instance
        
        Returns
        -------
        Boolean 
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            return self.real == other
        else:
            return self.real == other.real
    
    def __ne__(self, other):
        '''
        Compare the real part of two numbers.

        Parameters
        ----------
        other: int or float or DualNumber instance
        
        Returns
        -------
        Boolean 
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            return not self.real == other
        else:
            return not self.real == other.real
    
    def __lt__(self, other):
        '''
        Compare the real part of two numbers using "<"

        Parameters
        ----------
        other: int or float or DualNumber instance
        
        Returns
        -------
        Boolean 
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            return self.real < other
        else:
            return self.real < other.real
    
    def __le__(self, other):
        '''
        Compare the real part of two numbers using "<="

        Parameters
        ----------
        other: int or float or DualNumber instance
        
        Returns
        -------
        Boolean 
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            return self.real <= other
        else:
            return self.real <= other.real
    
    def __gt__(self, other):
        '''
        Compare the real part of two numbers using ">"

        Parameters
        ----------
        other: int or float or DualNumber instance
        
        Returns
        -------
        Boolean 
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            return self.real > other
        else:
            return self.real > other.real
    
    def __ge__(self, other):
        '''
        Compare the real part of two numbers using ">="

        Parameters
        ----------
        other: int or float or DualNumber instance
        
        Returns
        -------
        Boolean 
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            return self.real >= other
        else:
            return self.real >= other.real


    def __truediv__(self, other):
        '''
        Compute float division of dual number by int, float or dual number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number being divided.
        
        Returns
        -------
        DualNumber
        
        Raises
        ------
        ZeroDivisionError
            If the denominator other number's real part is zero.
            
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            return DualNumber(self.real/other, self.dual/other)
        else:
            return DualNumber(self.real/other.real, (self.dual*other.real - other.dual*self.real)/(other.real*other.real))

    def __rtruediv__(self, other):        
        '''
        Compute float division of real number by dual number.

        Parameters
        ----------
        other : int or float
            Other real number being divided.
        
        Returns
        -------
        DualNumber
        
        Raises
        ------
        ZeroDivisionError
            If the denominator dual number's real part is zero.
            
        '''
        if isinstance(other, self._supported_scalars):
            return DualNumber(other/self.real, (-1*other*self.dual)/(self.real*self.real))    
        else:
            raise TypeError(f"Unsupported type '{type(other)}'")

    #=================== inplace operation ===================#
    def __iadd__(self,other):
        '''
        Compute inplace addition of dual number by int, float or dual number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number being added.
        
        Returns
        -------
        DualNumber
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            self.real += other
            return self
        else:
            self.real += other.real
            self.dual += other.dual
            return self

    def __isub__(self,other):
        '''
        Compute inplace substraction of dual number by int, float or dual number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number being added.
        
        Returns
        -------
        DualNumber
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            self.real -= other
            return self
        else:
            self.real -= other.real
            self.dual -= other.dual
            return self
    
    def __imul__(self,other):
        '''
        Compute inplace multiplication of dual number with int, float or dual number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number being added.
        
        Returns
        -------
        DualNumber
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            self.real *= other
            self.dual *= other
            return self
        else:
            self.real,self.dual = self.real*other.real, self.dual*other.real + self.real*other.dual
            return self
    
    def __itruediv__(self,other):
        '''
        Compute inplace division of dual number by int, float or dual number.

        Parameters
        ----------
        other : int or float or DualNumber instance
            Other number being added.
        
        Returns
        -------
        DualNumber
        
        Raises
        ------
        ZeroDivisionError
            If the denominator other number's real part is zero.
            
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            self.real /= other
            self.dual /= other
            return self
        else:
            self.real,self.dual = self.real/other.real, (self.dual*other.real - self.real*other.dual)/(other.real*other.real)
            return self
