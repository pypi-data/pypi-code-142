import requests, os, json, time

class ft_connector:
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
		url = 'https://api.intra.42.fr/oauth/token'
		UID = env['UID']
		SECRET = env['SECRET']
		grant_type ='client_credentials'
		scope = "public projects profile elearning tig forum"
		try:
			reply = requests.post(url,auth=(UID, SECRET),data={'scope': scope, 'grant_type':grant_type,'client_id':UID,'client_secret':SECRET})
			reply.raise_for_status()
		except requests.exceptions.HTTPError as err:
				exit(print(self.RED + str(err)))
		token = json.loads(reply.text)
		self.head = {'Authorization' : "Bearer {}".format(token['access_token'])}
		self.url = 'https://api.intra.42.fr/v2'
		self.verbose = True
		print(self.BLUE + "[42 CONNECTOR] Verbose activate." + self.DEFAULT)
		print(self.GREEN + "[42 CONNECTOR] Connector ready to use! " + self.BLUE + "(If you need some information : helper() - or thanos@42paris.fr)" + self.DEFAULT)

#############################################
# Helper présentant les différentes commandes
#############################################
	def helper(self):
		print('[42 CONNECTOR] All function available :')
		print("\t- \"launcher([requests],[url],)\" -> Will launch the request on url.")
		print("\t- \"get([url])\" -> Will return the data of the get url.")
		print("\t- \"post([url],['body'])\" -> Will post the body on the url.")
		print("\t- \"patch([url],['body'])\" -> Will patch url with the body.")
		print("\t- \"delete([url])\" -> Will delete url.")
		print("\t- \"put_in_file([data],[*name])\" -> Will put the data in file, if name param was given, file will take the name, else file will be name output.json.")
		print("\t- \"build_list_email([lst_login])\" -> Will build list of email (login@student.42.fr) more display all the login of given list.")
		print("\t- \"get_login([id])\" -> Return login for given id.")
		print("\t- \"get_id([login])\" -> Return id for given login.")
		print("\t- \"get_mail([login])\" -> Return email for given login.")
		print("\t- \"get_level([login])\" -> Return level for given login.")
		print("\t- \"change_password([login],[new_password])\" -> Change password for given login.")
		print("\t- \"verbose()\" -> Activate verbose.")
		print("\t- \"unverbose()\" -> Deactivate verbose.")

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
			exit(print(self.RED + '[42 CONNECTOR] No .env detected.' + self.DEFAULT))
		if not 'UID' in ret or not 'SECRET' in ret:
			exit(print(self.RED + '[42 CONNECTOR] Wrong parameters in .env, you should put in your file:\nSECRET=[Your secret token]\nUID=[Your UID token]' + self.DEFAULT))
		return (ret)

###################################
# Créateur de .json avec de la data
###################################
	def put_in_file(self, data, **kwargs):
		to_write = json.dumps(data, indent=4, sort_keys=True)
		if 'name' in kwargs:
			name = '42_' + kwargs['name']
		else:
			name = '42_output.json'
		if os.path.exists(name):
			os.remove(name)
		output = open(name, 'w')
		for line in to_write:
			output.write(line)
		print(self.GREEN + f"[42 CONNECTOR] Data was put in {name}." + self.DEFAULT)

###################################
# Permet de lancer un call unitaire
###################################
	def launcher(self, ftc, url, **kwargs):
		function = self.build_function_dispatch()
		lst = url.split(' ')
		self.put_in_file(function[ftc](self.build_endpoint(lst)))

##################################
# Renvoie un pointeur sur fonction
##################################
	def build_function_dispatch(self):
		launch = {}
		launch['SCRAP'] = self.scrap
		launch['GET'] = self.get
		launch['DEL'] = self.delete
		launch['POST'] = self.post
		launch['PATCH'] = self.patch
		return (launch)

###########################################
# Constuit l'url en fonction des paramètres
###########################################
	def	build_endpoint(self, param):
		endpoint = param[0]
		for p in param[1:]:
			if '?' in endpoint:
				endpoint += "&" + p
			else:
				endpoint += "?" + p
		return (endpoint)

###############################################################################################
# Construit l'url en formatant le nombre de page et en permettant de récupérer des pages voulus
###############################################################################################
	def build_page(self, endpoint):
		if "?" in endpoint:
			endpoint += "&"
		else:
			endpoint += "?"
		endpoint += "page[size]=100&page[number]="
		return(endpoint)

