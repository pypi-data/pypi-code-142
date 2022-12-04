# -*- coding: utf-8 -*-
"""Get Unsplash Source's URL of a photo without the Official Unsplash API.

Attributes:
    scheme (str): Unsplash scheme.
    domain (str): Unsplash domain.
    status (str): Unsplash API Status URL.
    changelog (str): Unsplash API Changelog URL.
"""

from typing import Optional
import re

scheme = 'https'

domain = 'unsplash.com'

status = f'{scheme}://status.{domain}'

changelog = f'{scheme}://changelog.{domain}'

_unsplash = f'{scheme}://{domain}'

_unsplash_source = f'{scheme}://source.{domain}'

_registry = {
    'photo': {
        'unsplash': '/photos/{id}',
        'unsplash source': '/{id}',
    },
    'user': {
        'unsplash': '/@{id}',
        'unsplash source': '/user/{id}',
    },
    'collection': {
        'unsplash': '/collections/{id}/{name}',
        'unsplash source': '/collection/{id}',
    },
}


def _vprint(verbose, *args, **kwargs):
    """Verbose printer."""
    if verbose:
        print(*args, **kwargs)


def _count(*args):
    """Count the number of arguments that are not null."""
    return sum([arg is not None for arg in args])


def _url(link):
    """URL validator."""
    return scheme in link or domain in link


def id(link: str, verbose: bool = False) -> str:
    """Get the identifier given Unsplash share link URL.

    Get the ID of a photo
    ```
    https://unsplash.com/photos/{id}
    ```

    Get the username of a user
    ```
    https://unsplash.com/@{id}
    ```

    Get the ID of a collection
    ```
    https://unsplash.com/collections/{id}/{name}
    ```

    Args:
        link (str): Unsplash share link URL of a photo, a user, or a collection.
        verbose (bool): Whether to enable verbose output. Defaults to `False`.

    Returns:
        (str): The identifier, that can be the ID of a photo, the username of
    a user, or the ID of a collection.
    """
    for k, v in _registry.items():
        pattern = _unsplash + v['unsplash']
        pattern = pattern.replace('{id}', '(\S+)').replace('{name}', '\S+')
        matches = re.findall(pattern, link)
        if matches:
            _vprint(
                verbose,
                f'get the identifier given Unsplash share link URL of a {k}')
            return matches[0]
    raise ValueError(f"'{link}' is an invalid Unsplash share link URL")


def _identify(*args):
    """Identify the identifiers."""
    identifiers = []
    for arg in args:
        if arg is None:
            identifiers.append(arg)
        elif _url(arg):
            identifiers.append(id(arg))
        else:
            identifiers.append(arg)
    return tuple(identifiers)


def source(
    photo: Optional[str] = None,
    user: Optional[str] = None,
    liked: Optional[bool] = None,
    collection: Optional[str] = None,
    featured: Optional[bool] = None,
    resolution: Optional[str] = None,
    update: Optional[str] = None,
    query: Optional[str] = None,
    verbose: bool = False,
) -> str:
    """Get Unsplash Source download link URL of a photo given the parameters.

    Get a random photo
    ```
    https://source.unsplash.com/random
    ```
    Optionally, limit to a featured selection
    ```
    https://source.unsplash.com/featured
    ```
    Optionally, specify a size
    ```
    https://source.unsplash.com/{resolution}
    ```
    Optionally, limit to only updaing daily or weekly
    ```
    https://source.unsplash.com/{update}
    ```
    Optionally, limit to matching search terms
    ```
    https://source.unsplash.com/random?{query}
    ```
    Optionally, narrow the selection further
    ```
    https://source.unsplash.com/featured/{resolution}/{update}?{query}
    ```

    Get a photo
    ```
    https://source.unsplash.com/{id}
    ```
    Optionally, specify a size
    ```
    https://source.unsplash.com/{id}/{resolution}
    ```

    Get a random photo from a user's photos
    ```
    https://source.unsplash.com/user/{id}
    ```
    Optionally, narrow the selection further
    ```
    https://source.unsplash.com/user/{id}/featured/{resolution}/{update}
    ```

    Get a random photo from a user's liked photos
    ```
    https://source.unsplash.com/user/{id}/likes
    ```
    Optionally, specify a size
    ```
    https://source.unsplash.com/user/{id}/likes/{resolution}
    ```

    Get a random photo from a collection's photos
    ```
    https://source.unsplash.com/collection/{id}
    ```
    Optionally, narrow the selection further
    ```
    https://source.unsplash.com/collection/{id}/{resolution}/{update}
    ```

    Note:
        Unsplash Source is being deprecated. Existing uses will continue to
    work, however for new projects use the full Unsplash API.

    Args:
        photo (str): Unsplash share link URL or the ID of a photo.
        user (str): Unsplash share link URL or the username of a user.
        liked (bool): Whether to limit to a user's liked photos. Defaults to
    `False`.
        collection (str): Unsplash share link URL or the ID of a collection.
        featured (bool): Whether to limit to a featured selection. Defaults to
    `False`.
        resolution (str): The size of a photo to be set. Formats to
    `{width}x{height}`. Defaults to `None`.
        update (str): Whether to limit to only updating daily or weekly.
    Defaults to `False`.
        query (str): Comma-separated search terms. Defaults to `None`.
        verbose (bool): Whether to enable verbose output. Defaults to `False`.

    Returns:
        (str): Unsplash Source download link URL of a photo.

    Reference:
        [1] https://changelog.unsplash.com/deprecations/2021/11/25/source-deprecation.html
    """
    link = _unsplash_source
    allow_featured = True
    allow_resolution = True
    allow_update = True
    allow_query = True
    if _count(photo, user, collection) > 1:
        raise ValueError()
    elif _count(photo, user, collection) == 0:
        _vprint(verbose, 'get a random photo')
    else:
        allow_query = False
    photo, user, collection = _identify(photo, user, collection)
    if photo is not None:
        link += f'/{photo}'
        _vprint(verbose, 'get a photo')
        allow_featured = False
        allow_update = False
    if user is not None:
        link += f'/user/{user}'
        if liked:
            link += '/likes'
            _vprint(verbose, "get a random photo from a user's liked photos")
            allow_featured = False
            allow_update = False
        else:
            _vprint(verbose, "get a random photo from a user's photos")
    if collection is not None:
        link += f'/collection/{collection}'
        _vprint(verbose, "get a random photo from a collection's photos")
        allow_featured = False
    if allow_featured and featured:
        link += '/featured'
        _vprint(verbose, "optionally, limit to a featured selection")
    if allow_resolution and resolution is not None:
        link += f'/{resolution}'
        _vprint(verbose, 'optionally, specify a size')
    if allow_update and update is not None:
        if update not in ('daily', 'weekly'):
            raise ValueError(f'{update} updating is not supported')
        link += f'/{update}'
        _vprint(verbose, f'optionally, limit to only updaing {update}')
    if link == _unsplash_source:
        link += '/random'
    if allow_query and query is not None:
        link += f'?{query}'
        _vprint(verbose, 'optionally, limit to matching search terms')
    return link
