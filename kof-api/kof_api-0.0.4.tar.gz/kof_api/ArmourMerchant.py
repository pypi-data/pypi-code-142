from game_objects.NPC import NPC

class ArmourMerchant(NPC):
	def __init__(self, name, has_quests, city, region, building):
		self.is_merchant = True
		self.product_type = 'armour'
		self.wares = []
		
		super().__init__(name, has_quests, self.is_merchant, self.product_type, city, region, building, region.currency_type)
		
	def setup_wares(self, wares):
		for w in wares:
			self.wares.append(w)
			print(f"Added {w.name} to Merchants Sale List!")