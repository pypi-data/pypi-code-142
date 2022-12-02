# -*- coding: utf-8 -*-
#%%
import base64
import json
import getpass
import pandas as pd
import PySimpleGUI as sg
import json
import requests
import subprocess
import platform

# %% General functions
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

# =============================================================================
# # %% ldap
# class IFXldap():
#     """describe me"""
# 
#     __server = {'address': 'ldapnew.muc.infineon.com', 'port': 3268}
#     __user = [['CN', 'KlamminM'],
#               ['OU', 'EU'],
#               ['OU', 'IFX-Users'],
#               ['DC', 'infineon'],
#               ['DC', 'com']]
#     __pw = ''
# 
#     def __init__(self, pw):
#         self.__pw = pw
#         self.openConn()
# 
#     def setUser(self, user):
#         self.user = user
# 
#     def setServer(self, address, port=3268):
#         self.__server['server'] = address
#         self.__server['port'] = port
# 
#     def openConn(self):
#         """describe me"""
#         from ldap3 import Server, Connection, ALL
#         #    from ldap3 import SIMPLE, SYNC, SUBTREE,, NTLM
#         user = ','.join(["=".join(x) for x in self.__user])
#         ldap_server = Server(self.__server['address'],
#                              get_info=ALL,
#                              port=self.__server['port'])
#         self.conn = Connection(ldap_server,
#                                user=user,
#                                password=self.__pw,
#                                auto_bind=True)
# 
#     def searchUser(self, user, full=False):
#         """describe me"""
#         from ldap3 import ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
#         search_base = 'DC=infineon,DC=com'
# #        search_filter = '(&(objectClass=person)(sAMAccountName=' + user + ')(IFX-User-extensionAttribute7=true))'
#         search_filter = '(&(objectClass=person)(displayName=*' + user + '*))'
# #        search_filter = '(&(objectclass=person)(|(sn=*klamminge*)(givenName=klamminge)))(displayName~=' + user + ')'
# #        print( "Search filter = %s" % search_filter)
#         if full:
#             attributes = [ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES]
#         else:
#             attributes = ['cn', 'sAMAccountName', 'company', 'department',
#                           'displayName', 'givenName', 'sn', 'l', 'mail',
#                           'manager']
#         self.conn.search(search_base,
#                          search_filter,
#                          search_scope='SUBTREE',
#                          attributes=attributes)
#         return self.conn.entries
# 
#     def searchGroupe(self, group, full=False):
#         """describe me"""
#         from ldap3 import ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
#         search_base = 'DC=infineon,DC=com'
# #        search_filter = '(&(objectClass=person)(sAMAccountName=' + group + ')(IFX-User-extensionAttribute7=true))'
#         search_filter = '(&(objectClass=group)(sAMAccountName=*'+group+'*))'
#         if full:
#             attributes = [ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES]
#         else:
#             attributes = ['cn', 'sAMAccountName',
#                           'displayName', 'mail',
#                           'managedBy', 'info',
#                           'msExchGroupMemberCount']
#         self.conn.search(search_base,
#                          search_filter,
#                          search_scope='SUBTREE',
#                          attributes=attributes)
# 
#         return self.conn.entries
# 
#     def getGroupMembers(self, group):
#         search_base = 'DC=infineon,DC=com'
#         search_filter = '(sAMAccountName=' + group + ')'
#         attributes = ['member']
#         self.conn.search(search_base,
#                          search_filter,
#                          search_scope='SUBTREE',
#                          attributes=attributes)
# 
#         members = []
# 
#         search_filter = '(objectClass=Person)'
#         for u in self.conn.entries[0]['member']:
#             ldap.conn.search(u, search_filter, attributes=['cn'])
#             members.append(self.conn.entries[0].cn[0])
# 
#         return members
# 
#     def queryUser(self, usergroupname):
#         """describe me"""
#         from ldap3 import ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
#         search_base = 'DC=infineon,DC=com'
#         search_filter = '(&(objectClass=person)(sAMAccountName='+usergroupname+')(IFX-User-extensionAttribute7=true))'
#         search_filter = '(sAMAccountName=' + usergroupname + ')'
#         attributes = [ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES]
#         self.conn.search(search_base,
#                          search_filter,
#                          search_scope='SUBTREE',
#                          attributes=attributes)
#         return self.conn.entries
# 
#     def queryGroups(self):
#         """describe me"""
# # wo die Gruppen sind die ihr prüfen wollt
#         from ldap3 import ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
#         search_base = 'OU=Groups,OU=Users,OU=MUC,DC=eu,DC=infineon,DC=com'
#         search_base = 'DC=infineon,DC=com'
#         search_filter = '(objectClass=group)'
# #        search_filter = ''
#         attributes = [ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES]
#         self.conn.search(search_base,
#                          search_filter,
# #                         search_scope='BASE',
#                          attributes=attributes)
#         return self.conn.entries
# 
# =============================================================================

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

        # self.__loadProjectsFromServer()
        # if project:
        #     self.setProject(project)
        # else:
        #     self.__cur_prj = None
