from game_objects.Items.Chestplate import Chestplate

from game_objects.Utils.Math import Math

math = Math()

class Hauberk(Chestplate):
	def __init__(self):
		self.name = "Hauberk"
		self.defense = 1.5
		self.weight = math.convert_kg_lb(10)
		self.desc = "Very finely made shirt made from thin interloping rings of metal that could be worn just as a metal shirt, or interwoven into a tunic."
		super().__init__(self.name, self.defense, self.weight)