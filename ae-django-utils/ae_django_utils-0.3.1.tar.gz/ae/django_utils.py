"""
helpers for django projects
===========================

this module is providing helper functions for your django projects.

"""
from urllib.parse import urlparse, urlunparse

from django.utils.translation import get_language       # type: ignore


__version__ = '0.3.1'


def generic_language(lang_code: str) -> str:
    """ remove the country specific part - if exists - from the passed language code.

    :param lang_code:           lower-case language code with optional hyphen and country specific part.
    :return:                    stripped/short language code (e.g. return "en" if lang_code == "en-gb")
    """
    return lang_code.split('-')[0]


def requested_language() -> str:
    """ determine the currently requested short translation language code, fallback to english/'en' if unset.

    :return:                    short (without country specific part) and lower-case language code
    """
    lang_code = get_language() or 'en'
    return generic_language(lang_code)


def set_url_part(url: str, fragment: str = "", query: str = "", **set_part_values) -> str:
    """ add or replace fragment and/or query string of url.

    :param url:                 url to complete by adding and/or updating parts of it.
    :param fragment:            id of the fragment to add/replace.
    :param query:               query string to add/replace.
    :param set_part_values:     other parts like 'scheme', 'netloc', 'path', 'params' (see :func:urllib.parse.urlparse).
    :return:                    url with added/replaced parts.
    """
    if query:
        set_part_values['query'] = query
    if fragment:
        set_part_values['fragment'] = fragment

    if set_part_values:
        url_parts = urlparse(url)
        # noinspection PyProtectedMember
        url_parts = url_parts._replace(**set_part_values)
        url = urlunparse(url_parts)

    return url
