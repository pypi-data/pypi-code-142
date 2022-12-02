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

from flask import Blueprint,request
# from apricity_labs import main as _main



acc_blueprint = Blueprint('acc_blueprint', __name__)
'''Flask Blueprint containing the Account Routes.'''


@acc_blueprint.route("/api/1/account/register",methods=["POST","GET"])
def register_route():
    # return "register_route"

    # import services.auth.authorize as _route_module
    # route = _route_module.main()
    # return route.response
    if request.method is "GET":
        return "register_route"
    return "register_route"


@acc_blueprint.route("/api/1/account/login",methods=["POST"])
def login_route():

    # import services.auth.authorize as _route_module
    # route = _route_module.main()
    # return route.response
    return "login_route"

@acc_blueprint.route("/api/1/account/reset-password",methods=["POST"])
def reset_password_route():

    # import services.auth.authorize as _route_module
    # route = _route_module.main()
    # return route.response
    return "reset_password_route"

@acc_blueprint.route("/api/1/account/forgot-password",methods=["POST"])
def forgot_password_route():

    # import services.auth.authorize as _route_module
    # route = _route_module.main()
    # return route.response
    return "forgot_password_route"

@acc_blueprint.route("/api/1/account/confirm-password",methods=["POST"])
def confirm_password_route():

    # import services.auth.authorize as _route_module
    # route = _route_module.main()
    # return route.response
    return "confirm_password_route"




