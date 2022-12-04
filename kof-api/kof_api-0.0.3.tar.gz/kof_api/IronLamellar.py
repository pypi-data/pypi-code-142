from game_objects.Items.Chestplate import Chestplate

from game_objects.Utils.Math import Math

math = Math()

class IronLamellar(Chestplate):
	def __init__(self):
		self.name = "Iron Lamellar Chestplate"
		self.defense = 3
		self.weight = math.convert_kg_lb(14)
		self.desc = "Body armour, made from small rectangular plates of  iron laced into horizontal rows."
		
		super().__init__(self.name, self.defense, self.weight)