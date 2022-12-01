class Msg:

    def __init__(self, params, ttl=129):
        self._params = params
        self._ttl = ttl

    def get_params(self):
        self._ttl -= 1
        return self._params

    def set_params(self, params):
        self._params = params

    def ttl(self):
        return self._ttl