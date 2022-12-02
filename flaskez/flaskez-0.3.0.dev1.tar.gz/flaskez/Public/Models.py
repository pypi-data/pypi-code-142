_templates = [
    "base"
]


class Page:
    def __init__(self, tpe: str = "base"):
        self._tpe = tpe if tpe in _templates else "base"

    @property
    def tpe(self):
        return self._tpe

    @tpe.setter
    def tpe(self, value):
        self._tpe = value if value in _templates else "base"
