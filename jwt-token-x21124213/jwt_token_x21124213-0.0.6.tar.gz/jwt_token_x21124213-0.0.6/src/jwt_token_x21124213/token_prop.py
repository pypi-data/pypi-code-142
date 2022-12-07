import jwt
from jwt.exceptions import ExpiredSignatureError
    
my_secret = 't0k#N$#CR#T'

def generateJWTToken(name):
    
    payload_data = {
        "sub": "1313",
        "name": name,
        "nickname": name[0:2]
    }
    
    try:
        token = jwt.encode(
            algorithm='HS256',
            payload=payload_data,
            key=my_secret
        )
        
        return token
        
    except ExpiredSignatureError as error:
        print(f'Unable to encode the token, error: {error}')


def verifyJWTToken(name, token):
    
    try:
    
        header_data = jwt.get_unverified_header(token)
        
        decoded_payload = jwt.decode(
            token,
            key=my_secret,
            algorithms=[header_data['alg'], ]
        )
    
        if name == decoded_payload['name']:
            return True
        
        return False

    except ExpiredSignatureError as error:
        print(f'Unable to decode the token, error: {error}')
    
#Testing code here    
if __name__ == '__main__':
    
    name = "Raj"
    
    #Success Scenario
    token = generateJWTToken(name)
    print("\n Generated Token: {}".format(token))

    is_token_valid = verifyJWTToken(name, token)
    print("\n Token valid: {}".format(is_token_valid))