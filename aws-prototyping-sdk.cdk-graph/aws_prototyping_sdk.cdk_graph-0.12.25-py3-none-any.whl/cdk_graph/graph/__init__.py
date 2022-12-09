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
    ICounterRecord as _ICounterRecord_97e6658c,
    NodeTypeEnum as _NodeTypeEnum_d56eed04,
    ReferenceTypeEnum as _ReferenceTypeEnum_f84a272a,
)
from ..serialized_graph import (
    Attributes as _Attributes_b47661e3,
    Edge as _Edge_211392d6,
    GraphStore as _GraphStore_ffbd5720,
    ISerializableEdge as _ISerializableEdge_afcbbd54,
    ISerializableEntity as _ISerializableEntity_0dbfd411,
    ISerializableGraphStore as _ISerializableGraphStore_4640156f,
    ISerializableNode as _ISerializableNode_9eb400fa,
    Node as _Node_bc073df3,
    PlainObject as _PlainObject_c976ebcc,
    Tags as _Tags_cf30c388,
)


class AppNode(
    Node,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.AppNode",
):
    '''(experimental) AppNode defines a cdk App.

    :stability: experimental
    '''

    def __init__(self, props: "IAppNodeProps") -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: IAppNodeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isAppNode")
    @builtins.classmethod
    def is_app_node(cls, node: "Node") -> builtins.bool:
        '''(experimental) Indicates if node is a {@link AppNode}.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isAppNode", [node]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PATH")
    def PATH(cls) -> builtins.str:
        '''(experimental) Fixed path of the App.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PATH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="UUID")
    def UUID(cls) -> builtins.str:
        '''(experimental) Fixed UUID for App node.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "UUID"))


class AttributeReference(
    Reference,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.AttributeReference",
):
    '''(experimental) Attribute type reference edge.

    :stability: experimental
    '''

    def __init__(self, props: "IAttributeReferenceProps") -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: IAttributeReferenceProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isAtt")
    @builtins.classmethod
    def is_att(cls, edge: "Edge") -> builtins.bool:
        '''(experimental) Indicates if edge in an **Fn::GetAtt** {@link Reference}.

        :param edge: -

        :stability: experimental
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isAtt", [edge]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ATT_VALUE")
    def ATT_VALUE(cls) -> builtins.str:
        '''(experimental) Attribute key for resolved value of attribute reference.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ATT_VALUE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PREFIX")
    def PREFIX(cls) -> builtins.str:
        '''(experimental) Edge prefix to denote **Fn::GetAtt** type reference edge.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PREFIX"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''(experimental) Get the resolved attribute value.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "value"))


@jsii.implements(_ISerializableEntity_0dbfd411)
class BaseEntity(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.BaseEntity",
):
    '''(experimental) Base class for all store entities (Node and Edges).

    :stability: experimental
    '''

    def __init__(self, props: "IBaseEntityProps") -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: IBaseEntityProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addAttribute")
    def add_attribute(self, key: builtins.str, value: typing.Any) -> None:
        '''(experimental) Add attribute.

        :param key: -
        :param value: -

        :stability: experimental
        :throws: Error if attribute for key already exists
        '''
        if __debug__:
            def stub(key: builtins.str, value: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "addAttribute", [key, value]))

    @jsii.member(jsii_name="addFlag")
    def add_flag(self, flag: _FlagEnum_af90e158) -> None:
        '''(experimental) Add flag.

        :param flag: -

        :stability: experimental
        '''
        if __debug__:
            def stub(flag: _FlagEnum_af90e158) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument flag", value=flag, expected_type=type_hints["flag"])
        return typing.cast(None, jsii.invoke(self, "addFlag", [flag]))

    @jsii.member(jsii_name="addMetadata")
    def add_metadata(self, metadata_type: builtins.str, data: typing.Any) -> None:
        '''(experimental) Add metadata entry.

        :param metadata_type: -
        :param data: -

        :stability: experimental
        '''
        if __debug__:
            def stub(metadata_type: builtins.str, data: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument metadata_type", value=metadata_type, expected_type=type_hints["metadata_type"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        return typing.cast(None, jsii.invoke(self, "addMetadata", [metadata_type, data]))

    @jsii.member(jsii_name="addTag")
    def add_tag(self, key: builtins.str, value: builtins.str) -> None:
        '''(experimental) Add tag.

        :param key: -
        :param value: -

        :stability: experimental
        :throws: Throws Error is tag for key already exists
        '''
        if __debug__:
            def stub(key: builtins.str, value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "addTag", [key, value]))

    @jsii.member(jsii_name="applyData")
    def apply_data(
        self,
        data: "IBaseEntityDataProps",
        overwrite: typing.Optional[builtins.bool] = None,
        apply_flags: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Applies data (attributes, metadata, tags, flag) to entity.

        Generally used only for mutations such as collapse and consume to retain data.

        :param data: - The data to apply.
        :param overwrite: -
        :param apply_flags: - Indicates if data is overwritten - Indicates if flags should be applied.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                data: IBaseEntityDataProps,
                overwrite: typing.Optional[builtins.bool] = None,
                apply_flags: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument overwrite", value=overwrite, expected_type=type_hints["overwrite"])
            check_type(argname="argument apply_flags", value=apply_flags, expected_type=type_hints["apply_flags"])
        return typing.cast(None, jsii.invoke(self, "applyData", [data, overwrite, apply_flags]))

    @jsii.member(jsii_name="findMetadata")
    def find_metadata(
        self,
        metadata_type: builtins.str,
    ) -> typing.List[constructs.MetadataEntry]:
        '''(experimental) Retrieves all metadata entries of a given type.

        :param metadata_type: -

        :stability: experimental
        :type: Readonly<SerializedGraph.Metadata>
        '''
        if __debug__:
            def stub(metadata_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument metadata_type", value=metadata_type, expected_type=type_hints["metadata_type"])
        return typing.cast(typing.List[constructs.MetadataEntry], jsii.invoke(self, "findMetadata", [metadata_type]))

    @jsii.member(jsii_name="getAttribute")
    def get_attribute(self, key: builtins.str) -> typing.Any:
        '''(experimental) Get attribute by key.

        :param key: -

        :stability: experimental
        '''
        if __debug__:
            def stub(key: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(typing.Any, jsii.invoke(self, "getAttribute", [key]))

    @jsii.member(jsii_name="getTag")
    def get_tag(self, key: builtins.str) -> typing.Optional[builtins.str]:
        '''(experimental) Get tag by key.

        :param key: -

        :stability: experimental
        '''
        if __debug__:
            def stub(key: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "getTag", [key]))

    @jsii.member(jsii_name="hasAttribute")
    def has_attribute(
        self,
        key: builtins.str,
        value: typing.Any = None,
    ) -> builtins.bool:
        '''(experimental) Indicates if entity has a given attribute defined, and optionally with a specific value.

        :param key: -
        :param value: -

        :stability: experimental
        '''
        if __debug__:
            def stub(key: builtins.str, value: typing.Any = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.bool, jsii.invoke(self, "hasAttribute", [key, value]))

    @jsii.member(jsii_name="hasFlag")
    def has_flag(self, flag: _FlagEnum_af90e158) -> builtins.bool:
        '''(experimental) Indicates if entity has a given flag.

        :param flag: -

        :stability: experimental
        '''
        if __debug__:
            def stub(flag: _FlagEnum_af90e158) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument flag", value=flag, expected_type=type_hints["flag"])
        return typing.cast(builtins.bool, jsii.invoke(self, "hasFlag", [flag]))

    @jsii.member(jsii_name="hasMetadata")
    def has_metadata(
        self,
        metadata_type: builtins.str,
        data: typing.Any,
    ) -> builtins.bool:
        '''(experimental) Indicates if entity has matching metadata entry.

        :param metadata_type: -
        :param data: -

        :stability: experimental
        '''
        if __debug__:
            def stub(metadata_type: builtins.str, data: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument metadata_type", value=metadata_type, expected_type=type_hints["metadata_type"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        return typing.cast(builtins.bool, jsii.invoke(self, "hasMetadata", [metadata_type, data]))

    @jsii.member(jsii_name="hasTag")
    def has_tag(
        self,
        key: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> builtins.bool:
        '''(experimental) Indicates if entity has tag, optionally verifying tag value.

        :param key: -
        :param value: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                key: builtins.str,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.bool, jsii.invoke(self, "hasTag", [key, value]))

    @jsii.member(jsii_name="mutateDestroy")
    @abc.abstractmethod
    def mutate_destroy(self, strict: typing.Optional[builtins.bool] = None) -> None:
        '''(experimental) Destroy the entity be removing all references and removing from store.

        :param strict: - If ``strict``, then entity must not have any references remaining when attempting to destroy.

        :stability: experimental
        :destructive: true
        '''
        ...

    @jsii.member(jsii_name="setAttribute")
    def set_attribute(self, key: builtins.str, value: typing.Any) -> None:
        '''(experimental) Set attribute.

        This will overwrite existing attribute.

        :param key: -
        :param value: -

        :stability: experimental
        '''
        if __debug__:
            def stub(key: builtins.str, value: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "setAttribute", [key, value]))

    @jsii.member(jsii_name="setTag")
    def set_tag(self, key: builtins.str, value: builtins.str) -> None:
        '''(experimental) Set tag.

        Will overwrite existing tag.

        :param key: -
        :param value: -

        :stability: experimental
        '''
        if __debug__:
            def stub(key: builtins.str, value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "setTag", [key, value]))

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> _Attributes_b47661e3:
        '''(experimental) Get *readonly* record of all attributes.

        :stability: experimental
        :type: Readonly<SerializedGraph.Attributes>
        '''
        return typing.cast(_Attributes_b47661e3, jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="flags")
    def flags(self) -> typing.List[_FlagEnum_af90e158]:
        '''(experimental) Get *readonly* list of all flags.

        :stability: experimental
        :type: ReadonlyArray
        '''
        return typing.cast(typing.List[_FlagEnum_af90e158], jsii.get(self, "flags"))

    @builtins.property
    @jsii.member(jsii_name="isDestroyed")
    def is_destroyed(self) -> builtins.bool:
        '''(experimental) Indicates if the entity has been destroyed (eg: removed from store).

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isDestroyed"))

    @builtins.property
    @jsii.member(jsii_name="isMutated")
    def is_mutated(self) -> builtins.bool:
        '''(experimental) Indicates if the entity has had destructive mutations applied.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isMutated"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.List[constructs.MetadataEntry]:
        '''(experimental) Get *readonly* list of all metadata entries.

        :stability: experimental
        :type: Readonly<SerializedGraph.Metadata>
        '''
        return typing.cast(typing.List[constructs.MetadataEntry], jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="store")
    def store(self) -> "Store":
        '''(experimental) Reference to the store.

        :stability: experimental
        '''
        return typing.cast("Store", jsii.get(self, "store"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _Tags_cf30c388:
        '''(experimental) Get *readonly* record of all tags.

        :stability: experimental
        :type: Readonly<SerializedGraph.Tags>
        '''
        return typing.cast(_Tags_cf30c388, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        '''(experimental) Universally unique identifier.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "uuid"))


class _BaseEntityProxy(BaseEntity):
    @jsii.member(jsii_name="mutateDestroy")
    def mutate_destroy(self, strict: typing.Optional[builtins.bool] = None) -> None:
        '''(experimental) Destroy the entity be removing all references and removing from store.

        :param strict: - If ``strict``, then entity must not have any references remaining when attempting to destroy.

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(strict: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
        return typing.cast(None, jsii.invoke(self, "mutateDestroy", [strict]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BaseEntity).__jsii_proxy_class__ = lambda : _BaseEntityProxy


class CfnResourceNode(
    Node,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.CfnResourceNode",
):
    '''(experimental) CfnResourceNode defines an L1 cdk resource.

    :stability: experimental
    '''

    def __init__(self, props: "ICfnResourceNodeProps") -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: ICfnResourceNodeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isCfnResourceNode")
    @builtins.classmethod
    def is_cfn_resource_node(cls, node: "Node") -> builtins.bool:
        '''(experimental) Indicates if a node is a {@link CfnResourceNode}.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnResourceNode", [node]))

    @jsii.member(jsii_name="findNearestResource")
    def find_nearest_resource(self) -> typing.Optional["ResourceNode"]:
        '''(experimental) Finds the near *ancestor* that is a {@link ResourceNode}.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["ResourceNode"], jsii.invoke(self, "findNearestResource", []))

    @jsii.member(jsii_name="isEquivalentFqn")
    def is_equivalent_fqn(self, resource: "ResourceNode") -> builtins.bool:
        '''(experimental) Evaluates if CfnResourceNode fqn is equivalent to ResourceNode fqn.

        :param resource: - {@link Graph.ResourceNode} to compare.

        :return: Returns ``true`` if equivalent, otherwise ``false``

        :stability: experimental

        Example::

            `aws-cdk-lib.aws_lambda.Function` => `aws-cdk-lib.aws_lambda.CfnFunction`
        '''
        if __debug__:
            def stub(resource: ResourceNode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isEquivalentFqn", [resource]))

    @jsii.member(jsii_name="mutateDestroy")
    def mutate_destroy(self, strict: typing.Optional[builtins.bool] = None) -> None:
        '''(experimental) Destroys this node by removing all references and removing this node from the store.

        :param strict: -

        :stability: experimental
        :inheritdoc: true
        '''
        if __debug__:
            def stub(strict: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
        return typing.cast(None, jsii.invoke(self, "mutateDestroy", [strict]))


class Dependency(
    Edge,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.Dependency",
):
    '''(experimental) Dependency edge class defines CloudFormation dependency between resources.

    :stability: experimental
    '''

    def __init__(self, props: "ITypedEdgeProps") -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: ITypedEdgeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isDependency")
    @builtins.classmethod
    def is_dependency(cls, edge: "Edge") -> builtins.bool:
        '''(experimental) Indicates if given edge is a {@link Dependency} edge.

        :param edge: -

        :stability: experimental
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isDependency", [edge]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PREFIX")
    def PREFIX(cls) -> builtins.str:
        '''(experimental) Edge prefix to denote dependency edge.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PREFIX"))


@jsii.implements(_ISerializableEdge_afcbbd54)
class Edge(
    BaseEntity,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.Edge",
):
    '''(experimental) Edge class defines a link (relationship) between nodes, as in standard `graph theory <https://en.wikipedia.org/wiki/Graph_theory>`_.

    :stability: experimental
    '''

    def __init__(self, props: "IEdgeProps") -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: IEdgeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="findAllInChain")
    @builtins.classmethod
    def find_all_in_chain(
        cls,
        chain: typing.Mapping[typing.Any, typing.Any],
        predicate: "IEdgePredicate",
    ) -> typing.List["Edge"]:
        '''(experimental) Find all matching edges based on predicate within an EdgeChain.

        :param chain: -
        :param predicate: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                chain: typing.Mapping[typing.Any, typing.Any],
                predicate: IEdgePredicate,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument chain", value=chain, expected_type=type_hints["chain"])
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
        return typing.cast(typing.List["Edge"], jsii.sinvoke(cls, "findAllInChain", [chain, predicate]))

    @jsii.member(jsii_name="findInChain")
    @builtins.classmethod
    def find_in_chain(
        cls,
        chain: typing.Mapping[typing.Any, typing.Any],
        predicate: "IEdgePredicate",
    ) -> typing.Optional["Edge"]:
        '''(experimental) Find first edge matching predicate within an EdgeChain.

        :param chain: -
        :param predicate: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                chain: typing.Mapping[typing.Any, typing.Any],
                predicate: IEdgePredicate,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument chain", value=chain, expected_type=type_hints["chain"])
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
        return typing.cast(typing.Optional["Edge"], jsii.sinvoke(cls, "findInChain", [chain, predicate]))

    @jsii.member(jsii_name="isEquivalent")
    def is_equivalent(self, edge: "Edge") -> builtins.bool:
        '''(experimental) Indicates if this edge is equivalent to another edge.

        Edges are considered equivalent if they share same type, source, and target.

        :param edge: -

        :stability: experimental
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isEquivalent", [edge]))

    @jsii.member(jsii_name="mutateConsume")
    def mutate_consume(self, edge: "Edge") -> None:
        '''(experimental) Merge an equivalent edge's data into this edge and destroy the other edge.

        Used during filtering operations to consolidate equivalent edges.

        :param edge: - The edge to consume.

        :stability: experimental
        :destructive: true
        :throws: Error is edge is not *equivalent*
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(None, jsii.invoke(self, "mutateConsume", [edge]))

    @jsii.member(jsii_name="mutateDestroy")
    def mutate_destroy(self, _strict: typing.Optional[builtins.bool] = None) -> None:
        '''(experimental) Destroy the edge.

        Remove all references and remove from store.

        :param _strict: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(_strict: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _strict", value=_strict, expected_type=type_hints["_strict"])
        return typing.cast(None, jsii.invoke(self, "mutateDestroy", [_strict]))

    @jsii.member(jsii_name="mutateDirection")
    def mutate_direction(self, direction: _EdgeDirectionEnum_26ef4ba3) -> None:
        '''(experimental) Change the edge **direction**.

        :param direction: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(direction: _EdgeDirectionEnum_26ef4ba3) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
        return typing.cast(None, jsii.invoke(self, "mutateDirection", [direction]))

    @jsii.member(jsii_name="mutateSource")
    def mutate_source(self, node: "Node") -> None:
        '''(experimental) Change the edge **source**.

        :param node: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "mutateSource", [node]))

    @jsii.member(jsii_name="mutateTarget")
    def mutate_target(self, node: "Node") -> None:
        '''(experimental) Change the edge **target**.

        :param node: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "mutateTarget", [node]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(experimental) Get string representation of this edge.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="allowDestructiveMutations")
    def allow_destructive_mutations(self) -> builtins.bool:
        '''(experimental) Indicates if edge allows destructive mutations.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "allowDestructiveMutations"))

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> _EdgeDirectionEnum_26ef4ba3:
        '''(experimental) Indicates the direction in which the edge is directed.

        :stability: experimental
        '''
        return typing.cast(_EdgeDirectionEnum_26ef4ba3, jsii.get(self, "direction"))

    @builtins.property
    @jsii.member(jsii_name="edgeType")
    def edge_type(self) -> _EdgeTypeEnum_1b13d7ee:
        '''(experimental) Type of edge.

        :stability: experimental
        '''
        return typing.cast(_EdgeTypeEnum_1b13d7ee, jsii.get(self, "edgeType"))

    @builtins.property
    @jsii.member(jsii_name="isClosed")
    def is_closed(self) -> builtins.bool:
        '''(experimental) Indicates if the Edge's **source** and **target** are the same, or were the same when it was created (prior to mutations).

        To check whether it was originally closed, use ``hasFlag(FlagEnum.CLOSED_EDGE)`` instead.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isClosed"))

    @builtins.property
    @jsii.member(jsii_name="isCrossStack")
    def is_cross_stack(self) -> builtins.bool:
        '''(experimental) Indicates if **source** and **target** nodes reside in different *root* stacks.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isCrossStack"))

    @builtins.property
    @jsii.member(jsii_name="isExtraneous")
    def is_extraneous(self) -> builtins.bool:
        '''(experimental) Indicates if edge is extraneous which is determined by explicitly having *EXTRANEOUS* flag added and/or being a closed loop (source===target).

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isExtraneous"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "Node":
        '''(experimental) Edge **source** is the node that defines the edge (tail).

        :stability: experimental
        '''
        return typing.cast("Node", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "Node":
        '''(experimental) Edge **target** is the node being referenced by the **source** (head).

        :stability: experimental
        '''
        return typing.cast("Node", jsii.get(self, "target"))


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IAppNodeProps")
class IAppNodeProps(IBaseEntityDataProps, typing_extensions.Protocol):
    '''(experimental) {@link AppNode} props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="store")
    def store(self) -> "Store":
        '''(experimental) Store.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="cfnType")
    def cfn_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) Type of CloudFormation resource.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="constructInfo")
    def construct_info(self) -> typing.Optional[_ConstructInfo_e912d4bb]:
        '''(experimental) Synthesized construct information defining jii resolution data.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="logicalId")
    def logical_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) Logical id of the node, which is only unique within containing stack.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> typing.Optional["Node"]:
        '''(experimental) Parent node.

        :stability: experimental
        '''
        ...


