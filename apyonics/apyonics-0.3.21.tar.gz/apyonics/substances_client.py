import json
import os

import requests
import pandas as pd

class SubstancesClient(object):
    """Client for working with substances.

    This client manages the back-end substance data
    that are shared across all Aionics instances.
    To manage the substance tables on a specific instance,
    use the apyonics.client.Client class.
    """ 

    def __init__(self,service_url='',api_key=''):
        """Client initializer.

        Default credentials are read in from a file,
        $HOME/.aionics_substances_key, if available.
        This file should have the service URL on line 1,
        and the API key on line 2.
        Initialization arguments take precedence over key file entries. 

        Parameters
        ----------
        service_url : str
            Web URL pointing to an Aionics substances application
        api_key : str
            API authorization key for the application 
        """
        super(SubstancesClient,self).__init__()

        if not service_url or not api_key:
            if service_url:
                raise RuntimeError('An api_key is required')
            if api_key:
                raise RuntimeError('A service_url is required')
            homedir = os.path.expanduser('~')
            hostfile = os.path.join(homedir,'.aionics_substances_key')
            with open(hostfile,'r') as f:
                service_url = str(f.readline().strip())
                api_key = str(f.readline().strip())
        if not service_url[-1] == '/': service_url = service_url + '/'

        connect_url = service_url+'connect_client'
        sess = requests.Session()
        resp = sess.post(connect_url,headers={'x-api-key':api_key})
        if resp.status_code == 200:
            resp = resp.json()
            if resp['success']:
                self.service_url = service_url
                self.api_key = api_key
                self.session = sess
            else: 
                raise ConnectionError('connection unsuccessful: {}'.format(resp))
        else:
            raise RuntimeError('failed to connect to {} ({})'.format(service_url,resp.status_code))

    # SUBSTANCES

    def add_substance(self,name,source='',other_names=[],descriptors={},properties={},documents={}):
        """Add a Substance to the database.

        See documentation for apyonics.client.Client.add_substance().
        """
        resp = self.session.post(
            self.service_url+'add_substance', 
            headers={'x-api-key':self.api_key},
            json={
                'name':name,
                'descriptors':descriptors,
                'properties':properties,
                'documents':documents,
                'source':source,
                'other_names':other_names
            }
        )
        if resp.status_code == 200:
            respdata = resp.json()
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}

    def update_substance(self,name,source='',other_names=[],
            descriptors={},properties={},documents={},
            remove_other_descriptors=False,
            remove_other_properties=False,
            remove_other_documents=False
        ):
        """Update the attributes of an existing substance.

        See docs for apyonics.client.Client.update_substance().
        """
        resp = self.session.post(
            self.service_url+'update_substance', 
            headers={'x-api-key':self.api_key},
            json={
                'name':name,
                'source':source,
                'other_names':other_names,
                'descriptors':descriptors,
                'properties':properties,
                'documents':documents,
                'remove_other_descriptors':remove_other_descriptors,
                'remove_other_properties':remove_other_properties,
                'remove_other_documents':remove_other_documents
            }
        )
        if resp.status_code == 200:
            respdata = resp.json()
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}


    # DESCRIPTORS

    def check_substance_names(self,names):
        """Check for existence of substances by name.

        See documentation for apyonics.client.Client.check_substance_names().
        """
        resp = self.session.get(
            self.service_url+'check_substance_names', 
            headers={'x-api-key':self.api_key},
            json={'names':names}
        )
        if resp.status_code == 200:
            respdata = resp.json()
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_substance_data(self,name):
        """Get all data for a substance by providing a substance name.

        See documentation for apyonics.client.Client.get_substance_data().
        """
        resp = self.session.get(
            self.service_url+'download_substance', 
            headers={'x-api-key':self.api_key},
            json={
                'name':name
            }
        )
        if resp.status_code == 200:
            respdata = {'success':True,'data':resp.json()}
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_descriptors(self,substance_names,descriptor_names=[]):
        """Get substance descriptors by providing substance names.

        See documentation for apyonics.client.Client.get_descriptors().
        """
        resp = self.session.post(
            self.service_url+'get_descriptors', 
            headers={'x-api-key':self.api_key},
            json={
                'substance_names':substance_names
            }
        )
        if resp.status_code == 200:
            respdata = resp.json()
            ddf = pd.DataFrame.from_dict(respdata['descriptors'],orient='index')
            if descriptor_names:
                descnms = [descnm for descnm in descriptor_names if descnm in ddf.columns]
                ddf = ddf[descnms].copy()
                for subsnm in respdata['descriptors'].keys():
                    respdata['descriptors'][subsnm] = ddf.loc[subsnm].to_dict()
            respdata['descriptor_table'] = ddf
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}

