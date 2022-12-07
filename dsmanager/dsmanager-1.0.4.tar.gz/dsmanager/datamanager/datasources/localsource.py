"""@Author: Rayane AMROUCHE

Local Sources Handling
"""

from typing import Any

import pandas as pd  # type: ignore

from dsmanager.datamanager.datasources.datasource import DataSource
from dsmanager.datamanager.utils import DataManagerIOException


class LocalSource(DataSource):
    """Inherited Data Source Class for local sources
    """

    def read(self, source_info: dict, **kwargs: Any) -> Any:
        """Handle source and returns the source data

        Args:
            source_info (dict): Source metadatas

        Returns:
            Any: Source datas
        """
        data = None

        super().read(source_info, **kwargs)

        path = source_info["path"]

        if source_info["type"] == "csv":
            data = pd.read_csv(path, **source_info["args"])
        elif source_info["type"] == "excel":
            data = pd.read_excel(path, **source_info["args"])
        elif source_info["type"] == "json":
            data = pd.Series(path)
        elif source_info["type"] == "text":
            encoding = "utf-8"
            if "encoding" in source_info:
                encoding = source_info["encoding"]
            with open(path, "r", encoding=encoding) as file:
                data = file.read()
        else:
            raise DataManagerIOException(
                source_info,
                "File type unknown or not supported"
            )

        self.logger.info(
            "Get '%s' file from '%s'",
            source_info["type"],
            source_info["path"]
        )
        return data

    def read_db(self, source_info: dict, **kwargs: Any) -> Any:
        """Read source and returns a source engine

        Args:
            source_info (dict): Source metadatas

        Raises:
            Exception: Raised if missing needed metadatas

        Returns:
            Any: Source engine
        """

        super().read(source_info, **kwargs)
        raise DataManagerIOException(
            source_info,
            "Local source does not handle read_db"
        )
