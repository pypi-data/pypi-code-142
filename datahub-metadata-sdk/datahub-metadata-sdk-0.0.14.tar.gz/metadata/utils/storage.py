# -*- coding: utf-8 -*-

import os
import time
from abc import ABCMeta, abstractmethod
import json
import logging

import jwt
import requests
import tiefblue

from metadata.utils.url import build_url
from metadata.exception import MetadataException

logger = logging.getLogger(__name__)


class StorageClient(object, metaclass=ABCMeta):

    @abstractmethod
    def upload(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_prefix(self):
        pass

    @abstractmethod
    def list(self, prefix, recursive=False):
        pass

    @abstractmethod
    def upload(self, key, path):
        pass

    @abstractmethod
    def download(self, key, path):
        pass

    @abstractmethod
    def copy(self, src, dst):
        pass 

    @abstractmethod
    def delete(self, key):
        pass


class TiefblueStorageClient(StorageClient):

    def __init__(self, username, password, *, bohrium_endpoint=None, tiefblue_endpoint=None, **options):
        self.bohrium_endpoint = bohrium_endpoint or 'https://bohrium.dp.tech'
        self.tiefblue_endpoint = tiefblue_endpoint or 'https://tiefblue.dp.tech'
        self.username = username
        self.password = password
        self.options = options
        self.bohrium_user_id = None

        self.bohrium_token = None
        self.bohrium_last_refresh_at = None
        self.refresh_bohrium_ephemeral_token()

        self.tiefblue_token = None
        self.tiefblue_last_refresh_at = None
        self.client = None
        self.refresh_tiefblue_ephemeral_token()

        self.client = tiefblue.Client(base_url=self.tiefblue_endpoint, token=self.tiefblue_token)

    def get_name(self):
        return 'tiefblue'

    def get_prefix(self):
        if not self.bohrium_user_id:
            raise MetadataException('storage user not init')
        return f'dp/share/{self.bohrium_user_id}'

    def parse_token(self, token):
        return jwt.decode(token, verify=False, algorithms='HS256', options={"verify_signature": False})

    def check_refresh(self):
        if (not self.bohrium_last_refresh_at) or (time.time() - self.bohrium_last_refresh_at) / 60 < self.options.get('bohrium_token_refresh_threshold_minutes', 30):
            self.refresh_bohrium_ephemeral_token()
        if (not self.tiefblue_last_refresh_at) or (time.time() - self.tiefblue_last_refresh_at) / 60 < self.options.get('tiefblue_token_refresh_threshold_minutes', 40):
            self.refresh_tiefblue_ephemeral_token()

    def refresh_bohrium_ephemeral_token(self):
        data = {
            "username": self.username,
            "password": self.password,
        }
        try:
            response = requests.post(build_url(self.bohrium_endpoint, '/account/login'),
                headers={"Content-type": "application/json"},
                json=data,
            )
            response.raise_for_status()
            res = response.json()
            if res["code"] != "0000":
                raise Exception(f"error code return : {res}")
            self.bohrium_user_id = res['data']['user_id']
            self.bohrium_token = res['data']['token']
            self.bohrium_last_refresh_at = self.parse_token(self.bohrium_token)['exp']
        except Exception as e:
            raise MetadataException('failed get token ephemeral from bohrium') from e

    def refresh_tiefblue_ephemeral_token(self):   
        data = {
            "username": self.username,
            "password": self.password,
        }
        try:
            response = requests.post(build_url(self.bohrium_endpoint, '/account/login'),
                headers={"Content-type": "application/json"},
                json=data,
            )
            response.raise_for_status()
            res = response.json()
            if res["code"] != "0000":
                raise Exception(f"error code return : {res}")
            self.user_id = res['data']['user_id']
            response = requests.get(build_url(self.bohrium_endpoint, "/brm/v1/storage/token"),
                headers={
                    "Content-type": "application/json",
                    "Authorization": "jwt " + res['data']['token'],
                })
            response.raise_for_status()
            res = response.json()
            if res["code"] != 0:
                raise Exception(f"error code return : {res}")
            self.tiefblue_token = res["data"]["token"]
            self.tiefblue_last_refresh_at = self.parse_token(self.tiefblue_token)['exp']
            self.client = tiefblue.Client(base_url=self.tiefblue_endpoint, token=self.tiefblue_token)
        except Exception as e:
            raise MetadataException('failed get token ephemeral from bohrium') from e
  
    def upload(self, key, path):
        self.check_refresh()
        self.client.upload_from_file(key, path)

    def download(self, key, path):
        self.check_refresh()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.client.download_from_file(key, path)

    def list(self, prefix, recursive=False):
        self.check_refresh()
        keys = []
        next_token = ""
        while True:
            res = self.client.list(prefix=prefix, recursive=recursive, next_token=next_token)
            for obj in res["objects"]:
                if recursive and obj["path"][-1:] == "/":
                    continue
                keys.append(obj["path"])
            if not res["hasNext"]:
                break
            next_token = res["nextToken"]
        return keys

    def copy(self, src, dst):
        self.check_refresh()
        self.client.copy(src, dst)
    
    def delete(self, key):
        self.check_refresh()
        self.client.delete(key)