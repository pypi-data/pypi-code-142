'''
# `aws_network_interface`

Refer to the Terraform Registory for docs: [`aws_network_interface`](https://www.terraform.io/docs/providers/aws/r/network_interface).
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


class NetworkInterface(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.networkInterface.NetworkInterface",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/network_interface aws_network_interface}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        subnet_id: builtins.str,
        attachment: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkInterfaceAttachment", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        interface_type: typing.Optional[builtins.str] = None,
        ipv4_prefix_count: typing.Optional[jsii.Number] = None,
        ipv4_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv6_address_count: typing.Optional[jsii.Number] = None,
        ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv6_address_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv6_address_list_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ipv6_prefix_count: typing.Optional[jsii.Number] = None,
        ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_ip: typing.Optional[builtins.str] = None,
        private_ip_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_ip_list_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_ips_count: typing.Optional[jsii.Number] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_dest_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/network_interface aws_network_interface} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#subnet_id NetworkInterface#subnet_id}.
        :param attachment: attachment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#attachment NetworkInterface#attachment}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#description NetworkInterface#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#id NetworkInterface#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interface_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#interface_type NetworkInterface#interface_type}.
        :param ipv4_prefix_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv4_prefix_count NetworkInterface#ipv4_prefix_count}.
        :param ipv4_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv4_prefixes NetworkInterface#ipv4_prefixes}.
        :param ipv6_address_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_address_count NetworkInterface#ipv6_address_count}.
        :param ipv6_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_addresses NetworkInterface#ipv6_addresses}.
        :param ipv6_address_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_address_list NetworkInterface#ipv6_address_list}.
        :param ipv6_address_list_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_address_list_enabled NetworkInterface#ipv6_address_list_enabled}.
        :param ipv6_prefix_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_prefix_count NetworkInterface#ipv6_prefix_count}.
        :param ipv6_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_prefixes NetworkInterface#ipv6_prefixes}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ip NetworkInterface#private_ip}.
        :param private_ip_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ip_list NetworkInterface#private_ip_list}.
        :param private_ip_list_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ip_list_enabled NetworkInterface#private_ip_list_enabled}.
        :param private_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ips NetworkInterface#private_ips}.
        :param private_ips_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ips_count NetworkInterface#private_ips_count}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#security_groups NetworkInterface#security_groups}.
        :param source_dest_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#source_dest_check NetworkInterface#source_dest_check}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#tags NetworkInterface#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#tags_all NetworkInterface#tags_all}.
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
                subnet_id: builtins.str,
                attachment: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[NetworkInterfaceAttachment, typing.Dict[str, typing.Any]]]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                interface_type: typing.Optional[builtins.str] = None,
                ipv4_prefix_count: typing.Optional[jsii.Number] = None,
                ipv4_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
                ipv6_address_count: typing.Optional[jsii.Number] = None,
                ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
                ipv6_address_list: typing.Optional[typing.Sequence[builtins.str]] = None,
                ipv6_address_list_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                ipv6_prefix_count: typing.Optional[jsii.Number] = None,
                ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
                private_ip: typing.Optional[builtins.str] = None,
                private_ip_list: typing.Optional[typing.Sequence[builtins.str]] = None,
                private_ip_list_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
                private_ips_count: typing.Optional[jsii.Number] = None,
                security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
                source_dest_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        config = NetworkInterfaceConfig(
            subnet_id=subnet_id,
            attachment=attachment,
            description=description,
            id=id,
            interface_type=interface_type,
            ipv4_prefix_count=ipv4_prefix_count,
            ipv4_prefixes=ipv4_prefixes,
            ipv6_address_count=ipv6_address_count,
            ipv6_addresses=ipv6_addresses,
            ipv6_address_list=ipv6_address_list,
            ipv6_address_list_enabled=ipv6_address_list_enabled,
            ipv6_prefix_count=ipv6_prefix_count,
            ipv6_prefixes=ipv6_prefixes,
            private_ip=private_ip,
            private_ip_list=private_ip_list,
            private_ip_list_enabled=private_ip_list_enabled,
            private_ips=private_ips,
            private_ips_count=private_ips_count,
            security_groups=security_groups,
            source_dest_check=source_dest_check,
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

    @jsii.member(jsii_name="putAttachment")
    def put_attachment(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkInterfaceAttachment", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[NetworkInterfaceAttachment, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAttachment", [value]))

    @jsii.member(jsii_name="resetAttachment")
    def reset_attachment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttachment", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInterfaceType")
    def reset_interface_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterfaceType", []))

    @jsii.member(jsii_name="resetIpv4PrefixCount")
    def reset_ipv4_prefix_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4PrefixCount", []))

    @jsii.member(jsii_name="resetIpv4Prefixes")
    def reset_ipv4_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4Prefixes", []))

    @jsii.member(jsii_name="resetIpv6AddressCount")
    def reset_ipv6_address_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6AddressCount", []))

    @jsii.member(jsii_name="resetIpv6Addresses")
    def reset_ipv6_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6Addresses", []))

    @jsii.member(jsii_name="resetIpv6AddressList")
    def reset_ipv6_address_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6AddressList", []))

    @jsii.member(jsii_name="resetIpv6AddressListEnabled")
    def reset_ipv6_address_list_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6AddressListEnabled", []))

    @jsii.member(jsii_name="resetIpv6PrefixCount")
    def reset_ipv6_prefix_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6PrefixCount", []))

    @jsii.member(jsii_name="resetIpv6Prefixes")
    def reset_ipv6_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6Prefixes", []))

    @jsii.member(jsii_name="resetPrivateIp")
    def reset_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIp", []))

    @jsii.member(jsii_name="resetPrivateIpList")
    def reset_private_ip_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpList", []))

    @jsii.member(jsii_name="resetPrivateIpListEnabled")
    def reset_private_ip_list_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpListEnabled", []))

    @jsii.member(jsii_name="resetPrivateIps")
    def reset_private_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIps", []))

    @jsii.member(jsii_name="resetPrivateIpsCount")
    def reset_private_ips_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpsCount", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetSourceDestCheck")
    def reset_source_dest_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDestCheck", []))

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
    @jsii.member(jsii_name="attachment")
    def attachment(self) -> "NetworkInterfaceAttachmentList":
        return typing.cast("NetworkInterfaceAttachmentList", jsii.get(self, "attachment"))

    @builtins.property
    @jsii.member(jsii_name="macAddress")
    def mac_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macAddress"))

    @builtins.property
    @jsii.member(jsii_name="outpostArn")
    def outpost_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostArn"))

    @builtins.property
    @jsii.member(jsii_name="ownerId")
    def owner_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownerId"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsName")
    def private_dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateDnsName"))

    @builtins.property
    @jsii.member(jsii_name="attachmentInput")
    def attachment_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkInterfaceAttachment"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkInterfaceAttachment"]]], jsii.get(self, "attachmentInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="interfaceTypeInput")
    def interface_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4PrefixCountInput")
    def ipv4_prefix_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv4PrefixCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4PrefixesInput")
    def ipv4_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv4PrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressCountInput")
    def ipv6_address_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv6AddressCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressesInput")
    def ipv6_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv6AddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressListEnabledInput")
    def ipv6_address_list_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ipv6AddressListEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressListInput")
    def ipv6_address_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv6AddressListInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6PrefixCountInput")
    def ipv6_prefix_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv6PrefixCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6PrefixesInput")
    def ipv6_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv6PrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpInput")
    def private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpListEnabledInput")
    def private_ip_list_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privateIpListEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpListInput")
    def private_ip_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privateIpListInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpsCountInput")
    def private_ips_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "privateIpsCountInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpsInput")
    def private_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privateIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDestCheckInput")
    def source_dest_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sourceDestCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

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
    @jsii.member(jsii_name="interfaceType")
    def interface_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interfaceType"))

    @interface_type.setter
    def interface_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interfaceType", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4PrefixCount")
    def ipv4_prefix_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipv4PrefixCount"))

    @ipv4_prefix_count.setter
    def ipv4_prefix_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4PrefixCount", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4Prefixes")
    def ipv4_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv4Prefixes"))

    @ipv4_prefixes.setter
    def ipv4_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Prefixes", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressCount")
    def ipv6_address_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipv6AddressCount"))

    @ipv6_address_count.setter
    def ipv6_address_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6AddressCount", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6Addresses")
    def ipv6_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv6Addresses"))

    @ipv6_addresses.setter
    def ipv6_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Addresses", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressList")
    def ipv6_address_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv6AddressList"))

    @ipv6_address_list.setter
    def ipv6_address_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6AddressList", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressListEnabled")
    def ipv6_address_list_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ipv6AddressListEnabled"))

    @ipv6_address_list_enabled.setter
    def ipv6_address_list_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6AddressListEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6PrefixCount")
    def ipv6_prefix_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipv6PrefixCount"))

    @ipv6_prefix_count.setter
    def ipv6_prefix_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6PrefixCount", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6Prefixes")
    def ipv6_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipv6Prefixes"))

    @ipv6_prefixes.setter
    def ipv6_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Prefixes", value)

    @builtins.property
    @jsii.member(jsii_name="privateIp")
    def private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIp"))

    @private_ip.setter
    def private_ip(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIp", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpList")
    def private_ip_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateIpList"))

    @private_ip_list.setter
    def private_ip_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpList", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpListEnabled")
    def private_ip_list_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privateIpListEnabled"))

    @private_ip_list_enabled.setter
    def private_ip_list_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpListEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="privateIps")
    def private_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateIps"))

    @private_ips.setter
    def private_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIps", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpsCount")
    def private_ips_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "privateIpsCount"))

    @private_ips_count.setter
    def private_ips_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpsCount", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDestCheck")
    def source_dest_check(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sourceDestCheck"))

    @source_dest_check.setter
    def source_dest_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDestCheck", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

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
    jsii_type="@cdktf/provider-aws.networkInterface.NetworkInterfaceAttachment",
    jsii_struct_bases=[],
    name_mapping={"device_index": "deviceIndex", "instance": "instance"},
)
class NetworkInterfaceAttachment:
    def __init__(self, *, device_index: jsii.Number, instance: builtins.str) -> None:
        '''
        :param device_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#device_index NetworkInterface#device_index}.
        :param instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#instance NetworkInterface#instance}.
        '''
        if __debug__:
            def stub(*, device_index: jsii.Number, instance: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument device_index", value=device_index, expected_type=type_hints["device_index"])
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        self._values: typing.Dict[str, typing.Any] = {
            "device_index": device_index,
            "instance": instance,
        }

    @builtins.property
    def device_index(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#device_index NetworkInterface#device_index}.'''
        result = self._values.get("device_index")
        assert result is not None, "Required property 'device_index' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#instance NetworkInterface#instance}.'''
        result = self._values.get("instance")
        assert result is not None, "Required property 'instance' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInterfaceAttachment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkInterfaceAttachmentList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.networkInterface.NetworkInterfaceAttachmentList",
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
    def get(self, index: jsii.Number) -> "NetworkInterfaceAttachmentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkInterfaceAttachmentOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkInterfaceAttachment]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkInterfaceAttachment]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkInterfaceAttachment]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkInterfaceAttachment]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkInterfaceAttachmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.networkInterface.NetworkInterfaceAttachmentOutputReference",
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

    @builtins.property
    @jsii.member(jsii_name="attachmentId")
    def attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentId"))

    @builtins.property
    @jsii.member(jsii_name="deviceIndexInput")
    def device_index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deviceIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceInput")
    def instance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceIndex")
    def device_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deviceIndex"))

    @device_index.setter
    def device_index(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceIndex", value)

    @builtins.property
    @jsii.member(jsii_name="instance")
    def instance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instance"))

    @instance.setter
    def instance(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkInterfaceAttachment, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkInterfaceAttachment, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkInterfaceAttachment, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[NetworkInterfaceAttachment, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.networkInterface.NetworkInterfaceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "subnet_id": "subnetId",
        "attachment": "attachment",
        "description": "description",
        "id": "id",
        "interface_type": "interfaceType",
        "ipv4_prefix_count": "ipv4PrefixCount",
        "ipv4_prefixes": "ipv4Prefixes",
        "ipv6_address_count": "ipv6AddressCount",
        "ipv6_addresses": "ipv6Addresses",
        "ipv6_address_list": "ipv6AddressList",
        "ipv6_address_list_enabled": "ipv6AddressListEnabled",
        "ipv6_prefix_count": "ipv6PrefixCount",
        "ipv6_prefixes": "ipv6Prefixes",
        "private_ip": "privateIp",
        "private_ip_list": "privateIpList",
        "private_ip_list_enabled": "privateIpListEnabled",
        "private_ips": "privateIps",
        "private_ips_count": "privateIpsCount",
        "security_groups": "securityGroups",
        "source_dest_check": "sourceDestCheck",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class NetworkInterfaceConfig(cdktf.TerraformMetaArguments):
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
        subnet_id: builtins.str,
        attachment: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[NetworkInterfaceAttachment, typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        interface_type: typing.Optional[builtins.str] = None,
        ipv4_prefix_count: typing.Optional[jsii.Number] = None,
        ipv4_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv6_address_count: typing.Optional[jsii.Number] = None,
        ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv6_address_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv6_address_list_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ipv6_prefix_count: typing.Optional[jsii.Number] = None,
        ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_ip: typing.Optional[builtins.str] = None,
        private_ip_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_ip_list_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_ips_count: typing.Optional[jsii.Number] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_dest_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#subnet_id NetworkInterface#subnet_id}.
        :param attachment: attachment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#attachment NetworkInterface#attachment}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#description NetworkInterface#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#id NetworkInterface#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interface_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#interface_type NetworkInterface#interface_type}.
        :param ipv4_prefix_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv4_prefix_count NetworkInterface#ipv4_prefix_count}.
        :param ipv4_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv4_prefixes NetworkInterface#ipv4_prefixes}.
        :param ipv6_address_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_address_count NetworkInterface#ipv6_address_count}.
        :param ipv6_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_addresses NetworkInterface#ipv6_addresses}.
        :param ipv6_address_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_address_list NetworkInterface#ipv6_address_list}.
        :param ipv6_address_list_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_address_list_enabled NetworkInterface#ipv6_address_list_enabled}.
        :param ipv6_prefix_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_prefix_count NetworkInterface#ipv6_prefix_count}.
        :param ipv6_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_prefixes NetworkInterface#ipv6_prefixes}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ip NetworkInterface#private_ip}.
        :param private_ip_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ip_list NetworkInterface#private_ip_list}.
        :param private_ip_list_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ip_list_enabled NetworkInterface#private_ip_list_enabled}.
        :param private_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ips NetworkInterface#private_ips}.
        :param private_ips_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ips_count NetworkInterface#private_ips_count}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#security_groups NetworkInterface#security_groups}.
        :param source_dest_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#source_dest_check NetworkInterface#source_dest_check}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#tags NetworkInterface#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#tags_all NetworkInterface#tags_all}.
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
                subnet_id: builtins.str,
                attachment: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[NetworkInterfaceAttachment, typing.Dict[str, typing.Any]]]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                interface_type: typing.Optional[builtins.str] = None,
                ipv4_prefix_count: typing.Optional[jsii.Number] = None,
                ipv4_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
                ipv6_address_count: typing.Optional[jsii.Number] = None,
                ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
                ipv6_address_list: typing.Optional[typing.Sequence[builtins.str]] = None,
                ipv6_address_list_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                ipv6_prefix_count: typing.Optional[jsii.Number] = None,
                ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
                private_ip: typing.Optional[builtins.str] = None,
                private_ip_list: typing.Optional[typing.Sequence[builtins.str]] = None,
                private_ip_list_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
                private_ips_count: typing.Optional[jsii.Number] = None,
                security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
                source_dest_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument attachment", value=attachment, expected_type=type_hints["attachment"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument interface_type", value=interface_type, expected_type=type_hints["interface_type"])
            check_type(argname="argument ipv4_prefix_count", value=ipv4_prefix_count, expected_type=type_hints["ipv4_prefix_count"])
            check_type(argname="argument ipv4_prefixes", value=ipv4_prefixes, expected_type=type_hints["ipv4_prefixes"])
            check_type(argname="argument ipv6_address_count", value=ipv6_address_count, expected_type=type_hints["ipv6_address_count"])
            check_type(argname="argument ipv6_addresses", value=ipv6_addresses, expected_type=type_hints["ipv6_addresses"])
            check_type(argname="argument ipv6_address_list", value=ipv6_address_list, expected_type=type_hints["ipv6_address_list"])
            check_type(argname="argument ipv6_address_list_enabled", value=ipv6_address_list_enabled, expected_type=type_hints["ipv6_address_list_enabled"])
            check_type(argname="argument ipv6_prefix_count", value=ipv6_prefix_count, expected_type=type_hints["ipv6_prefix_count"])
            check_type(argname="argument ipv6_prefixes", value=ipv6_prefixes, expected_type=type_hints["ipv6_prefixes"])
            check_type(argname="argument private_ip", value=private_ip, expected_type=type_hints["private_ip"])
            check_type(argname="argument private_ip_list", value=private_ip_list, expected_type=type_hints["private_ip_list"])
            check_type(argname="argument private_ip_list_enabled", value=private_ip_list_enabled, expected_type=type_hints["private_ip_list_enabled"])
            check_type(argname="argument private_ips", value=private_ips, expected_type=type_hints["private_ips"])
            check_type(argname="argument private_ips_count", value=private_ips_count, expected_type=type_hints["private_ips_count"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument source_dest_check", value=source_dest_check, expected_type=type_hints["source_dest_check"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "subnet_id": subnet_id,
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
        if attachment is not None:
            self._values["attachment"] = attachment
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if interface_type is not None:
            self._values["interface_type"] = interface_type
        if ipv4_prefix_count is not None:
            self._values["ipv4_prefix_count"] = ipv4_prefix_count
        if ipv4_prefixes is not None:
            self._values["ipv4_prefixes"] = ipv4_prefixes
        if ipv6_address_count is not None:
            self._values["ipv6_address_count"] = ipv6_address_count
        if ipv6_addresses is not None:
            self._values["ipv6_addresses"] = ipv6_addresses
        if ipv6_address_list is not None:
            self._values["ipv6_address_list"] = ipv6_address_list
        if ipv6_address_list_enabled is not None:
            self._values["ipv6_address_list_enabled"] = ipv6_address_list_enabled
        if ipv6_prefix_count is not None:
            self._values["ipv6_prefix_count"] = ipv6_prefix_count
        if ipv6_prefixes is not None:
            self._values["ipv6_prefixes"] = ipv6_prefixes
        if private_ip is not None:
            self._values["private_ip"] = private_ip
        if private_ip_list is not None:
            self._values["private_ip_list"] = private_ip_list
        if private_ip_list_enabled is not None:
            self._values["private_ip_list_enabled"] = private_ip_list_enabled
        if private_ips is not None:
            self._values["private_ips"] = private_ips
        if private_ips_count is not None:
            self._values["private_ips_count"] = private_ips_count
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if source_dest_check is not None:
            self._values["source_dest_check"] = source_dest_check
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
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#subnet_id NetworkInterface#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attachment(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkInterfaceAttachment]]]:
        '''attachment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#attachment NetworkInterface#attachment}
        '''
        result = self._values.get("attachment")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkInterfaceAttachment]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#description NetworkInterface#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#id NetworkInterface#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interface_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#interface_type NetworkInterface#interface_type}.'''
        result = self._values.get("interface_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv4_prefix_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv4_prefix_count NetworkInterface#ipv4_prefix_count}.'''
        result = self._values.get("ipv4_prefix_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv4_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv4_prefixes NetworkInterface#ipv4_prefixes}.'''
        result = self._values.get("ipv4_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_address_count NetworkInterface#ipv6_address_count}.'''
        result = self._values.get("ipv6_address_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_addresses NetworkInterface#ipv6_addresses}.'''
        result = self._values.get("ipv6_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipv6_address_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_address_list NetworkInterface#ipv6_address_list}.'''
        result = self._values.get("ipv6_address_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipv6_address_list_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_address_list_enabled NetworkInterface#ipv6_address_list_enabled}.'''
        result = self._values.get("ipv6_address_list_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ipv6_prefix_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_prefix_count NetworkInterface#ipv6_prefix_count}.'''
        result = self._values.get("ipv6_prefix_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#ipv6_prefixes NetworkInterface#ipv6_prefixes}.'''
        result = self._values.get("ipv6_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ip NetworkInterface#private_ip}.'''
        result = self._values.get("private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ip_list NetworkInterface#private_ip_list}.'''
        result = self._values.get("private_ip_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_ip_list_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ip_list_enabled NetworkInterface#private_ip_list_enabled}.'''
        result = self._values.get("private_ip_list_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def private_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ips NetworkInterface#private_ips}.'''
        result = self._values.get("private_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_ips_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#private_ips_count NetworkInterface#private_ips_count}.'''
        result = self._values.get("private_ips_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#security_groups NetworkInterface#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_dest_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#source_dest_check NetworkInterface#source_dest_check}.'''
        result = self._values.get("source_dest_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#tags NetworkInterface#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/network_interface#tags_all NetworkInterface#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInterfaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "NetworkInterface",
    "NetworkInterfaceAttachment",
    "NetworkInterfaceAttachmentList",
    "NetworkInterfaceAttachmentOutputReference",
    "NetworkInterfaceConfig",
]

publication.publish()
