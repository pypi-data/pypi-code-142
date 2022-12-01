import pandas as pd
import numpy as np
from hestia_earth.utils.lookup import download_lookup

from .log import logger
from .utils import SIGMA_DUMMY
from .utils.storage import file_exists
from .utils.fao import LOOKUP_YIELD, get_fao_yield, create_df_fao, get_mean_std_per_country_per_product
from .utils.priors import read_prior_stats, generate_and_save_priors

PRIOR_YIELD_FILENAME = 'FAO_Yield_prior_per_product_per_country.pkl'


def calculate_worldwide_mean_sigma(product_id: str):
    """
    Calculate the means and sigmas for worldwide means and standard deviations of FAO yield for a specific product.

    Parameters
    ----------
    product_id: str
        Crop product term ID from Hestia glossary, e.g. 'wheatGrain'.

    Returns
    -------
    list of values:
        Means of worldwide means, std of worldwide means, mean of worldwide std, std of worldwide std.
    """
    df_fao = create_df_fao()
    world_means = []
    world_sigmas = []
    for gadm_code, row in df_fao.iterrows():
        stats = get_mean_std_per_country_per_product(product_id, gadm_code, get_fao_yield)
        if None not in stats:
            world_means.append(stats[0])
            world_sigmas.append(stats[1])
    world_means = np.array(world_means)
    world_sigmas = np.array(world_sigmas)
    return [world_means.mean(), world_means.std(), world_sigmas.mean(), world_sigmas.std()]


def _get_yield_priors(n_rows=10000):
    term_lookup = download_lookup('crop.csv')[:n_rows]
    yield_lookup = download_lookup(LOOKUP_YIELD)

    df_stats = pd.DataFrame(columns=yield_lookup['termid'], index=term_lookup['termid'])

    for product_id in term_lookup['termid']:
        logger.info(f'Processing {product_id}...')
        for gadm_code in yield_lookup['termid']:
            stats = get_mean_std_per_country_per_product(product_id, gadm_code, get_fao_yield)
            if None not in stats:
                df_stats.loc[product_id, gadm_code] = stats[0], stats[1], stats[2], SIGMA_DUMMY
    df_stats.index.rename('term.id', inplace=True)
    logger.info('Processing finished.')
    return df_stats


def generate_prior_yield_file(n: int = 2000, overwrite=False):
    """
    Return all prior statistics (means, std and n_years) of FAO yield from a CSV file.
    If prior file exisits, prior data will be read in; otherwise, generate priors and store into prior_file path.

    Parameters
    ----------
    n: int
        Optional - number of rows to return. Defaults to `2000`.
    overwrite: bool
        Optional - whether to overwrite existing prior file or not. Defaults to `False`.

    Returns
    -------
    pd.DataFrame
        DataFrame storing the prior of the means.
    """
    read_existing = file_exists(PRIOR_YIELD_FILENAME) and not overwrite
    return read_prior_stats(PRIOR_YIELD_FILENAME) if read_existing \
        else generate_and_save_priors(PRIOR_YIELD_FILENAME, _get_yield_priors, n)
