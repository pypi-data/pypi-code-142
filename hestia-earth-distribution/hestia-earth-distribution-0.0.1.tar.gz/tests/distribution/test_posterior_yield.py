from unittest.mock import patch
import os
import pandas as pd
from tests.utils import fixtures_path, remove_file
from hestia_earth.distribution.utils.priors import read_prior_stats
from hestia_earth.distribution.likelihood import likl_filename
from hestia_earth.distribution.prior_yield import PRIOR_YIELD_FILENAME
from hestia_earth.distribution.posterior_yield import (
    POSTERIOR_YIELD_FILENAME, post_filename, get_post, update_all_post, get_esemble_means
)

class_path = 'hestia_earth.distribution.posterior_yield'
fixtures_folder = os.path.join(fixtures_path, 'post_files')


def fake_generate_prior_yield_file(*args):
    return read_prior_stats(os.path.join(fixtures_path, 'prior_files', PRIOR_YIELD_FILENAME))


def fake_generate_likl_yield_file(country_id, product_id):
    likl_file = os.path.join(fixtures_path, 'likelihood_files', likl_filename(country_id, product_id))
    return pd.read_csv(likl_file) if os.path.exists(likl_file) else []


@patch(f"{class_path}.generate_prior_yield_file", side_effect=fake_generate_prior_yield_file)
@patch(f"{class_path}.generate_likl_yield_file", side_effect=fake_generate_likl_yield_file)
def test_get_post(*args):
    country_id = 'GADM-CHE'
    product_id = 'genericCropSeed'

    mu, sd = get_esemble_means(*get_post(country_id, product_id))
    remove_file(post_filename(country_id, product_id))
    assert int(mu) >= 2000 and int(mu) <= 5000


@patch(f"{class_path}.generate_prior_yield_file", side_effect=fake_generate_prior_yield_file)
@patch(f"{class_path}.generate_likl_yield_file", side_effect=fake_generate_likl_yield_file)
def test_update_all_post(*args):
    result = update_all_post(overwrite=True)
    remove_file(POSTERIOR_YIELD_FILENAME)
    remove_file(post_filename('GADM-CHE', 'genericCropSeed'))
    remove_file(post_filename('GADM-GBR', 'wheatGrain'))

    expected_file = os.path.join(fixtures_folder, POSTERIOR_YIELD_FILENAME)
    expected = pd.read_csv(expected_file, na_values='-', index_col=['term.id'])

    assert (result.columns == expected.columns).all() and (result.index == expected.index).all()
