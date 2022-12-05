import requests


class LotrException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UnAuthorizedException(LotrException):
    def __init__(self, message="Unauthorized."):
        self.message = message
        super().__init__(self.message)


class Client(object):
    """
    A client for accessing the lotr API.
    """
    def __init__(self, api_key, base_url=None):
        """
        Initializes the sdk client object
        :param api_key: The api_key for authentication
        :param base_url: The url for the API
        """
        self._base_url=base_url or f"https://the-one-api.dev/v2"
        self._api_key=api_key

    def _get(self, url, params=None):
        headers = {'Authorization': f"Bearer {self._api_key}"}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()["docs"]
        elif response.status_code == 401:
            raise UnAuthorizedException()
        else:
            raise LotrException(response.text)

    # Imported methods
    from ._movie import get_movies, get_movie
    from ._book import get_books, get_book
    from ._chapter import get_chapters, get_chapter, get_book_chapters
    from ._character import get_characters, get_character
    from ._quote import get_quotes, get_quote, get_movie_quotes, get_character_quotes

    def get_paginator(self, resource, page_size=1000, sort=None, id=None):
        """
        Creates a paginator object which can be used to iterate over the records
        :param resource: The resource for which the paginator is being created. Valid values are
            "books", "chapters", "book_chapters", "characters", "movies", "quotes", "movie_quotes", "character_quotes"
        :param page_size: The number of records to be retrieved for each iteration. Default is 1000
        :param sort: The sort key and type. e.g sort=name:asc, sort=character:desc. Default is None
        :param id: The id of the resource. id should only be specified when `resource` is one of `book_chapters`, `movie_quotes`, `character_quotes`
        :return: An iterator for the resource being requested

        An LotrException is raised if there are any issues.
        """
        return Client._Paginator(client=self, resource=resource, page_size=page_size, sort=sort, id=id)

    class _Paginator(object):
        def __init__(self, client, resource, page_size=1000, sort=None, id=None):
            self._resource_name = resource
            self._client = client
            self._sort=sort
            self._id=id
            if resource == "chapters":
                self._resource = self._client.get_chapters
            elif resource == "books":
                self._resource = self._client.get_books
            elif resource == "book_chapters":
                self._resource = self._client.get_book_chapters
                if not self._id:
                    raise  LotrException(f'Need a valid id for resource "book_chapters"')
            elif resource == "movies":
                self._resource = self._client.get_movies
            elif resource == "characters":
                self._resource = self._client.get_characters
            elif resource == "quotes":
                self._resource = self._client.get_quotes
            elif resource == "movie_quotes":
                self._resource = self._client.get_movie_quotes
                if not self._id:
                    raise LotrException(f'Need a valid id for resource "movie_quotes"')
            elif resource == "character_quotes":
                self._resource = self._client.get_character_quotes
                if not self._id:
                    raise LotrException(f'Need a valid id for resource "character_quotes"')
            else:
                raise LotrException(f'{resource} is invalid. Resource should be one of "books", "chapters", "book_chapters", "characters", "movies", "quotes", "movie_quotes", "character_quotes" ')
            self._limit = page_size
            self._page = 1

        def __iter__(self):
            return self

        def __next__(self):
            params={"limit":self._limit, "page":self._page}
            if self._sort:
                params["sort"] = self._sort
            if self._resource_name in ("book_chapters", "movie_quotes", "character_quotes"):
                items = self._resource(params=params, id=self._id)
            else:
                items = self._resource(params=params)
            self._page += 1
            if items:
                return items
            else:
                raise StopIteration
