# -*- coding: utf-8 -*-
"""

This module implements different optimizers classes, which is the key extension functionality for finding local minimum and maximum.

"""
from abc import abstractmethod
import numpy as np
from .function import function


class Optimizer():
    '''
    Create a optimizer object to handle general optimization request
    for user defined learning rate, within maximum iterations and tolerance threshold.
    
    '''

    def __init__(self, learning_rate = 0.001, max_iteration = 10000, eps = 1e-15):
        """
        Initialize an optimizer.
		
        Parameters
        ----------
        learning_rate : float
            User specified step size at each iteration while moving towards the goal of the optimization task.
        
        max_iteration : int
            User specified maximum number of iterations a optimization task should perform.     
        
        eps : float
            User specified tolerance threshold. When an iteration's magnitude of change for independent variable  
            vector is smaller than the given threshold the optimization task is said to reach the goal and
            iteration would terminate and produce a final result.
            
        """
        if callable(learning_rate):
            self.eta = learning_rate
        else:
            self.eta = lambda t : learning_rate
        self.max_iteration = max_iteration
        self.eps = eps

    @abstractmethod
    def minimize(self,f, x_dim = 1, x0 = None,verbose=False):
        """
        A place-holder for minimize method that all children optimizer class must implement.
        
        """        
        raise NotImplementedError

class GD(Optimizer):
    """
    Gradient Optimizer Class used to find local minimum or maximum of a given function

    """
    def minimize(self,f, x_dim = 1, x0 = None,verbose=False):
        """
        Minimize a function using gradient descent. 
	Each iteration the algorithm make a step in the steepest descent.

        Parameters
        ----------
        f: function class instance
            The function to minimize.
        x_dim : int
            Specify how many independent variables there are in all input functions.
        x0: int or float or array-like of numeric values.
            The starting values of the independent variables for the gradietn descent algorithm
        verbose: bool
            Whether to return the full iteration history of the gradient descent algorithm

        Returns
        -------
        x: float or array-like. 
            A scalar x value for scalar input, or a list of x values for vector inputs.
	    This is the value(s) of independent variable(s) at the found local minimum.
        f(x): float
            The value of the function at the minimum
        history: list
            Each element of the list represents one iteration which is a tuple.
	    Each element of that iteration tuple is made of two elements: a NumPy array of x's and function value at that iteration.
	    The NumPy array of x's for a iteration consists of the corresponding value(s) of independent variable(s) in the input order.
        
        Examples
        --------
        >>> def f(x_1,x_2):
        >>>   return (x_1+1)**2 + x_2**2 + 3
        >>> gd = ad.GD(learning_rate = 0.01, max_iteration = 10000, eps = 1e-12)
        >>> id_vars, f_min = gd.minimize(f, x_dim=2, x0 = [12, 6])
	>>> x_1, x_2 = id_vars
        >>> print(f"the local maximum function value is {f_min:.2f}")
        the local maximum function value is 3.00
        >>> print(f"the corresponding independent variable values are x = {x_1:.2f}, y={x_2:.2f}")
        the corresponding independent variable values are x = -1.00, y=0.00
	
        """
        if isinstance(f,function):
            if len(f.function_list) > 1: # only functions with a single output can be minimized
                raise TypeError("Cannot optimize vector-valued function")
        else:
            f = function(f,x_dim = x_dim)
        if x0 is None:
            x0 = np.zeros(f.x_dim) # initialize the starting point to be zero (vector)
        x = x0
        t = 0
        history = []
        for i in range(self.max_iteration):
            x_new = x - self.eta(t)*f.grad(x) # update rule of gradient descent
            if abs(f(x)-f(x_new)) < self.eps: # break the loop when the change in function is less than eps
                x = x_new
                break
            x = x_new
            t += 1
            if verbose:
                history.append((x,f(x)))
	if len(x) == 1: x=x[0] # unpack scalar input into float number
        if verbose:
            return x,f(x),history
        else:
            return x,f(x)

    def maximize(self,f, x_dim = 1, x0 = None,verbose=False):
        """
        Maximize a function using gradient descent. 
	Each iteration the algorithm make a step in the steepest ascent.
	Search for the maximum of -f(x) which makes the iterative process equivalent. 

        Parameters
        ----------
        f: function class instance
            The function to maximize.
        x_dim : int
            Specify how many independent variables there are in all input functions.
        x0: int or float or array-like of numeric values.
            The starting values of the independent variables for the gradietn descent algorithm
        verbose: bool
            Whether to return the full iteration history of the gradient descent algorithm

        Returns
        -------
        x: float or array-like. 
            A scalar x value for scalar input, or a list of x values for vector inputs.
	    This is the value(s) of independent variable(s) at the found local maximum.
        f(x): float
            The value of the function at the maximum
        history: list
            Each element of the list represents one iteration which is a tuple.
	    Each element of that iteration tuple is made of two elements: a NumPy array of x's and function value at that iteration.
	    The NumPy array of x's for a iteration consists of the corresponding value(s) of independent variable(s) in the input order.
        
        Examples
        --------
        >>> def f(x,y):
        >>>   return -(x+2)*(x+1)-(y+1)*(y+3)
        >>> gd = ad.GD(learning_rate = 0.2, max_iteration = 6000, eps = 1e-6)
        >>> id_vars, f_max = gd.maximize(f, x_dim=2, x0 = [3.1, -2])
	>>> x, y = id_vars
        >>> print(f"the local maximum function value is {f_max:.2f}")
        the local maximum function value is 1.25
        >>> print(f"the corresponding independent variable values are x = {x:.2f}, y={y:.2f}")
        the corresponding independent variable values are x = -1.50, y=-2.00
	
        """
        if isinstance(f,function):
            if len(f.function_list) > 1: # only functions with a single output can be maximized
                raise TypeError("Cannot optimize vector-valued function")
            neg_f = function(lambda *x: -1*f.function_list[0](*x),x_dim=x_dim) # build function object neg_f whose "f" attribute equal to -f
        else:
            neg_f = function(lambda *x: -1*f(*x),x_dim = x_dim) # build function object neg_f whose "f" attribute equal to -f
        if verbose:
            x,neg_f_min,history = self.minimize(neg_f,x_dim=x_dim,x0=x0,verbose=True) # recall max f = - min(-f); minimizing neg_f gives -max(f) and argmax(f) 
            history = [(tup[0],-1*tup[1]) for tup in history] # correct history which evaluated -f(x)
            return x,-1*neg_f_min,history
        x,neg_f_min = self.minimize(neg_f,x_dim=x_dim,x0=x0,verbose=False)
        return x,-1*neg_f_min

