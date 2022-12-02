class Plum:
    def __init__(self, expression, data) -> None:
        self.expression = expression
        self.data = data

    def plum(self, value):
        if isinstance(self.data, dict):
            if self.expression not in self.data:
                return
        self.data[self.expression] = value

    def peach(self):
        return self.data[self.expression]
