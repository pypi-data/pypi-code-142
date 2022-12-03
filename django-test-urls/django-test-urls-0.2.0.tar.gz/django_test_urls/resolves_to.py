#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" Contains functionality to test the mapping of URLs to views and parameters.

:copyright: (c) 2022 by Alan Verresen
:license: MIT, see LICENSE for more details.
"""

# DEV NOTE:
# ----------------------------------------------------------------------------
# It is important to be aware of the following (seemingly arbitrary) aspects
# of URL dispatching in Django:
#
# - if unnamed regex groups are used in addition to named regex groups,
#   then the values captured by unnamed regex groups are dropped by Django
# - key-value pairs captured by named regex groups will be overwritten by
#   key-value pairs with the same key specified as extra arguments
# - extra arguments can be used in addition to unnamed regex groups, and in
#   this case only, both `args` and `kwargs` will have values
#
# Django dropping values captured by unnamed regex groups
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For example, the following URL pattern contains two unnamed regex groups
# used for the year and the month, and one named regex group for the slug.
#
#   ^([0-9]{4})/(0[1-9]|1[0-2])/(?P<slug>[\w-]+)$
#
# The path `/2020/03/hello-world` would match the pattern above, but only the
# named value "hello-world" will be captured by Django.
#
#   found = resolve_url("/2020/03/hello-world")
#   found.args == ()
#   found.kwargs == {"slug": "hello-world"}
#
# For more information, check out the link below:
# https://docs.djangoproject.com/en/dev/topics/http/urls/#using-unnamed-regular-expression-groups

from django.urls import resolve as resolve_url
from django.urls.exceptions import Resolver404

from .exceptions import InvalidArgumentType


def resolves_to(url, expected_view, expected_args, expected_kwargs):
    """ Checks whether URL is resolved to the expected view and arguments.

    Note that Django does not capture unnamed arguments when mixing named and
    unnamed arguments in a URL pattern.

    :param str url: URL being mapped to a view and arguments
    :param function expected_view: expected view
    :param tuple|list expected_args: expected positional arguments
    :param dict expected_kwargs: expected keyword arguments
    :rtype: bool
    :return: Is the URL mapped to a view and arguments as expected?
    :raises InvalidArgumentType: args or kwargs expressed using invalid type
    """
    return resolves_to_view(url, expected_view) and \
        resolves_to_arguments(url, expected_args, expected_kwargs)


def resolves_to_view(url, expected_view):
    """ Checks whether URL is resolved to the expected view.

    :param str url: URL being mapped to a view
    :param function expected_view: expected view
    :rtype: bool
    :return: Is the URL mapped to a view as expected?
    """
    try:
        found = resolve_url(url)
    except Resolver404:
        return False
    return found.func == expected_view


def resolves_to_arguments(url, expected_args, expected_kwargs):
    """ Checks whether URL is resolved to the expected arguments.

    Note that Django does not capture unnamed arguments when mixing named and
    unnamed arguments in a URL pattern.

    :param str url: URL being mapped to arguments
    :param tuple|list expected_args: expected positional arguments
    :param dict expected_kwargs: expected keyword arguments
    :rtype: bool
    :return: Is the URL mapped to arguments as expected?
    :raises InvalidArgumentType: arguments expressed using invalid type
    """
    if not isinstance(expected_args, (tuple, list)):
        raise InvalidArgumentType()
    if not isinstance(expected_kwargs, dict):
        raise InvalidArgumentType()

    if isinstance(expected_args, list):
        expected_args = tuple(expected_args)

    try:
        found = resolve_url(url)
    except Resolver404:
        return False

    return expected_args == found.args and expected_kwargs == found.kwargs


def resolves_to_404(url):
    """ Checks whether URL couldn't be mapped to a view, resulting in a 404.

    :param str url: URL being mapped to a view and arguments
    :rtype: bool
    :return: Is URL resolved to a 404?
    """
    try:
        _ = resolve_url(url)
        return False
    except Resolver404:
        return True
