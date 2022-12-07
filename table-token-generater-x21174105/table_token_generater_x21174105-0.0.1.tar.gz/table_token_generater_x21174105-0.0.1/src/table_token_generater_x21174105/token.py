import secrets

def createtoken():
    token =''.join([secrets.choice('abcdefghijklmnopqrstuvwxyz') for i in range(5)])
    print(token)
    return token