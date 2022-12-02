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

from flask import Flask,Blueprint,make_response,render_template
# from apricity_labs import main as _main
import apricity_labs
app:Flask = apricity_labs.main.app


# acc_blueprint = Blueprint('acc_blueprint', __name__)
# '''Flask Blueprint containing the Account Routes.'''



# @app.errorhandler(404)
def not_found(e):
    '''
        Handles the 404 error and generates a response.
        ----------

        Arguments
        -------------------------
        `e`
            The flask error error

        Return {type}
        ----------------------
        return_description

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 12-02-2022 08:18:58
        `memberOf`: routes
        `version`: 1.0
        `method_name`: not_found
        * @TODO []: documentation for not_found
        
        * @TODO []: Create 404 response template
    '''
    # return make_response("nothing to see here", 404)
    return "404 bitch"


app.register_error_handler(404,not_found)