#        self.__loadUserFromServer()

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

#    def __loadProjectItems(self):
#        self.__project_items = self.getAll('items?project=' + str(self.__prj_id), debug=True)

    def getLastResult(self):
        return self.__result

#    def getProjectItems(self):
#        return self.__project_items

    def loadAllItems(self, itemTypeId=False, gui=False, debug=False):
        if itemTypeId:
            tmp = self.getAll("abstractitems?itemType={}".format(itemTypeId), gui=gui, debug=debug)
        else: # get all items of the specified item type
            tmp = self.getAll('items?project=' + str(self.__prj_id), gui=gui, debug=debug)
        self.__result = pd.io.json.json_normalize(tmp)

#    def getItems(self, itemTypeId=False, gui=False, debug=False):
#        if itemTypeId:
#            tmp = self.getAll("abstractitems?itemType={}".format(itemTypeId), gui=gui, debug=debug)
#        else: # get all items of the specified item type
#            tmp = self.getAll('items?project=' + str(self.__prj_id), gui=gui, debug=debug)
#        self.prj_items = pd.io.json.json_normalize(tmp)
#        return self.prj_items

    def getItemIDByKey(self, key):
        response = self.get( "abstractitems?documentKey=" +
                            key )

#            response = self.get( "abstractitems?project=" +
#                                str(self.__prj_id) +
#                                "&documentKey=" +
#                                key )
        return response['data'][0]['id']

    def getProjectIDbyKey(self, key):
        return self.__prj_list[key]['id']

    def getItemByID(self, key):
        response = self.get( "items/" + str(key))
        return response["data"]

    # def get_all_sub_items(self, key):
    #     url=self.host+ "/perspective.req#/containers/" +key+"?projectId=" + self.__prj_id
    #     print(url)
    #     response=self.get(url)
    #     print(response)



















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
# %% Jira
# =============================================================================
# class IFXjira():
#     """ """
# 
#     host = 'https://jiraatvprod.intra.infineon.com'
#     work_prj = None
#     last_issue = ''
#     reporter = False
# 
#     __del_entr = ['customfield_10001',
#                   'customfield_10200',
#                   'customfield_10901',
#                   'customfield_11302',
#                   'customfield_11711',
#                   'customfield_12800',
#                   'customfield_12601',
#                   'customfield_10103',
#                   'customfield_11700',
#                   'customfield_11701',
# 
#                   'customfield_10000',
#                   'customfield_10101',
#                   'customfield_10102',
#                   'customfield_10104',
#                   'customfield_10107',
#                   'customfield_12100',
#                   'customfield_12101',
#                   'customfield_13600',
# 
#                   'workratio',
#                   'lastViewed',
#                   'watches',
#                   'creator',
#                   'subtasks',
#                   'created',
#                   'reporter',
#                   'aggregateprogress',
#                   'progress',
#                   'votes',
#                   'comment',
#                   'worklog',
#                   'updated',
#                   'status',
#                   'attachment',
#                   'issuelinks',
#                   'assignee',
#                   'resolution',
#                   'resolutiondate']
# 
#     def __init__(self, user=None, pw=None,
#                  host=None, working_project=None):
#         if user:
#             self.user = user
#         else:
#             self.user = getpass.getuser()
# 
#         if pw:
#             self.__pw = pw
#         else:
#             self.__pw = getpw()
# 
#         if host:
#             self.host = host
# 
#         self.jiraInit()
# 
#         if working_project:
#             self.setWorkingProject(working_project)
# #
# #        proles = self.jac.project_roles(self.work_prj)
# #        rid = proles['pDevelopers']['id']
# #        p_dev = self.jac.project_role(self.work_prj, rid)
# #        self.pdev = []
# #
# #        self.target_issuetypes = self.jiraGetIssueTypes(self.jac,
# #                                                        self.work_prj)
# #
# #        print("Developers in the target project:")
# #        for un in p_dev.raw['actors']:
# #            self.pdev.append(un['name'].lower())
# #
# #        self.getVersions()
# 
#     def jiraInit(self):
#         from jira import JIRA
#         auth = (self.user, self.__pw)
#         jopt = {'verify': 0}
#         self.jac = JIRA(self.host, auth=auth, options=jopt)
# 
#     def jiraGetIssueTypes(self, jira_session, project):
#         jra = jira_session.project(project)
#         types = {}
#         for it in jra.issueTypes:
#             types[it.name] = it.id
#         return types
# 
#     def jiraGet(self, session, host, request):
#         return session.get(host + request, verify=False)
# 
#     def isUser(self, user):
#         u = self.searchUser(user)
#         if u:
#             return True
#         else:
#             return False
# 
#     def searchUser(self, user):
#         return self.jac.search_users(user)
# 
#     def searchProject(self, term):
#         all_projects = self.jac.projects()
#         projects = []
#         for prj in all_projects:
#             if term.lower() in prj.name.lower():
#                 projects.append(prj)
#         return projects
# 
#     def addUserToWorkingProject(self, user_id, role='pDevelopers'):
#         try:
#             rid = self.jac.project_roles(self.work_prj)[role]['id']
#         except:
#             print("No role %s in project" % role)
#             return None
# 
#         role = self.jac.project_role(self.work_prj, rid)
# 
#         return role.add_user({'user': [user_id]})
# 
#     def setWorkingProject(self, project):
#         self.work_prj = project
#         self.roles = self.jac.project_roles(self.work_prj)
# 
#     def getVersions(self):
#         if not self.work_prj:
#             raise Exception("No project defined")
# 
#         jra = self.jac.project(self.work_prj)
#         self.versions = {}
# 
#         for i in range(len(jra.versions)):
#             v = jra.versions[i]
#             self.versions[v.name] = v.id
# 
#     def checkVersion(self, version):
#         if version in self.versions:
#             return True
#         else:
#             return False
# 
#     def addVersion(self, version):
#         if not self.work_prj:
#             raise Exception("No project defined")
# 
#         v = self.jac.create_version(version, self.work_prj)
#         self.versions[version] = v.id
# 
#     def readCase(self, case):
#         self.last_issue = case
#         case = self.jac.issue(case)
#         return case
# 
#     def printCase(self, case):
#         self.last_issue = case
#         case = self.readCase(case)
# 
#         fields = case.raw['fields']
# 
#         for k in fields:
#             if fields[k]:
#                 print(k + fields[k])
# 
#     def getCloneFields(self, case):
#         if not self.work_prj:
#             raise Exception("No project defined")
# 
#         self.last_issue = case
#         case = self.readCase(case)
#         fields = case.raw['fields']
#         clone = {}
#         for k in fields:
#             if fields[k] and k not in self.__del_entr:
#                 clone[k] = fields[k]
# 
#         clone['project'] = self.work_prj
# 
#         assignee = fields['assignee']['name']
#         print("assignee %s" % (assignee))
#         if self.isUser(assignee):
#             clone['assignee'] = {'name': assignee}
#         else:
#             clone['assignee'] = {'name': getpass.getuser()}
# 
#         reporter = fields['reporter']['name']
#         print("reporter %s" % (reporter))
#         if self.isUser(reporter):
#             self.reporter = {'name': reporter}
#         else:
#             self.reporter = False
# 
#         # Check if versions already exist in project and create if not
#         if 'versions' in clone:
#             versions = []
#             for i in range(len(clone['versions'])):
#                 vname = clone['versions'][i]['name']
#                 if not self.checkVersion(vname):
#                     self.addVersion(vname)
#                 versions.append({'name': vname})
#             clone['versions'] = versions
#         if 'fixVersions' in clone:
#             fixversions = []
#             for i in range(len(clone['fixVersions'])):
#                 vname = clone['fixVersions'][i]['name']
#                 if not self.checkVersion(vname):
#                     self.addVersion(vname)
#                 fixversions.append({'name': vname})
#             clone['fixVersions'] = fixversions
# 
#         return clone
# 
#     def createClone(self, issue, add_comments=False):
#         self.last_issue = issue
# 
#         original_issue = self.readCase(issue)
# 
#         issue_fields = original_issue.raw['fields']
# 
#         self.clone_fields = self.getCloneFields(issue)
# 
#         new_issue = self.jac.create_issue(fields=self.clone_fields)
# 
#         # copy attachments:
#         for a in issue_fields['attachment']:
#             attatchment = self.jac.attachment(a['id'])
#             self.jac.add_attachment(new_issue,
#                                     attatchment.get(),
#                                     attatchment.filename)
# 
#         # copy comments:
#         if add_comments:
#             for c in issue_fields['comment']['comments']:
#                 self.jac.comment(issue, c['id'])
#                 cmd = self.jac.add_comment(new_issue, c['body'])
# 
#         # add link to original issue:
#         self.jac.create_issue_link('clones', new_issue, original_issue)
# 
#         return new_issue
# 
#     def getProjectRoles(self, project=None, full=False):
#         if project:
#             if full:
#                 return self.jac.project_roles(project)
#             else:
#                 return list(self.jac.project_roles(project).keys())
#         elif self.work_prj:
#             if full:
#                 return self.roles
#             else:
#                 return list(self.roles.keys())
#         else:
#             raise Exception("No project defined")
# 
#     def getProjectUser(self, project=None, role=None, full=False):
#         prj = None
#         if project:
#             prj = project
#             roles = self.jac.project_roles(prj)
#         elif self.work_prj:
#             prj = self.work_prj
#             roles = self.roles
#         else:
#             raise Exception("No project defined")
# 
#         user = []
#         if role:
#             if role in roles.keys():
#                 rid = roles[role]['id']
#     #            role_desc = self.jac.project_role(prj, rid)
#                 user = [(x.name, x.displayName) for x in self.jac.project_role(prj, rid).actors]
#             else:
#                 raise Exception("Role %s does not exist in project %s" % (role, prj))
#         else:
#             for role in roles.keys():
#                 rid = roles[role]['id']
#                 user += [(x.name, x.displayName) for x in self.jac.project_role(prj, rid).actors]\
# 
#         x = {}
#         for u in user:
#             if '(' in u[1]:
#                 x[u[0]] = u[1]
#             else:
#                 print("%s: %s" % (u[0], u[1]))
# 
#         return x
# 
# 
# # %% Main
# if __name__ == "__main__":
#     # execute only if run as a script
# 
# =============================================================================