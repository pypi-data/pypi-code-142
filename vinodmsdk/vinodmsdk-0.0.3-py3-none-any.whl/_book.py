def get_books(self, params=None):
    url = f"{self._base_url}/book"
    books = self._get(url, params)
    return books

def get_book(self, id):
    url = f"{self._base_url}/book/{id}"
    book = self._get(url)
    return book[0]
