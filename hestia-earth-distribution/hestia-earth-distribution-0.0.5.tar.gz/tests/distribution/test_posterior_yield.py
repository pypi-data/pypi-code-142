from unittest.mock import patch
import os
import json
import pandas as pd
from tests.utils import fixtures_path
from hestia_earth.distribution.utils.priors import read_prior_stats
from hestia_earth.distribution.posterior_yield import (
    update_all_post, get_post, get_post_ensemble, post_filename
)

class_path = 'hestia_earth.distribution.posterior_yield'
fixtures_folder = os.path.join(fixtures_path, 'posterior_yield')


def fake_generate_prior_yield_file(*args):
    return read_prior_stats(os.path.join(fixtures_folder, 'prior.csv'))


def fake_generate_likl_yield_file(country_id, product_id):
    likl_file = os.path.join(fixtures_folder, 'likelihood', f"{'-'.join([country_id, product_id])}.csv")
    return pd.read_csv(likl_file) if os.path.exists(likl_file) else []


def read_posterior_file(*args):
    with open(os.path.join(fixtures_folder, 'result.csv'), 'rb') as f:
        return f.read()


@patch(f"{class_path}.load_from_storage", side_effect=read_posterior_file)
def test_get_post(*args):
    mu, sd = get_post('GADM-CHE', 'genericCropSeed')
    assert mu == 2716
    assert sd == 486


@patch(f"{class_path}.load_from_storage", side_effect=read_posterior_file)
def test_get_post_missing(*args):
    # data is a `-`
    mu, sd = get_post('GADM-CHE', 'wheatGrain')
    assert mu is None
    assert sd is None

    # data is not present
    mu, sd = get_post('GADM-FRA', 'wheatGrain')
    assert mu is None
    assert sd is None


def read_posterior_json(filename: str):
    file = filename.split('/')[1]
    with open(os.path.join(fixtures_folder, file), 'rb') as f:
        return f.read()


@patch(f"{class_path}.load_from_storage", side_effect=read_posterior_json)
@patch(f"{class_path}.file_exists", return_value=True)
def test_get_post_ensemble(*args):
    mu_ensemble, sd_ensemble = get_post_ensemble('GADM-CHE', 'genericCropSeed')
    assert len(mu_ensemble) == 4
    assert len(sd_ensemble) == 4


@patch(f"{class_path}.generate_likl_yield_file", side_effect=fake_generate_likl_yield_file)
@patch(f"{class_path}.generate_prior_yield_file", side_effect=fake_generate_prior_yield_file)
@patch(f"{class_path}.write_to_storage")
@patch(f"{class_path}.file_exists", return_value=False)
def test_get_post_ensemble_missing(*args):
    mu_ensemble, sd_ensemble = get_post_ensemble('GADM-CHE', 'genericCropSeed')
    assert len(mu_ensemble) == 4
    assert len(sd_ensemble) == 4


@patch(f"{class_path}.load_from_storage", side_effect=read_posterior_json)
@patch(f"{class_path}.file_exists", return_value=True)
def test_get_post_ensemble_empty(*args):
    mu_ensemble, sd_ensemble = get_post_ensemble('GADM-AFG', 'wheatGrain')
    assert len(mu_ensemble) == 0
    assert len(sd_ensemble) == 0


def fake_get_post_ensemble(country_id, product_id, **kwargs):
    filepath = os.path.join(fixtures_folder, post_filename(country_id, product_id))
    data = {}
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
    return data.get('posterior', {}).get('mu', []), data.get('posterior', {}).get('sd', [])


@patch(f"{class_path}.get_post_ensemble", side_effect=fake_get_post_ensemble)
@patch(f"{class_path}.generate_prior_yield_file", side_effect=fake_generate_prior_yield_file)
@patch(f"{class_path}.write_to_storage")
def test_update_all_post(*args):
    result = update_all_post()
    expected_file = os.path.join(fixtures_folder, 'result.csv')
    expected = pd.read_csv(expected_file, na_values='-', index_col=['term.id'])
    assert (result.columns == expected.columns).all() and (result.index == expected.index).all()
