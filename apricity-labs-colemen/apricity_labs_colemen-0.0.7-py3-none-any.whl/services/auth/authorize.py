# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import


import jwt
import re
import datetime
# import time
import colemen_utils as c

from flask import Flask,redirect,url_for,request,Blueprint,make_response
from apricity_labs import main as _main
from modules.Route import Route
import modules.Validator as _valid
import modules.Token as _token


class RouteMain(Route):

    def __init__(self):
        super().__init__()
        self.settings={}
        self.data={}

        self.name = "API authorization"
        self.add_method("POST")

        self.form_data_required = False

        self.validation_schema = {}

    def master(self):
        result = self._validate()
        if self.token is not None:
            tk:_token._Token.Token = self.token
            # tk:_token._Token.Token = result.get_key("token")
            tk.set_nonce()
            self.result.data = {
                "access":tk.jwt()
            }
        else:
            result = _token.get_bearer_token()
            if result.success is False:
                reason = result.get_key("reason")
                if reason in ["MISSING_AUTH_HEADER","EXPIRED_ACCESS_TOKEN"]:
                    self.gen_new_token()
                    self.result.success = True
                    self.response.status_code = 200
                elif reason in ["INVALID_ACCESS_TOKEN","NON_BEARER_TOKEN"]:
                    return



    def gen_new_token(self):
        tk = _token.new_token()
        tk.set_nonce()
        self.result.data = {
            "access":tk.jwt()
        }



def main()->RouteMain:
    _main.log.add("Generate API Authorization.")
    route_instance = RouteMain()
    route_instance.master()
    return route_instance

