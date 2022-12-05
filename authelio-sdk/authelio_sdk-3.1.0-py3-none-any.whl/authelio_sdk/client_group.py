from typing import Any, Dict, Optional, List, Tuple

from authelio_sdk.client_base import ClientBase
from authelio_sdk.config import Config
from authelio_sdk.models.group import Group


class ClientGroup(ClientBase):
    def __init__(
            self,
            api_key: str,
            api_secret: str,
            config: Config
    ) -> None:
        super().__init__(api_key, api_secret, config)

    def get(self, *group_ids: str) -> Dict[str, Group]:
        parameters = [('group_id', group_id) for group_id in group_ids]
        groups_data = self.http_endpoint(
            path='/group/get',
            method='GET',
            fields=parameters
        ).call_to_json()

        return {
            group_id: Group(
                group_id=group['group_id'],
                group_name=group['group_name'],
                permissions=group['permissions']
            )
            for group_id, group in groups_data.items()
        }

    def delete(self, group_id: str) -> None:
        self.http_endpoint(
            path='/group/delete',
            method='DELETE',
            body={
                'group_id': group_id
            }
        ).call_to_response()

    def create(self, group_name: str, permissions: List[str], group_id: Optional[str] = None) -> Group:
        body = {
            'group_name': group_name,
            'permissions': permissions
        }

        if group_id:
            body['group_id'] = group_id

        group_json = self.http_endpoint(
            path='/group/create',
            method='POST',
            body=body
        ).call_to_json()

        return Group(
            group_id=group_json['group_id'],
            group_name=group_json['group_name'],
            permissions=group_json['permissions']
        )

    def filter(
            self,
            count: Optional[int] = None,
            page_id: Optional[str] = None
    ) -> Tuple[Dict[str, Group], str]:
        parameters = {
            'count': count,
            'page_id': page_id
        }
        parameters = {key: value for key, value in parameters.items() if value is not None}

        groups_json: Dict[str, Any] = self.http_endpoint(
            path='/group/filter',
            method='GET',
            fields=parameters
        ).call_to_json()

        groups = {
            key: Group(
                group_id=group['group_id'],
                group_name=group['group_name'],
                permissions=group['permissions']
            ) for key, group in groups_json['results'].items()
        }

        return groups, groups_json['next_page_id']

    def update(self, group_id: str, group_name: Optional[str] = None, permissions: Optional[List[str]] = None) -> None:
        body = {
            'group_id': group_id,
            'group_name': group_name,
            'permissions': permissions
        }
        body = {key: value for key, value in body.items() if value is not None}

        self.http_endpoint(
            path='/group/update',
            method='PUT',
            body=body
        ).call_to_response()

    def users(self, *group_ids: str) -> List[str]:
        parameters = [('group_id', group_id) for group_id in group_ids]

        return self.http_endpoint(
            path='/group/users',
            method='GET',
            fields=parameters
        ).call_to_json()['users']
