from kof_api.Item import Item

class Shield(Item):
	def __init__(self, name, defense, weight):
		self.name = name
		self.type = "lhand"
		self.atk, self.defense = (0, defense)
		
		super().__init__(self.name, self.type, self.atk, self.defense, weight)