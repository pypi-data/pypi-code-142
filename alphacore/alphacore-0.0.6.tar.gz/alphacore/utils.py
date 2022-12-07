import numpy as np
import json


def random_xy_data(
    model,
    parameters,
    x=None,
    xmin=None,
    xmax=None,
    size=None,
    sigma=None,
    logspace=False,
    x_positive_only = False,
    seed=None
):
    """
    Generates random data for a scatterplot. Returns the data as x,y

    Parameters
    ----------
    model : object
        A model from utils.linear_models
    parameters : array, list
        The parameters for the model
    x : array, list
        The x data to be used. If not specified, it is generated using xmin, xmax, and size
    xmin : float, int
        The lower x value to use for generating the data. Only used if x is not specified.
    xmax : float, int
        The upper x value to use for generating the data. Only used if x is not specified.
    size : int
        The size of the random data array. If not specified defaults to 1.
    sigma : float, int
        The standard deviation of the normal distribution used for the random noise. If not specified defaults to 1/10th the range of the noiseless x_data and x_data respectively.
    logspace : bool
        If True will provide logspaced data. If False will provide linspaced data. Default is False.
    x_positive_only :
        If True will force all the x data to be positive using abs(x).

    Returns
    -------
    x, y : tuple
        A tuple of arrays of the x and y data.
    """

    if seed is not None:
        np.random.seed(seed)

    if x is None:
        if xmin is None:
            xmin = 0
        if xmax is None:
            xmax = 10
        if xmin > xmax:
            xmin, xmax = xmax, xmin
        if size is None:
            size = 1
        if logspace is True:
            x = np.geomspace(xmin, xmax, size)
        else:
            x = np.linspace(xmin, xmax, size)
    x_range = max(x)-min(x)
    if sigma is None:
        sigma_x = x_range / 10
    else:
        sigma_x = sigma
    x_noise = np.random.normal(loc=0, scale=sigma_x, size=len(x))
    x_data = x + x_noise
    if x_positive_only is True:
        x_data = abs(x_data)

    y_true = model(x_data, *parameters)
    y_range = max(y_true) - min(y_true)
    if sigma is None:
        sigma_y = y_range / 10
    else:
        sigma_y = sigma
    y_noise = np.random.normal(loc=0, scale=sigma_y, size=len(x))
    y_data = y_true + y_noise
    return x_data, y_data


class linear_models:
    """
    A collection of linear models
    """

    @staticmethod
    def linear(x, a, b):
        """
        Straight line
        y = a * x + b
        """
        return a * x + b

    @staticmethod
    def poly_2(x, a, b, c):
        """
        Quadratic
        y = a * x**2 + b * x + c
        """
        return a * x**2 + b * x + c

    @staticmethod
    def poly_3(x, a, b, c, d):
        """
        Cubic
        y = a * x**3 + b * x**2 + c * x + d
        """
        return a * x**3 + b * x**2 + c * x + d

    @staticmethod
    def poly_4(x, a, b, c, d, e):
        """
        Quartic
        y = a * x**4 + b * x**3 + c * x**2 + d * x + e
        """
        return a * x**4 + b * x**3 + c * x**2 + d * x + e

    @staticmethod
    def poly_5(x, a, b, c, d, e, f):
        """
        Quintic
        y = a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f
        """
        return a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f

    @staticmethod
    def poly_6(x, a, b, c, d, e, f, g):
        """
        Sextic
        y = a * x**6 + b * x**5 + c * x**4 + d * x**3 + e * x**2 + f * x + g
        """
        return (
            a * x**6 + b * x**5 + c * x**4 + d * x**3 + e * x**2 + f * x + g
        )

    @staticmethod
    def logarithmic(x, a, b, c):
        """
        Logarithmic
        y = a * np.log(b * x) + c
        """
        return a * np.log(b * x) + c

    @staticmethod
    def exponential(x, a, b, c):
        """
        Exponential
        y = a * np.exp(b * x) + c
        """
        return a * np.exp(b * x) + c

    @staticmethod
    def power(x, a, b):
        """
        Power
        y = a * x**b
        """
        return a * x**b


def removeNegativesInX(x,y=None):
    '''
    Removes negatives from a list or array.

    Parameters
    ----------
    x : array, list
        The first array or list to be processed.
    y : array, list, optional
        The second array or list to be processed.

    Returns
    -------
    x_out : list, array
        A list or array of the same type as x input with the negatives removed.
    y_out : list, array
        A list or array of the same type as y input with the negatives removed.

    '''

    if y is not None:
        if type(x) == list:
            x = np.asarray(x)
            y = np.asarray(y)
            arr_out = False
        else:
            arr_out = True
        x_out = x[x>0]
        y_out = y[x>0]
        if arr_out is False:
            x_out = x_out.tolist()
            y_out = y_out.tolist()
        return x_out, y_out
    else:
        if type(x) == list:
            x = np.asarray(x)
            arr_out = False
        else:
            arr_out = True
        x_out = x[x>0]
        if arr_out is False:
            x_out = x_out.tolist()
        return x_out


