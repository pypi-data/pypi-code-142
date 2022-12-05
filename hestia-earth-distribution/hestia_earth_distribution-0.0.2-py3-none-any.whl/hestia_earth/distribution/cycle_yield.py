import pandas as pd
from hestia_earth.utils.model import find_primary_product
from hestia_earth.utils.tools import list_sum, list_average

# Yield = f(N,K,P, temp, rainfall, irrigation, seed, soil, pesticide, )

YIELD_COLUMN = 'Grain yield (kg/ha)'
FERTILISER_COLUMNS = [
    'Nitrogen (kg N)',
    'Phosphorus (kg P2O5)',
    'Potash (kg K2O)',
    'Magnesium (kg Mg)'
    # 'Sulphur (kg S)',
    # 'FertCompleteness'
]
FERTILISER_UNITS = [
    'kg N',
    'kg P2O5',
    'kg K2O',
    'kg Mg'
    # 'kg S'
]


def _cycle_fertilisers(cycle: dict):
    fertilisers = [
        i for i in cycle.get('inputs', []) if i.get('term', {}).get('termType') in [
            'inorganicFertiliser',
            'organicFertiliser',
            'inorganicFertilizer',
            'organicFertilizer'
        ] and list_sum(i.get('value', []), 0) > 0
    ]
    fert_array = [0, 0, 0, 0]  # init to 0 for each units
    for input in fertilisers:
        for index, fertiliser in enumerate(FERTILISER_UNITS):
            if input.get('term', {}).get('units') == fertiliser:
                fert_array[index] = fert_array[index] + list_sum(input.get('value'))
    return fert_array


def cycle_yield_distribution(cycles: list):
    df = pd.DataFrame(index=list(map(lambda c: c.get('@id'), cycles)), columns=[YIELD_COLUMN] + FERTILISER_COLUMNS)

    for cycle in cycles:
        value = list_average(find_primary_product(cycle).get('value'))
        df.loc[cycle.get('@id')] = [value] + _cycle_fertilisers(cycle)  # +[cycle.get('dataCompleteness')['fertilizer']]

    df.index.rename('cycle.id', inplace=True)
    return df
