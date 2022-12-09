from .elemFunctions import *
from .dualNum import DualNumber
from .node import Node
from .differentiation import *
import numpy as np

class Forward_AD():
    """A class for performing forward mode automatic differentiation.
    
    Attributes
    ======
        fn : function or list of functions
            The function or list of functions to differentiate
        val : numpy.ndarray
            The values of the function(s) evaluated at the input points
        inputs : list
            The input points at which to evaluate the function(s)
        der : matrix (numpy array)
            The gradient or Jacobian of the function(s) at the input points

    Methods
    ======
        set_fn(fn)
            Sets the function attribute of the class instance
        set_inputs(input_vals)
            Sets the input values to be used to calculate derivative/function values of the class instance
        values(inputs)
            Calculates the function values stored in the class instance at the input values. Calls set_inputs.
        grad(inputs)
            Calculates the gradient or Jacobian of the function stored in the class instance at the input values. Calls set_inputs.
    """

    def __init__(self, fn):
        """Constructor for the Forward_AD class.

        Parameters
        ======
        fn : (function or list of functions)
            The function or list of functions to differentiate
        """
        self.set_fn(fn)

    # setter method for functions
    def set_fn(self, fn):
        """Set the function(s) at which to evaluate the function(s).
        Parameters
        ======
        fn : function or list of functions
            The function or list of functions to differentiate
        """
        # turn function into list if isn't already to be used with jacobian
        if not isinstance(fn,list):
            self.fn = [fn]
        else:
            self.fn = fn

    # setter method for inputs values 
    def set_inputs(self, input_vals):
        """Set the input point(s) at which to evaluate the function(s).

        Parameters
        ======
        input_vals : list
            The input point(s) at which to evaluate the function(s)

        Returns
        =======
        list
            The input point(s)
        """
        self.val = [] # reset values after previous use of class instance
        if not isinstance(input_vals, list):
            input_vals = [input_vals]
        self.inputs = input_vals
        return self.inputs

    # getter method for evaluated function using input values 
    def values(self, inputs):
        """Get the values of the function(s) evaluated at the input points.
        
        Parameters
        ======
        inputs : list
            The input points at which to evaluate the function(s).
        
        Returns
        =======
        numpy array
            The values of the function(s) evaluated at the input points
        """
        self.val = [] # reset values after previous use of class instance
        self.val = np.asarray(get_values(self.fn, self.set_inputs(inputs)))
        return self.val

    # getter method for derivatives using forward mode 
    def grad(self, inputs):
        """Get the derivatives of the function(s) at the input point(s) using forward mode.
        
        Parameters
        ======
        inputs : list
            The input points at which to evaluate the derivatives of the function(s).
        
        Returns
        =======
        matrix (numpy array)
            The values of the first order partial derivatves of the function(s) evaluated at the input points
        """
        self.der = []
        # If no function provided, return index error 
        if len(self.fn) == 0:
            return IndexError('Need at least one function input') 
        # If single function, return gradient of list type 
        elif len(self.fn) == 1: 
            self.der = np.asarray(gradient(self.fn[0], self.set_inputs(inputs)))
            return self.der
        # If vector of functions, return jacobian of numpy array type 
        else:
            self.der = jacobian(self.fn, self.set_inputs(inputs))
            return self.der

class Reverse_AD(Forward_AD):
    """A class for performing reverse mode automatic differentiation.
    
    Attributes
    ======
        fn : function or list of functions
            The function or list of functions to differentiate
        val : numpy.ndarray
            The values of the function(s) evaluated at the input points
        inputs : list
            The input points at which to evaluate the function(s)
        der : matrix (numpy array)
            The gradient or Jacobian of the function(s) at the input points

    Methods
    ======
        set_fn(fn)
            Sets the function attribute of the class instance
        set_inputs(input_vals)
            Sets the input values to be used to calculate derivative/function values of the class instance
        values(inputs)
            Calculates the function values stored in the class instance at the input values. Calls set_inputs.
        grad(inputs)
            Calculates the gradient or Jacobian of the function stored in the class instance at the input values. Calls set_inputs.
    """
    def __init__(self, fn):
        """Constructor for the Reverse_AD class.

        Parameters
        ======
        fn : (function or list of functions)
            The function or list of functions to differentiate
        """
        super().__init__(fn)

    # turn function into list if isn't already to be used with jacobian
    def set_inputs(self, input_vals):
        """Set the input point(s) at which to evaluate the function(s).

        Parameters
        ======
        input_vals : list
            The input point(s) at which to evaluate the function(s)

        Returns
        =======
        list of Nodes
            The input point(s)
        """
        # reset values after previous use of class instance
        self.val = [] 
        # if inputs not in a list, put in list 
        if not isinstance(input_vals, list):
            input_vals = [input_vals]
        # need to make each input of node type 
        self.inputs = [Node(x) for x in input_vals]
        return self.inputs
    
    def values(self, input_vals):
        """Get the values of the function(s) evaluated at the input points.
        
        Parameters
        ======
        input_vals : list
            The input points at which to evaluate the function(s).
        
        Returns
        =======
        numpy array
            The values of the function(s) evaluated at the input points
        """
        input_nodes = self.set_inputs(input_vals)
        values = np.empty([len(self.fn)])
        #get value for each function provided and put in np.array 
        for i, f in enumerate(self.fn):
            z = f(*input_nodes)
            values[i] = (z.value)
        self.val = values
        return self.val

    def grad(self, input_vals):
        """Get the derivatives of the function(s) at the input point(s) using reverse mode.
        
        Parameters
        ======
        inputs : list of Nodes
            The input points at which to evaluate the derivatives of the function(s).
        
        Returns
        =======
        matrix (numpy array)
            The values of the first order partial derivatves of the function(s) evaluated at the input points
        """
        input_nodes = self.set_inputs(input_vals)
        # If no function provided, return index error 
        if len(self.fn) == 0: 
            return IndexError('Need at least one function input') 
        # If one function provided, return gradient of np.array type  
        elif len(self.fn) == 1:
            z = self.fn[0](*input_nodes)
            z.gradient = 1
            gradient_array = np.empty([len(input_nodes)])
            for i, n in enumerate(input_nodes):
                n.grad()
                gradient_array[i] = n.gradient
                n.clear()
            self.der = gradient_array
            return self.der
        # If vector of functions provided, return jacobian of np.array type
        else:
            jacobian = np.empty([len(self.fn), len(input_nodes)])
            for i, f in enumerate(self.fn):
                z = f(*input_nodes)
                z.gradient = 1 
                for j, n in enumerate(input_nodes):
                    n.grad()
                    jacobian[i, j] = n.gradient
                    n.clear()
            self.der = jacobian
            return self.der

