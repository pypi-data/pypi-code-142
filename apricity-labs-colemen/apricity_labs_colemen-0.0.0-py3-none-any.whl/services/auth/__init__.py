# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

import json
import re
import colemen_utils as c
from main import main as _main
# from cerberus import Validator
# import modules.Validator.cerberus as cerberus
from flask import Flask,redirect,url_for,request,Blueprint,make_response

auth_blueprint = Blueprint('auth_blueprint', __name__)


