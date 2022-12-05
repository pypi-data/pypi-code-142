from unittest.mock import patch
import os
from tests.utils import fixtures_path
from hestia_earth.distribution.utils.priors import read_prior_stats

from hestia_earth.distribution.prior_yield import (
    generate_prior_yield_file, calculate_worldwide_mean_sigma
)

fixtures_folder = os.path.join(fixtures_path, 'prior_yield')


def test_worldwide_mean_sigma():
    stats = calculate_worldwide_mean_sigma('wheatGrain')
    assert [round(s) for s in stats] == [3197, 1854, 371, 241]


@patch('hestia_earth.distribution.utils.priors.write_to_storage')
def test_generate_prior_yield_file(*args):
    result = generate_prior_yield_file(10, overwrite=True)
    expected = read_prior_stats(os.path.join(fixtures_folder, 'result.csv'))
    assert result.to_csv() == expected.to_csv()
