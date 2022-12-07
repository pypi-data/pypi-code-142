"""@Author: Rayane AMROUCHE

Utils for DataManager
"""

import os

from typing import Any, List
from datetime import datetime
from io import StringIO

import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import plotly.express as px  # type: ignore
import plotly.figure_factory as ff  # type: ignore

from IPython.display import display  # type: ignore

from dsmanager.controller.utils import is_interactive
from dsmanager.controller.logger import make_logger


class SklearnWrapperException(Exception):
    """Exception raised for errors related to the Sklearn function and class's
        wrapper
    """

    def __init__(self,
                 message: str):
        """Init the Exception

        Args:
            message (str, optional): Exception message. Defaults to "Data Type
                unknown or not supported".
        """

        self.message = message
        super().__init__(self.message)


class DataManagerIOException(Exception):
    """Exception raised for errors related to the DataManager reader and saver
    """

    def __init__(self,
                 file_info: dict,
                 message: str = "Data source unknown or not supported"):
        """Init the Exception

        Args:
            file_info (dict): File metadata informations
            message (str, optional): Exception message. Defaults to "Data Type
                unknown or not supported".
        """

        self.file_info = file_info
        self.message = message
        super().__init__(self.message)


class Utils:
    """Utils class brings utils tools for the data manager
    """

    def __init__(self,
                 dm_: Any,
                 logger_path: str = "/tmp/logs"):
        """Init class Utils with an empty local storage
        """
        self.dm_ = dm_
        self.logger = make_logger(
            os.path.join(logger_path, "datamanager"),
            "utils"
        )

    def get_local(self, name: str) -> Any:
        """Return a variable from local vars given its name

        Args:
            name (str): key name of the var in local vars
        """
        return self.dm_.local_vars[name]

    def copy_as(self,
                df_: pd.DataFrame,
                name: str) -> pd.DataFrame:
        """Copy a pandas DataFrame in the datamanager with a given name

            Args:
                df_ (pd.DataFrame): DataFrame to save
                name (str): Alias of the DataFrame in the DataStorage of the
                    DataManager

            Returns:
                pd.DataFrame: Returns original DataFrame to keep chaining
        """
        self.dm_.data_store[name] = df_
        return df_

    def sklearn_wrapper(self,
                        df_: pd.DataFrame,
                        func: Any,
                        output_cols: List[str] = None,
                        save: bool = False,
                        **kwargs: Any) -> pd.DataFrame:
        """Wrap sklearn functions and classes

        Args:
            df_ (pd.DataFrame): DataFrame whose head is to be displayed
            func (Any): Function to wrap

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        if output_cols is None:
            output_cols = []

        if "X" in kwargs:
            var_x = kwargs["X"]
            kwargs["X"] = df_[var_x]
            if "y" in kwargs:
                var_y = kwargs["y"]
                kwargs["y"] = df_[var_y].values.ravel()

            func_name = (
                str(func)
                .split(" ", 3)[-2]
                .replace(".", "_")
                if "." in str(func)
                else func.__name__
            )
            self.logger.info("Launch %s", func_name)
            res = func(**kwargs)

            output_nb = len(output_cols)

            var_name = func_name + "_" + datetime.now().strftime("%Y%m%d%H%M%S")
            if save:
                self.logger.info("Saved %s in local vars", var_name)
                self.dm_.local_vars[var_name] = res

            if isinstance(res, np.ndarray) and len(df_) == res.shape[0]:
                if not output_nb:
                    if res.ndim == 1 or res.shape[-1] == 1:
                        output_cols = [func_name + "_0"]
                        res = res.reshape(-1, 1)
                    else:
                        output_cols = [func_name + "_" +
                                       str(e) for e in range(res.shape[-1])]
                elif output_nb == 1 and (res.ndim == 1 or res.shape[-1] == 1):
                    res = res.reshape(-1, 1)
                elif output_nb not in [res.ndim, res.shape[-1]]:
                    raise SklearnWrapperException(
                        "Output_cols len does not match the output length"
                        f"(input is {str(output_nb)} instead of " +
                        str(res.shape[-1]) + ")"
                    )

                df_[output_cols] = res
            else:
                self.logger.info("Output of %s:%s -> %s (saved=%s)",
                                 func_name,
                                 str(type(res))[8:][:-2],
                                 res,
                                 var_name if save else "None"
                                 )
        else:
            raise SklearnWrapperException("Missing X (list of features)")
        return df_

    def head(self, df_: pd.DataFrame, n_val: int = 5) -> pd.DataFrame:
        """Print head of a dataframe

        Args:
            df_ (pd.DataFrame): DataFrame whose head is to be displayed
            n_val (int, optional): Number of rows to display. Defaults to 5.

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        if is_interactive():
            self.logger.info("NOTEBOOK - Head")
            display(df_.head(n_val))
        else:
            self.logger.info("Head:\n%s", df_.head(n_val).to_string())

        return df_

    def tail(self, df_: pd.DataFrame, n_val: int = 5) -> pd.DataFrame:
        """Print tail of a dataframe

        Args:
            df_ (pd.DataFrame): DataFrame whose tail is to be displayed
            n_val (int, optional): Number of rows to display. Defaults to 5.

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        if is_interactive():
            self.logger.info("NOTEBOOK - Tail")
            display(df_.tail(n_val))
        else:
            self.logger.info("Tail:\n%s", df_.tail(n_val).to_string())

        return df_

    def info(self, df_: pd.DataFrame) -> pd.DataFrame:
        """Print DataFrame info

        Args:
            df_ (pd.DataFrame): DataFrame whose info is to be displayed

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        buf = StringIO()
        df_.info(buf=buf, verbose=True, show_counts=True)
        self.logger.info("Info:\n%s", buf.getvalue())

        return df_

    def describe(self, df_: pd.DataFrame) -> pd.DataFrame:
        """Print DataFrame description

        Args:
            df_ (pd.DataFrame): DataFrame whose description is to be displayed

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """

        if is_interactive():
            self.logger.info("NOTEBOOK - Description")
            display(df_.describe())
        else:
            self.logger.info("Description:\n%s", df_.describe().to_string())

        return df_

    def columns(self, df_: pd.DataFrame) -> pd.DataFrame:
        """Print DataFrame columns names

        Args:
            df_ (pd.DataFrame): DataFrame whose columns is to be displayed

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        self.logger.info("Columns: %s", df_.columns.values)

        return df_

    def set_local_var(self, df_: pd.DataFrame,
                      var_name: str,
                      var_value: Any) -> pd.DataFrame:
        """Set a local variable during chaining

        Args:
            df_ (pd.DataFrame): Current DataFrame to be returned
            var_name (str): Name of the local variable
            var_value (Any): Value of the local variable

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        self.dm_.local_vars[var_name] = var_value
        return df_

    def save_df(self, df_: pd.DataFrame, df_name: str) -> pd.DataFrame:
        """Save the current DataFrame in local_vars

        Args:
            df_ (pd.DataFrame): Current DataFrame to be returned
            df_name (str): Name of the DataFrame variable

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        self.dm_.local_vars[df_name] = df_
        return df_

    def scatter_matrix(self, df_: pd.DataFrame, **kwargs: Any) -> pd.DataFrame:
        """Plot a scatterplot matrix of the current dataframe using plotly
            express scatter

        Args:
            df_ (pd.DataFrame): Current DataFrame to be returned
            kwargs (Any): Dictionnary of parameters for plotly express scatter

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        fig = ff.create_scatterplotmatrix(df_, diag='histogram', **kwargs)
        fig.show()
        return df_

    def displot(self, df_: pd.DataFrame, name: str, **kwargs: Any) -> pd.DataFrame:
        """Plot a distplot for a given variable of the current dataframe using
            plotly figure factory create_distplot

        Args:
            df_ (pd.DataFrame): Current DataFrame to be returned
            name (str): Variable for which distribution will be ploted

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        fig = ff.create_distplot([df_[name]], [name], **kwargs)
        fig.show()
        return df_

    def corr(self, df_: pd.DataFrame, squared: bool = False, **kwargs: Any) -> pd.DataFrame:
        """Plot a scatterplot matrix of the current dataframe using plotly
            express scatter

        Args:
            df_ (pd.DataFrame): Current DataFrame to be returned
            kwargs (Any): Dictionnary of parameters for plotly express scatter

        Returns:
            pd.DataFrame: Returns original DataFrame to keep chaining
        """
        corr = df_.corr()
        if squared:
            corr = corr ** 2
        fig = px.imshow(corr,
                        color_continuous_scale="Viridis",
                        text_auto=True,
                        aspect="auto",
                        **kwargs
                        )
        fig.show()
        self.logger.info("Correlation Matrix:\n%s", corr.to_string())
        return df_


def to_datamanager(df_: pd.DataFrame,
                   datamanager: Any,
                   name: str,
                   **kwargs: Any
                   ) -> pd.DataFrame:
    """Get info for a specified dataset and return it as a DataFrame

    Args:
        df_ (pd.DataFrame): DataFrame to be saved
        dm (DataManager): DataManager where the DataFrame will be saved
        name (str): Name of the dataset to save

    Returns:
        pd.DataFrame: Returns original DataFrame to keep chaining
    """
    file_info = datamanager.get_file_info(name)
    datamanager.save_data(df_, file_info, **kwargs)
    return df_


pd.core.base.PandasObject.to_datamanager = to_datamanager
