import base64
import json
import getpass
import pandas as pd
import PySimpleGUI as sg
import json
import requests
import subprocess
import platform
from requests_ntlm import HttpNtlmAuth

def ping(host):
    """
    Returns True if host responds to a ping request
    """

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0


def getpw(prompt="Enter your password:"):
    password = getpass.getpass(prompt)
    # Print 10000 new lines to get readable password out of the display buffer
    print("\n"*10000)
    return password

# %% GUI Functions
def PasswordGUI(username=''):
    layout = [
        [sg.Text('Please enter your infineon user name and password....', size=(40, 1))],
        [sg.Text('Username', size=(15, 1)), sg.InputText(username, key='name', focus=True) ],
        [sg.Text('Password', size=(15, 1)), sg.InputText('', key='pass', password_char='*')],
        [sg.Button('OK', bind_return_key=True)]]

    window = sg.Window('IFX Password').Layout(layout)
    (event, var) = window.Read()
    window.Close()
    if event == 'EXIT' or event is None:
        return 0
    else:
        return var


# %% Jama
class IFXjama:
    def __init__(self, user=None, pw=None,
                 host='https://rqmprod.intra.infineon.com', project=None):
        # replace {base_url}, username and password
        self.baseURL = host + "/rest/latest/"
        self.host = host
        self.__prj_id=project
        if user:
            self.username = user
        else:
            self.username = getpass.getuser()

        if pw:
            self.__pw = pw
        else:
            self.__pw = getpw()

        self.__auth = (self.username, self.__pw)

        self.__result = False



    def __loadProjectsFromServer(self):
        prjs = self.getAll("projects")
        self.__prj_list = {}
        self.__prj_names = {}
        for p in prjs:
            self.__prj_list[p['projectKey']] = p['fields']
            self.__prj_list[p['projectKey']]['id'] = p['id']
            self.__prj_names[p['fields']['name']] = p['projectKey']

    def __loadUserFromServer(self):
        user = self.getAll("users")
        self.__user_list = {}
        for u in user:
            self.__user_list[u['username']] = u

    def __loadProjectItemTypes(self):
        tmp = self.getAll('projects/' + str(self.__prj_id) + '/itemtypes')
        self.prj_item_types = pd.io.json.json_normalize(tmp)
        self.__prj_item_types = {}
        for p in tmp:
            self.__prj_item_types[p['id']] = p

    def __loadProjectGroups(self):
        tmp = self.getAll('usergroups?project=' + str(self.__prj_id))
        self.prj_groups = pd.io.json.json_normalize(tmp)
        self.__prj_groups = {}
        for g in tmp:
            self.__prj_groups[str(g['id'])] = g

    def __loadProjectUsers(self):
        self.__loadProjectGroups()
        tmp = []
        for gid in self.__prj_groups.keys():
            tmp.extend(self.getAll('usergroups/' + str(gid) + '/users'))
        self.prj_user = pd.io.json.json_normalize(tmp)
        self.prj_user.set_index('id', inplace=True )
        # remove duplicates:
        self.prj_user = self.prj_user[~self.prj_user.index.duplicated()]

        self.__prj_users = {}
        for u in tmp:
            self.__prj_users[u['id']] = u


    def getLastResult(self):
        return self.__result



    def loadAllItems(self, itemTypeId=False, gui=False, debug=False):
        if itemTypeId:
            tmp = self.getAll("abstractitems?itemType={}".format(itemTypeId), gui=gui, debug=debug)
        else: # get all items of the specified item type
            tmp = self.getAll('items?project=' + str(self.__prj_id), gui=gui, debug=debug)
        self.__result = pd.io.json.json_normalize(tmp)


    def getItemIDByKey(self, key):
        response = self.get( "abstractitems?documentKey=" +
                            key )

        return response['data'][0]['id']

    def getProjectIDbyKey(self, key):
        return self.__prj_list[key]['id']

    def getItemByID(self, key):
        response = self.get( "items/" + str(key))
        return response["data"]


    def getLockByID(self, key):
        response = self.get( "items/" + str(key) + "/lock" )
        if "OK" in response["meta"]["status"]:
            return response['data']['locked']
        else:
            return "ERR"


    def setLockByID(self, key, lock=True):
        payload = {
            "locked": lock
        }
        url = "items/" + str(key) + "/lock"
        self.put(url, payload)

    def getParentByID(self, key):
        response = self.get( "items/" + str(key) + "/parent" )
        #x = jama.get( "items/" + str(key) + "/parent" )
        return response['data']

    def getChildrenByID(self, key):
        response = self.get( "items/" + str(key) + "/children" )
        #x = jama.get( "items/" + str(key) + "/children" )
        return response['data']
        #return x

    def getPrjRelationships(self):
        # TODO: Implement
        x = jama.get( "relationships?project=152" )

    def test(self):
        tmp = self.getAll('items?project=' + str(self.__prj_id), True)
        self.prj_items = pd.io.json.json_normalize(tmp)

    def getProjectsNames(self):
        return list(self.__prj_names.keys())

    def getProjectsKeys(self):
        return list(self.__prj_names.values())

    def getCurentProject(self):
        return self.__cur_prj

    def getUserByID(self, ID):
        return self.prj_user['username'][ID]

    def setProject(self, pid):
        if pid in self.getProjectsNames():
            self.__cur_prj = self.__prj_names[pid]
        elif pid in self.getProjectsKeys():
            self.__cur_prj = pid
        if self.__cur_prj:
            self.__prj_id = self.__prj_list[self.__cur_prj]['id']
            self.__loadProjectUsers()
            self.__loadProjectItemTypes()
