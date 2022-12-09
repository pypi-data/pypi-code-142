# -*- coding: utf-8 -*-
"""
This module implements function class, a key component for forward mode autodifferentiation.

"""
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
        x_dim : int
            Specify how many independent variables there are in all input functions.
	    
        """
        self.x_dim = x_dim
        self.function_list = f #list of functions each returning one output

    def _plugin(self,x): # x is an iterable
        """
        Process independent variables as a vector input.
		
        ----------
        x : int or float or array-like of numeric values.
            Specify how many independent variables there are in all input functions.
	    
        """
        results = []
        for f in self.function_list:
            try:
                result = f(*x)
            except TypeError:
                try:
                    result = f(x)
                except TypeError:
                    raise TypeError ('Function fails to process given input.')
            results.append(result)
        results = np.array(results)
        return results


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
	    
        Notes
        ----------
        NumPy is known to return nan with integer inputs in cases
	when a mathematically correct answer should be a float number, 
        e.g. print([10**c for c in np.arange(-5,5)]) will raise a ValueError in Numpy
        saying ValueError: Integers to negative integer powers are not allowed.
        As such we convert all input to float to avoid such issues.
			
        """
        # Preprocess x accepting all kinds of input and make them into 1-d array
        x = np.array(x).reshape(-1).astype('float')  # convert numeric input to float to prevent NumPy delegated computation returning exact result for integer input
        if len(x) != self.x_dim:
            raise ValueError('Dimension Mismatch')
        result = self._plugin(x)
        if result.shape[0] == 1:
            return result[0]
        else: 
            return result

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
	    
        Examples
        --------
        >>> def f(x): # user-defined function
        >>>   return ad.sin(ad.exp(x)) + (6**ad.cos(x)/x)**x - 2*ad.tan(-x)
        >>> f = function(f) # initiate a function object
	>>> print("f(1) = {:.2f}".format(f(1))) # f(1) rounded to 2dp should be 6.16
        f(1) = 6.16
	>>> print("df/dx(1) = {:.2f}".format(f.grad(1))) # f'(1) rounded to 2dp should be 0.32
        df/dx(1) = 0.32
	
        """
        # Preprocess x
        x = np.array(x).reshape(-1) #accepting all kinds of input and make them into 1-d array
        if len(x) != self.x_dim:
            raise ValueError('Dimension Mismatch')
        
        J = []
        for i in range(self.x_dim):  
            p = np.identity(self.x_dim)[:,i].tolist()
            J.append(self._grad(x,p))
        result = np.array(J).T
        #putting into desired dimension, can be modified, right now we return 1-d array for R1 to Rn and Rm to R1
        if result.shape[0] == 1 and result.shape[1] ==1:
            return result[0,0]
        elif result.shape[0] == 1:
            return result[0,:]
        elif result.shape[1] == 1:
            return result[:,0]
        else: 
            return result

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
        results = self._plugin(dual_nums)
        return np.array([result.dual for result in results])
        
