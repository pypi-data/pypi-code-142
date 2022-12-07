"""@Author: Rayane AMROUCHE

Data Sources Handling
"""

from typing import Any
from logging import Logger


class DataSource():
    """Data Source Class
    """

    def __init__(self, logger: Logger) -> None:
        """Init a Data Source

        Args:
            logger (Logger): Passed down logger from the Data Manager
        """
        self.logger = logger

    def read(self, source_info: dict, **kwargs: Any) -> Any:
        """Read source and returns the source data

        Args:
            source_info (dict): Source metadatas

        Raises:
            Exception: Raised if missing needed metadatas

        Returns:
            Any: Source datas
        """
        if "args" in source_info:
            source_info["args"].update(**kwargs)

    def read_db(self, source_info: dict, **kwargs: Any) -> Any:
        """Read source and returns a source engine

        Args:
            source_info (dict): Source metadatas

        Raises:
            Exception: Raised if missing needed metadatas

        Returns:
            Any: Source engine
        """
        if "args" in source_info:
            source_info["args"].update(**kwargs)
