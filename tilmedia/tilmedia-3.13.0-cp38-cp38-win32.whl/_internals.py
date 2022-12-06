import logging
import numpy as np
from copy import deepcopy
from ctypes import c_int, c_char_p, CFUNCTYPE
from .exceptions import TILMediaErrorIncompatibleVectorLength, TILMediaError
from .core import BatchFunctionCaller_abort
from .properties import property_information

_tilmedia_message_c_functions = []
_tilmedia_error_c_functions = []
_logger_exceptions = {
    'fatal': True,
    'info': True
}

_handler = logging.StreamHandler()
_formatter = logging.Formatter()
_logger = logging.getLogger('TILMedia')
_logger.setLevel(logging.INFO)
_logger.addHandler(_handler)


CPRINTFUNCTION = CFUNCTYPE(c_int, c_char_p)
""" The following statements define a callback c-function for interaction with the python callback compatibility dll"""


def tilmedia_message_logger_function(exceptions: list, medium_wrapper: list, logger: logging.Logger, val):
    val = val.decode('utf8', errors='ignore')
    if val[-1] == '\n':
        val = val[:-1]
    logger.info(val)
    if exceptions is not None and _logger_exceptions['info']:
        exceptions.append(TILMediaError(val))
        if medium_wrapper and medium_wrapper[0] != 0:
            BatchFunctionCaller_abort(medium_wrapper[0])
    return 0


def tilmedia_error_logger_function(exceptions: list, medium_wrapper: list, logger: logging.Logger, val):
    val = val.decode('utf8', errors='ignore')
    if val[-1] == '\n':
        val = val[:-1]
    logger.error(val)
    if exceptions is not None and _logger_exceptions['fatal']:
        exceptions.append(TILMediaError(val))
        if medium_wrapper and medium_wrapper[0] != 0:
            BatchFunctionCaller_abort(medium_wrapper[0])
    # raise TILMediaError(val) # not handled well, c code after this call is still executed.
    return 0


def set_logger(logger: logging.Logger) -> None:
    """
    set the global logger (logging module) instance. The global logger instance is used, if no local one (instance constructor argument) was given.

    Args:
        logger (logging.Logger): logger instance
    """
    global _tilmedia_message_c_functions
    global _tilmedia_error_c_functions
    if logger is None:
        logger = logging.getLogger('TILMedia')
    globals()['_logger'] = logger


def set_logger_exceptions(log_level, active: bool):
    """
    activate the exceptions of the global logger for a specific log level.

    Args:
        log_level (str): either "fatal" or "info"
        active (bool): activate exceptions
    """

    globals()['_logger_exceptions'][log_level] = active


def var_normalize_inputs(*args) -> tuple:
    """
    align the sizes of all inputs. The last input is expected to be a concentration vector with one additional dimension.

    Raises:
        TILMediaError: incompatible vector lengths

    Returns:
        tuple: same order as args, just aligned sizes
    """
    array_shapes = []
    # var_are_arrays = []
    arrays = []
    for arg in args:
        if isinstance(arg, np.ndarray):
            var = arg
        else:
            var = np.array(arg)
        # if var.shape != ():
        #     var_are_arrays.append(True)
        array_shapes.append(var.shape)
        arrays.append(var)

    # vectorized arguments
    shapes = [v.shape for v in arrays]
    # remove concentration dimension
    shapes_wo_concentration = deepcopy(shapes)
    shapes_wo_concentration[-1] = shapes_wo_concentration[-1][:-1]

    # get the shape with the highest number of dimensions
    highest_dim_shape = sorted(shapes_wo_concentration, key=lambda x:len(x))[-1]
    if highest_dim_shape == tuple():
        highest_dim_shape = (1,)

    # missing dimensions at the beginning are filled with highest_dim_shape
    vectorized_shapes_wo_concentration = [
        tuple(
            list(highest_dim_shape[:len(highest_dim_shape)-len(shape)])
            + list(shape)
        )
        for shape in shapes_wo_concentration
    ]
    vectorized_shapes = deepcopy(vectorized_shapes_wo_concentration)
    vectorized_shapes[-1] = tuple(list(vectorized_shapes[-1]) + [arrays[-1].shape[-1]])

    vectorizations = set(vectorized_shapes_wo_concentration)
    if len(vectorizations) > 1:
        raise TILMediaErrorIncompatibleVectorLength("incompatible vector lengths of inputs")

    # missing dimensions at the beginning are filled with highest_dim_shape
    tile_shapes = [
        tuple(
            list(highest_dim_shape[:len(highest_dim_shape)-len(shape)])
            + [1]*len(shape)
        )
        for shape in shapes_wo_concentration
    ]
    # add concentration dimension
    tile_shapes[-1] = tuple(list(tile_shapes[-1]) + [1])

    normalized_arrays = []
    for expected_shape, tile_shape, var in zip(vectorized_shapes, tile_shapes, arrays):
        if var.shape == expected_shape:
            normalized_arrays.append(var)
        else:  # if var.shape == tuple():
            normalized_arrays.append(np.tile(var, tile_shape))
        # else:
        #     raise TILMediaError("unexpected error handling the vector inputs")

    return tuple(normalized_arrays)


def check_vector_size(vector: np.ndarray, expected: int):
    """
    compare the sizes of a vector and with the expected value. If they dont match raise an exception.

    Args:
        vector (np.ndarray): input vector
        expected (int): expected composition length

    Raises:
        TILMediaErrorIncompatibleVectorLength: length mismatch
    """
    if vector.shape[-1] != expected:
        raise TILMediaErrorIncompatibleVectorLength(
            'The composition vector length is ' + str(vector.shape[-1]) + ' but should be ' + str(expected))


def _generate_code(property_list: list):
    code_a = []
    code_b = []
    for name, _, mixture_dim, _ in property_list:
        info = property_information.get(name, {})
        if mixture_dim is None:
            template_a = (
                '        self.{name} = np.{data_type}(0)\n'
                "        '{escaped_description} [{unit}]'"
            )
            template_b = '        self._{name}_vector = np.zeros(1, dtype=np.{data_type})'
        else:
            template_a = (
                '        self.{name} = np.zeros((1, {n}), dtype=np.{data_type})\n'
                "        '{escaped_description} [{unit}]'"
            )
            template_b = '        self._{name}_vector = np.zeros((1, {n}), dtype=np.{data_type})'

        args = {
            'name': name,
            'data_type': info.get('numpy_type', ''),
            'unit': info.get('unit', ''),
            'description': info.get('description', ''),
            'n': max(0, 1 + mixture_dim if mixture_dim is not None else 0)
        }
        code_a.append(template_a.format(**args))
        code_b.append(template_b.format(**args))
    return code_a + [''] + code_b
