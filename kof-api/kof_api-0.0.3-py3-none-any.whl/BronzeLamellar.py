from game_objects.Items.Chestplate import Chestplate
from game_objects.Utils.Math import Math

math = Math()

class BronzeLamellar(Chestplate):
	def __init__(self):
		self.name = "Bronze Lamellar Chestplate"
		self.defense = 2
		self.weight = math.convert_kg_lb(11)
		self.desc = "Body armour, made from small rectangular plates of bronze laced into horizontal rows."
		
		super().__init__(self.name, self.defense, self.weight)