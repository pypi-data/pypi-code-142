from urllib.parse import urlparse

def get_domain(url):
    return urlparse(url).netloc
def get_full_domain(url):
    parsed_url = urlparse(url)
    return parsed_url[0] + '://' + parsed_url[1]
def is_absolute(url):
    return bool(urlparse(url).netloc)    