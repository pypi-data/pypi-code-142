import requests
import os
from easymaker.common import constants
from easymaker.common import utils
from easymaker.common import exceptions


class ApiSender:
    def __init__(self, region, appkey, secret_key=None):
        utils.validate_region(region)
        if os.environ.get('EM_PROFILE'):
            self._easymakerApiUrl = constants.EASYMAKER_DEV_API_URL.format(region, os.environ.get('EM_PROFILE')).rstrip("/")
            if os.environ.get('EM_PROFILE') == 'local':
                self._easymakerApiUrl = "http://127.0.0.1:10090".rstrip("/")
        else:
            self._easymakerApiUrl = constants.EASYMAKER_API_URL.format(region).rstrip("/")

        self._appkey = appkey
        self._secret_key = secret_key

    def _isSuccessful(self, response):
        isSuccess = response['header']['isSuccessful']
        if not isSuccess:
            raise exceptions.EasyMakerError(response['header']['resultMessage'])

        return isSuccess

    def _get_headers(self):
        if os.environ.get('EM_TOKEN'):
            headers = {'X-EasyMaker-Token': os.environ.get('EM_TOKEN')}
        else:
            headers = {'X-Secret-Key': self._secret_key}
        return headers

    def get_object_list(self, container_url, req_header, object_path):
        response = requests.get(container_url, headers=req_header, params={'prefix': object_path})

        if response.status_code != 200:
            raise exceptions.EasyMakerError(response)

        return response.text.split('\n')

    def get_objectstorage_token(self, tenant_id=None, username=None, password=None):

        if os.environ.get('EM_TOKEN'):
            response = requests.get(f'{self._easymakerApiUrl}/token/v1.0/appkeys/{self._appkey}/groups/{os.environ.get("EM_GROUP_ID")}/iaas-token',
                                    headers=self._get_headers()).json()
            self._isSuccessful(response)
            return response
        else:
            if tenant_id and username and password:
                token_url = constants.OBJECT_STORAGE_TOKEN_URL
                req_header = {'Content-Type': 'application/json'}
                body = {
                    'auth': {
                        'tenantId': tenant_id,
                        'passwordCredentials': {
                            'username': username,
                            'password': password
                        }
                    }
                }
                response = requests.post(token_url, headers=req_header, json=body).json()
                return response
            else:
                raise exceptions.EasyMakerError(f'Invalid object storage username/password')

    def get_instance_list(self):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/flavors',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        flavor_dict_list = []
        for flavor in response['flavorList']:
            flavor_dict_list.append({'id': flavor['id'], 'name': flavor['name']})
        return flavor_dict_list

    def get_image_list(self):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/images',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        image_dict_list = []
        for image in response['imageList']:
            if image['groupTypeCode'] == 'TRAINING':
                image_dict_list.append({'id': image['imageId'], 'name': image['imageName']})
        return image_dict_list

    def get_experiment_list(self):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/experiments',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        dict_list = []
        for experiment in response['experimentList']:
            dict_list.append({'id': experiment['experimentId'],
                              'name': experiment['experimentName']})
        return dict_list

    def create_experiment(self, experiment_name, experiment_description):
        body = {
            'experimentName': experiment_name,
            'description': experiment_description
        }
        response = requests.post(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/experiments',
                                 json=body,
                                 headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def get_experiment_by_id(self, experiment_id):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/experiments/{experiment_id}',
                                 headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def run_training(self, training_name, training_description, experiment_id, image_id, flavor_id,
                     instance_count, data_storage_size, source_dir_uri, entry_point, hyperparameter_list,
                     dataset_list, check_point_upload_uri, model_upload_uri, training_type_code, timeout_hours,
                     tag_list, use_log):
        body = {
            'trainingName': training_name,
            'description': training_description,
            'experimentId': experiment_id,
            'imageId': image_id,
            'flavorId': flavor_id,
            'instanceCount': instance_count,
            'dataStorageSize': data_storage_size,
            'sourceDirUri': source_dir_uri,
            'entryPoint': entry_point,
            'hyperparameterList': hyperparameter_list,
            'datasetList': dataset_list,
            'checkPointUploadUri': check_point_upload_uri,
            'modelUploadUri': model_upload_uri,
            'trainingTypeCode': training_type_code,
            'timeoutMinutes': timeout_hours * 60,
            'tagList': tag_list,
            'useLog': use_log,
        }
        response = requests.post(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/trainings',
                                 json=body,
                                 headers=self._get_headers()).json()

        self._isSuccessful(response)
        return response

    def get_training_list(self):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/trainings',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        dict_list = []
        for training in response['trainingList']:
            dict_list.append({'id': training['trainingId'],
                              'name': training['trainingName']})
        return dict_list

    def get_training_by_id(self, training_id):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/trainings/{training_id}',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def create_model(self, model_name, model_description=None, training_id=None,
                     framework_code=None, model_uri=None, tag_list=None):
        body = {
            'modelName': model_name,
            'description': model_description,
            'trainingId': training_id,
            'frameworkCode': framework_code,
            'modelUploadUri': model_uri,
            'tagList': tag_list,
        }

        response = requests.post(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/models',
                                 json=body,
                                 headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def get_model_list(self):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/models',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        dict_list = []
        for model in response['modelList']:
            dict_list.append({'id': model['modelId'],
                              'name': model['modelName']})
        return dict_list

    def get_model_by_id(self, model_id):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/models/{model_id}',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def create_endpoint(self,
                        endpoint_name,
                        endpoint_description,
                        flavor_id,
                        model_id,
                        apigw_resource_uri,
                        node_count,
                        tag_list,
                        use_log,
                        ca_enable=False,
                        ca_min_node_count=1,
                        ca_max_node_count=10,
                        ca_scale_down_enable=True,
                        ca_scale_down_util_thresh=50,
                        ca_scale_down_unneeded_time=10,
                        ca_scale_down_delay_after_add=10
                        ):
        body = {
            'endpointName': endpoint_name,
            'description': endpoint_description,
            'flavorId': flavor_id,
            'modelId': model_id,
            'apigwResourceUri': apigw_resource_uri,
            'nodeCount': node_count,
            'tagList': tag_list,
            'useLog': use_log,
            'caEnable': ca_enable,
            'caMinNodeCount': ca_min_node_count,
            'caMaxNodeCount': ca_max_node_count,
            'caScaleDownEnable': ca_scale_down_enable,
            'caScaleDownUtilThresh': ca_scale_down_util_thresh,
            'caScaleDownUnneededTime': ca_scale_down_unneeded_time,
            'caScaleDownDelayAfterAdd': ca_scale_down_delay_after_add,
        }
        response = requests.post(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/endpoints',
                                 json=body,
                                 headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def create_stage(self,
                     endpoint_id,
                     stage_name,
                     stage_description,
                     flavor_id,
                     model_id,
                     apigw_resource_uri,
                     node_count,
                     tag_list,
                     use_log,
                     ca_enable=False,
                     ca_min_node_count=1,
                     ca_max_node_count=10,
                     ca_scale_down_enable=True,
                     ca_scale_down_util_thresh=50,
                     ca_scale_down_unneeded_time=10,
                     ca_scale_down_delay_after_add=10
                     ):
        body = {
            'endpointId': endpoint_id,
            'apigwStageName': stage_name,
            'description': stage_description,
            'flavorId': flavor_id,
            'modelId': model_id,
            'apigwResourceUri': apigw_resource_uri,
            'nodeCount': node_count,
            'tagList': tag_list,
            'useLog': use_log,
            'caEnable': ca_enable,
            'caMinNodeCount': ca_min_node_count,
            'caMaxNodeCount': ca_max_node_count,
            'caScaleDownEnable': ca_scale_down_enable,
            'caScaleDownUtilThresh': ca_scale_down_util_thresh,
            'caScaleDownUnneededTime': ca_scale_down_unneeded_time,
            'caScaleDownDelayAfterAdd': ca_scale_down_delay_after_add,
        }

        response = requests.post(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/endpoint-stages',
                                 json=body,
                                 headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def get_endpoint_list(self):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/endpoints',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        dict_list = []
        for endpoint in response['endpointList']:
            dict_list.append({'id': endpoint['endpointId'],
                              'name': endpoint['endpointName']})
        return dict_list

    def get_endpoint_by_id(self, endpoint_id):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/endpoints/{endpoint_id}',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def get_endpoint_model_list(self, endpoint_id):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/endpoint-models',
                                headers=self._get_headers(),
                                params={'endpointId': endpoint_id}).json()
        self._isSuccessful(response)

        return response

    def get_endpoint_model_by_id(self, endpoint_model_id):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/endpoint-models/{endpoint_model_id}',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def get_endpoint_stage_list(self, endpoint_id):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/endpoint-stages',
                                headers=self._get_headers(),
                                params={'endpointId': endpoint_id}).json()
        self._isSuccessful(response)

        return response

    def get_endpoint_stage_by_id(self, endpoint_stage_id):
        response = requests.get(f'{self._easymakerApiUrl}/v1.0/appkeys/{self._appkey}/endpoint-stages/{endpoint_stage_id}',
                                headers=self._get_headers()).json()
        self._isSuccessful(response)

        return response

    def send_logncrash(self, logncrash_body):
        response = requests.post(constants.LOGNCRASH_URL, json=logncrash_body).json()
        return response
