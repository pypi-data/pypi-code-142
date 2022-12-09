import requests

class PDAAPI:
    def __init__(self, base_url, user, password):
        self.base_url = base_url
        self.user = user
        self.password = password
        self.auth = (self.user, self.password)

    def create_domain(self, name, kind, nameservers):
        url = self.base_url + '/api/v1/pdnsadmin/zones'
        payload = {
            'name': name,
            'kind': kind,
            'nameservers': nameservers
        }
        response = requests.post(url, json=payload, auth=self.auth)
        return response.json()

    def create_apikey(self, description, domains, role):
        url = self.base_url + '/api/v1/pdnsadmin/apikeys'
        payload = {
            'description': description,
            'domains': domains,
            'role': role
        }
        response = requests.post(url, json=payload, auth=self.auth)
        return response.json()

    def get_config(self):
        url = self.base_url + '/api/v1/server/config'
        response = requests.get(url, auth=self.auth)
        return response.json()

    def sync_domains(self, key):
        url = self.base_url + '/api/v1/server/sync_domains'
        headers = {'X-API-KEY': key}
        response = requests.post(url, headers=headers, auth=self.auth)
        return response.json()

    def get_powerdnsadmin(self, endpoint):
        url = self.base_url + '/api/v1/pdnsadmin/' + endpoint
        response = requests.get(url, auth=self.auth)
        return response.json()
