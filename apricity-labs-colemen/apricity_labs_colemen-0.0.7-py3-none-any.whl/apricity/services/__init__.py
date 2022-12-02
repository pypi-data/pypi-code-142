# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

'''
    This module is used to define the services that the API provides.

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 12-01-2022 16:57:15
    `memberOf`: __init__
    `version`: 1.0
    `method_name`: service
'''


import apricity.services.auth as auth
import apricity.services.home as home
import apricity.services.account as account
import apricity.services.errors

blue_prints = []
blue_prints.append(auth.auth_blueprint)
blue_prints.append(home.home_blueprint)
blue_prints.append(account.acc_blueprint)





