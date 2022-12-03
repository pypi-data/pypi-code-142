'''
# `aws_appmesh_virtual_node`

Refer to the Terraform Registory for docs: [`aws_appmesh_virtual_node`](https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node).
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


class AppmeshVirtualNode(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNode",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node aws_appmesh_virtual_node}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        mesh_name: builtins.str,
        name: builtins.str,
        spec: typing.Union["AppmeshVirtualNodeSpec", typing.Dict[str, typing.Any]],
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node aws_appmesh_virtual_node} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_name AppmeshVirtualNode#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#name AppmeshVirtualNode#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#spec AppmeshVirtualNode#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#id AppmeshVirtualNode#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_owner AppmeshVirtualNode#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags AppmeshVirtualNode#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags_all AppmeshVirtualNode#tags_all}.
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
                spec: typing.Union[AppmeshVirtualNodeSpec, typing.Dict[str, typing.Any]],
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
        config = AppmeshVirtualNodeConfig(
            mesh_name=mesh_name,
            name=name,
            spec=spec,
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
        backend: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppmeshVirtualNodeSpecBackend", typing.Dict[str, typing.Any]]]]] = None,
        backend_defaults: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaults", typing.Dict[str, typing.Any]]] = None,
        listener: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListener", typing.Dict[str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["AppmeshVirtualNodeSpecLogging", typing.Dict[str, typing.Any]]] = None,
        service_discovery: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscovery", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend AppmeshVirtualNode#backend}
        :param backend_defaults: backend_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend_defaults AppmeshVirtualNode#backend_defaults}
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#listener AppmeshVirtualNode#listener}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#logging AppmeshVirtualNode#logging}
        :param service_discovery: service_discovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_discovery AppmeshVirtualNode#service_discovery}
        '''
        value = AppmeshVirtualNodeSpec(
            backend=backend,
            backend_defaults=backend_defaults,
            listener=listener,
            logging=logging,
            service_discovery=service_discovery,
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
    def spec(self) -> "AppmeshVirtualNodeSpecOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecOutputReference", jsii.get(self, "spec"))

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
    def spec_input(self) -> typing.Optional["AppmeshVirtualNodeSpec"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpec"], jsii.get(self, "specInput"))

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeConfig",
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
        "id": "id",
        "mesh_owner": "meshOwner",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class AppmeshVirtualNodeConfig(cdktf.TerraformMetaArguments):
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
        spec: typing.Union["AppmeshVirtualNodeSpec", typing.Dict[str, typing.Any]],
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
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_name AppmeshVirtualNode#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#name AppmeshVirtualNode#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#spec AppmeshVirtualNode#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#id AppmeshVirtualNode#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_owner AppmeshVirtualNode#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags AppmeshVirtualNode#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags_all AppmeshVirtualNode#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(spec, dict):
            spec = AppmeshVirtualNodeSpec(**spec)
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
                spec: typing.Union[AppmeshVirtualNodeSpec, typing.Dict[str, typing.Any]],
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
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mesh_owner", value=mesh_owner, expected_type=type_hints["mesh_owner"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "mesh_name": mesh_name,
            "name": name,
            "spec": spec,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_name AppmeshVirtualNode#mesh_name}.'''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#name AppmeshVirtualNode#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(self) -> "AppmeshVirtualNodeSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#spec AppmeshVirtualNode#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("AppmeshVirtualNodeSpec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#id AppmeshVirtualNode#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_owner AppmeshVirtualNode#mesh_owner}.'''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags AppmeshVirtualNode#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags_all AppmeshVirtualNode#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpec",
    jsii_struct_bases=[],
    name_mapping={
        "backend": "backend",
        "backend_defaults": "backendDefaults",
        "listener": "listener",
        "logging": "logging",
        "service_discovery": "serviceDiscovery",
    },
)
class AppmeshVirtualNodeSpec:
    def __init__(
        self,
        *,
        backend: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppmeshVirtualNodeSpecBackend", typing.Dict[str, typing.Any]]]]] = None,
        backend_defaults: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaults", typing.Dict[str, typing.Any]]] = None,
        listener: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListener", typing.Dict[str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["AppmeshVirtualNodeSpecLogging", typing.Dict[str, typing.Any]]] = None,
        service_discovery: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscovery", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend AppmeshVirtualNode#backend}
        :param backend_defaults: backend_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend_defaults AppmeshVirtualNode#backend_defaults}
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#listener AppmeshVirtualNode#listener}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#logging AppmeshVirtualNode#logging}
        :param service_discovery: service_discovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_discovery AppmeshVirtualNode#service_discovery}
        '''
        if isinstance(backend_defaults, dict):
            backend_defaults = AppmeshVirtualNodeSpecBackendDefaults(**backend_defaults)
        if isinstance(listener, dict):
            listener = AppmeshVirtualNodeSpecListener(**listener)
        if isinstance(logging, dict):
            logging = AppmeshVirtualNodeSpecLogging(**logging)
        if isinstance(service_discovery, dict):
            service_discovery = AppmeshVirtualNodeSpecServiceDiscovery(**service_discovery)
        if __debug__:
            def stub(
                *,
                backend: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppmeshVirtualNodeSpecBackend, typing.Dict[str, typing.Any]]]]] = None,
                backend_defaults: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaults, typing.Dict[str, typing.Any]]] = None,
                listener: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListener, typing.Dict[str, typing.Any]]] = None,
                logging: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLogging, typing.Dict[str, typing.Any]]] = None,
                service_discovery: typing.Optional[typing.Union[AppmeshVirtualNodeSpecServiceDiscovery, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument backend_defaults", value=backend_defaults, expected_type=type_hints["backend_defaults"])
            check_type(argname="argument listener", value=listener, expected_type=type_hints["listener"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument service_discovery", value=service_discovery, expected_type=type_hints["service_discovery"])
        self._values: typing.Dict[str, typing.Any] = {}
        if backend is not None:
            self._values["backend"] = backend
        if backend_defaults is not None:
            self._values["backend_defaults"] = backend_defaults
        if listener is not None:
            self._values["listener"] = listener
        if logging is not None:
            self._values["logging"] = logging
        if service_discovery is not None:
            self._values["service_discovery"] = service_discovery

    @builtins.property
    def backend(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppmeshVirtualNodeSpecBackend"]]]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend AppmeshVirtualNode#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppmeshVirtualNodeSpecBackend"]]], result)

    @builtins.property
    def backend_defaults(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaults"]:
        '''backend_defaults block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend_defaults AppmeshVirtualNode#backend_defaults}
        '''
        result = self._values.get("backend_defaults")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaults"], result)

    @builtins.property
    def listener(self) -> typing.Optional["AppmeshVirtualNodeSpecListener"]:
        '''listener block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#listener AppmeshVirtualNode#listener}
        '''
        result = self._values.get("listener")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListener"], result)

    @builtins.property
    def logging(self) -> typing.Optional["AppmeshVirtualNodeSpecLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#logging AppmeshVirtualNode#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecLogging"], result)

    @builtins.property
    def service_discovery(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecServiceDiscovery"]:
        '''service_discovery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_discovery AppmeshVirtualNode#service_discovery}
        '''
        result = self._values.get("service_discovery")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecServiceDiscovery"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackend",
    jsii_struct_bases=[],
    name_mapping={"virtual_service": "virtualService"},
)
class AppmeshVirtualNodeSpecBackend:
    def __init__(
        self,
        *,
        virtual_service: typing.Union["AppmeshVirtualNodeSpecBackendVirtualService", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service AppmeshVirtualNode#virtual_service}
        '''
        if isinstance(virtual_service, dict):
            virtual_service = AppmeshVirtualNodeSpecBackendVirtualService(**virtual_service)
        if __debug__:
            def stub(
                *,
                virtual_service: typing.Union[AppmeshVirtualNodeSpecBackendVirtualService, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument virtual_service", value=virtual_service, expected_type=type_hints["virtual_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service": virtual_service,
        }

    @builtins.property
    def virtual_service(self) -> "AppmeshVirtualNodeSpecBackendVirtualService":
        '''virtual_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service AppmeshVirtualNode#virtual_service}
        '''
        result = self._values.get("virtual_service")
        assert result is not None, "Required property 'virtual_service' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaults",
    jsii_struct_bases=[],
    name_mapping={"client_policy": "clientPolicy"},
)
class AppmeshVirtualNodeSpecBackendDefaults:
    def __init__(
        self,
        *,
        client_policy: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicy", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        if isinstance(client_policy, dict):
            client_policy = AppmeshVirtualNodeSpecBackendDefaultsClientPolicy(**client_policy)
        if __debug__:
            def stub(
                *,
                client_policy: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_policy", value=client_policy, expected_type=type_hints["client_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_policy is not None:
            self._values["client_policy"] = client_policy

    @builtins.property
    def client_policy(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicy"]:
        '''client_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        result = self._values.get("client_policy")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaults(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicy",
    jsii_struct_bases=[],
    name_mapping={"tls": "tls"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicy:
    def __init__(
        self,
        *,
        tls: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        if isinstance(tls, dict):
            tls = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls(**tls)
        if __debug__:
            def stub(
                *,
                tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[str, typing.Any] = {}
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference",
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

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        validation: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation", typing.Dict[str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate", typing.Dict[str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls(
            validation=validation,
            certificate=certificate,
            enforce=enforce,
            ports=ports,
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls",
    jsii_struct_bases=[],
    name_mapping={
        "validation": "validation",
        "certificate": "certificate",
        "enforce": "enforce",
        "ports": "ports",
    },
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls:
    def __init__(
        self,
        *,
        validation: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation", typing.Dict[str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate", typing.Dict[str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.
        '''
        if isinstance(validation, dict):
            validation = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation(**validation)
        if isinstance(certificate, dict):
            certificate = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate(**certificate)
        if __debug__:
            def stub(
                *,
                validation: typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation, typing.Dict[str, typing.Any]],
                certificate: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate, typing.Dict[str, typing.Any]]] = None,
                enforce: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument enforce", value=enforce, expected_type=type_hints["enforce"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {
            "validation": validation,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if enforce is not None:
            self._values["enforce"] = enforce
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation":
        '''validation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        result = self._values.get("validation")
        assert result is not None, "Required property 'validation' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation", result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate"]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate"], result)

    @builtins.property
    def enforce(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.'''
        result = self._values.get("enforce")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.'''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile", typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds(**sds)
        if __debug__:
            def stub(
                *,
                file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile, typing.Dict[str, typing.Any]]] = None,
                sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_chain": "certificateChain",
        "private_key": "privateKey",
    },
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile:
    def __init__(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        if __debug__:
            def stub(
                *,
                certificate_chain: builtins.str,
                private_key: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_chain": certificate_chain,
            "private_key": private_key,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference",
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
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference",
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

    @jsii.member(jsii_name="putFile")
    def put_file(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile(
            certificate_chain=certificate_chain, private_key=private_key
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            def stub(*, secret_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference",
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
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference",
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

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile, typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate(
            file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putValidation")
    def put_validation(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust", typing.Dict[str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation(
            trust=trust, subject_alternative_names=subject_alternative_names
        )

        return typing.cast(None, jsii.invoke(self, "putValidation", [value]))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetEnforce")
    def reset_enforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforce", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference", jsii.get(self, "validation"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceInput")
    def enforce_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforceInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="validationInput")
    def validation_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation"], jsii.get(self, "validationInput"))

    @builtins.property
    @jsii.member(jsii_name="enforce")
    def enforce(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforce"))

    @enforce.setter
    def enforce(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforce", value)

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation:
    def __init__(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust", typing.Dict[str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        if isinstance(trust, dict):
            trust = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust(**trust)
        if isinstance(subject_alternative_names, dict):
            subject_alternative_names = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(**subject_alternative_names)
        if __debug__:
            def stub(
                *,
                trust: typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust, typing.Dict[str, typing.Any]],
                subject_alternative_names: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument trust", value=trust, expected_type=type_hints["trust"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
        self._values: typing.Dict[str, typing.Any] = {
            "trust": trust,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust":
        '''trust block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        '''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"]:
        '''subject_alternative_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference",
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

    @jsii.member(jsii_name="putSubjectAlternativeNames")
    def put_subject_alternative_names(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(
            match=match
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAlternativeNames", [value]))

    @jsii.member(jsii_name="putTrust")
    def put_trust(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm", typing.Dict[str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile", typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust(
            acm=acm, file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putTrust", [value]))

    @jsii.member(jsii_name="resetSubjectAlternativeNames")
    def reset_subject_alternative_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectAlternativeNames", []))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference", jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="trust")
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference", jsii.get(self, "trust"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNamesInput")
    def subject_alternative_names_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"], jsii.get(self, "subjectAlternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="trustInput")
    def trust_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust"], jsii.get(self, "trustInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames",
    jsii_struct_bases=[],
    name_mapping={"match": "match"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames:
    def __init__(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        if isinstance(match, dict):
            match = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(**match)
        if __debug__:
            def stub(
                *,
                match: typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[str, typing.Any] = {
            "match": match,
        }

    @builtins.property
    def match(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch:
    def __init__(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        if __debug__:
            def stub(*, exact: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
        self._values: typing.Dict[str, typing.Any] = {
            "exact": exact,
        }

    @builtins.property
    def exact(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.'''
        result = self._values.get("exact")
        assert result is not None, "Required property 'exact' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
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
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
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

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(
            exact=exact
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust",
    jsii_struct_bases=[],
    name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust:
    def __init__(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm", typing.Dict[str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile", typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(acm, dict):
            acm = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm(**acm)
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds(**sds)
        if __debug__:
            def stub(
                *,
                acm: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm, typing.Dict[str, typing.Any]]] = None,
                file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile, typing.Dict[str, typing.Any]]] = None,
                sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument acm", value=acm, expected_type=type_hints["acm"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if acm is not None:
            self._values["acm"] = acm
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def acm(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm"]:
        '''acm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        '''
        result = self._values.get("acm")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm"], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm",
    jsii_struct_bases=[],
    name_mapping={"certificate_authority_arns": "certificateAuthorityArns"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm:
    def __init__(
        self,
        *,
        certificate_authority_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.
        '''
        if __debug__:
            def stub(
                *,
                certificate_authority_arns: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_authority_arns", value=certificate_authority_arns, expected_type=type_hints["certificate_authority_arns"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_authority_arns": certificate_authority_arns,
        }

    @builtins.property
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.'''
        result = self._values.get("certificate_authority_arns")
        assert result is not None, "Required property 'certificate_authority_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference",
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
    @jsii.member(jsii_name="certificateAuthorityArnsInput")
    def certificate_authority_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateAuthorityArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificateAuthorityArns"))

    @certificate_authority_arns.setter
    def certificate_authority_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile",
    jsii_struct_bases=[],
    name_mapping={"certificate_chain": "certificateChain"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile:
    def __init__(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        if __debug__:
            def stub(*, certificate_chain: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_chain": certificate_chain,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference",
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
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference",
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

    @jsii.member(jsii_name="putAcm")
    def put_acm(
        self,
        *,
        certificate_authority_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm(
            certificate_authority_arns=certificate_authority_arns
        )

        return typing.cast(None, jsii.invoke(self, "putAcm", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile(
            certificate_chain=certificate_chain
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetAcm")
    def reset_acm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcm", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="acm")
    def acm(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference, jsii.get(self, "acm"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="acmInput")
    def acm_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm], jsii.get(self, "acmInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            def stub(*, secret_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference",
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
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsOutputReference",
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

    @jsii.member(jsii_name="putClientPolicy")
    def put_client_policy(
        self,
        *,
        tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicy(tls=tls)

        return typing.cast(None, jsii.invoke(self, "putClientPolicy", [value]))

    @jsii.member(jsii_name="resetClientPolicy")
    def reset_client_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="clientPolicy")
    def client_policy(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference, jsii.get(self, "clientPolicy"))

    @builtins.property
    @jsii.member(jsii_name="clientPolicyInput")
    def client_policy_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy], jsii.get(self, "clientPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaults]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaults], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaults],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaults],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppmeshVirtualNodeSpecBackendOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppmeshVirtualNodeSpecBackendOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVirtualService")
    def put_virtual_service(
        self,
        *,
        virtual_service_name: builtins.str,
        client_policy: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service_name AppmeshVirtualNode#virtual_service_name}.
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualService(
            virtual_service_name=virtual_service_name, client_policy=client_policy
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualService", [value]))

    @builtins.property
    @jsii.member(jsii_name="virtualService")
    def virtual_service(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference", jsii.get(self, "virtualService"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceInput")
    def virtual_service_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualService"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualService"], jsii.get(self, "virtualServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackend, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackend, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackend, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackend, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualService",
    jsii_struct_bases=[],
    name_mapping={
        "virtual_service_name": "virtualServiceName",
        "client_policy": "clientPolicy",
    },
)
class AppmeshVirtualNodeSpecBackendVirtualService:
    def __init__(
        self,
        *,
        virtual_service_name: builtins.str,
        client_policy: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service_name AppmeshVirtualNode#virtual_service_name}.
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        if isinstance(client_policy, dict):
            client_policy = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy(**client_policy)
        if __debug__:
            def stub(
                *,
                virtual_service_name: builtins.str,
                client_policy: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument virtual_service_name", value=virtual_service_name, expected_type=type_hints["virtual_service_name"])
            check_type(argname="argument client_policy", value=client_policy, expected_type=type_hints["client_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "virtual_service_name": virtual_service_name,
        }
        if client_policy is not None:
            self._values["client_policy"] = client_policy

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service_name AppmeshVirtualNode#virtual_service_name}.'''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_policy(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy"]:
        '''client_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        result = self._values.get("client_policy")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy",
    jsii_struct_bases=[],
    name_mapping={"tls": "tls"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy:
    def __init__(
        self,
        *,
        tls: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        if isinstance(tls, dict):
            tls = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls(**tls)
        if __debug__:
            def stub(
                *,
                tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[str, typing.Any] = {}
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference",
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

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        validation: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation", typing.Dict[str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate", typing.Dict[str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls(
            validation=validation,
            certificate=certificate,
            enforce=enforce,
            ports=ports,
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls",
    jsii_struct_bases=[],
    name_mapping={
        "validation": "validation",
        "certificate": "certificate",
        "enforce": "enforce",
        "ports": "ports",
    },
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls:
    def __init__(
        self,
        *,
        validation: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation", typing.Dict[str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate", typing.Dict[str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.
        '''
        if isinstance(validation, dict):
            validation = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation(**validation)
        if isinstance(certificate, dict):
            certificate = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate(**certificate)
        if __debug__:
            def stub(
                *,
                validation: typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation, typing.Dict[str, typing.Any]],
                certificate: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate, typing.Dict[str, typing.Any]]] = None,
                enforce: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument enforce", value=enforce, expected_type=type_hints["enforce"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {
            "validation": validation,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if enforce is not None:
            self._values["enforce"] = enforce
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation":
        '''validation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        result = self._values.get("validation")
        assert result is not None, "Required property 'validation' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation", result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate"]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate"], result)

    @builtins.property
    def enforce(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.'''
        result = self._values.get("enforce")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.'''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile", typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds(**sds)
        if __debug__:
            def stub(
                *,
                file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile, typing.Dict[str, typing.Any]]] = None,
                sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_chain": "certificateChain",
        "private_key": "privateKey",
    },
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile:
    def __init__(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        if __debug__:
            def stub(
                *,
                certificate_chain: builtins.str,
                private_key: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_chain": certificate_chain,
            "private_key": private_key,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference",
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
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference",
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

    @jsii.member(jsii_name="putFile")
    def put_file(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile(
            certificate_chain=certificate_chain, private_key=private_key
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            def stub(*, secret_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference",
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
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference",
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

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile, typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate(
            file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putValidation")
    def put_validation(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust", typing.Dict[str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation(
            trust=trust, subject_alternative_names=subject_alternative_names
        )

        return typing.cast(None, jsii.invoke(self, "putValidation", [value]))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetEnforce")
    def reset_enforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforce", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference", jsii.get(self, "validation"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceInput")
    def enforce_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforceInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="validationInput")
    def validation_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation"], jsii.get(self, "validationInput"))

    @builtins.property
    @jsii.member(jsii_name="enforce")
    def enforce(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforce"))

    @enforce.setter
    def enforce(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforce", value)

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation:
    def __init__(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust", typing.Dict[str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        if isinstance(trust, dict):
            trust = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust(**trust)
        if isinstance(subject_alternative_names, dict):
            subject_alternative_names = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames(**subject_alternative_names)
        if __debug__:
            def stub(
                *,
                trust: typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust, typing.Dict[str, typing.Any]],
                subject_alternative_names: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument trust", value=trust, expected_type=type_hints["trust"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
        self._values: typing.Dict[str, typing.Any] = {
            "trust": trust,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust":
        '''trust block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        '''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames"]:
        '''subject_alternative_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference",
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

    @jsii.member(jsii_name="putSubjectAlternativeNames")
    def put_subject_alternative_names(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames(
            match=match
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAlternativeNames", [value]))

    @jsii.member(jsii_name="putTrust")
    def put_trust(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm", typing.Dict[str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile", typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust(
            acm=acm, file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putTrust", [value]))

    @jsii.member(jsii_name="resetSubjectAlternativeNames")
    def reset_subject_alternative_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectAlternativeNames", []))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference", jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="trust")
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference", jsii.get(self, "trust"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNamesInput")
    def subject_alternative_names_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames"], jsii.get(self, "subjectAlternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="trustInput")
    def trust_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust"], jsii.get(self, "trustInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames",
    jsii_struct_bases=[],
    name_mapping={"match": "match"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames:
    def __init__(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        if isinstance(match, dict):
            match = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch(**match)
        if __debug__:
            def stub(
                *,
                match: typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[str, typing.Any] = {
            "match": match,
        }

    @builtins.property
    def match(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch:
    def __init__(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        if __debug__:
            def stub(*, exact: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
        self._values: typing.Dict[str, typing.Any] = {
            "exact": exact,
        }

    @builtins.property
    def exact(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.'''
        result = self._values.get("exact")
        assert result is not None, "Required property 'exact' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
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
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
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

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch(
            exact=exact
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust",
    jsii_struct_bases=[],
    name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust:
    def __init__(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm", typing.Dict[str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile", typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(acm, dict):
            acm = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm(**acm)
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds(**sds)
        if __debug__:
            def stub(
                *,
                acm: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm, typing.Dict[str, typing.Any]]] = None,
                file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile, typing.Dict[str, typing.Any]]] = None,
                sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument acm", value=acm, expected_type=type_hints["acm"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if acm is not None:
            self._values["acm"] = acm
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def acm(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm"]:
        '''acm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        '''
        result = self._values.get("acm")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm"], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm",
    jsii_struct_bases=[],
    name_mapping={"certificate_authority_arns": "certificateAuthorityArns"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm:
    def __init__(
        self,
        *,
        certificate_authority_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.
        '''
        if __debug__:
            def stub(
                *,
                certificate_authority_arns: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_authority_arns", value=certificate_authority_arns, expected_type=type_hints["certificate_authority_arns"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_authority_arns": certificate_authority_arns,
        }

    @builtins.property
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.'''
        result = self._values.get("certificate_authority_arns")
        assert result is not None, "Required property 'certificate_authority_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference",
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
    @jsii.member(jsii_name="certificateAuthorityArnsInput")
    def certificate_authority_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateAuthorityArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificateAuthorityArns"))

    @certificate_authority_arns.setter
    def certificate_authority_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile",
    jsii_struct_bases=[],
    name_mapping={"certificate_chain": "certificateChain"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile:
    def __init__(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        if __debug__:
            def stub(*, certificate_chain: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_chain": certificate_chain,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference",
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
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference",
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

    @jsii.member(jsii_name="putAcm")
    def put_acm(
        self,
        *,
        certificate_authority_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm(
            certificate_authority_arns=certificate_authority_arns
        )

        return typing.cast(None, jsii.invoke(self, "putAcm", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile(
            certificate_chain=certificate_chain
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetAcm")
    def reset_acm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcm", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="acm")
    def acm(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference, jsii.get(self, "acm"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="acmInput")
    def acm_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm], jsii.get(self, "acmInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            def stub(*, secret_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference",
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
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference",
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

    @jsii.member(jsii_name="putClientPolicy")
    def put_client_policy(
        self,
        *,
        tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy(tls=tls)

        return typing.cast(None, jsii.invoke(self, "putClientPolicy", [value]))

    @jsii.member(jsii_name="resetClientPolicy")
    def reset_client_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="clientPolicy")
    def client_policy(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference, jsii.get(self, "clientPolicy"))

    @builtins.property
    @jsii.member(jsii_name="clientPolicyInput")
    def client_policy_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy], jsii.get(self, "clientPolicyInput"))

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
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualService]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualService],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualService],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListener",
    jsii_struct_bases=[],
    name_mapping={
        "port_mapping": "portMapping",
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "outlier_detection": "outlierDetection",
        "timeout": "timeout",
        "tls": "tls",
    },
)
class AppmeshVirtualNodeSpecListener:
    def __init__(
        self,
        *,
        port_mapping: typing.Union["AppmeshVirtualNodeSpecListenerPortMapping", typing.Dict[str, typing.Any]],
        connection_pool: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPool", typing.Dict[str, typing.Any]]] = None,
        health_check: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerHealthCheck", typing.Dict[str, typing.Any]]] = None,
        outlier_detection: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerOutlierDetection", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeout", typing.Dict[str, typing.Any]]] = None,
        tls: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTls", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param port_mapping: port_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port_mapping AppmeshVirtualNode#port_mapping}
        :param connection_pool: connection_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#connection_pool AppmeshVirtualNode#connection_pool}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#health_check AppmeshVirtualNode#health_check}
        :param outlier_detection: outlier_detection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#outlier_detection AppmeshVirtualNode#outlier_detection}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout AppmeshVirtualNode#timeout}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        if isinstance(port_mapping, dict):
            port_mapping = AppmeshVirtualNodeSpecListenerPortMapping(**port_mapping)
        if isinstance(connection_pool, dict):
            connection_pool = AppmeshVirtualNodeSpecListenerConnectionPool(**connection_pool)
        if isinstance(health_check, dict):
            health_check = AppmeshVirtualNodeSpecListenerHealthCheck(**health_check)
        if isinstance(outlier_detection, dict):
            outlier_detection = AppmeshVirtualNodeSpecListenerOutlierDetection(**outlier_detection)
        if isinstance(timeout, dict):
            timeout = AppmeshVirtualNodeSpecListenerTimeout(**timeout)
        if isinstance(tls, dict):
            tls = AppmeshVirtualNodeSpecListenerTls(**tls)
        if __debug__:
            def stub(
                *,
                port_mapping: typing.Union[AppmeshVirtualNodeSpecListenerPortMapping, typing.Dict[str, typing.Any]],
                connection_pool: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPool, typing.Dict[str, typing.Any]]] = None,
                health_check: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerHealthCheck, typing.Dict[str, typing.Any]]] = None,
                outlier_detection: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetection, typing.Dict[str, typing.Any]]] = None,
                timeout: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeout, typing.Dict[str, typing.Any]]] = None,
                tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTls, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument port_mapping", value=port_mapping, expected_type=type_hints["port_mapping"])
            check_type(argname="argument connection_pool", value=connection_pool, expected_type=type_hints["connection_pool"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument outlier_detection", value=outlier_detection, expected_type=type_hints["outlier_detection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[str, typing.Any] = {
            "port_mapping": port_mapping,
        }
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if timeout is not None:
            self._values["timeout"] = timeout
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def port_mapping(self) -> "AppmeshVirtualNodeSpecListenerPortMapping":
        '''port_mapping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port_mapping AppmeshVirtualNode#port_mapping}
        '''
        result = self._values.get("port_mapping")
        assert result is not None, "Required property 'port_mapping' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerPortMapping", result)

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPool"]:
        '''connection_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#connection_pool AppmeshVirtualNode#connection_pool}
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPool"], result)

    @builtins.property
    def health_check(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#health_check AppmeshVirtualNode#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerHealthCheck"], result)

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerOutlierDetection"]:
        '''outlier_detection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#outlier_detection AppmeshVirtualNode#outlier_detection}
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerOutlierDetection"], result)

    @builtins.property
    def timeout(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout AppmeshVirtualNode#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeout"], result)

    @builtins.property
    def tls(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"grpc": "grpc", "http": "http", "http2": "http2", "tcp": "tcp"},
)
class AppmeshVirtualNodeSpecListenerConnectionPool:
    def __init__(
        self,
        *,
        grpc: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPoolGrpc", typing.Dict[str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPoolHttp", typing.Dict[str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPoolHttp2", typing.Dict[str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPoolTcp", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        if isinstance(grpc, dict):
            grpc = AppmeshVirtualNodeSpecListenerConnectionPoolGrpc(**grpc)
        if isinstance(http, dict):
            http = AppmeshVirtualNodeSpecListenerConnectionPoolHttp(**http)
        if isinstance(http2, dict):
            http2 = AppmeshVirtualNodeSpecListenerConnectionPoolHttp2(**http2)
        if isinstance(tcp, dict):
            tcp = AppmeshVirtualNodeSpecListenerConnectionPoolTcp(**tcp)
        if __debug__:
            def stub(
                *,
                grpc: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc, typing.Dict[str, typing.Any]]] = None,
                http: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolHttp, typing.Dict[str, typing.Any]]] = None,
                http2: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2, typing.Dict[str, typing.Any]]] = None,
                tcp: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolTcp, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grpc", value=grpc, expected_type=type_hints["grpc"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument http2", value=http2, expected_type=type_hints["http2"])
            check_type(argname="argument tcp", value=tcp, expected_type=type_hints["tcp"])
        self._values: typing.Dict[str, typing.Any] = {}
        if grpc is not None:
            self._values["grpc"] = grpc
        if http is not None:
            self._values["http"] = http
        if http2 is not None:
            self._values["http2"] = http2
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def grpc(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolGrpc"]:
        '''grpc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        '''
        result = self._values.get("grpc")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolGrpc"], result)

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolHttp"]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolHttp"], result)

    @builtins.property
    def http2(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolHttp2"]:
        '''http2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        '''
        result = self._values.get("http2")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolHttp2"], result)

    @builtins.property
    def tcp(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolTcp"]:
        '''tcp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolTcp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolGrpc",
    jsii_struct_bases=[],
    name_mapping={"max_requests": "maxRequests"},
)
class AppmeshVirtualNodeSpecListenerConnectionPoolGrpc:
    def __init__(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.
        '''
        if __debug__:
            def stub(*, max_requests: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_requests", value=max_requests, expected_type=type_hints["max_requests"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_requests": max_requests,
        }

    @builtins.property
    def max_requests(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.'''
        result = self._values.get("max_requests")
        assert result is not None, "Required property 'max_requests' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPoolGrpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference",
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
    @jsii.member(jsii_name="maxRequestsInput")
    def max_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRequests")
    def max_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequests"))

    @max_requests.setter
    def max_requests(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "max_connections": "maxConnections",
        "max_pending_requests": "maxPendingRequests",
    },
)
class AppmeshVirtualNodeSpecListenerConnectionPoolHttp:
    def __init__(
        self,
        *,
        max_connections: jsii.Number,
        max_pending_requests: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.
        :param max_pending_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_pending_requests AppmeshVirtualNode#max_pending_requests}.
        '''
        if __debug__:
            def stub(
                *,
                max_connections: jsii.Number,
                max_pending_requests: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_connections", value=max_connections, expected_type=type_hints["max_connections"])
            check_type(argname="argument max_pending_requests", value=max_pending_requests, expected_type=type_hints["max_pending_requests"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_connections": max_connections,
        }
        if max_pending_requests is not None:
            self._values["max_pending_requests"] = max_pending_requests

    @builtins.property
    def max_connections(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.'''
        result = self._values.get("max_connections")
        assert result is not None, "Required property 'max_connections' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_pending_requests(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_pending_requests AppmeshVirtualNode#max_pending_requests}.'''
        result = self._values.get("max_pending_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolHttp2",
    jsii_struct_bases=[],
    name_mapping={"max_requests": "maxRequests"},
)
class AppmeshVirtualNodeSpecListenerConnectionPoolHttp2:
    def __init__(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.
        '''
        if __debug__:
            def stub(*, max_requests: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_requests", value=max_requests, expected_type=type_hints["max_requests"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_requests": max_requests,
        }

    @builtins.property
    def max_requests(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.'''
        result = self._values.get("max_requests")
        assert result is not None, "Required property 'max_requests' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPoolHttp2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference",
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
    @jsii.member(jsii_name="maxRequestsInput")
    def max_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRequests")
    def max_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequests"))

    @max_requests.setter
    def max_requests(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference",
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

    @jsii.member(jsii_name="resetMaxPendingRequests")
    def reset_max_pending_requests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPendingRequests", []))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsInput")
    def max_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPendingRequestsInput")
    def max_pending_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPendingRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnections"))

    @max_connections.setter
    def max_connections(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxPendingRequests")
    def max_pending_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPendingRequests"))

    @max_pending_requests.setter
    def max_pending_requests(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPendingRequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference",
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

    @jsii.member(jsii_name="putGrpc")
    def put_grpc(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPoolGrpc(
            max_requests=max_requests
        )

        return typing.cast(None, jsii.invoke(self, "putGrpc", [value]))

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        max_connections: jsii.Number,
        max_pending_requests: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.
        :param max_pending_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_pending_requests AppmeshVirtualNode#max_pending_requests}.
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPoolHttp(
            max_connections=max_connections, max_pending_requests=max_pending_requests
        )

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="putHttp2")
    def put_http2(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPoolHttp2(
            max_requests=max_requests
        )

        return typing.cast(None, jsii.invoke(self, "putHttp2", [value]))

    @jsii.member(jsii_name="putTcp")
    def put_tcp(self, *, max_connections: jsii.Number) -> None:
        '''
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPoolTcp(
            max_connections=max_connections
        )

        return typing.cast(None, jsii.invoke(self, "putTcp", [value]))

    @jsii.member(jsii_name="resetGrpc")
    def reset_grpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpc", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @jsii.member(jsii_name="resetHttp2")
    def reset_http2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2", []))

    @jsii.member(jsii_name="resetTcp")
    def reset_tcp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcp", []))

    @builtins.property
    @jsii.member(jsii_name="grpc")
    def grpc(self) -> AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference, jsii.get(self, "grpc"))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="http2")
    def http2(self) -> AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference, jsii.get(self, "http2"))

    @builtins.property
    @jsii.member(jsii_name="tcp")
    def tcp(self) -> "AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference", jsii.get(self, "tcp"))

    @builtins.property
    @jsii.member(jsii_name="grpcInput")
    def grpc_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc], jsii.get(self, "grpcInput"))

    @builtins.property
    @jsii.member(jsii_name="http2Input")
    def http2_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2], jsii.get(self, "http2Input"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpInput")
    def tcp_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolTcp"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolTcp"], jsii.get(self, "tcpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={"max_connections": "maxConnections"},
)
class AppmeshVirtualNodeSpecListenerConnectionPoolTcp:
    def __init__(self, *, max_connections: jsii.Number) -> None:
        '''
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.
        '''
        if __debug__:
            def stub(*, max_connections: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_connections", value=max_connections, expected_type=type_hints["max_connections"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_connections": max_connections,
        }

    @builtins.property
    def max_connections(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.'''
        result = self._values.get("max_connections")
        assert result is not None, "Required property 'max_connections' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference",
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
    @jsii.member(jsii_name="maxConnectionsInput")
    def max_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnections"))

    @max_connections.setter
    def max_connections(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnections", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolTcp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolTcp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolTcp],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolTcp],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "healthy_threshold": "healthyThreshold",
        "interval_millis": "intervalMillis",
        "protocol": "protocol",
        "timeout_millis": "timeoutMillis",
        "unhealthy_threshold": "unhealthyThreshold",
        "path": "path",
        "port": "port",
    },
)
class AppmeshVirtualNodeSpecListenerHealthCheck:
    def __init__(
        self,
        *,
        healthy_threshold: jsii.Number,
        interval_millis: jsii.Number,
        protocol: builtins.str,
        timeout_millis: jsii.Number,
        unhealthy_threshold: jsii.Number,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#healthy_threshold AppmeshVirtualNode#healthy_threshold}.
        :param interval_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval_millis AppmeshVirtualNode#interval_millis}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.
        :param timeout_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout_millis AppmeshVirtualNode#timeout_millis}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unhealthy_threshold AppmeshVirtualNode#unhealthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.
        '''
        if __debug__:
            def stub(
                *,
                healthy_threshold: jsii.Number,
                interval_millis: jsii.Number,
                protocol: builtins.str,
                timeout_millis: jsii.Number,
                unhealthy_threshold: jsii.Number,
                path: typing.Optional[builtins.str] = None,
                port: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
            check_type(argname="argument interval_millis", value=interval_millis, expected_type=type_hints["interval_millis"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument timeout_millis", value=timeout_millis, expected_type=type_hints["timeout_millis"])
            check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "healthy_threshold": healthy_threshold,
            "interval_millis": interval_millis,
            "protocol": protocol,
            "timeout_millis": timeout_millis,
            "unhealthy_threshold": unhealthy_threshold,
        }
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def healthy_threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#healthy_threshold AppmeshVirtualNode#healthy_threshold}.'''
        result = self._values.get("healthy_threshold")
        assert result is not None, "Required property 'healthy_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval_millis(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval_millis AppmeshVirtualNode#interval_millis}.'''
        result = self._values.get("interval_millis")
        assert result is not None, "Required property 'interval_millis' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_millis(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout_millis AppmeshVirtualNode#timeout_millis}.'''
        result = self._values.get("timeout_millis")
        assert result is not None, "Required property 'timeout_millis' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unhealthy_threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unhealthy_threshold AppmeshVirtualNode#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        assert result is not None, "Required property 'unhealthy_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerHealthCheckOutputReference",
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

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalMillisInput")
    def interval_millis_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalMillisInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutMillisInput")
    def timeout_millis_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutMillisInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="intervalMillis")
    def interval_millis(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalMillis"))

    @interval_millis.setter
    def interval_millis(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalMillis", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutMillis")
    def timeout_millis(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutMillis"))

    @timeout_millis.setter
    def timeout_millis(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutMillis", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_duration": "baseEjectionDuration",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "max_server_errors": "maxServerErrors",
    },
)
class AppmeshVirtualNodeSpecListenerOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_duration: typing.Union["AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration", typing.Dict[str, typing.Any]],
        interval: typing.Union["AppmeshVirtualNodeSpecListenerOutlierDetectionInterval", typing.Dict[str, typing.Any]],
        max_ejection_percent: jsii.Number,
        max_server_errors: jsii.Number,
    ) -> None:
        '''
        :param base_ejection_duration: base_ejection_duration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#base_ejection_duration AppmeshVirtualNode#base_ejection_duration}
        :param interval: interval block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval AppmeshVirtualNode#interval}
        :param max_ejection_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_ejection_percent AppmeshVirtualNode#max_ejection_percent}.
        :param max_server_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_server_errors AppmeshVirtualNode#max_server_errors}.
        '''
        if isinstance(base_ejection_duration, dict):
            base_ejection_duration = AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration(**base_ejection_duration)
        if isinstance(interval, dict):
            interval = AppmeshVirtualNodeSpecListenerOutlierDetectionInterval(**interval)
        if __debug__:
            def stub(
                *,
                base_ejection_duration: typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration, typing.Dict[str, typing.Any]],
                interval: typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval, typing.Dict[str, typing.Any]],
                max_ejection_percent: jsii.Number,
                max_server_errors: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument base_ejection_duration", value=base_ejection_duration, expected_type=type_hints["base_ejection_duration"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument max_ejection_percent", value=max_ejection_percent, expected_type=type_hints["max_ejection_percent"])
            check_type(argname="argument max_server_errors", value=max_server_errors, expected_type=type_hints["max_server_errors"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_ejection_duration": base_ejection_duration,
            "interval": interval,
            "max_ejection_percent": max_ejection_percent,
            "max_server_errors": max_server_errors,
        }

    @builtins.property
    def base_ejection_duration(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration":
        '''base_ejection_duration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#base_ejection_duration AppmeshVirtualNode#base_ejection_duration}
        '''
        result = self._values.get("base_ejection_duration")
        assert result is not None, "Required property 'base_ejection_duration' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration", result)

    @builtins.property
    def interval(self) -> "AppmeshVirtualNodeSpecListenerOutlierDetectionInterval":
        '''interval block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval AppmeshVirtualNode#interval}
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerOutlierDetectionInterval", result)

    @builtins.property
    def max_ejection_percent(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_ejection_percent AppmeshVirtualNode#max_ejection_percent}.'''
        result = self._values.get("max_ejection_percent")
        assert result is not None, "Required property 'max_ejection_percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_server_errors(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_server_errors AppmeshVirtualNode#max_server_errors}.'''
        result = self._values.get("max_server_errors")
        assert result is not None, "Required property 'max_server_errors' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            def stub(*, unit: builtins.str, value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference",
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
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionInterval",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerOutlierDetectionInterval:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            def stub(*, unit: builtins.str, value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerOutlierDetectionInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference",
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
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference",
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

    @jsii.member(jsii_name="putBaseEjectionDuration")
    def put_base_ejection_duration(
        self,
        *,
        unit: builtins.str,
        value: jsii.Number,
    ) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putBaseEjectionDuration", [value_]))

    @jsii.member(jsii_name="putInterval")
    def put_interval(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerOutlierDetectionInterval(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putInterval", [value_]))

    @builtins.property
    @jsii.member(jsii_name="baseEjectionDuration")
    def base_ejection_duration(
        self,
    ) -> AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference, jsii.get(self, "baseEjectionDuration"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(
        self,
    ) -> AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference, jsii.get(self, "interval"))

    @builtins.property
    @jsii.member(jsii_name="baseEjectionDurationInput")
    def base_ejection_duration_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration], jsii.get(self, "baseEjectionDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="maxEjectionPercentInput")
    def max_ejection_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxEjectionPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxServerErrorsInput")
    def max_server_errors_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxServerErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxEjectionPercent")
    def max_ejection_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxEjectionPercent"))

    @max_ejection_percent.setter
    def max_ejection_percent(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxEjectionPercent", value)

    @builtins.property
    @jsii.member(jsii_name="maxServerErrors")
    def max_server_errors(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxServerErrors"))

    @max_server_errors.setter
    def max_server_errors(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxServerErrors", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutputReference",
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

    @jsii.member(jsii_name="putConnectionPool")
    def put_connection_pool(
        self,
        *,
        grpc: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc, typing.Dict[str, typing.Any]]] = None,
        http: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolHttp, typing.Dict[str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2, typing.Dict[str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolTcp, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPool(
            grpc=grpc, http=http, http2=http2, tcp=tcp
        )

        return typing.cast(None, jsii.invoke(self, "putConnectionPool", [value]))

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        healthy_threshold: jsii.Number,
        interval_millis: jsii.Number,
        protocol: builtins.str,
        timeout_millis: jsii.Number,
        unhealthy_threshold: jsii.Number,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#healthy_threshold AppmeshVirtualNode#healthy_threshold}.
        :param interval_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval_millis AppmeshVirtualNode#interval_millis}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.
        :param timeout_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout_millis AppmeshVirtualNode#timeout_millis}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unhealthy_threshold AppmeshVirtualNode#unhealthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.
        '''
        value = AppmeshVirtualNodeSpecListenerHealthCheck(
            healthy_threshold=healthy_threshold,
            interval_millis=interval_millis,
            protocol=protocol,
            timeout_millis=timeout_millis,
            unhealthy_threshold=unhealthy_threshold,
            path=path,
            port=port,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="putOutlierDetection")
    def put_outlier_detection(
        self,
        *,
        base_ejection_duration: typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration, typing.Dict[str, typing.Any]],
        interval: typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval, typing.Dict[str, typing.Any]],
        max_ejection_percent: jsii.Number,
        max_server_errors: jsii.Number,
    ) -> None:
        '''
        :param base_ejection_duration: base_ejection_duration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#base_ejection_duration AppmeshVirtualNode#base_ejection_duration}
        :param interval: interval block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval AppmeshVirtualNode#interval}
        :param max_ejection_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_ejection_percent AppmeshVirtualNode#max_ejection_percent}.
        :param max_server_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_server_errors AppmeshVirtualNode#max_server_errors}.
        '''
        value = AppmeshVirtualNodeSpecListenerOutlierDetection(
            base_ejection_duration=base_ejection_duration,
            interval=interval,
            max_ejection_percent=max_ejection_percent,
            max_server_errors=max_server_errors,
        )

        return typing.cast(None, jsii.invoke(self, "putOutlierDetection", [value]))

    @jsii.member(jsii_name="putPortMapping")
    def put_port_mapping(self, *, port: jsii.Number, protocol: builtins.str) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.
        '''
        value = AppmeshVirtualNodeSpecListenerPortMapping(port=port, protocol=protocol)

        return typing.cast(None, jsii.invoke(self, "putPortMapping", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        grpc: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutGrpc", typing.Dict[str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp", typing.Dict[str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp2", typing.Dict[str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutTcp", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeout(
            grpc=grpc, http=http, http2=http2, tcp=tcp
        )

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        certificate: typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificate", typing.Dict[str, typing.Any]],
        mode: builtins.str,
        validation: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mode AppmeshVirtualNode#mode}.
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        value = AppmeshVirtualNodeSpecListenerTls(
            certificate=certificate, mode=mode, validation=validation
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetConnectionPool")
    def reset_connection_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionPool", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetOutlierDetection")
    def reset_outlier_detection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutlierDetection", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="connectionPool")
    def connection_pool(
        self,
    ) -> AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference, jsii.get(self, "connectionPool"))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> AppmeshVirtualNodeSpecListenerHealthCheckOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerHealthCheckOutputReference, jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="outlierDetection")
    def outlier_detection(
        self,
    ) -> AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference, jsii.get(self, "outlierDetection"))

    @builtins.property
    @jsii.member(jsii_name="portMapping")
    def port_mapping(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerPortMappingOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerPortMappingOutputReference", jsii.get(self, "portMapping"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> "AppmeshVirtualNodeSpecListenerTimeoutOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "AppmeshVirtualNodeSpecListenerTlsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="connectionPoolInput")
    def connection_pool_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool], jsii.get(self, "connectionPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="outlierDetectionInput")
    def outlier_detection_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection], jsii.get(self, "outlierDetectionInput"))

    @builtins.property
    @jsii.member(jsii_name="portMappingInput")
    def port_mapping_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerPortMapping"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerPortMapping"], jsii.get(self, "portMappingInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeout"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTls"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecListener]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListener], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListener],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppmeshVirtualNodeSpecListener]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerPortMapping",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "protocol": "protocol"},
)
class AppmeshVirtualNodeSpecListenerPortMapping:
    def __init__(self, *, port: jsii.Number, protocol: builtins.str) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.
        '''
        if __debug__:
            def stub(*, port: jsii.Number, protocol: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
            "protocol": protocol,
        }

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerPortMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerPortMappingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerPortMappingOutputReference",
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
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerPortMapping]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerPortMapping], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerPortMapping],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerPortMapping],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeout",
    jsii_struct_bases=[],
    name_mapping={"grpc": "grpc", "http": "http", "http2": "http2", "tcp": "tcp"},
)
class AppmeshVirtualNodeSpecListenerTimeout:
    def __init__(
        self,
        *,
        grpc: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutGrpc", typing.Dict[str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp", typing.Dict[str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp2", typing.Dict[str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutTcp", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        if isinstance(grpc, dict):
            grpc = AppmeshVirtualNodeSpecListenerTimeoutGrpc(**grpc)
        if isinstance(http, dict):
            http = AppmeshVirtualNodeSpecListenerTimeoutHttp(**http)
        if isinstance(http2, dict):
            http2 = AppmeshVirtualNodeSpecListenerTimeoutHttp2(**http2)
        if isinstance(tcp, dict):
            tcp = AppmeshVirtualNodeSpecListenerTimeoutTcp(**tcp)
        if __debug__:
            def stub(
                *,
                grpc: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpc, typing.Dict[str, typing.Any]]] = None,
                http: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp, typing.Dict[str, typing.Any]]] = None,
                http2: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2, typing.Dict[str, typing.Any]]] = None,
                tcp: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutTcp, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grpc", value=grpc, expected_type=type_hints["grpc"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument http2", value=http2, expected_type=type_hints["http2"])
            check_type(argname="argument tcp", value=tcp, expected_type=type_hints["tcp"])
        self._values: typing.Dict[str, typing.Any] = {}
        if grpc is not None:
            self._values["grpc"] = grpc
        if http is not None:
            self._values["http"] = http
        if http2 is not None:
            self._values["http2"] = http2
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def grpc(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpc"]:
        '''grpc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        '''
        result = self._values.get("grpc")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpc"], result)

    @builtins.property
    def http(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp"]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp"], result)

    @builtins.property
    def http2(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2"]:
        '''http2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        '''
        result = self._values.get("http2")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2"], result)

    @builtins.property
    def tcp(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcp"]:
        '''tcp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpc",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class AppmeshVirtualNodeSpecListenerTimeoutGrpc:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle", typing.Dict[str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        if isinstance(idle, dict):
            idle = AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle(**idle)
        if isinstance(per_request, dict):
            per_request = AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest(**per_request)
        if __debug__:
            def stub(
                *,
                idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle, typing.Dict[str, typing.Any]]] = None,
                per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
            check_type(argname="argument per_request", value=per_request, expected_type=type_hints["per_request"])
        self._values: typing.Dict[str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle"], result)

    @builtins.property
    def per_request(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest"]:
        '''per_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutGrpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            def stub(*, unit: builtins.str, value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference",
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
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference",
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

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="putPerRequest")
    def put_per_request(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPerRequest", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @jsii.member(jsii_name="resetPerRequest")
    def reset_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="perRequest")
    def per_request(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference", jsii.get(self, "perRequest"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestInput")
    def per_request_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest"], jsii.get(self, "perRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            def stub(*, unit: builtins.str, value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference",
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
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttp:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttpIdle", typing.Dict[str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        if isinstance(idle, dict):
            idle = AppmeshVirtualNodeSpecListenerTimeoutHttpIdle(**idle)
        if isinstance(per_request, dict):
            per_request = AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest(**per_request)
        if __debug__:
            def stub(
                *,
                idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle, typing.Dict[str, typing.Any]]] = None,
                per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
            check_type(argname="argument per_request", value=per_request, expected_type=type_hints["per_request"])
        self._values: typing.Dict[str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpIdle"], result)

    @builtins.property
    def per_request(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest"]:
        '''per_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttp2:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle", typing.Dict[str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        if isinstance(idle, dict):
            idle = AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle(**idle)
        if isinstance(per_request, dict):
            per_request = AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest(**per_request)
        if __debug__:
            def stub(
                *,
                idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle, typing.Dict[str, typing.Any]]] = None,
                per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
            check_type(argname="argument per_request", value=per_request, expected_type=type_hints["per_request"])
        self._values: typing.Dict[str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle"], result)

    @builtins.property
    def per_request(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest"]:
        '''per_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttp2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            def stub(*, unit: builtins.str, value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference",
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
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference",
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

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="putPerRequest")
    def put_per_request(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPerRequest", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @jsii.member(jsii_name="resetPerRequest")
    def reset_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="perRequest")
    def per_request(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference", jsii.get(self, "perRequest"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestInput")
    def per_request_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest"], jsii.get(self, "perRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            def stub(*, unit: builtins.str, value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference",
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
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttpIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            def stub(*, unit: builtins.str, value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttpIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference",
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
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference",
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

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutHttpIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="putPerRequest")
    def put_per_request(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPerRequest", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @jsii.member(jsii_name="resetPerRequest")
    def reset_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="perRequest")
    def per_request(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference", jsii.get(self, "perRequest"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestInput")
    def per_request_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest"], jsii.get(self, "perRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            def stub(*, unit: builtins.str, value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference",
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
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutOutputReference",
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

    @jsii.member(jsii_name="putGrpc")
    def put_grpc(
        self,
        *,
        idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle, typing.Dict[str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeoutGrpc(
            idle=idle, per_request=per_request
        )

        return typing.cast(None, jsii.invoke(self, "putGrpc", [value]))

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle, typing.Dict[str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeoutHttp(
            idle=idle, per_request=per_request
        )

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="putHttp2")
    def put_http2(
        self,
        *,
        idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle, typing.Dict[str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeoutHttp2(
            idle=idle, per_request=per_request
        )

        return typing.cast(None, jsii.invoke(self, "putHttp2", [value]))

    @jsii.member(jsii_name="putTcp")
    def put_tcp(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutTcpIdle", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeoutTcp(idle=idle)

        return typing.cast(None, jsii.invoke(self, "putTcp", [value]))

    @jsii.member(jsii_name="resetGrpc")
    def reset_grpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpc", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @jsii.member(jsii_name="resetHttp2")
    def reset_http2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2", []))

    @jsii.member(jsii_name="resetTcp")
    def reset_tcp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcp", []))

    @builtins.property
    @jsii.member(jsii_name="grpc")
    def grpc(self) -> AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference, jsii.get(self, "grpc"))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="http2")
    def http2(self) -> AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference, jsii.get(self, "http2"))

    @builtins.property
    @jsii.member(jsii_name="tcp")
    def tcp(self) -> "AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference", jsii.get(self, "tcp"))

    @builtins.property
    @jsii.member(jsii_name="grpcInput")
    def grpc_input(self) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc], jsii.get(self, "grpcInput"))

    @builtins.property
    @jsii.member(jsii_name="http2Input")
    def http2_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2], jsii.get(self, "http2Input"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(self) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpInput")
    def tcp_input(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcp"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcp"], jsii.get(self, "tcpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeout]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeout],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeout],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutTcp",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle"},
)
class AppmeshVirtualNodeSpecListenerTimeoutTcp:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutTcpIdle", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        if isinstance(idle, dict):
            idle = AppmeshVirtualNodeSpecListenerTimeoutTcpIdle(**idle)
        if __debug__:
            def stub(
                *,
                idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
        self._values: typing.Dict[str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcpIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcpIdle"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutTcpIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutTcpIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            def stub(*, unit: builtins.str, value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutTcpIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference",
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
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference",
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

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutTcpIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcp],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcp],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTls",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "mode": "mode",
        "validation": "validation",
    },
)
class AppmeshVirtualNodeSpecListenerTls:
    def __init__(
        self,
        *,
        certificate: typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificate", typing.Dict[str, typing.Any]],
        mode: builtins.str,
        validation: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mode AppmeshVirtualNode#mode}.
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        if isinstance(certificate, dict):
            certificate = AppmeshVirtualNodeSpecListenerTlsCertificate(**certificate)
        if isinstance(validation, dict):
            validation = AppmeshVirtualNodeSpecListenerTlsValidation(**validation)
        if __debug__:
            def stub(
                *,
                certificate: typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificate, typing.Dict[str, typing.Any]],
                mode: builtins.str,
                validation: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsValidation, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate": certificate,
            "mode": mode,
        }
        if validation is not None:
            self._values["validation"] = validation

    @builtins.property
    def certificate(self) -> "AppmeshVirtualNodeSpecListenerTlsCertificate":
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsCertificate", result)

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mode AppmeshVirtualNode#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validation(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidation"]:
        '''validation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        result = self._values.get("validation")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificate",
    jsii_struct_bases=[],
    name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecListenerTlsCertificate:
    def __init__(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificateAcm", typing.Dict[str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificateFile", typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificateSds", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(acm, dict):
            acm = AppmeshVirtualNodeSpecListenerTlsCertificateAcm(**acm)
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecListenerTlsCertificateFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecListenerTlsCertificateSds(**sds)
        if __debug__:
            def stub(
                *,
                acm: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateAcm, typing.Dict[str, typing.Any]]] = None,
                file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateFile, typing.Dict[str, typing.Any]]] = None,
                sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateSds, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument acm", value=acm, expected_type=type_hints["acm"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if acm is not None:
            self._values["acm"] = acm
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def acm(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateAcm"]:
        '''acm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        '''
        result = self._values.get("acm")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateAcm"], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateFile"], result)

    @builtins.property
    def sds(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateAcm",
    jsii_struct_bases=[],
    name_mapping={"certificate_arn": "certificateArn"},
)
class AppmeshVirtualNodeSpecListenerTlsCertificateAcm:
    def __init__(self, *, certificate_arn: builtins.str) -> None:
        '''
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_arn AppmeshVirtualNode#certificate_arn}.
        '''
        if __debug__:
            def stub(*, certificate_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_arn": certificate_arn,
        }

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_arn AppmeshVirtualNode#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsCertificateAcm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference",
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
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateFile",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_chain": "certificateChain",
        "private_key": "privateKey",
    },
)
class AppmeshVirtualNodeSpecListenerTlsCertificateFile:
    def __init__(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        if __debug__:
            def stub(
                *,
                certificate_chain: builtins.str,
                private_key: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_chain": certificate_chain,
            "private_key": private_key,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsCertificateFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference",
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
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference",
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

    @jsii.member(jsii_name="putAcm")
    def put_acm(self, *, certificate_arn: builtins.str) -> None:
        '''
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_arn AppmeshVirtualNode#certificate_arn}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsCertificateAcm(
            certificate_arn=certificate_arn
        )

        return typing.cast(None, jsii.invoke(self, "putAcm", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsCertificateFile(
            certificate_chain=certificate_chain, private_key=private_key
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsCertificateSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetAcm")
    def reset_acm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcm", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="acm")
    def acm(self) -> AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference, jsii.get(self, "acm"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(self) -> "AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="acmInput")
    def acm_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm], jsii.get(self, "acmInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecListenerTlsCertificateSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            def stub(*, secret_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsCertificateSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference",
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
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateSds],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateSds],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTlsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsOutputReference",
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

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        acm: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateAcm, typing.Dict[str, typing.Any]]] = None,
        file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateFile, typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateSds, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecListenerTlsCertificate(
            acm=acm, file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putValidation")
    def put_validation(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrust", typing.Dict[str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidation(
            trust=trust, subject_alternative_names=subject_alternative_names
        )

        return typing.cast(None, jsii.invoke(self, "putValidation", [value]))

    @jsii.member(jsii_name="resetValidation")
    def reset_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidation", []))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(
        self,
    ) -> AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationOutputReference", jsii.get(self, "validation"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="validationInput")
    def validation_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidation"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidation"], jsii.get(self, "validationInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecListenerTls]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTls],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppmeshVirtualNodeSpecListenerTls]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class AppmeshVirtualNodeSpecListenerTlsValidation:
    def __init__(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrust", typing.Dict[str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        if isinstance(trust, dict):
            trust = AppmeshVirtualNodeSpecListenerTlsValidationTrust(**trust)
        if isinstance(subject_alternative_names, dict):
            subject_alternative_names = AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames(**subject_alternative_names)
        if __debug__:
            def stub(
                *,
                trust: typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationTrust, typing.Dict[str, typing.Any]],
                subject_alternative_names: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument trust", value=trust, expected_type=type_hints["trust"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
        self._values: typing.Dict[str, typing.Any] = {
            "trust": trust,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def trust(self) -> "AppmeshVirtualNodeSpecListenerTlsValidationTrust":
        '''trust block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        '''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames"]:
        '''subject_alternative_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsValidationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationOutputReference",
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

    @jsii.member(jsii_name="putSubjectAlternativeNames")
    def put_subject_alternative_names(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames(
            match=match
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAlternativeNames", [value]))

    @jsii.member(jsii_name="putTrust")
    def put_trust(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrustFile", typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationTrust(file=file, sds=sds)

        return typing.cast(None, jsii.invoke(self, "putTrust", [value]))

    @jsii.member(jsii_name="resetSubjectAlternativeNames")
    def reset_subject_alternative_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectAlternativeNames", []))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference", jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="trust")
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference", jsii.get(self, "trust"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNamesInput")
    def subject_alternative_names_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames"], jsii.get(self, "subjectAlternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="trustInput")
    def trust_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrust"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrust"], jsii.get(self, "trustInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidation]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames",
    jsii_struct_bases=[],
    name_mapping={"match": "match"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames:
    def __init__(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        if isinstance(match, dict):
            match = AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch(**match)
        if __debug__:
            def stub(
                *,
                match: typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[str, typing.Any] = {
            "match": match,
        }

    @builtins.property
    def match(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch:
    def __init__(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        if __debug__:
            def stub(*, exact: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
        self._values: typing.Dict[str, typing.Any] = {
            "exact": exact,
        }

    @builtins.property
    def exact(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.'''
        result = self._values.get("exact")
        assert result is not None, "Required property 'exact' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference",
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
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference",
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

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch(
            exact=exact
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(
        self,
    ) -> AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrust",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationTrust:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrustFile", typing.Dict[str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecListenerTlsValidationTrustFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecListenerTlsValidationTrustSds(**sds)
        if __debug__:
            def stub(
                *,
                file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile, typing.Dict[str, typing.Any]]] = None,
                sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationTrust(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustFile",
    jsii_struct_bases=[],
    name_mapping={"certificate_chain": "certificateChain"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationTrustFile:
    def __init__(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        if __debug__:
            def stub(*, certificate_chain: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_chain": certificate_chain,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationTrustFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference",
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
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference",
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

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationTrustFile(
            certificate_chain=certificate_chain
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationTrustSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrust]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrust], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrust],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrust],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationTrustSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            def stub(*, secret_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationTrustSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference",
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
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLogging",
    jsii_struct_bases=[],
    name_mapping={"access_log": "accessLog"},
)
class AppmeshVirtualNodeSpecLogging:
    def __init__(
        self,
        *,
        access_log: typing.Optional[typing.Union["AppmeshVirtualNodeSpecLoggingAccessLog", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_log: access_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#access_log AppmeshVirtualNode#access_log}
        '''
        if isinstance(access_log, dict):
            access_log = AppmeshVirtualNodeSpecLoggingAccessLog(**access_log)
        if __debug__:
            def stub(
                *,
                access_log: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLoggingAccessLog, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument access_log", value=access_log, expected_type=type_hints["access_log"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_log is not None:
            self._values["access_log"] = access_log

    @builtins.property
    def access_log(self) -> typing.Optional["AppmeshVirtualNodeSpecLoggingAccessLog"]:
        '''access_log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#access_log AppmeshVirtualNode#access_log}
        '''
        result = self._values.get("access_log")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecLoggingAccessLog"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingAccessLog",
    jsii_struct_bases=[],
    name_mapping={"file": "file"},
)
class AppmeshVirtualNodeSpecLoggingAccessLog:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecLoggingAccessLogFile", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecLoggingAccessLogFile(**file)
        if __debug__:
            def stub(
                *,
                file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLoggingAccessLogFile, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
        self._values: typing.Dict[str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file

    @builtins.property
    def file(self) -> typing.Optional["AppmeshVirtualNodeSpecLoggingAccessLogFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecLoggingAccessLogFile"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecLoggingAccessLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingAccessLogFile",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class AppmeshVirtualNodeSpecLoggingAccessLogFile:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.
        '''
        if __debug__:
            def stub(*, path: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecLoggingAccessLogFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference",
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
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecLoggingAccessLogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingAccessLogOutputReference",
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

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.
        '''
        value = AppmeshVirtualNodeSpecLoggingAccessLogFile(path=path)

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecLoggingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingOutputReference",
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

    @jsii.member(jsii_name="putAccessLog")
    def put_access_log(
        self,
        *,
        file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLoggingAccessLogFile, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        value = AppmeshVirtualNodeSpecLoggingAccessLog(file=file)

        return typing.cast(None, jsii.invoke(self, "putAccessLog", [value]))

    @jsii.member(jsii_name="resetAccessLog")
    def reset_access_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLog", []))

    @builtins.property
    @jsii.member(jsii_name="accessLog")
    def access_log(self) -> AppmeshVirtualNodeSpecLoggingAccessLogOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecLoggingAccessLogOutputReference, jsii.get(self, "accessLog"))

    @builtins.property
    @jsii.member(jsii_name="accessLogInput")
    def access_log_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog], jsii.get(self, "accessLogInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecLogging]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecLogging],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppmeshVirtualNodeSpecLogging]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecOutputReference",
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

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppmeshVirtualNodeSpecBackend, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppmeshVirtualNodeSpecBackend, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @jsii.member(jsii_name="putBackendDefaults")
    def put_backend_defaults(
        self,
        *,
        client_policy: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaults(client_policy=client_policy)

        return typing.cast(None, jsii.invoke(self, "putBackendDefaults", [value]))

    @jsii.member(jsii_name="putListener")
    def put_listener(
        self,
        *,
        port_mapping: typing.Union[AppmeshVirtualNodeSpecListenerPortMapping, typing.Dict[str, typing.Any]],
        connection_pool: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPool, typing.Dict[str, typing.Any]]] = None,
        health_check: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerHealthCheck, typing.Dict[str, typing.Any]]] = None,
        outlier_detection: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeout, typing.Dict[str, typing.Any]]] = None,
        tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTls, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param port_mapping: port_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port_mapping AppmeshVirtualNode#port_mapping}
        :param connection_pool: connection_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#connection_pool AppmeshVirtualNode#connection_pool}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#health_check AppmeshVirtualNode#health_check}
        :param outlier_detection: outlier_detection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#outlier_detection AppmeshVirtualNode#outlier_detection}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout AppmeshVirtualNode#timeout}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        value = AppmeshVirtualNodeSpecListener(
            port_mapping=port_mapping,
            connection_pool=connection_pool,
            health_check=health_check,
            outlier_detection=outlier_detection,
            timeout=timeout,
            tls=tls,
        )

        return typing.cast(None, jsii.invoke(self, "putListener", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        access_log: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLoggingAccessLog, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_log: access_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#access_log AppmeshVirtualNode#access_log}
        '''
        value = AppmeshVirtualNodeSpecLogging(access_log=access_log)

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putServiceDiscovery")
    def put_service_discovery(
        self,
        *,
        aws_cloud_map: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap", typing.Dict[str, typing.Any]]] = None,
        dns: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscoveryDns", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_cloud_map: aws_cloud_map block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#aws_cloud_map AppmeshVirtualNode#aws_cloud_map}
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#dns AppmeshVirtualNode#dns}
        '''
        value = AppmeshVirtualNodeSpecServiceDiscovery(
            aws_cloud_map=aws_cloud_map, dns=dns
        )

        return typing.cast(None, jsii.invoke(self, "putServiceDiscovery", [value]))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetBackendDefaults")
    def reset_backend_defaults(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendDefaults", []))

    @jsii.member(jsii_name="resetListener")
    def reset_listener(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListener", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetServiceDiscovery")
    def reset_service_discovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceDiscovery", []))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> AppmeshVirtualNodeSpecBackendList:
        return typing.cast(AppmeshVirtualNodeSpecBackendList, jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="backendDefaults")
    def backend_defaults(self) -> AppmeshVirtualNodeSpecBackendDefaultsOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsOutputReference, jsii.get(self, "backendDefaults"))

    @builtins.property
    @jsii.member(jsii_name="listener")
    def listener(self) -> AppmeshVirtualNodeSpecListenerOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerOutputReference, jsii.get(self, "listener"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> AppmeshVirtualNodeSpecLoggingOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecLoggingOutputReference, jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="serviceDiscovery")
    def service_discovery(
        self,
    ) -> "AppmeshVirtualNodeSpecServiceDiscoveryOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecServiceDiscoveryOutputReference", jsii.get(self, "serviceDiscovery"))

    @builtins.property
    @jsii.member(jsii_name="backendDefaultsInput")
    def backend_defaults_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaults]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaults], jsii.get(self, "backendDefaultsInput"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerInput")
    def listener_input(self) -> typing.Optional[AppmeshVirtualNodeSpecListener]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListener], jsii.get(self, "listenerInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional[AppmeshVirtualNodeSpecLogging]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLogging], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceDiscoveryInput")
    def service_discovery_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecServiceDiscovery"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecServiceDiscovery"], jsii.get(self, "serviceDiscoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpec]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshVirtualNodeSpec]) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppmeshVirtualNodeSpec]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscovery",
    jsii_struct_bases=[],
    name_mapping={"aws_cloud_map": "awsCloudMap", "dns": "dns"},
)
class AppmeshVirtualNodeSpecServiceDiscovery:
    def __init__(
        self,
        *,
        aws_cloud_map: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap", typing.Dict[str, typing.Any]]] = None,
        dns: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscoveryDns", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_cloud_map: aws_cloud_map block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#aws_cloud_map AppmeshVirtualNode#aws_cloud_map}
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#dns AppmeshVirtualNode#dns}
        '''
        if isinstance(aws_cloud_map, dict):
            aws_cloud_map = AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap(**aws_cloud_map)
        if isinstance(dns, dict):
            dns = AppmeshVirtualNodeSpecServiceDiscoveryDns(**dns)
        if __debug__:
            def stub(
                *,
                aws_cloud_map: typing.Optional[typing.Union[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap, typing.Dict[str, typing.Any]]] = None,
                dns: typing.Optional[typing.Union[AppmeshVirtualNodeSpecServiceDiscoveryDns, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument aws_cloud_map", value=aws_cloud_map, expected_type=type_hints["aws_cloud_map"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_cloud_map is not None:
            self._values["aws_cloud_map"] = aws_cloud_map
        if dns is not None:
            self._values["dns"] = dns

    @builtins.property
    def aws_cloud_map(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap"]:
        '''aws_cloud_map block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#aws_cloud_map AppmeshVirtualNode#aws_cloud_map}
        '''
        result = self._values.get("aws_cloud_map")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap"], result)

    @builtins.property
    def dns(self) -> typing.Optional["AppmeshVirtualNodeSpecServiceDiscoveryDns"]:
        '''dns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#dns AppmeshVirtualNode#dns}
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecServiceDiscoveryDns"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecServiceDiscovery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap",
    jsii_struct_bases=[],
    name_mapping={
        "namespace_name": "namespaceName",
        "service_name": "serviceName",
        "attributes": "attributes",
    },
)
class AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap:
    def __init__(
        self,
        *,
        namespace_name: builtins.str,
        service_name: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param namespace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#namespace_name AppmeshVirtualNode#namespace_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_name AppmeshVirtualNode#service_name}.
        :param attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#attributes AppmeshVirtualNode#attributes}.
        '''
        if __debug__:
            def stub(
                *,
                namespace_name: builtins.str,
                service_name: builtins.str,
                attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        self._values: typing.Dict[str, typing.Any] = {
            "namespace_name": namespace_name,
            "service_name": service_name,
        }
        if attributes is not None:
            self._values["attributes"] = attributes

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#namespace_name AppmeshVirtualNode#namespace_name}.'''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_name AppmeshVirtualNode#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#attributes AppmeshVirtualNode#attributes}.'''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference",
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

    @jsii.member(jsii_name="resetAttributes")
    def reset_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributes", []))

    @builtins.property
    @jsii.member(jsii_name="attributesInput")
    def attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "attributesInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceNameInput")
    def namespace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

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
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryDns",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname"},
)
class AppmeshVirtualNodeSpecServiceDiscoveryDns:
    def __init__(self, *, hostname: builtins.str) -> None:
        '''
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#hostname AppmeshVirtualNode#hostname}.
        '''
        if __debug__:
            def stub(*, hostname: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
        self._values: typing.Dict[str, typing.Any] = {
            "hostname": hostname,
        }

    @builtins.property
    def hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#hostname AppmeshVirtualNode#hostname}.'''
        result = self._values.get("hostname")
        assert result is not None, "Required property 'hostname' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecServiceDiscoveryDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference",
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
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecServiceDiscoveryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryOutputReference",
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

    @jsii.member(jsii_name="putAwsCloudMap")
    def put_aws_cloud_map(
        self,
        *,
        namespace_name: builtins.str,
        service_name: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param namespace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#namespace_name AppmeshVirtualNode#namespace_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_name AppmeshVirtualNode#service_name}.
        :param attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#attributes AppmeshVirtualNode#attributes}.
        '''
        value = AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap(
            namespace_name=namespace_name,
            service_name=service_name,
            attributes=attributes,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsCloudMap", [value]))

    @jsii.member(jsii_name="putDns")
    def put_dns(self, *, hostname: builtins.str) -> None:
        '''
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#hostname AppmeshVirtualNode#hostname}.
        '''
        value = AppmeshVirtualNodeSpecServiceDiscoveryDns(hostname=hostname)

        return typing.cast(None, jsii.invoke(self, "putDns", [value]))

    @jsii.member(jsii_name="resetAwsCloudMap")
    def reset_aws_cloud_map(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsCloudMap", []))

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @builtins.property
    @jsii.member(jsii_name="awsCloudMap")
    def aws_cloud_map(
        self,
    ) -> AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference, jsii.get(self, "awsCloudMap"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference, jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="awsCloudMapInput")
    def aws_cloud_map_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap], jsii.get(self, "awsCloudMapInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscovery]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscovery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscovery],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscovery],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppmeshVirtualNode",
    "AppmeshVirtualNodeConfig",
    "AppmeshVirtualNodeSpec",
    "AppmeshVirtualNodeSpecBackend",
    "AppmeshVirtualNodeSpecBackendDefaults",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicy",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsOutputReference",
    "AppmeshVirtualNodeSpecBackendList",
    "AppmeshVirtualNodeSpecBackendOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualService",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference",
    "AppmeshVirtualNodeSpecListener",
    "AppmeshVirtualNodeSpecListenerConnectionPool",
    "AppmeshVirtualNodeSpecListenerConnectionPoolGrpc",
    "AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference",
    "AppmeshVirtualNodeSpecListenerConnectionPoolHttp",
    "AppmeshVirtualNodeSpecListenerConnectionPoolHttp2",
    "AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference",
    "AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference",
    "AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference",
    "AppmeshVirtualNodeSpecListenerConnectionPoolTcp",
    "AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference",
    "AppmeshVirtualNodeSpecListenerHealthCheck",
    "AppmeshVirtualNodeSpecListenerHealthCheckOutputReference",
    "AppmeshVirtualNodeSpecListenerOutlierDetection",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionInterval",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference",
    "AppmeshVirtualNodeSpecListenerOutputReference",
    "AppmeshVirtualNodeSpecListenerPortMapping",
    "AppmeshVirtualNodeSpecListenerPortMappingOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeout",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpc",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpIdle",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutTcp",
    "AppmeshVirtualNodeSpecListenerTimeoutTcpIdle",
    "AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference",
    "AppmeshVirtualNodeSpecListenerTls",
    "AppmeshVirtualNodeSpecListenerTlsCertificate",
    "AppmeshVirtualNodeSpecListenerTlsCertificateAcm",
    "AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsCertificateFile",
    "AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsCertificateSds",
    "AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidation",
    "AppmeshVirtualNodeSpecListenerTlsValidationOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames",
    "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch",
    "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrust",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustFile",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustSds",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference",
    "AppmeshVirtualNodeSpecLogging",
    "AppmeshVirtualNodeSpecLoggingAccessLog",
    "AppmeshVirtualNodeSpecLoggingAccessLogFile",
    "AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference",
    "AppmeshVirtualNodeSpecLoggingAccessLogOutputReference",
    "AppmeshVirtualNodeSpecLoggingOutputReference",
    "AppmeshVirtualNodeSpecOutputReference",
    "AppmeshVirtualNodeSpecServiceDiscovery",
    "AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap",
    "AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference",
    "AppmeshVirtualNodeSpecServiceDiscoveryDns",
    "AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference",
    "AppmeshVirtualNodeSpecServiceDiscoveryOutputReference",
]

publication.publish()
