# -*- coding: utf-8 -*-
"""

This module implement overloading functions to handle arithmetic for dual numbers.

"""

import numpy as np
from .dual_number import DualNumber

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

def _log(x):
  '''
  Computes the natural logarithm. 

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

def log(x,base=None):
  '''
  Overloads the logarithm function for any base

  Parameters
  ----------
  x : int or float or DualNumber instance
  base: int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance

  '''
  if base is None:
    return _log(x)
  return _log(x)/_log(base)

def sqrt(x):
  '''
  Overloads the non-negative square-root function. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance

  '''
  if isinstance(x,DualNumber):
    return DualNumber(np.sqrt(x.real),.5*x.real**-.5*x.dual)
  else:
    return np.sqrt(x)

def sigmoid(x):
  '''
  Computes the sigmoid function evaluated on x. 

  Parameters
  ----------
  x : int or float or DualNumber instance

  Returns
  -------
  float or DualNumber instance

  '''
  return 1/(1+exp(-x))

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


