
# BUILD DE LA DATA FORMATE
class update_properties:
	def __init__(self, **kwargs):
		self.users = kwargs['users_list']

	def build_text(self, text):
		data = {
					"annotations": {
						"bold": False,
						"code": False,
						"color": "default",
						"italic": False,
						"strikethrough": False,
						"underline": False
					},
					"href": None,
					"plain_text": text,
					"text": {
						"content": text,
						"link": None
					},
				"type": "text"
			}
		return data

	# UPDATE ELEMENT
	def noneUpdate(self, elem):
		return None

	def update_date(self, elem):
		if elem['properties']['date'] != None and elem['value_start'] != None:
			if elem['properties']['date']['start'] != elem['value_start'] or elem['properties']['date']['end'] != elem['value_end']:
				elem['properties']['date']['start'] = elem['value_start']
				elem['properties']['date']['end'] = elem['value_end']
			else :
				return None
		elif elem['value_start'] != None and elem['properties']['date'] == None:
			print("ICI")
			elem['properties']['date'] = {}
			elem['properties']['date']['start'] = elem['value_start']
			elem['properties']['date']['end'] = elem['value_end']
			elem['properties']['date']['time_zone'] = None
		else:
			return None
		return elem['properties']


	def update_title(self, elem):
		if elem['properties']['title'] == [] and elem['value'] == None:
			return None
		elif elem['properties']['title'] != [] and elem['value'] == None:
			elem['properties']['title'] = []
		elif elem['properties']['title'] != [] and elem['value'] != elem['properties']['title'][0]['plain_text']:
				elem['properties']['title'][0]['plain_text'] = elem['value']
				elem['properties']['title'][0]['text']['content'] = elem['value']
		elif elem['properties']['title'] == [] and elem['value'] != None :
			elem['properties']['title'].append(self.build_text(elem['value']))
		else :
			return None
		return elem['properties']

	def update_rich_text(self, elem):
		if elem['properties']['rich_text'] == [] and elem['value'] == None:
			return None
		elif elem['properties']['rich_text'] != [] and elem['value'] == None:
			elem['properties']['rich_text'] = []
		elif elem['properties']['rich_text'] != [] and elem['value'] != elem['properties']['rich_text'][0]['plain_text']:
				elem['properties']['rich_text'][0]['plain_text'] = elem['value']
				elem['properties']['rich_text'][0]['text']['content'] = elem['value']
		elif elem['properties']['rich_text'] == [] and elem['value'] != None :
			elem['properties']['rich_text'].append(self.build_text(elem['value']))
		else :
			return None
		return elem['properties']

	def update_multi_select(self, elem):
		if elem['properties']['multi_select'] != elem['value']:
			elem['properties']['multi_select'] = []
			for obj in elem['value']:
				elem['properties']['multi_select'].append(obj)
		else:
			return None
		return elem['properties']

	def update_people(self, elem):
		if elem['properties']['people'] != elem['value']:
			elem['properties']['people'] = []
			for people in elem['value']:
				update = False
				for user in self.users:
					if people == user['name']:
						update = True
						elem['properties']['people'].append(user)
				if update == False:
					return None
		else:
			return None
		return elem['properties']

	def update_checkbox(self, elem):
		if elem['properties']['checkbox'] != elem['value']:
			elem['properties']['checkbox'] = elem['value']
		else:
			return None
		return elem['properties']

	def update_url(self, elem):
		if elem['properties']['url'] != elem['value']:
			elem['properties']['url'] = elem['value']
		else:
			return None
		return elem['properties']

	def update_number(self, elem):
		if elem['properties']['number'] != elem['value']:
			elem['properties']['number'] = elem['value']
		else:
			return None
		return elem['properties']

	def update_email(self, elem):
		if elem['properties']['email'] != elem['value']:
			elem['properties']['email'] = elem['value']
		else:
			return None
		return elem['properties']

	def update_phone_number(self, elem):
		if elem['properties']['phone_number'] != elem['value']:
			elem['properties']['phone_number'] = elem['value']
		else:
			return None
		return elem['properties']

	def update_properties(self, elem):
		function = {
			"title" : self.update_title,
			"rich_text" : self.update_rich_text,
			"date" : self.update_date,
			"number" : self.update_number,
			"checkbox" : self.update_checkbox,
			"url" : self.update_url,
			"email" : self.update_email,
			"phone_number" : self.update_phone_number,
			"multi_select" : self.update_multi_select,
			"people" : self.update_people,
			"last_edited_by": self.noneUpdate,
			"select" : self.noneUpdate,
			"status" : self.noneUpdate,
			"last_edited_time": self.noneUpdate,
			"created_by": self.noneUpdate,
			"created_time": self.noneUpdate,
			"formula" : self.noneUpdate
		}
		ret = function[elem['properties']['type']](elem)
		return ret
