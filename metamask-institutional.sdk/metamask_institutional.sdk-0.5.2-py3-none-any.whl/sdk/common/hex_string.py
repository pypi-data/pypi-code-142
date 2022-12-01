from pydantic import constr

"""A hexadecimal string of any length."""

HexString = constr(regex="^0x[0-9a-f]+$")
