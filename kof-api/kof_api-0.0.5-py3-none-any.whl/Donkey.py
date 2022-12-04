from kof_api.Animal import Animal

class Donkey(Animal):
	def __init__(self):
		self.name = "Donkey"
		self.can_carry = True
		self.max_capacity = 125
		self.weight = 400
		self.inv = []
		super().__init__(self.name, self.can_carry, self.weight, self.max_capacity)
		
	def add_inv(self, item):
		self.inv.append(item)
		self.capacity = self.capacity + item.weight
		self.weight = self.weight + self.capacity
		print(f"Added {item.name} to {self.name}'s inventory!")
		
	def remove_inv(self, item):
		for i in self.inv:
			if i.name == item.name:
				self.inv.pop(self.inv.index(i))
				self.capacity = self.capacity - i.weight
				self.weight = 400
				print(f"Removed {item.name} to {self.name}'s inventory!")
			else:
				print(f"{item.name} not found in {self.name}'s Inventory!")
				