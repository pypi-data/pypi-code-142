import requests

API_URL = 'https://ws.geonorge.no/kommuneinfo/v1/'

def get_kommune_by_nr(nr: str):
    service = 'kommuner/'
    resp = requests.get(url=API_URL+service+nr)
    return resp.json()['kommunenavn']