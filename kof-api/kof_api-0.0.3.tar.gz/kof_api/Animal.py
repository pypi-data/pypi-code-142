class Animal:
	def __init__(self, name, can_carry, weight, max_capacity):
		self.name = name
		self.can_carry = can_carry
		if self.can_carry:
			self.capacity, self.max_capacity = (0, max_capacity)
		else:
			self.capacity, self.max_capacity = (0,0)
		self.weight = weight