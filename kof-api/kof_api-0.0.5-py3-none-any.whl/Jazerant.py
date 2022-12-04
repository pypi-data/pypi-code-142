from kof_api.Chestplate import Chestplate

from kof_api.Math import Math

math = Math()

class Jazerant(Chestplate):
	def __init__(self):
		self.name = "Jazerant"
		self.defense = 1.5
		self.weight = math.convert_kg_lb(9.2)
		self.desc = "Light armor that placed mail armor between the layers of leather or fabric. It was mostly used in Middle East, Persia and Asia."
		
		super().__init__(self.name, self.defense, self.weight)
	