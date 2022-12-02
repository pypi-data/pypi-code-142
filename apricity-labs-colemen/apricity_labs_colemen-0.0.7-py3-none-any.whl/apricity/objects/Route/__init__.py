# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

import json
import importlib
from dataclasses import dataclass, field
from typing import Iterable, Union
import colemen_utils as c
from flask import Flask,redirect,make_response,request,Blueprint
from typing import List

# from apricity_labs import main as _main
import apricity.settings as _settings
import apricity.objects.Validator as _valid
import apricity.objects.Token as _token
import apricity.objects.Result as _result
# from settings.types import _Union


def load_route(module:str):
    route_instance = None
    route_module = importlib.import_module(module)
    valid_method = getattr(route_module, "main", None)
    if callable(valid_method):
        route_instance = valid_method()
    return route_instance

@dataclass
class Route:
    name:str = None
    '''The human name for this route.'''



    # main:_main = _main
    # app:Flask = _main.app

    # allowed_methods:list = None
    allowed_methods =None
    '''A list of allowed request methods for this route specifically'''

    _response = None
    '''The flask response for this route.'''


    result:_result.Result = None
    '''The result array for this route'''

    token:_token.Token.Token = None
    '''The validated bearer Token instance'''


    form_data_required:bool = False
    '''If True, the request data MUST have a value.'''

    form_data_type:str = 'json'
    '''The expected data type for the request.
    Default: json'''

    data:any = None
    '''The data provided with the request.'''

    validation_schema:dict = None
    '''The cerberus validation schema used for validating the request body'''

    validation_errors:dict = None
    '''The errors generated while validating the request data values.'''


    def __init__(self):
        self.settings = {}
        self.data = {}
        self._response = make_response()
        self.result = _result.Result()

    def _validate(self):

        self._response.status_code = 200
        output = False
        # result = _result.Result()
        validations = [
            "_validate_authorization",
            "_validate_method",
            "_validate_data_provided",
            "_validate_data_type",
            "_validate_form_data"
        ]

        for valid in validations:
            valid_method = getattr(self, valid, None)
            if callable(valid_method):
                output = valid_method()
                if output is False:
                    # result.success = False
                    # result.set_key(valid_method,False)
                    break
        return output
        # self.validate_authorization()
        # self.validate_method()
        # self.validate_form_data()

    @property
    def response(self):
        '''
            Get this routes Response object with data

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 11-25-2022 09:41:06
            `@memberOf`: __init__
            `@property`: response
        '''
        self._response.set_data(self.result.json)
        return self._response

    def _validate_authorization(self):
        '''
            Retrieve the bearer token from the request and validate its value.
            ----------

            Return {bool}
            ----------------------
            True if the token is found and successfully validated,
            False otherwise.

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 11-25-2022 08:22:37
            `memberOf`: __init__
            `version`: 1.0
            `method_name`: validate_authorization
            * @xxx [11-25-2022 08:23:33]: documentation for validate_authorization
        '''
        result = _token.utils.get_bearer_token()
        if result.success is False:
            reason = result.get_key("reason")
            if reason in ["MISSING_AUTH_HEADER","NON_BEARER_TOKEN","EXPIRED_ACCESS_TOKEN","INVALID_ACCESS_TOKEN"]:
                self._response.status_code = 401
                self.result.success = False
                self.result.public_response = "Nothing to see here"
                self._response.headers.add_header("WWW-Authenticate","Bearer")
                return False

        self.token = result.get_key("token")
        return True

    def _validate_method(self)->bool:
        '''
            validate that the request's method is valid and allowed for this route.
            ----------

            Return {bool}
            ----------------------
            True if the request method is valid and allowed to be used on this route specifically.

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 11-25-2022 09:13:11
            `memberOf`: __init__
            `version`: 1.0
            `method_name`: validate_method
            * @xxx [11-25-2022 09:39:09]: documentation for validate_method
        '''
        if request.method not in _settings.master_control.valid_request_methods:
            # _main.log.add("Unrecognized Request Method","error")
            self._response.status_code = 405
            self._response.headers.add_header("Allow",', '.join(self.allowed_methods))
        if request.method in self.allowed_methods:
            # _main.log.add("Successfully Validated Request Method","success")
            return True
        return False

    def add_method(self,method:Union[Iterable[str],str])->bool:
        '''
            Add request method(s) to this route.

            ----------

            Arguments
            -------------------------
            `method` {list,str}
                A single method or a list of allowed methods.

            Return {bool}
            ----------------------
            True upon success, false otherwise.
            If a list is provided, ALL methods must be added successfully for a True response.

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 11-25-2022 09:33:52
            `memberOf`: __init__
            `version`: 1.0
            `method_name`: add_method
            * @TODO []: documentation for add_method
        '''
        methods_added = False
        method = c.arr.force_list(method)
        methods = [x.upper() for x in method]

        am = [] if self.allowed_methods is None else self.allowed_methods

        for meth in methods:
            if meth not in _settings.master_control.valid_request_methods:
                continue
            elif meth in am:
                continue
            else:
                self.allowed_methods = am.append(meth)
                methods_added = True



        return methods_added



    def _validate_data_provided(self):
        '''
            Confirm that the request contains a data attribute that has a value
            other than None.
            ----------

            Return {bool}
            ----------------------
            True upon success, false otherwise.

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 11-25-2022 09:52:05
            `memberOf`: __init__
            `version`: 1.0
            `method_name`: validate_data_provided
            * @xxx [11-25-2022 09:52:46]: documentation for validate_data_provided
        '''
        if self.form_data_required is True:
            if request.data is None:
                self.response.status_code = 400
                self.result.success = False
                self.result.public_response = "Forgetting something?"
                return False
        return True

    def _validate_data_type(self):
        '''
            Validate that the request data is of the correct type.

            If the form_data_type is json, the request data is parsed as json.
            If it is successfully parsed, this will return True, False otherwise.

            If no data is provided, this will always return True.

            ----------

            Return {bool}
            ----------------------
            True upon success, false otherwise.

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 11-25-2022 09:59:06
            `memberOf`: __init__
            `version`: 1.0
            `method_name`: validate_data_type
            * @TODO []: documentation for validate_data_type
        '''
        self.data = request.data
        if self.data is None:
            return True

        if self.form_data_type == 'json':
            # @Mstep [] convert the data from bytes to utf-8 string for parsing.
            if isinstance(request.data,(bytes)):
                self.data = self.data.decode("utf-8")
            try:
                data = json.loads(self.data)
                self.data = data
            except json.JSONDecodeError:
                self.response.status_code = 400
                self.result.success = False
                self.result.public_response = "These things you say make no sense."
                return False
        return True

    def _validate_form_data(self):
        if self.data is None:
            return True
        if hasattr(self,'validation_schema') is False:
            raise Exception(f"Route {self.name} has no validation_schema")

        if isinstance(self.data,(dict)):
            raise Exception(f"Route {self.name} has no request_form_data")

        ra = _valid.cerberus.validate_from_schema(self.validation_schema,self.data)
        # v = Validator(self.validation_schema)
        # result = v.validate(self.request_data)

        if ra.success is False:
            self.validation_errors = ra.get_key("errors")
            self.response.status_code = 400
            self.result.public_response = "Correct the errors and try again."
            self.result.set_key("errors",self.validation_errors)
            return False
        return True


    def log_request(self):
        return None
    # def add_validation_error(self,field,error):
    #     errors = self.validation_errors
    #     if field not in errors:
    #         errors[field] = []
    #     errors[field].append(error)

    #     self.validation_errors = errors