class Adam(Optimizer):
    def __init__(self, learning_rate=0.001, max_iteration = 10000, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08):
        super().__init__(learning_rate, max_iteration)
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.epsilon = epsilon

    def minimize(self,f, x_dim = 1, x0 = None,verbose=False):
        if isinstance(f,function):
            if len(f.function_list) > 1: # only functions with a single output can be minimized
                raise TypeError("Cannot optimize vector-valued function")
        else:
            f = function(f,x_dim = x_dim)
        if x0 is None:
            x0 = np.zeros(f.x_dim) # initialize the starting point to be zero (vector)
        x = x0
        t = 0
        m = 0
        v = 0
        history = []
        for i in range(self.max_iteration):
            g = f.grad(x)
            m = self.beta_1 * m + (1-self.beta_1)*g
            v = self.beta_2 * v + (1-self.beta_2)*g**2
            m_hat = m/(1-self.beta_1**(t+1))
            v_hat = v/(1-self.beta_2**(t+1))
            x_new = x - self.eta(t)/np.sqrt(v_hat+self.epsilon)*m_hat # update rule of adam
            if abs(f(x)-f(x_new)) < self.eps: # break the loop when the change in function is less than eps
                x = x_new
                break
            x = x_new
            t += 1
            if verbose:
                    history.append((x,f(x)))
	if len(x) == 1: x=x[0] # unpack scalar input into float number
        if verbose:
            return x,f(x), history
        else:
            return x,f(x)
    
    def maximize(self,f, x_dim = 1, x0 = None,verbose=False):
        if isinstance(f,function):
            if len(f.function_list) > 1: # only functions with a single output can be maximized
                raise TypeError("Cannot optimize vector-valued function")
            neg_f = function(lambda *x: -1*f.function_list[0](*x),x_dim=x_dim) # build function object neg_f whose "f" attribute equal to -f
        else:
            neg_f = function(lambda *x: -1*f(*x),x_dim = x_dim) # build function object neg_f whose "f" attribute equal to -f
        if verbose:
            x,neg_f_min,history = self.minimize(neg_f,x_dim=x_dim,x0=x0,verbose=True) # recall max f = - min(-f); minimizing neg_f gives -max(f) and argmax(f) 
            history = [(tup[0],-1*tup[1]) for tup in history] # correct history which evaluated -f(x)
            return x,-1*neg_f_min,history
        x,neg_f_min = self.minimize(neg_f,x_dim=x_dim,x0=x0,verbose=False)
        return x,-1*neg_f_min


