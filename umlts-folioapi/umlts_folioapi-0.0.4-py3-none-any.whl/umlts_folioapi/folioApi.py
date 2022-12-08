#!/usr/bin/python

# Python version of mda515t\folio\Folioapi3 php class
# from mst but with Request sessions
import time
from requests import Session
from getpass import getpass
import uuid
import configparser
import json

# FolioApi class
class FolioApi():

    # Class Variables
    namespace = uuid.UUID('8405ae4d-b315-42e1-918a-d1919900cf3f')

    okapi_token = ''
    tenant = ''
    okapi_url = ''
    
    default_headers = {
        'x-okapi-tenant': tenant,
        'x-okapi-token': okapi_token
    }

    timeout = 10
    retries = 10
    retryMultiplier = 1.5
    lastQuery = ''
    lastCode = ''
    lastResponse = ''
    session = Session()
    #### Class Methods ####

    # Constructor method
    def __init__(self, filepath: str='src/config/config.ini'):
        self.setupConfig(filepath)
        if not self.okapi_token:
            _okapi_token = self.getToken()
            self.setToken(_okapi_token)
            self.updateConfig(filepath, 'folioapi', 'okapi_token', _okapi_token)

    def setupConfig(self, filepath: str):
        config = configparser.ConfigParser()
        config.read(filepath)
        self.okapi_token = config.get("folioapi", "okapi_token")
        self.tenant = config.get("folioapi", "tenant")
        self.okapi_url = config.get("folioapi", "okapi_url")
        self.default_headers = {
            'x-okapi-tenant': self.tenant,
            'x-okapi-token': self.okapi_token
        }
        self.session.headers.update(self.default_headers)
        
    def updateConfig(self, file, section, system, value):
        config = configparser.ConfigParser()
        config.read(file)
        cfgfile = open(file, 'w')
        config.set(section, system, value)
        config.write(cfgfile)
        cfgfile.close()

    def preStage(self, endpoint):
        self.getToken()
        self.lastQuery = ''
        self.lastCode = ''
        self.lastResponse = ''
        self.lastHeaders = []
        return str(endpoint).strip('/')

    def _delete(self, endpoint, id):
        try:
            endpoint = self.preStage(endpoint)
            url = self.okapi_url + str(endpoint) + "/" + str(id)
            print("DELETE url: " + url)
            response = self.session.delete(url, headers=self.default_headers)
            if response:
                if response.status_code == 204:
                    print("Deleted successfully")
                if response.content:
                    return json.loads(response.content)
                else:
                    return None
            else:
                print("No Response")
        except Exception as e:
            print(e)

    def get(self, endpoint, params=[], id=None):
        try:
            endpoint = self.preStage(endpoint)
            p = ''
            if params:
                p='?'
                for param in params:
                    p = p + str(param) + "=" + str(params[param]) + "&"
                p = p[0:-1]
            
            if id:
                endpoint = endpoint + "/" + str(id)
            endpoint = endpoint + p
            url = self.okapi_url + endpoint
            # print("GET url: " + url)
            response = self.session.get(url)
            if response:
                return json.loads(response.content)
            else:
                print("No Response")
        except Exception as e:
            print(e)

    def _post(self, endpoint, data=[], options=[]):
        try:
            endpoint = self.preStage(endpoint)
            url = self.okapi_url + endpoint
            headers = self.default_headers
            print("POST url: " + url)

            if data:
                print("data: " + str(data))

            if options:
                print("options: " + str(options))
                if 'headers' in options:
                    h = options['headers']
                    for key in h:
                        print(key + ": " + h[key])
                        headers[key] = h[key]
            print("headers: " + str(headers))
            response = self.session.post(url, headers=headers, json=data)
            if response:
                if response.status_code == 204:
                    print("Response code: 204 OK")
                if response.content:
                    return json.loads(response.content)
                else:
                    return None
            else:
                print("No Response")
        except Exception as e:
            print(e)

    def setToken(self, token):
        self.okapi_token = token
        
    def getToken(self):
        if self.okapi_token:
            return self.okapi_token
        else:
            try:
                username = input("Username?: ")
                password = getpass()
                payload = {
                    "tenant": self.tenant,
                    "username": username,
                    "password": password
                }
                url = self.okapi_url + "/authn/login"
                headers = {
                    "Content-type": "application/json",
                    "X-Okapi-Tenant": self.tenant
                }
                resp = self.session.post(url, headers=headers, json=payload)

                okapi_token = resp.headers['x-okapi-token']
                print(okapi_token)
                return okapi_token
            except Exception as e:
                print("Error: Could not get token.")

    def newFileDefinition(self, filename: str):
        try:
            payload = {}
            payload['fileName'] = filename
            response = self.post('/data-export/file-definitions', data=payload)
            if response:
                return response
            else:
                return None
        except Exception as e:
            print(e)


    def uploadFileDefinition(self, filename: str, fileDefinitionId):
        try:
            options = {}
            options['headers'] = {
                'Content-type': 'application/octet-stream'
            }
            with open(filename, 'r') as file:
                lines = file.read()
            response = self.post('/data-export/file-definitions/' + fileDefinitionId + '/upload', data=lines, options=options)
            if response:
                return response
            else:
                return None
        except Exception as e:
            print(e)
        pass


    def getJobExecutionById(self, jobExecutionId):
        try:
            options = {}
            options['query'] = '(id==' + str(jobExecutionId) + ')'
            response = self.get('/data-export/job-executions', params=options)
            if response:
                return response
            else:
                return None
        except Exception as e:
            print(e)

    ### getMarcRecordIdentifiers: 
    # Returns a list of recordIds returned by MARC Search Query API (see payload)
    def getMarcRecordIdentifiers(self, leaderSearch=None, fieldsSearch=None, offset=0, limit=10):
        recordIds = []
        url = F"{self.okapi_url}source-storage/stream/marc-record-identifiers"
        if leaderSearch and not fieldsSearch:
            payload = {
                "leaderSearchExpression": leaderSearch,
                "limit": limit,
                "offset": offset
            }
        elif fieldsSearch and not leaderSearch:
            payload = {
                "fieldsSearchExpression": fieldsSearch,
                "limit": limit,
                "offset": offset
            }
        elif fieldsSearch and leaderSearch:
            payload = {
                "leaderSearchExpression": leaderSearch,
                "fieldsSearchExpression": fieldsSearch,
                "limit": limit,
                "offset": offset
            }
        else:
            print("1 or more of leaderSearch or fieldsSearch must be provided.")
            return
        headers = self.default_headers
        headers['Content-type'] = 'application/json'
        try:
            # POST request to /marc-record-identifiers to get back an array of record uuids
            response = self.session.post(url, headers=headers, json=payload)
            if response.ok:
                records = response.json()
                total_count = records['totalCount']
                print("Records returned: " + str(total_count))
                recordIds.extend(records['records'])
                offset += limit
                while offset <= total_count:
                    print("offset: " + str(offset) + "/" + str(total_count))
                    payload['offset'] = offset
                    response = self.session.post(url, headers=headers, json=payload)
                    if response.ok:
                        records = response.json()
                        recordIds.extend(records['records'])
                        offset += limit
            return recordIds
        except Exception as e:
            print(e)
            time.sleep(5)

    def getLocationInstanceIds(self, loc_uuid, get_only_unsuppressed=True): # returns list of instanceIds for given location (loc_uuid)
        offset = 0
        limit = 250
        instanceIds = []
        instanceIdsFin = []
        # GET all holdings records from a location and grab their instanceIds
        if get_only_unsuppressed:
            query = 'discoverySuppress==false and effectiveLocationId==' + loc_uuid
        else:
            query = 'effectiveLocationId==' + loc_uuid
        url = F"{self.okapi_url}/holdings-storage/holdings?offset=" + str(offset) + "&limit=" + str(limit) + "&query=(" + query + ")"
        try:
            response = self.session.get(url, headers=self.default_headers)
            if not response.ok:
                print(response.reason)
                print(response.text)
            if response.ok:
                holdings_records = response.json()
                # logging.info(holdings_records)
                total_records = holdings_records['totalRecords']
                print("# of records for location " + str(loc_uuid) + ": " + str(total_records))
                print("API calls to get all items: " + str(int(total_records / limit) + 1) + "...")
                for record in holdings_records['holdingsRecords']:
                    instanceIds.append(record['instanceId'])
                # logging.info(instanceIds)
                offset += limit
                while offset <= total_records:
                    # print("------> offset: " + str(offset))
                    url = F"{self.okapi_url}/holdings-storage/holdings?offset=" + str(offset) + "&limit=" + str(limit) + "&query=(" + query + ")"
                    response = self.session.get(url, headers=self.default_headers)
                    if not response.ok:
                        print(response.reason)
                        print(response.text)
                    if response.ok:
                        holdings_records = response.json()
                        for record in holdings_records['holdingsRecords']:
                            instanceIds.append(record['instanceId'])
                        offset += limit
                # logging.info(str(len(instanceIds)))
                return instanceIds
        except Exception as e:
            print(e)
            time.sleep(5)

    def getInstancebyId(self, instance_uuid): # returns Instance Json object
        # GET instance JSON from FOLIO
        url = F"{self.okapi_url}instance-storage/instances/" + instance_uuid
        payload = ''
        try:
            response = self.session.get(url, headers=self.default_headers, data=payload)
            if not response.ok:
                print(response.reason)
                print(response.text)
            if response.ok:
                response_json = response.json()
                return(response_json)
        except Exception as e:
            print(e)
            time.sleep(5)
    

    def quickExport(self, recordUuids): # recordUuids is a list of records to export. Returns a jobExecutionId (uuid)
        # POST request to /data-export/quick-export to get jobExecutionId with list of record uuids as part of request body
        url = F"{self.okapi_url}data-export/quick-export"
        payload = {
            "uuids": recordUuids,
            "type": "uuid",
            "recordType": "INSTANCE"
        }
        headers = {
            'x-okapi-tenant': self.tenant,
            'x-okapi-token': self.okapi_token,
            'Content-type': 'application/json'          
        }
        try:
            response = self.session.post(url, headers=headers, json=payload)
            response_json = response.json()
            print(response_json)
            jobId = response_json['jobExecutionId']

            return jobId
        except Exception as e:
            print(e)
            time.sleep(5)

    def getHoldingsByInstanceId(self, instance_id): # Returns an array of Holdings json records
        query = '?query=(instanceId=="' + instance_id + '")'
        url = F"{self.okapi_url}holdings-storage/holdings" + query
        try:
            response = self.session.get(url, headers=self.default_headers)
            holdingsRecords = response.json()['holdingsRecords']
            
            return holdingsRecords
        except Exception as e:
            print(e)
            time.sleep(5)

    def dumpHoldings(self, offset=0, limit=10):
        url = F"{self.okapi_url}holdings-storage/holdings"
        try:
            response = self.session.get(url, headers=self.default_headers)
            holdingsRecords = response.json()

            return holdingsRecords
        except Exception as e:
            print(e)
            time.sleep(5)

    def postFileDefinition(self, filename):
        url = self.okapi_url + "/data-export/file-definitions"
        payload = {
            "fileName": filename
        }
        ### send POST request to /data-export/file-definitions with payload containing csv filename
        try:
            response = self.session.post(url, headers=self.default_headers, json=payload)
            fileDefinition = response.json()

            return fileDefinition
        except Exception as e:
            print(e)
            time.sleep(5)

    def uploadFile(self, fileDefId, fileObject): # the list of uuids is one per line with '\n' separating each record
        ### send POST request to /data-export/file-definitions/{fileDefinitionId}/upload
        url = self.okapi_url + "/data-export/file-definitions/" + str(fileDefId) + "/upload"
        headers = self.default_headers
        headers['Content-type'] = 'application/octet-stream'
        try:
            response = self.session.post(url, headers=headers, data=fileObject)
            response_json = response.json()

            return response_json
        except Exception as e:
            print(e)
            time.sleep(5)

    def startExport(self, jobProfileId, fileDefinitionId, idType="instance"): # idType enum: {"instance", "holding", }
        ### send POST request to /data-export/export with json body
        url = self.okapi_url + "data-export/export"
        payload = {
            "jobProfileId": jobProfileId,
            "fileDefinitionId": fileDefinitionId,
            "idType": idType
        }
        try:
            response = self.session.post(url, headers=self.default_headers, json=payload)
            if not response.ok:
                print(response.reason)
                print(response.text)
            if response.status_code == 204:
                print("Success")
        except Exception as e:
            print(e)
            time.sleep(5)
        pass


    def getLocations(self, limit=500):
        try:
            url = F"{self.okapi_url}/locations"
            params ={}
            params['limit'] = limit
            resp = self.session.get(url, headers=self.default_headers, params=params)
            if resp:
                if resp.ok:
                    return resp.json()
            else:
                return None
        except Exception as e:
            print(e)

    def searchInstances(self, query='cql.allRecords=1', expandAll=True, offset=0, limit=10):
        try:
            url = self.okapi_url + '/search/instances'
            params = {}
            params['query'] = query
            params['expandAll'] = expandAll
            params['offset'] = offset
            params['limit'] = limit
            resp = self.session.get(url, headers=self.default_headers, params=params)
            if resp:
                if resp.status_code == 200:
                    return resp.json()
        except Exception as e:
            print(e)

    def getInstanceIds(self, query):
        try:
            url = self.okapi_url + "/search/instances/ids"
            params = {}
            params['query'] = query
            resp = self.session.get(url, headers=self.default_headers, params=params)
            if resp:
                print(str(resp.status_code))
                if resp.status_code == 200:
                    return resp.json()
        except Exception as e:
            print("getInstanceIds() Exception")
            print(e)

### getHoldingsIds: Get a list of holding ids linked to instances found by the CQL query
##    Parameters: query <required>: A CQL query string with search conditions.
    def getHoldingIds(self, query: str):
        try:
            url = self.okapi_url + '/search/holdings/ids'
            params = {}
            params['query'] = query
            resp = self.session.get(url, headers=self.default_headers, params=params)
            if resp:
                if resp.status_code == 200:
                    return resp.json()
        except Exception as e:
            print(e)

    ### Gets all locations and returns them as an array of json Objects
    def getAllLocations(self):
        try:
            # Get all locations and store as object
            resp = self.session.get(F"{self.okapi_url}/locations?limit=99999", headers=self.default_headers)
            locations = resp.json()['locations']
            return locations
        except Exception as e:
            print(e)