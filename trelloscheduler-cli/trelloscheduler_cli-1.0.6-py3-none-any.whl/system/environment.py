import os

# Author: Olin Gallet
# Date: 14 Oct 2022
#
# The Environment contains methods to pull Trello information
# to connect to the API.

class Environment:
    def __init__(self):
        pass

    @staticmethod
    def get_trello_api_key():
        """Gets the Trello API key from the environment variables.
        
        :return: the Trello API key
        :rtype: str
        """
        response = None
        if 'TRELLO_API_KEY' in os.environ:
            response = os.environ['TRELLO_API_KEY']
        return response

    @staticmethod
    def get_trello_api_secret():
        """Gets the Trello API secret key from the environment variables.

        :return: the Trello API secret key
        :rtype: str
        """
        response = None
        if 'TRELLO_API_SECRET' in os.environ:
            response = os.environ['TRELLO_API_SECRET']
        return response

    @staticmethod
    def get_trello_token():
        """Gets the Trello token from the environment variables.

        :return: the Trello token
        :rtype: str
        """
        response = None
        if 'TRELLO_TOKEN' in os.environ:
            response = os.environ['TRELLO_TOKEN']
        return response
    
    @staticmethod
    def has_trello_keys():
        """States if the Trello keys are set in the environment.

        :return: are Trello keys set?
        :rtype: Boolean
        """
        return Environment.get_trello_api_key() is not None and Environment.get_trello_api_secret() is not None and Environment.get_trello_token() is not None
