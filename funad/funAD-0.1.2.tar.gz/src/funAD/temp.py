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
        
        '''
        if not isinstance(other, (*self._supported_scalars, DualNumber)):
            raise TypeError(f"Unsupported type '{type(other)}'")
        elif isinstance(other, self._supported_scalars):
            return DualNumber(self.real**other, other*self.real**(other-1)*self.dual)
        else:
            return DualNumber(self.real**other.real,self.real**other.real*(other.real*self.dual/self.real+other.dual*np.log(self.real)))
    
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


# -*- coding: utf-8 -*-
"""

This module implement overloading functions to handle arithmetic for dual numbers.

"""

import numpy as np

def exp(x):
  '''
  Overloads the exponential function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance

  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.exp(x.real), np.exp(x.real)*x.dual)
  else:
    return np.exp(x)

def log(x):
  '''
  Overloads the natural logarithm function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance

  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.log(x.real), x.dual/x.real)
  else:
    return np.log(x)

#=================== Trigonometric ===================#
def sin(x):
  '''
  Overloads the sin() function. 

  Parameters
  ----------
  x : int or float or DualNumber instance
      Each number represent angle in radians (:math:`2 \pi` rad equals 360 degrees).

  Returns
  -------
  float or DualNumber instance
      
  Examples
  --------
  Print sine of one angle:

  >>> ad.sin(np.pi/2.)
  1.0

  >>> x = DualNumber(np.pi/2)
  >>> ad.sin(x)
  DualNumber(real = 1., dual = 0.)
  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.sin(x.real), np.cos(x.real)*x.dual)
  else:
    return np.sin(x)

def cos(x):
  '''
  Overloads the cos() function. 

  Parameters
  ----------
  x : int or float or DualNumber instance
      Each number represent angle in radians (:math:`2 \pi` rad equals 360 degrees).

  Returns
  -------
  float or DualNumber instance
      
  Examples
  --------
  Print cosine of one angle:

  >>> ad.cos(np.pi/2.)
  0.0

  >>> x = DualNumber(np.pi/2)
  >>> ad.cos(x)
  DualNumber(real = 0., dual = -1.)
  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.cos(x.real), -1*np.sin(x.real)*x.dual)
  else:
    return np.cos(x)

def tan(x):  
  '''
  Overloads the tangent function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance
      
  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.tan(x.real), x.dual/(np.cos(x.real)**2))
  else:
    return np.tan(x)
  
def arcsin(x):
  '''
  Overloads the inverse sine function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance
      
  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.arcsin(x.real),x.dual/np.sqrt(1-x.real**2))
  else:
    return np.arcsin(x)

def arccos(x):
  '''
  Overloads the inverse cosine function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance
      
  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.arccos(x.real),-1*x.dual/np.sqrt(1-x.real**2))
  else:
    return np.arccos(x)

def arctan(x):
  '''
  Overloads the inverse tangent function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance
      
  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.arctan(x.real),x.dual/(1+x.real**2))
  else:
    return np.arctan(x)

#=================== Hyperbolic ===================#
def sinh(x):
  '''
  Overloads the hyperbolic sine function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance

  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.sinh(x.real),x.dual*np.cosh(x.real))
  else:
    return np.sinh(x)  

def cosh(x):
  '''
  Overloads the hyperbolic cosine function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance

  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.cosh(x.real),x.dual*np.sinh(x.real))
  else:
    return np.cosh(x) 

def tanh(x):
  '''
  Overloads the hyperbolic tangent function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance
      
  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.tanh(x.real),x.dual/np.cosh(x.real)**2)
  else:
    return np.tanh(x) 



