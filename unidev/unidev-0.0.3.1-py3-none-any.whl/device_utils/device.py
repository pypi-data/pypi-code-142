class Device:
    def __init__(self, **kwargs):
        if vendor := kwargs.get("vendor"):
            self.vendor = vendor
        if model := kwargs.get("model"):
            self.model = model
        if port_num := kwargs.get("port_num"):
            self.port_num = port_num

        self.params = {}
        self.procedure_list = {}

        if address := kwargs.get("address"):
            self.address = address
        if timeout := kwargs.get("timeout"):
            self.timeout = timeout
        if termination := kwargs.get("termination"):
            self.termination = termination

        if procedure := kwargs.get("procedure_list"):
            self.procedure_list = procedure

        self.connected = False

    def connect(self): ...

