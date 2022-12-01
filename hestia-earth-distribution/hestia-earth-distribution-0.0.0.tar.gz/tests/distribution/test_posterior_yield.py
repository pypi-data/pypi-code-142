from unittest.mock import patch
import os
import pandas as pd
from tests.utils import fixtures_path, remove_file
from hestia_earth.distribution.utils.priors import read_prior_stats
from hestia_earth.distribution.likelihood import likl_filename
from hestia_earth.distribution.posterior_yield import (
    POSTERIOR_YIELD_FILENAME, post_filename, get_post, update_all_post, get_esemble_means
)

class_path = 'hestia_earth.distribution.posterior_yield'
prior_yield_filepath = os.path.join(fixtures_path, 'prior_files', 'FAO_Yield_prior_per_product_per_country_n50.pkl')


def fake_generate_prior_yield_file(*args): return read_prior_stats(prior_yield_filepath)


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
    result = update_all_post(rows=list(range(3)), cols=list(range(30)))
    remove_file(POSTERIOR_YIELD_FILENAME)
    remove_file(post_filename('GADM-CHE', 'genericCropSeed'))

    expected = pd.read_csv(os.path.join(fixtures_path, 'post_files', 'posterior_crop_yield_3.csv'), index_col=0)

    result = result.dropna(axis=1, how='all').dropna(axis=0, how='all')
    expected = expected.dropna(axis=1, how='all').dropna(axis=0, how='all')

    assert (result.columns == expected.columns).all() and (result.index == expected.index).all()
