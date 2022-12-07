# -*- coding: utf-8 -*-

import json
import os.path
import requests
import sys
from datetime import datetime
from pytz import timezone

from easymaker.common import constants
from easymaker.common import exceptions
from easymaker.common import environment_variables
from easymaker.api.api_sender import ApiSender


class ObjectStorage:
    CHUNK_SIZE = 100 * 1024  # 100 KB
    FILE_SIZE_LIMIT = 5 * 1024 * 1024 * 1024  # 5 GB

    def __init__(self, easymaker_region=None, username=None, password=None):
        self.token_expires = None
        self.api_sender = None

        if easymaker_region:
            self.region = easymaker_region
        elif os.environ.get('EM_REGION'):
            self.region = os.environ.get('EM_REGION')
        else:
            self.region = constants.DEFAULT_REGION
        self.username = username
        self.password = password

    def _get_token(self, tenant_id=None):
        if tenant_id:
            self.tenant_id = tenant_id

        if self.token_expires is not None:
            if os.environ.get('EM_TOKEN'):
                self.now = datetime.now(timezone('Asia/Seoul'))
            else:
                self.now = datetime.utcnow()
            time_diff = self.token_expires - self.now
            if time_diff.total_seconds() > 600:
                return

        self.api_sender = ApiSender(self.region,
                                    os.environ.get('EM_APPKEY'),
                                    os.environ.get('EM_SECRET_KEY'))
        response = self.api_sender.get_objectstorage_token(tenant_id=self.tenant_id,
                                                           username=self.username,
                                                           password=self.password)
        try:
            self.token = response['access']['token']
        except KeyError:
            print(response)

        self.token_id = self.token['id']

        if os.environ.get('EM_TOKEN'):
            self.token_expires = datetime.strptime(self.token['expires'], '%Y-%m-%dT%H:%M:%S.%f%z')
        else:
            self.token_expires = datetime.strptime(self.token['expires'], '%Y-%m-%dT%H:%M:%SZ')

    def _get_request_header(self):
        self._get_token(self.tenant_id)
        return {'X-Auth-Token': self.token_id}

    def upload(self, easymaker_obs_uri, upload_path):
        """
        Args:
            easymaker_obs_uri : easymaker obs directory uri (obs://{object_storage_endpoint}/{container_name}/{path})
            upload_path : upload local path (file or directory)
        """
        obs_full_url, _, _, tenant_id, _, _ = parse_obs_uri(easymaker_obs_uri)
        self._get_token(tenant_id)

        if os.path.isfile(upload_path):
            upload_url = os.path.join(obs_full_url, os.path.basename(upload_path))
            self._upload_file(upload_url, upload_path)

        if os.path.isdir(upload_path):
            file_path_list = []
            for (root, dirs, files) in os.walk(upload_path):
                for file in files:
                    file_path_list.append(os.path.join(root, file))

            for upload_file_path in file_path_list:
                upload_url = os.path.join(obs_full_url,
                                          os.path.relpath(upload_file_path,
                                                          os.path.abspath(upload_path)))
                self._upload_file(upload_url, upload_file_path)

    def _upload_file(self, upload_url, upload_file_path):
        """
        Upload files under 5G
        Args:
            easymaker_obs_uri : obs object path (file)
            upload_file_path : upload local path (file)
        """
        if os.path.getsize(upload_file_path) >= self.FILE_SIZE_LIMIT:
            return self._upload_large_file(upload_url, upload_file_path)

        req_header = self._get_request_header()
        with open(upload_file_path, 'rb') as f:
            return requests.put(upload_url, headers=req_header, data=f.read())

    def _upload_large_file(self, upload_url, upload_file_path):
        """
        Objects with a capacity exceeding 5 GB are uploaded in segments of 5 GB or less.
        """
        req_header = self._get_request_header()

        with open(upload_file_path, 'rb') as f:
            chunk_index = 1
            chunk_size = self.CHUNK_SIZE
            total_bytes_read = 0
            obj_size = os.path.getsize(upload_file_path)

            while total_bytes_read < obj_size:
                remained_bytes = obj_size - total_bytes_read
                if remained_bytes < chunk_size:
                    chunk_size = remained_bytes

                req_url = '%s/%03d' % (upload_url, chunk_index)
                requests.put(
                    req_url, headers=req_header, data=f.read(chunk_size))
                total_bytes_read += chunk_size
                f.seek(total_bytes_read)
                chunk_index += 1

        # create manifest
        req_header = self._get_request_header()
        # X-Object-Manifest : AUTH_*****/ 뒷부분 경로
        uri_element_list = upload_url.split('/')
        for idx, val in enumerate(uri_element_list):
            if val.startswith('AUTH_'):
                object_manifest = '/'.join(uri_element_list[idx + 1:])
        req_header['X-Object-Manifest'] = object_manifest
        return requests.put(upload_url, headers=req_header)

    def download(self, easymaker_obs_uri, download_dir_path):
        """
        Args:
            easymaker_obs_uri : easymaker obs uri (obs://{object_storage_endpoint}/{container_name}/{path})
            download_dir_path : download local path (directory)
        """
        obs_full_url, _, container_url, tenant_id, _, object_prefix = parse_obs_uri(easymaker_obs_uri)
        self._get_token(tenant_id)
        isDirectoryObject = False
        file_object_list = []

        objectList = self.api_sender.get_object_list(container_url, self._get_request_header(), object_prefix)
        for obj in objectList:
            if (object_prefix.endswith('/') == False) and (obj == object_prefix):  # target object is file
                download_file_path = os.path.join(download_dir_path, os.path.basename(object_prefix))
                # object : depth1/file1
                # download_file_path => download_dir_path + /file1
                return self._download_file(container_url, object_prefix, download_file_path)

            if object_prefix.endswith('/') == False:
                object_prefix = ''.join([object_prefix, '/'])

            if obj.startswith(object_prefix):
                isDirectoryObject = True
                if not obj.endswith('/'):
                    file_object_list.append(obj)

        if isDirectoryObject:
            for file_object in file_object_list:
                download_file_path = os.path.join(download_dir_path, os.path.relpath(file_object, object_prefix))
                # object : deps1/deps2, file_object : deps1/deps2/deps3/file1
                # download_file_path => download_dir_path + /deps3/file1
                self._download_file(container_url, file_object, download_file_path)

    def _download_file(self, container_url, file_object, download_file_path):
        """
        Args:
            container_url : obs container url (https://{object_storage_endpoint}/{container_name})
            file_object : obs object path (file)
            download_file_path : download local path (file)
        """
        req_url = os.path.join(container_url, file_object)
        req_header = self._get_request_header()
        response = requests.get(req_url, headers=req_header)

        if response.status_code != 200:
            raise exceptions.EasyMakerError(f'Object storage donwload fail {response.json()}')

        os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
        with open(download_file_path, 'wb') as f:
            f.write(response.content)


