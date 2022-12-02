# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

# import colemen_utils as c
# from apricity_labs import main as _main
# # from cerberus import Validator
# import modules.Validator.cerberus as cerberus
from flask import Blueprint


# ---------------------------------------------------------------------------- #
#                           IMPORT PACKAGE BLUEPRINT                           #
# ---------------------------------------------------------------------------- #

import apricity.services.auth.routes as auth_routes
auth_blueprint = auth_routes.auth_blueprint






