#%%
import requests



class Pyjama:
    debug = 'False'
    logging = 'False'
    def __init__(self, project_id, username, password, test_instance=False, use_labs=False):
        self.project = project_id
        self.username = username
        self.password = password
        self.project_id=project_id
        self.instance = "https://rqmprod.intra.infineon.com"
        if (test_instance) : self.instance = "https://rqmtest.intra.infineon.com"
        self.api_version = "latest"
        if (use_labs) : self.api_version = "labs"
        #compose the endpoint now
        self.endpoint = self.instance + "/rest/" + self.api_version + "/"



    ######## GET ITEM ##########

    def get_items(self):
        """Get all items in the project with the specified ID"""
        base_url = self.endpoint + "items/"
        params = {
            "project": self.project
        }
        response = requests.get(base_url, auth=(self.username, self.password), params=params)
        return response.json()

    def get_item_by_id(self, item_id):
        """Get the item with the specified ID"""
        base_url = self.endpoint + f"items/{item_id}"
        params = {
            "project": self.project
        }
        response = requests.get(base_url, auth=(self.username, self.password), params=params)
        return response.json()
    def get_documentKey (self, item_id) :
        response = self.get_item_by_id(item_id)
        if "data" in response : 
            return response['data']['documentKey']
        else : return "n.a."    
        
    
        
    ######## POST ITEMS ########
    def post_item(self, name, item_type, parent_id, project_id=None, description=None):
        """Create a new item.Item type numbers:\n Test Case: 26;\n Requirement: 47"""
        base_url = self.endpoint + f"items"
        if (project_id == None) : 
            project_id = self.project_id
        body = {
            "project": project_id,
            "itemType": item_type,
            "childItemType": item_type,
            "location": {
                "parent": {
                    # "item": 8873864,
                    "item": parent_id,
                }
            },
            "fields": {
                "name": name,
                "description" : description
            }
        }
        response = requests.post(base_url, auth=(self.username, self.password), json=body)
        daten=response.json()
        id="null"
        status="null"
        if daten["meta"]["status"] == "Created":
            try:
                id=daten["meta"]["id"]
                status= True
            except:
                pass
        else:
            id="null"
            status= False

        return daten, id



    def post_TC_set(self, name, parent_id, project_id=None, description=None):
        """Create a new item.Item type numbers:\n Test Case: 26;\n Requirement: 47"""
        base_url = self.endpoint + f"items"
        if (project_id == None) : 
            project_id = self.project_id
        body = {
            "project": project_id,
            "itemType": 31,
            "childItemType": 26,
            "location": {
                "parent": {
                    # "item": 8873864,
                    "item": parent_id,
                }
            },
            "fields": {
                "setKey": "TC",
                "name": name,
                "description" : description
            }
        }
        response = requests.post(base_url, auth=(self.username, self.password), json=body)
        print(response.json())
        daten=response.json()
        id="null"
        status="null"
        if daten["meta"]["status"] == "Created":
            try:
                id=daten["meta"]["id"]
                status= True
            except:
                pass
        else:
            id="null"
            status= False

        return daten, id


    def post_folder(self, name, parent_id, childItemType,  project_id=None, description=None):
        """Create a new item.Item type numbers:\n Test Case: 26;\n Requirement: 57"""
        base_url = self.endpoint + f"items"
        if (project_id == None) : 
            project_id = self.project_id
        body = {
            "project": project_id,
            "itemType": 32,
            "childItemType": childItemType,
            "location": {
                "parent": {
                    # "item": 8873864,
                    "item": parent_id,
                }
            },
            "fields": {
                "setKey": "TC",
                "name": name,
                "description" : description
            }
        }
        response = requests.post(base_url, auth=(self.username, self.password), json=body)
        print(response.json())
        daten=response.json()
        id=daten["meta"]["id"]

        return id



# %%