class _IAppNodePropsProxy(
    jsii.proxy_for(IBaseEntityDataProps), # type: ignore[misc]
):
    '''(experimental) {@link AppNode} props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IAppNodeProps"

    @builtins.property
    @jsii.member(jsii_name="store")
    def store(self) -> "Store":
        '''(experimental) Store.

        :stability: experimental
        '''
        return typing.cast("Store", jsii.get(self, "store"))

    @builtins.property
    @jsii.member(jsii_name="cfnType")
    def cfn_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) Type of CloudFormation resource.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cfnType"))

    @builtins.property
    @jsii.member(jsii_name="constructInfo")
    def construct_info(self) -> typing.Optional[_ConstructInfo_e912d4bb]:
        '''(experimental) Synthesized construct information defining jii resolution data.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_ConstructInfo_e912d4bb], jsii.get(self, "constructInfo"))

    @builtins.property
    @jsii.member(jsii_name="logicalId")
    def logical_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) Logical id of the node, which is only unique within containing stack.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logicalId"))

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> typing.Optional["Node"]:
        '''(experimental) Parent node.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["Node"], jsii.get(self, "parent"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppNodeProps).__jsii_proxy_class__ = lambda : _IAppNodePropsProxy


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IAttributeReferenceProps"
)
class IAttributeReferenceProps(ITypedEdgeProps, typing_extensions.Protocol):
    '''(experimental) Attribute type reference props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(
        self,
    ) -> typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]]:
        '''(experimental) Resolved attribute value.

        :stability: experimental
        '''
        ...

    @value.setter
    def value(
        self,
        value: typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]],
    ) -> None:
        ...


class _IAttributeReferencePropsProxy(
    jsii.proxy_for(ITypedEdgeProps), # type: ignore[misc]
):
    '''(experimental) Attribute type reference props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IAttributeReferenceProps"

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(
        self,
    ) -> typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]]:
        '''(experimental) Resolved attribute value.

        :stability: experimental
        '''
        return typing.cast(typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]], jsii.get(self, "value"))

    @value.setter
    def value(
        self,
        value: typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAttributeReferenceProps).__jsii_proxy_class__ = lambda : _IAttributeReferencePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IBaseEntityDataProps")
class IBaseEntityDataProps(typing_extensions.Protocol):
    '''(experimental) Base interface for all store entities **data** props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[_Attributes_b47661e3]:
        '''(experimental) Attributes.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="flags")
    def flags(self) -> typing.Optional[typing.List[_FlagEnum_af90e158]]:
        '''(experimental) Flags.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[typing.List[constructs.MetadataEntry]]:
        '''(experimental) Metadata entries.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[_Tags_cf30c388]:
        '''(experimental) Tags.

        :stability: experimental
        '''
        ...


class _IBaseEntityDataPropsProxy:
    '''(experimental) Base interface for all store entities **data** props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IBaseEntityDataProps"

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Optional[_Attributes_b47661e3]:
        '''(experimental) Attributes.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_Attributes_b47661e3], jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="flags")
    def flags(self) -> typing.Optional[typing.List[_FlagEnum_af90e158]]:
        '''(experimental) Flags.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[_FlagEnum_af90e158]], jsii.get(self, "flags"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[typing.List[constructs.MetadataEntry]]:
        '''(experimental) Metadata entries.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[constructs.MetadataEntry]], jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[_Tags_cf30c388]:
        '''(experimental) Tags.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_Tags_cf30c388], jsii.get(self, "tags"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBaseEntityDataProps).__jsii_proxy_class__ = lambda : _IBaseEntityDataPropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IBaseEntityProps")
