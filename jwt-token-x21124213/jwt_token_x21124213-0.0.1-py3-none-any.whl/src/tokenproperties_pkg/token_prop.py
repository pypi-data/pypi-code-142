import jwt
from jwt.exceptions import ExpiredSignatureError

class TokenGenerator():
    
    my_secret = 't0k#N$#CR#T'
    
    def generateJWTToken(self, username):
        
        payload_data = {
            "sub": "1313",
            "name": username,
            "nickname": username[0:2]
        }
        
        try:
            token = jwt.encode(
                algorithm='HS256',
                payload=payload_data,
                key=self.my_secret
            )
            
            return token
            
        except ExpiredSignatureError as error:
            print(f'Unable to encode the token, error: {error}')
    
    def verifyJWTToken(self, token):
        
        try:
        
            header_data = jwt.get_unverified_header(token)
            #print("header: ", header_data)
            
            decoded_payload = jwt.decode(
                token,
                key=self.my_secret,
                algorithms=[header_data['alg'], ]
            )
        
            return decoded_payload
    
        except ExpiredSignatureError as error:
            print(f'Unable to decode the token, error: {error}')
    
#Testing code here    
if __name__ == '__main__':
    tokengen = TokenGenerator()
    
    username = "Raj"
    
    #Success Scenario
    token = tokengen.generateJWTToken(username)
    print("\n Generated Token: {}".format(token))

    decodedValue = tokengen.verifyJWTToken(token)
    print("\n Decoded Payload: {}".format(decodedValue))