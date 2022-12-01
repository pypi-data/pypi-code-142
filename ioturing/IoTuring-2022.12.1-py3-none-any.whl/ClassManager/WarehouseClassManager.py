from IoTuring.ClassManager.ClassManager import ClassManager
from IoTuring.ClassManager import consts
from IoTuring.Warehouse.Warehouse import Warehouse

class WarehouseClassManager(ClassManager): # Class to load Entities from the Entitties dir and get them from name 
    def __init__(self):
        ClassManager.__init__(self)
        self.baseClass = Warehouse
        self.GetModulesFilename(consts.WAREHOUSES_PATH) 