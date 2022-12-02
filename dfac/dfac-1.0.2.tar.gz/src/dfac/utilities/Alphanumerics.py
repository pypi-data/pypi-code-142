class Alphanumerics:

    def __init__(self) -> None:
        self.lowercase_ascii_start = 97
        self.lowercase_ascii_end = 122
        self.uppercase_ascii_start=65
        self.uppercase_ascii_end=90
        self.ascii_symbols=[[32,47],[91,96],[123,126]]

    def alphalower(self):
        l=[]
        for i in range(self.lowercase_ascii_start,self.lowercase_ascii_end+1):
            l.append(chr(i))
        return l

    def alphaupper(self):
        l=[]
        for i in range(self.uppercase_ascii_start,self.uppercase_ascii_end+1):
            l.append(chr(i))
        return l

    def symbols(self):
        l=[]
        for i in self.ascii_symbols:
            for j in range(i[0],i[1]+1):
                l.append(chr(j))
        return l

    def numeric(self):
        l=[]
        for i in range(10):
            l.append(str(i))
        return l

    