# -*- coding: utf-8 -*-
"""
This module implements function class, a key component for forward mode autodifferentiation.

"""
import numpy as np

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
        self.x_dim = x_dim
        self.function_list = f #list of functions each returning one output

    def _plugin(self,x): # x is an iterable
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
			
        """
        # Preprocess x
        x = np.array(x).reshape(-1) #accepting all kinds of input and make them into 1-d array
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
    
    def min(self, optimizer='gd', x0=None, verbose=False, **kwargs):
        if optimizer.lower() == 'gd':
            gd = GD(**kwargs)
            results = gd.minimize(self,x_dim=self.x_dim,x0=x0,verbose=verbose)
            return results[1]
        elif optimizer.lower() == 'adam':
            adam = Adam(**kwargs)
            results = adam.minimize(self,x_dim=self.x_dim,x0=x0,verbose=verbose)
            return results[1]
        else:
            raise ValueError('Unidentified optimizer')
            
from abc import abstractmethod


class Optimizer():
    def __init__(self, learning_rate = 0.001, max_iteration = 10000, eps = 1e-15):
        if callable(learning_rate):
            self.eta = learning_rate
        else:
            self.eta = lambda t : learning_rate
        self.max_iteration = max_iteration
        self.eps = eps

    @abstractmethod
    def minimize(self,f, x_dim = 1, x0 = None,verbose=False):
        raise NotImplementedError

class GD(Optimizer):
    def minimize(self,f, x_dim = 1, x0 = None,verbose=False):
        if isinstance(f,function):
            if len(f.function_list) > 1:
                raise TypeError("Cannot optimize vector-valued function")
        else:
            f = function(f,x_dim = x_dim)
        if x0 is None:
            x0 = np.zeros(f.x_dim)
        x = x0
        t = 0
        history = []
        for i in range(self.max_iteration):
            x_new = x - self.eta(t)*f.grad(x)
            if abs(f(x)-f(x_new)) < self.eps:
                x = x_new
                break
            x = x_new
            t += 1
            if verbose:
                history.append((x,f(x)))
        if verbose:
            return x,f(x),history
        else:
            return x,f(x)
    def maximize(self,f, x_dim = 1, x0 = None,verbose=False):
        if isinstance(f,function):
            if len(f.function_list) > 1:
                raise TypeError("Cannot optimize vector-valued function")
            neg_f = function(lambda *x: -1*f.function_list[0](*x),x_dim=x_dim)
        else:
            neg_f = function(lambda *x: -1*f(*x),x_dim = x_dim)
        return self.minimize(neg_f,x_dim=x_dim,x0=x0,verbose=verbose)

class Adam(Optimizer):
    def __init__(self, learning_rate=0.001, max_iteration = 10000, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08):
        super().__init__(learning_rate, max_iteration)
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.epsilon = epsilon

    def minimize(self,f, x_dim = 1, x0 = None,verbose=False):
        if isinstance(f,function):
            if len(f.function_list) > 1:
                raise TypeError("Cannot optimize vector-valued function")
        else:
            f = function(f,x_dim = x_dim)
        if x0 is None:
            x0 = np.zeros(f.x_dim)
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
            x_new = x - self.eta(t)/np.sqrt(v_hat+self.epsilon)*m_hat
            if abs(f(x)-f(x_new)) < self.eps:
                x = x_new
                break
            x = x_new
            t += 1
            if verbose:
                    history.append((x,f(x)))
        if verbose:
            return x,f(x), history
        else:
            return x,f(x)



if __name__=='__main__':

    # # R2 to R2
    # def fcn_f_R2(x1,x2):
    #     return x1**4-100
    # def fcn_g_R2(x1,x2):
    #     return sin(exp(x1))
    # fcn2 = function(fcn_f_R2,fcn_g_R2,x_dim=2)
    # print(fcn2(1,2))
    # print(fcn2.grad(1,2))

    # # R1 to R1
    # def fcn_R1(x1):
    #     return sin(exp(x1)) + 6 * (cos(x1)) / x1 - 2 * x1
        
    # fcn = function(fcn_R1)
    # print(fcn(1))
    # print(fcn.grad(1))

    # adam = Adam()
    # x, min, history = adam.minimize(fcn_f_R2, x_dim = 2,verbose=True)
    # print(min)

    def f1(x):
        return (x-2)**2+7
    f1 = function(f1)
    print(f1.min())

