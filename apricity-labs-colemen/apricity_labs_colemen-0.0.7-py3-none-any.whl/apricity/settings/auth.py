





cookie_name:str = "aesopian"
'''The name of the cookie in which the API access token can be stored.'''

access_token_expiration:int = 3600
'''How many seconds the access token is valid.\n
default:3600'''

access_token_algo:str = "HS256"
'''The algorithm to use for generating the JWT signature.'''

access_token_secret:str = "w9v5K61EJbp8.RDa5GUuOBFbwJhHqX1z2Dep6tO0NJAspac2DxexJBIPH1u6k"
'''The token secret key used for encryption'''

access_token_value_length:int = 128
'''How long (in characters) the value stored in the JWT token & database should be'''





