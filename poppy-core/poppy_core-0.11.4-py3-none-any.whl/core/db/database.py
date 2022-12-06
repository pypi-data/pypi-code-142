#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote_plus

from poppy.core.logger import logger

from contextlib import contextmanager

from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import DisconnectionError
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.exc import NoSuchTableError
from sqlalchemy.engine.url import make_url
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.pool import Pool
from sqlalchemy import event
from functools import wraps
from copy import copy
from poppy.core.tools.exceptions import print_exception
from poppy.core.generic.metaclasses import ManagerMeta
from poppy.core.generic.cache import CachedProperty
from poppy.core.generic.manager import Manager
from poppy.core.generic.signals import Signal

__all__ = ['Database', 'DatabaseException']


@event.listens_for(Pool, 'checkout')
def ping_connection(dbapi_connection, connection_record, connection_proxy):
    """
    This is for handling the case of a closed connection for the MySQL
    database, only happening with the AIT and maybe CNES database. This is
    making me crazy, since all standard for session handling in SQLAlchemy seem
    to be respected. This is clearly an hack, whose the problem must be solved
    in a better way.
    """
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute('SELECT 1')
    except:
        # optional - dispose the whole pool
        # instead of invalidating one at a time
        # connection_proxy._pool.dispose()

        # raise DisconnectionError - pool will try
        # connecting again up to three times before raising.
        logger.warning('Connection error, trying again')
        raise DisconnectionError()
    cursor.close()


class DatabaseException(Exception):
    pass


class BaseManager(Manager):
    """
    Special manager for the bases of mapping classes for tables in sqlachemy in
    order to not have problems of 'race conditions' for the creation of the
    first base, if used in several plugins, modules.
    """

    def get(self, name):
        """
        Add a base class with name if not already in the manager, else create a
        base and add it to the manager. The base will be shared across modules
        once we want to get it.
        """
        # if present return it
        if name in self.availables:
            return self.availables[name]

        # else create it and add it
        Base = declarative_base()
        self.add(name, Base)

        return Base


class DatabaseMeta(ManagerMeta):
    """
    Override some behaviour of the manager metaclass to add specific ones.
    """

    def __init__(cls, name, bases, attr):
        # init the class as usual
        super(ManagerMeta, cls).__init__(name, bases, attr)

        # add a manager of the connectors
        if not hasattr(cls, 'manager'):
            # manager for database instances
            cls.manager = Manager()

            # also a manager for bases for sqlalchemy
            cls.bases_manager = BaseManager()


