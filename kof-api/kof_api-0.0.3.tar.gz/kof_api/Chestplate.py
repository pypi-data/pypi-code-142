from game_objects.Item import Item

class Chestplate(Item):
	def __init__(self, name, defense, weight):
		self.type = 'torso'
		self.atk, self.defense = (0, defense)
		super().__init__(name, self.type, self.atk, self.defense, weight)