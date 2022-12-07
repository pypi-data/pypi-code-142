import jwt
from jwt.exceptions import ExpiredSignatureError
    
my_secret = 't0k#N$#CR#T'


def generateJWTToken(username):
    
    payload_data = {
        "sub": "1313",
        "name": username,
        "nickname": username[0:2]
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


def verifyJWTToken(token):
    
    try:
    
        header_data = jwt.get_unverified_header(token)
        #print("header: ", header_data)
        
        decoded_payload = jwt.decode(
            token,
            key=my_secret,
            algorithms=[header_data['alg'], ]
        )
    
        return decoded_payload

    except ExpiredSignatureError as error:
        print(f'Unable to decode the token, error: {error}')
    
#Testing code here    
if __name__ == '__main__':
    
    username = "Raj"
    
    #Success Scenario
    token = generateJWTToken(username)
    print("\n Generated Token: {}".format(token))

    decodedValue = verifyJWTToken(token)
    print("\n Decoded Payload: {}".format(decodedValue))