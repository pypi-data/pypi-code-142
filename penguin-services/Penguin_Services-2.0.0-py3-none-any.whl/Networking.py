import requests

def get(url: str, headers: dict = {}):
    return json.loads(requests.get(url, headers=headers).text)
