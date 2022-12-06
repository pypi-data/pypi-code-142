import uuid
import json
import time
import os
import zipfile

import requests
import pandas as pd
import numpy as np
from io import BytesIO, StringIO

class Client(object):

    def __init__(self,service_url='',username='',api_key=''):
        """Client initializer.

        Default credentials are read in from a file,
        $HOME/.aionics_key, if available.
        This file should have the service URL on line 1,
        the username on line 2,
        and the API key on line 3.
        Initialization arguments take precedence over key file entries. 

        Parameters
        ----------
        service_url : str
            Web URL pointing to your Aionics service
        username : str
            Username for your account on the Aionics service
        api_key : str
            API authorization key for your account on the Aionics service
        """
        super(Client,self).__init__()

        if not service_url or not username or not api_key:
            if service_url:
                raise RuntimeError('A username and api_key are required')
            if username:
                raise RuntimeError('A service_url and api_key are required')
            if api_key:
                raise RuntimeError('A service_url and username are required')
            homedir = os.path.expanduser('~')
            hostfile = os.path.join(homedir,'.aionics_key')
            with open(hostfile,'r') as f:
                service_url = str(f.readline().strip())
                username = str(f.readline().strip())
                api_key = str(f.readline().strip())
        if not service_url[-1] == '/': service_url = service_url + '/'

        connect_url = service_url+'api/connect_client'
        sess = requests.Session()
        resp = sess.post(connect_url,headers={'username':username,'x-api-key':api_key})
        if resp.status_code == 200:
            resp = resp.json()
            if resp['success'] and (resp['response'] == 'connected to Aionics'):
                self.service_url = service_url
                self.username = username 
                self.api_key = api_key
                self.session = sess
            else: 
                raise ConnectionError('connection unsuccessful: {}'.format(resp))
        else:
            raise RuntimeError('failed to connect to {} ({})'.format(service_url,resp.status_code))

    # GENERIC GET/POST JSON

    def get_json(self,method,url,json):
        resp = self.session.get(url,json=json)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def post_json(self,url,json):
        resp = self.session.post(url,json=json)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}


    # DESCRIPTORS

    def get_descriptors(self,substance_names,descriptor_set='all',include_properties=False):
        """Get substance descriptors by providing substance names.

        Descriptors are looked up and returned for all substance names
        that are found in Aionics' substances database.
        Substance names that are not found in the database 
        are dropped from the table of results.

        This function returns a process id that can be used
        to track the progress of the computation and, 
        when finished, fetch the results.

        Parameters
        ----------
        substance_names : list
            List of names (strings) of each substance to be looked up.
        descriptor_set : str
            Specifies a descriptor subset. 
            By default, all available descriptors are returned.
            The most common choices are 'all' or 'rdkit_universal'.
            The 'all' descriptor set includes all available descriptors.
            The 'rdkit_universal' descriptor set includes only rdkit descriptors
            that are real-valued across most available substances.
            To see all available descriptor sets, log in by web browser
            and examine the featurization step of a modeling pipeline.
        include_properties : bool
            Flag for including substance properties in the featurization.    

        Returns
        -------
        response : dict
            Dict containing status report and process id. 
            The process id is used to check the progress
            and to fetch the results after it is finished.
        """
        #pid_resp = self.session.get(
        #    self.service_url+'process_id', 
        #    data={'process_tag':'DESCRIPTORS'+uuid.uuid4().hex}
        #)
        procid = pid_resp.json()['process_id']
        resp = self.session.post(
            self.service_url+'api/get_descriptors', 
            json={
                'substance_names':substance_names,
                'descriptor_set':descriptor_set,
                'process_id':procid,
                'include_properties':include_properties
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def compute_descriptors(self,featurization,source_data={},file_paths={},structure_random_seed=None,return_files=False,structure_sample_size=100):
        """Compute substance descriptors by providing substance source data.

        Descriptors are computed for each entry in source_data or file_paths,
        depending on which featurization is selected.
        The source_data values should be SMILES string (for 'rdkit' featurization).
        The files in file_paths are uploaded to Aionics.
        This is expected to work for ICSD CIF files,
        CIF files generated by pymatgen or VESTA, 
        or POSCAR files.

        This function returns a process id that can be used
        to track the progress of the computation and, 
        when finished, fetch the results.

        Parameters
        ----------
        featurization : str
            Specifies which featurization to apply. 
            This should be 'lithium_ionic', 'anion_redox', or 'rdkit'.
            The 'anion_redox' option is disabled by default 
            (only specific instances of the application are allowed to use it).
        source_data : dict 
            Dict of source data (SMILES strings) for 'rdkit' featurization.
            The keys of this dict are used to index
            the returned table of descriptors.
        file_paths : dict 
            Dict of file paths containing substance data
            for 'lithium_ionic' or 'anion_redox' featurization.
            Each path is opened and uploaded to Aionics.
            The keys of this dict are used to index
            the returned table of descriptors.
        structure_random_seed : int
            Integer seed used for the random number generator
            that is used to sample packing fractions 
            and site occupancies
            for 'lithium_ionic' or 'anion_redox' featurization.
        structure_sample_size : int
            Number of structures to sample 
            for structures with fractionally occupied sites,
            for 'lithium_ionic' or 'anion_redox' featurization.
        return_files : bool
            If True, a zip file is returned containing 
            descriptors as a .csv file
            and all sampled structures as POSCAR files,
            for 'lithium_ionic' or 'anion_redox' featurization.

        Returns
        -------
        response : dict
            Dict containing status report and file tag. 
            The results can be fetched by file tag
            via client.download_descriptor_results()
            after the process is finished.
        """
        if featurization in ['lithium_ionic','anion_redox']:
            resp = self.session.post(
                self.service_url+'api/compute_descriptors', 
                data={
                    'featurization':featurization,
                    'structure_random_seed':structure_random_seed,
                    'structure_sample_size':structure_sample_size,
                    'return_files':return_files
                },
                files={nm:open(fp,'rb') for nm,fp in file_paths.items()}
            )
        elif featurizaton == 'rdkit':
            resp = self.session.post(
                self.service_url+'api/compute_descriptors', 
                data={
                    'featurization':featurization,
                    'source_data':source_data
                },
            )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def download_descriptor_results(self,file_tag,wait=False,wait_interval=3.,output_path=None):
        """Get status or results of a descriptor process.

        This is used to download the results of a call to
        get_descriptors() or compute_descriptors().
        If the process is finished, the results are returned.
        If the process is not finished and wait==False,
        a progress report is returned.
        If the process is not finished and wait==True,
        The client checks periodically until the process is finished,
        and then the results are returned.

        Parameters
        ----------
        file_tag : str 
            The tag of the output file assigned to the descriptor computation.
            This is returned as part of the compute_descriptors() response.
        wait : bool
            Specifies whether or not to wait for the file to show up. 
            If wait==False and the file is not present,
            the response will indicate a missing file.
        wait_interval : float
            If wait==True, this is the time delay (in seconds)
            between attempts to check for the file. 
            The interval must be at least one second.
            If a value less than 1 is provided, it is set to 1.
        output_path : str 
            If output_path is provided, apyonics attempts to save 
            the results to this path.

        Returns
        -------
        response : dict
            Dict containing either a report of process status or a table of results.
        """
        if wait_interval < 1: wait_interval = 1.
        n_waits = 0
        file_found = False
        while not file_found and wait: 
            # check for the file
            try:
                res = self.session.get(
                    self.service_url+'download_file',
                    json={'file_tag':file_tag}
                )
                data = res._content 
                file_found = bool(data)
            except Exception as ex:
                print('{}'.format(ex))
                n_waits += 1
                # gradually slow down status checks
                if np.mod(n_waits,100) == 0 and wait_interval < 30:
                    wait_interval += 1
                time.sleep(wait_interval)
        # we now presume the process to be finished, 
        # and the output file to be present
        try:
            if output_path:
                with open(output_path,'wb') as f:
                    f.write(data)
        except:
            return {'success':False,'error':'unable to download file'}
        zf = zipfile.ZipFile(BytesIO(data))
        data_df = None
        try:
            data_df = pd.read_csv(zf.open('descriptors.csv'),index_col='name')
        except:
            pass
        return {'success':True,'data_df':data_df,'data':data,'output_path':output_path}


    # DATASETS

    def get_dataset_index(self):
        """Download the index of available datasets.

        Returns
        -------
        response : dict
            Dict containing information about datasets available to the client.
        """
        resp = self.session.get(self.service_url+'api/dataset_index')
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def new_dataset(self,filepath,name,description='',table_name='',table_desc=''):
        """Create a new dataset on Aionics.

        The data for the dataset should be in .csv format.
        The .csv should include a header for column names.
        One column should be named "id", and should contain unique integers-
        if it is not present, it is added automatically after the upload.

        Parameters
        ----------
        filepath : str
            Path to a csv file on the local filesystem-
            this file defines the dataset's first table.
        name : str
            Name for the new dataset- must be unique.
        description : str
            Description of the new dataset.
        table_name : str
            Name for the dataset's first table-
            defaults to the dataset name if not provided 
        table_desc : str
            Description for the dataset's first table- 
            defaults to the dataset description if not provided 

        Returns
        -------
        response : dict
            Dict containing the new dataset id or an error report.
        """
        resp = self.session.post(
            self.service_url+'api/new_dataset',
            files={
                'dataset':open(filepath,'rb'),
                'metadata':json.dumps({
                    'name':name,
                    'description':description,
                    'table_name':table_name,
                    'table_description':table_desc,
                }).encode()
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_dataset_id(self,dataset_name):
        """Get the id of a dataset by providing its name.

        Parameters
        ----------
        dataset_name : str 
            Name of the desired dataset. 

        Returns
        -------
        response : dict 
            Response data or error report. 
        """
        resp = self.session.get(
            self.service_url+'api/get_dataset_id',
            params={'dataset_name':dataset_name}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_dataset(self,dataset_id):
        """Download a dataset from Aionics by providing its id.

        Parameters
        ----------
        dataset_id : int
            Integer index of the desired dataset.

        Returns
        -------
        response : dict 
            Response data or error report, 
            including the dataset table (as a pandas.DataFrame) if successful.
        """
        msg = 'Deprecation: get_dataset(dataset_id) is deprecated. '\
            'Use get_table(table_id) instead. '\
            'Use get_table_index(dataset_id) to get an index of tables '\
            'that are attached to the dataset.'\
            'Use get_table_id(table_name) to get the id of a table by name.'
        raise RuntimeError(msg)

    def get_table_index(self,dataset_id):
        resp = self.session.get(self.service_url+'api/table_index',json={'dataset_id':dataset_id})
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def new_table(self,dataset_id,filepath,name,description=''):
        """Create a new table under a dataset on Aionics.

        The data for the table should be in .csv format.
        The .csv should include a header for column names.
        One column should be named "id", and should contain unique integers-
        if it is not present, it is added automatically after the upload.

        Parameters
        ----------
        dataset_id : int
            Id of the dataset to associate with the new table.
        filepath : str
            Path to csv file containing table data on the local filesystem.
        name : str
            Name for the new table- must be unique. 
        description : str
            Description of the new table (optional).

        Returns
        -------
        response : dict
            Dict containing the new table id or an error report.
        """
        resp = self.session.post(
            self.service_url+'api/new_table',
            files={
                'table':BytesIO(open(filepath,'rb').read()),
                'metadata':json.dumps({
                    'dataset_id':dataset_id,
                    'name':name,
                    'description':description
                }).encode()
            },
            verify=False
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_table(self,table_id):
        resp = self.session.get(
            self.service_url+'api/download_table',
            params={'table_id':table_id}
        )
        if resp.status_code == 200:
            return {
                'success':True,
                'table':pd.read_csv(
                    StringIO(resp._content.decode()),
                    index_col='id'
                )
            }
        else:
            return {
                'success':False,
                'status_code':resp.status_code
            }

    def get_table_id(self,table_name):
        """Get the id of a table by providing its name.

        Parameters
        ----------
        table_name : str 
            Name of the desired table. 

        Returns
        -------
        response : dict 
            Response data or error report. 
        """
        resp = self.session.get(
            self.service_url+'api/get_table_id',
            params={'table_name':table_name}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def delete_dataset(self,dataset_id):
        """Delete a dataset from Aionics, permanently.

        Any Models or Designs built on the dataset
        will also be deleted permanently.

        Parameters
        ----------
        dataset_id : int
            Integer index of the dataset to delete.

        Returns
        -------
        resp : dict
            Report of success or failure in deleting the dataset.
        """
        resp = self.session.post(
            self.service_url+'api/delete_dataset', 
            json={'dataset_id':dataset_id}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def edit_dataset_metadata(self,dataset_id,name='',description=''):
        """Edit dataset metadata (name and description).

        Parameters
        ----------
        dataset_id : int
            Integer id of the dataset to be edited.
        name : str
            New name for the dataset being edited 
            (must be unique among datasets).
            If not provided, the name is not updated.
        description : str
            New description for the dataset being edited.
            If not provided, the description is not updated.

        Returns
        -------
        resp : dict
            Contains status report.
        """
        resp = self.session.post(
            self.service_url+'api/edit_dataset', 
            json={'dataset_id':dataset_id,'name':name,'description':description}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}


    # MODELS

    def get_model_index(self,dataset_id):
        """Download the index of available models for a given dataset.

        Parameters
        ----------
        dataset_id : int
            Id of the dataset for which the model index will be downloaded.

        Returns
        -------
        resp : dict
            Response containing a name-to-id map for models under the specified dataset.
        """
        resp = self.session.get(self.service_url+'api/model_index',json={'dataset_id':dataset_id})
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_model_id(self,model_name):
        """Get the id of a model by providing its name.

        Parameters
        ----------
        model_name : str 
            Name of the desired model. 

        Returns
        -------
        response : dict 
            Response data or error report. 
        """
        resp = self.session.get(
            self.service_url+'api/get_model_id',
            params={'model_name':model_name}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def new_model(self,table_id,name,description=''):
        """Create a new model on Aionics.

        Parameters
        ----------
        table_id : int 
            Id of the table that will be the model's training set. 
        name : str
            Name for the new model- must be unique across all models.
        description : str
            Description of the new model.

        Returns
        -------
        resp : object 
            Contains the new model's id or an error report
        """
        resp = self.session.post(
            self.service_url+'api/new_model',
            json={
                'table_id':table_id,
                'name':name,
                'description':description
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def delete_model(self,model_id):
        """Delete a model from Aionics, permanently.

        Any Designs that are configured to use the model
        will be rolled back to a state where the model
        has not yet been specified. 

        Parameters
        ----------
        model_id : int
            Integer id of the model to be deleted.

        Returns
        -------
        resp : dict
            Dict reporting success or failure in deleting the model.
        """
        resp = self.session.post(
            self.service_url+'api/delete_model', 
            json={'model_id':model_id}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def edit_model_metadata(self,model_id,name='',description=''):
        """Edit model metadata (name and description).

        Parameters
        ----------
        model_id : int
            Integer id of the model to be edited.
        name : str
            New name for the model being edited 
            (must be unique among models).
            If not provided, the name is not updated.
        description : str
            New description for the model being edited.
            If not provided, the description is not updated.

        Returns
        -------
        resp : dict
            Contains status report.
        """
        resp = self.session.post(
            self.service_url+'api/edit_model', 
            json={'model_id':model_id,'name':name,'description':description}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_model_settings(self,model_id,settings_key=None):
        """Get model creation settings or a selection thereof.

        Parameters
        ----------
        model_id : int
            Integer id of the model to be queried.
        settings_key : str
            Optional key for selecting a subset of the model settings,
            specific to one step of the model creation pipeline.
            Valid keys:

            - 'MODEL_CONFIG'
            - 'FEATURIZATION'
            - 'TRANSFORMATION'
            - 'FEATURE_SELECTION'
            - 'MODEL_TRAINING'

        Returns
        -------
        resp : dict
            Contains status report and, if successful, model settings.
        """
        resp = self.session.get(
            self.service_url+'model_settings', 
            params={'model_id':model_id,'settings_key':settings_key}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_model_results(self,model_id,results_key=None):
        """Get model creation results or a selection thereof.

        Parameters
        ----------
        model_id : int
            Integer id of the model to be queried.
        results_key : str
            Optional key for selecting a subset of the model results,
            specific to one step of the model creation pipeline.
            Valid keys:

            - 'MODEL_CONFIG'
            - 'FEATURIZATION'
            - 'TRANSFORMATION'
            - 'FEATURE_SELECTION'
            - 'MODEL_TRAINING'

        Returns
        -------
        resp : dict
            Contains status report and, if successful, model results.
        """
        resp = self.session.get(
            self.service_url+'model_results', 
            params={'model_id':model_id,'results_key':results_key}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}
        

    # DESIGNS

    def get_design_index(self,dataset_id):
        """Download the index of available designs for a given dataset.

        Parameters
        ----------
        dataset_id : int
            Id of the dataset for which the design index will be downloaded. 

        Returns
        -------
        resp : dict
            Response data including a name-to-id map for designs under the specified dataset. 
        """
        resp = self.session.get(self.service_url+'api/design_index',json={'dataset_id':dataset_id})
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_design_id(self,design_name):
        """Get the id of a design by providing its name.

        Parameters
        ----------
        design_name : str 
            Name of the desired design. 

        Returns
        -------
        response : dict 
            Response data or error report. 
        """
        resp = self.session.get(
            self.service_url+'api/get_design_id',
            params={'design_name':design_name}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def new_design(self,table_id,name,description=''):
        """Create a new design on Aionics.

        Parameters
        ----------
        table_id : int 
            Id of the table that will be the design's training set. 
        name : str
            Name for the new design- must be unique.
        description : str
            Description of the new design.

        Returns
        -------
        resp : object 
            Contains the new design's id or an error report.
        """
        resp = self.session.post(
            self.service_url+'api/new_design',
            json={
                'table_id':table_id,
                'name':name,
                'description':description
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def delete_design(self,design_id):
        """Delete a design from Aionics, permanently.

        Parameters
        ----------
        design_id : int
            Integer id of the design to be deleted.

        Returns
        -------
        resp : dict
            Dict reporting success or failure in deleting the design.
        """
        resp = self.session.post(
            self.service_url+'api/delete_design', 
            json={'design_id':design_id}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def edit_design_metadata(self,design_id,name='',description=''):
        """Edit design metadata (name and description).

        Parameters
        ----------
        model_id : int
            Integer id of the model to be edited.
        name : str
            New name for the model being edited 
            (must be unique among models).
            If not provided, the name is not updated.
        description : str
            New description for the model being edited.
            If not provided, the description is not updated.

        Returns
        -------
        resp : dict
            Contains status report.
        """
        resp = self.session.post(
            self.service_url+'api/edit_design', 
            json={'design_id':design_id,'name':name,'description':description}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_design_settings(self,design_id,settings_key=None):
        """Get design settings or a selection thereof.

        Parameters
        ----------
        design_id : int
            Integer id of the design to be queried.
        settings_key : str
            Optional key for selecting a subset of the design settings,
            specific to one step of the design pipeline.
            Valid keys:

            - 'DESIGN_CONFIG'
            - 'CANDIDATE_CONFIG'
            - 'SCREENING'

        Returns
        -------
        resp : dict
            Contains status report and, if successful, design settings.
        """
        resp = self.session.get(
            self.service_url+'design_settings', 
            params={'design_id':design_id,'settings_key':settings_key}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_design_results(self,design_id,results_key=None):
        """Get design results or a selection thereof.

        Parameters
        ----------
        design_id : int
            Integer id of the design to be queried.
        settings_key : str
            Optional key for selecting a subset of the design results,
            specific to one step of the design pipeline.
            Valid keys:

            - 'DESIGN_CONFIG'
            - 'CANDIDATE_CONFIG'
            - 'SCREENING'

        Returns
        -------
        resp : dict
            Contains status report and, if successful, design results.
        """
        resp = self.session.get(
            self.service_url+'design_results', 
            params={'design_id':design_id,'results_key':results_key}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}
        

    # MODELING PIPELINE
    
    def configure_model(self,model_id,output_key='none',scalar_columns=[],substance_columns=[]):
        """Perform model configuration: step 1 of the model creation pipeline.

        The goal of this step is to specify 
        how each column of the dataset will be handled.

        Parameters
        ----------
        model_id : int
            Integer id of the model being worked on.
        output_key : str
            Name of dataset column to be used as output, or 'none'.
            If 'none', the model can only be used for input space evaluation,
            e.g. for exploratory screening.
        scalar_columns : list
            List of names of columns that contain scalar inputs.
        substance_columns : list
            List of names of columns that contain substance names. 

        Returns
        -------
        resp : dict
            Contains status report.
        """
        resp = self.session.post(
            self.service_url+'configure_model', 
            json={
                'model_id':model_id,
                'output_key':output_key,
                'scalar_columns':scalar_columns,
                'substance_columns':substance_columns
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def run_featurization(self,model_id,settings):
        """Run featurization: step 2 of the model creation pipeline.

        The goal of this step is to collect substance descriptors 
        for all of the entries in the substance columns
        that were specified in the model configuration step.

        Parameters
        ----------
        model_id : int
            Integer id of the model being worked on.
        settings : dict
            The featurization configurations are provided here.
            The keys of this dict should be the names of the substance columns.
            The values are dicts of settings that specify 
            how substances in the column are to be featurized.
            Each substance can have the following settings:

            - 'featurization' (bool): Specifies whether or not the substance should be featurized. 
            - 'use_descriptors' (bool): Optional, default True. Includes any available descriptors in featurization. 
            - 'descriptor_set' (str): Descriptor subset (optional). See `get_descriptors()`.
            - 'concentration_weighted' (bool): Optional, default False. Multiplies the descriptors by substance concentrations. For a column named 'substance1', the concentration data is assumed to be in a column named 'substance1_conc'.
            - 'in_solution' (bool): Optional, default False. Substances in solution get their descriptors combined additively with the descriptors of other substances in the same solution.
            - 'solution_name' (str): If in_solution, specifies which solution the substance is in.
            - 'use_properties' (bool): Optional, default False. Includes any properties attached to the substance as descriptors for featurization. 

        Returns
        -------
        resp : dict
            Contains status report and, if successful,
            a process id for monitoring the featurization.
        """
        pid_resp = self.session.get(
            self.service_url+'model_process_id', 
            json={
                'model_id':model_id,
                'process_tag':'FEATURIZATION'
            }
        )
        procid = pid_resp.json()['process_id']
        data = {'model_id':model_id,'process_id':procid}
        for subsk,stgs in settings.items():
            data[subsk+'_featurization'] = stgs['featurization']
            if 'descriptor_set' in stgs:
                data[subsk+'_descset'] = stgs['descriptor_set']
            if 'concentration_weighted' in stgs:
                data[subsk+'_concwtd'] = stgs['concentration_weighted']
            if 'in_solution' in stgs:
                data[subsk+'_insoln'] = stgs['in_solution']
            if 'solution_name' in stgs:
                data[subsk+'_solnname'] = stgs['solution_name']
            if 'use_properties' in stgs:
                data[subsk+'_useprops'] = stgs['use_properties']
            if 'use_descriptors' in stgs:
                data[subsk+'_usedescs'] = stgs['use_descriptors']
            else:
                data[subsk+'_usedescs'] = True
        resp = self.session.post(
            self.service_url+'featurize', 
            json=data
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def run_transformation(self,model_id,settings):
        """Run transformation: step 3 of the model creation pipeline.

        The goal of this step is to transform the featurized dataset
        to make it work better for the modeling task at hand.

        Parameters
        ----------
        model_id : int
            Integer id of the model being worked on.
        settings : dict
            The transformation settings. Keys: 

            - 'input_trans' (str): How to transform the input space. Either 'none' or 'standardize'. 
            - 'do_PCA' (bool): If 'input_trans'=='standardize' and 'do_PCA'==True, a Principle Component Analysis is performed after standardization. The principle component magnitudes are then standardized and used for modeling.
            - 'output_trans' (str): How to transform the output space. Either 'none', 'standardize', or 'log' (take log, then standardize). 

        Returns
        -------
        resp : dict
            Contains status report and, if successful,
            a process id for monitoring the transformation.
        """
        pid_resp = self.session.get(
            self.service_url+'model_process_id', 
            json={
                'model_id':model_id,
                'process_tag':'TRANSFORMATION'
            }
        )
        data = {'model_id':model_id,'process_id':pid_resp.json()['process_id']}
        data.update(settings) 
        resp = self.session.post(
            self.service_url+'transform', 
            json=data
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def run_feature_inspection(self,model_id,settings):
        """Run feature inspection: step 4 of the model creation pipeline.

        The goal of this step is to down-select features 
        from the transformed dataset for optimal model performance.

        Parameters
        ----------
        model_id : int
            Integer id of the model being worked on.
        settings : dict
            Feature inspection settings. Keys: 

            - 'inspection_strategy' (str): Options:

                - 'none' (keep all or select manually)
                - 'variances' (rank inputs in order of decreasing variance)
                - 'rfe_coefs' (recursive elimination by regression coefficients or feature importances)
                - 'combinatorial' (full combinatorial inspection) 

            - 'inspection_model' (str): Options:

                - 'ridge': Ridge regression- only for 'rfe_coefs' strategy
                - 'rf_regressor': Random forest regression- only for 'rfe_coefs' strategy 
                - 'logistic': Logistic regression- works for 'rfe_coefs' or 'combinatorial' strategies
 
            - 'reserved_inputs' (list of str): Specifies inputs that should not be eliminated
            - 'regularization' (float): Regularization coefficient for 'ridge' model
            - 'output_encoding' (str): Output encoding for 'logistic' model- either 'categorical' or 'scalar_threshold'
            - 'output_threshold' (float): Output threshold for 'logistic' model with 'scalar_threshold' encoding- values greater than or equal to the output threshold are flagged True, and the others are flagged False.
            - 'balance_class_weights' (bool): Whether or not to weight samples by class population when evaluating the objective for fitting a classifier 
            - 'multiclass_averaging' (str): Determines how classifier performance metrics are averaged over classes- either 'weighted', 'macro', or 'micro'
            - 'penalty' (str): Specification of penalty function for 'logistic' model- either 'none', 'l1', or 'l2'
            - 'cost' (float): Inverse regularization coefficient for 'logistic' model
            - 'n_estimators' (int): Number of decision trees to train for random forest models
            - 'max_depth' (int): Maximum tree depth for random forest models (optional- omit this to handle tree depth automatically) 
            - 'min_feats' (int): Minimum number of features to inspect- only for 'combinatorial' strategy
            - 'max_feats' (int): Maximum number of features to inspect- for 'combinatorial', 'rfe_coefs', and 'variances'
            - 'n_splits_cv' (int): Number of cross-validation splits- for 'rfe_coefs' or 'combinatorial'
            - 'shuffle_cv' (bool): Whether or not to shuffle during cross-validation

        Returns
        -------
        resp : dict
            Contains status report and, if successful,
            a process id for monitoring the feature inspection.
        """
        pid_resp = self.session.get(
            self.service_url+'model_process_id', 
            json={
                'model_id':model_id,
                'process_tag':'FEATURE_INSPECTION'
            }
        )
        data = {'model_id':model_id,'process_id':pid_resp.json()['process_id']}
        data.update(settings) 
        resp = self.session.post(
            self.service_url+'inspect_features', 
            json=data
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}
    
    def run_feature_selection(self,model_id,settings):
        """Run feature selection: second part of step 4 of model creation.

        The goal of this step is to select a feature set
        from the feature inspection results
        for final model training. 

        Parameters
        ----------
        model_id : int
            Integer id of the model being worked on.
        settings : dict
            Feature selection settings. Keys: 

            - 'n_feats' (str): Options:
            - 'fs_objective' (str): If different performance metrics lead to different feature sets, this specifies which feature set to keep. For 'combinatorial' strategy and 'logistic' model, this must be 'f1', 'precision', 'recall', or 'accuracy'. 

        Returns
        -------
        resp : dict
            Contains status report and, if successful,
            a process id for monitoring the feature selection.
        """
        pid_resp = self.session.get(
            self.service_url+'model_process_id', 
            json={
                'model_id':model_id,
                'process_tag':'FEATURE_SELECTION'
            }
        )
        data = {'model_id':model_id,'process_id':pid_resp.json()['process_id']}
        data.update(settings) 
        resp = self.session.post(
            self.service_url+'select_features', 
            json=data
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def run_model_training(self,model_id,settings):
        """Run model training: step 5 of the model creation pipeline.

        The goal of this step is to train a model
        from the featurized, transformed, and feature-selected dataset. 

        Parameters
        ----------
        model_id : int
            Integer id of the model being worked on.
        settings : dict
            Model training settings. Keys: 
            - 'model' (str): Options:

                - 'none': No model is trained- the model is only for input space operations 
                - 'ridge': Ridge regression
                - 'logistic': Logistic regression
                - 'rf_regressor': Random forest regression 
                - 'gp': Gaussian Process regression- use caution with large training sets 
 
            - 'regularization' (float): Regularization coefficient for 'ridge' model
            - 'output_encoding' (str): Output encoding for 'logistic' model- either 'categorical' or 'scalar_threshold'
            - 'output_threshold' (float): Output threshold for 'logistic' model with 'scalar_threshold' encoding- values greater than or equal to the output threshold are flagged True, and the others are flagged False.
            - 'balance_class_weights' (bool): Whether or not to weight samples by class population when evaluating the objective for fitting a classifier 
            - 'multiclass_averaging' (str): Determines how classifier performance metrics are averaged over classes- either 'weighted', 'macro', or 'micro'
            - 'penalty' (str): Specification of penalty function- for 'logistic' model- either 'none', 'l1', or 'l2'
            - 'cost' (float): Inverse regularization coefficient for 'logistic' model
            - 'n_estimators' (int): Number of decision trees to train for random forest models
            - 'max_depth' (int): Maximum tree depth for random forest models (optional- omit this to handle tree depth automatically) 
            - 'kernel' (str): Kernel selection for 'gp' model- either 'rbf' or 'inv_exp' 
            - 'kernel_width' (float): Characteristic width of kernel for 'gp' model 
            - 'noise_estimate' (float): Diagonal noise estimate for 'gp' model kernel regularization 
            - 'n_splits_cv' (int): Number of cross-validation splits- for 'rfe_coefs' or 'combinatorial'
            - 'shuffle_cv' (bool): Whether or not to shuffle during cross-validation

        Returns
        -------
        resp : dict
            Contains status report and, if successful,
            a process id for monitoring the model training.
        """
        pid_resp = self.session.get(
            self.service_url+'model_process_id', 
            json={
                'model_id':model_id,
                'process_tag':'MODEL_TRAINING'
            }
        )
        data = {'model_id':model_id,'process_id':pid_resp.json()['process_id']}
        data.update(settings) 
        resp = self.session.post(
            self.service_url+'train_model', 
            json=data
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def finalize_model(self,model_id):
        """Finalize a model.

        After finalization, the model can be applied to samples,
        or used in design pipelines.
        Models cannot be changed after finalization,
        and finalization cannot be undone.

        Returns 
        -------
        response : dict
            Dict containing status report.
        """
        resp = self.session.post(
            self.service_url+'finalize_model', 
            json={'model_id':model_id}
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}


    # APPLY MODEL

    def apply_models(self,dataset_id,model_ids,samples,run_featurization=True,run_transformation=True):
        """Apply multiple models to one or more samples by providing model inputs.

        Parameters
        ----------
        model_ids : list of int
            List of integer ids of the models to be applied
        samples : dict or pandas.DataFrame
            Model inputs- if it is a dict, the keys are sample ids, 
            and values are dicts of model inputs. 
            If it is a DataFrame, the index contains sample ids,
            and the columns are the model inputs.
        run_featurization : bool
            Whether or not to run featurization on the samples
        run_transformation : bool
            Whether or not to run transformation on the samples

        Returns
        -------
        resp : dict
            Dict containing model results or error reports
        """
        if isinstance(samples,pd.DataFrame):
            samples = samples.to_dict(orient='index')
        resp = self.session.post(
            self.service_url+'api/apply_models', 
            json = {
                'dataset_id':dataset_id,
                'model_ids':model_ids,
                'run_featurization':run_featurization,
                'run_transformation':run_transformation,
                'samples':samples
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}
            
    def apply_model(self,model_id,samples,run_featurization=True,run_transformation=True):
        """Apply a model to one or more samples by providing model inputs.

        Parameters
        ----------
        model_id : int
            Integer id of the model to be applied
        samples : dict or pandas.DataFrame
            Model inputs- if it is a dict, the keys are sample ids, 
            and values are dicts of model inputs. 
            If it is a DataFrame, the index contains sample ids,
            and the columns are the model inputs.
        run_featurization : bool
            Whether or not to run the model's featurization on the samples
        run_transformation : bool
            Whether or not to run the model's transformation on the samples

        Returns
        -------
        resp : dict
            Dict containing model results or error reports
        """
        if isinstance(samples,pd.DataFrame):
            samples = samples.to_dict(orient='index')
        pid_resp = self.session.get(
            self.service_url+'model_process_id', 
            json={
                'model_id':model_id,
                'process_tag':'APPLY_MODEL_'+uuid.uuid4().hex
            }
        )
        procid = pid_resp.json()['process_id']
        resp = self.session.post(
            self.service_url+'api/apply_model', 
            json = {
                'model_id':model_id,
                'process_id':procid,
                'run_featurization':run_featurization,
                'run_transformation':run_transformation,
                'samples':samples
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def download_apply_model_results(self,dataset_id,process_id,wait=False,wait_interval=1.,output_path=None):
        """Fetch results or progress report for a model execution.

        Parameters
        ----------
        dataset_id : int
            Integer id of the dataset to which the model belongs.
        process_id : int
            Integer id, as assigned to the process when it was started
        wait : bool
            If True, the client will retrieve the report repeatedly,
            until the process is finished, and then return the result.
            If False, the client may immediately return a report
            that expresses the progress.
        wait_interval : float
            Interval to wait between status checks.

        Returns
        -------
        resp : dict
            Dict containing progress report, results, or error report
        """
        res = self.download_process_results(
            dataset_id,
            process_id,
            wait=wait,
            wait_interval=wait_interval,
            make_dataframe=True,
            output_path=output_path
        )
        # COMPATIBILITY PATCH
        res['df'] = res.get('data')
        return res

    def download_process_results(self,dataset_id,process_id,wait=False,wait_interval=1.,make_dataframe=False,output_path=''):
        """Fetch results or progress report for any process by process id.

        Parameters
        ----------
        dataset_id : int
            Integer id, indicates the parent dataset of the process 
        process_id : int
            Integer id, as assigned to the process when it was started
        wait : bool
            If True, the client will retrieve the report repeatedly,
            until the process is finished, and then return the result.
            If False, the client may immediately return a report
            that expresses the progress.
        wait_interval : float
            Interval to wait between status checks.
        make_dataframe : bool
            If True, attempt to read the file as a pandas.DataFrame.
        output_path : str
            If provided, and make_dataframe is True,
            the dataframe is written to this path.

        Returns
        -------
        resp : dict
            Dict containing progress report, results, or error report

        Returns
        -------
        resp : dict
            Dict containing progress report, results, or error report
        """
        procstat = self.session.get(
            self.service_url+'process_status',
            params={'process_id':process_id}
        ).json()
        if wait:
            while not procstat['status'] in ['FINISHED','ERROR']: 
                time.sleep(wait_interval)
                procstat = self.session.get(
                    self.service_url+'process_status',
                    params={'process_id':process_id}
                ).json()
        if procstat['status'] == 'FINISHED':
            res = self.session.get(
                self.service_url+'download_file',
                json={'file_tag':'{}.RESULTS_{}'.format(dataset_id,process_id)}
            )
            data = res._content
            df = None
            if make_dataframe:
                try:
                    df = pd.read_csv(BytesIO(res._content))
                    if output_path:
                        df.to_csv(output_path)
                except:
                    pass 
            return {'success':True,'data':data,'df':df}
        else:
            return procstat


    def configure_design(self,design_id,scalar_columns=[],substance_columns=[],model_output_columns=[]):
        """Perform design configuration: step 1 of the design pipeline.

        The goal of this step is to specify 
        how each column of the dataset will be handled
        for design purposes.
        Similar to configure_model().

        Parameters
        ----------
        design_id : int
            Integer id of the design being worked on.
        scalar_columns : list
            List of names of columns that contain scalar inputs.
        substance_columns : list
            List of names of columns that contain substance names. 
        model_output_columns : list 
            List of columns whose values will be estimated by model predictions. Each of these columns must already have a model trained and finalized, based on the same dataset as this design. Each of those models must have their input spaces among the 'scalar_columns' and 'substance_columns'.

        Returns
        -------
        resp : dict
            Contains status report.
        """
        resp = self.session.post(
            self.service_url+'configure_design', 
            json={
                'design_id':design_id,
                'scalar_columns':scalar_columns,
                'substance_columns':substance_columns,
                'model_output_columns':model_output_columns
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def configure_candidates(self,design_id,settings={},substance_settings={},scalar_settings={},model_settings={}):
        """Perform candidate configuration: step 2 of the design pipeline.

        The goal of this step is to specify 
        how candidates will be generated.

        Parameters
        ----------
        design_id : int
            Integer id of the design being worked on.
        settings : dict
            Dict of general candidate configurations:

            - 'candidate_source' (str): Specifies source of candidates. Either 'candidate_generator' (default) or 'table'.
            - 'candidate_table_id' (int): If 'candidate_source'=='table', this is the integer id of the table that defines the candidates.

        substance_settings : dict
            Settings for generating candidate substances 
            (only used if settings['candidate_source']=='candidate_generator').
            The keys of this dict should be the names of the substance columns.
            The values are dicts of settings for generating candidates for that substance. 
            Each dict may have the following keys:

            - 'candidates' (str): Specifies a candidate substance set. This should be the name of an available substance set, or 'single' to specify a single substance.
            - 'selection' (str): If 'candidates'=='single', this is the name of the substance to use 
            - 'conc_source' (str): If the substance has a concentration, this specifies how to generate scalar concentration values. Either 'single_value', 'grid', or 'zip_sequence'.
            - 'conc_value' (float): If 'conc_source'=='single_value', this is the value to use
            - 'conc_minvalue' (float): If 'conc_source'=='grid', this is the minimum value.
            - 'conc_maxvalue' (float): If 'conc_source'=='grid', this is the maximum value.
            - 'conc_resolution' (float): If 'conc_source'=='grid', this is the grid spacing.

        scalar_settings : dict
            Settings for generating candidate scalar values
            (only used if settings['candidate_source']=='candidate_generator').
            The keys of this dict should be the names of the scalar columns.
            The values are dicts of settings for generating candidate scalar values. 
            Each dict may have the following keys:

            - 'source' (str): Specifies how to generate scalar values. Either 'single_value', 'grid', or 'zip_sequence'.
            - 'value' (float): If 'source'=='single_value', this is the value to use
            - 'minvalue' (float): If 'source'=='grid', this is the minimum value.
            - 'maxvalue' (float): If 'source'=='grid', this is the maximum value.
            - 'resolution' (float): If 'source'=='grid', this is the grid spacing.

        model_settings : dict
            The keys must be the names of the model output columns.
            Each value must be the name of the model to use to estimate values for the column.
        """
        data = {'design_id':design_id}
        data.update(settings)
        for subsnm,stgs in substance_settings.items():
            for stgnm,stgval in stgs.items():
                data[subsnm+'_'+stgnm] = stgval
        for nm,stgs in scalar_settings.items():
            for stgnm,stgval in stgs.items():
                data[nm+'_'+stgnm] = stgval
        for modnm,mdl in model_settings.items():
            data[modnm+'_model'] = mdl 
            #for stgnm,stgval in stgs.items():
        resp = self.session.post(
            self.service_url+'generate_candidates', 
            json=data
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def run_screening(self,design_id,settings={},model_settings={}):
        """Run candidate screening: the third and final step of the design pipeline.

        The goal of this step is to specify how candidates will be evaluated,
        and then to evaluate all of the candidates,
        and keep only the best-scoring ones. 

        Parameters
        ----------
        design_id : int
            Integer id of the design being worked on.
        settings : dict
            Basic screening settings and input space handling. Keys:

            - 'max_n_keep' (int): Maximum number of candidates to keep. Keep as few as possible to keep the screening operation running fast and reduce garbage data accumulation. 
            - 'joint_screening_strategy' (str): Specification of strategy for evaluating candidates jointly. Acquisition values are combined either by weighted mean or by weighted geometric mean. Options are (the default) 'mean' or 'geometric_mean'.
            - 'input_space_strategy' (str): Screening strategy for input space. Options:

                - 'ignore' : Input space screening is skipped.
                - 'distance' : Candidates are scored based on their Euclidean distance from training set samples in the model training space. For explorative screening with little or no output data.
            
            - 'input_space_target' (str): target for input space evaluation, either 'max' or 'min'. 
            - 'input_space_model' (str): Name of the model to use for input space evaluation. 
            - 'input_space_sequential' (str): Sequential evaluation mode. Either 'sequential' or 'none' (default is 'none'). 
            - 'input_space_weight' (float): For joint screening, this is the weight applied to the input space acquisition value.

        model_settings : dict
            Settings for model-output-based screening. 
            The keys of this dict should be the names of the model output columns.
            The values are dicts of settings for evaluating candidates. 
            Each dict may have the following keys:

            - 'strategy' (str): Specifies screening strategy. Options:

                - 'ignore' : Every candidate gets an acquisition value of 1.
                - 'value' : Screen based on predicted values for scalar models. Acquistion values are scaled according to training set values.
                - 'class_probability' : Screen based on probability of target class membership.
                - 'uncertainty' : For 'gp' models. Acquisition value is equal to prediction variance.
                - 'ucb' : For 'gp' models. Like 'value' screening but performed on the upper confidence bound of the model predictions. 
                - 'lcb' : For 'gp' models. Like 'value' screening but performed on the lower confidence bound of the model predictions. 
                - 'pi' : For 'gp' models. Acquisition value is the probability of improvement relative to the best value in the training set. 
 
            - 'target' (str): For scalar-valued outputs, specifies whether to minimize or maximize- must be 'max' or 'min'. For categorical outputs, specifies which class to target. 
            - 'exploration_incentive' (float): If 'strategy'=='pi', this shifts the incumbent best value away from optimal to facilitate higher acquisition values in unexplored spaces. 
            - 'weight' (float): For joint screening, specifies the weight applied to this result 

        """
        pid_resp = self.session.get(
            self.service_url+'design_process_id', 
            json={
                'design_id':design_id,
                'process_tag':'SCREENING'
            }
        )
        data = {'design_id':design_id,'process_id':pid_resp.json()['process_id']}
        data.update(settings)
        for nm,stgs in model_settings.items():
            for stgnm,stgval in stgs.items():
                data[nm+'_'+stgnm] = stgval
        resp = self.session.post(
            self.service_url+'screen_candidates', 
            json=data
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}


    # SUBSTANCES

    def check_substance_names(self,names,location='shared'):
        """Check for existence of substances by name.

        Parameters
        ----------
        names : list
            List of names (strings) to be checked.
        location : str
            Location of substances ('private' or 'shared').

        Returns
        -------
        response : dict
            Dict containing status report and results.
        """
        resp = self.session.get(
            self.service_url+'api/check_substance_names', 
            headers={'x-api-key':self.api_key},
            json={'names':names,'location':location}
        )
        if resp.status_code == 200:
            respdata = resp.json()
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}

    def pull_shared_substance(self,name):
        """Copy a substance from the shared to the private substance tables.

        This allows users to pull shared substances into their private tables,
        so that they can edit the substances without affecting the shared data,
        and so that they can add sensitive information to their tables
        without allowing other instances to access it.

        Parameters
        ----------
        name : str 
            A name that is assigned to the substance to be copied.

        Returns
        -------
        response : dict
            Dict containing status report and results.
        """
        resp = self.session.get(
            self.service_url+'api/pull_shared_substance', 
            json={'name':name}
        )
        if resp.status_code == 200:
            respdata = resp.json()
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}

    def add_substance(self,name,source='',other_names=[],descriptors={},properties={},documents={},featurization={}):
        """Add a substance to the private substance tables.

        Parameters
        ----------
        name : str
            A name for the Substance.
        source : str
            A representation of the structure of the Substance,
            sufficient for extracting descriptors.
            For example, a molecule might be represented by a SMILES string,
            and a crystalline solid might be represented by a CIF file.
        other_names : list
            Any number of additional names to assign to the Substance.
            Substance names must be unique, so if any of these names
            are already assigned to substances in the database,
            this operation will fail.
        descriptors : dict
            Keys are descriptor names, and values are descriptor values.
            Descriptors are expected to be real-valued.
        properties : dict
            Keys are property names, and values are property values.
            Properties are expected to be real-valued.
        documents : dict
            Keys are document names, and values are documents.
            Documents may be any sort of jsonable object.
        featurization : dict
            Keys are featurizations to attempt on the new substance.
            Values are dicts of settings pertaining to the featurization.
        """
        resp = self.session.post(
            self.service_url+'api/add_substance', 
            json = {
                'name':name,
                'descriptors':descriptors,
                'properties':properties,
                'documents':documents,
                'source':source,
                'other_names':other_names,
                'featurization':featurization
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
        """Update substance data in the private substance tables.

        Parameters
        ----------
        name : str
            A name that is already assigned to the Substance of interest. 
        source : str
            A string representing of the structure of the Substance,
            sufficient for extracting descriptors.
        other_names : list
            Any number of additional names to assign to the Substance.
        descriptors : dict
            Keys are descriptor names, and values are descriptor values.
        properties : dict
            Keys are property names, and values are property values.
        documents : dict
            Keys are document names, and values are documents.
            Documents may be strings or anything json-like.
        remove_other_descriptors : bool 
            If True, descriptors other than those provided will be deleted. 
        remove_other_properties : bool 
            If True, properties other than those provided will be deleted. 
        remove_other_documents : bool 
            If True, documents other than those provided will be deleted. 

        Returns
        -------
        response : dict
            Dict containing status report and results.
        """
        resp = self.session.post(
            self.service_url+'api/update_substance', 
            json = {
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

    def get_substance_data(self,name,location='shared'):
        """Get all data for a substance by providing a substance name.

        Parameters
        ----------
        name : str 
            Name of the substance.
        location : str
            Location of the substance ('private' or 'shared'). 

        Returns
        -------
        resp : dict
            Contains status report and, if successful, substance data. 
        """
        resp = self.session.get(
            self.service_url+'api/download_substance', 
            json={'name':name,'location':location}
        )
        if resp.status_code == 200:
            respdata = resp.json()
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_substance_set(self,name):
        """Get a substance set by name.

        Parameters
        ----------
        name : str
            Name of the substance set.

        Returns
        -------
        resp : dict
            Contains status report and, if successful, substance set data.
        """
        resp = self.session.get(
            self.service_url+'api/substance_set', 
            json={'name':name}
        )
        if resp.status_code == 200: 
            respdata = resp.json()
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}

    def new_substance_set(self,name,substance_names=[]):
        """Create a new substance set.

        Parameters
        ----------
        name : str
            Name to assign to the new substance set.
        substance_names : list of str
            Substance names to add to the set.

        Returns
        -------
        resp : dict
            Contains status report and, if successful, new substance set id
        """
        resp = self.session.post(
            self.service_url+'api/new_substance_set', 
            json={'name':name,'substance_names':substance_names}
        )
        if resp.status_code == 200: 
            respdata = resp.json()
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}

    def edit_substance_set(self,set_id,names_to_add=[],names_to_remove=[]):
        """Update an existing substance set.

        Parameters
        ----------
        set_id : int 
            Integer id of the substance set to be updated.
        names_to_add : list of str
            Substance names to add to the set. 
        names_to_remove : list of str
            Substance names to remove from the set. 

        Returns
        -------
        resp : dict
            Contains status report and, if successful, new substance set id
        """
        resp = self.session.post(
            self.service_url+'api/edit_substance_set', 
            json={
                'set_id':set_id,
                'names_to_add':names_to_add,
                'names_to_remove':names_to_remove
            }
        )
        if resp.status_code == 200: 
            respdata = resp.json()
            return respdata
        else:
            return {'success':False,'status_code':resp.status_code}


    # MEASUREMENTS

    def get_measurement_index(self):
        """Download the index of available measurements.

        Returns
        -------
        response : dict
            Dict containing information about measurements available to the client.
        """
        resp = self.session.get(self.service_url+'api/measurement_index')
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def new_measurement(self,filepath,type,name,description=''):
        """Create a new measurement on Aionics.

        The data for the measurement may be in any format,
        provided there is a processing workflow available on platform for it.

        Parameters
        ----------
        filepath : str
            Path to measurement source file on the local filesystem.
        type : str
            String describing the measurement type. 
            Valid types:

            - 'cycler_nda'

        name : str
            Name for the new measurement- must be unique.
        description : str
            Description of the new measurement (optional).

        Returns
        -------
        response : dict
            Dict containing the new measurement id or an error report.
        """
        resp = self.session.post(
            self.service_url+'api/new_measurement',
            files={
                'source_file':open(filepath,'rb'),
                'metadata':json.dumps({
                    'type':type,
                    'name':name,
                    'description':description
                }).encode()
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def process_measurement(self,measurement_id,settings):
        """Start processing a measurement.

        Parameters
        ----------
        measurement_id : int
            Integer id of the measurement to be edited.
        settings : dict
            Dict of measurement processing configurations.
            Configurations include:

            - 'processing': Selects a processing workflow. Options are: 

                - 'cycle_summary_v1': For 'cycler_nda' type measurements, process cycle data.
                - 'cycle_life_rpt_hppc_v1': For 'cycler_nda' type measurements, process cycle data, determine cycle life, and interpret the RPT and HPPC metrics of selected cycles.

            - 'featurization': Selects a processing workflow. Options are:

                - 'discharge_capacity': For 'cycler_nda' type measurements, apply the featurization of Severson and Attia, et al, for predicting cycle life from early cycle data.

            - For 'cycler_nda' type measurements to be processed by 'cycle_summary_v1' or 'cycle_life_rpt_hppc_v1', the following settings are required:

                - 'active_material_mass': The mass of the active material, in grams, for determining specific capacity.
                - 'cathode_area': Real-valued area of a single layer of cathode material, for determining ASI.
                - 'layer_count': Integer number of cathode layers, for determining ASI.
                - 'ignore_cycles': List of cycle id's that should be ignored for featurization, cycle summary, and determination of cycle life.

            - For 'cycler_nda' type measurements to be processed by 'cycle_life_rpt_hppc_v1', the following settings are required:

                - 'cycle_life_threshold': Percentage of initial cycle life at which the battery should be considered dead.
                - 'rpt_cycles': List of cycle id's that should be processed as RPT tests.
                - 'hppc_cycles': List of cycle id's that should be processed as HPPC tests.

            - For 'cycler_nda' type measurements to be featurized by 'discharge_capacity', the following settings are required:

                - 'qofv_index_1': Cycle id for the first Q(V) profile 
                - 'qofv_index_2': Cycle id for the second Q(V) profile 
                - 'capacity_index_1': Cycle id for the first Q(N) point for capacity trajectory fitting 
                - 'capacity_index_2': Cycle id for the intermediate Q(N) point for capacity trajectory fitting 
                - 'capacity_index_3': Cycle id for the final Q(N) point for capacity trajectory fitting 

        Returns
        -------
        resp : dict
            Contains status report and, if successful,
            a process id for monitoring the process.
        """
        pid_resp = self.session.get(
            self.service_url+'measurement_process_id', 
            json={'measurement_id':measurement_id}
        )
        if not pid_resp.status_code == 200:
            return {'success':False,'status_code':pid_resp.status_code}
        procid = pid_resp.json()['process_id']
        data = settings.copy()
        data.update({
            'measurement_id':measurement_id,
            'process_id':procid
        })
        resp = self.session.post(
            self.service_url+'process_measurement', 
            json=data
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}

    def get_measurement_data(self,measurement_id):
        """Get measurement settings and results.

        Parameters
        ----------
        measurement_id : int
            Integer id of the measurement to be queried.

        Returns
        -------
        resp : dict
            Contains status report and, if successful, 
            the settings and results of the measurement.
        """
        settings_resp = self.session.get(
            self.service_url+'measurement_settings', 
            params={'measurement_id':measurement_id}
        )
        if settings_resp.status_code == 200:
            settings = settings_resp.json()['data']
        else:
            return {'success':False,'status_code':resp.status_code}
        results_resp = self.session.get(
            self.service_url+'measurement_results', 
            params={'measurement_id':measurement_id}
        )
        if results_resp.status_code == 200:
            results = results_resp.json()['data']
        else:
            return {'success':False,'status_code':resp.status_code}
        return {'success':True,'settings':settings,'results':results}

    def download_model_file(self,model_id,file_tag,output_path):
        """Download a file for a given model by providing the file tag and model id.

        Parameters
        ----------
        model_id : int
            Integer index of the desired model.
        file_tag : str
            String indicating which file to download.
            Depending on model settings,
            the following file tags may exist: 

            - 'SOURCE_DATASET': the model's training set table 
            - 'CONFIGURED_DATASET': training set table post-configuration 
            - 'OUTPUT_HISTOGRAM': graphical histogram of output values 
            - 'FEATURIZED_DATASET': training set table post-featurization
            - 'PCA_DATASET': training set table post-PCA, pre-standardization
            - 'TRANSFORMED_DATASET': training set table post-transformation
            - 'TRANSFORMED_OUTPUT_HISTOGRAM': graphical histogram of transformed output values 
            - 'FS_OBJECTIVES': graphical plot of model performance objectives with respect to input space dimensionality 
            - 'SELECTED_FEATURES_BARCHART': graphical bar chart of selected feature coefficients 
            - 'FS_MODEL_PERFORMANCE': predicted (and cross-validated) versus actual values in transformed space for the model used in feature selection
            - 'FS_MODEL_RESIDUALS_TR': graphical histogram of residuals in transformed space for the model used in feature selection
            - 'FS_MODEL_CONFUSION_TRAINING': graphical training set confusion matrix for the model used in feature selection
            - 'FS_MODEL_CONFUSION_XVAL': graphical cross-validation confusion matrix for the model used in feature selection
            - 'FS_DATASET': training set table post-feature selection 
            - 'MODEL_PERFORMANCE_TR': predicted (and cross-validated) versus actual values in transformed space for the fully-trained model
            - 'MODEL_PERFORMANCE': predicted (and cross-validated) versus actual values for the fully-trained model
            - 'MODEL_RESIDUALS_TR': graphical histogram of trained model residuals in transformed space
            - 'MODEL_PREDICTION_HISTOGRAM_TR': graphical histogram of trained model predictions and cross-validations in transformed space
            - 'MODEL_PREDICTION_HISTOGRAM': graphical histogram of trained model predictions and cross-validations
            - 'MODEL_PREDICTION_VARIANCES_TR': graphical histogram of trained model prediction and cross-validation variances in transformed space
            - 'MODEL_PREDICTION_VARIANCES': graphical histogram of trained model prediction and cross-validation variances
            - 'MODEL_CONFUSION_TRAINING': graphical training set confusion matrix for the trained model
            - 'MODEL_CONFUSION_XVAL': graphical cross-validation confusion matrix for the trained model
            - 'TRAINED_DATASET': training set table post-model training 

        output_path : str
            Local filesystem path where the file should be saved.

        Returns
        -------
        response : dict 
            Response data or error report. 
        """
        resp = self.session.get(
            self.service_url+'model_file',
            params={
                'model_id':model_id,
                'file_tag':file_tag
            }
        )
        if resp.status_code == 200:
            output_dir, fname = os.path.split(output_path)
            if not os.path.exists(output_dir):
                raise IOError('output directory {} does not exist'.format(output_dir))
            open(output_path,'wb').write(resp._content)
            return {'success':True}
        else:
            return {'success':False,'status_code':resp.status_code}

    def download_design_file(self,design_id,file_tag,output_path):
        """Download a file for a given design by providing the file tag and design id.

        Parameters
        ----------
        design_id : int
            Integer index of the desired design.
        file_tag : str
            String indicating which file to download.
            Depending on design settings,
            the following file tags may exist: 

            - 'SOURCE_DATASET': the design's main table (defines the design space)
            - 'CANDIDATE_SOURCE_DATASET': copy of the data table defining the design candidates 
            - 'SCREENED_CANDIDATE_DATASET': data table of candidates post-screening
            - '<output>_SCREENING_PROB_HISTOGRAM': graphical histogram of prediction probabilities for <output>
            - '<output>_SCREENING_PRED_HISTOGRAM': graphical histogram of predictions for <output>
            - '<output>_SCREENING_TRANS_PRED_HISTOGRAM': graphical histogram of transformed predictions for <output>
            - '<output>_SCREENING_VAR_HISTOGRAM': graphical histogram of prediction variances for <output>
            - '<output>_SCREENING_TRANS_VAR_HISTOGRAM': graphical histogram of transformed prediction variances for <output>
            - '<output>_SCREENING_TRANS_PRED_VAR_SCATTER': graphical scatter of transformed variance-versus-prediction for <output>
            - '<output>_SCREENING_PRED_VAR_SCATTER': graphical scatter of variance-versus-prediction for <output>

        output_path : str
            Local filesystem path where the file should be saved.

        Returns
        -------
        response : dict 
            Response data or error report. 
        """
        resp = self.session.get(
            self.service_url+'design_file',
            params={
                'design_id':design_id,
                'file_tag':file_tag
            }
        )
        if resp.status_code == 200:
            output_dir, fname = os.path.split(output_path)
            if not os.path.exists(output_dir):
                raise IOError('output directory {} does not exist'.format(output_dir))
            open(output_path,'wb').write(resp._content)
            return {'success':True}
        else:
            return {'success':False,'status_code':resp.status_code}

    def download_measurement_file(self,measurement_id,file_tag,output_path):
        """Download a measurement file by providing the file tag and measurement id.

        Parameters
        ----------
        measurement_id : int
            Integer index of the desired measurement.
        file_tag : str
            String indicating which file to download.
            All measurements have a file with tag 'SOURCE_DATA'.
            Depending on processing settings,
            measurements of 'cycler_nda' type may also have:

            - 'SOURCE_TABLE': .csv table unpacked from source binary
            - 'STEP_TABLE': .csv table of key values from each cycler step
            - 'CYCLE_TABLE': .csv table of key outcomes from each cycle
            - 'RPT_TABLE': .csv table of RPT test results
            - 'HPPC_TABLE': .csv table of HPPC test results

        output_path : str
            Local filesystem path where the file should be saved.

        Returns
        -------
        response : dict 
            Response data or error report. 
        """
        resp = self.session.get(
            self.service_url+'measurement_file',
            params={
                'measurement_id':measurement_id,
                'file_tag':file_tag
            }
        )
        if resp.status_code == 200:
            output_dir, fname = os.path.split(output_path)
            if not os.path.exists(output_dir):
                raise IOError('output directory {} does not exist'.format(output_dir))
            open(output_path,'wb').write(resp._content)
            return {'success':True}
        else:
            return {'success':False,'status_code':resp.status_code}

    def edit_measurement_metadata(self,measurement_id,name='',description=''):
        """Edit measurement metadata (name and description).

        Parameters
        ----------
        measurement_id : int
            Integer id of the measurement to be edited.
        name : str
            New name for the measurement being edited 
            (must be unique among measurements).
            If not provided, the name is not updated.
        description : str
            New description for the measurement being edited.
            If not provided, the description is not updated.

        Returns
        -------
        resp : dict
            Contains status report.
        """
        resp = self.session.post(
            self.service_url+'api/edit_measurement', 
            json={
                'measurement_id':measurement_id,
                'name':name,
                'description':description
            }
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'success':False,'status_code':resp.status_code}


    # UTILITIES 

    def check_process(self,process_id):
        """Check a process status by providing the process id.

        Parameters
        ----------
        process_id : int
            Integer id of the process to be queried.

        Returns
        -------
        response : dict
            Dict containing process status report.
        """
        procstat = self.session.get(self.service_url+'process_status',params={'process_id':process_id}).json()
        return procstat 

    def wait_for_process(self,process_id,delay_seconds=1):
        """Periodically checks on a process until it is finished.

        Parameters
        ----------
        process_id : int
            Integer process id to monitor.
        delay_seconds : float
            Number of seconds to wait between checks.
            Must be at least one second.

        Returns
        -------
        reponse : dict
            Dict containing status report.
        """
        if delay_seconds < 1: delay_seconds = 1.
        procstat = self.session.get(self.service_url+'process_status',params={'process_id':process_id}).json()
        while not procstat['status'] in ['FINISHED','ERROR']:
            time.sleep(delay_seconds)
            procstat = self.session.get(self.service_url+'process_status',params={'process_id':process_id}).json()
        return procstat

    def check_model_status(self,model_id,stat='',wait=False,wait_interval=1.):
        """Check a model's status, and optionally wait for it.

        Parameters
        ----------
        model_id : int
            Integer model id to monitor.
        stat : str 
            Model status to check or wait for. Valid values:

            - 'ERROR'
            - 'NEW'
            - 'CONFIGURED'
            - 'FEATURIZATION_READY'
            - 'FEATURIZATION_RUNNING'
            - 'FEATURIZATION_COMPLETE'
            - 'TRANSFORMATION_CONFIGURED'
            - 'TRANSFORMATION_RUNNING'
            - 'TRANSFORMED'
            - 'FEATURE_INSPECTION_CONFIGURED'
            - 'FEATURE_INSPECTION_RUNNING'
            - 'FEATURE_INSPECTION_COMPLETE'
            - 'FEATURE_SELECTION_RUNNING'
            - 'FEATURE_SELECTION_COMPLETE'
            - 'MODEL_TRAINING_CONFIGURED'
            - 'MODEL_TRAINING_RUNNING'
            - 'MODEL_TRAINING_COMPLETE'
            - 'FINISHED'

        wait : bool
            Whether or not to wait for the model to get to the specified status.
        wait_interval : float
            How long to wait between status checks, in seconds.
            Must be at least one second.

        Returns
        -------
        reponse : dict
            Dict containing status report.
        """
        if wait_interval < 1: wait_interval = 1.
        mdlstat = self.session.get(
            self.service_url+'model_status',
            params={'model_id':model_id,'status_tag':stat}
        ).json()
        if wait:
            if not mdlstat['ready']:
                time.sleep(wait_interval)
                mdlstat = self.session.get(
                    self.service_url+'model_status',
                    params={'model_id':model_id,'status_tag':stat}
                ).json()
        return mdlstat

    def check_design_status(self,design_id,stat='',wait=False,wait_interval=1.):
        """Check a design's status, and optionally wait for it.

        Parameters
        ----------
        design_id : int
            Integer design id to monitor.
        stat : str 
            Design status to check or wait for. Valid values:

            - 'ERROR'
            - 'NEW'
            - 'CONFIGURED'
            - 'CANDIDATES_CONFIGURED'
            - 'CANDIDATES_READY'
            - 'SCREENING_CONFIGURED'
            - 'SCREENING_RUNNING'
            - 'SCREENING_COMPLETE'

        wait : bool
            Whether or not to wait for the design to get to the specified status.
        wait_interval : float
            How long to wait between status checks, in seconds.
            Must be at least one second.

        Returns
        -------
        reponse : dict
            Dict containing status report.
        """
        if wait_interval < 1: wait_interval = 1.
        dstat = self.session.get(
            self.service_url+'design_status',
            params={'design_id':design_id,'status_tag':stat}
        )
        if wait:
            dstat = dstat.json()
            if not dstat['ready']:
                time.sleep(wait_interval)
                dstat = self.session.get(
                    self.service_url+'design_status',
                    params={'design_id':design_id,'status_tag':stat}
                ).json()
        return dstat

