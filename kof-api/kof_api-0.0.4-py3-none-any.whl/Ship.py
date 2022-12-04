class Ship:
	def __init__(self, name, type, desc, max_cap, max_crew):
		self.name = name
		self.type = type
		self.desc = desc
		self.capacity, self.max_capacity = (0, max_cap)
		self.crew, self.max_crew = (0, max_crew)
		
		self.inv = []
		
	def add_inv(self, item):
		if self.capacity < self.max_capacity:
			self.inv.append(item)
			self.capacity = self.capacity + item.weight
			cap =  self.max_capacity - self.capacity
			print(f"""Added {item.name} to Ship's Inventory!
		
Available Space: {cap}
		
		""")
		else:
			print(f"{self.name} has no free Inventory space Available!")
			
	def remove_inv(self, item):
		for obj in self.inv:
			if obj.name == item.name:
				self.inv.pop(self.inv.index(obj))
				print(f"Removed {item.name} from {self.name}'s Inventory!")
				break
			elif obj.name != item.name:
				print(f"{item.name} is not in {self.name}'s Inventory")
		