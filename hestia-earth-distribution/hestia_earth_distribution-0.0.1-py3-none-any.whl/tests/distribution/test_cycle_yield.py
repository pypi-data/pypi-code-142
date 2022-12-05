import pandas as pd
import os
import json
from tests.utils import fixtures_path, round_df_column

from hestia_earth.distribution.cycle_yield import cycle_yield_distribution

fixtures_folder = os.path.join(fixtures_path, 'cycle_yield')


def test_cycle_yield_distribution():
    with open(f"{fixtures_folder}/cycles.jsonld", encoding='utf-8') as f:
        cycles = json.load(f)

    expected = pd.read_csv(os.path.join(fixtures_folder, 'distribution.csv'), index_col='cycle.id')
    result = cycle_yield_distribution(cycles)
    round_df_column(result, 'Grain yield (kg/ha)')
    round_df_column(result, 'Nitrogen (kg N)')
    assert result.to_csv() == expected.to_csv()
