# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

import jwt
import colemen_utils as c
from flask import request,Blueprint
from apricity_labs import main as _main
from modules.Token import Token as _Token
import settings as _settings
import modules.Result as _result
# import modules.Auth as _Auth
# import modules.API as _api
# import modules.Result as _result


# from modules.Token.routes import token_blueprint
# token_blueprint = Blueprint('token_blueprint', __name__)


def get_bearer_token():
    '''
        Get the bearer token from the request header and validate it.

        ----------

        Return {Token}
        ----------------------
        An instance of the Token if a JWT token is found, None otherwise.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 11-24-2022 19:15:29
        `memberOf`: __init__
        `version`: 1.0
        `method_name`: get_bearer_token
        * @xxx [11-24-2022 19:19:34]: documentation for get_bearer_token
    '''
    ra = _result.Result()
    ra.set_key("reason",None)
    ra.set_key("token",None)
    hdr = request.headers
    if 'authorization' in hdr:
        result = validate_access_token(hdr['authorization'])
        if isinstance(result,(dict)):
            ra.success = True
            _main.log.add("Generating Token From bearer dictionary","info")
            tk = new_token()
            tk.token_type = result['token_type']
            tk.nonce = result['value']
            tk.timestamp = result['iat']
            tk.expiration = result['exp']
            # result = tk
            ra.set_key("token",tk)
        else:
            ra.set_key("reason",result)
        # return result
    else:
        ra.set_key("reason","MISSING_AUTH_HEADER")
        _main.log.add("No authorization header found.","warning")

    return ra

def new_token()->_Token.Token:
    '''
        Create a new instance of a token
        ----------

        Return {Token}
        ----------------------
        An instance of the Token

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 11-24-2022 19:20:09
        `memberOf`: __init__
        `version`: 1.0
        `method_name`: new_token
        * @xxx [11-24-2022 19:21:48]: documentation for new_token
    '''
    return _Token.Token()

def validate_access_token(token):
    '''
        validate a JWT token
        ----------

        Return {str,dict}
        ----------------------
        EXPIRED_ACCESS_TOKEN - if the token is expired
        INVALID_ACCESS_TOKEN - if the token cannot be decoded
        NON_BEARER_TOKEN     - if the authorization field is missing 'bearer'
        The dictionary of token data if successfully decoded

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 11-25-2022 08:17:44
        `memberOf`: __init__
        `version`: 1.0
        `method_name`: validate_access_token
        * @xxx [11-25-2022 08:19:22]: documentation for validate_access_token
    '''
    token = token.split(" ")
    auth_type = token[0]
    token = token[1]

    if auth_type.lower() != "bearer":
        _main.log.add("Non-bearer token provided.","error")
        return "NON_BEARER_TOKEN"

    ac = _settings.auth
    try:
        result = jwt.decode(token,ac.access_token_secret,ac.access_token_algo)
    except jwt.ExpiredSignatureError:
        # print(f"token: {token}")
        # print(e)
        _main.log.add("Access token has expired.","error")
        return "EXPIRED_ACCESS_TOKEN"

    except jwt.exceptions.DecodeError:
        # print(f"token: {token}")
        # print(e)
        _main.log.add("Failed to validate access token.","error")
        return "INVALID_ACCESS_TOKEN"

    _main.log.add("Successfully validated access token.","success")
    return result

