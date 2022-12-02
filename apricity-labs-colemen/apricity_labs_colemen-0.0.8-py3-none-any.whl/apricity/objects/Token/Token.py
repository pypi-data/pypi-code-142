# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import



import datetime
import time
import jwt
from dataclasses import dataclass


import colemen_utils as c
# from flask import Flask,redirect,url_for,request,Blueprint
# import apricity.objects.Validator as _valid

import apricity.settings as _settings


@dataclass
class Token:

    token_id:int = None
    '''The numeric id of this token in the tokens table.'''

    hash_id:str = f"tk_{c.rand.rand()}"
    '''The hash_id of this token in the tokens table.
    example: tk_cAHxyz1BrRis
    '''

    role_id:int = None
    '''The id of the role associated to this token.'''

    user_id:int = None
    '''The id of the user associated to this token.'''

    session_id:int = None
    '''The id of the session associated to this token.'''

    token_type:str = None
    '''The type of token this is [access]'''

    nonce:str = c.rand.rand(_settings.auth.access_token_value_length)
    '''The Randomly generated value stored in the token'''

    expiration:int = None
    '''When this token will expire as a unix timestamp'''

    timestamp:int = datetime.datetime.now(tz=datetime.timezone.utc)
    '''When this token was created as a unix timestamp\n
    Defaults to the UTC unix timestamp of when this was instantiated.'''

    deleted:int = None
    '''When this token was deleted as a unix timestamp'''

    modified_timestamp:int = None
    '''When this token was last modified as a unix timestamp'''



    def __init__(self):
        # self.main = _main
        # self.app = _main.app
        # self.db = _main.db
        self.settings = {}
        self.data = {}

    def jwt(self):
        '''Generate a JWT from this token's data'''

        data = {}

        ac = _settings.auth
        # dtn = datetime.datetime.now(tz=datetime.timezone.utc)

        data['token_type'] = self.token_type
        data['value'] = self.nonce
        data['exp'] = self.timestamp.timestamp() + datetime.timedelta(seconds=ac.access_token_expiration).total_seconds()
        data['iss'] = "apricity"
        data['iat'] = self.timestamp.timestamp()
        encoded_jwt = jwt.encode(data,ac.access_token_secret,algorithm=ac.access_token_algo,)
        return encoded_jwt


    def set_nonce(self,value=None):
        '''
            Set the value (nonce) of this token.
            ----------

            Arguments
            -------------------------
            `value`=None {str}
                The value of the new nonce, if not provided a random one is generated.


            Return
            ----------------------
            returns nothing

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 11-25-2022 08:20:11
            `memberOf`: Token
            `version`: 1.0
            `method_name`: set_nonce
            * @xxx [11-25-2022 08:21:16]: documentation for set_nonce
        '''
        if value is None:
            value = c.rand.rand(_settings.auth.access_token_value_length)
        self.nonce = value
        self.modified_timestamp = time.time()


def new()->Token:
    return Token()

