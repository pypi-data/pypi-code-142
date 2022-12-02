import json
import requests
import Maxar_Portal_SDK.process as process
import warnings
warnings.filterwarnings("ignore")

class Token:

    def __init__(self, auth):
        self.base_url = auth.api_base_url
        self.auth = auth

    def get_user_tokens(self):
        """
        Gets a list of all tokens associated with your user
        :return: json response object
        """

        authorization = process.authorization(self.auth)
        url = "{}/tokenservice/api/v1/token".format(self.base_url)
        response = requests.request("GET", url, headers=authorization, verify=self.auth.SSL)
        process._response_handler(response)
        return response.json()

    def create_token_record(self, name=None, description=None):
        """
        Creates a new token to utilize in place of an OAuth token. A dictionary is returned with the id, name,
        description, createDate, and secret fields. NOTE: Make sure to save the secret key as this will be the only time
        it is visible. If a secret key is lost, a new one must be created.
        :return: json response object
        """
        authorization = process.authorization(self.auth)
        url = "{}/tokenservice/api/v1/token".format(self.base_url)
        payload = {
            "name": name,
            "description": description
        }
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=authorization, data=payload, verify=self.auth.SSL)
        process._response_handler(response)
        return response.json()

    def delete_tokens(self, token):
        """
        Deletes one or more tokens for one or more ids. Pass either a string of a token id to delete a single token or
        pass a list of strings of token ids to delete multiple tokens at once
        :param token: String if only deleting one token, or list if deleting multiple tokens
        :return: json response object
        """
        authorization = process.authorization(self.auth)
        if type(token) == str:
            url = "{}/tokenservice/api/v1/token/id/{}".format(self.base_url, token)
            response = requests.request("DELETE", url, headers=authorization,verify=self.auth.SSL)
        elif type(token) == list:
            url = "{}/tokenservice/api/v1/token".format(self.base_url)
            payload = json.dumps({"ids": token})
            response = requests.request("DELETE", url, headers=authorization, data=payload,verify=self.auth.SSL)
        else:
            raise Exception('Please pass either a string of the token ID or a list of strings of token ids to delete')
        process._response_handler(response)
        if response.status_code == 200:
            return "Token {} successfully deleted".format(token)
        else:
            return "Token not deleted, response code of {} received".format(response.status_code)
