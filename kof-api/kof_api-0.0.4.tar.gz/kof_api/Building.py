class Building:
	def __init__(self, name, is_business, city, region):
		self.name = name
		self.is_business = is_business
		self.city, self.region = (city, region)