def get_characters(self, params=None):
    url = f"{self._base_url}/character"
    characters = self._get(url, params)
    return characters

def get_character(self, id):
    url = f"{self._base_url}/character/{id}"
    character = self._get(url)
    return character[0]
