import requests, os, json, time
from ftThanos.notion_get_properties import *
from ftThanos.notion_update_properties import *

class notion_connector:
	ESC = "\x1b"
	BLACK = ESC + "[30m"
	BLUE = ESC + "[34m"
	RED = ESC + "[31m"
	GREEN = ESC + "[32m"
	DEFAULT = ESC + "[39m"
	verbose = False

###############
# Main fonction
###############
	def __init__(self, **kwargs):
		env = self.dot_env_parser()
		TOKEN = env['TOKEN']
		self.head = {
		"Accept": "application/json",
		"Authorization": "Bearer " + TOKEN,
		"Content-Type": "application/json",
		"Notion-Version": "2022-06-28"
		}
		self.url = 'https://api.notion.com/v1'
		self.all_users = (json.loads(requests.get(self.url + '/users', headers=self.head).text))['results']
		self.update = update_properties(users_list=self.all_users)
		self.verbose = True
		print(self.BLUE + "[NOTION CONNECTOR] Verbose activate." + self.DEFAULT)
		print(self.GREEN + "[NOTION CONNECTOR] Connector ready to use! " + self.BLUE + "(If you need some information : helper() - or thanos@42paris.fr)" + self.DEFAULT)

#############################################
# Helper présentant les différentes commandes
#############################################
	def helper(self):
		print('[NOTION CONNECTOR] All function available :')
		print("\t- \"put_in_file([data],[*name])\" -> Will put the data in file, if name param was given, file will "
			  "take the name, else file will be name output.json.")
		print("\t- \"getDb(dbId)\" -> Activate verbose.")
		print("\t- \"updateDb(pageId, data)\" -> Activate verbose.")
		print("\t- \"createDb(parentId)\" -> Activate verbose.")
		print("\t- \"addPageDb(dbId, name)\" -> Activate verbose.")
		print("\t- \"getIdLine(elem)\" -> Activate verbose.")
		print("\t- \"getProperties(elem)\" -> Activate verbose.")
		print("\t- \"updateProperties(elem)\" -> Activate verbose.")
		print("\t- \"getAllUsers()\" -> Activate verbose.")
		print("\t- \"verbose()\" -> Activate verbose.")
		print("\t- \"unverbose()\" -> Deactivate verbose.")

###################################
# Créateur de .json avec de la data
###################################
	def put_in_file(self, data, *args):
		to_write = json.dumps(data, indent=4, sort_keys=True)
		if len(args) > 0:
			name = 'notion_' + args[0]
		else:
			name = 'notion_output.json'
		if os.path.exists(name):
			os.remove(name)
		output = open(name, 'w')
		for line in to_write:
			output.write(line)
		print(self.GREEN + f"[NOTION CONNECTOR] Data was put in {name}." + self.DEFAULT)

################
# Parser de .env
################
	def dot_env_parser(self):
		ret = {}
		try :
			with open ('.env', 'r') as file:
				for line in file:
					lst = line.split('=')
					if len(lst) != 2:
						continue
					ret[lst[0]] = lst[1][:-1]
		except IOError:
			exit(print(self.RED + '[NOTION CONNECTOR] No .env detected.' + self.DEFAULT))
		if not 'TOKEN' in ret:
			exit(print(self.RED + '[NOTION CONNECTOR] Wrong parameters in .env, you should put in your file:\nTOKEN=[Your notion token]' + self.DEFAULT))
		return (ret)

###############################
# Utilisation sur les databases
###############################
	def getDb(self, dbId):
		url = self.url + '/databases/' + dbId + '/query'
		body = {
			"sorts": [],
			"page_size": 100
		}
		data = []
		end_reply = {"next_cursor" : None}
		try :
			while (True):
				if end_reply['next_cursor'] is not None:
					if end_reply['has_more'] == True:
							body = {"sorts" : [],
									"start_cursor" : end_reply['next_cursor']
									}
				reply = requests.post(url, data=json.dumps(body), headers=self.head)
				reply.raise_for_status()
				end_reply = json.loads(reply.text)
				data += end_reply['results']
				if end_reply['next_cursor'] is None:
					break
		except requests.exceptions.HTTPError as err:
			self.put_in_file(json.loads(reply.text), 'error.json')
			print(self.RED + '[NOTION CONNECTOR] ' + str(err) + ' on POST ' + url + self.DEFAULT)
		ret = []
		for line in data:
			data_line = {
				'page_id' : line['id'],
				'properties' : {}
			}
			for i in line['properties'].items():
				if i[1]['type'] == 'title':
					data_line['title'] = self.getProperties(i[1])['value']
				data_line['properties'][i[0]] = self.getProperties(i[1])
			ret.append(data_line)
		return (ret)

#################################################
# Search title in db and return it if exist, else return None
#################################################
	def getTitle(self, db, title):
		for line in db:
			if 'title' in line.keys():
				if line['title'] == title:
					return (line)
		return None

