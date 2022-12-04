from typing import Union
import pandas as pd
from pandas.core.frame import DataFrame, Series


def series_to_dataframe(
    df: Union[pd.Series, pd.DataFrame]
) -> (Union[pd.Series, pd.DataFrame], bool):
    dataf = df.copy()
    isseries = False
    if isinstance(dataf, pd.Series):
        columnname = dataf.name
        dataf = dataf.to_frame()

        try:
            dataf.columns = [columnname]
        except Exception:
            dataf.index = [columnname]
            dataf = dataf.T
        isseries = True

    return dataf, isseries


def get_duplicates(
    df: Union[pd.DataFrame, pd.Series], subset: Union[list, None] = None
):
    df2, isseries = series_to_dataframe(df)
    df2 = df2.reset_index(drop=True)
    if subset is None:
        subset = df2.columns.to_list()
    count = 0
    dupis = df2.loc[
        list(
            set(df2.index.to_list()).symmetric_difference(
                set(df2.drop_duplicates(subset=subset, keep=False).index.to_list())
            )
        )
    ]
    dupis2 = dupis.copy()
    for col in dupis:
        try:
            dupis[col] = dupis[col].astype("string")
            dupis[col] = dupis[col].fillna("")
        except Exception:
            pass
    allresa = []
    for name, group in dupis.groupby(subset):
        groupindex = len(group.index) * [tuple(group.index.to_list())]
        allresa.append(dupis2.loc[group.index].copy().assign(DUPLICATEINDEX=groupindex))
        count += 1
    return pd.concat(allresa, ignore_index=True)

def pd_add_duplicates_to_df():
    DataFrame.ds_get_duplicates = get_duplicates
    Series.ds_get_duplicates = get_duplicates