def removeNaNs(x,y=None):
    """
    Removes NaNs and inf from a list or array.

    Parameters
    ----------
    x : array, list
        The first array or list to be processed.
    y : array, list, optional
        The second array or list to be processed.

    Returns
    -------
    x_out : list, array
        A list or array of the same type as x input with the NaNs removed.
    y_out : list, array
        A list or array of the same type as y input with the NaNs removed.


    Notes
    -----
    This is better than simply using "x = x[numpy.logical_not(numpy.isnan(x))]"
    as numpy crashes for str and bool.
    """
    if y is not None:
        if len(x) != len(y):
            raise ValueError('x and y must be the same length')
        if type(x) == np.ndarray:
            x = list(x)
            y = list(y)
            arr_out = True
        else:
            arr_out = False
        x_out = []
        y_out = []
        for i in range(len(x)):
            keep_x,keep_y = 0,0
            xi = x[i]
            yi = y[i]
            if type(xi) in [str, bool, np.str_]:
                if xi not in ["nan","inf"]:
                    keep_x = 1
            elif type(xi) in [int, float, np.int16, np.int32, np.float16, np.float32, np.float64]:
                if np.logical_not(np.isnan(xi)) and np.logical_not(np.isinf(xi)):  # this only works for numbers
                    keep_x = 1
            else:
                raise ValueError('Unexpected type in X: ',str(type(xi)))
            if type(yi) in [str, bool, np.str_]:
                if yi not in ["nan", "inf"]:
                    keep_y = 1
            elif type(yi) in [int, float, np.int16, np.int32, np.float16, np.float32, np.float64]:
                if np.logical_not(np.isnan(yi)) and np.logical_not(np.isinf(yi)):  # this only works for numbers
                    keep_y = 1
            else:
                raise ValueError('Unexpected type in X: ',str(type(xi)))

            keep = keep_x * keep_y
            if keep == 1:
                x_out.append(xi)
                y_out.append(yi)

        if arr_out is True:
            x_out = np.asarray(x_out)
            y_out = np.asarray(y_out)
        return x_out, y_out
    else:
        if type(x) == np.ndarray:
            x = list(x)
            arr_out = True
        else:
            arr_out = False
        out = []
        for i in x:
            if type(i) in [str, bool, np.str_]:
                if i not in ["nan","inf"]:
                    out.append(i)
            elif np.logical_not(np.isnan(i)) and np.logical_not(np.isinf(i)):  # this only works for numbers
                out.append(i)
        if arr_out is True:
            out = np.asarray(out)
        return out

def printObject(object):
    """
    This function provides a simplified way of extracting all the values from an
    object and printing them.
    """
    object_dict = object.__dict__
    keys = object_dict.keys()
    for item in keys:
        print(item, "=", object_dict[item])
    print("")


class objectConverters:
    '''
    Converters for python objects. Includes:
    List to Dictionary
    List to Object
    Dictionary to Object
    '''

    def list2dict(keys, values):
        '''
        Generates a dictionary using keys and values
        '''
        return dict(zip(keys, values))

    @staticmethod
    class list2object:
        '''
        Generates an object using keys and values
        '''
        def __init__(self,keys,values,object_to_use=None):
            if len(keys) == len(values):
                for i in range(len(keys)):
                    if object_to_use is None:
                        setattr(self, keys[i], values[i])
                    else:
                        setattr(object_to_use, keys[i], values[i])
            else:
                raise ValueError('number of keys does not match number of values')

    @staticmethod
    class dict2object:
        '''
        Generates an object from a dictionary
        '''
        def __init__(self, dictionary=None, object_to_use=None):
            if dictionary is not None:
                for key, value in dictionary.items():
                    if object_to_use is None:
                        setattr(self, key, value)
                    else:
                        setattr(object_to_use, key, value)

    @staticmethod
    def object2dict(object_to_use):
        '''
        Generates a dictionary from an object
        '''
        dict_out = object_to_use.__dict__
        return dict_out

    @staticmethod
    def object2json(object_to_use):
        '''
        Generates json object from a python object
        '''
        json_out = json.dumps(vars(object_to_use))
        return json_out