#################################################
# Permet de mettre à jour une des lignes de la db
#################################################
	def updateDb(self, pageId, properties):
		data = {'properties': {}}
		i = False
		for i in properties.items():
			data['properties'][i[0]] = self.updateProperties(i[1])
			if data['properties'][i[0]] == None:
				del data['properties'][i[0]]
				continue
			i = True
		if i == False:
			return
		self.put_in_file(data, 'test.json')
		url = self.url + '/pages/' + pageId
		try :
			reply = requests.patch(url, headers=self.head, data=json.dumps(data))
			reply.raise_for_status()
			print(self.GREEN + "[NOTION CONNECTOR] Success PATCH on " + url + self.DEFAULT)
		except requests.exceptions.HTTPError as err:
			self.put_in_file(json.loads(reply.text), 'error.json')
			print(self.RED + '[NOTION CONNECTOR] ' + str(err) + ' on PATCH ' + url + self.DEFAULT)
		return (json.loads(reply.text))

##################################
# Créé une nouvelle base de donnée
##################################
	def createDb(self, parentId):
		url = self.url + '/blocks/' + parentId + '/children'
		data = {
			"children": [
					{
					"object": "block",
					"type": "database_id",
					"database_id": {
						"title": "Unnamed"
					},
				}
			]
		}
		try :
			reply = requests.patch(url, hearders=self.head, data=json.dumps(data))
			reply.raise_for_status()
			if self.verbose == True:
				print(self.GREEN + "[NOTION CONNECTOR] Success PATCH on " + url + self.DEFAULT)
		except requests.exceptions.HTTPError as err:
			self.put_in_file(json.loads(reply.text), 'error.json')
			print(self.RED + '[NOTION CONNECTOR] ' + str(err) + ' on PATCH ' + url + self.DEFAULT)
		return (json.loads(reply.text))

###################################
# Retourne le champs title de la db
###################################
	def getTitleProperties(self, db):
		line = db[0]['properties']
		for i in line.items():
			if i[1]['properties']['type'] == 'title':
				return(i[0])

############################################################################
# Rajoute une ligne à la base de donnée, avec pour title le nom mis en param
############################################################################
	def addPageDb(self, dbId, name):
		title = self.getTitleProperties(self.getDb(dbId))
		url = self.url + '/pages'
		data = {
			"parent": { "type": "database_id",
						"database_id": dbId },
			"properties": {
				title: {
					"title": [
						{
							"text": {
								"content": name
							}
						}
					]
				},
			}
		}
		try :
			reply = requests.post(url, headers=self.head, data=json.dumps(data))
			reply.raise_for_status()
			if self.verbose == True:
				print(self.GREEN + "[NOTION CONNECTOR] Success POST on " + url + self.DEFAULT)
		except requests.exceptions.HTTPError as err:
			self.put_in_file(json.loads(reply.text), 'error.json')
			print(self.RED + '[NOTION CONNECTOR] ' + str(err) + ' on POST ' + url + self.DEFAULT)
		line = json.loads(reply.text)
		data_line = {
			'page_id' : line['id'],
			'properties' : {}
		}
		for i in line['properties'].items():
			if i[1]['type'] == 'title':
				data_line['title'] = self.getProperties(i[1])['value']
			data_line['properties'][i[0]] = self.getProperties(i[1])
		return(data_line)

#############################################
# Récupère la l'id de la ligne de la Database
#############################################
	def getIdLine(self, elem):
		return(elem['id'])

#####################################################
# Récupère la fonction pour avoir un obj de propriété
#####################################################
	def getProperties(self, elem):
		return (get_properties(elem))

##################################################
# Met à jour une propriété avec les elements voulu
##################################################
	def updateProperties(self, elem):
		return (self.update.update_properties(elem))

##################################################
# Recupère tout les utilisateurs de l'access token
##################################################
	def getAllUsers(self):
		url = self.url + '/users'
		ret = []
		try :
			reply = requests.get(url, headers=self.head)
			reply.raise_for_status()
			end_reply = json.loads(reply.text)
			ret += end_reply['results']
			if self.verbose == True:
				print(self.GREEN + "[NOTION CONNECTOR] Success POST on " + url + self.DEFAULT)
		except requests.exceptions.HTTPError as err:
			self.put_in_file(json.loads(reply.text), 'error.json')
			print(self.RED + '[NOTION CONNECTOR] ' + str(err) + 'on GET ' + url + self.DEFAULT)
		return (ret)

#####################################
# Active le mode verbose du connector
#####################################
	def verbose(self):
		self.verbose = True
		print(self.BLUE + "[NOTION CONNECTOR] Verbose activate." + self.DEFAULT)

########################################
# Desactive le mode verbose du connector
########################################
	def unverbose(self):
		self.verbose = False
		print(self.BLUE + "[NOTION CONNECTOR] Verbose desactivate." + self.DEFAULT)
