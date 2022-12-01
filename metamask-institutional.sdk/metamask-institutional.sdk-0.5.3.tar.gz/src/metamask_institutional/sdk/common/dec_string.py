from pydantic import constr

"""A decimal number of any length as a string."""

DecString = constr(regex="[0-9a-f]+$")
