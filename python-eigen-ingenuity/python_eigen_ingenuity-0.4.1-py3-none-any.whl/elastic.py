"""Eigen Ingenuity - Elasticsearch

This package deals with the Eigen Ingenuity Elasticsearch database.

To retrieve an AssetObject use matchNode, or execute a custom cypher query with 

  from eigeningenuity.assetmodel import matchNode
  from time import gmtime, asctime

  nodes = matchNodes("code","System_")
  
  for node in nodes:
      code = node.code
      print(code)  
"""

from eigeningenuity import EigenServer
from urllib.parse import quote as urlquote
from eigeningenuity.historian import get_historian
from eigeningenuity.util import is_list,force_list,_do_eigen_json_request,EigenException
from eigeningenuity.core import get_default_server
import pandas as pd
import datetime as dt
import json
import requests
from requests.exceptions import ConnectionError
from urllib.error import URLError

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class ElasticConnection (object):
    """An elasticsearch instance which talks the Eigen elastic endpoint.
    """

    def __init__(self, baseurl):
       """This is a constructor. It takes in a URL like http://infra:8080/ei-applet/search/"""
       self.baseurl = baseurl

    def _doJsonRequest(self,cmd,params):
        url = self.baseurl + "?cmd=" + urlquote(cmd)
        print(url)
        return _do_eigen_json_request(url,**params)

    def _testConnection(self):
        """Preflight Request to verify connection to ingenuity"""
        try:
            status = requests.get(self.baseurl).status_code
            if status != 200:
                raise ConnectionError(
                    "Invalid API Response from " + self.baseurl + ". Please check the url is correct and the instance is up.")
        except (URLError, ConnectionError):
            raise ConnectionError ("Failed to connect to ingenuity instance at " + self.baseurl + ". Please check the url is correct and the instance is up.")

    def executeRawQuery(self,index:str, query:str, instance:str = "elasticsearch-int", output:str = "json", filepath:str = None):
        """Executes a raw cypher query against Elastic.

        Args:
            index: The elasticsearch index to query
            query: The body of the query
            instance: (Optional) The instance of elasticsearch to query. Defaults to elasticsearch-int
            output: (Optional) The format in which to return the data. Accepts one of: "raw" - The raw json returned by the API; "json" - A processed version of the json response; "df" - A formatted pandas dataframe object; "file" - Writes the response to a .json file in the local directory. Defaults to "json"
            filepath: (Optional) Name and path to the .json file that will be created/overwritten. If omitted, will create a file in the current directory with a generated name. Has no effect unless output is "file".
            
        Returns:
            Elasticsearch API response to the query, the format is dependent on the output parameter
        """
        self._testConnection()
        validOutputTypes = ["raw", "json", "df", "file"]
        if output not in validOutputTypes:
            raise ValueError("output must be one of %r." % validOutputTypes)
        args = {}
        args["clientname"] = instance
        args["index"] = index
        args["search"] = query

        response = self._doJsonRequest("DODIRECTSEARCH", args)

        if output == "raw":
            return response
        elif output == "json":
            return response['results']
        elif output == "df":
            return pd.json_normalize(response['results'])
        elif output == "file":
            if filepath is None:
                filepath = "eigenElasticResponse-" + index + "-" + str(dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
            with open(filepath + ".json", "w") as f:
                f.write(json.dumps(response, indent=4))


def get_elastic(eigenserver:EigenServer = None):
    """Instantiate an elasticsearch connection for the given EigenServer.

    Args:
        eigenserver: (Optional) An EigenServer Object linked to the ingenuity url containing the elasticsearch. Can be omitted if environmental variable "EIGENSERVER" exists and is equal to the Ingenuity base url

    Returns:
        An Object that can be used to query elasticsearch data from the ingenuity.
    """
    if eigenserver is None:
        eigenserver = get_default_server()
    return ElasticConnection(eigenserver.getEigenServerUrl() + "ei-applet/search")