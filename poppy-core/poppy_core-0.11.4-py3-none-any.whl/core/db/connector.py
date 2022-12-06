#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from poppy.core.logger import logger

from functools import wraps
from poppy.core.generic.metaclasses import SingletonManager
from poppy.core.db.database import Database
from poppy.core.db.dry_runner import DryRunner



__all__ = ["Connector"]


class ConnectorNotAvailable(Exception):
    pass


class Connector(object, metaclass=SingletonManager):
    """
    Base class for managing sessions with various databases.
    """
    def __init__(self, name, database=None):
        """
        Init a connector with useful information.
        """
        # store the name of the connector, useful to reference it later
        self.name = name

        # init the session to a None value to see if already in use or not
        self.session = None

        # if a database is given, set it
        if database is not None:
            self.database = database

    @DryRunner.dry_run
    def bind(self):
        """
        To bind the database to the models of the ORM.
        """
        # get the database
        database = self.get_database()

        # and connect
        database.connectDatabase()

        # check the connection is good
        if not database.connected:
            message = "{0} is not connected".format(database)
            logger.error(message)
            raise Exception(message)

        # check that a session is already in use
        if self.session is not None:
            # close the session
            try:
                self.session.close()
            except Exception as e:
                logger.error(e)
                raise e

        # get a scoped session to be synchronized with others
        self.session = self.factory(database)

    def rollback(self):
        """
        Undo what has been done in the current transaction.
        """
        self.session.rollback()

    @DryRunner.dry_run
    def update_database(self):
        """
        Commit all changes for the current session.
        """
        self.session.commit()

    @DryRunner.dry_run
    def flush(self):
        """
        Flush the session, i.e. it transfers python objects to the transaction
        buffer of the database, thus the memory of the session is cleaned up.
        But if an error occurred, the transaction is rolled back.
        """
        self.session.flush()

    @DryRunner.dry_run
    def add(self, obj):
        """
        Add an object into the session. A simple wrapper around the session.
        """
        # add the object into the shared session
        self.session.add(obj)

    def factory(self, database):
        """
        Given the database, return the session factory.
        """
        return database.session_factory()

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, database):
        # store database in use
        self._database = database

    def get_database(self):
        """
        Return the database object.
        """
        return Database.manager[self._database]

    @classmethod
    def if_connected(cls, *args):
        """
        A decorator to execute a function or method only if the database named
        name is connected.
        """
        def decorator(func):
            """
            Return the function that will be used to decorate.
            """
            @wraps(func)
            def wrapper(*fargs, **kwargs):
                """
                The function that will check the connection and run the wrapped
                function if the database is available.
                """
                # loop over names
                for name in args:
                    # get the connector instance from the given name
                    if name not in cls.manager:
                        message = "Connector {0} not available".format(name)
                        logger.error(message)
                        raise ConnectorNotAvailable(message)

                    # get the connector
                    connector = cls.manager[name]

                    # get the database
                    database = connector.get_database()

                    # check the connection
                    if not database.is_available_with_error():
                        message = "No connection for {0}".format(database)
                        return None

                # run the wrapped function as usual
                return func(*fargs, **kwargs)

            return wrapper

        return decorator

    def __repr__(self):
        """
        A better representation of a connector.
        """
        return "Connector {0}".format(self.name)