class Database(Signal, metaclass=DatabaseMeta):
    """
    A class to manage the connection status to the database and inform all the
    other controllers connected to this class that the connection appeared or
    is gone.
    """

    def __init__(self, name, *args, **kwargs):
        super(Database, self).__init__(*args, **kwargs)

        # set the name
        self.name = name

        # a configuration parameter
        self.binded = False

        # keep the session of the database
        self.session_factory = sessionmaker()

    def connectDatabase(self):
        """
        To make a connection to the database through SQLAlchemy with the
        parameters in the configuration file.
        """
        # check if the database is available
        connected = self.is_available()

        # emit the signal that the database is connected or not, only if change
        if not hasattr(self, 'connected') or self.connected is not connected:
            # set the new status
            self.connected = connected

            # make the connections of the database if necessary (reflections,
            # etc)
            self.makeConnections(connected)

            # send the signal with the new status of the database
            self(connected)

    def connectDatabaseAdmin(self):
        """
        To make a connection to the database through SQLAlchemy with the
        parameters in the configuration file.
        """
        # check if the database is available
        connected = self.is_available()

        # emit the signal that the database is connected or not, only if change
        if not hasattr(self, 'connected') or self.connected is not connected:
            # set the new status
            self.connected = connected

            # make the connections of the database if necessary (reflections,
            # etc)
            self.makeConnectionsAdmin(connected)

            # send the signal with the new status of the database
            self(connected)

    def makeConnections(self, connected):
        """
        To make the appropriate connections to the database.
        """
        if connected:
            if not self.binded:
                # create the engine of the database, since it is the first time
                # that we have a connection to it
                self.create_engine()

                # reflect the database
                self.reflect()

                # configure the session
                self.configure()

                # store the database connection
                self.create_connection()

                # indicate binded
                self.binded = True

    def makeConnectionsAdmin(self, connected):
        """
        To make the appropriate connections to the database.
        """
        if connected:
            if not self.binded:
                # create the engine of the database, since it is the first time
                # that we have a connection to it
                self.create_engine(admin=True)

                # reflect the database
                self.reflect()

                # configure the session
                self.configure()

                # indicate binded
                self.binded = True

    def unbind(self):
        """
        To indicate that the database is no more binded, allowing to rebind it
        to a new engine.
        """
        self.binded = False

    def configure(self):
        """
        To bind the session to the engine.
        """
        # configure a session
        self.session_factory.configure(bind=self.engine)

    def reflect(self):
        """
        To make the reflection of model classes to the database for the current
        engine, in order to be able to use those classes instances as
        representation of databases.
        """
        # bind the engine to the base class for declarative in order to
        # be able to autoload the structure of the tables directly from
        # the database
        try:
            DeferredReflection.prepare(self.engine)
        except NoSuchTableError as e:
            logger.warning(f'The table {e} does not exist')


    def is_available(self):
        """
        From the package sqlalchemy-utils to check if the database exists, i.e.
        is connected or not.
        """
        # regenerate the url if not already done
        url = self.generate_url()

        # create an url
        url = copy(make_url(url))
        text = 'SELECT 1'
        try:
            # logger.debug("Checking connection to {0}".format(self))
            engine = create_engine(url)
            result = engine.execute(text)
            result.close()
            engine.dispose()
            return True

        except (ProgrammingError, OperationalError):
            logger.exception('Connection error with {0}'.format(self))
            return False

    def is_available_with_error(self):
        # regenerate the url if not already done
        url = self.generate_url()

        # create an url
        url = copy(make_url(url))
        text = 'SELECT 1'
        try:
            # logger.debug("Checking connection to {0}".format(self))
            engine = create_engine(url)
            result = engine.execute(text)
            result.close()
            engine.dispose()
            return True

        except (ProgrammingError, OperationalError) as e:
            logger.error('{0}'.format(e))
            return False

    def generate_url(self):
        """
        Generate the URL of the database from the parameters.
        """

        vendor = self.parameters.get('vendor', None)

        if vendor == 'sqlite':
            return '{vendor}:///{address}'.format(
                **self.parameters
            )
        else:
            # Make sure that special characters are well passed in URL
            user, password = self.parameters['user'].split(':')
            port = self.parameters.get('port', None)
            if port:
                address = self.parameters['address'] + ':' + port
            else:
                address = self.parameters['address']
            return '{0}://{1}@{2}/{3}'.format(
                vendor, quote_plus(user) + ':' + quote_plus(password),
                address, self.parameters['database']
            )

    def generate_url_admin(self):
        """
        Generate the URL of the database from the parameters, using database
        admin
        """
        if 'admin' not in self.parameters:
            raise KeyError('You need admin credentials to use admin functions')

        vendor = self.parameters.get('vendor', None)

        if vendor == 'sqlite':
            return '{vendor}:///{address}'.format(
                **self.parameters
            )
        else:
            # Make sure that special characters are well passed in URL
            admin, password = self.parameters['admin'].split(':')
            port = self.parameters.get('port', None)
            if port:
                address = self.parameters['address'] + ':' + port
            else:
                address = self.parameters['address']
            return '{0}://{1}@{2}/{3}'.format(
                vendor, quote_plus(admin) + ':' + quote_plus(password),
                address, self.parameters['database']
            )


    @classmethod
    def connection(cls, name):
        """
        A decorator in order to provide a wrapper connector to a given
        database, not polluting too much the code with redundant instructions.
        """

        # create a decorator to connect to the database with the given name
        def decorator(func):
            # the wrapper function
            @wraps(func)
            def wrapper(*args, **kwargs):
                # get the database in argument
                if name not in cls.manager:
                    message = "Database {0} doesn't exist".format(name)
                    logger.error(message)
                    raise DatabaseException(message)
                database = cls.manager[name]

                # make the connection to the database if not already done
                database.connectDatabase()

                # call the function as usual
                func(*args, **kwargs)

            return wrapper

        return decorator

    @classmethod
    def is_connected(cls, name):
        """
        Decorator to ensure that a connection exists before running the it.
        """

        # create a decorator to connect to the database with the given name
        def decorator(func):
            # the wrapper function
            @wraps(func)
            def wrapper(*args, **kwargs):
                # get the database in argument
                if name not in cls.manager:
                    message = "Database {0} doesn't exist".format(name)
                    logger.error(message)
                    raise DatabaseException(message)
                database = cls.manager[name]

                # check the connection to the database
                if database.is_available():
                    # call the function as usual
                    func(*args, **kwargs)
                else:
                    message = 'Database {0} is not connected'.format(database)
                    logger.error(message)
                    raise DatabaseException(message)

            return wrapper

        return decorator

    def create_connection(self):
        no_engine_exception = DatabaseException('You have to instantiate an engine before you can establish a '
                                                'connection')

        if hasattr(self, 'engine'):
            if self.engine:
                self.db_connection = self.engine.connect()
            else:
                raise no_engine_exception
        else:
            raise no_engine_exception

    def create_engine(self, admin=False):
        """
        Create the engine associated to the url of this database.
        """
        if admin:
            url = self.generate_url_admin()
        else:
            url = self.generate_url()

        self.engine = create_engine(url)

        return self.engine

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        self._parameters = parameters

    @CachedProperty
    def scoped_session(self):
        """
        Return a scoped session. This a simply a register for sessions that
        return always the same session if we want to make one. Allows to not
        transfer the session object across the code, simply using it as a
        singleton.
        """
        # check that a session_factory is created
        if hasattr(self, 'session_factory'):
            # not already scoped, create a scoped session
            return scoped_session(self.session_factory)
        else:
            logger.error(
                'Trying to create a scoped session on an not existing ' +
                'session. Have you created the database?'
            )
            return None

    @contextmanager
    def query_context(self):
        """
        A context manager to create a session for a query and be able to close
        correctly the session when finished, errors, etc.
        """
        # get a session
        session = self.session_factory()

        # return the session and do stuff in the context with it to query
        # information
        try:
            yield session
        except:
            print_exception()
            raise DatabaseException(
                'Error in query context of {0}'.format(self)
            )
        finally:
            session.close()

    def __repr__(self):
        return 'Database {0}'.format(self.name)
