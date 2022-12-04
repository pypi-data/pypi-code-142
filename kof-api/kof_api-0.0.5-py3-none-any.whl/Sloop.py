from kof_api.Ship import Ship

class Sloop(Ship):
	def __init__(self):
		self.name = "Sloop"
		self.type = 'civilian'
		self.desc = ""
		self.max_capacity = 300
		self.max_crew = 25
		
		super().__init__(self.name, self.type, self.desc, self.max_capacity, self.max_crew)