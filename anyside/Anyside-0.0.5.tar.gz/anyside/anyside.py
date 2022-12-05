import requests

class Anyside:
    def __init__(self,api_key):
        self.api_endpoint = "https://anyside.com/public"
        self.api_key = api_key
        self.sess = requests.session()

    def query_domain(self,domain):
        try:
            response = self.sess.post(url=f"{self.api_endpoint}/queryDomain",json={"domain":domain,"api_key":self.api_key})
            return response.json()
        except Exception as error:
            return {"message":error}

    def lookup_wallet(self,wallet_address):
        try:
            response = self.sess.post(url=f"{self.api_endpoint}/lookupWallet",json={"wallet_address":wallet_address,"api_key":self.api_key})
            return response.json()
        except Exception as error:
            return {"message":error}