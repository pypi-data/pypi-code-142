'''
# `aws_s3control_multi_region_access_point`

Refer to the Terraform Registory for docs: [`aws_s3control_multi_region_access_point`](https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point).
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


class S3ControlMultiRegionAccessPoint(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point aws_s3control_multi_region_access_point}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        details: typing.Union["S3ControlMultiRegionAccessPointDetails", typing.Dict[str, typing.Any]],
        account_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["S3ControlMultiRegionAccessPointTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point aws_s3control_multi_region_access_point} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param details: details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#details S3ControlMultiRegionAccessPoint#details}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#account_id S3ControlMultiRegionAccessPoint#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#id S3ControlMultiRegionAccessPoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#timeouts S3ControlMultiRegionAccessPoint#timeouts}
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
                details: typing.Union[S3ControlMultiRegionAccessPointDetails, typing.Dict[str, typing.Any]],
                account_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[S3ControlMultiRegionAccessPointTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = S3ControlMultiRegionAccessPointConfig(
            details=details,
            account_id=account_id,
            id=id,
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

    @jsii.member(jsii_name="putDetails")
    def put_details(
        self,
        *,
        name: builtins.str,
        region: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["S3ControlMultiRegionAccessPointDetailsRegion", typing.Dict[str, typing.Any]]]],
        public_access_block: typing.Optional[typing.Union["S3ControlMultiRegionAccessPointDetailsPublicAccessBlock", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#name S3ControlMultiRegionAccessPoint#name}.
        :param region: region block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#region S3ControlMultiRegionAccessPoint#region}
        :param public_access_block: public_access_block block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#public_access_block S3ControlMultiRegionAccessPoint#public_access_block}
        '''
        value = S3ControlMultiRegionAccessPointDetails(
            name=name, region=region, public_access_block=public_access_block
        )

        return typing.cast(None, jsii.invoke(self, "putDetails", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#create S3ControlMultiRegionAccessPoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#delete S3ControlMultiRegionAccessPoint#delete}.
        '''
        value = S3ControlMultiRegionAccessPointTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="alias")
    def alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alias"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="details")
    def details(self) -> "S3ControlMultiRegionAccessPointDetailsOutputReference":
        return typing.cast("S3ControlMultiRegionAccessPointDetailsOutputReference", jsii.get(self, "details"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "S3ControlMultiRegionAccessPointTimeoutsOutputReference":
        return typing.cast("S3ControlMultiRegionAccessPointTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="detailsInput")
    def details_input(
        self,
    ) -> typing.Optional["S3ControlMultiRegionAccessPointDetails"]:
        return typing.cast(typing.Optional["S3ControlMultiRegionAccessPointDetails"], jsii.get(self, "detailsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["S3ControlMultiRegionAccessPointTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["S3ControlMultiRegionAccessPointTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "details": "details",
        "account_id": "accountId",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class S3ControlMultiRegionAccessPointConfig(cdktf.TerraformMetaArguments):
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
        details: typing.Union["S3ControlMultiRegionAccessPointDetails", typing.Dict[str, typing.Any]],
        account_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["S3ControlMultiRegionAccessPointTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param details: details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#details S3ControlMultiRegionAccessPoint#details}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#account_id S3ControlMultiRegionAccessPoint#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#id S3ControlMultiRegionAccessPoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#timeouts S3ControlMultiRegionAccessPoint#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(details, dict):
            details = S3ControlMultiRegionAccessPointDetails(**details)
        if isinstance(timeouts, dict):
            timeouts = S3ControlMultiRegionAccessPointTimeouts(**timeouts)
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
                details: typing.Union[S3ControlMultiRegionAccessPointDetails, typing.Dict[str, typing.Any]],
                account_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[S3ControlMultiRegionAccessPointTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument details", value=details, expected_type=type_hints["details"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "details": details,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if id is not None:
            self._values["id"] = id
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
    def details(self) -> "S3ControlMultiRegionAccessPointDetails":
        '''details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#details S3ControlMultiRegionAccessPoint#details}
        '''
        result = self._values.get("details")
        assert result is not None, "Required property 'details' is missing"
        return typing.cast("S3ControlMultiRegionAccessPointDetails", result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#account_id S3ControlMultiRegionAccessPoint#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#id S3ControlMultiRegionAccessPoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["S3ControlMultiRegionAccessPointTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#timeouts S3ControlMultiRegionAccessPoint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["S3ControlMultiRegionAccessPointTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlMultiRegionAccessPointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointDetails",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "region": "region",
        "public_access_block": "publicAccessBlock",
    },
)
class S3ControlMultiRegionAccessPointDetails:
    def __init__(
        self,
        *,
        name: builtins.str,
        region: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["S3ControlMultiRegionAccessPointDetailsRegion", typing.Dict[str, typing.Any]]]],
        public_access_block: typing.Optional[typing.Union["S3ControlMultiRegionAccessPointDetailsPublicAccessBlock", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#name S3ControlMultiRegionAccessPoint#name}.
        :param region: region block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#region S3ControlMultiRegionAccessPoint#region}
        :param public_access_block: public_access_block block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#public_access_block S3ControlMultiRegionAccessPoint#public_access_block}
        '''
        if isinstance(public_access_block, dict):
            public_access_block = S3ControlMultiRegionAccessPointDetailsPublicAccessBlock(**public_access_block)
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                region: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[S3ControlMultiRegionAccessPointDetailsRegion, typing.Dict[str, typing.Any]]]],
                public_access_block: typing.Optional[typing.Union[S3ControlMultiRegionAccessPointDetailsPublicAccessBlock, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument public_access_block", value=public_access_block, expected_type=type_hints["public_access_block"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "region": region,
        }
        if public_access_block is not None:
            self._values["public_access_block"] = public_access_block

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#name S3ControlMultiRegionAccessPoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["S3ControlMultiRegionAccessPointDetailsRegion"]]:
        '''region block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#region S3ControlMultiRegionAccessPoint#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["S3ControlMultiRegionAccessPointDetailsRegion"]], result)

    @builtins.property
    def public_access_block(
        self,
    ) -> typing.Optional["S3ControlMultiRegionAccessPointDetailsPublicAccessBlock"]:
        '''public_access_block block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#public_access_block S3ControlMultiRegionAccessPoint#public_access_block}
        '''
        result = self._values.get("public_access_block")
        return typing.cast(typing.Optional["S3ControlMultiRegionAccessPointDetailsPublicAccessBlock"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlMultiRegionAccessPointDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlMultiRegionAccessPointDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointDetailsOutputReference",
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

    @jsii.member(jsii_name="putPublicAccessBlock")
    def put_public_access_block(
        self,
        *,
        block_public_acls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        block_public_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ignore_public_acls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restrict_public_buckets: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param block_public_acls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#block_public_acls S3ControlMultiRegionAccessPoint#block_public_acls}.
        :param block_public_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#block_public_policy S3ControlMultiRegionAccessPoint#block_public_policy}.
        :param ignore_public_acls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#ignore_public_acls S3ControlMultiRegionAccessPoint#ignore_public_acls}.
        :param restrict_public_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#restrict_public_buckets S3ControlMultiRegionAccessPoint#restrict_public_buckets}.
        '''
        value = S3ControlMultiRegionAccessPointDetailsPublicAccessBlock(
            block_public_acls=block_public_acls,
            block_public_policy=block_public_policy,
            ignore_public_acls=ignore_public_acls,
            restrict_public_buckets=restrict_public_buckets,
        )

        return typing.cast(None, jsii.invoke(self, "putPublicAccessBlock", [value]))

    @jsii.member(jsii_name="putRegion")
    def put_region(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["S3ControlMultiRegionAccessPointDetailsRegion", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[S3ControlMultiRegionAccessPointDetailsRegion, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegion", [value]))

    @jsii.member(jsii_name="resetPublicAccessBlock")
    def reset_public_access_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicAccessBlock", []))

    @builtins.property
    @jsii.member(jsii_name="publicAccessBlock")
    def public_access_block(
        self,
    ) -> "S3ControlMultiRegionAccessPointDetailsPublicAccessBlockOutputReference":
        return typing.cast("S3ControlMultiRegionAccessPointDetailsPublicAccessBlockOutputReference", jsii.get(self, "publicAccessBlock"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> "S3ControlMultiRegionAccessPointDetailsRegionList":
        return typing.cast("S3ControlMultiRegionAccessPointDetailsRegionList", jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicAccessBlockInput")
    def public_access_block_input(
        self,
    ) -> typing.Optional["S3ControlMultiRegionAccessPointDetailsPublicAccessBlock"]:
        return typing.cast(typing.Optional["S3ControlMultiRegionAccessPointDetailsPublicAccessBlock"], jsii.get(self, "publicAccessBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["S3ControlMultiRegionAccessPointDetailsRegion"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["S3ControlMultiRegionAccessPointDetailsRegion"]]], jsii.get(self, "regionInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3ControlMultiRegionAccessPointDetails]:
        return typing.cast(typing.Optional[S3ControlMultiRegionAccessPointDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlMultiRegionAccessPointDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlMultiRegionAccessPointDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointDetailsPublicAccessBlock",
    jsii_struct_bases=[],
    name_mapping={
        "block_public_acls": "blockPublicAcls",
        "block_public_policy": "blockPublicPolicy",
        "ignore_public_acls": "ignorePublicAcls",
        "restrict_public_buckets": "restrictPublicBuckets",
    },
)
class S3ControlMultiRegionAccessPointDetailsPublicAccessBlock:
    def __init__(
        self,
        *,
        block_public_acls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        block_public_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ignore_public_acls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restrict_public_buckets: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param block_public_acls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#block_public_acls S3ControlMultiRegionAccessPoint#block_public_acls}.
        :param block_public_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#block_public_policy S3ControlMultiRegionAccessPoint#block_public_policy}.
        :param ignore_public_acls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#ignore_public_acls S3ControlMultiRegionAccessPoint#ignore_public_acls}.
        :param restrict_public_buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#restrict_public_buckets S3ControlMultiRegionAccessPoint#restrict_public_buckets}.
        '''
        if __debug__:
            def stub(
                *,
                block_public_acls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                block_public_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                ignore_public_acls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                restrict_public_buckets: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument block_public_acls", value=block_public_acls, expected_type=type_hints["block_public_acls"])
            check_type(argname="argument block_public_policy", value=block_public_policy, expected_type=type_hints["block_public_policy"])
            check_type(argname="argument ignore_public_acls", value=ignore_public_acls, expected_type=type_hints["ignore_public_acls"])
            check_type(argname="argument restrict_public_buckets", value=restrict_public_buckets, expected_type=type_hints["restrict_public_buckets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if block_public_acls is not None:
            self._values["block_public_acls"] = block_public_acls
        if block_public_policy is not None:
            self._values["block_public_policy"] = block_public_policy
        if ignore_public_acls is not None:
            self._values["ignore_public_acls"] = ignore_public_acls
        if restrict_public_buckets is not None:
            self._values["restrict_public_buckets"] = restrict_public_buckets

    @builtins.property
    def block_public_acls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#block_public_acls S3ControlMultiRegionAccessPoint#block_public_acls}.'''
        result = self._values.get("block_public_acls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def block_public_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#block_public_policy S3ControlMultiRegionAccessPoint#block_public_policy}.'''
        result = self._values.get("block_public_policy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ignore_public_acls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#ignore_public_acls S3ControlMultiRegionAccessPoint#ignore_public_acls}.'''
        result = self._values.get("ignore_public_acls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def restrict_public_buckets(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#restrict_public_buckets S3ControlMultiRegionAccessPoint#restrict_public_buckets}.'''
        result = self._values.get("restrict_public_buckets")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlMultiRegionAccessPointDetailsPublicAccessBlock(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlMultiRegionAccessPointDetailsPublicAccessBlockOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointDetailsPublicAccessBlockOutputReference",
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

    @jsii.member(jsii_name="resetBlockPublicAcls")
    def reset_block_public_acls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockPublicAcls", []))

    @jsii.member(jsii_name="resetBlockPublicPolicy")
    def reset_block_public_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockPublicPolicy", []))

    @jsii.member(jsii_name="resetIgnorePublicAcls")
    def reset_ignore_public_acls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnorePublicAcls", []))

    @jsii.member(jsii_name="resetRestrictPublicBuckets")
    def reset_restrict_public_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictPublicBuckets", []))

    @builtins.property
    @jsii.member(jsii_name="blockPublicAclsInput")
    def block_public_acls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blockPublicAclsInput"))

    @builtins.property
    @jsii.member(jsii_name="blockPublicPolicyInput")
    def block_public_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blockPublicPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="ignorePublicAclsInput")
    def ignore_public_acls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignorePublicAclsInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictPublicBucketsInput")
    def restrict_public_buckets_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "restrictPublicBucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="blockPublicAcls")
    def block_public_acls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "blockPublicAcls"))

    @block_public_acls.setter
    def block_public_acls(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockPublicAcls", value)

    @builtins.property
    @jsii.member(jsii_name="blockPublicPolicy")
    def block_public_policy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "blockPublicPolicy"))

    @block_public_policy.setter
    def block_public_policy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockPublicPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="ignorePublicAcls")
    def ignore_public_acls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignorePublicAcls"))

    @ignore_public_acls.setter
    def ignore_public_acls(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignorePublicAcls", value)

    @builtins.property
    @jsii.member(jsii_name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "restrictPublicBuckets"))

    @restrict_public_buckets.setter
    def restrict_public_buckets(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictPublicBuckets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlMultiRegionAccessPointDetailsPublicAccessBlock]:
        return typing.cast(typing.Optional[S3ControlMultiRegionAccessPointDetailsPublicAccessBlock], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlMultiRegionAccessPointDetailsPublicAccessBlock],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlMultiRegionAccessPointDetailsPublicAccessBlock],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointDetailsRegion",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket"},
)
class S3ControlMultiRegionAccessPointDetailsRegion:
    def __init__(self, *, bucket: builtins.str) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#bucket S3ControlMultiRegionAccessPoint#bucket}.
        '''
        if __debug__:
            def stub(*, bucket: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#bucket S3ControlMultiRegionAccessPoint#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlMultiRegionAccessPointDetailsRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlMultiRegionAccessPointDetailsRegionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointDetailsRegionList",
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
    def get(
        self,
        index: jsii.Number,
    ) -> "S3ControlMultiRegionAccessPointDetailsRegionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3ControlMultiRegionAccessPointDetailsRegionOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[S3ControlMultiRegionAccessPointDetailsRegion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[S3ControlMultiRegionAccessPointDetailsRegion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[S3ControlMultiRegionAccessPointDetailsRegion]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[S3ControlMultiRegionAccessPointDetailsRegion]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlMultiRegionAccessPointDetailsRegionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointDetailsRegionOutputReference",
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
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3ControlMultiRegionAccessPointDetailsRegion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3ControlMultiRegionAccessPointDetailsRegion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3ControlMultiRegionAccessPointDetailsRegion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[S3ControlMultiRegionAccessPointDetailsRegion, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class S3ControlMultiRegionAccessPointTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#create S3ControlMultiRegionAccessPoint#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#delete S3ControlMultiRegionAccessPoint#delete}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#create S3ControlMultiRegionAccessPoint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_multi_region_access_point#delete S3ControlMultiRegionAccessPoint#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlMultiRegionAccessPointTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlMultiRegionAccessPointTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlMultiRegionAccessPoint.S3ControlMultiRegionAccessPointTimeoutsOutputReference",
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

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3ControlMultiRegionAccessPointTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3ControlMultiRegionAccessPointTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3ControlMultiRegionAccessPointTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[S3ControlMultiRegionAccessPointTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3ControlMultiRegionAccessPoint",
    "S3ControlMultiRegionAccessPointConfig",
    "S3ControlMultiRegionAccessPointDetails",
    "S3ControlMultiRegionAccessPointDetailsOutputReference",
    "S3ControlMultiRegionAccessPointDetailsPublicAccessBlock",
    "S3ControlMultiRegionAccessPointDetailsPublicAccessBlockOutputReference",
    "S3ControlMultiRegionAccessPointDetailsRegion",
    "S3ControlMultiRegionAccessPointDetailsRegionList",
    "S3ControlMultiRegionAccessPointDetailsRegionOutputReference",
    "S3ControlMultiRegionAccessPointTimeouts",
    "S3ControlMultiRegionAccessPointTimeoutsOutputReference",
]

publication.publish()
