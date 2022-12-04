from game_objects.Items.Helmet import Helmet

from game_objects.Utils.Math import Math

math = Math()

class Spangenhelm(Helmet):
	def __init__(self):
		self.name = "Spangenhelm"
		self.defense = .5
		self.img = ''
		self.weight = math.convert_kg_lb(3)
		super().__init__(self.name, self.defense, self.weight)