from io import BytesIO
import pandas as pd
import numpy as np
from hestia_earth.utils.api import download_hestia

SIGMA_SCALER = 2.5  # Scaler (for standard deviation) value of the prior


def is_nonempty_str(value): return (type(value) in [str, np.str_, np.string_]) and value != ''


def get_stats_from_df(df, country_id: str, product_id: str):
    try:
        yield_stats = df.loc[product_id][country_id]
        # this happens when read priors in from a CSV file
        vals = [float(v) for v in yield_stats.strip('()').split(',')] if type(yield_stats) == str else yield_stats
        return vals[0], vals[1]  # mu, sigma
    except Exception:
        return None, None  # data could not be parsed


def get_fert_group_name(fert_id: str):
    """
    Look up the fertiliser group (N, P2O5, K2O) of a Hestia fertliser term

    Parameters
    ----------
    fert_id: str
        Inorganic or organic fertiliser term ID from Hestia glossary, e.g. 'ammoniumNitrateKgN'.

    Returns
    -------
    str
        fertiliser group, e.g. 'N', 'P2O5' or 'K2O'.
    """
    units = download_hestia(fert_id).get('units')
    return units.replace('kg ', '') if units else None


def df_to_csv_buffer(df: pd.DataFrame):
    buffer = BytesIO()
    df.to_csv(buffer)
    return buffer.getvalue()
