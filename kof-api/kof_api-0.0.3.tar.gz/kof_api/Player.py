class Player:
	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age
		self.health = 100
		self.current_carry, self.max_carry = (0,150)
		self.atk, self.defense = (1,1)
		self.loc = ""
		self.animals = []
		self.wagons = []
		self.ships = []
		self.wallet = {}
		
		self.equipped = {
			"head" : "Empty",
			"torso" : "Tattered Cloth Shirt",
			"rhand" : "Empty",
			"lhand" : "Empty",
			"legs" : "Tattered Cloth Pants",
			"feet" : "Leather Boots",
			"mount" : "Empty"
		}
		
		self.inventory = []
	
	def add_inv(self, item):
		if self.current_carry < self.max_carry:
			self.current_carry = self.current_carry + item.weight
			self.inventory.append(item)
			print(f"Added {item.name} to inventory")
		else:
			print("Inventory Full!")
		
	def remove_inv(self, item):
		self.inventory.pop(item)
		print(f"Removed {item.name} from inventory")
		
	def equip_item(self, slot, item):
		if item not in self.inventory:
			print(f"No Cheating! You must obtain a {item.name} first!")
		else:
			if item.type == slot:
				self.equipped[slot] = item.name
				self.atk = self.atk + item.atk
				self.defense = self.defense + item.defense
				print(f"Equipped {item.name} to {slot}")
			else:
				print(f"{item.name} can't be equipped to {slot}")
	
	def unequip_item(self, slot):
		item = self.equipped[slot]
		self.equipped[slot] = "Empty"
		self.atk, self.defense = (1,1)
		print(f"Unequipped {item}...")
		
	def add_animal(self, animal):
		self.animals.append(animal)
		print(f"Added {animal.name} to owned Animals!")
		
	def remove_animal(self, animal):
		for a in self.animals:
			if a.name == animal.name:
				self.animals.pop()
				print(f"Removed {animal.name} from owned Animals!")
				
	def add_wagon(self, wagon):
		self.wagons.append(wagon)
		print(f"Added {wagon.name} to Owned Wagons!")
		
	def remove_wagon(self, wagon):
		for w in self.wagons:
			if w.name == wagon.name:
				self.wagons.pop()
				print(f"Removed {wagon.name} from Owned Wagons!")
	
	def add_ship(self, ship):
		self.ship.append(ship)
		print(f"Added {ship.name} to Owned Ships!")
		
	def remove_ship(self, ship):
		for s in self.ships:
			if s.name == ship.name:
				self.ships.pop()
				print(f"Removed {ship.name} from Owned Ships!")
				
	def observe_gear(self):
		for equip in self.equipped:
			print(f"{equip} : {self.equipped[equip]}")
			
	def add_wallet(self, currency_type,  amount):
			if currency_type not in self.wallet.keys():
				self.wallet[currency_type] = amount
				print(f"""{currency_type} doesn't exist in the Player's wallet! Created new wallet for {currency_type}
				
New Balance: {self.wallet[currency_type]} {currency_type}				
				""")
				return
			
			if self.wallet[currency_type] == 0:
				self.wallet[currency_type] = amount
				print(f"""Added {amount} {currency_type} to Players Wallet!
				
New Balance: {self.wallet[currency_type]} {currency_type}
				""")
				
			else:
				self.wallet[currency_type] = self.wallet[currency_type] + amount
				
				print(f"""Added {amount} {currency_type} to Players Wallet!
				
New Balance: {self.wallet[currency_type]} {currency_type}
				""")
				
	def observe_wallet(self):
			for wallet in self.wallet:
				print(f"{self.wallet[wallet]} {wallet}")
				
	def browse_wares(self, merchant):
			for item in merchant.wares:
				print(f"{item.name} : {item.price} {merchant.region.currency_type}")
				
	def observe_animal(self):
			for animal in self.animals:
				print(f"""
Name : {animal.name}
Weight : {animal.weight}
Capacity : ({animal.capacity}, {animal.max_capacity})

Inventory:
""")
				for i in animal.inv:
					print(f"{i.name}")
			