class IBaseEntityProps(IBaseEntityDataProps, typing_extensions.Protocol):
    '''(experimental) Base interface for all store entities props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="store")
    def store(self) -> "Store":
        '''(experimental) Store.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        '''(experimental) UUID.

        :stability: experimental
        '''
        ...


class _IBaseEntityPropsProxy(
    jsii.proxy_for(IBaseEntityDataProps), # type: ignore[misc]
):
    '''(experimental) Base interface for all store entities props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IBaseEntityProps"

    @builtins.property
    @jsii.member(jsii_name="store")
    def store(self) -> "Store":
        '''(experimental) Store.

        :stability: experimental
        '''
        return typing.cast("Store", jsii.get(self, "store"))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        '''(experimental) UUID.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBaseEntityProps).__jsii_proxy_class__ = lambda : _IBaseEntityPropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.ICfnResourceNodeProps")
class ICfnResourceNodeProps(ITypedNodeProps, typing_extensions.Protocol):
    '''(experimental) CfnResourceNode props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> typing.Optional[_NodeTypeEnum_d56eed04]:
        '''
        :stability: experimental
        '''
        ...

    @node_type.setter
    def node_type(self, value: typing.Optional[_NodeTypeEnum_d56eed04]) -> None:
        ...


class _ICfnResourceNodePropsProxy(
    jsii.proxy_for(ITypedNodeProps), # type: ignore[misc]
):
    '''(experimental) CfnResourceNode props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.ICfnResourceNodeProps"

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> typing.Optional[_NodeTypeEnum_d56eed04]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[_NodeTypeEnum_d56eed04], jsii.get(self, "nodeType"))

    @node_type.setter
    def node_type(self, value: typing.Optional[_NodeTypeEnum_d56eed04]) -> None:
        if __debug__:
            def stub(value: typing.Optional[_NodeTypeEnum_d56eed04]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeType", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICfnResourceNodeProps).__jsii_proxy_class__ = lambda : _ICfnResourceNodePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IEdgePredicate")
class IEdgePredicate(typing_extensions.Protocol):
    '''(experimental) Predicate to match edge.

    :stability: experimental
    '''

    pass


class _IEdgePredicateProxy:
    '''(experimental) Predicate to match edge.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IEdgePredicate"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEdgePredicate).__jsii_proxy_class__ = lambda : _IEdgePredicateProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IEdgeProps")
class IEdgeProps(ITypedEdgeProps, typing_extensions.Protocol):
    '''(experimental) Edge props interface.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> _EdgeDirectionEnum_26ef4ba3:
        '''(experimental) Indicates the direction in which the edge is directed.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="edgeType")
    def edge_type(self) -> _EdgeTypeEnum_1b13d7ee:
        '''(experimental) Type of edge.

        :stability: experimental
        '''
        ...


class _IEdgePropsProxy(
    jsii.proxy_for(ITypedEdgeProps), # type: ignore[misc]
):
    '''(experimental) Edge props interface.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IEdgeProps"

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> _EdgeDirectionEnum_26ef4ba3:
        '''(experimental) Indicates the direction in which the edge is directed.

        :stability: experimental
        '''
        return typing.cast(_EdgeDirectionEnum_26ef4ba3, jsii.get(self, "direction"))

    @builtins.property
    @jsii.member(jsii_name="edgeType")
    def edge_type(self) -> _EdgeTypeEnum_1b13d7ee:
        '''(experimental) Type of edge.

        :stability: experimental
        '''
        return typing.cast(_EdgeTypeEnum_1b13d7ee, jsii.get(self, "edgeType"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEdgeProps).__jsii_proxy_class__ = lambda : _IEdgePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IFindEdgeOptions")
class IFindEdgeOptions(typing_extensions.Protocol):
    '''(experimental) Options for edge based search operations.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> typing.Optional[constructs.ConstructOrder]:
        '''(experimental) The order of traversal during search path.

        :stability: experimental
        '''
        ...

    @order.setter
    def order(self, value: typing.Optional[constructs.ConstructOrder]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="predicate")
    def predicate(self) -> typing.Optional[IEdgePredicate]:
        '''(experimental) The predicate to match edges(s).

        :stability: experimental
        '''
        ...

    @predicate.setter
    def predicate(self, value: typing.Optional[IEdgePredicate]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="reverse")
    def reverse(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates reverse order.

        :stability: experimental
        '''
        ...

    @reverse.setter
    def reverse(self, value: typing.Optional[builtins.bool]) -> None:
        ...


class _IFindEdgeOptionsProxy:
    '''(experimental) Options for edge based search operations.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IFindEdgeOptions"

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> typing.Optional[constructs.ConstructOrder]:
        '''(experimental) The order of traversal during search path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[constructs.ConstructOrder], jsii.get(self, "order"))

    @order.setter
    def order(self, value: typing.Optional[constructs.ConstructOrder]) -> None:
        if __debug__:
            def stub(value: typing.Optional[constructs.ConstructOrder]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="predicate")
    def predicate(self) -> typing.Optional[IEdgePredicate]:
        '''(experimental) The predicate to match edges(s).

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IEdgePredicate], jsii.get(self, "predicate"))

    @predicate.setter
    def predicate(self, value: typing.Optional[IEdgePredicate]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IEdgePredicate]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predicate", value)

    @builtins.property
    @jsii.member(jsii_name="reverse")
    def reverse(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates reverse order.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "reverse"))

    @reverse.setter
    def reverse(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reverse", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFindEdgeOptions).__jsii_proxy_class__ = lambda : _IFindEdgeOptionsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IFindNodeOptions")
class IFindNodeOptions(typing_extensions.Protocol):
    '''(experimental) Options for node based search operations.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> typing.Optional[constructs.ConstructOrder]:
        '''(experimental) The order of traversal during search path.

        :stability: experimental
        '''
        ...

    @order.setter
    def order(self, value: typing.Optional[constructs.ConstructOrder]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="predicate")
    def predicate(self) -> typing.Optional["INodePredicate"]:
        '''(experimental) The predicate to match node(s).

        :stability: experimental
        '''
        ...

    @predicate.setter
    def predicate(self, value: typing.Optional["INodePredicate"]) -> None:
        ...


class _IFindNodeOptionsProxy:
    '''(experimental) Options for node based search operations.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IFindNodeOptions"

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> typing.Optional[constructs.ConstructOrder]:
        '''(experimental) The order of traversal during search path.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[constructs.ConstructOrder], jsii.get(self, "order"))

    @order.setter
    def order(self, value: typing.Optional[constructs.ConstructOrder]) -> None:
        if __debug__:
            def stub(value: typing.Optional[constructs.ConstructOrder]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="predicate")
    def predicate(self) -> typing.Optional["INodePredicate"]:
        '''(experimental) The predicate to match node(s).

        :stability: experimental
        '''
        return typing.cast(typing.Optional["INodePredicate"], jsii.get(self, "predicate"))

    @predicate.setter
    def predicate(self, value: typing.Optional["INodePredicate"]) -> None:
        if __debug__:
            def stub(value: typing.Optional[INodePredicate]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predicate", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFindNodeOptions).__jsii_proxy_class__ = lambda : _IFindNodeOptionsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.INestedStackNodeProps")
class INestedStackNodeProps(IStackNodeProps, typing_extensions.Protocol):
    '''(experimental) {@link NestedStackNode} props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="parentStack")
    def parent_stack(self) -> "StackNode":
        '''(experimental) Parent stack.

        :stability: experimental
        '''
        ...


class _INestedStackNodePropsProxy(
    jsii.proxy_for(IStackNodeProps), # type: ignore[misc]
):
    '''(experimental) {@link NestedStackNode} props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.INestedStackNodeProps"

    @builtins.property
    @jsii.member(jsii_name="parentStack")
    def parent_stack(self) -> "StackNode":
        '''(experimental) Parent stack.

        :stability: experimental
        '''
        return typing.cast("StackNode", jsii.get(self, "parentStack"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INestedStackNodeProps).__jsii_proxy_class__ = lambda : _INestedStackNodePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.INodePredicate")
class INodePredicate(typing_extensions.Protocol):
    '''(experimental) Predicate to match node.

    :stability: experimental
    '''

    pass


class _INodePredicateProxy:
    '''(experimental) Predicate to match node.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.INodePredicate"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INodePredicate).__jsii_proxy_class__ = lambda : _INodePredicateProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.INodeProps")
class INodeProps(ITypedNodeProps, typing_extensions.Protocol):
    '''(experimental) Node props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> _NodeTypeEnum_d56eed04:
        '''(experimental) Type of node.

        :stability: experimental
        '''
        ...


class _INodePropsProxy(
    jsii.proxy_for(ITypedNodeProps), # type: ignore[misc]
):
    '''(experimental) Node props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.INodeProps"

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> _NodeTypeEnum_d56eed04:
        '''(experimental) Type of node.

        :stability: experimental
        '''
        return typing.cast(_NodeTypeEnum_d56eed04, jsii.get(self, "nodeType"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INodeProps).__jsii_proxy_class__ = lambda : _INodePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IOutputNodeProps")
class IOutputNodeProps(ITypedNodeProps, typing_extensions.Protocol):
    '''(experimental) OutputNode props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(experimental) Resolved output value.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="exportName")
    def export_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Export name.

        :stability: experimental
        '''
        ...


class _IOutputNodePropsProxy(
    jsii.proxy_for(ITypedNodeProps), # type: ignore[misc]
):
    '''(experimental) OutputNode props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IOutputNodeProps"

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(experimental) Resolved output value.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="exportName")
    def export_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Export name.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exportName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOutputNodeProps).__jsii_proxy_class__ = lambda : _IOutputNodePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IParameterNodeProps")
class IParameterNodeProps(ITypedNodeProps, typing_extensions.Protocol):
    '''(experimental) {@link ParameterNode} props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''(experimental) Parameter type.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(experimental) Resolved value.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description.

        :stability: experimental
        '''
        ...


class _IParameterNodePropsProxy(
    jsii.proxy_for(ITypedNodeProps), # type: ignore[misc]
):
    '''(experimental) {@link ParameterNode} props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IParameterNodeProps"

    @builtins.property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> builtins.str:
        '''(experimental) Parameter type.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterType"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(experimental) Resolved value.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameterNodeProps).__jsii_proxy_class__ = lambda : _IParameterNodePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IReferenceProps")
class IReferenceProps(ITypedEdgeProps, typing_extensions.Protocol):
    '''(experimental) Reference edge props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="referenceType")
    def reference_type(self) -> typing.Optional[_ReferenceTypeEnum_f84a272a]:
        '''(experimental) Type of reference.

        :stability: experimental
        '''
        ...

    @reference_type.setter
    def reference_type(
        self,
        value: typing.Optional[_ReferenceTypeEnum_f84a272a],
    ) -> None:
        ...


class _IReferencePropsProxy(
    jsii.proxy_for(ITypedEdgeProps), # type: ignore[misc]
):
    '''(experimental) Reference edge props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IReferenceProps"

    @builtins.property
    @jsii.member(jsii_name="referenceType")
    def reference_type(self) -> typing.Optional[_ReferenceTypeEnum_f84a272a]:
        '''(experimental) Type of reference.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_ReferenceTypeEnum_f84a272a], jsii.get(self, "referenceType"))

    @reference_type.setter
    def reference_type(
        self,
        value: typing.Optional[_ReferenceTypeEnum_f84a272a],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[_ReferenceTypeEnum_f84a272a]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "referenceType", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReferenceProps).__jsii_proxy_class__ = lambda : _IReferencePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IResourceNodeProps")
class IResourceNodeProps(ITypedNodeProps, typing_extensions.Protocol):
    '''(experimental) ResourceNode props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cdkOwned")
    def cdk_owned(self) -> builtins.bool:
        '''(experimental) Indicates if this resource is owned by cdk (defined in cdk library).

        :stability: experimental
        '''
        ...

    @cdk_owned.setter
    def cdk_owned(self, value: builtins.bool) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> typing.Optional[_NodeTypeEnum_d56eed04]:
        '''(experimental) Type of node.

        :stability: experimental
        '''
        ...

    @node_type.setter
    def node_type(self, value: typing.Optional[_NodeTypeEnum_d56eed04]) -> None:
        ...


