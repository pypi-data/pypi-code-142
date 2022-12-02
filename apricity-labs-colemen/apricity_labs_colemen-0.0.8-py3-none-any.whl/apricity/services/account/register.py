# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import


# import jwt
# import re
# import datetime
# import time
# import colemen_utils as c

# from flask import Flask,redirect,url_for,request,Blueprint,make_response
from apricity.objects.Route import Route
import apricity.objects.Validator as _valid
import apricity.objects.Log as log





class RouteMain(Route):

    def __init__(self):
        super().__init__()
        self.settings={}
        self.data={}

        self.name = "Account"
        self.add_method("POST")

        self.form_data_required = False

        self.validation_schema = {
            'first_name':{
                'type': 'string',
                'empty': False,
                'nullable': False,
                'required': True,
                'minlength': 3,
                'maxlength': 255,
            },
            'last_name':{
                'type': 'string',
                'empty': False,
                'nullable': False,
                'required': True,
                'minlength': 3,
                'maxlength': 255,
            },
            'email':{
                'type': 'string',
                'empty': False,
                'nullable': False,
                'required': True,
                'minlength': 3,
                'maxlength': 100,
                'check_with':_valid.cerberus.is_email
            },
            'password':{
                'type': 'string',
                'empty': False,
                'nullable': False,
                'required': True,
                'minlength': 3,
                'maxlength': 100,
            }
        }

    def master(self):
        result = self._validate()




    # def gen_new_token(self):
    #     tk = _token.new_token()
    #     tk.set_nonce()
    #     self.result.data = {
    #         "access":tk.jwt()
    #     }



def main()->RouteMain:
    log.add("Register for an account.")
    route_instance = RouteMain()
    route_instance.master()
    return route_instance

