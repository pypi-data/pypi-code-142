'''
# `aws_dx_transit_virtual_interface`

Refer to the Terraform Registory for docs: [`aws_dx_transit_virtual_interface`](https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface).
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


class DxTransitVirtualInterface(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dxTransitVirtualInterface.DxTransitVirtualInterface",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface aws_dx_transit_virtual_interface}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        address_family: builtins.str,
        bgp_asn: jsii.Number,
        connection_id: builtins.str,
        dx_gateway_id: builtins.str,
        name: builtins.str,
        vlan: jsii.Number,
        amazon_address: typing.Optional[builtins.str] = None,
        bgp_auth_key: typing.Optional[builtins.str] = None,
        customer_address: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mtu: typing.Optional[jsii.Number] = None,
        sitelink_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DxTransitVirtualInterfaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface aws_dx_transit_virtual_interface} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param address_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#address_family DxTransitVirtualInterface#address_family}.
        :param bgp_asn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#bgp_asn DxTransitVirtualInterface#bgp_asn}.
        :param connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#connection_id DxTransitVirtualInterface#connection_id}.
        :param dx_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#dx_gateway_id DxTransitVirtualInterface#dx_gateway_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#name DxTransitVirtualInterface#name}.
        :param vlan: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#vlan DxTransitVirtualInterface#vlan}.
        :param amazon_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#amazon_address DxTransitVirtualInterface#amazon_address}.
        :param bgp_auth_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#bgp_auth_key DxTransitVirtualInterface#bgp_auth_key}.
        :param customer_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#customer_address DxTransitVirtualInterface#customer_address}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#id DxTransitVirtualInterface#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mtu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#mtu DxTransitVirtualInterface#mtu}.
        :param sitelink_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#sitelink_enabled DxTransitVirtualInterface#sitelink_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#tags DxTransitVirtualInterface#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#tags_all DxTransitVirtualInterface#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#timeouts DxTransitVirtualInterface#timeouts}
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
                address_family: builtins.str,
                bgp_asn: jsii.Number,
                connection_id: builtins.str,
                dx_gateway_id: builtins.str,
                name: builtins.str,
                vlan: jsii.Number,
                amazon_address: typing.Optional[builtins.str] = None,
                bgp_auth_key: typing.Optional[builtins.str] = None,
                customer_address: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                mtu: typing.Optional[jsii.Number] = None,
                sitelink_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[DxTransitVirtualInterfaceTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = DxTransitVirtualInterfaceConfig(
            address_family=address_family,
            bgp_asn=bgp_asn,
            connection_id=connection_id,
            dx_gateway_id=dx_gateway_id,
            name=name,
            vlan=vlan,
            amazon_address=amazon_address,
            bgp_auth_key=bgp_auth_key,
            customer_address=customer_address,
            id=id,
            mtu=mtu,
            sitelink_enabled=sitelink_enabled,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#create DxTransitVirtualInterface#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#delete DxTransitVirtualInterface#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#update DxTransitVirtualInterface#update}.
        '''
        value = DxTransitVirtualInterfaceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAmazonAddress")
    def reset_amazon_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmazonAddress", []))

    @jsii.member(jsii_name="resetBgpAuthKey")
    def reset_bgp_auth_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgpAuthKey", []))

    @jsii.member(jsii_name="resetCustomerAddress")
    def reset_customer_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerAddress", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMtu")
    def reset_mtu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMtu", []))

    @jsii.member(jsii_name="resetSitelinkEnabled")
    def reset_sitelink_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSitelinkEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="amazonSideAsn")
    def amazon_side_asn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amazonSideAsn"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="awsDevice")
    def aws_device(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsDevice"))

    @builtins.property
    @jsii.member(jsii_name="jumboFrameCapable")
    def jumbo_frame_capable(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "jumboFrameCapable"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DxTransitVirtualInterfaceTimeoutsOutputReference":
        return typing.cast("DxTransitVirtualInterfaceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="addressFamilyInput")
    def address_family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressFamilyInput"))

    @builtins.property
    @jsii.member(jsii_name="amazonAddressInput")
    def amazon_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amazonAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="bgpAsnInput")
    def bgp_asn_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bgpAsnInput"))

    @builtins.property
    @jsii.member(jsii_name="bgpAuthKeyInput")
    def bgp_auth_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bgpAuthKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionIdInput")
    def connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customerAddressInput")
    def customer_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="dxGatewayIdInput")
    def dx_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dxGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mtuInput")
    def mtu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mtuInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sitelinkEnabledInput")
    def sitelink_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sitelinkEnabledInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DxTransitVirtualInterfaceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DxTransitVirtualInterfaceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vlanInput")
    def vlan_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vlanInput"))

    @builtins.property
    @jsii.member(jsii_name="addressFamily")
    def address_family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addressFamily"))

    @address_family.setter
    def address_family(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressFamily", value)

    @builtins.property
    @jsii.member(jsii_name="amazonAddress")
    def amazon_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amazonAddress"))

    @amazon_address.setter
    def amazon_address(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonAddress", value)

    @builtins.property
    @jsii.member(jsii_name="bgpAsn")
    def bgp_asn(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bgpAsn"))

    @bgp_asn.setter
    def bgp_asn(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgpAsn", value)

    @builtins.property
    @jsii.member(jsii_name="bgpAuthKey")
    def bgp_auth_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bgpAuthKey"))

    @bgp_auth_key.setter
    def bgp_auth_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgpAuthKey", value)

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value)

    @builtins.property
    @jsii.member(jsii_name="customerAddress")
    def customer_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerAddress"))

    @customer_address.setter
    def customer_address(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerAddress", value)

    @builtins.property
    @jsii.member(jsii_name="dxGatewayId")
    def dx_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dxGatewayId"))

    @dx_gateway_id.setter
    def dx_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dxGatewayId", value)

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
    @jsii.member(jsii_name="mtu")
    def mtu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mtu"))

    @mtu.setter
    def mtu(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mtu", value)

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
    @jsii.member(jsii_name="sitelinkEnabled")
    def sitelink_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sitelinkEnabled"))

    @sitelink_enabled.setter
    def sitelink_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sitelinkEnabled", value)

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
    @jsii.member(jsii_name="vlan")
    def vlan(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vlan"))

    @vlan.setter
    def vlan(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vlan", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dxTransitVirtualInterface.DxTransitVirtualInterfaceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "address_family": "addressFamily",
        "bgp_asn": "bgpAsn",
        "connection_id": "connectionId",
        "dx_gateway_id": "dxGatewayId",
        "name": "name",
        "vlan": "vlan",
        "amazon_address": "amazonAddress",
        "bgp_auth_key": "bgpAuthKey",
        "customer_address": "customerAddress",
        "id": "id",
        "mtu": "mtu",
        "sitelink_enabled": "sitelinkEnabled",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class DxTransitVirtualInterfaceConfig(cdktf.TerraformMetaArguments):
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
        address_family: builtins.str,
        bgp_asn: jsii.Number,
        connection_id: builtins.str,
        dx_gateway_id: builtins.str,
        name: builtins.str,
        vlan: jsii.Number,
        amazon_address: typing.Optional[builtins.str] = None,
        bgp_auth_key: typing.Optional[builtins.str] = None,
        customer_address: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mtu: typing.Optional[jsii.Number] = None,
        sitelink_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DxTransitVirtualInterfaceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param address_family: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#address_family DxTransitVirtualInterface#address_family}.
        :param bgp_asn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#bgp_asn DxTransitVirtualInterface#bgp_asn}.
        :param connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#connection_id DxTransitVirtualInterface#connection_id}.
        :param dx_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#dx_gateway_id DxTransitVirtualInterface#dx_gateway_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#name DxTransitVirtualInterface#name}.
        :param vlan: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#vlan DxTransitVirtualInterface#vlan}.
        :param amazon_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#amazon_address DxTransitVirtualInterface#amazon_address}.
        :param bgp_auth_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#bgp_auth_key DxTransitVirtualInterface#bgp_auth_key}.
        :param customer_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#customer_address DxTransitVirtualInterface#customer_address}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#id DxTransitVirtualInterface#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mtu: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#mtu DxTransitVirtualInterface#mtu}.
        :param sitelink_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#sitelink_enabled DxTransitVirtualInterface#sitelink_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#tags DxTransitVirtualInterface#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#tags_all DxTransitVirtualInterface#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#timeouts DxTransitVirtualInterface#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DxTransitVirtualInterfaceTimeouts(**timeouts)
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
                address_family: builtins.str,
                bgp_asn: jsii.Number,
                connection_id: builtins.str,
                dx_gateway_id: builtins.str,
                name: builtins.str,
                vlan: jsii.Number,
                amazon_address: typing.Optional[builtins.str] = None,
                bgp_auth_key: typing.Optional[builtins.str] = None,
                customer_address: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                mtu: typing.Optional[jsii.Number] = None,
                sitelink_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[DxTransitVirtualInterfaceTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument address_family", value=address_family, expected_type=type_hints["address_family"])
            check_type(argname="argument bgp_asn", value=bgp_asn, expected_type=type_hints["bgp_asn"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument dx_gateway_id", value=dx_gateway_id, expected_type=type_hints["dx_gateway_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument vlan", value=vlan, expected_type=type_hints["vlan"])
            check_type(argname="argument amazon_address", value=amazon_address, expected_type=type_hints["amazon_address"])
            check_type(argname="argument bgp_auth_key", value=bgp_auth_key, expected_type=type_hints["bgp_auth_key"])
            check_type(argname="argument customer_address", value=customer_address, expected_type=type_hints["customer_address"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
            check_type(argname="argument sitelink_enabled", value=sitelink_enabled, expected_type=type_hints["sitelink_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "address_family": address_family,
            "bgp_asn": bgp_asn,
            "connection_id": connection_id,
            "dx_gateway_id": dx_gateway_id,
            "name": name,
            "vlan": vlan,
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
        if amazon_address is not None:
            self._values["amazon_address"] = amazon_address
        if bgp_auth_key is not None:
            self._values["bgp_auth_key"] = bgp_auth_key
        if customer_address is not None:
            self._values["customer_address"] = customer_address
        if id is not None:
            self._values["id"] = id
        if mtu is not None:
            self._values["mtu"] = mtu
        if sitelink_enabled is not None:
            self._values["sitelink_enabled"] = sitelink_enabled
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def address_family(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#address_family DxTransitVirtualInterface#address_family}.'''
        result = self._values.get("address_family")
        assert result is not None, "Required property 'address_family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bgp_asn(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#bgp_asn DxTransitVirtualInterface#bgp_asn}.'''
        result = self._values.get("bgp_asn")
        assert result is not None, "Required property 'bgp_asn' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def connection_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#connection_id DxTransitVirtualInterface#connection_id}.'''
        result = self._values.get("connection_id")
        assert result is not None, "Required property 'connection_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dx_gateway_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#dx_gateway_id DxTransitVirtualInterface#dx_gateway_id}.'''
        result = self._values.get("dx_gateway_id")
        assert result is not None, "Required property 'dx_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#name DxTransitVirtualInterface#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vlan(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#vlan DxTransitVirtualInterface#vlan}.'''
        result = self._values.get("vlan")
        assert result is not None, "Required property 'vlan' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def amazon_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#amazon_address DxTransitVirtualInterface#amazon_address}.'''
        result = self._values.get("amazon_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bgp_auth_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#bgp_auth_key DxTransitVirtualInterface#bgp_auth_key}.'''
        result = self._values.get("bgp_auth_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#customer_address DxTransitVirtualInterface#customer_address}.'''
        result = self._values.get("customer_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#id DxTransitVirtualInterface#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mtu(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#mtu DxTransitVirtualInterface#mtu}.'''
        result = self._values.get("mtu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sitelink_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#sitelink_enabled DxTransitVirtualInterface#sitelink_enabled}.'''
        result = self._values.get("sitelink_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#tags DxTransitVirtualInterface#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#tags_all DxTransitVirtualInterface#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DxTransitVirtualInterfaceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#timeouts DxTransitVirtualInterface#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DxTransitVirtualInterfaceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DxTransitVirtualInterfaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dxTransitVirtualInterface.DxTransitVirtualInterfaceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DxTransitVirtualInterfaceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#create DxTransitVirtualInterface#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#delete DxTransitVirtualInterface#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#update DxTransitVirtualInterface#update}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#create DxTransitVirtualInterface#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#delete DxTransitVirtualInterface#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/dx_transit_virtual_interface#update DxTransitVirtualInterface#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DxTransitVirtualInterfaceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DxTransitVirtualInterfaceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dxTransitVirtualInterface.DxTransitVirtualInterfaceTimeoutsOutputReference",
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

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DxTransitVirtualInterfaceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DxTransitVirtualInterfaceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DxTransitVirtualInterfaceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DxTransitVirtualInterfaceTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DxTransitVirtualInterface",
    "DxTransitVirtualInterfaceConfig",
    "DxTransitVirtualInterfaceTimeouts",
    "DxTransitVirtualInterfaceTimeoutsOutputReference",
]

publication.publish()
