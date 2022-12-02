class Cabrillo:
    def __init__(self, file):
        self.file = file
        self.head = [
                "Freq",
                "Mode",
                "Date",
                "Time",
                "MyCall",
                "RSTSent",
                "SerialSent",
                "Call",
                "RSTReceived",
                "SerialReceived"
            ]
        self.decoded_data = {}

    def _init__(self, file, head):
        self.file = file
        self.head = head
        self.decoded_data = {}
    
    def decode_QSO_cabrillo(self, data):
        temp = {}
        buffer = {}
        
        buffer = data.split()  
        
        for index, (value)  in enumerate(self.head):
            temp[value] = buffer[index]
            
        return temp

    def decode(self):
        if (self.file):
            lines = self.file.readlines()
            for line in lines:
                line = line.replace("\n", "")
                d = line.split(':')
                d[1] = d[1].lstrip()
                
                if (len(d) > 1):
                    if (d[0] != "QSO"):
                        self.decoded_data[d[0]] = d[1]
                    elif (d[0] == "QSO"):
                        if (self.decoded_data.get("QSO") == None):
                            self.decoded_data["QSO"] = []
                        
                        # decoded_qso_data = self.decode_QSO_cabrillo(d[1])
                        self.decoded_data["QSO"].append(self.decode_QSO_cabrillo(d[1]))
                
                else:
                    self.decoded_data[d[0]] = ""
            
            return self.decoded_data