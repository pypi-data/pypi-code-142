def get_movies(self, params=None):
    url = f"{self._base_url}/movie"
    movies = self._get(url, params)
    return movies

def get_movie(self, id):
    url = f"{self._base_url}/movie/{id}"
    movie = self._get(url)
    return movie[0]
