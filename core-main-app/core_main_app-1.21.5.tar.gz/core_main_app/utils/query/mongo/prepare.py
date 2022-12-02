"""Mongo query builder tools
"""
import copy
import re

from mongoengine.queryset.visitor import Q

from core_main_app.commons.exceptions import QueryError


def _compile_regex(query):
    """Compile all regular expressions in the query

    Args:
        query:

    Returns:

    """
    for key, value in query.items():
        if key == "$and" or key == "$or":
            for sub_value in value:
                _compile_regex(sub_value)
        elif isinstance(value, str) or isinstance(value, str):
            if len(value) >= 2 and value[0] == "/" and value[-1] == "/":
                query[key] = re.compile(value[1:-1])
        elif isinstance(value, dict):
            _compile_regex(value)


def _add_sub_document_root(query, sub_document_root):
    """Adds a sub document root to each criteria

    Returns:

    """
    for key in list(query.keys()):
        if key == "$and" or key == "$or":
            for value in query[key]:
                _add_sub_document_root(value, sub_document_root)
        elif not key.startswith("$"):
            query["{}.{}".format(sub_document_root, key)] = query.pop(key)


def prepare_query(query_dict, regex=True, sub_document_root=None):
    """Prepares the query to before executing it

    Args:
        query_dict:
        regex:
        sub_document_root:

    Returns:

    """
    # get a copy of the query
    query = copy.deepcopy(query_dict)

    if regex:
        # compile the regular expressions
        _compile_regex(query)

    if sub_document_root is not None:
        # add a sub document root
        _add_sub_document_root(query, sub_document_root)

    return query


def sanitize(query_dict):
    """Sanitize query

    Returns:

    """
    # create a query object
    q_list = Q()

    # create $where operator
    if "$where" in str(query_dict):
        raise QueryError("Unsupported operator found")

    # iterate through query dict key/value pairs
    for key, value in query_dict.items():
        # if the key is not an operator
        if not key.startswith("$"):
            if "$" in key:
                raise QueryError("Unsupported $ operator found")
            # replace dots by double underscores (django notation)
            key = key.replace(".", "__") if "." in key else key
            # initialize operator
            operator = "exact"
            # check if not operator
            if isinstance(value, dict) and "$not" in value:
                # add not to key
                key += "__not"
                # move value to document in $not
                value = value["$not"]
            # if value is a regex
            if isinstance(value, re.Pattern):
                # set regex operator
                operator = "regex"
                # set value with regex pattern
                value = value.pattern
            # if value is None
            elif value is None:
                # mongo: __exact = None / django: __exact = None
                value = None
            # if the value is a dict
            elif isinstance(value, dict):
                # check if ne operator (not equal)
                if "$ne" in value:
                    # set ne operator
                    operator = "ne"
                    # set value
                    value = value["$ne"]
                # check if eq operator (equal to)
                elif "$eq" in value:
                    # set value
                    value = value["$eq"]
                # check if lt operator (less than)
                elif "$lt" in value:
                    # set lt operator
                    operator = "lt"
                    # set value
                    value = sanitize_number(value["$lt"])
                # check if lt operator (less than or equal)
                elif "$lte" in value:
                    # set lte operator
                    operator = "lte"
                    # set value
                    value = sanitize_number(value["$lte"])
                # check if gt operator (greater than)
                elif "$gt" in value:
                    # set gt operator
                    operator = "gt"
                    # set value
                    value = sanitize_number(value["$gt"])
                # check if gte operator (greater than or equal)
                elif "$gte" in value:
                    # set gte operator
                    operator = "gte"
                    # set value
                    value = sanitize_number(value["$gte"])
                # check if in operator (included in list)
                elif "$in" in value:
                    # set in operator
                    operator = "in"
                    # set value
                    value = value["$in"]
                # check if regex operator
                elif "$regex" in value:
                    # set regex operator
                    operator = "regex"
                    # set the value
                    value = value["$regex"]
                # check if exists operator
                elif "$exists" in value:
                    # skip case where set to False for now (i.e. can not look for documents where path is absent)
                    if not value["$exists"]:
                        raise QueryError(
                            'Unsupported operator found: {"$exists": False}'
                        )
                    # set exists operator
                    operator = "exists"
                    value = True
                else:
                    # If an operator not listed above is found, an exception is raised
                    raise QueryError(f"Unsupported operator found: {value}")
            # build query
            query = Q(**{f"{key}__{operator}": sanitize_value(value)})

            # add AND query filter from string key and value
            q_list &= query
        else:
            # if operator and
            if key == "$and":
                # iterate though sub dict
                for sub_value in value:
                    # add AND filters to the query
                    q_list &= sanitize(sub_value)
            # if operator or
            elif key == "$or":
                # iterate through sub dict
                for sub_value in value:
                    # add OR filters to the query
                    q_list |= sanitize(sub_value)
            # if operators text and search found
            elif key == "$text" and "$search" in value:
                # get text query
                text_query = query_dict["$text"]["$search"]
                # check text query is a string
                if not isinstance(text_query, str):
                    raise QueryError(f"Unsupported value found in: {key}")
                # strip white spaces
                text_query = text_query.strip()
                # sanitize string
                sanitize_value(text_query)
                # if data stored in MongoDB
                q_list &= Q(__raw__={"$text": {"$search": text_query}})
            else:
                # raise an error if another operator was found
                raise QueryError(f"Unsupported operator found: {key}")

    return q_list


def sanitize_number(value):
    """Sanitize number


    Args:
        value:

    Returns:

    """
    # check type of value
    if not (isinstance(value, (int, float))):
        raise QueryError("Unsupported value: expected a number.")
    return value


def sanitize_value(value):
    """Sanitize value

    Args:
        value:

    Returns:

    """
    # check if operator in value
    if "$" in str(value):
        raise QueryError("Unsupported $ operator found.")
    # if value is a list
    if isinstance(value, list):
        # check for $ sign in the list
        for item in value:
            sanitize_value(item)
    return value
