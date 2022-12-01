import os
import pandas as pd
import numpy as np
from tests.utils import fixtures_path, remove_file
from hestia_earth.distribution.utils.priors import read_prior_stats

from hestia_earth.distribution.prior_fert import (
    PRIOR_FERT_FILENAME, get_fert_priors_NPK, generate_prior_fert_file, get_fao_fert
)

fixtures_folder = os.path.join(fixtures_path, 'prior_files')
product_per_country_pkl_file = os.path.join(fixtures_folder, PRIOR_FERT_FILENAME)


def test_get_fao_fert():
    val1 = get_fao_fert('GADM-GBR', 'inorganicNitrogenFertiliserUnspecifiedKgN')
    val2 = get_fao_fert('GADM-GBR', 'manureDryKgN')
    assert (val1 == val2).all() == np.True_


def test_get_fertuse_priors():
    df_expected = pd.read_pickle(product_per_country_pkl_file)
    df_stats = get_fert_priors_NPK()
    assert df_stats.equals(df_expected)


def test_generate_prior_fert_npk():
    df_stats = generate_prior_fert_file()
    remove_file(PRIOR_FERT_FILENAME)

    df_expected = read_prior_stats(product_per_country_pkl_file)
    assert df_stats.to_string() == df_expected.to_string()