class _IResourceNodePropsProxy(
    jsii.proxy_for(ITypedNodeProps), # type: ignore[misc]
):
    '''(experimental) ResourceNode props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IResourceNodeProps"

    @builtins.property
    @jsii.member(jsii_name="cdkOwned")
    def cdk_owned(self) -> builtins.bool:
        '''(experimental) Indicates if this resource is owned by cdk (defined in cdk library).

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "cdkOwned"))

    @cdk_owned.setter
    def cdk_owned(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdkOwned", value)

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> typing.Optional[_NodeTypeEnum_d56eed04]:
        '''(experimental) Type of node.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_NodeTypeEnum_d56eed04], jsii.get(self, "nodeType"))

    @node_type.setter
    def node_type(self, value: typing.Optional[_NodeTypeEnum_d56eed04]) -> None:
        if __debug__:
            def stub(value: typing.Optional[_NodeTypeEnum_d56eed04]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeType", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceNodeProps).__jsii_proxy_class__ = lambda : _IResourceNodePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IStackNodeProps")
class IStackNodeProps(ITypedNodeProps, typing_extensions.Protocol):
    '''(experimental) {@link StackNode} props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> typing.Optional[_NodeTypeEnum_d56eed04]:
        '''(experimental) Type of node.

        :stability: experimental
        '''
        ...

    @node_type.setter
    def node_type(self, value: typing.Optional[_NodeTypeEnum_d56eed04]) -> None:
        ...


class _IStackNodePropsProxy(
    jsii.proxy_for(ITypedNodeProps), # type: ignore[misc]
):
    '''(experimental) {@link StackNode} props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IStackNodeProps"

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> typing.Optional[_NodeTypeEnum_d56eed04]:
        '''(experimental) Type of node.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_NodeTypeEnum_d56eed04], jsii.get(self, "nodeType"))

    @node_type.setter
    def node_type(self, value: typing.Optional[_NodeTypeEnum_d56eed04]) -> None:
        if __debug__:
            def stub(value: typing.Optional[_NodeTypeEnum_d56eed04]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeType", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackNodeProps).__jsii_proxy_class__ = lambda : _IStackNodePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.IStoreCounts")
class IStoreCounts(typing_extensions.Protocol):
    '''(experimental) Interface for store counts.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cfnResources")
    def cfn_resources(self) -> _ICounterRecord_97e6658c:
        '''(experimental) Returns {@link ICounterRecord} containing total number of each *cfnResourceType*.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="edges")
    def edges(self) -> jsii.Number:
        '''(experimental) Counts total number of edges in the store.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="edgeTypes")
    def edge_types(self) -> _ICounterRecord_97e6658c:
        '''(experimental) Returns {@link ICounterRecord} containing total number of each *edge type* ({@link EdgeTypeEnum}).

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> jsii.Number:
        '''(experimental) Counts total number of nodes in the store.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="nodeTypes")
    def node_types(self) -> _ICounterRecord_97e6658c:
        '''(experimental) Returns {@link ICounterRecord} containing total number of each *node type* ({@link NodeTypeEnum}).

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> jsii.Number:
        '''(experimental) Counts total number of stacks in the store.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="stages")
    def stages(self) -> jsii.Number:
        '''(experimental) Counts total number of stages in the store.

        :stability: experimental
        '''
        ...


class _IStoreCountsProxy:
    '''(experimental) Interface for store counts.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.IStoreCounts"

    @builtins.property
    @jsii.member(jsii_name="cfnResources")
    def cfn_resources(self) -> _ICounterRecord_97e6658c:
        '''(experimental) Returns {@link ICounterRecord} containing total number of each *cfnResourceType*.

        :stability: experimental
        '''
        return typing.cast(_ICounterRecord_97e6658c, jsii.get(self, "cfnResources"))

    @builtins.property
    @jsii.member(jsii_name="edges")
    def edges(self) -> jsii.Number:
        '''(experimental) Counts total number of edges in the store.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "edges"))

    @builtins.property
    @jsii.member(jsii_name="edgeTypes")
    def edge_types(self) -> _ICounterRecord_97e6658c:
        '''(experimental) Returns {@link ICounterRecord} containing total number of each *edge type* ({@link EdgeTypeEnum}).

        :stability: experimental
        '''
        return typing.cast(_ICounterRecord_97e6658c, jsii.get(self, "edgeTypes"))

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> jsii.Number:
        '''(experimental) Counts total number of nodes in the store.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "nodes"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypes")
    def node_types(self) -> _ICounterRecord_97e6658c:
        '''(experimental) Returns {@link ICounterRecord} containing total number of each *node type* ({@link NodeTypeEnum}).

        :stability: experimental
        '''
        return typing.cast(_ICounterRecord_97e6658c, jsii.get(self, "nodeTypes"))

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> jsii.Number:
        '''(experimental) Counts total number of stacks in the store.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "stacks"))

    @builtins.property
    @jsii.member(jsii_name="stages")
    def stages(self) -> jsii.Number:
        '''(experimental) Counts total number of stages in the store.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "stages"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStoreCounts).__jsii_proxy_class__ = lambda : _IStoreCountsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.ITypedEdgeProps")
class ITypedEdgeProps(IBaseEntityProps, typing_extensions.Protocol):
    '''(experimental) Base edge props agnostic to edge type.

    Used for extending per edge class with type specifics.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "Node":
        '''(experimental) Edge **source** is the node that defines the edge (tail).

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "Node":
        '''(experimental) Edge **target** is the node being referenced by the **source** (head).

        :stability: experimental
        '''
        ...


class _ITypedEdgePropsProxy(
    jsii.proxy_for(IBaseEntityProps), # type: ignore[misc]
):
    '''(experimental) Base edge props agnostic to edge type.

    Used for extending per edge class with type specifics.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.ITypedEdgeProps"

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "Node":
        '''(experimental) Edge **source** is the node that defines the edge (tail).

        :stability: experimental
        '''
        return typing.cast("Node", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "Node":
        '''(experimental) Edge **target** is the node being referenced by the **source** (head).

        :stability: experimental
        '''
        return typing.cast("Node", jsii.get(self, "target"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITypedEdgeProps).__jsii_proxy_class__ = lambda : _ITypedEdgePropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.ITypedNodeProps")
class ITypedNodeProps(IBaseEntityProps, typing_extensions.Protocol):
    '''(experimental) Base node props agnostic to node type.

    Used for extending per node class with type specifics.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''(experimental) Node id, which is unique within parent scope.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''(experimental) Path of the node.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="cfnType")
    def cfn_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) Type of CloudFormation resource.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="constructInfo")
    def construct_info(self) -> typing.Optional[_ConstructInfo_e912d4bb]:
        '''(experimental) Synthesized construct information defining jii resolution data.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="logicalId")
    def logical_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) Logical id of the node, which is only unique within containing stack.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> typing.Optional["Node"]:
        '''(experimental) Parent node.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="stack")
    def stack(self) -> typing.Optional["StackNode"]:
        '''(experimental) Stack the node is contained.

        :stability: experimental
        '''
        ...


class _ITypedNodePropsProxy(
    jsii.proxy_for(IBaseEntityProps), # type: ignore[misc]
):
    '''(experimental) Base node props agnostic to node type.

    Used for extending per node class with type specifics.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.Graph.ITypedNodeProps"

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''(experimental) Node id, which is unique within parent scope.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''(experimental) Path of the node.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="cfnType")
    def cfn_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) Type of CloudFormation resource.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cfnType"))

    @builtins.property
    @jsii.member(jsii_name="constructInfo")
    def construct_info(self) -> typing.Optional[_ConstructInfo_e912d4bb]:
        '''(experimental) Synthesized construct information defining jii resolution data.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_ConstructInfo_e912d4bb], jsii.get(self, "constructInfo"))

    @builtins.property
    @jsii.member(jsii_name="logicalId")
    def logical_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) Logical id of the node, which is only unique within containing stack.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logicalId"))

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> typing.Optional["Node"]:
        '''(experimental) Parent node.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["Node"], jsii.get(self, "parent"))

    @builtins.property
    @jsii.member(jsii_name="stack")
    def stack(self) -> typing.Optional["StackNode"]:
        '''(experimental) Stack the node is contained.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["StackNode"], jsii.get(self, "stack"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITypedNodeProps).__jsii_proxy_class__ = lambda : _ITypedNodePropsProxy


class ImportReference(
    Reference,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.ImportReference",
):
    '''(experimental) Import reference defines **Fn::ImportValue** type reference edge.

    :stability: experimental
    '''

    def __init__(self, props: ITypedEdgeProps) -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: ITypedEdgeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isImport")
    @builtins.classmethod
    def is_import(cls, edge: Edge) -> builtins.bool:
        '''(experimental) Indicates if edge is **Fn::ImportValue** based {@link Reference}.

        :param edge: -

        :stability: experimental
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isImport", [edge]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PREFIX")
    def PREFIX(cls) -> builtins.str:
        '''(experimental) Edge prefix to denote **Fn::ImportValue** type reference edge.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PREFIX"))


class NestedStackNode(
    StackNode,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.NestedStackNode",
):
    '''(experimental) NestedStackNode defines a cdk NestedStack.

    :stability: experimental
    '''

    def __init__(self, props: INestedStackNodeProps) -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: INestedStackNodeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isNestedStackNode")
    @builtins.classmethod
    def is_nested_stack_node(cls, node: "Node") -> builtins.bool:
        '''(experimental) Indicates if node is a {@link NestedStackNode}.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isNestedStackNode", [node]))

    @jsii.member(jsii_name="mutateHoist")
    def mutate_hoist(self, new_parent: "Node") -> None:
        '''(experimental) Hoist *this node* to an *ancestor* by removing it from its current parent node and in turn moving it to the ancestor.

        :param new_parent: -

        :stability: experimental
        :inheritdoc: true
        '''
        if __debug__:
            def stub(new_parent: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument new_parent", value=new_parent, expected_type=type_hints["new_parent"])
        return typing.cast(None, jsii.invoke(self, "mutateHoist", [new_parent]))

    @builtins.property
    @jsii.member(jsii_name="parentStack")
    def parent_stack(self) -> typing.Optional["StackNode"]:
        '''(experimental) Get parent stack of this nested stack.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["StackNode"], jsii.get(self, "parentStack"))


