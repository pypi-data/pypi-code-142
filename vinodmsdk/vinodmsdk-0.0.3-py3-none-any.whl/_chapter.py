def get_chapters(self, params=None):
    url = f"{self._base_url}/chapter"
    chapters = self._get(url, params)
    return chapters

def get_chapter(self, id):
    url = f"{self._base_url}/chapter/{id}"
    chapter = self._get(url)
    return chapter[0]

def get_book_chapters(self, id, params=None):
    url = f"{self._base_url}/book/{id}/chapter"
    chapters = self._get(url, params)
    return chapters
