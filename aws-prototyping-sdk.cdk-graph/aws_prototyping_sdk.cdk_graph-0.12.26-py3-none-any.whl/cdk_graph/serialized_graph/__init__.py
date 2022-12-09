import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs
from .. import (
    ConstructInfo as _ConstructInfo_e912d4bb,
    EdgeDirectionEnum as _EdgeDirectionEnum_26ef4ba3,
    EdgeTypeEnum as _EdgeTypeEnum_1b13d7ee,
    FlagEnum as _FlagEnum_af90e158,
    NodeTypeEnum as _NodeTypeEnum_d56eed04,
)


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.Attributes",
    jsii_struct_bases=[],
    name_mapping={},
)
class Attributes:
    def __init__(self) -> None:
        '''(experimental) Serializable attributes mapping.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Attributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.Edge",
    jsii_struct_bases=[Entity],
    name_mapping={
        "uuid": "uuid",
        "attributes": "attributes",
        "flags": "flags",
        "metadata": "metadata",
        "tags": "tags",
        "direction": "direction",
        "edge_type": "edgeType",
        "source": "source",
        "target": "target",
    },
)
class Edge(Entity):
    def __init__(
        self,
        *,
        uuid: builtins.str,
        attributes: typing.Optional[typing.Union[Attributes, typing.Dict[str, typing.Any]]] = None,
        flags: typing.Optional[typing.Sequence[_FlagEnum_af90e158]] = None,
        metadata: typing.Optional[typing.Sequence[typing.Union[constructs.MetadataEntry, typing.Dict[str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Union["Tags", typing.Dict[str, typing.Any]]] = None,
        direction: _EdgeDirectionEnum_26ef4ba3,
        edge_type: _EdgeTypeEnum_1b13d7ee,
        source: builtins.str,
        target: builtins.str,
    ) -> None:
        '''(experimental) Serializable graph edge entity.

        :param uuid: (experimental) Universally unique identity.
        :param attributes: (experimental) Serializable entity attributes.
        :param flags: (experimental) Serializable entity flags.
        :param metadata: (experimental) Serializable entity metadata.
        :param tags: (experimental) Serializable entity tags.
        :param direction: (experimental) Indicates the direction in which the edge is directed.
        :param edge_type: (experimental) Type of edge.
        :param source: (experimental) UUID of edge **source** node (tail).
        :param target: (experimental) UUID of edge **target** node (head).

        :stability: experimental
        '''
        if isinstance(attributes, dict):
            attributes = Attributes(**attributes)
        if isinstance(tags, dict):
            tags = Tags(**tags)
        if __debug__:
            def stub(
                *,
                uuid: builtins.str,
                attributes: typing.Optional[typing.Union[Attributes, typing.Dict[str, typing.Any]]] = None,
                flags: typing.Optional[typing.Sequence[_FlagEnum_af90e158]] = None,
                metadata: typing.Optional[typing.Sequence[typing.Union[constructs.MetadataEntry, typing.Dict[str, typing.Any]]]] = None,
                tags: typing.Optional[typing.Union[Tags, typing.Dict[str, typing.Any]]] = None,
                direction: _EdgeDirectionEnum_26ef4ba3,
                edge_type: _EdgeTypeEnum_1b13d7ee,
                source: builtins.str,
                target: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uuid", value=uuid, expected_type=type_hints["uuid"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument flags", value=flags, expected_type=type_hints["flags"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
            check_type(argname="argument edge_type", value=edge_type, expected_type=type_hints["edge_type"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "uuid": uuid,
            "direction": direction,
            "edge_type": edge_type,
            "source": source,
            "target": target,
        }
        if attributes is not None:
            self._values["attributes"] = attributes
        if flags is not None:
            self._values["flags"] = flags
        if metadata is not None:
            self._values["metadata"] = metadata
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def uuid(self) -> builtins.str:
        '''(experimental) Universally unique identity.

        :stability: experimental
        '''
        result = self._values.get("uuid")
        assert result is not None, "Required property 'uuid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[Attributes]:
        '''(experimental) Serializable entity attributes.

        :see: {@link Attributes}
        :stability: experimental
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[Attributes], result)

    @builtins.property
    def flags(self) -> typing.Optional[typing.List[_FlagEnum_af90e158]]:
        '''(experimental) Serializable entity flags.

        :see: {@link FlagEnum}
        :stability: experimental
        '''
        result = self._values.get("flags")
        return typing.cast(typing.Optional[typing.List[_FlagEnum_af90e158]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.List[constructs.MetadataEntry]]:
        '''(experimental) Serializable entity metadata.

        :see: {@link Metadata}
        :stability: experimental
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.List[constructs.MetadataEntry]], result)

    @builtins.property
    def tags(self) -> typing.Optional["Tags"]:
        '''(experimental) Serializable entity tags.

        :see: {@link Tags}
        :stability: experimental
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["Tags"], result)

    @builtins.property
    def direction(self) -> _EdgeDirectionEnum_26ef4ba3:
        '''(experimental) Indicates the direction in which the edge is directed.

        :stability: experimental
        '''
        result = self._values.get("direction")
        assert result is not None, "Required property 'direction' is missing"
        return typing.cast(_EdgeDirectionEnum_26ef4ba3, result)

    @builtins.property
    def edge_type(self) -> _EdgeTypeEnum_1b13d7ee:
        '''(experimental) Type of edge.

        :stability: experimental
        '''
        result = self._values.get("edge_type")
        assert result is not None, "Required property 'edge_type' is missing"
        return typing.cast(_EdgeTypeEnum_1b13d7ee, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''(experimental) UUID of edge **source**  node (tail).

        :stability: experimental
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''(experimental) UUID of edge **target**  node (head).

        :stability: experimental
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Edge(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.Entity",
    jsii_struct_bases=[],
    name_mapping={
        "uuid": "uuid",
        "attributes": "attributes",
        "flags": "flags",
        "metadata": "metadata",
        "tags": "tags",
    },
)
class Entity:
    def __init__(
        self,
        *,
        uuid: builtins.str,
        attributes: typing.Optional[typing.Union[Attributes, typing.Dict[str, typing.Any]]] = None,
        flags: typing.Optional[typing.Sequence[_FlagEnum_af90e158]] = None,
        metadata: typing.Optional[typing.Sequence[typing.Union[constructs.MetadataEntry, typing.Dict[str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Union["Tags", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Serializable graph entity.

        :param uuid: (experimental) Universally unique identity.
        :param attributes: (experimental) Serializable entity attributes.
        :param flags: (experimental) Serializable entity flags.
        :param metadata: (experimental) Serializable entity metadata.
        :param tags: (experimental) Serializable entity tags.

        :stability: experimental
        '''
        if isinstance(attributes, dict):
            attributes = Attributes(**attributes)
        if isinstance(tags, dict):
            tags = Tags(**tags)
        if __debug__:
            def stub(
                *,
                uuid: builtins.str,
                attributes: typing.Optional[typing.Union[Attributes, typing.Dict[str, typing.Any]]] = None,
                flags: typing.Optional[typing.Sequence[_FlagEnum_af90e158]] = None,
                metadata: typing.Optional[typing.Sequence[typing.Union[constructs.MetadataEntry, typing.Dict[str, typing.Any]]]] = None,
                tags: typing.Optional[typing.Union[Tags, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uuid", value=uuid, expected_type=type_hints["uuid"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument flags", value=flags, expected_type=type_hints["flags"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "uuid": uuid,
        }
        if attributes is not None:
            self._values["attributes"] = attributes
        if flags is not None:
            self._values["flags"] = flags
        if metadata is not None:
            self._values["metadata"] = metadata
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def uuid(self) -> builtins.str:
        '''(experimental) Universally unique identity.

        :stability: experimental
        '''
        result = self._values.get("uuid")
        assert result is not None, "Required property 'uuid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[Attributes]:
        '''(experimental) Serializable entity attributes.

        :see: {@link Attributes}
        :stability: experimental
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[Attributes], result)

    @builtins.property
    def flags(self) -> typing.Optional[typing.List[_FlagEnum_af90e158]]:
        '''(experimental) Serializable entity flags.

        :see: {@link FlagEnum}
        :stability: experimental
        '''
        result = self._values.get("flags")
        return typing.cast(typing.Optional[typing.List[_FlagEnum_af90e158]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.List[constructs.MetadataEntry]]:
        '''(experimental) Serializable entity metadata.

        :see: {@link Metadata}
        :stability: experimental
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.List[constructs.MetadataEntry]], result)

    @builtins.property
    def tags(self) -> typing.Optional["Tags"]:
        '''(experimental) Serializable entity tags.

        :see: {@link Tags}
        :stability: experimental
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["Tags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Entity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.GraphStore",
    jsii_struct_bases=[],
    name_mapping={"edges": "edges", "tree": "tree", "version": "version"},
)
class GraphStore:
    def __init__(
        self,
        *,
        edges: typing.Sequence[typing.Union[Edge, typing.Dict[str, typing.Any]]],
        tree: typing.Union["Node", typing.Dict[str, typing.Any]],
        version: builtins.str,
    ) -> None:
        '''(experimental) Serializable graph store.

        :param edges: (experimental) List of edges.
        :param tree: (experimental) Node tree.
        :param version: (experimental) Store version.

        :stability: experimental
        '''
        if isinstance(tree, dict):
            tree = Node(**tree)
        if __debug__:
            def stub(
                *,
                edges: typing.Sequence[typing.Union[Edge, typing.Dict[str, typing.Any]]],
                tree: typing.Union[Node, typing.Dict[str, typing.Any]],
                version: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edges", value=edges, expected_type=type_hints["edges"])
            check_type(argname="argument tree", value=tree, expected_type=type_hints["tree"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "edges": edges,
            "tree": tree,
            "version": version,
        }

    @builtins.property
    def edges(self) -> typing.List[Edge]:
        '''(experimental) List of edges.

        :stability: experimental
        '''
        result = self._values.get("edges")
        assert result is not None, "Required property 'edges' is missing"
        return typing.cast(typing.List[Edge], result)

    @builtins.property
    def tree(self) -> "Node":
        '''(experimental) Node tree.

        :stability: experimental
        '''
        result = self._values.get("tree")
        assert result is not None, "Required property 'tree' is missing"
        return typing.cast("Node", result)

    @builtins.property
    def version(self) -> builtins.str:
        '''(experimental) Store version.

        :stability: experimental
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphStore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.ISerializableEdge"
)
class ISerializableEdge(typing_extensions.Protocol):
    '''(experimental) Interface for serializable graph edge entity.

    :stability: experimental
    '''

    pass


class _ISerializableEdgeProxy:
    '''(experimental) Interface for serializable graph edge entity.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.SerializedGraph.ISerializableEdge"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISerializableEdge).__jsii_proxy_class__ = lambda : _ISerializableEdgeProxy


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.ISerializableEntity"
)
class ISerializableEntity(typing_extensions.Protocol):
    '''(experimental) Interface for serializable graph entities.

    :stability: experimental
    '''

    pass


class _ISerializableEntityProxy:
    '''(experimental) Interface for serializable graph entities.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.SerializedGraph.ISerializableEntity"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISerializableEntity).__jsii_proxy_class__ = lambda : _ISerializableEntityProxy


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.ISerializableGraphStore"
)
class ISerializableGraphStore(typing_extensions.Protocol):
    '''(experimental) Interface for serializable graph store.

    :stability: experimental
    '''

    @jsii.member(jsii_name="serialize")
    def serialize(self) -> GraphStore:
        '''
        :stability: experimental
        '''
        ...


class _ISerializableGraphStoreProxy:
    '''(experimental) Interface for serializable graph store.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.SerializedGraph.ISerializableGraphStore"

    @jsii.member(jsii_name="serialize")
    def serialize(self) -> GraphStore:
        '''
        :stability: experimental
        '''
        return typing.cast(GraphStore, jsii.invoke(self, "serialize", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISerializableGraphStore).__jsii_proxy_class__ = lambda : _ISerializableGraphStoreProxy


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.ISerializableNode"
)
class ISerializableNode(typing_extensions.Protocol):
    '''(experimental) Interface for serializable graph node entity.

    :stability: experimental
    '''

    pass


class _ISerializableNodeProxy:
    '''(experimental) Interface for serializable graph node entity.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.SerializedGraph.ISerializableNode"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISerializableNode).__jsii_proxy_class__ = lambda : _ISerializableNodeProxy


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.Node",
    jsii_struct_bases=[Entity],
    name_mapping={
        "uuid": "uuid",
        "attributes": "attributes",
        "flags": "flags",
        "metadata": "metadata",
        "tags": "tags",
        "id": "id",
        "node_type": "nodeType",
        "path": "path",
        "cfn_type": "cfnType",
        "children": "children",
        "construct_info": "constructInfo",
        "edges": "edges",
        "logical_id": "logicalId",
        "parent": "parent",
        "stack": "stack",
    },
)
class Node(Entity):
    def __init__(
        self,
        *,
        uuid: builtins.str,
        attributes: typing.Optional[typing.Union[Attributes, typing.Dict[str, typing.Any]]] = None,
        flags: typing.Optional[typing.Sequence[_FlagEnum_af90e158]] = None,
        metadata: typing.Optional[typing.Sequence[typing.Union[constructs.MetadataEntry, typing.Dict[str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Union["Tags", typing.Dict[str, typing.Any]]] = None,
        id: builtins.str,
        node_type: _NodeTypeEnum_d56eed04,
        path: builtins.str,
        cfn_type: typing.Optional[builtins.str] = None,
        children: typing.Optional[typing.Mapping[builtins.str, typing.Union["Node", typing.Dict[str, typing.Any]]]] = None,
        construct_info: typing.Optional[typing.Union[_ConstructInfo_e912d4bb, typing.Dict[str, typing.Any]]] = None,
        edges: typing.Optional[typing.Sequence[builtins.str]] = None,
        logical_id: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        stack: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Serializable graph node entity.

        :param uuid: (experimental) Universally unique identity.
        :param attributes: (experimental) Serializable entity attributes.
        :param flags: (experimental) Serializable entity flags.
        :param metadata: (experimental) Serializable entity metadata.
        :param tags: (experimental) Serializable entity tags.
        :param id: (experimental) Node id within parent (unique only between parent child nodes).
        :param node_type: (experimental) Node type.
        :param path: (experimental) Node path.
        :param cfn_type: (experimental) CloudFormation resource type for this node.
        :param children: (experimental) Child node record.
        :param construct_info: (experimental) Synthesized construct information defining jii resolution data.
        :param edges: (experimental) List of edge UUIDs where this node is the **source**.
        :param logical_id: (experimental) Logical id of the node, which is only unique within containing stack.
        :param parent: (experimental) UUID of node parent.
        :param stack: (experimental) UUID of node stack.

        :stability: experimental
        '''
        if isinstance(attributes, dict):
            attributes = Attributes(**attributes)
        if isinstance(tags, dict):
            tags = Tags(**tags)
        if isinstance(construct_info, dict):
            construct_info = _ConstructInfo_e912d4bb(**construct_info)
        if __debug__:
            def stub(
                *,
                uuid: builtins.str,
                attributes: typing.Optional[typing.Union[Attributes, typing.Dict[str, typing.Any]]] = None,
                flags: typing.Optional[typing.Sequence[_FlagEnum_af90e158]] = None,
                metadata: typing.Optional[typing.Sequence[typing.Union[constructs.MetadataEntry, typing.Dict[str, typing.Any]]]] = None,
                tags: typing.Optional[typing.Union[Tags, typing.Dict[str, typing.Any]]] = None,
                id: builtins.str,
                node_type: _NodeTypeEnum_d56eed04,
                path: builtins.str,
                cfn_type: typing.Optional[builtins.str] = None,
                children: typing.Optional[typing.Mapping[builtins.str, typing.Union[Node, typing.Dict[str, typing.Any]]]] = None,
                construct_info: typing.Optional[typing.Union[_ConstructInfo_e912d4bb, typing.Dict[str, typing.Any]]] = None,
                edges: typing.Optional[typing.Sequence[builtins.str]] = None,
                logical_id: typing.Optional[builtins.str] = None,
                parent: typing.Optional[builtins.str] = None,
                stack: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uuid", value=uuid, expected_type=type_hints["uuid"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument flags", value=flags, expected_type=type_hints["flags"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument cfn_type", value=cfn_type, expected_type=type_hints["cfn_type"])
            check_type(argname="argument children", value=children, expected_type=type_hints["children"])
            check_type(argname="argument construct_info", value=construct_info, expected_type=type_hints["construct_info"])
            check_type(argname="argument edges", value=edges, expected_type=type_hints["edges"])
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
        self._values: typing.Dict[str, typing.Any] = {
            "uuid": uuid,
            "id": id,
            "node_type": node_type,
            "path": path,
        }
        if attributes is not None:
            self._values["attributes"] = attributes
        if flags is not None:
            self._values["flags"] = flags
        if metadata is not None:
            self._values["metadata"] = metadata
        if tags is not None:
            self._values["tags"] = tags
        if cfn_type is not None:
            self._values["cfn_type"] = cfn_type
        if children is not None:
            self._values["children"] = children
        if construct_info is not None:
            self._values["construct_info"] = construct_info
        if edges is not None:
            self._values["edges"] = edges
        if logical_id is not None:
            self._values["logical_id"] = logical_id
        if parent is not None:
            self._values["parent"] = parent
        if stack is not None:
            self._values["stack"] = stack

    @builtins.property
    def uuid(self) -> builtins.str:
        '''(experimental) Universally unique identity.

        :stability: experimental
        '''
        result = self._values.get("uuid")
        assert result is not None, "Required property 'uuid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[Attributes]:
        '''(experimental) Serializable entity attributes.

        :see: {@link Attributes}
        :stability: experimental
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[Attributes], result)

    @builtins.property
    def flags(self) -> typing.Optional[typing.List[_FlagEnum_af90e158]]:
        '''(experimental) Serializable entity flags.

        :see: {@link FlagEnum}
        :stability: experimental
        '''
        result = self._values.get("flags")
        return typing.cast(typing.Optional[typing.List[_FlagEnum_af90e158]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.List[constructs.MetadataEntry]]:
        '''(experimental) Serializable entity metadata.

        :see: {@link Metadata}
        :stability: experimental
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.List[constructs.MetadataEntry]], result)

    @builtins.property
    def tags(self) -> typing.Optional["Tags"]:
        '''(experimental) Serializable entity tags.

        :see: {@link Tags}
        :stability: experimental
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["Tags"], result)

    @builtins.property
    def id(self) -> builtins.str:
        '''(experimental) Node id within parent (unique only between parent child nodes).

        :stability: experimental
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_type(self) -> _NodeTypeEnum_d56eed04:
        '''(experimental) Node type.

        :stability: experimental
        '''
        result = self._values.get("node_type")
        assert result is not None, "Required property 'node_type' is missing"
        return typing.cast(_NodeTypeEnum_d56eed04, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''(experimental) Node path.

        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cfn_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) CloudFormation resource type for this node.

        :stability: experimental
        '''
        result = self._values.get("cfn_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def children(self) -> typing.Optional[typing.Mapping[builtins.str, "Node"]]:
        '''(experimental) Child node record.

        :stability: experimental
        '''
        result = self._values.get("children")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "Node"]], result)

    @builtins.property
    def construct_info(self) -> typing.Optional[_ConstructInfo_e912d4bb]:
        '''(experimental) Synthesized construct information defining jii resolution data.

        :stability: experimental
        '''
        result = self._values.get("construct_info")
        return typing.cast(typing.Optional[_ConstructInfo_e912d4bb], result)

    @builtins.property
    def edges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of edge UUIDs where this node is the **source**.

        :stability: experimental
        '''
        result = self._values.get("edges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logical_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) Logical id of the node, which is only unique within containing stack.

        :stability: experimental
        '''
        result = self._values.get("logical_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent(self) -> typing.Optional[builtins.str]:
        '''(experimental) UUID of node parent.

        :stability: experimental
        '''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stack(self) -> typing.Optional[builtins.str]:
        '''(experimental) UUID of node stack.

        :stability: experimental
        '''
        result = self._values.get("stack")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Node(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.PlainObject",
    jsii_struct_bases=[],
    name_mapping={},
)
class PlainObject:
    def __init__(self) -> None:
        '''(experimental) Serializable plain object value (JSII supported).

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlainObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.SerializedGraph.Tags",
    jsii_struct_bases=[],
    name_mapping={},
)
class Tags:
    def __init__(self) -> None:
        '''(experimental) Serializable dictionary of tags (key value pairs).

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Tags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Attributes",
    "Edge",
    "Entity",
    "GraphStore",
    "ISerializableEdge",
    "ISerializableEntity",
    "ISerializableGraphStore",
    "ISerializableNode",
    "Node",
    "PlainObject",
    "Tags",
]

publication.publish()