def parse_obs_uri(easymaker_obs_uri):
    uri_split = easymaker_obs_uri.split("://")

    if len(uri_split) != 2 or uri_split[0].lower() != 'obs' or len(uri_split[1].split('//')) > 1:
        raise exceptions.EasyMakerError(f'Object storage uri parse fail. Invalid uri {easymaker_obs_uri}')

    obs_full_url = 'https://' + uri_split[1]

    uri_list = obs_full_url.split('/')

    if len(uri_list) < 7:
        raise exceptions.EasyMakerError(f'Object storage uri parse fail. Invalid uri {easymaker_obs_uri}')

    obs_host = uri_list[2]
    if uri_list[4].startswith('AUTH_'):
        tenant_id = uri_list[4][5:]
        container_url = '/'.join(uri_list[:6])
    else:
        raise exceptions.EasyMakerError(f'Object storage uri parse fail. Invalid uri {easymaker_obs_uri}')

    container_name = uri_list[5]
    object_prefix = '/'.join(uri_list[6:])

    return obs_full_url, obs_host, container_url, tenant_id, container_name, object_prefix


def download(easymaker_obs_uri, download_dir_path, easymaker_region=None, username=None, password=None):
    """
    Args:
        easymaker_obs_uri (str): easymaker obs uri (obs://{object_storage_endpoint}/{container_name}/{path})
        download_dir_path (str): download local path (directory)
        easymaker_region (str): NHN Cloud object storage Region
        username (str): NHN Cloud object storage username
        password (str): NHN Cloud object storage password
    """
    object_storage = ObjectStorage(easymaker_region=easymaker_region, username=username, password=password)
    object_storage.download(easymaker_obs_uri, download_dir_path)


def upload(easymaker_obs_uri, src_dir_path, easymaker_region=None, username=None, password=None):
    """
    Args:
        easymaker_obs_uri (str): easymaker obs directory uri (obs://{object_storage_endpoint}/{container_name}/{path})
        src_dir_path (str): upload local path (file or directory)
        easymaker_region (str): NHN Cloud object storage Region
        username (str): NHN Cloud object storage username
        password (str): NHN Cloud object storage password
    """
    object_storage = ObjectStorage(easymaker_region=easymaker_region, username=username, password=password)
    object_storage.upload(easymaker_obs_uri, src_dir_path)
