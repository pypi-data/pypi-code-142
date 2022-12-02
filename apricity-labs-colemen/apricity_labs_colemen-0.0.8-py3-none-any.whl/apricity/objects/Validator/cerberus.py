# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

# import json
# import time
import re
# import colemen_utils as c
# from apricity_labs import main as _main
from cerberus import Validator
import apricity.objects.Result as _result


def single_value(field,schema:dict,value):
    '''
        validate a value using the cerberus library
        ----------

        Arguments
        -------------------------
        `field` {str}
            The field name to validate.

        `schema` {dict}
            A dictionary of validation rules to use.

            {
                'type': 'string',
                'empty': False,
                'nullable': False,
                'required': True,
                'minlength': 3,
                'maxlength': 255,
            }

        `value` {any}
            The value to be validated.

        Return {tuple}
        ----------------------
        (result,Validator)

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 11-23-2022 08:47:13
        `memberOf`: cerberus
        `version`: 1.0
        `method_name`: single_value
        * @TODO []: documentation for single_value
    '''
    vdict = {field:value}
    if field not in schema:
        schema = {field:schema}
    sdict = {field:schema[field]}
    return validate_from_schema(sdict,vdict)


def validate_from_schema(schema:dict,value:dict)->_result.Result:
    ra = _result.Result()
    errors = {}

    v = Validator(schema)
    ra.success = v.validate(value)
    if ra.success is False:
        for field,val in v.errors.items():
            if field not in errors:
                errors[field] = []
            errors[field].append(val[0])


    ra.set_key('errors',errors)
    return ra



def is_email(field,value,error):
    if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',value) is None:
        error(field,"invalid email")


def alpha_only(field,value,error):
    if re.match(r'^[a-zA-Z]*$',value) is None:
        error(field,"non alphabetic characters")

def alphanumeric_only(field,value,error):
    if re.match(r'^[a-zA-Z0-9]*$',value) is None:
        error(field,"non alphanumeric characters")

def numeric_only(field,value,error):
    if re.match(r'^[0-9]*$',value) is None:
        error(field,"non-numeric characters")

def phone_number(field,value,error):
    if re.match(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',value) is None:
        error(field,"invalid phone number")







