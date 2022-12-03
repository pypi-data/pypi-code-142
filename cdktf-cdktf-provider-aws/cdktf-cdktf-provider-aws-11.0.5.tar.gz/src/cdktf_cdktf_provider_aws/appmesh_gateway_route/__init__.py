'''
# `aws_appmesh_gateway_route`

Refer to the Terraform Registory for docs: [`aws_appmesh_gateway_route`](https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route).
'''
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

import cdktf
import constructs


class AppmeshGatewayRoute(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRoute",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route aws_appmesh_gateway_route}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        mesh_name: builtins.str,
        name: builtins.str,
        spec: typing.Union["AppmeshGatewayRouteSpec", typing.Dict[str, typing.Any]],
        virtual_gateway_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route aws_appmesh_gateway_route} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_name AppmeshGatewayRoute#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#name AppmeshGatewayRoute#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#spec AppmeshGatewayRoute#spec}
        :param virtual_gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_gateway_name AppmeshGatewayRoute#virtual_gateway_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#id AppmeshGatewayRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_owner AppmeshGatewayRoute#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags AppmeshGatewayRoute#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags_all AppmeshGatewayRoute#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id_: builtins.str,
                *,
                mesh_name: builtins.str,
                name: builtins.str,
                spec: typing.Union[AppmeshGatewayRouteSpec, typing.Dict[str, typing.Any]],
                virtual_gateway_name: builtins.str,
                id: typing.Optional[builtins.str] = None,
                mesh_owner: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppmeshGatewayRouteConfig(
            mesh_name=mesh_name,
            name=name,
            spec=spec,
            virtual_gateway_name=virtual_gateway_name,
            id=id,
            mesh_owner=mesh_owner,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        grpc_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecGrpcRoute", typing.Dict[str, typing.Any]]] = None,
        http2_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2Route", typing.Dict[str, typing.Any]]] = None,
        http_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRoute", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc_route: grpc_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#grpc_route AppmeshGatewayRoute#grpc_route}
        :param http2_route: http2_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http2_route AppmeshGatewayRoute#http2_route}
        :param http_route: http_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http_route AppmeshGatewayRoute#http_route}
        '''
        value = AppmeshGatewayRouteSpec(
            grpc_route=grpc_route, http2_route=http2_route, http_route=http_route
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMeshOwner")
    def reset_mesh_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMeshOwner", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="resourceOwner")
    def resource_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceOwner"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "AppmeshGatewayRouteSpecOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="meshNameInput")
    def mesh_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshNameInput"))

    @builtins.property
    @jsii.member(jsii_name="meshOwnerInput")
    def mesh_owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["AppmeshGatewayRouteSpec"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualGatewayNameInput")
    def virtual_gateway_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualGatewayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshName", value)

    @builtins.property
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshOwner", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="virtualGatewayName")
    def virtual_gateway_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualGatewayName"))

    @virtual_gateway_name.setter
    def virtual_gateway_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualGatewayName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "mesh_name": "meshName",
        "name": "name",
        "spec": "spec",
        "virtual_gateway_name": "virtualGatewayName",
        "id": "id",
        "mesh_owner": "meshOwner",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class AppmeshGatewayRouteConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        mesh_name: builtins.str,
        name: builtins.str,
        spec: typing.Union["AppmeshGatewayRouteSpec", typing.Dict[str, typing.Any]],
        virtual_gateway_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_name AppmeshGatewayRoute#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#name AppmeshGatewayRoute#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#spec AppmeshGatewayRoute#spec}
        :param virtual_gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_gateway_name AppmeshGatewayRoute#virtual_gateway_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#id AppmeshGatewayRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_owner AppmeshGatewayRoute#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags AppmeshGatewayRoute#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags_all AppmeshGatewayRoute#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(spec, dict):
            spec = AppmeshGatewayRouteSpec(**spec)
        if __debug__:
            def stub(
                *,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
                mesh_name: builtins.str,
                name: builtins.str,
                spec: typing.Union[AppmeshGatewayRouteSpec, typing.Dict[str, typing.Any]],
                virtual_gateway_name: builtins.str,
                id: typing.Optional[builtins.str] = None,
                mesh_owner: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument mesh_name", value=mesh_name, expected_type=type_hints["mesh_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument virtual_gateway_name", value=virtual_gateway_name, expected_type=type_hints["virtual_gateway_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mesh_owner", value=mesh_owner, expected_type=type_hints["mesh_owner"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "mesh_name": mesh_name,
            "name": name,
            "spec": spec,
            "virtual_gateway_name": virtual_gateway_name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if mesh_owner is not None:
            self._values["mesh_owner"] = mesh_owner
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def mesh_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_name AppmeshGatewayRoute#mesh_name}.'''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#name AppmeshGatewayRoute#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(self) -> "AppmeshGatewayRouteSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#spec AppmeshGatewayRoute#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("AppmeshGatewayRouteSpec", result)

    @builtins.property
    def virtual_gateway_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_gateway_name AppmeshGatewayRoute#virtual_gateway_name}.'''
        result = self._values.get("virtual_gateway_name")
        assert result is not None, "Required property 'virtual_gateway_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#id AppmeshGatewayRoute#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_owner AppmeshGatewayRoute#mesh_owner}.'''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags AppmeshGatewayRoute#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags_all AppmeshGatewayRoute#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpec",
    jsii_struct_bases=[],
    name_mapping={
        "grpc_route": "grpcRoute",
        "http2_route": "http2Route",
        "http_route": "httpRoute",
    },
)
class AppmeshGatewayRouteSpec:
    def __init__(
        self,
        *,
        grpc_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecGrpcRoute", typing.Dict[str, typing.Any]]] = None,
        http2_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2Route", typing.Dict[str, typing.Any]]] = None,
        http_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRoute", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc_route: grpc_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#grpc_route AppmeshGatewayRoute#grpc_route}
        :param http2_route: http2_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http2_route AppmeshGatewayRoute#http2_route}
        :param http_route: http_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http_route AppmeshGatewayRoute#http_route}
        '''
        if isinstance(grpc_route, dict):
            grpc_route = AppmeshGatewayRouteSpecGrpcRoute(**grpc_route)
        if isinstance(http2_route, dict):
            http2_route = AppmeshGatewayRouteSpecHttp2Route(**http2_route)
        if isinstance(http_route, dict):
            http_route = AppmeshGatewayRouteSpecHttpRoute(**http_route)
        if __debug__:
            def stub(
                *,
                grpc_route: typing.Optional[typing.Union[AppmeshGatewayRouteSpecGrpcRoute, typing.Dict[str, typing.Any]]] = None,
                http2_route: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2Route, typing.Dict[str, typing.Any]]] = None,
                http_route: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRoute, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grpc_route", value=grpc_route, expected_type=type_hints["grpc_route"])
            check_type(argname="argument http2_route", value=http2_route, expected_type=type_hints["http2_route"])
            check_type(argname="argument http_route", value=http_route, expected_type=type_hints["http_route"])
        self._values: typing.Dict[str, typing.Any] = {}
        if grpc_route is not None:
            self._values["grpc_route"] = grpc_route
        if http2_route is not None:
            self._values["http2_route"] = http2_route
        if http_route is not None:
            self._values["http_route"] = http_route

    @builtins.property
    def grpc_route(self) -> typing.Optional["AppmeshGatewayRouteSpecGrpcRoute"]:
        '''grpc_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#grpc_route AppmeshGatewayRoute#grpc_route}
        '''
        result = self._values.get("grpc_route")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecGrpcRoute"], result)

    @builtins.property
    def http2_route(self) -> typing.Optional["AppmeshGatewayRouteSpecHttp2Route"]:
        '''http2_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http2_route AppmeshGatewayRoute#http2_route}
        '''
        result = self._values.get("http2_route")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2Route"], result)

    @builtins.property
    def http_route(self) -> typing.Optional["AppmeshGatewayRouteSpecHttpRoute"]:
        '''http_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http_route AppmeshGatewayRoute#http_route}
        '''
        result = self._values.get("http_route")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRoute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRoute",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "match": "match"},
)
class AppmeshGatewayRouteSpecGrpcRoute:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshGatewayRouteSpecGrpcRouteAction", typing.Dict[str, typing.Any]],
        match: typing.Union["AppmeshGatewayRouteSpecGrpcRouteMatch", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        if isinstance(action, dict):
            action = AppmeshGatewayRouteSpecGrpcRouteAction(**action)
        if isinstance(match, dict):
            match = AppmeshGatewayRouteSpecGrpcRouteMatch(**match)
        if __debug__:
            def stub(
                *,
                action: typing.Union[AppmeshGatewayRouteSpecGrpcRouteAction, typing.Dict[str, typing.Any]],
                match: typing.Union[AppmeshGatewayRouteSpecGrpcRouteMatch, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "match": match,
        }

    @builtins.property
    def action(self) -> "AppmeshGatewayRouteSpecGrpcRouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteAction", result)

    @builtins.property
    def match(self) -> "AppmeshGatewayRouteSpecGrpcRouteMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteAction",
    jsii_struct_bases=[],
    name_mapping={"target": "target"},
)
class AppmeshGatewayRouteSpecGrpcRouteAction:
    def __init__(
        self,
        *,
        target: typing.Union["AppmeshGatewayRouteSpecGrpcRouteActionTarget", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        if isinstance(target, dict):
            target = AppmeshGatewayRouteSpecGrpcRouteActionTarget(**target)
        if __debug__:
            def stub(
                *,
                target: typing.Union[AppmeshGatewayRouteSpecGrpcRouteActionTarget, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
        }

    @builtins.property
    def target(self) -> "AppmeshGatewayRouteSpecGrpcRouteActionTarget":
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteActionTarget", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecGrpcRouteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        value = AppmeshGatewayRouteSpecGrpcRouteActionTarget(
            virtual_service=virtual_service
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecGrpcRouteActionTarget"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecGrpcRouteActionTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_service": "virtualService"},
)
class AppmeshGatewayRouteSpecGrpcRouteActionTarget:
    def __init__(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        if isinstance(virtual_service, dict):
            virtual_service = AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService(**virtual_service)
        if __debug__:
            def stub(
                *,
                virtual_service: typing.Union[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument virtual_service", value=virtual_service, expected_type=type_hints["virtual_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service": virtual_service,
        }

    @builtins.property
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService":
        '''virtual_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        result = self._values.get("virtual_service")
        assert result is not None, "Required property 'virtual_service' is missing"
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRouteActionTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVirtualService")
    def put_virtual_service(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        value = AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService(
            virtual_service_name=virtual_service_name
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualService", [value]))

    @builtins.property
    @jsii.member(jsii_name="virtualService")
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference", jsii.get(self, "virtualService"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceInput")
    def virtual_service_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService"], jsii.get(self, "virtualServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTarget]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTarget],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTarget],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService",
    jsii_struct_bases=[],
    name_mapping={"virtual_service_name": "virtualServiceName"},
)
class AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService:
    def __init__(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        if __debug__:
            def stub(*, virtual_service_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument virtual_service_name", value=virtual_service_name, expected_type=type_hints["virtual_service_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service_name": virtual_service_name,
        }

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.'''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="virtualServiceNameInput")
    def virtual_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceName")
    def virtual_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualServiceName"))

    @virtual_service_name.setter
    def virtual_service_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteMatch",
    jsii_struct_bases=[],
    name_mapping={"service_name": "serviceName"},
)
class AppmeshGatewayRouteSpecGrpcRouteMatch:
    def __init__(self, *, service_name: builtins.str) -> None:
        '''
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#service_name AppmeshGatewayRoute#service_name}.
        '''
        if __debug__:
            def stub(*, service_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "service_name": service_name,
        }

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#service_name AppmeshGatewayRoute#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecGrpcRouteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        target: typing.Union[AppmeshGatewayRouteSpecGrpcRouteActionTarget, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        value = AppmeshGatewayRouteSpecGrpcRouteAction(target=target)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, service_name: builtins.str) -> None:
        '''
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#service_name AppmeshGatewayRoute#service_name}.
        '''
        value = AppmeshGatewayRouteSpecGrpcRouteMatch(service_name=service_name)

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshGatewayRouteSpecGrpcRouteActionOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecGrpcRouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRoute]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRoute],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppmeshGatewayRouteSpecGrpcRoute]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2Route",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "match": "match"},
)
class AppmeshGatewayRouteSpecHttp2Route:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshGatewayRouteSpecHttp2RouteAction", typing.Dict[str, typing.Any]],
        match: typing.Union["AppmeshGatewayRouteSpecHttp2RouteMatch", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        if isinstance(action, dict):
            action = AppmeshGatewayRouteSpecHttp2RouteAction(**action)
        if isinstance(match, dict):
            match = AppmeshGatewayRouteSpecHttp2RouteMatch(**match)
        if __debug__:
            def stub(
                *,
                action: typing.Union[AppmeshGatewayRouteSpecHttp2RouteAction, typing.Dict[str, typing.Any]],
                match: typing.Union[AppmeshGatewayRouteSpecHttp2RouteMatch, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "match": match,
        }

    @builtins.property
    def action(self) -> "AppmeshGatewayRouteSpecHttp2RouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteAction", result)

    @builtins.property
    def match(self) -> "AppmeshGatewayRouteSpecHttp2RouteMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2Route(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteAction",
    jsii_struct_bases=[],
    name_mapping={"target": "target", "rewrite": "rewrite"},
)
class AppmeshGatewayRouteSpecHttp2RouteAction:
    def __init__(
        self,
        *,
        target: typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionTarget", typing.Dict[str, typing.Any]],
        rewrite: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewrite", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        :param rewrite: rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        if isinstance(target, dict):
            target = AppmeshGatewayRouteSpecHttp2RouteActionTarget(**target)
        if isinstance(rewrite, dict):
            rewrite = AppmeshGatewayRouteSpecHttp2RouteActionRewrite(**rewrite)
        if __debug__:
            def stub(
                *,
                target: typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionTarget, typing.Dict[str, typing.Any]],
                rewrite: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionRewrite, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument rewrite", value=rewrite, expected_type=type_hints["rewrite"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
        }
        if rewrite is not None:
            self._values["rewrite"] = rewrite

    @builtins.property
    def target(self) -> "AppmeshGatewayRouteSpecHttp2RouteActionTarget":
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionTarget", result)

    @builtins.property
    def rewrite(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewrite"]:
        '''rewrite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        result = self._values.get("rewrite")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewrite"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRewrite")
    def put_rewrite(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname", typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: prefix block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteActionRewrite(
            hostname=hostname, prefix=prefix
        )

        return typing.cast(None, jsii.invoke(self, "putRewrite", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteActionTarget(
            virtual_service=virtual_service
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @jsii.member(jsii_name="resetRewrite")
    def reset_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRewrite", []))

    @builtins.property
    @jsii.member(jsii_name="rewrite")
    def rewrite(
        self,
    ) -> "AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference", jsii.get(self, "rewrite"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="rewriteInput")
    def rewrite_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewrite"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewrite"], jsii.get(self, "rewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionTarget"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewrite",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "prefix": "prefix"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionRewrite:
    def __init__(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname", typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: prefix block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        if isinstance(hostname, dict):
            hostname = AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname(**hostname)
        if isinstance(prefix, dict):
            prefix = AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix(**prefix)
        if __debug__:
            def stub(
                *,
                hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname, typing.Dict[str, typing.Any]]] = None,
                prefix: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def hostname(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname"]:
        '''hostname block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname"], result)

    @builtins.property
    def prefix(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix"]:
        '''prefix block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname",
    jsii_struct_bases=[],
    name_mapping={"default_target_hostname": "defaultTargetHostname"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname:
    def __init__(self, *, default_target_hostname: builtins.str) -> None:
        '''
        :param default_target_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.
        '''
        if __debug__:
            def stub(*, default_target_hostname: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_target_hostname", value=default_target_hostname, expected_type=type_hints["default_target_hostname"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_target_hostname": default_target_hostname,
        }

    @builtins.property
    def default_target_hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.'''
        result = self._values.get("default_target_hostname")
        assert result is not None, "Required property 'default_target_hostname' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultTargetHostnameInput")
    def default_target_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultTargetHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTargetHostname")
    def default_target_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultTargetHostname"))

    @default_target_hostname.setter
    def default_target_hostname(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTargetHostname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHostname")
    def put_hostname(self, *, default_target_hostname: builtins.str) -> None:
        '''
        :param default_target_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname(
            default_target_hostname=default_target_hostname
        )

        return typing.cast(None, jsii.invoke(self, "putHostname", [value]))

    @jsii.member(jsii_name="putPrefix")
    def put_prefix(
        self,
        *,
        default_prefix: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.
        '''
        value_ = AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix(
            default_prefix=default_prefix, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPrefix", [value_]))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(
        self,
    ) -> AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(
        self,
    ) -> "AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference", jsii.get(self, "prefix"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix"], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewrite]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewrite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewrite],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewrite],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix",
    jsii_struct_bases=[],
    name_mapping={"default_prefix": "defaultPrefix", "value": "value"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix:
    def __init__(
        self,
        *,
        default_prefix: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.
        '''
        if __debug__:
            def stub(
                *,
                default_prefix: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_prefix", value=default_prefix, expected_type=type_hints["default_prefix"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_prefix is not None:
            self._values["default_prefix"] = default_prefix
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def default_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.'''
        result = self._values.get("default_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefaultPrefix")
    def reset_default_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultPrefix", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="defaultPrefixInput")
    def default_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPrefix")
    def default_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultPrefix"))

    @default_prefix.setter
    def default_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_service": "virtualService"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionTarget:
    def __init__(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        if isinstance(virtual_service, dict):
            virtual_service = AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService(**virtual_service)
        if __debug__:
            def stub(
                *,
                virtual_service: typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument virtual_service", value=virtual_service, expected_type=type_hints["virtual_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service": virtual_service,
        }

    @builtins.property
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService":
        '''virtual_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        result = self._values.get("virtual_service")
        assert result is not None, "Required property 'virtual_service' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVirtualService")
    def put_virtual_service(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService(
            virtual_service_name=virtual_service_name
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualService", [value]))

    @builtins.property
    @jsii.member(jsii_name="virtualService")
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference", jsii.get(self, "virtualService"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceInput")
    def virtual_service_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService"], jsii.get(self, "virtualServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTarget]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTarget],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTarget],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService",
    jsii_struct_bases=[],
    name_mapping={"virtual_service_name": "virtualServiceName"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService:
    def __init__(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        if __debug__:
            def stub(*, virtual_service_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument virtual_service_name", value=virtual_service_name, expected_type=type_hints["virtual_service_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service_name": virtual_service_name,
        }

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.'''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="virtualServiceNameInput")
    def virtual_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceName")
    def virtual_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualServiceName"))

    @virtual_service_name.setter
    def virtual_service_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteMatch",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "prefix": "prefix"},
)
class AppmeshGatewayRouteSpecHttp2RouteMatch:
    def __init__(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteMatchHostname", typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.
        '''
        if isinstance(hostname, dict):
            hostname = AppmeshGatewayRouteSpecHttp2RouteMatchHostname(**hostname)
        if __debug__:
            def stub(
                *,
                hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteMatchHostname, typing.Dict[str, typing.Any]]] = None,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def hostname(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteMatchHostname"]:
        '''hostname block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteMatchHostname"], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteMatchHostname",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "suffix": "suffix"},
)
class AppmeshGatewayRouteSpecHttp2RouteMatchHostname:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.
        '''
        if __debug__:
            def stub(
                *,
                exact: typing.Optional[builtins.str] = None,
                suffix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if suffix is not None:
            self._values["suffix"] = suffix

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.'''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suffix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.'''
        result = self._values.get("suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteMatchHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetSuffix")
    def reset_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuffix", []))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHostname")
    def put_hostname(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteMatchHostname(
            exact=exact, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putHostname", [value]))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttp2RouteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        target: typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionTarget, typing.Dict[str, typing.Any]],
        rewrite: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionRewrite, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        :param rewrite: rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteAction(target=target, rewrite=rewrite)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteMatchHostname, typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteMatch(
            hostname=hostname, prefix=prefix
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshGatewayRouteSpecHttp2RouteActionOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2Route]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2Route], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2Route],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppmeshGatewayRouteSpecHttp2Route]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRoute",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "match": "match"},
)
class AppmeshGatewayRouteSpecHttpRoute:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshGatewayRouteSpecHttpRouteAction", typing.Dict[str, typing.Any]],
        match: typing.Union["AppmeshGatewayRouteSpecHttpRouteMatch", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        if isinstance(action, dict):
            action = AppmeshGatewayRouteSpecHttpRouteAction(**action)
        if isinstance(match, dict):
            match = AppmeshGatewayRouteSpecHttpRouteMatch(**match)
        if __debug__:
            def stub(
                *,
                action: typing.Union[AppmeshGatewayRouteSpecHttpRouteAction, typing.Dict[str, typing.Any]],
                match: typing.Union[AppmeshGatewayRouteSpecHttpRouteMatch, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "match": match,
        }

    @builtins.property
    def action(self) -> "AppmeshGatewayRouteSpecHttpRouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteAction", result)

    @builtins.property
    def match(self) -> "AppmeshGatewayRouteSpecHttpRouteMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteAction",
    jsii_struct_bases=[],
    name_mapping={"target": "target", "rewrite": "rewrite"},
)
class AppmeshGatewayRouteSpecHttpRouteAction:
    def __init__(
        self,
        *,
        target: typing.Union["AppmeshGatewayRouteSpecHttpRouteActionTarget", typing.Dict[str, typing.Any]],
        rewrite: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewrite", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        :param rewrite: rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        if isinstance(target, dict):
            target = AppmeshGatewayRouteSpecHttpRouteActionTarget(**target)
        if isinstance(rewrite, dict):
            rewrite = AppmeshGatewayRouteSpecHttpRouteActionRewrite(**rewrite)
        if __debug__:
            def stub(
                *,
                target: typing.Union[AppmeshGatewayRouteSpecHttpRouteActionTarget, typing.Dict[str, typing.Any]],
                rewrite: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteActionRewrite, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument rewrite", value=rewrite, expected_type=type_hints["rewrite"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
        }
        if rewrite is not None:
            self._values["rewrite"] = rewrite

    @builtins.property
    def target(self) -> "AppmeshGatewayRouteSpecHttpRouteActionTarget":
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionTarget", result)

    @builtins.property
    def rewrite(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewrite"]:
        '''rewrite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        result = self._values.get("rewrite")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewrite"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRewrite")
    def put_rewrite(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname", typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: prefix block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        value = AppmeshGatewayRouteSpecHttpRouteActionRewrite(
            hostname=hostname, prefix=prefix
        )

        return typing.cast(None, jsii.invoke(self, "putRewrite", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        value = AppmeshGatewayRouteSpecHttpRouteActionTarget(
            virtual_service=virtual_service
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @jsii.member(jsii_name="resetRewrite")
    def reset_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRewrite", []))

    @builtins.property
    @jsii.member(jsii_name="rewrite")
    def rewrite(self) -> "AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference", jsii.get(self, "rewrite"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="rewriteInput")
    def rewrite_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewrite"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewrite"], jsii.get(self, "rewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionTarget"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewrite",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "prefix": "prefix"},
)
class AppmeshGatewayRouteSpecHttpRouteActionRewrite:
    def __init__(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname", typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: prefix block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        if isinstance(hostname, dict):
            hostname = AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname(**hostname)
        if isinstance(prefix, dict):
            prefix = AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix(**prefix)
        if __debug__:
            def stub(
                *,
                hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname, typing.Dict[str, typing.Any]]] = None,
                prefix: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def hostname(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname"]:
        '''hostname block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname"], result)

    @builtins.property
    def prefix(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix"]:
        '''prefix block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname",
    jsii_struct_bases=[],
    name_mapping={"default_target_hostname": "defaultTargetHostname"},
)
class AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname:
    def __init__(self, *, default_target_hostname: builtins.str) -> None:
        '''
        :param default_target_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.
        '''
        if __debug__:
            def stub(*, default_target_hostname: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_target_hostname", value=default_target_hostname, expected_type=type_hints["default_target_hostname"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_target_hostname": default_target_hostname,
        }

    @builtins.property
    def default_target_hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.'''
        result = self._values.get("default_target_hostname")
        assert result is not None, "Required property 'default_target_hostname' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultTargetHostnameInput")
    def default_target_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultTargetHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTargetHostname")
    def default_target_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultTargetHostname"))

    @default_target_hostname.setter
    def default_target_hostname(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTargetHostname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHostname")
    def put_hostname(self, *, default_target_hostname: builtins.str) -> None:
        '''
        :param default_target_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.
        '''
        value = AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname(
            default_target_hostname=default_target_hostname
        )

        return typing.cast(None, jsii.invoke(self, "putHostname", [value]))

    @jsii.member(jsii_name="putPrefix")
    def put_prefix(
        self,
        *,
        default_prefix: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.
        '''
        value_ = AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix(
            default_prefix=default_prefix, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPrefix", [value_]))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(
        self,
    ) -> AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(
        self,
    ) -> "AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference", jsii.get(self, "prefix"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix"], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewrite]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewrite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewrite],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewrite],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix",
    jsii_struct_bases=[],
    name_mapping={"default_prefix": "defaultPrefix", "value": "value"},
)
class AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix:
    def __init__(
        self,
        *,
        default_prefix: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.
        '''
        if __debug__:
            def stub(
                *,
                default_prefix: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_prefix", value=default_prefix, expected_type=type_hints["default_prefix"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_prefix is not None:
            self._values["default_prefix"] = default_prefix
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def default_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.'''
        result = self._values.get("default_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefaultPrefix")
    def reset_default_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultPrefix", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="defaultPrefixInput")
    def default_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPrefix")
    def default_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultPrefix"))

    @default_prefix.setter
    def default_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_service": "virtualService"},
)
class AppmeshGatewayRouteSpecHttpRouteActionTarget:
    def __init__(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        if isinstance(virtual_service, dict):
            virtual_service = AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService(**virtual_service)
        if __debug__:
            def stub(
                *,
                virtual_service: typing.Union[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument virtual_service", value=virtual_service, expected_type=type_hints["virtual_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service": virtual_service,
        }

    @builtins.property
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService":
        '''virtual_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        result = self._values.get("virtual_service")
        assert result is not None, "Required property 'virtual_service' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVirtualService")
    def put_virtual_service(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        value = AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService(
            virtual_service_name=virtual_service_name
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualService", [value]))

    @builtins.property
    @jsii.member(jsii_name="virtualService")
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference", jsii.get(self, "virtualService"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceInput")
    def virtual_service_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService"], jsii.get(self, "virtualServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTarget]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTarget],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTarget],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService",
    jsii_struct_bases=[],
    name_mapping={"virtual_service_name": "virtualServiceName"},
)
class AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService:
    def __init__(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        if __debug__:
            def stub(*, virtual_service_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument virtual_service_name", value=virtual_service_name, expected_type=type_hints["virtual_service_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service_name": virtual_service_name,
        }

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.'''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="virtualServiceNameInput")
    def virtual_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceName")
    def virtual_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualServiceName"))

    @virtual_service_name.setter
    def virtual_service_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteMatch",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "prefix": "prefix"},
)
class AppmeshGatewayRouteSpecHttpRouteMatch:
    def __init__(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteMatchHostname", typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.
        '''
        if isinstance(hostname, dict):
            hostname = AppmeshGatewayRouteSpecHttpRouteMatchHostname(**hostname)
        if __debug__:
            def stub(
                *,
                hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteMatchHostname, typing.Dict[str, typing.Any]]] = None,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def hostname(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteMatchHostname"]:
        '''hostname block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteMatchHostname"], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteMatchHostname",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "suffix": "suffix"},
)
class AppmeshGatewayRouteSpecHttpRouteMatchHostname:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.
        '''
        if __debug__:
            def stub(
                *,
                exact: typing.Optional[builtins.str] = None,
                suffix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if suffix is not None:
            self._values["suffix"] = suffix

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.'''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suffix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.'''
        result = self._values.get("suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteMatchHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetSuffix")
    def reset_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuffix", []))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttpRouteMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteMatchOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHostname")
    def put_hostname(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.
        '''
        value = AppmeshGatewayRouteSpecHttpRouteMatchHostname(
            exact=exact, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putHostname", [value]))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttpRouteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        target: typing.Union[AppmeshGatewayRouteSpecHttpRouteActionTarget, typing.Dict[str, typing.Any]],
        rewrite: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteActionRewrite, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        :param rewrite: rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        value = AppmeshGatewayRouteSpecHttpRouteAction(target=target, rewrite=rewrite)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteMatchHostname, typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.
        '''
        value = AppmeshGatewayRouteSpecHttpRouteMatch(hostname=hostname, prefix=prefix)

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshGatewayRouteSpecHttpRouteActionOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshGatewayRouteSpecHttpRouteMatchOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRoute]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRoute],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppmeshGatewayRouteSpecHttpRoute]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGrpcRoute")
    def put_grpc_route(
        self,
        *,
        action: typing.Union[AppmeshGatewayRouteSpecGrpcRouteAction, typing.Dict[str, typing.Any]],
        match: typing.Union[AppmeshGatewayRouteSpecGrpcRouteMatch, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        value = AppmeshGatewayRouteSpecGrpcRoute(action=action, match=match)

        return typing.cast(None, jsii.invoke(self, "putGrpcRoute", [value]))

    @jsii.member(jsii_name="putHttp2Route")
    def put_http2_route(
        self,
        *,
        action: typing.Union[AppmeshGatewayRouteSpecHttp2RouteAction, typing.Dict[str, typing.Any]],
        match: typing.Union[AppmeshGatewayRouteSpecHttp2RouteMatch, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        value = AppmeshGatewayRouteSpecHttp2Route(action=action, match=match)

        return typing.cast(None, jsii.invoke(self, "putHttp2Route", [value]))

    @jsii.member(jsii_name="putHttpRoute")
    def put_http_route(
        self,
        *,
        action: typing.Union[AppmeshGatewayRouteSpecHttpRouteAction, typing.Dict[str, typing.Any]],
        match: typing.Union[AppmeshGatewayRouteSpecHttpRouteMatch, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        value = AppmeshGatewayRouteSpecHttpRoute(action=action, match=match)

        return typing.cast(None, jsii.invoke(self, "putHttpRoute", [value]))

    @jsii.member(jsii_name="resetGrpcRoute")
    def reset_grpc_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpcRoute", []))

    @jsii.member(jsii_name="resetHttp2Route")
    def reset_http2_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2Route", []))

    @jsii.member(jsii_name="resetHttpRoute")
    def reset_http_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRoute", []))

    @builtins.property
    @jsii.member(jsii_name="grpcRoute")
    def grpc_route(self) -> AppmeshGatewayRouteSpecGrpcRouteOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecGrpcRouteOutputReference, jsii.get(self, "grpcRoute"))

    @builtins.property
    @jsii.member(jsii_name="http2Route")
    def http2_route(self) -> AppmeshGatewayRouteSpecHttp2RouteOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteOutputReference, jsii.get(self, "http2Route"))

    @builtins.property
    @jsii.member(jsii_name="httpRoute")
    def http_route(self) -> AppmeshGatewayRouteSpecHttpRouteOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteOutputReference, jsii.get(self, "httpRoute"))

    @builtins.property
    @jsii.member(jsii_name="grpcRouteInput")
    def grpc_route_input(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRoute]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRoute], jsii.get(self, "grpcRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="http2RouteInput")
    def http2_route_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2Route]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2Route], jsii.get(self, "http2RouteInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRouteInput")
    def http_route_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRoute]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRoute], jsii.get(self, "httpRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpec]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshGatewayRouteSpec]) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppmeshGatewayRouteSpec]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppmeshGatewayRoute",
    "AppmeshGatewayRouteConfig",
    "AppmeshGatewayRouteSpec",
    "AppmeshGatewayRouteSpecGrpcRoute",
    "AppmeshGatewayRouteSpecGrpcRouteAction",
    "AppmeshGatewayRouteSpecGrpcRouteActionOutputReference",
    "AppmeshGatewayRouteSpecGrpcRouteActionTarget",
    "AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference",
    "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService",
    "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference",
    "AppmeshGatewayRouteSpecGrpcRouteMatch",
    "AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference",
    "AppmeshGatewayRouteSpecGrpcRouteOutputReference",
    "AppmeshGatewayRouteSpecHttp2Route",
    "AppmeshGatewayRouteSpecHttp2RouteAction",
    "AppmeshGatewayRouteSpecHttp2RouteActionOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewrite",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionTarget",
    "AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService",
    "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteMatch",
    "AppmeshGatewayRouteSpecHttp2RouteMatchHostname",
    "AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteOutputReference",
    "AppmeshGatewayRouteSpecHttpRoute",
    "AppmeshGatewayRouteSpecHttpRouteAction",
    "AppmeshGatewayRouteSpecHttpRouteActionOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionRewrite",
    "AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname",
    "AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix",
    "AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionTarget",
    "AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService",
    "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteMatch",
    "AppmeshGatewayRouteSpecHttpRouteMatchHostname",
    "AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteMatchOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteOutputReference",
    "AppmeshGatewayRouteSpecOutputReference",
]

publication.publish()