#            self.__loadProjectItems()
        else:
            print('error no such key')

    def getItemTypes(self, get_all=False):
        # using this for the item type IDs and not for the configuration of fields
        if get_all or not self.__cur_prj:
            return self.getAll("itemtypes")
        else:
            return self.getAll("/projects/" + self.__cur_prj + "/itemtypes")

    def getComments(self):
        return self.getAll("comments")

    def getRelationships(self, projectId):
        relationships = self.getAll("relationships?project={}".format(projectId))
        for relationship in relationships:
            relationship["project"] = projectId
        return relationships

    def get (self, resource):
        url = self.baseURL + resource
        response = requests.get(url, auth=self.__auth, verify=False)
        return json.loads(response.text)

    def put(self, resource, payload):
        url = self.baseURL + resource
        response = requests.put(url, json=payload,
                                auth=self.__auth, verify=False)
        return response.status_code
    
    def post(self, resource, payload):
        url = self.baseURL + resource
        response = requests.post(url, json=payload,
                                auth=self.__auth, verify=False)
        return response

    def getAll(self, resource, load_num=20, gui=False, debug=False):
        allResults = []
        resultsRemaining = True
        currentStartIndex = 0
        resultCount = 0
        totalResults = 0
        delim = '&' if '?' in resource else '?'

        while resultsRemaining:
            startAt = delim + "startAt={}".format(currentStartIndex)
            jsonResponse = self.get(resource + startAt)
            if "pageInfo" in jsonResponse["meta"]:
                resultCount = jsonResponse["meta"]["pageInfo"]["resultCount"]
                totalResults = jsonResponse["meta"]["pageInfo"]["totalResults"]
                if debug:
                    print("---------------------------------------------")
                    print("JAMA-URL: %s" % (self.baseURL + resource + startAt))
                    print("startIndex={}".format(currentStartIndex))
                    print("totalResults={}".format(totalResults))
                    print("resultCount={}".format(resultCount))
                    print("\n\n")

            resultsRemaining = currentStartIndex + resultCount < totalResults
            currentStartIndex += load_num
            if "data" in jsonResponse:
                allResults.extend(jsonResponse["data"])
            if gui:
                x = sg.OneLineProgressMeter('Getting Requirements from JAMA', currentStartIndex, totalResults, 'key')
                if not x and resultsRemaining: # Cancel button was presed
                    return allResults
            else:
                remaining = totalResults-currentStartIndex if resultsRemaining else 0
                print("%d jama-items of %d remaining" % (remaining, totalResults))
        return allResults

    def getID(self, string_to_find):
        url = "abstractitems?contains=" + string_to_find
        json_response = self.get(url)

        total_results = json_response["meta"]["pageInfo"]["totalResults"]

        if total_results == 1:
            data = json_response["data"]
            item = data[0]
            return item["id"]
        else:
            print( "string_to_find wasn't unique")
            # sys.exit(1)

    def searchDescription(self, search_str, get_all=False):
        url = "abstractitems?"
        # using this for the item type IDs and not for the configuration of fields
        if not get_all and self.__cur_prj:
            url = url + "abstractitems?project=" + self.__cur_prj + "&"
        url = url + "contains=" + search_str
        response = self.getAll(url)
        self.__result = pd.io.json.json_normalize(response)
        return self.__result

    def getItem(item_id):
        url = "items/" + str(item_id)
        json_response = self.get(url)

        return json_response["data"]

    def putItem(self, item_id, payload):
        url = "items/" + str(item_id)
        status_code = self.put(url, payload)
        if status_code < 400:
            return True  # success
        else:
            return False

    def getID2(string_to_find):
        url = "abstractitems?contains=" + string_to_find
        json_response = self.get(url)

        total_results = json_response["meta"]["pageInfo"]["totalResults"]

        return json_response["data"]
    
    def getFilters(self):
        url = "filters?project=" + str(self.__prj_id)
        json_response = self.getAll(url)

        return json_response   
    
    def getFilterResults(self, filter_id):
        url = "filters/" + str(filter_id) + "/results"
        json_response = self.getAll(url)

        return json_response
    
    def getUpstreamRelatedItems(self, item_id):
        url = "items/" + str(item_id) + "/upstreamrelated"
        json_response = self.getAll(url)
        
        return json_response

    def getDownstreamRelatedItems(self, item_id):
        url = "items/" + str(item_id) + "/downstreamrelated"
        json_response = self.getAll(url)
        
        return json_response

    def getDownstreamRelationships(self, item_id):
        url = "items/" + str(item_id) + "/downstreamrelationships"
        json_response = self.getAll(url)
        
        return json_response
    
    def setRelationship(self, from_item, to_item, relationship_type):
       resource = "relationships"
       payload = {
          "fromItem": from_item,
          "toItem": to_item,
          "relationshipType": relationship_type
          }         
       response = self.post(resource, payload)
       if response.status_code == 201:
             return True
       else:
             print(response.text)
             return False   
            
    def getSyncedItems(self, item_id):
        url = "items/" + str(item_id) + "/synceditems"
        json_response = self.getAll(url)
        
        return json_response
    
    def getSyncedStatus(self, item_id, synced_item_id):
        url = "items/" + str(item_id) + "/synceditems/" + str(synced_item_id) + "/syncstatus"
        json_response = self.get(url)
        
        return json_response["data"]["inSync"]
        
    def getBaselines(self, project_id):
        url = "baselines/?project=" + str(project_id)
        json_response = self.getAll(url)
        
        return json_response
    
    def getBaselineVersionedItems(self, baseline_id):
        url = "baselines/" +str(baseline_id) +"/versioneditems"
        json_response = self.getAll(url)
        
        return json_response
    
    def getItemVersions(self, item_id):
        url = "items/" + str(item_id) + "/versions"
        json_response = self.getAll(url)
        
        return json_response
    
    def getUpstreamRelationships(self, item_id):
        url = "items/" + str(item_id) + "/upstreamrelationships"
        json_response = self.getAll(url)
        
        return json_response



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



