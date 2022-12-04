from kof_api.Shield import Shield
from kof_api.Math import Math

math = Math()

class LegionaryScutum(Shield):
	def __init__(self):
		self.name = "Legionary Scutum"
		self.defense = 6
		self.weight = math.convert_kg_lb(10)
		self.desc = "curved rectangular shields carried by Legionaries ('Roman Citizens')"
		
		super().__init__(self.name, self.defense, self.weight)