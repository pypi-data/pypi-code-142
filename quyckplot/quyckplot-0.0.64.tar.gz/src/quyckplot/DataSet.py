"""
This file contains the DataSet class.
The purpose of this class is to store data from multiple files in a single object.
The class' main attribute is the dataframes attribute, which is a list of dictionaries.
Each dictionary contains the data from a single file as well as the parameters of that file.
For example, if the file name is "T=10K-I=1.5A.csv", then the dictionary may be as follows:
    {
        "data": pd.DataFrame(...),
        "params": {
            "temp": "10",
            "current": "1.5"
        }
    }
The user can choose the "params" format.
The class contains methods for plotting the data.
"""

import pandas as pd
from .utils import getFileNamesFromRegex, formatted_string2dict
from .Plotter import Plotter

class DataSet:
    def __init__(self):
        self.dataframes = []

    @classmethod
    def fromFiles(cls, filenames, name_format="", dir="", **kwargs):
        """
        Creates a new DataSet object from the given files.
        """
        data = cls()
        data.loadFromFileNames(filenames, name_format, dir=dir, **kwargs)
        return data

    @classmethod
    def fromRegex(cls, regex, name_format, dir="", **kwargs):
        """
        Creates a new DataSet object from the files matching the given regex.
        """
        data = cls()
        data.loadFromRegex(regex, name_format, dir=dir, **kwargs)
        return data

    def clearData(self):
        self.dataframes = []

    def map(self, func):
        for df in self.dataframes:
            func(df)

    def plot(self, x="x", y="y", *args, **kwargs):
        Plotter.plot(self, x, y, *args, **kwargs)

    def scatter(self, x="x", y="y", *args, **kwargs):
        Plotter.scatter(self, x, y, *args, **kwargs)

    def loadFromFileNames(self, filenames, name_format, columns=None, dir="", **kwargs):  
        """
        Loads data from the files at the given paths.
        """
        self.clearData()

        if columns is None:
            columns = ["x", "y"]
        # for each file, read it as csv and append it to the list of dataframes
        for name in filenames:
            path = f"{dir}/{name}" if dir else name

            # raise an error if the extension is not csv, txt or xls
            if not path.endswith(".csv") and not path.endswith(".txt") and not path.endswith(".xls"):
                raise Exception(f"File {path} has an invalid extension.")
            else:
                df = pd.read_csv(path, names=columns, **kwargs)
            
            params = formatted_string2dict(name, name_format)
            self.dataframes.append({"params": {"name": name, **params}, "data": df})

    def loadFromRegex(self, regex, name_format, dir="", **kwargs):
        """
        Loads data from the files at the given paths.
        """
        paths = getFileNamesFromRegex(regex, dir)
        self.loadFromFileNames(paths, name_format, dir=dir, **kwargs)