'''
Methods:
1. rangeFinder
'''

def rangeFinder(df):
    ## START
    """
    Parameters
    ----------
    df : dataframe
        1 .dataframe should contain numerical columns named open, high, low, close
        2. dataframe should contain atleast 15 rows
    """
    ## END

    short_sma= 5
    long_sma = 10
    SMAs=[short_sma, long_sma]

    for i in SMAs:
        df["SMA_"+str(i)]= ((9.9 * (df["high"].shift(1) - df["low"].shift(1)) + 0.1 * (abs(df["open"] - df["open"].shift(1))))/10).rolling(window=i).mean()/2
    df["R1"] = df["open"] + df["SMA_5"]
    df["R2"] = df["open"] + df["SMA_10"]
    df["S1"] = df["open"] - df["SMA_5"]
    df["S2"] = df["open"] - df["SMA_10"]

    return df