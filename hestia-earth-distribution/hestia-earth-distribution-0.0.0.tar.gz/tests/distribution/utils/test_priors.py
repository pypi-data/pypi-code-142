import os
from tests.utils import fixtures_path

from hestia_earth.distribution.prior_yield import PRIOR_YIELD_FILENAME
from hestia_earth.distribution.prior_fert import PRIOR_FERT_FILENAME
from hestia_earth.distribution.utils.priors import get_prior_by_country_by_product

fixtures_folder = os.path.join(fixtures_path, 'prior_files')


def test_get_prior_by_country_by_product():
    # test for crop
    product_id = 'wheatGrain'
    prior_filename = os.path.join(fixtures_folder, PRIOR_YIELD_FILENAME)
    vals = get_prior_by_country_by_product(prior_filename, 'GADM-AFG', product_id)
    assert [round(v) for v in vals] == [2002, 182, 10, -999]

    # test for fertiliser
    product_id = 'inorganicNitrogenFertiliserUnspecifiedKgN'
    prior_filename = os.path.join(fixtures_folder, PRIOR_FERT_FILENAME)
    vals = get_prior_by_country_by_product(prior_filename, 'GADM-AFG', product_id)
    assert [round(v) for v in vals] == [8, 5, 10, -999]
