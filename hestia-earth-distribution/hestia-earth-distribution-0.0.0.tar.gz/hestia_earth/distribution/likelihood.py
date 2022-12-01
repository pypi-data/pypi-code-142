from io import BytesIO
import pandas as pd

from .utils import df_to_csv_buffer
from .utils.storage import file_exists, load_from_storage, write_to_storage
from .utils.cycle import find_cycles
from .cycle_yield import cycle_yield_distribution


def _read_likl_file(likl_filename: str):
    data = load_from_storage(likl_filename)
    return pd.read_csv(BytesIO(data)).set_index('cycle.id')


def _generate_likl_file(country_id: str, product_id: str, filepath: str, limit: int):
    cycles = find_cycles(country_id, product_id, limit=limit)
    df_yield = cycle_yield_distribution(cycles)
    if len(df_yield) > 0:
        write_to_storage(filepath, df_to_csv_buffer(df_yield))
    return df_yield


def likl_filename(country_id: str, product_id: str): return f'{country_id}_{product_id}_non-aggregated_cycles.csv'


def generate_likl_yield_file(country_id: str, product_id: str, limit: int = 10000, overwrite=False):
    """
    Return all likelihood data for a given country and a given product.
    If likelihood file exisits, data will be read in; otherwise, generate likelihood data and store
    into likl_filename path.

    Parameters
    ----------
    country_id: str
        Region `@id` from Hestia glossary, e.g. 'GADM-GBR', or 'region-south-america'.
    product_id: str
        Product term `@id` from Hestia glossary, e.g. 'wheatGrain'.
    limit: int
        Max number of Cycles to compute likelihood data. Defaults to `10000`.
    overwrite: bool
        Whether to overwrite existing likelihood file or not. Defaults to `False`.

    Returns
    -------
    pd.DataFrame
        A dataframe storing the likelihood data.
    """
    filepath = likl_filename(country_id, product_id)
    read_existing = file_exists(filepath) and not overwrite
    return _read_likl_file(filepath) if read_existing else _generate_likl_file(country_id, product_id, filepath, limit)
