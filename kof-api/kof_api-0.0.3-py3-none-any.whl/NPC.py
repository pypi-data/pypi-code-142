class NPC:
	def __init__(self, name, has_quests, is_merchant, product_type, city, region, building, default_currency):
		self.name = name
		self.has_quests = has_quests
		self.quests = []
		self.is_merchant = is_merchant
		self.product_type = product_type
		self.products = {}
		self.city, self.region = (city, region)
		self.building = building
		self.default_currency = default_currency
		
	