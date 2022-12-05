def get_quotes(self, params=None):
    url = f"{self._base_url}/quote"
    quotes = self._get(url, params)
    return quotes

def get_quote(self, id):
    url = f"{self._base_url}/quote/{id}"
    quote = self._get(url)
    return quote[0]

def get_movie_quotes(self, id, params=None):
    url = f"{self._base_url}/movie/{id}/quote"
    quotes = self._get(url, params)
    return quotes

def get_character_quotes(self, id, params=None):
    url = f"{self._base_url}/character/{id}/quote"
    quotes = self._get(url, params)
    return quotes
