import os
import numpy as np
from tests.utils import fixtures_path, remove_file
from hestia_earth.distribution.utils.priors import read_prior_stats

from hestia_earth.distribution.prior_fert import (
    PRIOR_FERT_FILENAME, generate_prior_fert_file, get_fao_fert
)

fixtures_folder = os.path.join(fixtures_path, 'prior_files')


def test_get_fao_fert():
    val1 = get_fao_fert('GADM-GBR', 'inorganicNitrogenFertiliserUnspecifiedKgN')
    val2 = get_fao_fert('GADM-GBR', 'manureDryKgN')
    assert (val1 == val2).all() == np.True_


def test_generate_prior_fert_file():
    result = generate_prior_fert_file(overwrite=True)
    remove_file(PRIOR_FERT_FILENAME)

    expected = read_prior_stats(os.path.join(fixtures_folder, PRIOR_FERT_FILENAME))
    assert result.to_csv() == expected.to_csv()
