# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

import json
import colemen_utils as c
# from flask import Flask,redirect,url_for,request,Blueprint
# from apricity_labs import main as _main




class Result:
    app = None
    main = None

    def __init__(self):
        # self.main = _main
        # self.app = _main.app
        self.settings = {}
        self._data = {
            "success":False,
            "data":None,
            "public_response":None,
        }

    @property
    def json(self):
        '''
            Get the json property's value

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 11-21-2022 16:09:59
            `@memberOf`: __init__
            `@property`: json
        '''
        data = {
            "success":self.success,
            "data":self.data,
            "public_response":self.public_response,
        }
        return json.dumps(data)
        

    @property
    def success(self)->bool:
        '''
            Get the success value.

            `default`:False


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 11-21-2022 16:07:36
            `@memberOf`: PostArg
            `@property`: success
        '''
        value = c.obj.get_arg(self._data,['success'],False,(bool))
        return value

    @success.setter
    def success(self,value):
        '''
            Set the success value.

            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 11-21-2022 16:07:36
            `@memberOf`: PostArg
            `@property`: success
        '''
        self._data['success'] = c.types.to_bool(value)

    @property
    def data(self):
        '''
            Get the data value.

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 11-21-2022 16:08:46
            `@memberOf`: PostArg
            `@property`: data
        '''
        value = c.obj.get_arg(self._data,['data'],None)
        return value

    @data.setter
    def data(self,value:dict):
        '''
            Set the data value.

            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 11-21-2022 16:08:46
            `@memberOf`: PostArg
            `@property`: data
        '''
        self._data['data'] = value

    @property
    def public_response(self)->str:
        '''
            Get the public_response value.

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 11-21-2022 16:09:26
            `@memberOf`: PostArg
            `@property`: public_response
        '''
        value = c.obj.get_arg(self._data,['public_response'],None,(str))
        return value

    @public_response.setter
    def public_response(self,value:str):
        '''
            Set the public_response value.

            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 11-21-2022 16:09:26
            `@memberOf`: PostArg
            `@property`: public_response
        '''
        self._data['public_response'] = str(value)


    def set_key(self,key,value):
        d = self.data
        if d is None:
            d = {}
        d[key] = value
        self.data = d

    def get_key(self,key,default=None,value_type=None):
        d = self.data
        if isinstance(d,(dict)) is False:
            return default

        result = c.obj.get_arg(d,key,default,value_type)
        return result

    # def add_field_error(self,field:str,error:_Union(str,list)):
    #     error = c.arr.force_list(error)

    #     errors = c.obj.get_arg(self.data,['errors'],{},dict)
    #     if field not in errors:
    #         errors[field] = []
    #     errors[field] = c.arr.remove_duplicates(errors[field] + error)

    #     self.data['data']['errors'] = errors

