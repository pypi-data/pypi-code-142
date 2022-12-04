from threading import Thread


class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=None, kwargs=None):
        self._data = kwargs
        super().__init__(group, target, name, args, kwargs)
        self._result = None

    def run(self):
        if self._target:
            self._result = self._target(self._data)

    def join(self):

        super().join()
        return self._result
