class Math:
	def convert_kg_lb(self, kg):
		lb = kg / 0.45359237
		return round(lb, 2)
		
	def convert_lb_kg(self, lb):
		kg = lb / 2.2046
		return round(kg, 2)