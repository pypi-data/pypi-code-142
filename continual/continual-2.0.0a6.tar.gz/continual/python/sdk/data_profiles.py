from __future__ import annotations
from typing import List, Optional
from continual.python.sdk.iterators import Pager

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.events import EventManager


class DataProfilesManager(Manager):
    """Manages data_profile resources."""

    name_pattern: str = "projects/{project}/datasets/{dataset}/dataset_versions/{version}/data_profiles/{data_profile}"

    def get(self, id: str) -> DataProfile:
        """Get data_profile.

        Arguments:
            id: DataProfile name or id.

        Returns
            A data_profile.
        """

        req = management_pb2.GetDataProfileRequest(name=self.name(id))
        data_profile = self.client._management.GetDataProfile(req)
        return DataProfile.from_proto(data_profile, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
    ) -> List[DataProfile]:
        """List data_profiles.

        Arguments:
            resource_name: string name of the object on which data_profiles reside
            page_size: Number of items to return.

        Returns:
            A list of data_profiles.
        """
        req = management_pb2.ListDataProfilesRequest(
            parent=self.parent, page_size=page_size
        )
        resp = self.client._management.ListDataProfiles(req)
        return [
            DataProfile.from_proto(x, client=self.client) for x in resp.data_profiles
        ]

    def list_all(self, resource_name: str) -> Pager[DataProfile]:
        """List all data_profiles.

        Pages through all data_profiles using an iterator.

        Returns:
            A iterator of all data_profiles.
        """

        def next_page(next_page_token):
            req = management_pb2.ListDataProfilesRequest(
                resource_name=resource_name, page_token=next_page_token
            )
            resp = self.client._management.ListDataProfiles(req)
            return (
                [
                    DataProfile.from_proto(x, client=self.client)
                    for x in resp.data_profiles
                ],
                resp.next_page_token,
            )

        return Pager(next_page)

    def create(self, data_profile: DataProfile):
        """Create an data_profile.

        Arguments:
            data_profile

        Returns:
            A new data_profile.
        """
        req = management_pb2.CreateDataProfileRequest(
            parent=self.parent,
            data_profile=data_profile.to_proto(),
        )

        resp = self.client._management.CreateDataProfile(req)
        return DataProfile.from_proto(resp, client=self.client)

    def update(self, data_profile: DataProfile, update_paths: List[str]):
        """Update a data profile

        Arguments:
            data_profile: DataProfile
            update_paths: The fields to update
        """

        req = management_pb2.UpdateDataProfileRequest(
            data_profile=data_profile.to_proto(), update_paths=update_paths
        )

        resp = self.client._management.UpdateDataProfile(req)
        return DataProfile.from_proto(resp, client=self.client)


class DataProfile(Resource, types.DataProfile):
    """DataProfile resource."""

    name_pattern: str = "projects/{project}/datasets/{dataset}/dataset_versions/{version}/data_profiles/{data_profile}"
    manager: DataProfilesManager

    events: EventManager
    """Event manager."""

    def _init(self):
        self.manager = DataProfilesManager(parent=self.parent, client=self.client)
