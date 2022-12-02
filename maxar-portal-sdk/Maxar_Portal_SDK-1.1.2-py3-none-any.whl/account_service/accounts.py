import json
import requests
import sys
import Maxar_Portal_SDK.process as process


class Info:

    def __init__(self, auth):
        self.auth = auth
        self.base_url = auth.api_base_url
        self.response = None
        self.version = auth.version

    def Search(self, search):
        """
        Function searches through all accounts and lists accounts that match the search term
        Args:
            search (string) = Search term. Searches through account numbers, account names, SAP license ids, sold to,
            and licensees
        Returns:
            Dictionary of the found account or accounts
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/accounts?search={}'.format(search)
        response = requests.request("GET", url, headers=authorization, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        if len(response.json()["accounts"]) < 1:
            raise Exception("No search results for {}. Please try another search term".format(search))
        return response.json()


    def GetAccounts(self, accountId=None, accountName=None, accountNumber=None, id_names=False, types=False):
        """
        Function lists a single account, a list of accounts, or account types and their details
        Args:
            accountId (int) = ID of the desired account. Defaults to None
            accountName (string) = Name of the desired account. Defaults to None
            accountNumber (string) = Number of the desired account. Defaults to None
            id_names (bool) = Binary for short list of account IDs and account names. Defaults to False
            types (bool) = Binary for list of all account types. Defaults to False
        Returns:
            Dictionary of account details, list of accounts and their details, or account types and their details
        """

        authorization = process.authorization(self.auth)
        if accountId:
            url = self.base_url + '/accountservice/api/v1/accounts/{}'.format(accountId)
        elif accountName:
            url = self.base_url + '/accountservice/api/v1/accounts/name/{}'.format(accountName)
        elif accountNumber:
            url = self.base_url + '/accountservice/api/v1/accounts/roles/{}'.format(accountNumber)
        elif id_names == True:
            url = self.base_url + '/accountservice/api/v1/accounts/idnames'
        elif types == True:
            url = self.base_url + '/accountservice/api/v1/accounts/types'
        else:
            url = self.base_url + '/accountservice/api/v1/accounts'
        response = requests.request("GET", url, headers=authorization, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        return response.json()

    def GetRoles(self):
        """
        Function lists all roles available for accounts
        Returns:
            Dictionary of all roles available for accounts
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/roles/'
        response = requests.request("GET", url, headers=authorization, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        return response.json()

    def GetComment(self, account_id):
        """
        Function lists all comments and their details for an account
        Args:
            account_id (int) = ID of the desired account
        Returns:
            Dictionary of all comments and their details for a desired account
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/accounts/{}/comments'.format(account_id)
        response = requests.request("GET", url, headers=authorization, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        if len(response.text) < 1:
            return {
                "id": "0",
                    "accountId": account_id,
                    "message": "No comments available"
            }
        else:
            return response.json()

class Account:

    def __init__(self, auth):
        self.auth = auth
        self.base_url = auth.api_base_url
        self.response = None
        self.version = auth.version

    def CreateAccount(self, type, name, **kwargs):
        """
        Function creates an account
        Args:
            type (string) = Account type. Options are:
                internal
                revenue
                contractor
                education
                free
            name (string) = Desired name for the account
        Kwargs:
            sapLicenseId (string) = SAP license number
            soldTo (string) = Name of person contract was sold to
            licensee (string) = Purchaser of the resold content
            isActive (bool) = Binary of whether or not the account is activated on creation
            pointsOfContact (list(dict)):
                firstName (string) = First name of the contact
                lastName (string) = Last name of the contact
                emailAddress (string) = Email address of the contact
                country (string) = Country of residence of the contact
                phone (string) = Phone number of the contact
        Returns:
            Dictionary of the created account's details
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/accounts'
        types = {"internal": 15000, "revenue": 15001, "contractor": 15002, "education": 15003, "free": 15004}
        poc = ["firstName", "lastName", "emailAddress", "country", "phone"]
        if type.lower() in types.keys():
            type_name = type
            type = types[type]
        else:
            raise Exception("{} is not a valid account type, please enter a valid account type".format(type))

        payload = {
            "address": {},
            "name": name,
            "pointsOfContact": [
                {}
            ],
            "isActive": False,
            "accountType": {
                "id": type,
                "name": type_name.upper(),
                "description": "Free",
                "createDate": "2022-02-08T16:34:23.062+00:00",
                "updateDate": "2022-02-08T16:34:23.062+00:00"
            }
        }
        for item in kwargs.keys():
            if item in poc:
                payload.update({"pointsOfContact"[0]: payload["pointsOfContact"][0].update({item: kwargs[item]})})
            payload.update({item: kwargs[item]})
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=authorization, data=payload, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        return response.json()

    def UpdateAccount(self, account_id, **kwargs):
        """
        Function updates a desired account
        Args:
            account_id (int) = ID of the desired account
        Kwargs:
            name (string) = Desired name for the account
            sapLicenseId (string) = SAP license number
            soldTo (string) = Name of person contract was sold to
            licensee (string) = Purchaser of the resold content
            isActive (bool) = Binary of whether or not the account is activated on creation
            pointsOfContact (list(dict)):
                firstName (string) = First name of the contact
                lastName (string) = Last name of the contact
                emailAddress (string) = Email address of the contact
                country (string) = Country of residence of the contact
                phone (string) = Phone number of the contact
        Returns:
            Dictionary of the updated account's details
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/accounts'
        account_info = Info.GetAccounts(self, account_id)
        payload = {
            "id": account_id,
            "name": account_info["name"],
            "accountType": account_info["accountType"],
            "sapLicenseId": account_info["sapLicenseId"],
            "soldTo": account_info["soldTo"],
            "licensee": account_info["licensee"],
            "address": account_info["address"],
            "pointsOfContact": account_info["pointsOfContact"],
            "comments": account_info["comments"]
        }
        for item in kwargs.keys():
            if item in account_info["pointsOfContact"][0]:
                payload.update({"pointsOfContact"[0]: payload["pointsOfContact"][0].update({item: kwargs[item]})})
            payload.update({item: kwargs[item]})
        payload = json.dumps(payload)
        response = requests.request("PUT", url, headers=authorization, data=payload, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        return response.json()

    def AddRoles(self, account_number, role_name):
        """
        Function adds a roll or rolls for an account
        Args:
            account_number (string) = Number of the desired account
            role_name (string or list) = Name or names of the desired role. Role names can be found by running the
            GetRoles function in the Info classe
        Returns:
            Dictionary of the updated account's details
        """

        authorization = process.authorization(self.auth)
        roles_info = Info.GetRoles(self)
        role_message = role_name
        if type(role_name) == str:
            role = [i for i in roles_info if i['name'] == role_name.upper()]
            if role:
                role_name = role[0]['name']
                role_id = role[0]['id']
            else:
                raise Exception("{} is not a valid role name. Please enter a valid role name".format(role_name))
            payload = [{
                "id": role_id,
                "name": role_name
            }]
        elif type(role_name) == list:
            role = [i for i in roles_info for j in role_name if i['name'] == j.upper()]
            if len(role_name) != len(role):
                raise Exception("One or more of the provided role names is not valid. Please enter a list of valid role"
                                "names")
            if role:
                payload = []
                for i in role:
                    role_name = i['name']
                    role_id = i['id']
                    payload.append({"id": role_id, "name": role_name})
        payload = json.dumps(payload)
        url = self.base_url + '/accountservice/api/v1/accounts/{}/assignroles'.format(account_number)
        response = requests.request("POST", url, headers=authorization, data=payload, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        return response.json()

    def RemoveRoles(self, account_number, role_name):
        """
        Function removes a roll or rolls for an account
        Args:
            account_number (string) = Number of the desired account
            role_name (string or list) = Name or names of the desired role. Role names can be found by running the
            GetRoles function in the Info classe
        Returns:
            Dictionary of the updated account's details
        """

        authorization = process.authorization(self.auth)
        roles_info = Info.GetRoles(self)
        role_message = role_name
        if type(role_name) == str:
            role = [i for i in roles_info if i['name'] == role_name.upper()]
            if role:
                role_name = role[0]['name']
                role_id = role[0]['id']
            else:
                raise Exception("{} is not a valid role name. Please enter a valid role name".format(role_name))
            payload = [{
                "id": role_id,
                "name": role_name
            }]
        elif type(role_name) == list:
            role = [i for i in roles_info for j in role_name if i['name'] == j.upper()]
            if len(role_name) != len(role):
                raise Exception("One or more of the provided role names is not valid. Please enter a list of valid role"
                                "names")
            if role:
                payload = []
                for i in role:
                    role_name = i['name']
                    role_id = i['id']
                    payload.append({"id": role_id, "name": role_name})
        payload = json.dumps(payload)
        url = self.base_url + '/accountservice/api/v1/accounts/{}/removeroles'.format(account_number)
        response = requests.request("POST", url, headers=authorization, data=payload, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        if type(role_message) == list:
            return "Roles {} successfully removed".format(role_message)
        else:
            return "Role {} successfully removed".format(role_message)

    def DeleteAccount(self, account_id):
        """
        Function deletes an account
        Args:
            account_id (int) = ID of the desired account
        Returns:
            Message of successful deletion
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/accounts?id={}'.format(account_id)
        response = requests.request("DELETE", url, headers=authorization, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        return "Account {} successfully deleted".format(account_id)

class Comment:

    def __init__(self, auth):
        self.auth = auth
        self.base_url = auth.api_base_url
        self.response = None
        self.version = auth.version

    def AddComment(self, account_id, author=None, message=None):
        """
        Function adds a comment to a desired account
        Args:
            account_id (int) = ID of the desired account
            author (string) = Name of the author of the comment. Defaults to None
            message (string) = Desired message for the comment. Defaults to None
        Returns:
            Dictionary of the comment's details
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/accounts/{}/comments'.format(account_id)
        payload = {
            "author": author,
            "message": message
        }
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=authorization, data=payload, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        return response.json()

    def UpdateComment(self, account_id, comment_id, **kwargs):
        """
        Function updates a comment for an account
        Args:
            account_id (int) = ID of the desired account
            comment_id (int) = Id of the desired string
        Kwargs:
            author (string) = Name of the author of the comment
            message (string) = Desired message for the comment
        Returns:
            Dictionary of the updated comment's details
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/accounts/{}/comments/{}'.format(account_id, comment_id)
        comment_info = Info.GetComment(self, account_id)
        for comment in comment_info:
            author = comment['author']
            message = comment['message']
        payload = {
            "id": comment_id,
            "author": author,
            "message": message
        }
        for item in kwargs.keys():
            payload.update({item: kwargs[item]})
        payload = json.dumps(payload)
        response = requests.request("PUT", url, headers=authorization, data=payload, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        return response.json()

    def DeleteComment(self, account_id, comment_id):
        """
        Function deletes a comment
        Args:
            account_id (int) = ID of the desired account
            comment_id (int) = Id of the desired string
        Returns:
            Message of successful deletion
        """

        authorization = process.authorization(self.auth)
        url = self.base_url + '/accountservice/api/v1/accounts/{}/comments/{}'.format(account_id, comment_id)
        response = requests.request("DELETE", url, headers=authorization, verify=self.auth.SSL)
        process_response = process._response_handler(response)
        return "Comment {} successfully deleted".format(comment_id)
