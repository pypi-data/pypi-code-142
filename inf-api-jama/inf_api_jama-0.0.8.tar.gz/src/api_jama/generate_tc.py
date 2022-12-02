# %%
from ifx import IFXjama
import base64
import requests
from requests_ntlm import HttpNtlmAuth
from compactPyjama import Pyjama


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


# %%
