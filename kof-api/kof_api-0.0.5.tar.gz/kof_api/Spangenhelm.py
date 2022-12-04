from kof_api.Helmet import Helmet

from kof_api.Math import Math

math = Math()

class Spangenhelm(Helmet):
	def __init__(self):
		self.name = "Spangenhelm"
		self.defense = .5
		self.img = ''
		self.weight = math.convert_kg_lb(3)
		super().__init__(self.name, self.defense, self.weight)