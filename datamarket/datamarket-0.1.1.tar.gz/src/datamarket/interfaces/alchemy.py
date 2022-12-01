########################################################################################################################
# IMPORTS

import logging
from urllib.parse import quote_plus

from sqlalchemy import create_engine, DDL
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

########################################################################################################################
# CLASSES

logger = logging.getLogger(__name__)


class AlchemyInterface:
    def __init__(self, config):
        if "db" in config:
            self.config = config["db"]

            self.engine = create_engine(self.get_conn_str())
            self.session = sessionmaker(bind=self.engine)()
            self.cursor = self.session.connection().connection.cursor()

        else:
            logger.warning("no db section in config")

    def get_conn_str(self):
        return (
            f'{self.config["engine"]}://'
            f'{self.config["user"]}:{quote_plus(self.config["password"])}'
            f'@{self.config["host"]}:{self.config["port"]}'
            f'/{self.config["database"]}'
        )

    @staticmethod
    def get_schema_from_table(table):
        for table_arg in table.__table_args__:
            if isinstance(table_arg, dict) and "schema" in table_arg:
                return table_arg["schema"]

    def create_tables(self, tables):
        for table in tables:
            schema = self.get_schema_from_table(table)
            self.engine.execute(DDL(f"CREATE SCHEMA IF NOT EXISTS {schema}"))

            if not self.engine.has_table(table.__tablename__, schema=schema):
                logger.info(f"creating table {table.__tablename__}...")
                table.__table__.create(self.engine)
            else:
                logger.info(f"table {table.__tablename__} already exists")

    def drop_tables(self, tables):
        for table in tables:
            schema = self.get_schema_from_table(table)

            if self.engine.has_table(table.__tablename__, schema=schema):
                logger.info(f"dropping table {table.__tablename__}...")
                self.engine.execute(
                    DDL(f"DROP TABLE {schema}.{table.__tablename__} CASCADE")
                )

    def reset_db(self, tables, drop):
        if drop:
            self.drop_tables(tables)

        self.create_tables(tables)

    def insert_alchemy_obj(self, alchemy_obj):
        try:
            logger.info(f"adding {alchemy_obj}...")

            self.session.add(alchemy_obj)
            self.session.commit()

        except IntegrityError:
            logger.info(f"{alchemy_obj} already in db")
            self.session.rollback()
