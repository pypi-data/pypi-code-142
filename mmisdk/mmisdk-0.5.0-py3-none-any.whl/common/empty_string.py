from pydantic import constr

"""
Pydantic field constraint, that matches only the empty string.
Typically combined with an other constraint, under a union like so:

Union[HexString, EmptyString]: Would match either a hexadecimal string, or the empty string.
"""

EmptyString = constr(regex=".?")
