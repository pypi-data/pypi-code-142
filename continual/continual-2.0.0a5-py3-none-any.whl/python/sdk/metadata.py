from __future__ import annotations
from typing import List, Optional

from continual.python.sdk.iterators import Pager
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.events import EventManager
from continual.rpc.management.v1 import (
    management_types_pb2,
    management_pb2,
    types as management_types_py,
)
import json
import numpy as np


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


class MetadataManager(Manager):
    """Manages metadata resources."""

    # the name pattern for metadata depends on the resource it was created for
    name_pattern: str = ""

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
    ) -> List[Metadata]:
        """List metadata.

        Arguments:
            page_size: Number of items to return.

        Returns:
            A list of metadata.
        """
        if not self.client:
            print(f"Cannot list metadata without client")
            return

        req = management_pb2.ListMetadataRequest(
            parent=self.parent,
            page_size=page_size,
            filters=filters,
        )
        resp = self.client._management.ListMetadata(req)
        return [Metadata.from_proto(x, client=self.client) for x in resp.metadata]

    def list_all(self) -> Pager[Metadata]:
        """List all metadata.

        Pages through all metadata using an iterator.

        Returns:
            A iterator of all metadata.
        """

        def next_page(next_page_token):
            req = management_pb2.ListMetadataRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListMetadata(req)
            return (
                [Metadata.from_proto(x, client=self.client) for x in resp.metadata],
                resp.next_page_token,
            )

        return Pager(next_page)

    def get(self, name: str) -> management_types_pb2.Metadata:
        if not self.client:
            print(f"Cannot fetch metadata without client")
            return

        req = management_pb2.GetMetadataRequest(name=name)
        res = self.client._management.GetMetadata(req)
        return res

    def delete(self, name: str):
        if not self.client:
            print(f"Cannot delete metaadata without client")
            return

        req = management_pb2.DeleteMetadataRequest(name=name)
        self.client._management.DeleteMetadata(req)

    def create(
        self,
        data: dict,
        type: str = "MAP",
        group_name: str = "",
    ) -> Metadata:
        """Create metadata.

        Arguments:
            data: the metadata
            type: the type of metadata
            group_name: the group the metadata is associated with

        Returns
            Metadata.
        """
        req = management_pb2.CreateMetadataRequest(
            parent=self.parent,
            metadata=management_types_pb2.Metadata(
                data=json.dumps(data, cls=NpEncoder),
                type=type,
                group_name=group_name,
            ),
        )
        resp = self.client._management.CreateMetadata(req)
        return Metadata.from_proto(resp, client=self.client)


class Metadata(Resource, management_types_py.Metadata):
    """Metadata resource."""

    # the name pattern for metadata depends on the resource it was created for
    name_pattern: str = ""
    manager: MetadataManager

    events: EventManager
    """Event manager."""

    def _init(self):
        self.manager = MetadataManager(parent=self.parent, client=self.client)
