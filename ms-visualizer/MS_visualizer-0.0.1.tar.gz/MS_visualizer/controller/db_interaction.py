from MS_visualizer.model.models import *  # Note for Matteo: contents of this file will change depending on Pony, so it's fine.

from datetime import date

import pandas as pd


@db_session
def add_to_db(entity_name: str, dictionary: dict) -> None:
    """Takes a DB Table name and a dictionary and writes the dictionary to the specified Table"""

    table = getattr(db, entity_name)
    table(**dictionary)


def save_to_db(entity_names: list, list_of_dicts: list) -> None:
    """saves multiple dictionaries to the database"""

    if len(entity_names) != len(list_of_dicts):
        raise ValueError("Number of Entities does not match number of dictionaries")

    # iterate over the lists add everything to the database
    for index in range(len(entity_names)):
        add_to_db(entity_names[index], list_of_dicts[index])


def create_save_dict(**kwargs) -> dict:
    return kwargs


def get_attributes(obj, attr):
    if type(attr) == list:
        # if it's a list: get the attributes recursively
        if obj is None:
            return None
        elif len(attr) == 1:
            try:
                return getattr(obj, attr[0])
            except:
                return getattr(obj, 'id')
        else:
            return get_attributes(getattr(obj, attr[0]), attr[1:])
    else:
        # not a list: get the attribute
        return getattr(obj, attr)


@db_session
def general_query(entity_name, query_dict, col='id'):
    table = getattr(db, entity_name)

    query = select(i for i in table).order_by(desc(getattr(table, col)))
    df = pd.DataFrame({key: get_attributes(x, value) for key, value in query_dict.items()} for x in query)

    return df


@db_session
def get_new_id():
    table = db.Evaluation
    try:
        query = select(i for i in table).order_by(table.id)[:][-1]
        return query.id + 1
    except:
        return 1


@db_session
def create_standard_user():
    """ Create a standard user for tests if there is no user"""
    if not User.select().exists():
        db.User(name="Test User", password="123")


@db_session
def get_label_value():
    table = db.Evaluation
    query = select(i for i in table).order_by(table.id)[:]

    return [["{} - Score: {} - {} - {}".format(x.user.name, x.score, x.created.strftime("%d/%m/%Y %H:%M:%S"), x.comment), x.id] for x in query]


@db_session
def get_options():
    if Evaluation.select().exists():
        label = get_label_value()
        options = [{"label": i[0], "value": i[1]} for i in label]

        return options
    else:
        return []


@db_session
def get_label_value_algo():
    table = db.Algorithm
    query = select(i for i in table).order_by(table.id)[:]

    return [["{}".format(x.name), x.id] for x in query]



@db_session
def get_algo_options():
    if Algorithm.select().exists():
        label = get_label_value_algo()
        options = [{"label": i[0], "value": i[1]} for i in label]

        return options
    else:
        return []


@db_session
def get_loaded_value(entity, id_, value):
    table = getattr(db, entity)
    query = select(i for i in table if i.id == id_)[:][-1]
    return getattr(query, value)


@db_session
def get_algorithm(id_, value):
    table = db.Algorithm
    query = select(i for i in table if i.id == id_)[:][-1]
    return getattr(query, value)
