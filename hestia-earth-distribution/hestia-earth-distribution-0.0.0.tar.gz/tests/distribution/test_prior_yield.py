import os
from tests.utils import fixtures_path, remove_file
from hestia_earth.distribution.utils.priors import read_prior_stats

from hestia_earth.distribution.prior_yield import (
    PRIOR_YIELD_FILENAME, generate_prior_yield_file, calculate_worldwide_mean_sigma
)

fixtures_folder = os.path.join(fixtures_path, 'prior_files')


def test_generate_prior_yield_file():
    df_stats = generate_prior_yield_file(50)
    remove_file(PRIOR_YIELD_FILENAME)

    df_expected = read_prior_stats(os.path.join(fixtures_folder, 'FAO_Yield_prior_per_product_per_country_n50.pkl'))
    assert df_stats.equals(df_expected)


def test_worldwide_mean_sigma():
    stats = calculate_worldwide_mean_sigma('wheatGrain')
    assert [round(s) for s in stats] == [3197, 1854, 371, 241]
