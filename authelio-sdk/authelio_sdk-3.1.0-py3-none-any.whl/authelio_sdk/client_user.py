from typing import Optional, List, Dict, Tuple

from b_lambda_layer_common.util.http_endpoint import HttpCall

from authelio_sdk.client_base import ClientBase
from authelio_sdk.config import Config
from authelio_sdk.models.token import Token
from authelio_sdk.models.user import User


class ClientUser(ClientBase):
    def __init__(
            self,
            api_key: str,
            api_secret: str,
            config: Config
    ) -> None:
        super().__init__(api_key, api_secret, config)

    def get(self, *user_ids: str) -> Dict[str, User]:
        parameters = [('user_id', user_id) for user_id in user_ids]
        users_data = self.http_endpoint(
            path='/user/get',
            method='GET',
            fields=parameters
        ).call_to_json()

        return {
            user_id: User(
                # Unique identifiers.
                user_id=user['user_id'],
                username=user['username'],
                email=user['email'],
                # Other personal data.
                first_name=user['first_name'],
                last_name=user['last_name'],
                # User status.
                is_active=user['is_active'],
                # Permissions.
                direct_permissions=user['direct_permissions'],
                group_ids=user['group_ids']
            )
            for user_id, user in users_data.items()
        }

    def delete(self, user_id: str) -> None:
        self.http_endpoint(
            path='/user/delete',
            method='DELETE',
            body={
                'user_id': user_id,
            }
        ).call_to_response()

    def create(
            self,
            email: str,
            first_name: str,
            last_name: str,
            user_id: Optional[str] = None,
            username: Optional[str] = None,
            group_ids: Optional[List[str]] = None,
            direct_permissions: Optional[List[str]] = None,
            auth_type: Optional[str] = None
    ) -> User:
        group_ids = group_ids or []
        direct_permissions = direct_permissions or []

        body = {
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'group_ids': group_ids,
                'direct_permissions': direct_permissions
            }
        if user_id: body.update(user_id=user_id)
        if username: body.update(username=username)
        if auth_type: body.update(auth_type=auth_type)

        user_json = self.http_endpoint(
            path='/user/create',
            method='POST',
            body=body
        ).call_to_json()

        return User(
            group_ids=group_ids,
            user_id=user_json['user_id'],
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            tmp_password=user_json['tmp_password'],
            direct_permissions=direct_permissions,
            auth_type=auth_type
        )

    def enable(self, user_id: str) -> None:
        self.http_endpoint(
            path='/user/enable',
            method='POST',
            body={
                'user_id': user_id
            }
        ).call_to_response()

    def disable(self, user_id: str) -> None:
        self.http_endpoint(
            path='/user/disable',
            method='POST',
            body={
                'user_id': user_id
            }
        ).call_to_response()

    def update(
            self,
            user_id: str,
            email: Optional[str] = None,
            username: Optional[str] = None,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            group_ids: Optional[List[str]] = None,
            direct_permissions: Optional[List[str]] = None
    ) -> None:
        body = {
            'user_id': user_id,
            'email': email,
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'group_ids': group_ids,
            'direct_permissions': direct_permissions
        }
        body = {key: value for key, value in body.items() if value is not None}

        self.http_endpoint(
            path='/user/update',
            method='PUT',
            body=body
        ).call_to_response()

    def filter(
            self,
            is_active: Optional[bool] = None,
            count: Optional[int] = None,
            page_id: Optional[str] = None
    ) -> Tuple[Dict[str, User], str]:
        parameters = {
            'is_active': is_active,
            'count': count,
            'page_id': page_id
        }
        parameters = {key: value for key, value in parameters.items() if value is not None}

        response_body_json = self.http_endpoint(
            path='/user/filter',
            method='GET',
            fields=parameters
        ).call_to_json()

        users = {
            user_id: User(
                user_id=user['user_id'],
                username=user['username'],
                email=user['email'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                group_ids=user['group_ids'],
                direct_permissions=user['direct_permissions']
            )
            for user_id, user in response_body_json['results'].items()
        }

        return users, response_body_json['next_page_id']

    def confirm(self, username: str, tmp_password: str, new_password: str) -> None:
        token_json = self.http_endpoint(
            path='/token/create',
            method='POST',
            body={
                'username': username,
                'password': tmp_password
            }
        ).call_to_json()

        if token_json['is_challenge'] is True:
            token_json = self.http_endpoint(
                path='/token/challenge',
                method='POST',
                body={
                    'challenge_name': token_json['challenge']['challenge_name'],
                    'challenge_session': token_json['challenge']['session'],
                    'challenge_response': {
                        'USERNAME': username,
                        'NEW_PASSWORD': new_password
                    }
                }
            ).call_to_json()

        try:
            access_token = token_json['authentication']['access_token']
        except (KeyError, ValueError):
            access_token = None

        if not access_token:
            raise ValueError(
                'Something went wrong. '
                'Access token was not created, hence, the new user probably was not confirmed. '
                'Please try again, or contact administrators.'
            )

    def validate_token(self, access_token: str) -> bool:
        response = self.http_endpoint(
            path='/token/validate',
            method='POST',
            body={
                'access_token': access_token
            }
        ).call_to_json()

        return response['valid']

    def create_token(self, username: str, password: str) -> Token:
        token_json = self.http_endpoint(
            path='/token/create',
            method='POST',
            body={
                'username': username,
                'password': password
            }
        ).call_to_json()

        if token_json['is_challenge'] is True:
            raise ValueError(
                f'User was not confirmed. '
                f'Please confirm user first, before creating tokens. '
                f'Hint: to confirm user, call "{ClientUser.__name__}.{ClientUser.confirm.__name__}" method.'
            )

        return Token(**token_json['authentication'])

    def exchange_auth_code(self, authorization_code: str, redirect_uri: Optional[str] = None) -> Token:
        token_json = self.http_endpoint(
            path='/token/create',
            method='POST',
            body={
                'authorization_code': authorization_code,
                'redirect_uri': redirect_uri
            }
        ).call_to_json()

        return Token(**token_json['authentication'])

    def refresh_token(self, refresh_token: str) -> Token:
        token_json = self.http_endpoint(
            path='/token/refresh',
            method='POST',
            body={
                'refresh_token': refresh_token
            }
        ).call_to_json()

        return Token(**token_json)

    def permissions(self, user_id: str) -> List[str]:
        permissions = self.http_endpoint(
            path='/permission/get',
            method='GET',
            fields={
                'user_id': user_id
            }
        ).call_to_json()

        return permissions['permissions']

    def login(self, redirect_uri: Optional[str] = None, response_type: Optional[str] = None) -> str:
        parameters = {
            'redirect_uri': redirect_uri,
            'response_type': response_type
        }
        parameters = {key: value for key, value in parameters.items() if value is not None}

        response = HttpCall.call(
            method='GET',
            url=f'{self.config.public_api_url}/login',
            fields=parameters,
            headers=self.basic_auth_header,
            redirect=False
        )

        return response.headers['location']
