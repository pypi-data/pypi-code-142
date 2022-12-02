# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import
# pylint: disable=import-outside-toplevel



# import jwt
# import re
# import datetime
# import time
# import colemen_utils as c

from flask import Blueprint
import apricity.objects.Log as log


# from flask import Flask,redirect,url_for,request,Blueprint,make_response
# from apricity_labs import main as _main


home_blueprint = Blueprint('home_blueprint', __name__)
'''Flask Blueprint containing the Home Routes.'''


@home_blueprint.route("/",methods=["GET","POST"])
def home_route():
    log.add("whats up nerd.")
    return "You seem a little lost."


