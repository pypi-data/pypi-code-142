'''
# `aws_vpc_peering_connection_options`

Refer to the Terraform Registory for docs: [`aws_vpc_peering_connection_options`](https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options).
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


class VpcPeeringConnectionOptions(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options aws_vpc_peering_connection_options}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        vpc_peering_connection_id: builtins.str,
        accepter: typing.Optional[typing.Union["VpcPeeringConnectionOptionsAccepter", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        requester: typing.Optional[typing.Union["VpcPeeringConnectionOptionsRequester", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options aws_vpc_peering_connection_options} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param vpc_peering_connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#vpc_peering_connection_id VpcPeeringConnectionOptions#vpc_peering_connection_id}.
        :param accepter: accepter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#accepter VpcPeeringConnectionOptions#accepter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#id VpcPeeringConnectionOptions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param requester: requester block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#requester VpcPeeringConnectionOptions#requester}
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
                vpc_peering_connection_id: builtins.str,
                accepter: typing.Optional[typing.Union[VpcPeeringConnectionOptionsAccepter, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                requester: typing.Optional[typing.Union[VpcPeeringConnectionOptionsRequester, typing.Dict[str, typing.Any]]] = None,
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
        config = VpcPeeringConnectionOptionsConfig(
            vpc_peering_connection_id=vpc_peering_connection_id,
            accepter=accepter,
            id=id,
            requester=requester,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAccepter")
    def put_accepter(
        self,
        *,
        allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_classic_link_to_remote_vpc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.
        :param allow_vpc_to_remote_classic_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.
        '''
        value = VpcPeeringConnectionOptionsAccepter(
            allow_classic_link_to_remote_vpc=allow_classic_link_to_remote_vpc,
            allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution,
            allow_vpc_to_remote_classic_link=allow_vpc_to_remote_classic_link,
        )

        return typing.cast(None, jsii.invoke(self, "putAccepter", [value]))

    @jsii.member(jsii_name="putRequester")
    def put_requester(
        self,
        *,
        allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_classic_link_to_remote_vpc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.
        :param allow_vpc_to_remote_classic_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.
        '''
        value = VpcPeeringConnectionOptionsRequester(
            allow_classic_link_to_remote_vpc=allow_classic_link_to_remote_vpc,
            allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution,
            allow_vpc_to_remote_classic_link=allow_vpc_to_remote_classic_link,
        )

        return typing.cast(None, jsii.invoke(self, "putRequester", [value]))

    @jsii.member(jsii_name="resetAccepter")
    def reset_accepter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccepter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRequester")
    def reset_requester(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequester", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accepter")
    def accepter(self) -> "VpcPeeringConnectionOptionsAccepterOutputReference":
        return typing.cast("VpcPeeringConnectionOptionsAccepterOutputReference", jsii.get(self, "accepter"))

    @builtins.property
    @jsii.member(jsii_name="requester")
    def requester(self) -> "VpcPeeringConnectionOptionsRequesterOutputReference":
        return typing.cast("VpcPeeringConnectionOptionsRequesterOutputReference", jsii.get(self, "requester"))

    @builtins.property
    @jsii.member(jsii_name="accepterInput")
    def accepter_input(self) -> typing.Optional["VpcPeeringConnectionOptionsAccepter"]:
        return typing.cast(typing.Optional["VpcPeeringConnectionOptionsAccepter"], jsii.get(self, "accepterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="requesterInput")
    def requester_input(
        self,
    ) -> typing.Optional["VpcPeeringConnectionOptionsRequester"]:
        return typing.cast(typing.Optional["VpcPeeringConnectionOptionsRequester"], jsii.get(self, "requesterInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConnectionIdInput")
    def vpc_peering_connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcPeeringConnectionIdInput"))

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
    @jsii.member(jsii_name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcPeeringConnectionId"))

    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcPeeringConnectionId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsAccepter",
    jsii_struct_bases=[],
    name_mapping={
        "allow_classic_link_to_remote_vpc": "allowClassicLinkToRemoteVpc",
        "allow_remote_vpc_dns_resolution": "allowRemoteVpcDnsResolution",
        "allow_vpc_to_remote_classic_link": "allowVpcToRemoteClassicLink",
    },
)
class VpcPeeringConnectionOptionsAccepter:
    def __init__(
        self,
        *,
        allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_classic_link_to_remote_vpc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.
        :param allow_vpc_to_remote_classic_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.
        '''
        if __debug__:
            def stub(
                *,
                allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allow_classic_link_to_remote_vpc", value=allow_classic_link_to_remote_vpc, expected_type=type_hints["allow_classic_link_to_remote_vpc"])
            check_type(argname="argument allow_remote_vpc_dns_resolution", value=allow_remote_vpc_dns_resolution, expected_type=type_hints["allow_remote_vpc_dns_resolution"])
            check_type(argname="argument allow_vpc_to_remote_classic_link", value=allow_vpc_to_remote_classic_link, expected_type=type_hints["allow_vpc_to_remote_classic_link"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_classic_link_to_remote_vpc is not None:
            self._values["allow_classic_link_to_remote_vpc"] = allow_classic_link_to_remote_vpc
        if allow_remote_vpc_dns_resolution is not None:
            self._values["allow_remote_vpc_dns_resolution"] = allow_remote_vpc_dns_resolution
        if allow_vpc_to_remote_classic_link is not None:
            self._values["allow_vpc_to_remote_classic_link"] = allow_vpc_to_remote_classic_link

    @builtins.property
    def allow_classic_link_to_remote_vpc(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.'''
        result = self._values.get("allow_classic_link_to_remote_vpc")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.'''
        result = self._values.get("allow_remote_vpc_dns_resolution")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_vpc_to_remote_classic_link(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.'''
        result = self._values.get("allow_vpc_to_remote_classic_link")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionOptionsAccepter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcPeeringConnectionOptionsAccepterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsAccepterOutputReference",
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

    @jsii.member(jsii_name="resetAllowClassicLinkToRemoteVpc")
    def reset_allow_classic_link_to_remote_vpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowClassicLinkToRemoteVpc", []))

    @jsii.member(jsii_name="resetAllowRemoteVpcDnsResolution")
    def reset_allow_remote_vpc_dns_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowRemoteVpcDnsResolution", []))

    @jsii.member(jsii_name="resetAllowVpcToRemoteClassicLink")
    def reset_allow_vpc_to_remote_classic_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowVpcToRemoteClassicLink", []))

    @builtins.property
    @jsii.member(jsii_name="allowClassicLinkToRemoteVpcInput")
    def allow_classic_link_to_remote_vpc_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowClassicLinkToRemoteVpcInput"))

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolutionInput")
    def allow_remote_vpc_dns_resolution_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowRemoteVpcDnsResolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowVpcToRemoteClassicLinkInput")
    def allow_vpc_to_remote_classic_link_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowVpcToRemoteClassicLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="allowClassicLinkToRemoteVpc")
    def allow_classic_link_to_remote_vpc(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowClassicLinkToRemoteVpc"))

    @allow_classic_link_to_remote_vpc.setter
    def allow_classic_link_to_remote_vpc(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowClassicLinkToRemoteVpc", value)

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowRemoteVpcDnsResolution"))

    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowRemoteVpcDnsResolution", value)

    @builtins.property
    @jsii.member(jsii_name="allowVpcToRemoteClassicLink")
    def allow_vpc_to_remote_classic_link(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowVpcToRemoteClassicLink"))

    @allow_vpc_to_remote_classic_link.setter
    def allow_vpc_to_remote_classic_link(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVpcToRemoteClassicLink", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpcPeeringConnectionOptionsAccepter]:
        return typing.cast(typing.Optional[VpcPeeringConnectionOptionsAccepter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpcPeeringConnectionOptionsAccepter],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[VpcPeeringConnectionOptionsAccepter],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "vpc_peering_connection_id": "vpcPeeringConnectionId",
        "accepter": "accepter",
        "id": "id",
        "requester": "requester",
    },
)
class VpcPeeringConnectionOptionsConfig(cdktf.TerraformMetaArguments):
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
        vpc_peering_connection_id: builtins.str,
        accepter: typing.Optional[typing.Union[VpcPeeringConnectionOptionsAccepter, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        requester: typing.Optional[typing.Union["VpcPeeringConnectionOptionsRequester", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param vpc_peering_connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#vpc_peering_connection_id VpcPeeringConnectionOptions#vpc_peering_connection_id}.
        :param accepter: accepter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#accepter VpcPeeringConnectionOptions#accepter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#id VpcPeeringConnectionOptions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param requester: requester block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#requester VpcPeeringConnectionOptions#requester}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(accepter, dict):
            accepter = VpcPeeringConnectionOptionsAccepter(**accepter)
        if isinstance(requester, dict):
            requester = VpcPeeringConnectionOptionsRequester(**requester)
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
                vpc_peering_connection_id: builtins.str,
                accepter: typing.Optional[typing.Union[VpcPeeringConnectionOptionsAccepter, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                requester: typing.Optional[typing.Union[VpcPeeringConnectionOptionsRequester, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument vpc_peering_connection_id", value=vpc_peering_connection_id, expected_type=type_hints["vpc_peering_connection_id"])
            check_type(argname="argument accepter", value=accepter, expected_type=type_hints["accepter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument requester", value=requester, expected_type=type_hints["requester"])
        self._values: typing.Dict[str, typing.Any] = {
            "vpc_peering_connection_id": vpc_peering_connection_id,
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
        if accepter is not None:
            self._values["accepter"] = accepter
        if id is not None:
            self._values["id"] = id
        if requester is not None:
            self._values["requester"] = requester

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
    def vpc_peering_connection_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#vpc_peering_connection_id VpcPeeringConnectionOptions#vpc_peering_connection_id}.'''
        result = self._values.get("vpc_peering_connection_id")
        assert result is not None, "Required property 'vpc_peering_connection_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accepter(self) -> typing.Optional[VpcPeeringConnectionOptionsAccepter]:
        '''accepter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#accepter VpcPeeringConnectionOptions#accepter}
        '''
        result = self._values.get("accepter")
        return typing.cast(typing.Optional[VpcPeeringConnectionOptionsAccepter], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#id VpcPeeringConnectionOptions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requester(self) -> typing.Optional["VpcPeeringConnectionOptionsRequester"]:
        '''requester block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#requester VpcPeeringConnectionOptions#requester}
        '''
        result = self._values.get("requester")
        return typing.cast(typing.Optional["VpcPeeringConnectionOptionsRequester"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionOptionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsRequester",
    jsii_struct_bases=[],
    name_mapping={
        "allow_classic_link_to_remote_vpc": "allowClassicLinkToRemoteVpc",
        "allow_remote_vpc_dns_resolution": "allowRemoteVpcDnsResolution",
        "allow_vpc_to_remote_classic_link": "allowVpcToRemoteClassicLink",
    },
)
class VpcPeeringConnectionOptionsRequester:
    def __init__(
        self,
        *,
        allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_classic_link_to_remote_vpc: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.
        :param allow_remote_vpc_dns_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.
        :param allow_vpc_to_remote_classic_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.
        '''
        if __debug__:
            def stub(
                *,
                allow_classic_link_to_remote_vpc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                allow_remote_vpc_dns_resolution: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                allow_vpc_to_remote_classic_link: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allow_classic_link_to_remote_vpc", value=allow_classic_link_to_remote_vpc, expected_type=type_hints["allow_classic_link_to_remote_vpc"])
            check_type(argname="argument allow_remote_vpc_dns_resolution", value=allow_remote_vpc_dns_resolution, expected_type=type_hints["allow_remote_vpc_dns_resolution"])
            check_type(argname="argument allow_vpc_to_remote_classic_link", value=allow_vpc_to_remote_classic_link, expected_type=type_hints["allow_vpc_to_remote_classic_link"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_classic_link_to_remote_vpc is not None:
            self._values["allow_classic_link_to_remote_vpc"] = allow_classic_link_to_remote_vpc
        if allow_remote_vpc_dns_resolution is not None:
            self._values["allow_remote_vpc_dns_resolution"] = allow_remote_vpc_dns_resolution
        if allow_vpc_to_remote_classic_link is not None:
            self._values["allow_vpc_to_remote_classic_link"] = allow_vpc_to_remote_classic_link

    @builtins.property
    def allow_classic_link_to_remote_vpc(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_classic_link_to_remote_vpc VpcPeeringConnectionOptions#allow_classic_link_to_remote_vpc}.'''
        result = self._values.get("allow_classic_link_to_remote_vpc")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_remote_vpc_dns_resolution VpcPeeringConnectionOptions#allow_remote_vpc_dns_resolution}.'''
        result = self._values.get("allow_remote_vpc_dns_resolution")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_vpc_to_remote_classic_link(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpc_peering_connection_options#allow_vpc_to_remote_classic_link VpcPeeringConnectionOptions#allow_vpc_to_remote_classic_link}.'''
        result = self._values.get("allow_vpc_to_remote_classic_link")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcPeeringConnectionOptionsRequester(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcPeeringConnectionOptionsRequesterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpcPeeringConnectionOptions.VpcPeeringConnectionOptionsRequesterOutputReference",
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

    @jsii.member(jsii_name="resetAllowClassicLinkToRemoteVpc")
    def reset_allow_classic_link_to_remote_vpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowClassicLinkToRemoteVpc", []))

    @jsii.member(jsii_name="resetAllowRemoteVpcDnsResolution")
    def reset_allow_remote_vpc_dns_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowRemoteVpcDnsResolution", []))

    @jsii.member(jsii_name="resetAllowVpcToRemoteClassicLink")
    def reset_allow_vpc_to_remote_classic_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowVpcToRemoteClassicLink", []))

    @builtins.property
    @jsii.member(jsii_name="allowClassicLinkToRemoteVpcInput")
    def allow_classic_link_to_remote_vpc_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowClassicLinkToRemoteVpcInput"))

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolutionInput")
    def allow_remote_vpc_dns_resolution_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowRemoteVpcDnsResolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowVpcToRemoteClassicLinkInput")
    def allow_vpc_to_remote_classic_link_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowVpcToRemoteClassicLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="allowClassicLinkToRemoteVpc")
    def allow_classic_link_to_remote_vpc(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowClassicLinkToRemoteVpc"))

    @allow_classic_link_to_remote_vpc.setter
    def allow_classic_link_to_remote_vpc(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowClassicLinkToRemoteVpc", value)

    @builtins.property
    @jsii.member(jsii_name="allowRemoteVpcDnsResolution")
    def allow_remote_vpc_dns_resolution(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowRemoteVpcDnsResolution"))

    @allow_remote_vpc_dns_resolution.setter
    def allow_remote_vpc_dns_resolution(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowRemoteVpcDnsResolution", value)

    @builtins.property
    @jsii.member(jsii_name="allowVpcToRemoteClassicLink")
    def allow_vpc_to_remote_classic_link(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowVpcToRemoteClassicLink"))

    @allow_vpc_to_remote_classic_link.setter
    def allow_vpc_to_remote_classic_link(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVpcToRemoteClassicLink", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpcPeeringConnectionOptionsRequester]:
        return typing.cast(typing.Optional[VpcPeeringConnectionOptionsRequester], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpcPeeringConnectionOptionsRequester],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[VpcPeeringConnectionOptionsRequester],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VpcPeeringConnectionOptions",
    "VpcPeeringConnectionOptionsAccepter",
    "VpcPeeringConnectionOptionsAccepterOutputReference",
    "VpcPeeringConnectionOptionsConfig",
    "VpcPeeringConnectionOptionsRequester",
    "VpcPeeringConnectionOptionsRequesterOutputReference",
]

publication.publish()