def get_all_Req(MainCompID, Jama):
    req_list=[]
    
    instance1=Jama.getChildrenByID(str(MainCompID))
    #print(instance1)
    comp_list=[MainCompID]

    for entry in instance1:
        if entry["itemType"]==31 and entry['childItemType']==57:
            req_list.append(entry["id"])
        elif entry["itemType"] == 30:
            comp_list.append(entry["id"])

    while comp_list != []:
        for item in comp_list:
            instance_temp=Jama.getChildrenByID(str(item))
            for entry in instance_temp:
                if entry["itemType"]==31 and entry['childItemType']==57:  #--> Findet set von REQ
                    req_list.append(entry["id"])
                elif entry["itemType"] == 30:
                    comp_list.append(entry["id"])

            #print(item)

            comp_list.remove(item)
            
    req_list=list(set(req_list))

    return(req_list)


def get_parent_id_dict(id_list, Jama): 
    parent_id_dict={}

    for item in id_list:
        output=Jama.getParentByID(str(item))

        par_id=output["id"]

        if par_id in parent_id_dict:
            parent_id_dict[par_id].append(item)
            
        elif par_id not in parent_id_dict:
            parent_id_dict[par_id]=[item]
            
    return parent_id_dict


def create_TC_for_ReQ(parent_id_dict, Jama, Jama2):
    req_TC_list=[]

    #create set of TC for set of ReQ:
    for element in parent_id_dict:
        element_info=Jama.getItemByID(element)
        status, req_set_id = Jama2.post_TC_set("TCs for '" + element_info["fields"]["name"] + "'", element)
        #status, TC_id = Jama2.post_item(TC_name, 26,  set_id)
        req_TC_list.append((int(str(parent_id_dict[element])[1:-1]),req_set_id))

    return req_TC_list


