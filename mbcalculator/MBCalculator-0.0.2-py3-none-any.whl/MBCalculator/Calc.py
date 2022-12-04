class Calc():

    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        self.result = a + b
        return self.result
    
    def sub(self, a, b):
        self.result = a - b
        return self.result
    
    def mul(self, a, b):
        self.result = a * b
        return self.result
    
    def div(self, a, b):
        self.result = a / b
        return self.result
    
    def remainder(self, a, b):
        self.result = a % b
        return self.result
   
        