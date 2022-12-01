import pandas as pd
import sqlalchemy
from dataclasses import dataclass


@dataclass
class PostgresManager:
    """Manage database connection."""

    database: str
    password: str = ""
    host: str = "localhost"
    port: str = "5432"
    user: str = "postgres"

    def __post_init__(self):
        # self.URL = f"postgresql://postgres@localhost:5432/postgres"
        self.URL = (
            f"postgresql://{self.user}:{self.password}@{self.host}:5432/{self.database}"
        )
        self.engine = sqlalchemy.create_engine(self.URL)

    def create_table(self, name: str, df: pd.DataFrame) -> pd.DataFrame:
        """Creates a SQL table, replace if exists.

        Args:
            name (str): Table name.
            df (pd.DataFrame): Dataframe to use for creating table.

        Returns:
            pd.DataFrame: Returns the dataframe confirmation fromq querying the SQL database.
        """
        df.to_sql(name, self.engine, if_exists="replace")
        return pd.read_sql_table(name, self.engine)

    def read_table(self, name: str, **kwargs) -> pd.DataFrame:
        """Read a single table by name.

        Args:
            name (str): Name of table.

        Returns:
            pd.DataFrame: Dataframe from table.
        """
        return pd.read_sql_table(name, self.engine, **kwargs)

    def read_join(
        self, left: str, right: str, last: str = None, **kwargs
    ) -> pd.DataFrame:
        """Get a dataframe from the join of two tables.
        If "last" is included, join it to the join of the first two.

        Args:
            left (str): Left table in join.
            right (str): Right table in join.
            last (str, optional): Right join after the first join. Defaults to None.

        Returns:
            pd.DataFrame: Joined dataframe.
        """
        left_df = pd.read_sql_table(left, self.engine)
        right_df = pd.read_sql_table(right, self.engine)
        if last is None:
            return pd.merge(left_df, right_df, **kwargs)
        last_df = pd.read_sql_table(last, self.engine)
        return pd.merge(pd.merge(left_df, right_df), last_df, **kwargs)

    def read_query(self, query: str, **kwargs) -> pd.DataFrame:
        return pd.read_sql_query(query, self.engine, **kwargs)
