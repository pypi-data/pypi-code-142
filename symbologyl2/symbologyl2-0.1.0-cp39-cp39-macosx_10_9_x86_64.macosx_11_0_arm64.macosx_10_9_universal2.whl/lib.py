"""
Wrapper lib for `symbologyl2 <https://github.com/onechronos/symbologyl2>`_
"""

from typing import Optional

from symbologyl2 import _symbologyl2


def from_any_to_root(symbol: str) -> str:
    """Extracts the symbol root from an input string in CQS, CMS, or NASDAQ integrated
    symbology format.

    .. testsetup:: *

        import symbologyl2

    .. doctest::

        >>> symbologyl2.from_any_to_root('TEST A')
        'TEST'

    .. doctest::

        >>> symbologyl2.from_any_to_root('TEST.A')
        'TEST'

    Parameters
    ----------
    symbol : str
        The input symbol, in CQS, CMS, or NASDAQ integrated symbology format

    Returns
    -------
    str
        The symbol root
    """
    return _symbologyl2.from_any_to_root(symbol)


def from_any_to_cms(symbol: str) -> str:
    """Returns the given symbol in CMS format.

    .. testsetup:: *

        import symbologyl2

    .. doctest::

        >>> symbologyl2.from_any_to_cms('TEST')
        'TEST'

    .. doctest::

        >>> symbologyl2.from_any_to_cms('TEST A')
        'TEST A'

    .. doctest::

        >>> symbologyl2.from_any_to_cms('TEST.A')
        'TEST A'

    Parameters
    ----------
    symbol : str
        The input symbol, in CQS, CMS, or NASDAQ integrated symbology format

    Returns
    -------
    str
        The original symbol in CMS format
    """
    return _symbologyl2.from_any_to_cms(symbol)


def from_any_to_cqs(symbol: str) -> str:
    """Returns the given symbol in CQS format.

    .. testsetup:: *

        import symbologyl2

    .. doctest::

        >>> symbologyl2.from_any_to_cqs('TEST')
        'TEST'

    .. doctest::

        >>> symbologyl2.from_any_to_cqs('TEST A')
        'TEST.A'

    .. doctest::

        >>> symbologyl2.from_any_to_cqs('TEST.A')
        'TEST.A'

    Parameters
    ----------
    symbol : str
        The input symbol, in CQS, CMS, or NASDAQ integrated symbology format

    Returns
    -------
    str
        The original symbol in CQS format
    """
    return _symbologyl2.from_any_to_cqs(symbol)


def from_any_to_nasdaq_integrated(symbol: str) -> str:
    """Returns the given symbol in Nasdaq integrated format.

    .. testsetup:: *

        import symbologyl2

    .. doctest::

        >>> symbologyl2.from_any_to_nasdaq_integrated('TEST')
        'TEST'

    .. doctest::

        >>> symbologyl2.from_any_to_nasdaq_integrated('TEST A')
        'TEST.A'

    .. doctest::

        >>> symbologyl2.from_any_to_nasdaq_integrated('TEST.A')
        'TEST.A'

    Parameters
    ----------
    symbol : str
        The input symbol, in CQS, CMS, or NASDAQ integrated symbology format

    Returns
    -------
    str
        The original symbol in Nasdaq integrated format
    """
    return _symbologyl2.from_any_to_cqs(symbol)


def from_any_to_cms_suffix(symbol: str) -> Optional[str]:
    """Returns the given symbol suffix (if present) in CMS format, and None otherwise.

    .. testsetup:: *

        import symbologyl2

    .. doctest::

        >>> symbologyl2.from_any_to_cms_suffix('TEST')

    .. doctest::

        >>> symbologyl2.from_any_to_cms_suffix('TEST A')
        'A'

    .. doctest::

        >>> symbologyl2.from_any_to_cms_suffix('TEST.A')
        'A'

    Parameters
    ----------
    symbol : str
        The input symbol, in CQS, CMS, or NASDAQ integrated symbology format

    Returns
    -------
    suffix : str or None
        The suffix in CMS format, or None if there is no suffix.
    """
    return _symbologyl2.from_any_to_cms_suffix(symbol)


def from_any_to_cqs_suffix(symbol: str) -> Optional[str]:
    """Returns the given symbol suffix (if present) in CMS format, and None otherwise.

    .. testsetup:: *

        import symbologyl2

    .. doctest::

        >>> symbologyl2.from_any_to_cqs_suffix('TEST')

    .. doctest::

        >>> symbologyl2.from_any_to_cqs_suffix('TEST A')
        '.A'

    .. doctest::

        >>> symbologyl2.from_any_to_cqs_suffix('TEST.A')
        '.A'

    Parameters
    ----------
    symbol : str
        The input symbol, in CQS, CMS, or NASDAQ integrated symbology format

    Returns
    -------
    suffix : str or None
        The suffix in CQS format, or None if there is no suffix.
    """
    return _symbologyl2.from_any_to_cqs_suffix(symbol)


def from_any_to_nasdaq_suffix(symbol: str) -> Optional[str]:
    """Returns the given symbol suffix (if present) in Nasdaq integrated format, and
    None otherwise.

    .. testsetup:: *

        import symbologyl2

    .. doctest::

        >>> symbologyl2.from_any_to_nasdaq_suffix('TEST')

    .. doctest::

        >>> symbologyl2.from_any_to_nasdaq_suffix('TEST A')
        '.A'

    .. doctest::

        >>> symbologyl2.from_any_to_nasdaq_suffix('TEST.A')
        '.A'

    Parameters
    ----------
    symbol : str
        The input symbol, in CQS, CMS, or NASDAQ integrated symbology format

    Returns
    -------
    suffix : str or None
        The suffix in Nasdaq integrated format, or None if there is no suffix.
    """
    return _symbologyl2.from_any_to_nasdaq_suffix(symbol)
