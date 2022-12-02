from Maxar_Portal_SDK.ogc.interface import Interface as ogc_interface
from Maxar_Portal_SDK.account_service.interface import Interface as account_interface
from Maxar_Portal_SDK.auth.auth import Auth
from Maxar_Portal_SDK.token_service.token import Token


class Interface:

    def __init__(self, *args):

        if len(args) > 0:
            try:
                #base_url = args[0]
                username = args[0]
                password = args[1]
            except:
                raise Exception("MPS-config file not formatted correctly")
            self.auth = Auth(username, password)
        else:
            self.auth = Auth()

        self.ogc = ogc_interface(self.auth)
        self.account_service = account_interface(self.auth)
        self.token = Token(self.auth)

