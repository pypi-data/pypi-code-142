from .elemFunctions import * 
from .dualNum import DualNumber

_supported_types = (int, float, np.int32, np.int64)

def derivative(fn, x, args=None):
    """Returns derivative of a function.

    Parameters
    ==========
    fn : function
        Defined mulivariable variable function
    args : int, float, np.int32, np.int64
        Values at which the partial derivatives are evalauted at

    Returns
    ==========  
    float
        Derivative of the function evaluated at x

    Examples
    ========== 
    >>> def fn(x):
    >>>     return sin(x)
    >>> print(derivative(fn,0))
    [1.0]

    """

    if args is None:
        return fn(DualNumber(x, 1)).dual

    fn_args = []
    for i, arg in enumerate(args):
        if i == x:
            fn_args.append(DualNumber(arg, 1))
        else:
            fn_args.append(DualNumber(arg, 0))

    return fn(*fn_args)

def gradient(fn, args):
    """Returns directional derivative for multivariate functions.

    Parameters
    ==========
    fn : function
        Defined mulivariable function
    args : int, float, np.int32, np.int64
        Values at which the partial derivatives are evalauted at

    Returns
    ==========  
    vector
        Partial derivatves of function fn -> [df/dx,df/dy]

    Examples
    ========== 

    >>> def fn(x,y):
    >>>    return x**2 + 3*y
    >>> print(gradient(fn,[1,2]))
    [2,3]

    """
    # Initialize empty list which holds gradients of one function 
    grad = []
    # For each variable in function, find the derivative at a given value 
    for i, _ in enumerate(args):
        grad.append(derivative(fn, i, args).dual)
    return grad

def jacobian(fn, args):
    """Returns jacobian vector matrix for multivariate functions.

    Parameters
    ==========
    fn : function
        Defined mulivariable function(s)
    args : int, float, np.int32, np.int64
        Values at which the partial derivatives are evalauted at

    Returns
    ==========  
    matrix (numpy array)
        First order partial derivatves of function(s) fn -> [df1/dx,df1/dy],[df2/dx,df2/dy]

    Examples
    ========== 
    >>> def fn1(x,y):
    >>>     return x + 2*y
    >>> def fn2(x,y):
    >>>     return 2*x + cos(y)
    >>> print(jacobian([fn1,fn2],[0,0]))
    [[1. 2.]
    [2. 0.]]
    
    """
    # Initialize jacobian which holds gradients of each function provided 
    jacob = []
    # For each function, calculate the gradiant and append to the jacobian matrix 
    for i in fn:
        jacob.append(gradient(i, args))
    return np.array(jacob)

def get_values(fn, args):
    """Get values of input function(s) evaluated at input args.
    Parameters
    ==========
    fn : function
        Defined mulivariable variable function(s)
    args : int, float, np.int32, np.int64
        Values at which the partial derivatives are evalauted at

    Returns
    ==========  
    numpy array
        Values of input function(s) fn evaluated at input args
    
    Examples
    ==========
    >>> def fn(x):
    >>>     return sin(x)
    >>> print(get_values([fn],[0]))
    0.
    
    Raises
    =======
        TypeError: Type `[args type]` is not of type list
        TypeError: Type `[args type]` is not supported for non-function type
    """
    # Initial input values must be in a list type 
    if not isinstance(args, list):
        raise TypeError(
            f"Type `{type(args)}` is not of type list"
            )
    # Initial input values inside list must be supported type 
    elif not all(isinstance(n, _supported_types) for n in args):
        raise TypeError(
            f"Items within list are not of type: int, float, np.int32, np.int64"
            )
    # Function must also be within a list 
    elif not isinstance(fn, list):
        raise TypeError(
            f"Type `{type(args)}` is not of type list"
            )
    else:
        # Initialize empty list which holds values
        v = []
        # For each function, append the evaluated function into v
        for f in fn:
            if not callable(f):
                raise TypeError(
                f"Type `{type(f)}` is not supported for non-function type"
                )
            v.append(f(*args))
        return np.array(v)

