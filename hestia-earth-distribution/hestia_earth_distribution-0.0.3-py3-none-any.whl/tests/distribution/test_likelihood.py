from unittest.mock import patch
import os
import pandas as pd
import json
from tests.utils import fixtures_path, round_df_column

from hestia_earth.distribution.likelihood import generate_likl_yield_file

class_path = 'hestia_earth.distribution.likelihood'
fixtures_folder = os.path.join(fixtures_path, 'likelihood')

with open(os.path.join(fixtures_folder, 'cycles.jsonld'), 'r') as f:
    cycles = json.load(f)


@patch(f"{class_path}.find_cycles", return_value=cycles)
@patch(f"{class_path}.file_exists", return_value=False)
@patch(f"{class_path}.write_to_storage")
def test_generate_likl_yield_file(*args):
    country_id = 'GADM-GBR'
    product_id = 'wheatGrain'

    expected = pd.read_csv(os.path.join(fixtures_folder, 'result.csv'), index_col=0)
    result = generate_likl_yield_file(country_id, product_id)
    round_df_column(result, 'Grain yield (kg/ha)')
    round_df_column(result, 'Nitrogen (kg N)')

    assert result.to_csv() == expected.to_csv()