###########################################
# Scrapping de la data via get sur l'api 42
###########################################
	def scrap(self, url):
		i = 0
		sum_dict = []
		endpoint = self.build_page(url)
		while True:
			url = self.url + endpoint + str(i)
			try :
				reply = requests.get(url, headers=self.head)
				if reply.status_code == 429:
					continue
				reply.raise_for_status()
			except requests.exceptions.HTTPError as err:
				print(self.RED + '[42 CONNECTOR] ' + str(err) + " on SCRAP " + endpoint + self.DEFAULT)
				return
			if 'X-Page' in reply.headers :
				sum_dict += json.loads(reply.text)
				if int(reply.headers['X-Page']) * int(reply.headers['X-Per-Page']) >= int(reply.headers['X-Total']):
					break
			else:
				if self.verbose == True:
					print(self.GREEN + "[42 CONNECTOR] Success SCRAP on " + url + self.DEFAULT)
				return (json.loads(reply.text))
			i+=1
		print(self.GREEN + "[42 CONNECTOR] Success SCRAP on " + url + self.DEFAULT)
		return (sum_dict)

##############################################
# Récupération de la data via get sur l'api 42
##############################################
	def get(self, url):
		if "?" in url:
			url += "&page[size]=100"
		else:
			url += "?page[size]=100"
		try:
			reply = requests.get(self.url + url, headers=self.head)
			if reply.status_code == 429:
				self.get(url)
			reply.raise_for_status()
		except requests.exceptions.HTTPError as err:
			print(self.RED + '[42 CONNECTOR] ' + str(err) + " on GET " + self.url + url + self.DEFAULT)
			return
		print(self.GREEN + "[42 CONNECTOR] Success GET on " + url + self.DEFAULT)
		return (json.loads(reply.text))

######################################################
# Post de la data sur un url en fonction du body donné
######################################################
	def post(self, endpoint, **kwargs):
		url = self.url + endpoint
		try:
			reply = requests.post(url, json=kwargs['body'], headers=self.head)
			reply.raise_for_status()
			if self.verbose == True:
				print(self.GREEN + "[42 CONNECTOR] Success POST on " + url + self.DEFAULT)
		except requests.exceptions.HTTPError as err:
			self.put_in_file(json.loads(reply.text), name='error.json')
			print(self.RED + '[42 CONNECTOR] ' + str(err) + ' on POST ' + url + self.DEFAULT)

#######################################################
# Patch de la data sur un url en fonction du body donné
#######################################################
	def patch(self, endpoint, **kwargs):
		url = self.url + endpoint
		try:
			reply = requests.patch(url, json=kwargs['body'], headers=self.head, )
			reply.raise_for_status()
			if self.verbose == True:
				print(self.GREEN + "[42 CONNECTOR] Success PATCH on " + url + self.DEFAULT)
		except requests.exceptions.HTTPError as err:
			self.put_in_file(json.loads(reply.text), name='error.json')
			print(self.RED + '[42 CONNECTOR] ' + str(err) + ' on PATCH ' + url + self.DEFAULT)

##############################
# Delete de la data sur un url
##############################
	def delete(self, endpoint, **kwargs):
		url = self.url + endpoint
		try:
			reply = requests.delete(url, headers=self.head )
			reply.raise_for_status()
			if self.verbose == True:
				print(self.GREEN + "[42 CONNECTOR] Success DELETE on " + url + self.DEFAULT)
		except requests.exceptions.HTTPError as err:
			self.put_in_file(json.loads(reply.text), name='error.json')
			print(self.RED + '[42 CONNECTOR] ' + str(err) + ' on DELETE ' + url + self.DEFAULT)

################################################################################################
# Prends une liste de login et ajoute @student.42.fr au login en l'imprimant sous forme de liste
################################################################################################
	def build_list_email(self, all_logins):
		print("[", end='')
		i = 0
		for login in all_logins:
			print("\""+ login + "@student.42.fr\"", end='')
			if i != len(all_logins) - 1:
				print(",",end='')
			i+=1
		print("]")
		for login in all_logins:
			print(login)

###################################
# Renvoie un login pour un id donné
###################################
	def get_login(self, id):
		url = f"/users/{id}"
		data = self.get(url)
		return (data['login'])

###################################
# Renvoie un id pour un login donné
###################################
	def get_id(self, login):
		url = f"/users/{login}"
		data = self.get(url)
		return((((data['cursus_users'])[0])['user'])['id'])

#########################################################
# Renvoie le mail privé d'un étudiant pour un login donné
#########################################################
	def get_mail(self, login):
		url = f"/users/{login}/user_candidature"
		data = self.get(url)
		return(data['email'])

###########################
# Modifie le mdp d'un login
###########################
	def change_password(self, login, new_password):
		url = f"/users/{login}?user[password]={new_password}"
		body = None
		data = self.patch(url, body=body)
		return (data)

######################################
# Renvoie le level pour un login donné
######################################
	def get_level(self, login):
		url = f"/users/{login}/cursus_users?filter[cursus_id]=21"
		data = self.get(url)
		return (data[0]['level'])

#####################################
# Active le mode verbose du connector
#####################################
	def verbose(self):
		self.verbose = True
		print(self.BLUE + "[42 CONNECTOR] Verbose activate." + self.DEFAULT)


########################################
# Desactive le mode verbose du connector
########################################
	def unverbose(self):
		self.verbose = False
		print(self.BLUE + "[42 CONNECTOR] Verbose desactivate." + self.DEFAULT)
