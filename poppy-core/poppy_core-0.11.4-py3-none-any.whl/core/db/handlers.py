#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from poppy.core.db.connector import Connector
from poppy.core.db.database import Database
from poppy.core.logger import logger
from poppy.core.tools.imports import import_class
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

__all__ = [
    "load_databases",
    "link_databases",
    "yield_limit",
    "connect_databases",
    "get_or_create",
    "get_or_create_with_info",
    "create", "update_one",
    "get_model_dict",
]


def yield_limit(qry, pk_attr, maxrq=1000):
    """
    Specialized windowed query generator (using LIMIT/OFFSET)

    This recipe is to select through a large number of rows thats too
    large to fetch at once. The technique depends on the primary key
    of the FROM clause being an integer value, and selects items
    using LIMIT.
    """
    firstid = None
    while True:
        q = qry
        if firstid is not None:
            q = qry.filter(pk_attr > firstid)
        rec = None
        for rec in q.order_by(pk_attr).limit(maxrq):
            yield rec
        if rec is None:
            break
        firstid = pk_attr.__get__(rec, pk_attr) if rec else None


def load_databases(databases):
    """
    Load databases according to the information provided in the dictionary in
    argument.
    """
    # loop over parameters in the argument
    for database in databases:
        # create the database
        name = database["identifier"]
        logger.debug("Instantiate the database {0}".format(name))
        db = Database(name)

        # set the base used to reflect the database
        if database["identifier"] in Database.bases_manager.availables:
            db.base = Database.bases_manager.availables[database["identifier"]]
        else:
            logger.info("Base of database {0} isn't registered".format(
                database["identifier"]))
            continue

        # update the parameters used by the database
        db.parameters = database["login_info"]


def link_databases(databases):
    """
    Given a list of databases with their properties in a dictionary, create the
    connectors if not already created.
    """
    # loop over databases
    for database in databases:
        # name of the database
        name = database["identifier"]

        # if the connector is already defined
        if name in Connector.manager:
            logger.debug("Connector {0} already instantiated".format(name))
            return

        # get the class for the connector
        if "connector" in database:
            connector = import_class(database["connector"])
        else:
            connector = Connector

        # create an instance of the connector with the name provided
        instance = connector(name)

        # set the database name for the connector
        instance.database = name


def connect_databases():
    """
    Make a connection and reflection of databases registered.
    """
    # loop over databases instances and make the connection
    for database in Database.manager.instances:
        # connect to the database
        database.connectDatabase()

        # if the database is not connected, display it to the user
        if not database.connected:
            logger.error("{0} is not connected".format(database))


def get_or_create(
    session,
    model,
    create_method="",
    create_method_kwargs=None,
    **kwargs
):
    """
    Simply get an object if already present in the database or create it in the
    other case. See
    http://skien.cc/blog/2014/01/15/sqlalchemy-and-race-conditions-implementing/
    and
    http://skien.cc/blog/2014/02/06/sqlalchemy-and-race-conditions-follow-up/
    for better details on why this function as been upgraded to the provided
    example. Better handling of weird cases in the situation of multiple
    processes using the database at the same time.
    """
    try:
        return session.query(model).filter_by(**kwargs).one()
    except NoResultFound:
        kwargs.update(create_method_kwargs or {})
        created = getattr(model, create_method, model)(**kwargs)
        try:
            session.add(created)
            session.commit()
            return created
        except IntegrityError:
            session.rollback()
            return session.query(model).filter_by(**kwargs).one()


def get_update_or_create(
        session,
        model,
        create_method="",
        update_fields=None,
        **kwargs
):
    """
    Get an object if already present in the database and update it. If not, create it
    """
    try:
        # get the obj instance
        instance = session.query(model).filter_by(**kwargs).one()

        # update it
        for field in update_fields or {}:
            setattr(instance, field, update_fields[field])
        session.commit()
        return instance

    except NoResultFound:
        # create the obj instance
        kwargs.update(update_fields or {})
        created = getattr(model, create_method, model)(**kwargs)
        try:
            session.add(created)
            session.commit()
            return created
        except IntegrityError:
            session.rollback()
            return session.query(model).filter_by(**kwargs).one()

def get_or_create_with_info(
    session,
    model,
    create_method="",
    create_method_kwargs=None,
    **kwargs
):
    """
    Simply get an object if already present in the database or create it in the
    other case. See
    http://skien.cc/blog/2014/01/15/sqlalchemy-and-race-conditions-implementing/
    and
    http://skien.cc/blog/2014/02/06/sqlalchemy-and-race-conditions-follow-up/
    for better details on why this function as been upgraded to the provided
    example. Better handling of weird cases in the situation of multiple
    processes using the database at the same time.
    """
    try:
        return session.query(model).filter_by(**kwargs).one(), False
    except NoResultFound:
        kwargs.update(create_method_kwargs or {})
        created = getattr(model, create_method, model)(**kwargs)
        try:
            session.add(created)
            session.commit()
            return created, True
        except IntegrityError:
            session.rollback()
            return session.query(model).filter_by(**kwargs).one(), False


def create(session, model, **kwargs):
    """
    Simply create an object and add it into the database.
    """
    # create it and add it
    instance = model(**kwargs)
    session.add(instance)
    session.commit()
    return instance


def update_one(
    session,
    model,
    values,
    **kwargs
):
    """Update column values of a single entry in the database."""

    # Check if the entry already exists...
    try:
        entry = session.query(model).filter_by(**kwargs).one()
    except NoResultFound:
        # if not return false
        logger.error("NO ENTRY FOUND IN THE DATABASE FOR ({0})!".format(model))
        raise(NoResultFound)
    except MultipleResultsFound:
        # if multiple entries get the first one
        logger.warning(
            "Multiple entries found in the database ({0})!".format(model))
        entry = session.query(model).filter_by(**kwargs).first()

    # Else update column values for the existing entry
    for col in values.keys():
        exec("entry.{0} = values['{0}']".format(col))

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        return False


def get_model_dict(model, ignore=[]):
    """
    Return dictionary where keywords are the columns of
     the input database table model.

    :param model: database table model
    :param ignore: list of columns to ignore
    :return: dictionary with table column names as keywords (values are empty).
    """
    return dict((column.name, getattr(model, column.name))
                for column in model.__table__.columns if column.name not in ignore)