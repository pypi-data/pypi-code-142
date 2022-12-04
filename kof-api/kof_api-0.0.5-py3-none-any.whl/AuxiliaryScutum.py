from kof_api.Shield import Shield

from kof_api.Math import Math

math = Math()

class AuxiliaryScutum(Shield):
	def __init__(self):
		self.name = "Auxiliary Scutum"
		self.defense = 5.7
		self.weight = math.convert_kg_lb(6)
		self.description = "oval shaped shields used by Auixilary Roman Soldiers ('Non Roman Citizens')"
		
		super().__init__(self.name, self.defense, self.weight)