from norske_kommuner.models import FylkerKommunerFull, KomFull
from collections import Counter
import json

API_URL = 'https://ws.geonorge.no/kommuneinfo/v1/'

with open('resources/fylkeskommuner.json', 'r') as f:
    raw = f.read()

kommuner_pydantic = [FylkerKommunerFull.parse_obj(i) for i in json.loads(raw)]
kommuner_flat = [k for fylke in kommuner_pydantic for k in fylke.kommuner]
kommune_names_count = Counter([kommune.kommunenavn for kommune in kommuner_flat])
popular_names = {k for k, v in kommune_names_count.items() if v > 1}
kommuner: dict[str, KomFull] = dict()
for kommune in kommuner_flat:
    name = kommune.kommunenavn
    if name in popular_names:
        name = f'{name}_{kommune.fylkesnavn}'
    name = name.replace(' ', '').replace('-', '')
    kommuner[name] = kommune


def get_kommune_by_nr(nr: str) -> KomFull:
    return next((k for k in kommuner.values() if k.kommunenummer == nr), None)
