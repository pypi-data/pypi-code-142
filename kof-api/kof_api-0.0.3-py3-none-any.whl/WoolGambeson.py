from game_objects.Items.Chestplate import Chestplate

from game_objects.Utils.Math import Math

math = Math()

class WoolGambeson(Chestplate):
	def __init__(self):
		self.name = "Wool Gambeson"
		self.defense = .5
		self.weight = math.convert_kg_lb(3)
		self.desc = "Heavily padded canvas armor."
		super().__init__(self.name, self.defense, self.weight)