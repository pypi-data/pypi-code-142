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

from flask import Flask,redirect,url_for,request,Blueprint,make_response
# from apricity_labs import main as _main



auth_blueprint = Blueprint('auth_blueprint', __name__)
'''Flask Blueprint containing the Authorization Routes.'''


@auth_blueprint.route("/api/1/auth",methods=["POST"])
def auth_route():
    # import modules.Route as _route
    # route = _route.load_route("services.user.register")
    # route.master()

    import services.auth.authorize as _route_module
    route = _route_module.main()
    
    
    return route.response


