from unittest.mock import patch
import os
import numpy as np
from tests.utils import fixtures_path
from hestia_earth.distribution.utils.priors import read_prior_stats

from hestia_earth.distribution.prior_fert import (
    generate_prior_fert_file, get_fao_fert
)

fixtures_folder = os.path.join(fixtures_path, 'prior_fert')


def test_get_fao_fert():
    val1 = get_fao_fert('GADM-GBR', 'inorganicNitrogenFertiliserUnspecifiedKgN')
    val2 = get_fao_fert('GADM-GBR', 'manureDryKgN')
    assert (val1 == val2).all() == np.True_


@patch('hestia_earth.distribution.utils.priors.write_to_storage')
def test_generate_prior_fert_file(*args):
    result = generate_prior_fert_file(overwrite=True)
    expected = read_prior_stats(os.path.join(fixtures_folder, 'result.csv'))
    assert result.to_csv() == expected.to_csv()