@jsii.implements(_ISerializableNode_9eb400fa)
class Node(
    BaseEntity,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.Node",
):
    '''(experimental) Node class is the base definition of **node** entities in the graph, as in standard `graph theory <https://en.wikipedia.org/wiki/Graph_theory>`_.

    :stability: experimental
    '''

    def __init__(self, props: INodeProps) -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: INodeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addChild")
    def add_child(self, node: "Node") -> None:
        '''(experimental) Add *child* node.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "addChild", [node]))

    @jsii.member(jsii_name="addLink")
    def add_link(self, edge: Edge) -> None:
        '''(experimental) Add *link* to another node.

        :param edge: -

        :stability: experimental
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(None, jsii.invoke(self, "addLink", [edge]))

    @jsii.member(jsii_name="addReverseLink")
    def add_reverse_link(self, edge: Edge) -> None:
        '''(experimental) Add *link* from another node.

        :param edge: -

        :stability: experimental
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(None, jsii.invoke(self, "addReverseLink", [edge]))

    @jsii.member(jsii_name="doesDependOn")
    def does_depend_on(self, node: "Node") -> builtins.bool:
        '''(experimental) Indicates if *this node* depends on *another node*.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.invoke(self, "doesDependOn", [node]))

    @jsii.member(jsii_name="doesReference")
    def does_reference(self, node: "Node") -> builtins.bool:
        '''(experimental) Indicates if *this node* references *another node*.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.invoke(self, "doesReference", [node]))

    @jsii.member(jsii_name="find")
    def find(self, predicate: INodePredicate) -> typing.Optional["Node"]:
        '''(experimental) Recursively find the nearest sub-node matching predicate.

        :param predicate: -

        :stability: experimental
        '''
        if __debug__:
            def stub(predicate: INodePredicate) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
        return typing.cast(typing.Optional["Node"], jsii.invoke(self, "find", [predicate]))

    @jsii.member(jsii_name="findAll")
    def find_all(
        self,
        options: typing.Optional[IFindNodeOptions] = None,
    ) -> typing.List["Node"]:
        '''(experimental) Return this construct and all of its sub-nodes in the given order.

        Optionally filter nodes based on predicate.

        :param options: -

        :stability: experimental
        '''
        if __debug__:
            def stub(options: typing.Optional[IFindNodeOptions] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        return typing.cast(typing.List["Node"], jsii.invoke(self, "findAll", [options]))

    @jsii.member(jsii_name="findAllLinks")
    def find_all_links(
        self,
        options: typing.Optional[IFindEdgeOptions] = None,
    ) -> typing.List[Edge]:
        '''(experimental) Return all direct links of this node and that of all sub-nodes.

        Optionally filter links based on predicate.

        :param options: -

        :stability: experimental
        '''
        if __debug__:
            def stub(options: typing.Optional[IFindEdgeOptions] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        return typing.cast(typing.List[Edge], jsii.invoke(self, "findAllLinks", [options]))

    @jsii.member(jsii_name="findAncestor")
    def find_ancestor(
        self,
        predicate: INodePredicate,
        max: typing.Optional[jsii.Number] = None,
    ) -> typing.Optional["Node"]:
        '''(experimental) Find nearest *ancestor* of *this node* matching given predicate.

        :param predicate: - Predicate to match ancestor.
        :param max: -

        :stability: experimental
        :max: {number} [max] - Optional maximum levels to ascend
        '''
        if __debug__:
            def stub(
                predicate: INodePredicate,
                max: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
        return typing.cast(typing.Optional["Node"], jsii.invoke(self, "findAncestor", [predicate, max]))

    @jsii.member(jsii_name="findChild")
    def find_child(self, id: builtins.str) -> typing.Optional["Node"]:
        '''(experimental) Find child with given *id*.

        Similar to ``find`` but does not throw error if no child found.

        :param id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(typing.Optional["Node"], jsii.invoke(self, "findChild", [id]))

    @jsii.member(jsii_name="findLink")
    def find_link(
        self,
        predicate: IEdgePredicate,
        reverse: typing.Optional[builtins.bool] = None,
        follow: typing.Optional[builtins.bool] = None,
        direct: typing.Optional[builtins.bool] = None,
    ) -> typing.Optional[Edge]:
        '''(experimental) Find link of this node based on predicate.

        By default this will follow link
        chains to evaluate the predicate against and return the matching direct link
        of this node.

        :param predicate: Edge predicate function to match edge.
        :param reverse: Indicates if links are search in reverse order.
        :param follow: Indicates if link chain is followed.
        :param direct: Indicates that only *direct* links should be searched.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                predicate: IEdgePredicate,
                reverse: typing.Optional[builtins.bool] = None,
                follow: typing.Optional[builtins.bool] = None,
                direct: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
            check_type(argname="argument reverse", value=reverse, expected_type=type_hints["reverse"])
            check_type(argname="argument follow", value=follow, expected_type=type_hints["follow"])
            check_type(argname="argument direct", value=direct, expected_type=type_hints["direct"])
        return typing.cast(typing.Optional[Edge], jsii.invoke(self, "findLink", [predicate, reverse, follow, direct]))

    @jsii.member(jsii_name="findLinks")
    def find_links(
        self,
        predicate: IEdgePredicate,
        reverse: typing.Optional[builtins.bool] = None,
        follow: typing.Optional[builtins.bool] = None,
        direct: typing.Optional[builtins.bool] = None,
    ) -> typing.List[Edge]:
        '''(experimental) Find all links of this node based on predicate.

        By default this will follow link
        chains to evaluate the predicate against and return the matching direct links
        of this node.

        :param predicate: Edge predicate function to match edge.
        :param reverse: Indicates if links are search in reverse order.
        :param follow: Indicates if link chain is followed.
        :param direct: Indicates that only *direct* links should be searched.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                predicate: IEdgePredicate,
                reverse: typing.Optional[builtins.bool] = None,
                follow: typing.Optional[builtins.bool] = None,
                direct: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
            check_type(argname="argument reverse", value=reverse, expected_type=type_hints["reverse"])
            check_type(argname="argument follow", value=follow, expected_type=type_hints["follow"])
            check_type(argname="argument direct", value=direct, expected_type=type_hints["direct"])
        return typing.cast(typing.List[Edge], jsii.invoke(self, "findLinks", [predicate, reverse, follow, direct]))

    @jsii.member(jsii_name="getCfnProp")
    def get_cfn_prop(
        self,
        key: builtins.str,
    ) -> typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]]]:
        '''(experimental) Get specific CloudFormation property.

        :param key: -

        :stability: experimental
        '''
        if __debug__:
            def stub(key: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]]], jsii.invoke(self, "getCfnProp", [key]))

    @jsii.member(jsii_name="getChild")
    def get_child(self, id: builtins.str) -> "Node":
        '''(experimental) Get *child* node with given *id*.

        :param id: -

        :stability: experimental
        :throws: Error if no child with given id
        '''
        if __debug__:
            def stub(id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast("Node", jsii.invoke(self, "getChild", [id]))

    @jsii.member(jsii_name="getLinkChains")
    def get_link_chains(
        self,
        reverse: typing.Optional[builtins.bool] = None,
    ) -> typing.List[typing.Mapping[typing.Any, typing.Any]]:
        '''(experimental) Resolve all link chains.

        :param reverse: -

        :see: {@link EdgeChain}
        :stability: experimental
        '''
        if __debug__:
            def stub(reverse: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument reverse", value=reverse, expected_type=type_hints["reverse"])
        return typing.cast(typing.List[typing.Mapping[typing.Any, typing.Any]], jsii.invoke(self, "getLinkChains", [reverse]))

    @jsii.member(jsii_name="getNearestAncestor")
    def get_nearest_ancestor(self, node: "Node") -> "Node":
        '''(experimental) Gets the nearest **common** *ancestor* shared between *this node* and another *node*.

        :param node: -

        :stability: experimental
        :throws: Error if *node* does not share a **common** *ancestor*
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast("Node", jsii.invoke(self, "getNearestAncestor", [node]))

    @jsii.member(jsii_name="isAncestor")
    def is_ancestor(self, ancestor: "Node") -> builtins.bool:
        '''(experimental) Indicates if a specific *node* is an *ancestor* of *this node*.

        :param ancestor: -

        :stability: experimental
        '''
        if __debug__:
            def stub(ancestor: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument ancestor", value=ancestor, expected_type=type_hints["ancestor"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isAncestor", [ancestor]))

    @jsii.member(jsii_name="isChild")
    def is_child(self, node: "Node") -> builtins.bool:
        '''(experimental) Indicates if specific *node* is a *child* of *this node*.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isChild", [node]))

    @jsii.member(jsii_name="mutateCollapse")
    def mutate_collapse(self) -> None:
        '''(experimental) Collapses all sub-nodes of *this node* into *this node*.

        :stability: experimental
        :destructive: true
        '''
        return typing.cast(None, jsii.invoke(self, "mutateCollapse", []))

    @jsii.member(jsii_name="mutateCollapseTo")
    def mutate_collapse_to(self, ancestor: "Node") -> "Node":
        '''(experimental) Collapses *this node* into *an ancestor*.

        :param ancestor: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(ancestor: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument ancestor", value=ancestor, expected_type=type_hints["ancestor"])
        return typing.cast("Node", jsii.invoke(self, "mutateCollapseTo", [ancestor]))

    @jsii.member(jsii_name="mutateCollapseToParent")
    def mutate_collapse_to_parent(self) -> "Node":
        '''(experimental) Collapses *this node* into *it's parent node*.

        :stability: experimental
        :destructive: true
        '''
        return typing.cast("Node", jsii.invoke(self, "mutateCollapseToParent", []))

    @jsii.member(jsii_name="mutateDestroy")
    def mutate_destroy(self, strict: typing.Optional[builtins.bool] = None) -> None:
        '''(experimental) Destroys this node by removing all references and removing this node from the store.

        :param strict: - Indicates that this node must not have references.

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(strict: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
        return typing.cast(None, jsii.invoke(self, "mutateDestroy", [strict]))

    @jsii.member(jsii_name="mutateHoist")
    def mutate_hoist(self, new_parent: "Node") -> None:
        '''(experimental) Hoist *this node* to an *ancestor* by removing it from its current parent node and in turn moving it to the ancestor.

        :param new_parent: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(new_parent: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument new_parent", value=new_parent, expected_type=type_hints["new_parent"])
        return typing.cast(None, jsii.invoke(self, "mutateHoist", [new_parent]))

    @jsii.member(jsii_name="mutateRemoveChild")
    def mutate_remove_child(self, node: "Node") -> builtins.bool:
        '''(experimental) Remove a *child* node from *this node*.

        :param node: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.invoke(self, "mutateRemoveChild", [node]))

    @jsii.member(jsii_name="mutateRemoveLink")
    def mutate_remove_link(self, link: Edge) -> builtins.bool:
        '''(experimental) Remove a *link* from *this node*.

        :param link: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(link: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument link", value=link, expected_type=type_hints["link"])
        return typing.cast(builtins.bool, jsii.invoke(self, "mutateRemoveLink", [link]))

    @jsii.member(jsii_name="mutateRemoveReverseLink")
    def mutate_remove_reverse_link(self, link: Edge) -> builtins.bool:
        '''(experimental) Remove a *link* to *this node*.

        :param link: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(link: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument link", value=link, expected_type=type_hints["link"])
        return typing.cast(builtins.bool, jsii.invoke(self, "mutateRemoveReverseLink", [link]))

    @jsii.member(jsii_name="mutateUncluster")
    def mutate_uncluster(self) -> None:
        '''(experimental) Hoist all children to parent and collapse node to parent.

        :stability: experimental
        :destructive: true
        '''
        return typing.cast(None, jsii.invoke(self, "mutateUncluster", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''(experimental) Get string representation of this node.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="allowDestructiveMutations")
    def allow_destructive_mutations(self) -> builtins.bool:
        '''(experimental) Indicates if this node allows destructive mutations.

        :see: {@link Store.allowDestructiveMutations}
        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "allowDestructiveMutations"))

    @builtins.property
    @jsii.member(jsii_name="children")
    def children(self) -> typing.List["Node"]:
        '''(experimental) Get all direct child nodes.

        :stability: experimental
        '''
        return typing.cast(typing.List["Node"], jsii.get(self, "children"))

    @builtins.property
    @jsii.member(jsii_name="dependedOnBy")
    def depended_on_by(self) -> typing.List["Node"]:
        '''(experimental) Get list of **Nodes** that *depend on this node*.

        :see: {@link Node.reverseDependencyLinks}
        :stability: experimental
        '''
        return typing.cast(typing.List["Node"], jsii.get(self, "dependedOnBy"))

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.List["Node"]:
        '''(experimental) Get list of **Nodes** that *this node depends on*.

        :see: {@link Node.dependencyLinks}
        :stability: experimental
        '''
        return typing.cast(typing.List["Node"], jsii.get(self, "dependencies"))

    @builtins.property
    @jsii.member(jsii_name="dependencyLinks")
    def dependency_links(self) -> typing.List[Dependency]:
        '''(experimental) Gets list of {@link Dependency} links (edges) where this node is the **source**.

        :stability: experimental
        '''
        return typing.cast(typing.List[Dependency], jsii.get(self, "dependencyLinks"))

    @builtins.property
    @jsii.member(jsii_name="depth")
    def depth(self) -> jsii.Number:
        '''(experimental) Indicates the depth of the node relative to root (0).

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "depth"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''(experimental) Node id, which is only unique within parent scope.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="isAsset")
    def is_asset(self) -> builtins.bool:
        '''(experimental) Indicates if this node is considered a {@link FlagEnum.ASSET}.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isAsset"))

    @builtins.property
    @jsii.member(jsii_name="isCluster")
    def is_cluster(self) -> builtins.bool:
        '''(experimental) Indicates if this node is considered a {@link FlagEnum.CLUSTER}.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isCluster"))

    @builtins.property
    @jsii.member(jsii_name="isCustomResource")
    def is_custom_resource(self) -> builtins.bool:
        '''(experimental) Indicates if node is a *Custom Resource*.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isCustomResource"))

    @builtins.property
    @jsii.member(jsii_name="isExtraneous")
    def is_extraneous(self) -> builtins.bool:
        '''(experimental) Indicates if this node is considered a {@link FlagEnum.EXTRANEOUS} node or determined to be extraneous: - Clusters that contain no children.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isExtraneous"))

    @builtins.property
    @jsii.member(jsii_name="isGraphContainer")
    def is_graph_container(self) -> builtins.bool:
        '''(experimental) Indicates if this node is considered a {@link FlagEnum.GRAPH_CONTAINER}.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isGraphContainer"))

    @builtins.property
    @jsii.member(jsii_name="isLeaf")
    def is_leaf(self) -> builtins.bool:
        '''(experimental) Indicates if this node is a *leaf* node, which means it does not have children.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isLeaf"))

    @builtins.property
    @jsii.member(jsii_name="isResourceWrapper")
    def is_resource_wrapper(self) -> builtins.bool:
        '''(experimental) Indicates if this node is considered a {@link FlagEnum.RESOURCE_WRAPPER}.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isResourceWrapper"))

    @builtins.property
    @jsii.member(jsii_name="isTopLevel")
    def is_top_level(self) -> builtins.bool:
        '''(experimental) Indicates if node is direct child of the graph root node.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isTopLevel"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> typing.List[Edge]:
        '''(experimental) Gets all links (edges) in which this node is the **source**.

        :stability: experimental
        '''
        return typing.cast(typing.List[Edge], jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> _NodeTypeEnum_d56eed04:
        '''(experimental) Type of node.

        :stability: experimental
        '''
        return typing.cast(_NodeTypeEnum_d56eed04, jsii.get(self, "nodeType"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''(experimental) Path of the node.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="referencedBy")
    def referenced_by(self) -> typing.List["Node"]:
        '''(experimental) Get list of **Nodes** that *reference this node*.

        :see: {@link Node.reverseReferenceLinks}
        :stability: experimental
        '''
        return typing.cast(typing.List["Node"], jsii.get(self, "referencedBy"))

    @builtins.property
    @jsii.member(jsii_name="referenceLinks")
    def reference_links(self) -> typing.List["Reference"]:
        '''(experimental) Gets list of {@link Reference} links (edges) where this node is the **source**.

        :stability: experimental
        '''
        return typing.cast(typing.List["Reference"], jsii.get(self, "referenceLinks"))

    @builtins.property
    @jsii.member(jsii_name="references")
    def references(self) -> typing.List["Node"]:
        '''(experimental) Get list of **Nodes** that *this node references*.

        :see: {@link Node.referenceLinks}
        :stability: experimental
        '''
        return typing.cast(typing.List["Node"], jsii.get(self, "references"))

    @builtins.property
    @jsii.member(jsii_name="reverseDependencyLinks")
    def reverse_dependency_links(self) -> typing.List[Dependency]:
        '''(experimental) Gets list of {@link Dependency} links (edges) where this node is the **target**.

        :stability: experimental
        '''
        return typing.cast(typing.List[Dependency], jsii.get(self, "reverseDependencyLinks"))

    @builtins.property
    @jsii.member(jsii_name="reverseLinks")
    def reverse_links(self) -> typing.List[Edge]:
        '''(experimental) Gets all links (edges) in which this node is the **target**.

        :stability: experimental
        '''
        return typing.cast(typing.List[Edge], jsii.get(self, "reverseLinks"))

    @builtins.property
    @jsii.member(jsii_name="reverseReferenceLinks")
    def reverse_reference_links(self) -> typing.List["Reference"]:
        '''(experimental) Gets list of {@link Reference} links (edges) where this node is the **target**.

        :stability: experimental
        '''
        return typing.cast(typing.List["Reference"], jsii.get(self, "reverseReferenceLinks"))

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List["Node"]:
        '''(experimental) Gets descending ordered list of ancestors from the root.

        :stability: experimental
        '''
        return typing.cast(typing.List["Node"], jsii.get(self, "scopes"))

    @builtins.property
    @jsii.member(jsii_name="siblings")
    def siblings(self) -> typing.List["Node"]:
        '''(experimental) Get list of *siblings* of this node.

        :stability: experimental
        '''
        return typing.cast(typing.List["Node"], jsii.get(self, "siblings"))

    @builtins.property
    @jsii.member(jsii_name="cfnProps")
    def cfn_props(self) -> typing.Optional[_PlainObject_c976ebcc]:
        '''(experimental) Gets CloudFormation properties for this node.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_PlainObject_c976ebcc], jsii.get(self, "cfnProps"))

    @builtins.property
    @jsii.member(jsii_name="cfnType")
    def cfn_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) Get the CloudFormation resource type for this node.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cfnType"))

    @builtins.property
    @jsii.member(jsii_name="constructInfo")
    def construct_info(self) -> typing.Optional[_ConstructInfo_e912d4bb]:
        '''(experimental) Synthesized construct information defining jii resolution data.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_ConstructInfo_e912d4bb], jsii.get(self, "constructInfo"))

    @builtins.property
    @jsii.member(jsii_name="constructInfoFqn")
    def construct_info_fqn(self) -> typing.Optional[builtins.str]:
        '''(experimental) Synthesized construct information defining jii resolution data.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "constructInfoFqn"))

    @builtins.property
    @jsii.member(jsii_name="logicalId")
    def logical_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) Logical id of the node, which is only unique within containing stack.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logicalId"))

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> typing.Optional["Node"]:
        '''(experimental) Parent node.

        Only the root node should not have parent.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["Node"], jsii.get(self, "parent"))

    @builtins.property
    @jsii.member(jsii_name="rootStack")
    def root_stack(self) -> typing.Optional["StackNode"]:
        '''(experimental) Get **root** stack.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["StackNode"], jsii.get(self, "rootStack"))

    @builtins.property
    @jsii.member(jsii_name="stack")
    def stack(self) -> typing.Optional["StackNode"]:
        '''(experimental) Stack the node is contained in.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["StackNode"], jsii.get(self, "stack"))


class OutputNode(
    Node,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.OutputNode",
):
    '''(experimental) OutputNode defines a cdk CfnOutput resources.

    :stability: experimental
    '''

    def __init__(self, props: IOutputNodeProps) -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: IOutputNodeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isOutputNode")
    @builtins.classmethod
    def is_output_node(cls, node: Node) -> builtins.bool:
        '''(experimental) Indicates if node is an {@link OutputNode}.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isOutputNode", [node]))

    @jsii.member(jsii_name="mutateDestroy")
    def mutate_destroy(self, strict: typing.Optional[builtins.bool] = None) -> None:
        '''(experimental) Destroys this node by removing all references and removing this node from the store.

        :param strict: -

        :stability: experimental
        :inheritdoc: true
        '''
        if __debug__:
            def stub(strict: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
        return typing.cast(None, jsii.invoke(self, "mutateDestroy", [strict]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ATTR_EXPORT_NAME")
    def ATTR_EXPORT_NAME(cls) -> builtins.str:
        '''(experimental) Attribute key where output export name is stored.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ATTR_EXPORT_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ATTR_VALUE")
    def ATTR_VALUE(cls) -> builtins.str:
        '''(experimental) Attribute key where output value is stored.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ATTR_VALUE"))

    @builtins.property
    @jsii.member(jsii_name="isExport")
    def is_export(self) -> builtins.bool:
        '''(experimental) Indicates if {@link OutputNode} is **exported**.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isExport"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(experimental) Get the *value** attribute.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="exportName")
    def export_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Get the export name attribute.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exportName"))


class ParameterNode(
    Node,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.ParameterNode",
):
    '''(experimental) ParameterNode defines a CfnParameter node.

    :stability: experimental
    '''

    def __init__(self, props: IParameterNodeProps) -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: IParameterNodeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isParameterNode")
    @builtins.classmethod
    def is_parameter_node(cls, node: Node) -> builtins.bool:
        '''(experimental) Indicates if node is a {@link ParameterNode}.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isParameterNode", [node]))

    @jsii.member(jsii_name="mutateDestroy")
    def mutate_destroy(self, strict: typing.Optional[builtins.bool] = None) -> None:
        '''(experimental) Destroys this node by removing all references and removing this node from the store.

        :param strict: -

        :stability: experimental
        :inheritdoc: true
        '''
        if __debug__:
            def stub(strict: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
        return typing.cast(None, jsii.invoke(self, "mutateDestroy", [strict]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ATTR_TYPE")
    def ATTR_TYPE(cls) -> builtins.str:
        '''(experimental) Attribute key where parameter type is stored.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ATTR_TYPE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ATTR_VALUE")
    def ATTR_VALUE(cls) -> builtins.str:
        '''(experimental) Attribute key where parameter value is store.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ATTR_VALUE"))

    @builtins.property
    @jsii.member(jsii_name="isStackReference")
    def is_stack_reference(self) -> builtins.bool:
        '''(experimental) Indicates if parameter is a reference to a stack.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isStackReference"))

    @builtins.property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> typing.Any:
        '''(experimental) Get the parameter type attribute.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "parameterType"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''(experimental) Get the value attribute.

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))


class Reference(
    Edge,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.Reference",
):
    '''(experimental) Reference edge class defines a directed relationship between nodes.

    :stability: experimental
    '''

    def __init__(self, props: IReferenceProps) -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: IReferenceProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isRef")
    @builtins.classmethod
    def is_ref(cls, edge: Edge) -> builtins.bool:
        '''(experimental) Indicates if edge is a **Ref** based {@link Reference} edge.

        :param edge: -

        :stability: experimental
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isRef", [edge]))

    @jsii.member(jsii_name="isReference")
    @builtins.classmethod
    def is_reference(cls, edge: Edge) -> builtins.bool:
        '''(experimental) Indicates if edge is a {@link Reference}.

        :param edge: -

        :stability: experimental
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isReference", [edge]))

    @jsii.member(jsii_name="resolveChain")
    def resolve_chain(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''(experimental) Resolve reference chain.

        :stability: experimental
        '''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "resolveChain", []))

    @jsii.member(jsii_name="resolveTargets")
    def resolve_targets(self) -> typing.List[Node]:
        '''(experimental) Resolve targets by following potential edge chain.

        :see: {@link EdgeChain}
        :stability: experimental
        '''
        return typing.cast(typing.List[Node], jsii.invoke(self, "resolveTargets", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ATT_TYPE")
    def ATT_TYPE(cls) -> builtins.str:
        '''(experimental) Attribute defining the type of reference.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ATT_TYPE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PREFIX")
    def PREFIX(cls) -> builtins.str:
        '''(experimental) Edge prefix to denote **Ref** type reference edge.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PREFIX"))

    @builtins.property
    @jsii.member(jsii_name="referenceType")
    def reference_type(self) -> _ReferenceTypeEnum_f84a272a:
        '''(experimental) Get type of reference.

        :stability: experimental
        '''
        return typing.cast(_ReferenceTypeEnum_f84a272a, jsii.get(self, "referenceType"))


class ResourceNode(
    Node,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.ResourceNode",
):
    '''(experimental) ResourceNode class defines a L2 cdk resource construct.

    :stability: experimental
    '''

    def __init__(self, props: IResourceNodeProps) -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: IResourceNodeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isResourceNode")
    @builtins.classmethod
    def is_resource_node(cls, node: Node) -> builtins.bool:
        '''(experimental) Indicates if node is a {@link ResourceNode}.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isResourceNode", [node]))

    @jsii.member(jsii_name="mutateCfnResource")
    def mutate_cfn_resource(
        self,
        cfn_resource: typing.Optional[CfnResourceNode] = None,
    ) -> None:
        '''(experimental) Modifies the L1 resource wrapped by this L2 resource.

        :param cfn_resource: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(cfn_resource: typing.Optional[CfnResourceNode] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cfn_resource", value=cfn_resource, expected_type=type_hints["cfn_resource"])
        return typing.cast(None, jsii.invoke(self, "mutateCfnResource", [cfn_resource]))

    @jsii.member(jsii_name="mutateRemoveChild")
    def mutate_remove_child(self, node: Node) -> builtins.bool:
        '''(experimental) Remove a *child* node from *this node*.

        :param node: -

        :stability: experimental
        :inheritdoc: true
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.invoke(self, "mutateRemoveChild", [node]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ATT_WRAPPED_CFN_PROPS")
    def ATT_WRAPPED_CFN_PROPS(cls) -> builtins.str:
        '''(experimental) Attribute key for cfn properties.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ATT_WRAPPED_CFN_PROPS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ATT_WRAPPED_CFN_TYPE")
    def ATT_WRAPPED_CFN_TYPE(cls) -> builtins.str:
        '''(experimental) Attribute key for cfn resource type.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ATT_WRAPPED_CFN_TYPE"))

    @builtins.property
    @jsii.member(jsii_name="isCdkOwned")
    def is_cdk_owned(self) -> builtins.bool:
        '''(experimental) Indicates if this resource is owned by cdk (defined in cdk library).

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isCdkOwned"))

    @builtins.property
    @jsii.member(jsii_name="cfnProps")
    def cfn_props(self) -> typing.Optional[_PlainObject_c976ebcc]:
        '''(experimental) Get the cfn properties from the L1 resource that this L2 resource wraps.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_PlainObject_c976ebcc], jsii.get(self, "cfnProps"))

    @builtins.property
    @jsii.member(jsii_name="cfnResource")
    def cfn_resource(self) -> typing.Optional[CfnResourceNode]:
        '''(experimental) Get the L1 cdk resource that this L2 resource wraps.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[CfnResourceNode], jsii.get(self, "cfnResource"))

    @builtins.property
    @jsii.member(jsii_name="cfnType")
    def cfn_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) Get the CloudFormation resource type for this L2 resource or for the L1 resource is wraps.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cfnType"))


class RootNode(
    Node,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.RootNode",
):
    '''(experimental) RootNode represents the root of the store tree.

    :stability: experimental
    '''

    def __init__(self, store: "Store") -> None:
        '''
        :param store: -

        :stability: experimental
        '''
        if __debug__:
            def stub(store: Store) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument store", value=store, expected_type=type_hints["store"])
        jsii.create(self.__class__, self, [store])

    @jsii.member(jsii_name="isRootNode")
    @builtins.classmethod
    def is_root_node(cls, node: Node) -> builtins.bool:
        '''(experimental) Indicates if node is a {@link RootNode}.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isRootNode", [node]))

    @jsii.member(jsii_name="findAll")
    def find_all(
        self,
        options: typing.Optional[IFindNodeOptions] = None,
    ) -> typing.List[Node]:
        '''(experimental) Return this construct and all of its sub-nodes in the given order.

        Optionally filter nodes based on predicate.

        :param options: -

        :stability: experimental
        :inheritdoc: **The root not is excluded from list**
        '''
        if __debug__:
            def stub(options: typing.Optional[IFindNodeOptions] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        return typing.cast(typing.List[Node], jsii.invoke(self, "findAll", [options]))

    @jsii.member(jsii_name="mutateCollapse")
    def mutate_collapse(self) -> None:
        '''(experimental) > {@link RootNode} does not support this mutation.

        :stability: experimental
        :inheritdoc: true
        :throws: Error does not support
        '''
        return typing.cast(None, jsii.invoke(self, "mutateCollapse", []))

    @jsii.member(jsii_name="mutateCollapseTo")
    def mutate_collapse_to(self, _ancestor: Node) -> Node:
        '''(experimental) > {@link RootNode} does not support this mutation.

        :param _ancestor: -

        :stability: experimental
        :inheritdoc: true
        :throws: Error does not support
        '''
        if __debug__:
            def stub(_ancestor: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _ancestor", value=_ancestor, expected_type=type_hints["_ancestor"])
        return typing.cast(Node, jsii.invoke(self, "mutateCollapseTo", [_ancestor]))

    @jsii.member(jsii_name="mutateCollapseToParent")
    def mutate_collapse_to_parent(self) -> Node:
        '''(experimental) > {@link RootNode} does not support this mutation.

        :stability: experimental
        :inheritdoc: true
        :throws: Error does not support
        '''
        return typing.cast(Node, jsii.invoke(self, "mutateCollapseToParent", []))

    @jsii.member(jsii_name="mutateDestroy")
    def mutate_destroy(self, _strict: typing.Optional[builtins.bool] = None) -> None:
        '''(experimental) > {@link RootNode} does not support this mutation.

        :param _strict: -

        :stability: experimental
        :inheritdoc: true
        :throws: Error does not support
        '''
        if __debug__:
            def stub(_strict: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _strict", value=_strict, expected_type=type_hints["_strict"])
        return typing.cast(None, jsii.invoke(self, "mutateDestroy", [_strict]))

    @jsii.member(jsii_name="mutateHoist")
    def mutate_hoist(self, _new_parent: Node) -> None:
        '''(experimental) > {@link RootNode} does not support this mutation.

        :param _new_parent: -

        :stability: experimental
        :inheritdoc: true
        :throws: Error does not support
        '''
        if __debug__:
            def stub(_new_parent: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _new_parent", value=_new_parent, expected_type=type_hints["_new_parent"])
        return typing.cast(None, jsii.invoke(self, "mutateHoist", [_new_parent]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PATH")
    def PATH(cls) -> builtins.str:
        '''(experimental) Fixed path of root.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PATH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="UUID")
    def UUID(cls) -> builtins.str:
        '''(experimental) Fixed UUID of root.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "UUID"))


class StackNode(
    Node,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.StackNode",
):
    '''(experimental) StackNode defines a cdk Stack.

    :stability: experimental
    '''

    def __init__(self, props: IStackNodeProps) -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: IStackNodeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isStackNode")
    @builtins.classmethod
    def is_stack_node(cls, node: Node) -> builtins.bool:
        '''(experimental) Indicates if node is a {@link StackNode}.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isStackNode", [node]))

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, node: Node) -> "StackNode":
        '''(experimental) Gets the {@link StackNode} containing a given resource.

        :param node: -

        :stability: experimental
        :throws: Error is node is not contained in a stack
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast("StackNode", jsii.sinvoke(cls, "of", [node]))

    @jsii.member(jsii_name="addOutput")
    def add_output(self, node: OutputNode) -> None:
        '''(experimental) Associate {@link OutputNode} with this stack.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: OutputNode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "addOutput", [node]))

    @jsii.member(jsii_name="addParameter")
    def add_parameter(self, node: ParameterNode) -> None:
        '''(experimental) Associate {@link ParameterNode} with this stack.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: ParameterNode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "addParameter", [node]))

    @jsii.member(jsii_name="findOutput")
    def find_output(self, logical_id: builtins.str) -> OutputNode:
        '''(experimental) Find {@link OutputNode} with *logicalId* defined by this stack.

        :param logical_id: -

        :stability: experimental
        :throws: Error is no output found matching *logicalId*
        '''
        if __debug__:
            def stub(logical_id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
        return typing.cast(OutputNode, jsii.invoke(self, "findOutput", [logical_id]))

    @jsii.member(jsii_name="findParameter")
    def find_parameter(self, parameter_id: builtins.str) -> ParameterNode:
        '''(experimental) Find {@link ParameterNode} with *parameterId* defined by this stack.

        :param parameter_id: -

        :stability: experimental
        :throws: Error is no parameter found matching *parameterId*
        '''
        if __debug__:
            def stub(parameter_id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parameter_id", value=parameter_id, expected_type=type_hints["parameter_id"])
        return typing.cast(ParameterNode, jsii.invoke(self, "findParameter", [parameter_id]))

    @jsii.member(jsii_name="mutateDestroy")
    def mutate_destroy(self, strict: typing.Optional[builtins.bool] = None) -> None:
        '''(experimental) Destroys this node by removing all references and removing this node from the store.

        :param strict: -

        :stability: experimental
        :inheritdoc: true
        '''
        if __debug__:
            def stub(strict: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
        return typing.cast(None, jsii.invoke(self, "mutateDestroy", [strict]))

    @jsii.member(jsii_name="mutateHoist")
    def mutate_hoist(self, new_parent: Node) -> None:
        '''(experimental) Hoist *this node* to an *ancestor* by removing it from its current parent node and in turn moving it to the ancestor.

        :param new_parent: -

        :stability: experimental
        :inheritdoc: true
        '''
        if __debug__:
            def stub(new_parent: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument new_parent", value=new_parent, expected_type=type_hints["new_parent"])
        return typing.cast(None, jsii.invoke(self, "mutateHoist", [new_parent]))

    @jsii.member(jsii_name="mutateRemoveOutput")
    def mutate_remove_output(self, node: OutputNode) -> builtins.bool:
        '''(experimental) Disassociate {@link OutputNode} from this stack.

        :param node: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(node: OutputNode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.invoke(self, "mutateRemoveOutput", [node]))

    @jsii.member(jsii_name="mutateRemoveParameter")
    def mutate_remove_parameter(self, node: ParameterNode) -> builtins.bool:
        '''(experimental) Disassociate {@link ParameterNode} from this stack.

        :param node: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(node: ParameterNode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.invoke(self, "mutateRemoveParameter", [node]))

    @builtins.property
    @jsii.member(jsii_name="exports")
    def exports(self) -> typing.List[OutputNode]:
        '''(experimental) Get all **exported** {@link OutputNode}s defined by this stack.

        :stability: experimental
        '''
        return typing.cast(typing.List[OutputNode], jsii.get(self, "exports"))

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(self) -> typing.List[OutputNode]:
        '''(experimental) Get all {@link OutputNode}s defined by this stack.

        :stability: experimental
        '''
        return typing.cast(typing.List[OutputNode], jsii.get(self, "outputs"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.List[ParameterNode]:
        '''(experimental) Get all {@link ParameterNode}s defined by this stack.

        :stability: experimental
        '''
        return typing.cast(typing.List[ParameterNode], jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> typing.Optional["StageNode"]:
        '''(experimental) Get {@link StageNode} containing this stack.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["StageNode"], jsii.get(self, "stage"))