def create_all_TCs(req_TC_list, Jama, Jama2):
    for req_id, set_id in req_TC_list:
        req_children=Jama.getChildrenByID(req_id)
        for dictionary in req_children:

            if dictionary["itemType"]==32:
                tc_folder_id = Jama2.post_folder(dictionary["fields"]["name"], set_id, 26)
                req_folder_children = Jama.getChildrenByID(dictionary["id"])

                
                for item in req_folder_children:
                    if  item["itemType"]==57:
                        status, tc_id=Jama2.post_item(item["fields"]["name"], 26, tc_folder_id)
                        status_response=Jama.setRelationship(item["id"],tc_id,  15)

            elif dictionary["itemType"]==57:
                status, tc_id=Jama2.post_item(dictionary["fields"]["name"], 26, set_id)
                status_response=Jama.setRelationship(dictionary["id"],tc_id,  15)



class JamaAPI:

    def __init__(self, username, password, project_id):
        self.username=username
        self.project_id=project_id
        self.__password=password
        self.Jama = IFXjama(user=self.username, pw=self.__password, project=self.project_id)
        self.Jama2 = Pyjama(project_id=self.project_id, username=self.username, password=self.__password)


    def generateTC(self, MainCompID):

        test = get_all_Req(MainCompID, self.Jama)
        parent_id_dict = get_parent_id_dict(test, self.Jama)
        req_TC_list = create_TC_for_ReQ(parent_id_dict, self.Jama, self.Jama2)
        create_all_TCs(req_TC_list, self.Jama, self.Jama2)

        return req_TC_list


    def delete_TC_set(self, id_list):
        basic_auth = base64.encodebytes(('%s:%s' % (self.username, self.__password)).encode()).decode().strip()
        headers =    {'JamaAuth': basic_auth}
        for id in id_list:
            try:
                url="https://webnetdev.muc.infineon.com/unicon_DEVELOP/Api/JamaProd/items/deleteItem?id="+str(id)
                response=requests.delete(url, auth=HttpNtlmAuth(self.username, self.__password), headers=headers, verify=False)
                print(response.json())

            except:
                pass
