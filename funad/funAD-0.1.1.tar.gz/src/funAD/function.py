# -*- coding: utf-8 -*-
"""
This module implements function class, a key component for forward mode autodifferentiation.

"""

from collections.abc import Iterable 
import numpy as np
from .dual_number import DualNumber

class function:
    '''
    Create a function object to handle evalutation of a function at particular x coordinates
    and compute corresponding Jacobian through forward mode automatic differentiation.

    '''

    def __init__(self, *f, x_dim=1):
        """
        Record user defined function.
		
        ----------
        f : user defined function(s)
            A function or multiple functions that takes in a vector of x or one x as a scalar and compute arithmetic result.

        """
        if len(f) == 1:
            self.f = f[0]
        else:
            self.f = lambda *x: [f(*x) for f in f]
        self.x_dim = x_dim

    def __call__(self,*x):
        """
        Execute user defined function.
		
        Parameters
        ----------
        f : user defined function
            A function that takes in a vector or scalar of x and compute arithmetic result.
        x : array_like
            An array of numeric values (int or float).
            It could be a scalar (int or float).
			
        Returns
        -------
        f : user defined function
            A function evaluated at x. 
			
        """
        return self.f(*x)

    def grad(self,*x):
        """
        Compute Jacobian based on user specified function(s), based on input independent variable values.
		
        Parameters
        ----------
        x : array_like
            An array of numeric values (int or float).
            It could be a scalar (int or float).
			
        Returns
        -------
        J : array_like
            Jacobian matrix for given function.

        """
        self.array_type_input = False

        if len(x) == 1: #single input
            if isinstance(x[0],Iterable): # if the input is iterable, has len() function
                self.array_type_input = True
                x = x[0]
                if len(x) != self.x_dim:
                    raise ValueError('Dimension Mismatch')
            else: # sinle input x
                if self.x_dim != 1:
                    raise ValueError('Dimension Mismatch')

        else: #multiple input
            if len(x)!=self.x_dim :
                raise ValueError('Dimension Mismatch')

        J = []
        for i in range(self.x_dim):  
            p = np.identity(self.x_dim)[:,i].tolist()
            J.append(self._grad(x,p))
        if len(J) == 1:
            return J[0]
        else:
            return np.array(J).T

    def _grad(self,x,p):
        """
        Computes the derivative w.r.t. each input.
		
        Parameters
        ----------
        x : array_like
            An array of numeric values (int or float) as independent variables.
            It could be a scalar (int or float).
	p : array_like
            An array of numeric values (int or float) as seed directional vector.
            It could be a scalar (int or float).
			
        Returns
        -------
        J : array_like
            Jacobian matrix for given function.

        """
        dual_nums = [DualNumber(*input) for input in zip(x,p)]
        if self.array_type_input == True:
            result = self.f(dual_nums)
        else:
            result = self.f(*dual_nums)
        if isinstance(result,DualNumber):
            return result.dual
        else:
            return np.array([d.dual for d in result])
