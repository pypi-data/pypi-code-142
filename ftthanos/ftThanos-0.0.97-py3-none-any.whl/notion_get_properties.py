def build_ret(elem):
	ret = {
		'properties' : elem,
		'value' : None
	}
	return (ret)

def ret_status(elem):
	ret = build_ret(elem)
	ret.update({
		'color' : elem['status']['color'],
		'value' : elem['status']['name']
	})
	return ret

def ret_date(elem):
	ret = {
		'properties' : elem,
		'value_start' : None,
		'value_end': None
	}
	if elem['date'] != None:
		ret.update({
			'value_start' : elem['date']['start'],
			'value_end' : elem['date']['end']
		})
	return ret

def ret_formula(elem):
	ret = build_ret(elem)
	if elem['formula'] != None:
		ret.update({
			'value' : elem['formula']['number']
		})
	return ret

def ret_rich_text(elem):
	ret = build_ret(elem)
	if elem['rich_text'] != []:
		ret.update({
			'value' : elem['rich_text'][0]['plain_text']
		})
	return ret

def ret_title(elem):
	ret = build_ret(elem)
	if elem['title'] != []:
		ret.update({
			'value' : elem['title'][0]['plain_text']
		})
	return ret

def ret_number(elem):
	ret = build_ret(elem)
	ret.update({
		'value' : elem['number']
	})
	return ret

def ret_select(elem):
	ret = build_ret(elem)
	if elem['select'] != None:
		ret.update({
			'color' : elem['select']['color'],
			'value' : elem['select']['name']
		})
	return ret

def ret_multi_select(elem):
	ret = build_ret(elem)
	ret.update({
		'value' : []
	})
	for select in ret['properties']['multi_select']:
		del select['id']
		data = {
		'color' : select['color'],
		'name' : select['name']
		}
		ret['value'].append(data)
	return ret

def ret_checkbox(elem):
	ret = build_ret(elem)
	ret.update({
		'value' : elem['checkbox']
	})
	return ret

def ret_people(elem):
	ret = build_ret(elem)
	ret.update({
		'value' : []
	})
	for people in elem['people']:
		ret['value'].append(people['name'])
	return ret

def ret_url(elem):
	ret = build_ret(elem)
	if elem['url'] != None:
		ret.update({
			'value' : elem['url']
		})
	return ret

def ret_created_time(elem):
	ret = build_ret(elem)
	ret.update({
		'value_time' : elem['created_time']
	})
	return ret

def ret_created_by(elem):
	ret = build_ret(elem)
	ret.update({
		'value' : elem['created_by']['name']
	})
	return ret

def ret_last_edited_time(elem):
	ret = build_ret(elem)
	ret.update({
		'value_time' : elem['last_edited_time']
	})
	return ret

def ret_last_edited_by(elem):
	ret = build_ret(elem)
	ret.update({
		'value_name' : elem['last_edited_by']['name']
	})
	return ret

def ret_email(elem):
	ret = build_ret(elem)
	if elem['email'] != None:
		ret.update({
			'value' : elem['email']
		})
	return ret

def ret_phone_number(elem):
	ret = build_ret(elem)
	if elem['phone_number'] != None:
		ret.update({
			'value' : elem['phone_number']
		})
	return ret


def get_properties(elem):
	function = {
		"status" : ret_status,
		"date" : ret_date,
		"rich_text" : ret_rich_text,
		"title" : ret_title,
		"number" : ret_number,
		"select" : ret_select,
		"people" : ret_people,
		"checkbox" : ret_checkbox,
		"url" : ret_url,
		"email" : ret_email,
		"phone_number" : ret_phone_number,
		"multi_select" : ret_multi_select,
		"created_time" : ret_created_time,
		"created_by" : ret_created_by,
		"last_edited_time" : ret_last_edited_time,
		"last_edited_by" : ret_last_edited_by,
		"formula" : ret_formula
	}
	ret = function[elem['type']](elem)
	return ret
