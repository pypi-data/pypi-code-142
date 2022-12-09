import os
import re

from typing import Union


ALLOWED_EMAILS = [
    'gmail.com',
    'yahoo.com',
    'hotmail.com',
    'aol.com',
    'hotmail.co.uk',
    'hotmail.fr',
    'msn.com',
    'wanadoo.fr',
    'live.com',
    'hotmail.it',
    'qq.com'
]


# Check

def check_domain(domain: str):
    """Check domain ping."""

    domain = re.sub(r'[;|&\-\s​]', '', domain)
    return os.system(f'ping -c 1 -s 8 {domain}') == 0


def check_email(email: str):
    """Check email format and ping the domain."""

    if re.match(r'.*[+\-*/\\;&|\s​].*', email):
        return False

    domain = email.split('@')[-1].lower()

    if domain.lower() in ALLOWED_EMAILS:
        return True

    return check_domain(domain)


def isint_or_digit(text: Union[int, str]):
    """Check if the value is int or isdigit."""

    return isint(text) or (isstr(text) and text.isdigit())


def isbytes(*args):
    """Determine whether it is bytes."""

    return all([isinstance(arg, bytes) for arg in args])


def isdict(*args):
    """Determine whether it is dict."""

    return all([isinstance(arg, dict) for arg in args])


def isfile(*args):
    """Determine whether it is file."""

    return all([os.path.isfile(arg) for arg in args])


def isint(*args):
    """Determine whether it is int."""

    return all([isinstance(arg, int) for arg in args])


def islist(*args):
    """Determine whether it is list."""

    return all([isinstance(arg, list) for arg in args])


def isstr(*args):
    """Determine whether it is str."""

    return all([isinstance(arg, str) for arg in args])
