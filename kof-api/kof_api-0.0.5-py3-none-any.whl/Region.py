from kof_api.City import City

class Region(City):
	def __init__(self, name, currency_type):
		self.funds, self.pop = (0,0)
		self.cities = []
		self.capital = ""
		self.currency_type = currency_type
		super().__init__(name, self.funds, False, self.pop)
		
	def add_city(self, city):
		if city.is_capital:
			self.capital = city.name
			self.cities.append(city)
			print(f"Added {city.name} to {self.name}")
			print(f"{city.name} is now the capital of {self.name}")
		else:
			self.cities.append(city)
			print(f"Added {city.name} to {self.name}")