from kof_api.Chestplate import Chestplate

from kof_api.Math import Math

math = Math()

class LoricaHamata(Chestplate):
	def __init__(self):
		self.name = "Lorica Hamata"
		self.defense = 1.7
		self.weight = math.convert_kg_lb(11)
		self.desc = "is a type of mail armor used by soldiers."
		
		super().__init__(self.name, self.defense, self.weight)