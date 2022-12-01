# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

import json
import re
import colemen_utils as c
from apricity_labs import main as _main
from cerberus import Validator
import modules.Validator.cerberus as cerberus



# # define Python user-defined exceptions
# class Error(Exception):
#     """Base class for other exceptions"""
#     pass


# class ValueTooSmallError(Error):
#     """Raised when the input value is too small"""
#     pass

# class ValueTooLargeError(Error):
#     """Raised when the input value is too large"""
#     pass

# class ValueTooLong(Error):
#     """Raised when the input value has too many characters"""
#     pass


def is_email(value):
    if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',value) is None:
        return False
    return True

def integer_id(value)->bool:
    '''
        Determine if the value is a valid integer id.
        ----------

        Arguments
        -------------------------
        `value` {any}
            The value ot validate.


        Return {bool}
        ----------------------
        True if the value is an integer greater than zero, false otherwise.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 11-27-2022 18:48:21
        `memberOf`: __init__
        `version`: 1.0
        `method_name`: integer_id
        * @xxx [11-27-2022 18:49:52]: documentation for integer_id
    '''
    if isinstance(value,(int)):
        if value > 0:
            return True
    return False



def sql_type_to_python_type(value:str)->str:
    '''
        Convert an SQL type to its PHP equivalent.
        ----------

        Arguments
        -------------------------
        `value` {str}
            The SQL type to convert.


        Return {str}
        ----------------------
        The converted type string, or the original string if no conversion occurred.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 11-27-2022 19:23:42
        `memberOf`: __init__
        `version`: 1.0
        `method_name`: sql_type_to_python_type
        * @xxx [11-27-2022 19:24:14]: documentation for sql_type_to_python_type
    '''
    if value in ["decimal","float"]:
        return "float"
    elif value in ["bigint","int","integer"]:
        return "integer"
    elif value in ["tinyint"]:
        return "boolean"
    elif value in ["varchar"]:
        return "string"
    elif value in ["timestamp"]:
        return "string"
    else:
        return value



