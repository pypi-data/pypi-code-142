import requests


def download_file(filepath, url, **kwargs):
    """
    Download a file from the given URL

    :param filepath: path where the file will be downloaded
    :param url: URL of the file to download
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return:
    """

    response = requests.get(url, **kwargs)

    # if the response was successful, no Exception will be raised
    response.raise_for_status()

    with open(filepath, 'wb') as out_file:
        for chunk in response:
            out_file.write(chunk)
