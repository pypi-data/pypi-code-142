import pandas as pd
from .utils import getFileNamesFromRegex, formatted_string2dict
from scipy import stats
import numpy as np

class DataSet:
    def __init__(self, title=""):
        self.title = title
        self.dataframes = []

    def clearData(self):
        """
        Clears the list of dataframes.
        """
        self.dataframes = []

    def map(self, func):
        """
        Applies the given function to each dataframe in the list of dataframes.
        """
        for df in self.dataframes:
            df["data"] = func(df["data"])

    def fit(self, x, y, **kwargs):
        """
        Fits a linear regression to the data.
        """
        def fit(df):
            r = stats.linregress(df[x],df[y])
            slope, intercept, stderr, intercept_stderr = r.slope, r.intercept, r.stderr, r.intercept_stderr
            
            x_fit = np.linspace(x.min(), x.max(), 100)
            y_fit = slope * x_fit + intercept

            df["fit"] = y_fit

        self.map(fit)


    def loadFromFileNames(self, filenames, name_format, dir="", **kwargs):  
        """
        Loads data from the files at the given paths.
        """
        self.clearData()
        # for each file, read it as csv or txt and append it to the list of dataframes
        for name in filenames:
            if dir:
                path = f"{dir}/{name}"
            else:
                path = name

            # raise an error if the extension is not csv, txt or xls
            if not path.endswith(".csv") and not path.endswith(".txt") and not path.endswith(".xls"):
                raise Exception(f"File {path} has an invalid extension.")
            else:
                df = pd.read_csv(path, **kwargs)
            
            params = formatted_string2dict(name, name_format)
            self.dataframes.append({"params": params, "data": df})

    def loadFromRegex(self, regex, name_format, columns, dir="", **kwargs):
        """
        Loads data from the files at the given paths.
        """
        self.clearData()
        paths = getFileNamesFromRegex(regex, dir)

        self.loadFromFileNames(paths, name_format, columns, dir=dir, **kwargs)