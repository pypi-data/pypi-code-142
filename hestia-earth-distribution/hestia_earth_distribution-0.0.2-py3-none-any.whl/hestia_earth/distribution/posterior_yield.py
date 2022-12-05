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


def _posterior_by_country(df_prior: pd.DataFrame, df_likl, country_id: str, product_id: str):
    # prior
    mu_country, sigma_country = get_stats_from_df(df_prior, country_id, product_id)

    # likelihood
    data = df_likl[YIELD_COLUMN]

    logger.info(f'Prior mu ={mu_country}, std = {sigma_country}; Obs mean ={data.mean()}, std ={data.std()}')

    with pm.Model() as model:
        mu = pm.Normal('mu', mu=mu_country, sigma=sigma_country)
        sd = pm.HalfNormal('sd', sigma=sigma_country)

        idata = pm.sample(2000, tune=1000, cores=4)
        idata.extend(pm.sample_posterior_predictive(idata))

        mu, sd = pm.summary(idata)['mean']
        return idata, model, mu, sd


def _write_post(country_id: str, product_id: str, post_file: str, df_prior: pd.DataFrame = None):
    df_likl = generate_likl_yield_file(country_id, product_id)

    if len(df_likl) > 0:
        # make sure we don't load prior file muliple times when generating all posteriors
        _df_prior = generate_prior_yield_file() if df_prior is None else df_prior
        idata, model, mu, sd = _posterior_by_country(_df_prior, df_likl, country_id, product_id)
        data = {
            'posterior': {
                'mu': idata['posterior']['mu'].to_dict()['data'],
                'sd': idata['posterior']['sd'].to_dict()['data']
            }

        }
        write_to_storage(post_file, json.dumps(data).encode('utf-8'))
        return idata['posterior']['mu'], idata['posterior']['sd']

    return [], []


def _read_post(filename: str):
    data = json.loads(load_from_storage(filename))
    return data['posterior']['mu'], data['posterior']['sd']


def post_filename(country_id: str, product_id: str): return f'posterior_{country_id}_{product_id}.json'


def get_post(country_id: str, product_id: str, overwrite=False, df_prior: pd.DataFrame = None):
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
    return _read_post(filepath) if read_existing else _write_post(country_id, product_id, filepath, df_prior)


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
    return (np.array(mu_ensemble).mean(), np.array(sd_ensemble).mean()) if all([
        len(mu_ensemble) > 0,
        len(sd_ensemble) > 0
    ]) else None


def _get_index_range(values: list, index: list): return values or list(range(len(index)))


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
    rows = _get_index_range(rows, df_prior.index)
    product_ids = df_prior.index[rows]
    cols = _get_index_range(cols, df_prior.columns)
    country_ids = df_prior.columns[cols]
    df = pd.DataFrame(index=product_ids, columns=country_ids)

    for country_id in country_ids:
        for product_id in product_ids:
            if not pd.isnull(df_prior.loc[product_id, country_id]):
                mu_ensemble, sd_ensemble = get_post(country_id, product_id, overwrite=overwrite, df_prior=df_prior)
                df.loc[product_id, country_id] = get_esemble_means(mu_ensemble, sd_ensemble)

    df.index.rename('term.id', inplace=True)
    write_to_storage(POSTERIOR_YIELD_FILENAME, df_to_csv_buffer(df))
    return df.dropna(axis=1, how='all').dropna(axis=0, how='all')
