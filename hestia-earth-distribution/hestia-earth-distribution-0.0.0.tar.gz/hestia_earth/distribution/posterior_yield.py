import json
import pandas as pd
import numpy as np
import pymc as pm

from .log import logger
from .utils import df_to_csv_buffer
from .utils.storage import file_exists, load_from_storage, write_to_storage
from .prior_yield import generate_prior_yield_file
from .likelihood import generate_likl_yield_file
from .cycle_yield import YIELD_COLUMN

POSTERIOR_YIELD_FILENAME = 'posterior_crop_yield.csv'


def get_stats_from_df(df, country_id: str, product_id: str):
    yield_stats = df.loc[product_id][country_id]
    # this happens when read priors in from a CSV file
    vals = [float(v) for v in yield_stats.strip('()').split(',')] if type(yield_stats) == str else yield_stats
    return vals[0], vals[1]  # mu, sigma


def _posterior_by_country(df_prior, df_likl, country_id: str, product_id: str):
    # prior
    mu_country, sigma_country = get_stats_from_df(df_prior, country_id, product_id)

    # likelihood
    data = df_likl[YIELD_COLUMN]

    logger.info(f'Prior mu ={mu_country}, std = {sigma_country}; Obs mean ={data.mean()}, std ={data.std()}')

    with pm.Model() as model:
        mu = pm.Normal("mu", mu=mu_country, sigma=sigma_country)
        sd = pm.HalfNormal('sd', sigma=sigma_country)
        # obs = pm.Normal("obs", mu=data.mean(), sigma=data.std(), observed=data)
        pm.Normal("obs", mu=mu, sigma=sd, observed=data)

        idata = pm.sample(2000, tune=1000, cores=4)
        idata.extend(pm.sample_posterior_predictive(idata))

        mu, sd = pm.summary(idata)['mean']
        return idata, model, mu, sd


def _write_post(country_id: str, product_id: str, post_file: str):
    df_prior = generate_prior_yield_file()
    df_likl = generate_likl_yield_file(country_id, product_id)

    if df_likl.size > 0:
        idata, model, mu, sd = _posterior_by_country(df_prior, df_likl, country_id, product_id)
        data = {
            'posterior': {
                'mu': idata['posterior']['mu'].to_dict()['data'],
                'sd': idata['posterior']['sd'].to_dict()['data']
            }

        }
        write_to_storage(post_file, json.dumps(data).encode('utf-8'))
        return idata['posterior']['mu'], idata['posterior']['sd']

    return None, None


def _read_post(filename: str):
    data = json.loads(load_from_storage(filename))
    return data['posterior']['mu'], data['posterior']['sd']


def post_filename(country_id: str, product_id: str): return f'posterior_{country_id}_{product_id}.json'


def get_post(country_id: str, product_id: str, overwrite=False):
    """
    Return posterior data for a given country and a given product.
    If posterior file exisits, data will be read in; otherwise, generate posterior data and store
    into a pickle or json file.

    Parameters
    ----------
    country_id: str
        Region `@id` from Hestia glossary, e.g. 'GADM-GBR', or 'region-south-america'.
    product_id: str
        Product term `@id` from Hestia glossary, e.g. 'wheatGrain'.
    overwrite: bool
        Whether to overwrite existing posterior file or not. Defaults to `False`.

    Returns
    -------
    mu_list: list
        List of list of float storing the posterior mu ensembles.
    sd_list: list
        List of list of float storing the posterior sd ensembles.
    """
    filepath = post_filename(country_id, product_id)
    read_existing = file_exists(filepath) and not overwrite
    return _read_post(filepath) if read_existing else _write_post(country_id, product_id, filepath)


def get_esemble_means(mu_ensemble: list, sd_ensemble: list):
    """
    Return posterior means for an ensembles of mu and an ensembles of sigma (sd).

    Parameters
    ----------
    mu_ensemble: list
        List of list of float storing the posterior mu ensembles.
    sd_ensemble: list
        List of list of float storing the posterior sd ensembles.

    Returns
    -------
    tuple(mu, sd)
        The mean of posterior mu and the mean of posterior sigma (sd)
    """
    return np.array(mu_ensemble).mean(), np.array(sd_ensemble).mean()


def _get_full_rows_or_cols(rows: list, index: list):
    return list(range(len(index))) if not rows else rows


def update_all_post(rows: list = None, cols: list = None, overwrite=True):
    """
    Update crop posterior data for all countries and all products.
    It creates or re-write json files to store posterior data for each country and each product.
    It also writes all distribution stats (mu, sigma) into one csv file.

    Parameters
    ----------
    rows: list of int
        Rows (products) to be updated. Default None to include all products.
    cols: list of int
        Columns (countries) to be updated. Default None to include all countries.
    overwrite: bool
        Whether to overwrite the posterior json files. Defaults to `True`.
    """
    df_prior = generate_prior_yield_file()
    rows = _get_full_rows_or_cols(rows, df_prior.index)
    cols = _get_full_rows_or_cols(cols, df_prior.columns)
    df_post = pd.DataFrame(index=df_prior.index[rows], columns=df_prior.columns[cols])

    for country_id in df_prior.columns[cols]:
        for product_id in df_prior.index[rows]:
            if type(df_prior.loc[product_id, country_id]) == tuple:
                df = generate_likl_yield_file(country_id, product_id)
                if len(df) > 0:
                    mu_ensemble, sd_ensemble = get_post(country_id, product_id, overwrite=overwrite)
                    df_post.loc[product_id, country_id] = get_esemble_means(mu_ensemble, sd_ensemble)

    df_post.index.rename('cycle.id', inplace=True)
    write_to_storage(POSTERIOR_YIELD_FILENAME, df_to_csv_buffer(df_post))
    return df_post
