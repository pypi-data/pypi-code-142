import json
import os

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.provider import EnvCredentialProvider
from huaweicloudsdkcsms import v1 as csms


class CsmsService:

    def __init__(self, access_key: str = None, secret_key: str = None, project_id: str = None, region: str = None):
        if access_key:
            self._credentials = BasicCredentials(access_key, secret_key, project_id)
        else:
            provider = EnvCredentialProvider.get_basic_credential_env_provider()
            self._credentials = provider.get_credentials()

        if region is None:
            region = os.environ.get('HUAWEICLOUD_REGION')

        self.client = csms.CsmsClient.new_builder().with_credentials(self._credentials)
        if region:
            self.client = self.client.with_region(csms.region.csms.CsmsRegion.value_of(region))

        self.client = self.client.build()

    def get_raw_secret(self, secret_name: str, version_id='latest'):
        request = csms.ShowSecretVersionRequest(secret_name, version_id)
        response = self.client.show_secret_version(request)
        return response.to_dict()['version']['secret_string']

    def get_json_secret(self, secret_name: str, version_id='latest'):
        return json.loads(self.get_raw_secret(secret_name, version_id))
