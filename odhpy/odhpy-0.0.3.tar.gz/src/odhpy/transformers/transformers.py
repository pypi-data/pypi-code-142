import pandas as pd

def to_exceedence(obs_df, mod_df, plotting_position="cunnane") -> pd.DataFrame:
    """_summary_

    Args:
        obs_df (_type_): _description_
        mod_df (_type_): _description_
        plotting_position (str, optional): _description_. Defaults to "cunnane". Other supported values: "weibull", "gringorten". See https://glossary.ametsoc.org/wiki/Plotting_position

    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
    """
    df = obs_df.join(mod_df, how='inner')
    df = df.dropna()
    df.columns = ['x', 'y']
    df.x = df.x.sort_values(ascending=False).values
    df.y = df.y.sort_values(ascending=False).values
    n = len(df)
    index_starting_at_one = [i + 1 for i in range(n)]
    if plotting_position == "cunnane":
        df.index = [100 * (r - 0.4)/(n + 0.2) for r in index_starting_at_one]
    elif plotting_position == "weibull":
        df.index = [100 * (r/(n + 1)) for r in index_starting_at_one]
    elif plotting_position == "gringorten":
        df.index = [100 * (r - 0.44)/(n + 0.12) for r in index_starting_at_one]
    else:
        raise Exception(f"Plotting position not supported: {plotting_position}")
    return df