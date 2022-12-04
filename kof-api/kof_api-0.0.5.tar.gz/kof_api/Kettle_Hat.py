from kof_api.Helmet import Helmet

from kof_api.Math import Math

math = Math()

class KettleHat(Helmet):
	def __init__(self):
		self.name = "Kettle Hat"
		self.defense = 1.5
		self.img = ''
		self.weight = math.convert_kg_lb(1.9)
		super().__init__(self.name, self.defense, self.weight)
	