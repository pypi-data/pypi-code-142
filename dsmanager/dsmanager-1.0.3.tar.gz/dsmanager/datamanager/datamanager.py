"""@Author: Rayane AMROUCHE

Datamanager Class
"""

import os
import io

from urllib.parse import quote
from typing import Any, Tuple

import paramiko  # type: ignore
import requests  # type: ignore
import sqlalchemy  # type: ignore
import pandas as pd  # type: ignore

from dotenv import load_dotenv  # type: ignore
from shareplum import Site  # type: ignore
from shareplum import Office365  # type: ignore
from shareplum.site import Version  # type: ignore

from dsmanager.datamanager.utils import Utils
from dsmanager.controller.logger import make_logger
from dsmanager.controller.utils import json_to_dict
from dsmanager.datamanager.datastorage import DataStorage

REQUEST_PARAMS = [
    "url", "data", "json", "params", "headers", "cookies",
    "files", "auth", "timeout", "allow_redirects", "proxies", "hooks",
    "stream", "verify", "cert",
]


class DataManagerIOException(Exception):
    """Exception raised for errors related to the DataManager reader and saver
    """

    def __init__(self,
                 file_info: dict,
                 message: str = "Data Type unknown or not supported"):
        """Init the Exception

        Args:
            file_info (dict): File metadata informations
            message (str, optional): Exception message. Defaults to "Data Type
                unknown or not supported".
        """

        self.file_info = file_info
        self.message = message
        super().__init__(self.message)


