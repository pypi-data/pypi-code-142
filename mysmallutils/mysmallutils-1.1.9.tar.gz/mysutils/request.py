from json import dumps, loads
from logging import getLogger
from time import sleep
from typing import Union, Callable

try:
    import requests
    from urllib3.exceptions import MaxRetryError
except ModuleNotFoundError as e:
    raise ModuleNotFoundError('ModuleNotFoundError: No module named \'requests\'. '
                              'Please install it with the command:\n\n'
                              'pip install requests~=2.25.1')

log = getLogger(__name__)
MAX_ATTEMPTS = 3
WAIT = 10


def json_post(host: str, msg: Union[list, dict, str]) -> Union[list, dict, str]:
    """ Makes a http json post.
    :param host: The host.
    :param msg: Object to send to the server.
    """
    res = requests.post(host, dumps(msg), headers={'content-type': 'application/json'})
    if not res.ok:
        raise requests.RequestException(f'Error {res.status_code} connecting with "{host}":'
                                        f'\n{res.content.decode("utf-8")}')
    return loads(res.content)


def trying_get(url, max_attempts: int = MAX_ATTEMPTS, wait: int = WAIT, **kwargs) -> requests.Response:
    """ Makes a get request to an url trying several times if it fails.
    :param url: The URL to request.
    :param max_attempts: The maximum number of attempts to download the video.
    :param wait: The number of seconds to wait between each attempt.
    :param kwargs: The get parameters.
    :return: A http response.
    """
    return _trying_request(requests.get, url, max_attempts, wait, **kwargs)


def trying_post(url, max_attempts: int = MAX_ATTEMPTS, wait: int = WAIT, **kwargs) -> requests.Response:
    """ Makes a post request to an url trying several times if it fails.
    :param url: The URL to request.
    :param max_attempts: The maximum number of attempts to download the video.
    :param wait: The number of seconds to wait between each attempt.
    :param kwargs: The post parameters.
    :return: A http response.
    """
    return _trying_request(requests.post, url, max_attempts, wait, **kwargs)


def trying_delete(url, max_attempts: int = MAX_ATTEMPTS, wait: int = WAIT, **kwargs) -> requests.Response:
    """ Makes a delete request to an url trying several times if it fails.
    :param url: The URL to request.
    :param max_attempts: The maximum number of attempts to download the video.
    :param wait: The number of seconds to wait between each attempt.
    :param kwargs: The delete parameters.
    :return: A http response.
    """
    return _trying_request(requests.delete, url, max_attempts, wait, **kwargs)


def trying_put(url, max_attempts: int = MAX_ATTEMPTS, wait: int = WAIT, **kwargs) -> requests.Response:
    """ Makes a put request to an url trying several times if it fails.
    :param url: The URL to request.
    :param max_attempts: The maximum number of attempts to download the video.
    :param wait: The number of seconds to wait between each attempt.
    :param kwargs: The put parameters.
    :return: A http response.
    """
    return _trying_request(requests.put, url, max_attempts, wait, **kwargs)


def _trying_request(method: Callable, url, max_attempts: int = MAX_ATTEMPTS, wait: int = WAIT, **kwargs) -> requests.Response:
    """ Makes a get request to an url trying several times if it fails.
    :param url: The URL to request.
    :param max_attempts: The maximum number of attempts to download the video.
    :param wait: The number of seconds to wait between each attempt.
    :return: A http response.
    """
    attempts = max_attempts
    while attempts:
        try:
            return method(url, **kwargs)
        except (requests.exceptions.ConnectionError, MaxRetryError) as e:
            attempts -= 1
            log.warning(f'Connection error to "{url}" trying again '
                        f'{max_attempts - attempts} of {max_attempts} after {wait} seconds...')
            if not attempts:
                raise e
            sleep(wait)
