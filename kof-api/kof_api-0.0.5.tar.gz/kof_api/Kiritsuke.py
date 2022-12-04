from kof_api.Chestplate import Chestplate

from kof_api.Math import Math

math = Math()

class Kiritsuke(Chestplate):
	def __init__(self):
		self.name ="Kiritsuke Iyozane"
		self.defense = 6
		self.weight = math.convert_kg_lb(18)
		self.desc = "a form of laminar armour constructed from long strips of leather and iron which were perforated, laced, and notched and made to replicate the look of real lamellar plates."
		
		super().__init__(self.name, self.defense, self.weight)