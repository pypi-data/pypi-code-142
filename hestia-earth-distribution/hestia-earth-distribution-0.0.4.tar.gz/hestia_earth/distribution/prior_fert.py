import pandas as pd
from hestia_earth.utils.lookup import download_lookup

from .log import logger
from .utils import get_fert_group_name, SIGMA_SCALER
from .utils.storage import file_exists
from .utils.fao import (
    LOOKUP_FERTUSE, FERT_GROUPS, get_fao_fertuse, get_mean_std_per_country_per_product
)
from .utils.priors import read_prior_stats, generate_and_save_priors

FOLDER = 'prior_files'
PRIOR_FERT_FILENAME = 'FAO_fert_prior_per_country.csv'


def get_fao_fert(country_id: str, fert_id: str, n_years: int = 10):
    """
    Look up the FAO yield per country per product from the glossary.

    Parameters
    ----------
    country_id: str
        Region `@id` from Hestia glossary, e.g. 'GADM-GBR', or 'region-south-america'.
    fert_id: str
        Inorganic or organic fertiliser term ID from Hestia glossary, e.g. 'ammoniumNitrateKgN'.
    n_years: int
        Number of years (in reverse chronological order) of FAO data record to get. Defaults to `10` years.

    Returns
    -------
    nunpy.array or None
        A 2-D array with years and yield values from FAO yield record, if successful.
    """
    fert_group = get_fert_group_name(fert_id)
    return get_fao_fertuse(country_id, FERT_GROUPS.get(fert_group), n_years=n_years)


def get_fert_priors_NPK(n_rows: int = 3):
    """
    Get FAO fert use priors as a DataFrame for all products for all countries and regions.

    Parameters
    ----------
    n_rows: int
        Max number of rows to return.

    Returns
    -------
    pd.DataFrame
        A dataframe of all prior information (mu, sigma_of_mu, and n_years, sigma).
    """
    fert_lookup = download_lookup(LOOKUP_FERTUSE)
    countries = pd.Series(fert_lookup['termid']).drop_duplicates()
    # idx = FERT_GROUPS.values()[:min(n_rows, len(FERT_GROUPS))]
    df_stats = pd.DataFrame(columns=countries, index=FERT_GROUPS.values())[:n_rows]

    for fert_id in FERT_GROUPS.values():
        # fert_group = get_fert_group_name(fert_id)
        logger.info(f'Processing {fert_id}...')
        for gadm_code in fert_lookup['termid']:
            stats = get_mean_std_per_country_per_product(fert_id, gadm_code, get_fao_fertuse)
            if None not in stats:
                df_stats.loc[fert_id, gadm_code] = stats[0], stats[1], stats[2], stats[1]*SIGMA_SCALER

    df_stats.index.rename('term.id', inplace=True)
    logger.info('Processing finished.')
    return df_stats


def generate_prior_fert_file(overwrite=False):
    """
    Return all prior statistics (means, std and n_years) of FAO fertiliser use from a CSV file.
    If prior file exisits, prior data will be read in; otherwise, generate priors and stores it on disk.

    Parameters
    ----------
    overwrite: bool
        Optional - whether to overwrite existing prior file or not.

    Returns
    -------
    pd.DataFrame
        The prior of the means.
    """
    filepath = f"{FOLDER}/{PRIOR_FERT_FILENAME}"
    read_existing = file_exists(filepath) and not overwrite
    return read_prior_stats(filepath) if read_existing else generate_and_save_priors(filepath, get_fert_priors_NPK)
