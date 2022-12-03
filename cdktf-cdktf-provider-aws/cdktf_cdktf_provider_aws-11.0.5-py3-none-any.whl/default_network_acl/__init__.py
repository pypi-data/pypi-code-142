'''
# `aws_default_network_acl`

Refer to the Terraform Registory for docs: [`aws_default_network_acl`](https://www.terraform.io/docs/providers/aws/r/default_network_acl).
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


class DefaultNetworkAcl(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.defaultNetworkAcl.DefaultNetworkAcl",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl aws_default_network_acl}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        default_network_acl_id: builtins.str,
        egress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclEgress", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclIngress", typing.Dict[str, typing.Any]]]]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl aws_default_network_acl} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_network_acl_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#default_network_acl_id DefaultNetworkAcl#default_network_acl_id}.
        :param egress: egress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#egress DefaultNetworkAcl#egress}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#id DefaultNetworkAcl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ingress DefaultNetworkAcl#ingress}
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#subnet_ids DefaultNetworkAcl#subnet_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags DefaultNetworkAcl#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags_all DefaultNetworkAcl#tags_all}.
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
                default_network_acl_id: builtins.str,
                egress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclEgress, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                ingress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclIngress, typing.Dict[str, typing.Any]]]]] = None,
                subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        config = DefaultNetworkAclConfig(
            default_network_acl_id=default_network_acl_id,
            egress=egress,
            id=id,
            ingress=ingress,
            subnet_ids=subnet_ids,
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

    @jsii.member(jsii_name="putEgress")
    def put_egress(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclEgress", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclEgress, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEgress", [value]))

    @jsii.member(jsii_name="putIngress")
    def put_ingress(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclIngress", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclIngress, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIngress", [value]))

    @jsii.member(jsii_name="resetEgress")
    def reset_egress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgress", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIngress")
    def reset_ingress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngress", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

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
    @jsii.member(jsii_name="egress")
    def egress(self) -> "DefaultNetworkAclEgressList":
        return typing.cast("DefaultNetworkAclEgressList", jsii.get(self, "egress"))

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> "DefaultNetworkAclIngressList":
        return typing.cast("DefaultNetworkAclIngressList", jsii.get(self, "ingress"))

    @builtins.property
    @jsii.member(jsii_name="ownerId")
    def owner_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownerId"))

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="defaultNetworkAclIdInput")
    def default_network_acl_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultNetworkAclIdInput"))

    @builtins.property
    @jsii.member(jsii_name="egressInput")
    def egress_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DefaultNetworkAclEgress"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DefaultNetworkAclEgress"]]], jsii.get(self, "egressInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressInput")
    def ingress_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DefaultNetworkAclIngress"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DefaultNetworkAclIngress"]]], jsii.get(self, "ingressInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

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
    @jsii.member(jsii_name="defaultNetworkAclId")
    def default_network_acl_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultNetworkAclId"))

    @default_network_acl_id.setter
    def default_network_acl_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultNetworkAclId", value)

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
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

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
    jsii_type="@cdktf/provider-aws.defaultNetworkAcl.DefaultNetworkAclConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_network_acl_id": "defaultNetworkAclId",
        "egress": "egress",
        "id": "id",
        "ingress": "ingress",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DefaultNetworkAclConfig(cdktf.TerraformMetaArguments):
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
        default_network_acl_id: builtins.str,
        egress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclEgress", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclIngress", typing.Dict[str, typing.Any]]]]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        :param default_network_acl_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#default_network_acl_id DefaultNetworkAcl#default_network_acl_id}.
        :param egress: egress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#egress DefaultNetworkAcl#egress}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#id DefaultNetworkAcl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ingress DefaultNetworkAcl#ingress}
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#subnet_ids DefaultNetworkAcl#subnet_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags DefaultNetworkAcl#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags_all DefaultNetworkAcl#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
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
                default_network_acl_id: builtins.str,
                egress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclEgress, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                ingress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclIngress, typing.Dict[str, typing.Any]]]]] = None,
                subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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
            check_type(argname="argument default_network_acl_id", value=default_network_acl_id, expected_type=type_hints["default_network_acl_id"])
            check_type(argname="argument egress", value=egress, expected_type=type_hints["egress"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_network_acl_id": default_network_acl_id,
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
        if egress is not None:
            self._values["egress"] = egress
        if id is not None:
            self._values["id"] = id
        if ingress is not None:
            self._values["ingress"] = ingress
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
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
    def default_network_acl_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#default_network_acl_id DefaultNetworkAcl#default_network_acl_id}.'''
        result = self._values.get("default_network_acl_id")
        assert result is not None, "Required property 'default_network_acl_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def egress(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DefaultNetworkAclEgress"]]]:
        '''egress block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#egress DefaultNetworkAcl#egress}
        '''
        result = self._values.get("egress")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DefaultNetworkAclEgress"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#id DefaultNetworkAcl#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DefaultNetworkAclIngress"]]]:
        '''ingress block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ingress DefaultNetworkAcl#ingress}
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DefaultNetworkAclIngress"]]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#subnet_ids DefaultNetworkAcl#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags DefaultNetworkAcl#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags_all DefaultNetworkAcl#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefaultNetworkAclConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.defaultNetworkAcl.DefaultNetworkAclEgress",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "from_port": "fromPort",
        "protocol": "protocol",
        "rule_no": "ruleNo",
        "to_port": "toPort",
        "cidr_block": "cidrBlock",
        "icmp_code": "icmpCode",
        "icmp_type": "icmpType",
        "ipv6_cidr_block": "ipv6CidrBlock",
    },
)
class DefaultNetworkAclEgress:
    def __init__(
        self,
        *,
        action: builtins.str,
        from_port: jsii.Number,
        protocol: builtins.str,
        rule_no: jsii.Number,
        to_port: jsii.Number,
        cidr_block: typing.Optional[builtins.str] = None,
        icmp_code: typing.Optional[jsii.Number] = None,
        icmp_type: typing.Optional[jsii.Number] = None,
        ipv6_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#action DefaultNetworkAcl#action}.
        :param from_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#from_port DefaultNetworkAcl#from_port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#protocol DefaultNetworkAcl#protocol}.
        :param rule_no: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#rule_no DefaultNetworkAcl#rule_no}.
        :param to_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#to_port DefaultNetworkAcl#to_port}.
        :param cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#cidr_block DefaultNetworkAcl#cidr_block}.
        :param icmp_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_code DefaultNetworkAcl#icmp_code}.
        :param icmp_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_type DefaultNetworkAcl#icmp_type}.
        :param ipv6_cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ipv6_cidr_block DefaultNetworkAcl#ipv6_cidr_block}.
        '''
        if __debug__:
            def stub(
                *,
                action: builtins.str,
                from_port: jsii.Number,
                protocol: builtins.str,
                rule_no: jsii.Number,
                to_port: jsii.Number,
                cidr_block: typing.Optional[builtins.str] = None,
                icmp_code: typing.Optional[jsii.Number] = None,
                icmp_type: typing.Optional[jsii.Number] = None,
                ipv6_cidr_block: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument rule_no", value=rule_no, expected_type=type_hints["rule_no"])
            check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument icmp_code", value=icmp_code, expected_type=type_hints["icmp_code"])
            check_type(argname="argument icmp_type", value=icmp_type, expected_type=type_hints["icmp_type"])
            check_type(argname="argument ipv6_cidr_block", value=ipv6_cidr_block, expected_type=type_hints["ipv6_cidr_block"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "from_port": from_port,
            "protocol": protocol,
            "rule_no": rule_no,
            "to_port": to_port,
        }
        if cidr_block is not None:
            self._values["cidr_block"] = cidr_block
        if icmp_code is not None:
            self._values["icmp_code"] = icmp_code
        if icmp_type is not None:
            self._values["icmp_type"] = icmp_type
        if ipv6_cidr_block is not None:
            self._values["ipv6_cidr_block"] = ipv6_cidr_block

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#action DefaultNetworkAcl#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def from_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#from_port DefaultNetworkAcl#from_port}.'''
        result = self._values.get("from_port")
        assert result is not None, "Required property 'from_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#protocol DefaultNetworkAcl#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_no(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#rule_no DefaultNetworkAcl#rule_no}.'''
        result = self._values.get("rule_no")
        assert result is not None, "Required property 'rule_no' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def to_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#to_port DefaultNetworkAcl#to_port}.'''
        result = self._values.get("to_port")
        assert result is not None, "Required property 'to_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#cidr_block DefaultNetworkAcl#cidr_block}.'''
        result = self._values.get("cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def icmp_code(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_code DefaultNetworkAcl#icmp_code}.'''
        result = self._values.get("icmp_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def icmp_type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_type DefaultNetworkAcl#icmp_type}.'''
        result = self._values.get("icmp_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ipv6_cidr_block DefaultNetworkAcl#ipv6_cidr_block}.'''
        result = self._values.get("ipv6_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefaultNetworkAclEgress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DefaultNetworkAclEgressList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.defaultNetworkAcl.DefaultNetworkAclEgressList",
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
    def get(self, index: jsii.Number) -> "DefaultNetworkAclEgressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DefaultNetworkAclEgressOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DefaultNetworkAclEgress]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DefaultNetworkAclEgress]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DefaultNetworkAclEgress]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DefaultNetworkAclEgress]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DefaultNetworkAclEgressOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.defaultNetworkAcl.DefaultNetworkAclEgressOutputReference",
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

    @jsii.member(jsii_name="resetCidrBlock")
    def reset_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrBlock", []))

    @jsii.member(jsii_name="resetIcmpCode")
    def reset_icmp_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpCode", []))

    @jsii.member(jsii_name="resetIcmpType")
    def reset_icmp_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpType", []))

    @jsii.member(jsii_name="resetIpv6CidrBlock")
    def reset_ipv6_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6CidrBlock", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlockInput")
    def cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="fromPortInput")
    def from_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fromPortInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpCodeInput")
    def icmp_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "icmpCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpTypeInput")
    def icmp_type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "icmpTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlockInput")
    def ipv6_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleNoInput")
    def rule_no_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ruleNoInput"))

    @builtins.property
    @jsii.member(jsii_name="toPortInput")
    def to_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "toPortInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidrBlock"))

    @cidr_block.setter
    def cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="fromPort")
    def from_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fromPort"))

    @from_port.setter
    def from_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromPort", value)

    @builtins.property
    @jsii.member(jsii_name="icmpCode")
    def icmp_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "icmpCode"))

    @icmp_code.setter
    def icmp_code(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpCode", value)

    @builtins.property
    @jsii.member(jsii_name="icmpType")
    def icmp_type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "icmpType"))

    @icmp_type.setter
    def icmp_type(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpType", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6CidrBlock"))

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6CidrBlock", value)

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
    @jsii.member(jsii_name="ruleNo")
    def rule_no(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleNo"))

    @rule_no.setter
    def rule_no(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleNo", value)

    @builtins.property
    @jsii.member(jsii_name="toPort")
    def to_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "toPort"))

    @to_port.setter
    def to_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DefaultNetworkAclEgress, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DefaultNetworkAclEgress, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DefaultNetworkAclEgress, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DefaultNetworkAclEgress, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.defaultNetworkAcl.DefaultNetworkAclIngress",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "from_port": "fromPort",
        "protocol": "protocol",
        "rule_no": "ruleNo",
        "to_port": "toPort",
        "cidr_block": "cidrBlock",
        "icmp_code": "icmpCode",
        "icmp_type": "icmpType",
        "ipv6_cidr_block": "ipv6CidrBlock",
    },
)
class DefaultNetworkAclIngress:
    def __init__(
        self,
        *,
        action: builtins.str,
        from_port: jsii.Number,
        protocol: builtins.str,
        rule_no: jsii.Number,
        to_port: jsii.Number,
        cidr_block: typing.Optional[builtins.str] = None,
        icmp_code: typing.Optional[jsii.Number] = None,
        icmp_type: typing.Optional[jsii.Number] = None,
        ipv6_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#action DefaultNetworkAcl#action}.
        :param from_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#from_port DefaultNetworkAcl#from_port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#protocol DefaultNetworkAcl#protocol}.
        :param rule_no: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#rule_no DefaultNetworkAcl#rule_no}.
        :param to_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#to_port DefaultNetworkAcl#to_port}.
        :param cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#cidr_block DefaultNetworkAcl#cidr_block}.
        :param icmp_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_code DefaultNetworkAcl#icmp_code}.
        :param icmp_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_type DefaultNetworkAcl#icmp_type}.
        :param ipv6_cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ipv6_cidr_block DefaultNetworkAcl#ipv6_cidr_block}.
        '''
        if __debug__:
            def stub(
                *,
                action: builtins.str,
                from_port: jsii.Number,
                protocol: builtins.str,
                rule_no: jsii.Number,
                to_port: jsii.Number,
                cidr_block: typing.Optional[builtins.str] = None,
                icmp_code: typing.Optional[jsii.Number] = None,
                icmp_type: typing.Optional[jsii.Number] = None,
                ipv6_cidr_block: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument rule_no", value=rule_no, expected_type=type_hints["rule_no"])
            check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument icmp_code", value=icmp_code, expected_type=type_hints["icmp_code"])
            check_type(argname="argument icmp_type", value=icmp_type, expected_type=type_hints["icmp_type"])
            check_type(argname="argument ipv6_cidr_block", value=ipv6_cidr_block, expected_type=type_hints["ipv6_cidr_block"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "from_port": from_port,
            "protocol": protocol,
            "rule_no": rule_no,
            "to_port": to_port,
        }
        if cidr_block is not None:
            self._values["cidr_block"] = cidr_block
        if icmp_code is not None:
            self._values["icmp_code"] = icmp_code
        if icmp_type is not None:
            self._values["icmp_type"] = icmp_type
        if ipv6_cidr_block is not None:
            self._values["ipv6_cidr_block"] = ipv6_cidr_block

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#action DefaultNetworkAcl#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def from_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#from_port DefaultNetworkAcl#from_port}.'''
        result = self._values.get("from_port")
        assert result is not None, "Required property 'from_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#protocol DefaultNetworkAcl#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_no(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#rule_no DefaultNetworkAcl#rule_no}.'''
        result = self._values.get("rule_no")
        assert result is not None, "Required property 'rule_no' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def to_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#to_port DefaultNetworkAcl#to_port}.'''
        result = self._values.get("to_port")
        assert result is not None, "Required property 'to_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#cidr_block DefaultNetworkAcl#cidr_block}.'''
        result = self._values.get("cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def icmp_code(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_code DefaultNetworkAcl#icmp_code}.'''
        result = self._values.get("icmp_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def icmp_type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_type DefaultNetworkAcl#icmp_type}.'''
        result = self._values.get("icmp_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ipv6_cidr_block DefaultNetworkAcl#ipv6_cidr_block}.'''
        result = self._values.get("ipv6_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefaultNetworkAclIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DefaultNetworkAclIngressList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.defaultNetworkAcl.DefaultNetworkAclIngressList",
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
    def get(self, index: jsii.Number) -> "DefaultNetworkAclIngressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DefaultNetworkAclIngressOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DefaultNetworkAclIngress]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DefaultNetworkAclIngress]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DefaultNetworkAclIngress]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DefaultNetworkAclIngress]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DefaultNetworkAclIngressOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.defaultNetworkAcl.DefaultNetworkAclIngressOutputReference",
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

    @jsii.member(jsii_name="resetCidrBlock")
    def reset_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrBlock", []))

    @jsii.member(jsii_name="resetIcmpCode")
    def reset_icmp_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpCode", []))

    @jsii.member(jsii_name="resetIcmpType")
    def reset_icmp_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpType", []))

    @jsii.member(jsii_name="resetIpv6CidrBlock")
    def reset_ipv6_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6CidrBlock", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlockInput")
    def cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="fromPortInput")
    def from_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fromPortInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpCodeInput")
    def icmp_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "icmpCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpTypeInput")
    def icmp_type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "icmpTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlockInput")
    def ipv6_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleNoInput")
    def rule_no_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ruleNoInput"))

    @builtins.property
    @jsii.member(jsii_name="toPortInput")
    def to_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "toPortInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidrBlock"))

    @cidr_block.setter
    def cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="fromPort")
    def from_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fromPort"))

    @from_port.setter
    def from_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromPort", value)

    @builtins.property
    @jsii.member(jsii_name="icmpCode")
    def icmp_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "icmpCode"))

    @icmp_code.setter
    def icmp_code(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpCode", value)

    @builtins.property
    @jsii.member(jsii_name="icmpType")
    def icmp_type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "icmpType"))

    @icmp_type.setter
    def icmp_type(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpType", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6CidrBlock"))

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6CidrBlock", value)

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
    @jsii.member(jsii_name="ruleNo")
    def rule_no(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleNo"))

    @rule_no.setter
    def rule_no(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleNo", value)

    @builtins.property
    @jsii.member(jsii_name="toPort")
    def to_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "toPort"))

    @to_port.setter
    def to_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DefaultNetworkAclIngress, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DefaultNetworkAclIngress, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DefaultNetworkAclIngress, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DefaultNetworkAclIngress, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DefaultNetworkAcl",
    "DefaultNetworkAclConfig",
    "DefaultNetworkAclEgress",
    "DefaultNetworkAclEgressList",
    "DefaultNetworkAclEgressOutputReference",
    "DefaultNetworkAclIngress",
    "DefaultNetworkAclIngressList",
    "DefaultNetworkAclIngressOutputReference",
]

publication.publish()
