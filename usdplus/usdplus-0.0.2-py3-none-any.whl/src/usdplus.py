import requests

'''
o = Optimism
m = Matic
b = Binance
a = Avalanche
'''


class USDPlus:
    def __init__(self, network):
        nets = ['o', 'm', 'b', 'a']
        if network == nets[0]:
            self.network = 'op'
        if network == nets[1]:
            self.network = 'app'
        if network == nets[2]:
            self.network = 'bsc'
        if network == nets[3]:
            self.network = 'avax'

    def allPools(self):
        req = requests.get(f'https://{self.network}.overnight.fi/api/pools/all').json()
        return req

    def strategies(self):
        req = requests.get(f'https://{self.network}.overnight.fi/api/dapp/strategies').json()
        return req

    def hedgeStrategies(self, contract):
        """
            strategies contract can be found by running def strategies
        """
        req = requests.get(f'https://{self.network}.overnight.fi/api/hedge-strategies/{contract}/').json()
        return req

    def hedgeStrategiesAvgApyInfo(self, contract):
        req = requests.get(
            f'https://{self.network}.overnight.fi/api/hedge-strategies/{contract}/avg-apy-info/month').json()
        return req

    '''def challenge_platform(self):

        772a5af688641912 # ↓ found when looking into this ---> Figure out ↓
        7729ed4d4a828c96


        req = requests.get(
            f'https://{self.network}.overnight.fi/cdn-cgi/challenge-platform/h/b/cv/result/7729ed4d4a828c96').json()
        return req'''

    def getTotalUsdPlusValue(self):
        req = requests.get(f'https://{self.network}.overnight.fi/api/dapp/getTotalUsdPlusValue').json()
        return req

    def getTotalUsdPlusProfit(self):
        req = requests.get(f'https://{self.network}.overnight.fi/api/dapp/getTotalUsdPlusProfit').json()
        return req

    def payouts(self):
        req = requests.get(f'https://{self.network}.overnight.fi/api/dapp/payouts').json()
        return req

    def avgApyInfoAll(self):
        req = requests.get(f'https://{self.network}.overnight.fi/api/widget/avg-apy-info/all').json()
        return req

    def avgApyInfoMonth(self):
        req = requests.get(f'https://{self.network}.overnight.fi/api/widget/avg-apy-info/month').json()
        return req

    def totalCollateral(self):
        req = requests.get(f'https://{self.network}.overnight.fi/api/dapp/collateral/total').json()
        return req