class StageNode(
    Node,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.StageNode",
):
    '''(experimental) StageNode defines a cdk Stage.

    :stability: experimental
    '''

    def __init__(self, props: ITypedNodeProps) -> None:
        '''
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(props: ITypedNodeProps) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="isStageNode")
    @builtins.classmethod
    def is_stage_node(cls, node: Node) -> builtins.bool:
        '''(experimental) Indicates if node is a {@link StageNode}.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isStageNode", [node]))

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, node: Node) -> "StageNode":
        '''(experimental) Gets the {@link StageNode} containing a given resource.

        :param node: -

        :stability: experimental
        :throws: Error is node is not contained in a stage
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast("StageNode", jsii.sinvoke(cls, "of", [node]))

    @jsii.member(jsii_name="addStack")
    def add_stack(self, stack: StackNode) -> None:
        '''(experimental) Associate a {@link StackNode} with this stage.

        :param stack: -

        :stability: experimental
        '''
        if __debug__:
            def stub(stack: StackNode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
        return typing.cast(None, jsii.invoke(self, "addStack", [stack]))

    @jsii.member(jsii_name="mutateRemoveStack")
    def mutate_remove_stack(self, stack: StackNode) -> builtins.bool:
        '''(experimental) Disassociate {@link StackNode} from this stage.

        :param stack: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(stack: StackNode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
        return typing.cast(builtins.bool, jsii.invoke(self, "mutateRemoveStack", [stack]))

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[StackNode]:
        '''(experimental) Gets all stacks contained by this stage.

        :stability: experimental
        '''
        return typing.cast(typing.List[StackNode], jsii.get(self, "stacks"))


@jsii.implements(_ISerializableGraphStore_4640156f)
class Store(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.Graph.Store",
):
    '''(experimental) Store class provides the in-memory database-like interface for managing all entities in the graph.

    :stability: experimental
    '''

    def __init__(
        self,
        allow_destructive_mutations: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param allow_destructive_mutations: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                allow_destructive_mutations: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allow_destructive_mutations", value=allow_destructive_mutations, expected_type=type_hints["allow_destructive_mutations"])
        jsii.create(self.__class__, self, [allow_destructive_mutations])

    @jsii.member(jsii_name="fromSerializedStore")
    @builtins.classmethod
    def from_serialized_store(
        cls,
        *,
        edges: typing.Sequence[typing.Union[_Edge_211392d6, typing.Dict[str, typing.Any]]],
        tree: typing.Union[_Node_bc073df3, typing.Dict[str, typing.Any]],
        version: builtins.str,
    ) -> "Store":
        '''(experimental) Builds store from serialized store data.

        :param edges: (experimental) List of edges.
        :param tree: (experimental) Node tree.
        :param version: (experimental) Store version.

        :stability: experimental
        '''
        serialized_store = _GraphStore_ffbd5720(
            edges=edges, tree=tree, version=version
        )

        return typing.cast("Store", jsii.sinvoke(cls, "fromSerializedStore", [serialized_store]))

    @jsii.member(jsii_name="addEdge")
    def add_edge(self, edge: Edge) -> None:
        '''(experimental) Add **edge** to the store.

        :param edge: -

        :stability: experimental
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(None, jsii.invoke(self, "addEdge", [edge]))

    @jsii.member(jsii_name="addNode")
    def add_node(self, node: Node) -> None:
        '''(experimental) Add **node** to the store.

        :param node: -

        :stability: experimental
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "addNode", [node]))

    @jsii.member(jsii_name="addStack")
    def add_stack(self, stack: StackNode) -> None:
        '''(experimental) Add **stack** node to the store.

        :param stack: -

        :stability: experimental
        '''
        if __debug__:
            def stub(stack: StackNode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
        return typing.cast(None, jsii.invoke(self, "addStack", [stack]))

    @jsii.member(jsii_name="addStage")
    def add_stage(self, stage: StageNode) -> None:
        '''(experimental) Add **stage** to the store.

        :param stage: -

        :stability: experimental
        '''
        if __debug__:
            def stub(stage: StageNode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        return typing.cast(None, jsii.invoke(self, "addStage", [stage]))

    @jsii.member(jsii_name="clone")
    def clone(
        self,
        allow_destructive_mutations: typing.Optional[builtins.bool] = None,
    ) -> "Store":
        '''(experimental) Clone the store to allow destructive mutations.

        :param allow_destructive_mutations: Indicates if destructive mutations are allowed; defaults to ``true``

        :return: Returns a clone of the store that allows destructive mutations

        :stability: experimental
        '''
        if __debug__:
            def stub(
                allow_destructive_mutations: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allow_destructive_mutations", value=allow_destructive_mutations, expected_type=type_hints["allow_destructive_mutations"])
        return typing.cast("Store", jsii.invoke(self, "clone", [allow_destructive_mutations]))

    @jsii.member(jsii_name="computeLogicalUniversalId")
    def compute_logical_universal_id(
        self,
        stack: StackNode,
        logical_id: builtins.str,
    ) -> builtins.str:
        '''(experimental) Compute **universal** *logicalId* based on parent stack and construct *logicalId* (``<stack>:<logicalId>``).

        Construct *logicalIds are only unique within their containing stack, so to use *logicalId*
        lookups universally (like resolving references) we need a universal key.

        :param stack: -
        :param logical_id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(stack: StackNode, logical_id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
        return typing.cast(builtins.str, jsii.invoke(self, "computeLogicalUniversalId", [stack, logical_id]))

    @jsii.member(jsii_name="findNodeByLogicalId")
    def find_node_by_logical_id(
        self,
        stack: StackNode,
        logical_id: builtins.str,
    ) -> Node:
        '''(experimental) Find node within given **stack** with given *logicalId*.

        :param stack: -
        :param logical_id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(stack: StackNode, logical_id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
        return typing.cast(Node, jsii.invoke(self, "findNodeByLogicalId", [stack, logical_id]))

    @jsii.member(jsii_name="findNodeByLogicalUniversalId")
    def find_node_by_logical_universal_id(self, uid: builtins.str) -> Node:
        '''(experimental) Find node by **universal** *logicalId* (``<stack>:<logicalId>``).

        :param uid: -

        :stability: experimental
        '''
        if __debug__:
            def stub(uid: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
        return typing.cast(Node, jsii.invoke(self, "findNodeByLogicalUniversalId", [uid]))

    @jsii.member(jsii_name="getEdge")
    def get_edge(self, uuid: builtins.str) -> Edge:
        '''(experimental) Get stored **edge** by UUID.

        :param uuid: -

        :stability: experimental
        '''
        if __debug__:
            def stub(uuid: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uuid", value=uuid, expected_type=type_hints["uuid"])
        return typing.cast(Edge, jsii.invoke(self, "getEdge", [uuid]))

    @jsii.member(jsii_name="getNode")
    def get_node(self, uuid: builtins.str) -> Node:
        '''(experimental) Get stored **node** by UUID.

        :param uuid: -

        :stability: experimental
        '''
        if __debug__:
            def stub(uuid: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uuid", value=uuid, expected_type=type_hints["uuid"])
        return typing.cast(Node, jsii.invoke(self, "getNode", [uuid]))

    @jsii.member(jsii_name="getStack")
    def get_stack(self, uuid: builtins.str) -> StackNode:
        '''(experimental) Get stored **stack** node by UUID.

        :param uuid: -

        :stability: experimental
        '''
        if __debug__:
            def stub(uuid: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uuid", value=uuid, expected_type=type_hints["uuid"])
        return typing.cast(StackNode, jsii.invoke(self, "getStack", [uuid]))

    @jsii.member(jsii_name="getStage")
    def get_stage(self, uuid: builtins.str) -> StageNode:
        '''(experimental) Get stored **stage** node by UUID.

        :param uuid: -

        :stability: experimental
        '''
        if __debug__:
            def stub(uuid: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uuid", value=uuid, expected_type=type_hints["uuid"])
        return typing.cast(StageNode, jsii.invoke(self, "getStage", [uuid]))

    @jsii.member(jsii_name="mutateRemoveEdge")
    def mutate_remove_edge(self, edge: Edge) -> builtins.bool:
        '''(experimental) Remove **edge** from the store.

        :param edge: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(edge: Edge) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument edge", value=edge, expected_type=type_hints["edge"])
        return typing.cast(builtins.bool, jsii.invoke(self, "mutateRemoveEdge", [edge]))

    @jsii.member(jsii_name="mutateRemoveNode")
    def mutate_remove_node(self, node: Node) -> builtins.bool:
        '''(experimental) Remove **node** from the store.

        :param node: -

        :stability: experimental
        :destructive: true
        '''
        if __debug__:
            def stub(node: Node) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(builtins.bool, jsii.invoke(self, "mutateRemoveNode", [node]))

    @jsii.member(jsii_name="recordLogicalId")
    def record_logical_id(
        self,
        stack: StackNode,
        logical_id: builtins.str,
        resource: Node,
    ) -> None:
        '''(experimental) Record a **universal** *logicalId* to node mapping in the store.

        :param stack: -
        :param logical_id: -
        :param resource: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                stack: StackNode,
                logical_id: builtins.str,
                resource: Node,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(None, jsii.invoke(self, "recordLogicalId", [stack, logical_id, resource]))

    @jsii.member(jsii_name="serialize")
    def serialize(self) -> _GraphStore_ffbd5720:
        '''(experimental) Serialize the store.

        :stability: experimental
        '''
        return typing.cast(_GraphStore_ffbd5720, jsii.invoke(self, "serialize", []))

    @jsii.member(jsii_name="verifyDestructiveMutationAllowed")
    def verify_destructive_mutation_allowed(self) -> None:
        '''(experimental) Verifies that the store allows destructive mutations.

        :stability: experimental
        :throws: Error is store does **not** allow mutations
        '''
        return typing.cast(None, jsii.invoke(self, "verifyDestructiveMutationAllowed", []))

    @builtins.property
    @jsii.member(jsii_name="allowDestructiveMutations")
    def allow_destructive_mutations(self) -> builtins.bool:
        '''(experimental) Indicates if the store allows destructive mutations.

        Destructive mutations are only allowed on clones of the store to prevent plugins and filters from
        mutating the store for downstream plugins.

        All ``mutate*`` methods are only allowed on stores that allow destructive mutations.

        This behavior may change in the future if the need arises for plugins to pass mutated stores
        to downstream plugins. But it will be done cautiously with ensuring the intent of
        downstream plugin is to receive the mutated store.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "allowDestructiveMutations"))

    @builtins.property
    @jsii.member(jsii_name="counts")
    def counts(self) -> IStoreCounts:
        '''(experimental) Get record of all store counters.

        :stability: experimental
        '''
        return typing.cast(IStoreCounts, jsii.get(self, "counts"))

    @builtins.property
    @jsii.member(jsii_name="edges")
    def edges(self) -> typing.List[Edge]:
        '''(experimental) Gets all stored **edges**.

        :stability: experimental
        :type: ReadonlyArray
        '''
        return typing.cast(typing.List[Edge], jsii.get(self, "edges"))

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> typing.List[Node]:
        '''(experimental) Gets all stored **nodes**.

        :stability: experimental
        :type: ReadonlyArray
        '''
        return typing.cast(typing.List[Node], jsii.get(self, "nodes"))

    @builtins.property
    @jsii.member(jsii_name="root")
    def root(self) -> RootNode:
        '''(experimental) Root node in the store.

        The **root** node is not the computed root, but the graph root
        which is auto-generated and can not be mutated.

        :stability: experimental
        '''
        return typing.cast(RootNode, jsii.get(self, "root"))

    @builtins.property
    @jsii.member(jsii_name="rootStacks")
    def root_stacks(self) -> typing.List[StackNode]:
        '''(experimental) Gets all stored **root stack** nodes.

        :stability: experimental
        :type: ReadonlyArray
        '''
        return typing.cast(typing.List[StackNode], jsii.get(self, "rootStacks"))

    @builtins.property
    @jsii.member(jsii_name="stacks")
    def stacks(self) -> typing.List[StackNode]:
        '''(experimental) Gets all stored **stack** nodes.

        :stability: experimental
        :type: ReadonlyArray
        '''
        return typing.cast(typing.List[StackNode], jsii.get(self, "stacks"))

    @builtins.property
    @jsii.member(jsii_name="stages")
    def stages(self) -> typing.List[StageNode]:
        '''(experimental) Gets all stored **stage** nodes.

        :stability: experimental
        :type: ReadonlyArray
        '''
        return typing.cast(typing.List[StageNode], jsii.get(self, "stages"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''(experimental) Current SemVer version of the store.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))


__all__ = [
    "AppNode",
    "AttributeReference",
    "BaseEntity",
    "CfnResourceNode",
    "Dependency",
    "Edge",
    "IAppNodeProps",
    "IAttributeReferenceProps",
    "IBaseEntityDataProps",
    "IBaseEntityProps",
    "ICfnResourceNodeProps",
    "IEdgePredicate",
    "IEdgeProps",
    "IFindEdgeOptions",
    "IFindNodeOptions",
    "INestedStackNodeProps",
    "INodePredicate",
    "INodeProps",
    "IOutputNodeProps",
    "IParameterNodeProps",
    "IReferenceProps",
    "IResourceNodeProps",
    "IStackNodeProps",
    "IStoreCounts",
    "ITypedEdgeProps",
    "ITypedNodeProps",
    "ImportReference",
    "NestedStackNode",
    "Node",
    "OutputNode",
    "ParameterNode",
    "Reference",
    "ResourceNode",
    "RootNode",
    "StackNode",
    "StageNode",
    "Store",
]

publication.publish()