class DataManager:
    """DataManager class handle all the data work"""

    def __init__(self,
                 metafile_path: str = "data/metadata.json",
                 logger_path: str = "/tmp/logs",
                 env_path: str = None,
                 preload=False
                 ) -> None:
        """Init Datamanager by giving the datasets metadata path

        Args:
            metafile_path (str, optional): Path of the metadata file of the
                datasets. Defaults to "data/metadata.json".
        """
        if env_path:
            load_dotenv(env_path)

        json_to_dict(metafile_path)
        self.metadata_path = metafile_path
        self.local_vars = DataStorage()
        self.data_store = DataStorage()
        self.database_store = DataStorage()
        self.logger = make_logger(
            os.path.join(logger_path, "datamanager"),
            "datamanager"
        )

        self.utils = Utils(self, logger_path)

        if preload:
            metadata = json_to_dict(self.metadata_path)
            for key in metadata.keys():
                try:
                    self.get_data(key)
                    self.logger.info("Preloaded %s", key)
                except DataManagerIOException as dm_e:
                    self.logger.info("Failed to preload '%s' with message : '%s'",
                                     key,
                                     dm_e)

    def handle_local(self, file_info: dict) -> str:
        """function that returns a local/online file to be read by pandas

        Args:
            file_info (dict): file metadata

        Returns:
            str: path of the local file or url
        """
        file = file_info["path"]
        self.logger.info("Handle local file in path: %s", file)
        return file

    def handle_sftp(self, file_info: dict) -> str:
        """function that returns a local/online file to be read by pandas

        Args:
            file_info (dict): file metadata

        Returns:
            str: path of the local file or url
        """
        sftp_server = file_info["sftp_server"]
        port = int(file_info["port"])
        username = os.environ.get(file_info["username_env_name"], "")
        password = os.environ.get(file_info["password_env_name"], "")

        transport = paramiko.Transport((sftp_server, port))
        transport.connect(None, username, password)
        engine = paramiko.SFTPClient.from_transport(transport)

        file = None
        if "path" in file_info:
            file = engine.open(file_info["path"])

        self.logger.info(
            "Handle sftp file in path: %s on server %s", file, sftp_server)
        return file, engine

    def handle_query(self, file_info: dict) -> Tuple[str, sqlalchemy.engine.Engine]:
        """function that returns a query the engine to request it

        Args:
            file_info (dict): file metadata

        Returns:
            Tuple[str, sqlalchemy.engine.Engine]: query to request, engine to
                connect to the database
        """
        dialect = file_info["dialect"]
        database = file_info["database"]
        username = os.environ.get(file_info["username_env_name"], "")
        password = os.environ.get(file_info["password_env_name"], "")
        address = file_info["address"]
        eng_str = f"{dialect}://{username}:{quote(password)}@{address}/{database}"
        log_str = f"{dialect}://{username}:***@{address}/{database}"
        engine = sqlalchemy.create_engine(eng_str)
        query = file_info["query"] or file_info["table_name"]
        self.logger.info(
            "Query sql server '%s' with main param: '%s'", log_str, query)
        return query, engine

    def format_request(self, file_info: dict):
        """function that take kwargs and returns a dict of parameters for requests

        Args:
            file_info (dict): file metadata

        Returns:
            dict: dict of parameters for requests
        """
        request_params = {}

        for param in REQUEST_PARAMS:
            if param in file_info:
                request_params[param] = file_info[param]
            if param in file_info["args"]:
                if param in request_params and isinstance(file_info[param], dict):
                    request_params[param].update(file_info["args"][param])
                else:
                    request_params[param] = file_info["args"][param]
                del file_info["args"][param]
        return request_params

    def handle_request(self, file_info: dict) -> str:
        """function that returns a json file from a request

        Args:
            file_info (dict): file metadata

        Returns:
            str: path of the local file or url
        """
        session = requests.Session()

        args = self.format_request(file_info)

        if file_info['request_type'] == "get":
            res = session.get(**args)
        elif file_info['request_type'] == "post":
            res = session.post(**args)
        else:
            raise DataManagerIOException(file_info, "request type not handled")

        self.logger.info(
            "Handle request '%s' with response: '%s'", str(args), res)
        if file_info["type"] == "json":
            file = res.json()
        elif file_info["type"] == "text":
            file = res.text
        else:
            file = res
        return file

    def handle_sharepoint(self, file_info: dict) -> str:
        """function that returns a sharepoint file to be read by pandas

        Args:
            file_info (dict): file metadata

        Returns:
            str: binary file
        """
        path = file_info['sharepoint_path'].split("/")
        authcookie = Office365(
            "/".join(path[:3]),
            username=os.environ.get(file_info["username_env_name"]),
            password=os.environ.get(file_info["password_env_name"]),
        ).GetCookies()
        site = Site(
            "/".join(path[:5]),
            version=Version.v365,
            authcookie=authcookie,
        )
        folder = site.Folder("/".join(path[5:-1]))
        file = folder.get_file(path[-1])

        if isinstance(file, bytes) and "encoding" in file_info:
            try:
                file = io.StringIO(file.decode(file_info["encoding"]))
            except UnicodeDecodeError:
                return file

        self.logger.info(
            "Handle sharepoint file '%s' in site '%s'",
            "/".join(path[-1]),
            "/".join(path[:5])
        )

        return file

    def get_file_info(self, name: str) -> dict:
        """Handle access to metadata info for a given dataset

        Args:
            name (str): Name of the dataset to access

        Raises:
            Exception: Raised if the name given is not in the metadata dict

        Returns:
            dict: Return the metadata of the dataset
        """
        metadata = json_to_dict(self.metadata_path)
        if name not in metadata:
            raise DataManagerIOException(
                {}, f"{name} not in the metadata file")
        data = metadata[name]
        return data

    def read_data(self, file_info: dict, **kwargs: Any) -> pd.DataFrame:
        """Read a dataset as a pandas DataFrame from a file metadata

        Args:
            file_info (dict): Metadata of a file containing a dataset

        Raises:
            Exception: Raised if the Data type is not supported

        Returns:
            pd.DataFrame: DataFrame of the dataset file
        """

        file_info["args"].update(**kwargs)

        engine = None

        if "sharepoint_path" in file_info:
            file = self.handle_sharepoint(file_info)
        elif "dialect" in file_info:
            query, engine = self.handle_query(file_info)
        elif "url" in file_info:
            file = self.handle_request(file_info)
        elif "sftp_server" in file_info:
            file, engine = self.handle_sftp(file_info)
        else:
            file = self.handle_local(file_info)

        if file_info["type"] == "csv":
            data = pd.read_csv(file, **file_info["args"])
        elif file_info["type"] == "excel":
            data = pd.read_excel(file, **file_info["args"])
        elif file_info["type"] == "sql":
            conn = engine.connect()
            data = pd.read_sql_query(query, conn, **file_info["args"])
            conn.close()
        elif file_info["type"] == "json":
            data = pd.Series(file)
        elif file_info["type"] == "text":
            data = file
        else:
            raise DataManagerIOException(file_info)
        if engine:
            engine.close()

        return data

    def save_data(self, df_: pd.DataFrame, file_info: dict, **kwargs: Any):
        """Save a pandas DataFrame given info from a file metadata

        Args:
            df_ (pd.DataFrame): DataFrame to be saved
            file_info (dict): Metadata of a file to receive a dataset

        Raises:
            Exception: Raised if the Data type is not supported
        """

        file_info["args"].update(**kwargs)

        if "sharepoint" in file_info:
            raise DataManagerIOException(file_info,
                                         "Saving does not handle sharepoint")
        if "dialect" in file_info:
            table_name, engine = self.handle_query(file_info)
        else:
            file = self.handle_local(file_info)

        if file_info["type"] == "csv":
            try:
                folder = os.path.dirname(file)
                os.makedirs(folder, exist_ok=True)
            finally:
                df_.to_csv(file, **file_info["args"])
        elif file_info["type"] == "excel":
            try:
                folder = os.path.dirname(file)
                os.makedirs(folder, exist_ok=True)
            finally:
                df_.to_excel(file, **file_info["args"])
        elif file_info["type"] == "sql":
            conn = engine.connect()
            df_.to_sql(table_name, conn, index=False,
                       **file_info["args"])
            conn.close()
        else:
            raise DataManagerIOException(file_info)

    def read_database(self,
                      file_info: dict,
                      **kwargs: Any
                      ) -> Any:
        """Read a dataset as a pandas DataFrame from a file metadata

        Args:
            file_info (dict): Metadata of a database

        Raises:
            Exception: Raised if the Database type is not supported

        Returns:
            Any: SqlAlchemy or SFTP engine of the database
        """

        file_info["args"].update(**kwargs)

        if "dialect" in file_info:
            _, engine = self.handle_query(file_info)
        elif "sftp_server" in file_info:
            _, engine = self.handle_sftp(file_info)
        else:
            raise DataManagerIOException(file_info)

        return engine

    def get_data(self,
                 name: str,
                 save: bool = True,
                 reload: bool = False,
                 alias: str = None,
                 **kwargs: Any
                 ) -> pd.DataFrame:
        """Get info for a specified dataset and return it as a DataFrame

        Args:
            name (str): Name of the dataset to return
            save (bool, optional): If True save DataFrame of the requested
                dataset. Defaults to True.
            reload (bool, optional): If False try to load from data_store.
                Defaults to False.
            alias (str, optional): Alias name of the dataset in the data_store.
                Defaults to None.

        Returns:
            pd.DataFrame: Requested Dataset as a DataFrame
        """
        if not reload and name in self.data_store:
            data = self.data_store[name]
        else:
            file_info = self.get_file_info(name)
            data = self.read_data(file_info, **kwargs)
        if save:
            self.data_store[name] = data
            if alias:
                self.data_store[alias] = self.data_store[name]

        return data

    def get_database(self,
                     name: str,
                     save: bool = True,
                     reload: bool = False,
                     alias: str = None,
                     **kwargs: Any
                     ) -> sqlalchemy.engine.Engine:
        """Get info for a specified dataset and return it as a DataFrame

        Args:
            name (str): Name of the dataset to return
            save (bool, optional): If True save DataFrame of the requested
                dataset. Defaults to True.
            reload (bool, optional): If False try to load from database_store.
                Defaults to False.
            alias (str, optional): Alias name of the dataset in the data_store.
                Defaults to None.

        Returns:
            sqlalchemy.engine.Engine: Requested Database as an sqlalchemy engine
        """
        if not reload and name in self.database_store:
            database = self.database_store[name]
        else:
            file_info = self.get_file_info(name)
            database = self.read_database(file_info, **kwargs)
        if save:
            self.database_store[name] = database
            if alias:
                self.data_store[alias] = self.data_store[name]
        return database

    def get_env(self,
                name: str,
                default: str = "",
                ) -> str:
        """Get info for a specified dataset and return it as a DataFrame

        Args:
            name (str): Name of the variable in env
            default (str): Default value if name is not in env
            env_path (str): Path of the env file

        Returns:
            str: env variable
        """
        res = os.environ.get(name, default)
        return res


def to_datamanager(df_: pd.DataFrame,
                   datamanager: DataManager,
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
