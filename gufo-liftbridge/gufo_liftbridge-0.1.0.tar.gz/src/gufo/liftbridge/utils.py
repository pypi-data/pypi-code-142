# ----------------------------------------------------------------------
# Gufo Liftbridge: Various utilities.
# ----------------------------------------------------------------------
# Copyright (C) 2022, Gufo Labs
# See LICENSE.md for details
# ----------------------------------------------------------------------

# Python modules
import socket


def is_ipv4(addr: str) -> bool:
    """
    Check value is valid IPv4 address.

    Args:
        addr: String to check.
    Returns:
        `True`, if is valid IPv4 address. `False` otherwise.
    """
    parts = addr.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(x) <= 255 for x in parts) and bool(
            socket.inet_aton(addr)
        )
    except (ValueError, OSError):
        return False
