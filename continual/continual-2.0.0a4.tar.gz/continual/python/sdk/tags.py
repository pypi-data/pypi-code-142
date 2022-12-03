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


class TagsManager(Manager):
    """Manages tag resources."""

    # the name pattern for tags depends on the resource it was created for
    name_pattern: str = ""

    def list(
        self,
        page_size: Optional[int] = None,
        filters: List[str] = None,
    ) -> List[Tag]:
        """List tags.

        Arguments:
            page_size: Number of items to return.

        Returns:
            A list of tags.
        """
        if not self.client:
            print(f"Cannot list tags without client")
            return

        req = management_pb2.ListTagsRequest(
            parent=self.parent,
            page_size=page_size,
            filters=filters,
        )
        resp = self.client._management.ListTags(req)
        return [Tag.from_proto(x, client=self.client) for x in resp.tags]

    def list_all(self) -> Pager[Tag]:
        """List all tags.

        Pages through all tags using an iterator.

        Returns:
            A iterator of all tag.
        """

        def next_page(next_page_token):
            req = management_pb2.ListTagsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListTags(req)
            return (
                [Tag.from_proto(x, client=self.client) for x in resp.tags],
                resp.next_page_token,
            )

        return Pager(next_page)

    def get(self, name: str, key: str) -> management_types_pb2.Tag:
        if not self.client:
            print(f"Cannot fetch tag without client")
            return

        req = management_pb2.GetTagRequest(resource_name=name, key=key)
        res = self.client._management.GetTag(req)
        return res

    def delete(self, name: str):
        if not self.client:
            print(f"Cannot delete tag without client")
            return

        req = management_pb2.DeleteTagRequest(name=name)
        self.client._management.DeleteTag(req)

    def create(
        self,
        key: str,
        value: str,
    ) -> Tag:
        """Create tag.

        Arguments:
            key: the tag key
            value: the tag value

        Returns
            A tag.
        """
        req = management_pb2.CreateTagRequest(
            parent=self.parent,
            key=key,
            value=str(value),
        )
        resp = self.client._management.CreateTag(req)
        return Tag.from_proto(resp, client=self.client)


class Tag(Resource, management_types_py.Tag):
    """Tag resource."""

    # the name pattern for tags depends on the resource it was created for
    name_pattern: str = ""
    manager: TagsManager

    events: EventManager
    """Event manager."""

    def _init(self):
        self.manager = TagsManager(parent=self.parent, client=self.client)
