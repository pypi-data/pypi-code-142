def signup(name:str):
    print ("Hope it was easy to signup! Welcome",name)
    return 'main:home'
    
def login(name:str):
    print ("Welcome back! hope you enjoy your time here",name)
    return 'main:home'

def logout():
    print ("Thanks for your time ,have a nice day!!")
    return '/'