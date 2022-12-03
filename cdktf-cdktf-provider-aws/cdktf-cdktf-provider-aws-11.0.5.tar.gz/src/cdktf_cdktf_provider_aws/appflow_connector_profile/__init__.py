'''
# `aws_appflow_connector_profile`

Refer to the Terraform Registory for docs: [`aws_appflow_connector_profile`](https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile).
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


class AppflowConnectorProfile(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfile",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile aws_appflow_connector_profile}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        connection_mode: builtins.str,
        connector_profile_config: typing.Union["AppflowConnectorProfileConnectorProfileConfig", typing.Dict[str, typing.Any]],
        connector_type: builtins.str,
        name: builtins.str,
        connector_label: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile aws_appflow_connector_profile} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connection_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connection_mode AppflowConnectorProfile#connection_mode}.
        :param connector_profile_config: connector_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_config AppflowConnectorProfile#connector_profile_config}
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_type AppflowConnectorProfile#connector_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#name AppflowConnectorProfile#name}.
        :param connector_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_label AppflowConnectorProfile#connector_label}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#id AppflowConnectorProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#kms_arn AppflowConnectorProfile#kms_arn}.
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
                connection_mode: builtins.str,
                connector_profile_config: typing.Union[AppflowConnectorProfileConnectorProfileConfig, typing.Dict[str, typing.Any]],
                connector_type: builtins.str,
                name: builtins.str,
                connector_label: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                kms_arn: typing.Optional[builtins.str] = None,
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
        config = AppflowConnectorProfileConfig(
            connection_mode=connection_mode,
            connector_profile_config=connector_profile_config,
            connector_type=connector_type,
            name=name,
            connector_label=connector_label,
            id=id,
            kms_arn=kms_arn,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConnectorProfileConfig")
    def put_connector_profile_config(
        self,
        *,
        connector_profile_credentials: typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials", typing.Dict[str, typing.Any]],
        connector_profile_properties: typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param connector_profile_credentials: connector_profile_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_credentials AppflowConnectorProfile#connector_profile_credentials}
        :param connector_profile_properties: connector_profile_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_properties AppflowConnectorProfile#connector_profile_properties}
        '''
        value = AppflowConnectorProfileConnectorProfileConfig(
            connector_profile_credentials=connector_profile_credentials,
            connector_profile_properties=connector_profile_properties,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectorProfileConfig", [value]))

    @jsii.member(jsii_name="resetConnectorLabel")
    def reset_connector_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectorLabel", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsArn")
    def reset_kms_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsArn", []))

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
    @jsii.member(jsii_name="connectorProfileConfig")
    def connector_profile_config(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigOutputReference", jsii.get(self, "connectorProfileConfig"))

    @builtins.property
    @jsii.member(jsii_name="credentialsArn")
    def credentials_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialsArn"))

    @builtins.property
    @jsii.member(jsii_name="connectionModeInput")
    def connection_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorLabelInput")
    def connector_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileConfigInput")
    def connector_profile_config_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfig"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfig"], jsii.get(self, "connectorProfileConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorTypeInput")
    def connector_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsArnInput")
    def kms_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsArnInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionMode")
    def connection_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionMode"))

    @connection_mode.setter
    def connection_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionMode", value)

    @builtins.property
    @jsii.member(jsii_name="connectorLabel")
    def connector_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorLabel"))

    @connector_label.setter
    def connector_label(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorLabel", value)

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @connector_type.setter
    def connector_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorType", value)

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
    @jsii.member(jsii_name="kmsArn")
    def kms_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsArn"))

    @kms_arn.setter
    def kms_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsArn", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "connection_mode": "connectionMode",
        "connector_profile_config": "connectorProfileConfig",
        "connector_type": "connectorType",
        "name": "name",
        "connector_label": "connectorLabel",
        "id": "id",
        "kms_arn": "kmsArn",
    },
)
class AppflowConnectorProfileConfig(cdktf.TerraformMetaArguments):
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
        connection_mode: builtins.str,
        connector_profile_config: typing.Union["AppflowConnectorProfileConnectorProfileConfig", typing.Dict[str, typing.Any]],
        connector_type: builtins.str,
        name: builtins.str,
        connector_label: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param connection_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connection_mode AppflowConnectorProfile#connection_mode}.
        :param connector_profile_config: connector_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_config AppflowConnectorProfile#connector_profile_config}
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_type AppflowConnectorProfile#connector_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#name AppflowConnectorProfile#name}.
        :param connector_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_label AppflowConnectorProfile#connector_label}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#id AppflowConnectorProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#kms_arn AppflowConnectorProfile#kms_arn}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(connector_profile_config, dict):
            connector_profile_config = AppflowConnectorProfileConnectorProfileConfig(**connector_profile_config)
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
                connection_mode: builtins.str,
                connector_profile_config: typing.Union[AppflowConnectorProfileConnectorProfileConfig, typing.Dict[str, typing.Any]],
                connector_type: builtins.str,
                name: builtins.str,
                connector_label: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                kms_arn: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument connection_mode", value=connection_mode, expected_type=type_hints["connection_mode"])
            check_type(argname="argument connector_profile_config", value=connector_profile_config, expected_type=type_hints["connector_profile_config"])
            check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument connector_label", value=connector_label, expected_type=type_hints["connector_label"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_arn", value=kms_arn, expected_type=type_hints["kms_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_mode": connection_mode,
            "connector_profile_config": connector_profile_config,
            "connector_type": connector_type,
            "name": name,
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
        if connector_label is not None:
            self._values["connector_label"] = connector_label
        if id is not None:
            self._values["id"] = id
        if kms_arn is not None:
            self._values["kms_arn"] = kms_arn

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
    def connection_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connection_mode AppflowConnectorProfile#connection_mode}.'''
        result = self._values.get("connection_mode")
        assert result is not None, "Required property 'connection_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_profile_config(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfig":
        '''connector_profile_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_config AppflowConnectorProfile#connector_profile_config}
        '''
        result = self._values.get("connector_profile_config")
        assert result is not None, "Required property 'connector_profile_config' is missing"
        return typing.cast("AppflowConnectorProfileConnectorProfileConfig", result)

    @builtins.property
    def connector_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_type AppflowConnectorProfile#connector_type}.'''
        result = self._values.get("connector_type")
        assert result is not None, "Required property 'connector_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#name AppflowConnectorProfile#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_label AppflowConnectorProfile#connector_label}.'''
        result = self._values.get("connector_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#id AppflowConnectorProfile#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#kms_arn AppflowConnectorProfile#kms_arn}.'''
        result = self._values.get("kms_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfig",
    jsii_struct_bases=[],
    name_mapping={
        "connector_profile_credentials": "connectorProfileCredentials",
        "connector_profile_properties": "connectorProfileProperties",
    },
)
class AppflowConnectorProfileConnectorProfileConfig:
    def __init__(
        self,
        *,
        connector_profile_credentials: typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials", typing.Dict[str, typing.Any]],
        connector_profile_properties: typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param connector_profile_credentials: connector_profile_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_credentials AppflowConnectorProfile#connector_profile_credentials}
        :param connector_profile_properties: connector_profile_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_properties AppflowConnectorProfile#connector_profile_properties}
        '''
        if isinstance(connector_profile_credentials, dict):
            connector_profile_credentials = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials(**connector_profile_credentials)
        if isinstance(connector_profile_properties, dict):
            connector_profile_properties = AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties(**connector_profile_properties)
        if __debug__:
            def stub(
                *,
                connector_profile_credentials: typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials, typing.Dict[str, typing.Any]],
                connector_profile_properties: typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connector_profile_credentials", value=connector_profile_credentials, expected_type=type_hints["connector_profile_credentials"])
            check_type(argname="argument connector_profile_properties", value=connector_profile_properties, expected_type=type_hints["connector_profile_properties"])
        self._values: typing.Dict[str, typing.Any] = {
            "connector_profile_credentials": connector_profile_credentials,
            "connector_profile_properties": connector_profile_properties,
        }

    @builtins.property
    def connector_profile_credentials(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials":
        '''connector_profile_credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_credentials AppflowConnectorProfile#connector_profile_credentials}
        '''
        result = self._values.get("connector_profile_credentials")
        assert result is not None, "Required property 'connector_profile_credentials' is missing"
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials", result)

    @builtins.property
    def connector_profile_properties(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties":
        '''connector_profile_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#connector_profile_properties AppflowConnectorProfile#connector_profile_properties}
        '''
        result = self._values.get("connector_profile_properties")
        assert result is not None, "Required property 'connector_profile_properties' is missing"
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials",
    jsii_struct_bases=[],
    name_mapping={
        "amplitude": "amplitude",
        "custom_connector": "customConnector",
        "datadog": "datadog",
        "dynatrace": "dynatrace",
        "google_analytics": "googleAnalytics",
        "honeycode": "honeycode",
        "infor_nexus": "inforNexus",
        "marketo": "marketo",
        "redshift": "redshift",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "service_now": "serviceNow",
        "singular": "singular",
        "slack": "slack",
        "snowflake": "snowflake",
        "trendmicro": "trendmicro",
        "veeva": "veeva",
        "zendesk": "zendesk",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials:
    def __init__(
        self,
        *,
        amplitude: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude", typing.Dict[str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector", typing.Dict[str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog", typing.Dict[str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace", typing.Dict[str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics", typing.Dict[str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode", typing.Dict[str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus", typing.Dict[str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo", typing.Dict[str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift", typing.Dict[str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce", typing.Dict[str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData", typing.Dict[str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow", typing.Dict[str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular", typing.Dict[str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack", typing.Dict[str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake", typing.Dict[str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro", typing.Dict[str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva", typing.Dict[str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        if isinstance(amplitude, dict):
            amplitude = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude(**amplitude)
        if isinstance(custom_connector, dict):
            custom_connector = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector(**custom_connector)
        if isinstance(datadog, dict):
            datadog = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog(**datadog)
        if isinstance(dynatrace, dict):
            dynatrace = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace(**dynatrace)
        if isinstance(google_analytics, dict):
            google_analytics = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics(**google_analytics)
        if isinstance(honeycode, dict):
            honeycode = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode(**honeycode)
        if isinstance(infor_nexus, dict):
            infor_nexus = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus(**infor_nexus)
        if isinstance(marketo, dict):
            marketo = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo(**marketo)
        if isinstance(redshift, dict):
            redshift = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift(**redshift)
        if isinstance(salesforce, dict):
            salesforce = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce(**salesforce)
        if isinstance(sapo_data, dict):
            sapo_data = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData(**sapo_data)
        if isinstance(service_now, dict):
            service_now = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow(**service_now)
        if isinstance(singular, dict):
            singular = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular(**singular)
        if isinstance(slack, dict):
            slack = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack(**slack)
        if isinstance(snowflake, dict):
            snowflake = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake(**snowflake)
        if isinstance(trendmicro, dict):
            trendmicro = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro(**trendmicro)
        if isinstance(veeva, dict):
            veeva = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva(**veeva)
        if isinstance(zendesk, dict):
            zendesk = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk(**zendesk)
        if __debug__:
            def stub(
                *,
                amplitude: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude, typing.Dict[str, typing.Any]]] = None,
                custom_connector: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector, typing.Dict[str, typing.Any]]] = None,
                datadog: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog, typing.Dict[str, typing.Any]]] = None,
                dynatrace: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace, typing.Dict[str, typing.Any]]] = None,
                google_analytics: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics, typing.Dict[str, typing.Any]]] = None,
                honeycode: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode, typing.Dict[str, typing.Any]]] = None,
                infor_nexus: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus, typing.Dict[str, typing.Any]]] = None,
                marketo: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo, typing.Dict[str, typing.Any]]] = None,
                redshift: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift, typing.Dict[str, typing.Any]]] = None,
                salesforce: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce, typing.Dict[str, typing.Any]]] = None,
                sapo_data: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData, typing.Dict[str, typing.Any]]] = None,
                service_now: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow, typing.Dict[str, typing.Any]]] = None,
                singular: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular, typing.Dict[str, typing.Any]]] = None,
                slack: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack, typing.Dict[str, typing.Any]]] = None,
                snowflake: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake, typing.Dict[str, typing.Any]]] = None,
                trendmicro: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro, typing.Dict[str, typing.Any]]] = None,
                veeva: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva, typing.Dict[str, typing.Any]]] = None,
                zendesk: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
            check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
            check_type(argname="argument honeycode", value=honeycode, expected_type=type_hints["honeycode"])
            check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
            check_type(argname="argument trendmicro", value=trendmicro, expected_type=type_hints["trendmicro"])
            check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
            check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
        self._values: typing.Dict[str, typing.Any] = {}
        if amplitude is not None:
            self._values["amplitude"] = amplitude
        if custom_connector is not None:
            self._values["custom_connector"] = custom_connector
        if datadog is not None:
            self._values["datadog"] = datadog
        if dynatrace is not None:
            self._values["dynatrace"] = dynatrace
        if google_analytics is not None:
            self._values["google_analytics"] = google_analytics
        if honeycode is not None:
            self._values["honeycode"] = honeycode
        if infor_nexus is not None:
            self._values["infor_nexus"] = infor_nexus
        if marketo is not None:
            self._values["marketo"] = marketo
        if redshift is not None:
            self._values["redshift"] = redshift
        if salesforce is not None:
            self._values["salesforce"] = salesforce
        if sapo_data is not None:
            self._values["sapo_data"] = sapo_data
        if service_now is not None:
            self._values["service_now"] = service_now
        if singular is not None:
            self._values["singular"] = singular
        if slack is not None:
            self._values["slack"] = slack
        if snowflake is not None:
            self._values["snowflake"] = snowflake
        if trendmicro is not None:
            self._values["trendmicro"] = trendmicro
        if veeva is not None:
            self._values["veeva"] = veeva
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def amplitude(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude"]:
        '''amplitude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        '''
        result = self._values.get("amplitude")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude"], result)

    @builtins.property
    def custom_connector(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector"]:
        '''custom_connector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        '''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector"], result)

    @builtins.property
    def datadog(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog"], result)

    @builtins.property
    def dynatrace(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace"]:
        '''dynatrace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        '''
        result = self._values.get("dynatrace")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace"], result)

    @builtins.property
    def google_analytics(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics"]:
        '''google_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        '''
        result = self._values.get("google_analytics")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics"], result)

    @builtins.property
    def honeycode(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode"]:
        '''honeycode block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        '''
        result = self._values.get("honeycode")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode"], result)

    @builtins.property
    def infor_nexus(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus"]:
        '''infor_nexus block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        '''
        result = self._values.get("infor_nexus")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus"], result)

    @builtins.property
    def marketo(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo"]:
        '''marketo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        '''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo"], result)

    @builtins.property
    def redshift(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift"]:
        '''redshift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift"], result)

    @builtins.property
    def salesforce(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce"]:
        '''salesforce block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        '''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce"], result)

    @builtins.property
    def sapo_data(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData"]:
        '''sapo_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        '''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData"], result)

    @builtins.property
    def service_now(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow"]:
        '''service_now block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        '''
        result = self._values.get("service_now")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow"], result)

    @builtins.property
    def singular(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular"]:
        '''singular block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        '''
        result = self._values.get("singular")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular"], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack"], result)

    @builtins.property
    def snowflake(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake"]:
        '''snowflake block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        '''
        result = self._values.get("snowflake")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake"], result)

    @builtins.property
    def trendmicro(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro"]:
        '''trendmicro block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        '''
        result = self._values.get("trendmicro")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro"], result)

    @builtins.property
    def veeva(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva"]:
        '''veeva block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        '''
        result = self._values.get("veeva")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva"], result)

    @builtins.property
    def zendesk(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk"]:
        '''zendesk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "secret_key": "secretKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude:
    def __init__(self, *, api_key: builtins.str, secret_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_key AppflowConnectorProfile#secret_key}.
        '''
        if __debug__:
            def stub(*, api_key: builtins.str, secret_key: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
            "secret_key": secret_key,
        }

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_key AppflowConnectorProfile#secret_key}.'''
        result = self._values.get("secret_key")
        assert result is not None, "Required property 'secret_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference",
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
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "api_key": "apiKey",
        "basic": "basic",
        "custom": "custom",
        "oauth2": "oauth2",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        api_key: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey", typing.Dict[str, typing.Any]]] = None,
        basic: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic", typing.Dict[str, typing.Any]]] = None,
        custom: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom", typing.Dict[str, typing.Any]]] = None,
        oauth2: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#authentication_type AppflowConnectorProfile#authentication_type}.
        :param api_key: api_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}
        :param basic: basic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic AppflowConnectorProfile#basic}
        :param custom: custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom AppflowConnectorProfile#custom}
        :param oauth2: oauth2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2 AppflowConnectorProfile#oauth2}
        '''
        if isinstance(api_key, dict):
            api_key = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey(**api_key)
        if isinstance(basic, dict):
            basic = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic(**basic)
        if isinstance(custom, dict):
            custom = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom(**custom)
        if isinstance(oauth2, dict):
            oauth2 = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2(**oauth2)
        if __debug__:
            def stub(
                *,
                authentication_type: builtins.str,
                api_key: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey, typing.Dict[str, typing.Any]]] = None,
                basic: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic, typing.Dict[str, typing.Any]]] = None,
                custom: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom, typing.Dict[str, typing.Any]]] = None,
                oauth2: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument basic", value=basic, expected_type=type_hints["basic"])
            check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
            check_type(argname="argument oauth2", value=oauth2, expected_type=type_hints["oauth2"])
        self._values: typing.Dict[str, typing.Any] = {
            "authentication_type": authentication_type,
        }
        if api_key is not None:
            self._values["api_key"] = api_key
        if basic is not None:
            self._values["basic"] = basic
        if custom is not None:
            self._values["custom"] = custom
        if oauth2 is not None:
            self._values["oauth2"] = oauth2

    @builtins.property
    def authentication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#authentication_type AppflowConnectorProfile#authentication_type}.'''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_key(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey"]:
        '''api_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}
        '''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey"], result)

    @builtins.property
    def basic(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic"]:
        '''basic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic AppflowConnectorProfile#basic}
        '''
        result = self._values.get("basic")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic"], result)

    @builtins.property
    def custom(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom"]:
        '''custom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom AppflowConnectorProfile#custom}
        '''
        result = self._values.get("custom")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom"], result)

    @builtins.property
    def oauth2(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2"]:
        '''oauth2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2 AppflowConnectorProfile#oauth2}
        '''
        result = self._values.get("oauth2")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "api_secret_key": "apiSecretKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        api_secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param api_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.
        '''
        if __debug__:
            def stub(
                *,
                api_key: builtins.str,
                api_secret_key: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_secret_key", value=api_secret_key, expected_type=type_hints["api_secret_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
        }
        if api_secret_key is not None:
            self._values["api_secret_key"] = api_secret_key

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_secret_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.'''
        result = self._values.get("api_secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference",
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

    @jsii.member(jsii_name="resetApiSecretKey")
    def reset_api_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiSecretKey", []))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiSecretKeyInput")
    def api_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="apiSecretKey")
    def api_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiSecretKey"))

    @api_secret_key.setter
    def api_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            def stub(*, password: builtins.str, username: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference",
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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom",
    jsii_struct_bases=[],
    name_mapping={
        "custom_authentication_type": "customAuthenticationType",
        "credentials_map": "credentialsMap",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom:
    def __init__(
        self,
        *,
        custom_authentication_type: builtins.str,
        credentials_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param custom_authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_authentication_type AppflowConnectorProfile#custom_authentication_type}.
        :param credentials_map: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#credentials_map AppflowConnectorProfile#credentials_map}.
        '''
        if __debug__:
            def stub(
                *,
                custom_authentication_type: builtins.str,
                credentials_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument custom_authentication_type", value=custom_authentication_type, expected_type=type_hints["custom_authentication_type"])
            check_type(argname="argument credentials_map", value=credentials_map, expected_type=type_hints["credentials_map"])
        self._values: typing.Dict[str, typing.Any] = {
            "custom_authentication_type": custom_authentication_type,
        }
        if credentials_map is not None:
            self._values["credentials_map"] = credentials_map

    @builtins.property
    def custom_authentication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_authentication_type AppflowConnectorProfile#custom_authentication_type}.'''
        result = self._values.get("custom_authentication_type")
        assert result is not None, "Required property 'custom_authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credentials_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#credentials_map AppflowConnectorProfile#credentials_map}.'''
        result = self._values.get("credentials_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference",
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

    @jsii.member(jsii_name="resetCredentialsMap")
    def reset_credentials_map(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentialsMap", []))

    @builtins.property
    @jsii.member(jsii_name="credentialsMapInput")
    def credentials_map_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "credentialsMapInput"))

    @builtins.property
    @jsii.member(jsii_name="customAuthenticationTypeInput")
    def custom_authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAuthenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsMap")
    def credentials_map(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "credentialsMap"))

    @credentials_map.setter
    def credentials_map(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsMap", value)

    @builtins.property
    @jsii.member(jsii_name="customAuthenticationType")
    def custom_authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customAuthenticationType"))

    @custom_authentication_type.setter
    def custom_authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAuthenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest", typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest(**oauth_request)
        if __debug__:
            def stub(
                *,
                access_token: typing.Optional[builtins.str] = None,
                client_id: typing.Optional[builtins.str] = None,
                client_secret: typing.Optional[builtins.str] = None,
                oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest, typing.Dict[str, typing.Any]]] = None,
                refresh_token: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            def stub(
                *,
                auth_code: typing.Optional[builtins.str] = None,
                redirect_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference",
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

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference",
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

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference",
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

    @jsii.member(jsii_name="putApiKey")
    def put_api_key(
        self,
        *,
        api_key: builtins.str,
        api_secret_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param api_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey(
            api_key=api_key, api_secret_key=api_secret_key
        )

        return typing.cast(None, jsii.invoke(self, "putApiKey", [value]))

    @jsii.member(jsii_name="putBasic")
    def put_basic(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putBasic", [value]))

    @jsii.member(jsii_name="putCustom")
    def put_custom(
        self,
        *,
        custom_authentication_type: builtins.str,
        credentials_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param custom_authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_authentication_type AppflowConnectorProfile#custom_authentication_type}.
        :param credentials_map: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#credentials_map AppflowConnectorProfile#credentials_map}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom(
            custom_authentication_type=custom_authentication_type,
            credentials_map=credentials_map,
        )

        return typing.cast(None, jsii.invoke(self, "putCustom", [value]))

    @jsii.member(jsii_name="putOauth2")
    def put_oauth2(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest, typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2(
            access_token=access_token,
            client_id=client_id,
            client_secret=client_secret,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putOauth2", [value]))

    @jsii.member(jsii_name="resetApiKey")
    def reset_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiKey", []))

    @jsii.member(jsii_name="resetBasic")
    def reset_basic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasic", []))

    @jsii.member(jsii_name="resetCustom")
    def reset_custom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustom", []))

    @jsii.member(jsii_name="resetOauth2")
    def reset_oauth2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth2", []))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference, jsii.get(self, "apiKey"))

    @builtins.property
    @jsii.member(jsii_name="basic")
    def basic(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference, jsii.get(self, "basic"))

    @builtins.property
    @jsii.member(jsii_name="custom")
    def custom(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference, jsii.get(self, "custom"))

    @builtins.property
    @jsii.member(jsii_name="oauth2")
    def oauth2(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference, jsii.get(self, "oauth2"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="basicInput")
    def basic_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic], jsii.get(self, "basicInput"))

    @builtins.property
    @jsii.member(jsii_name="customInput")
    def custom_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom], jsii.get(self, "customInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2Input")
    def oauth2_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2], jsii.get(self, "oauth2Input"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "application_key": "applicationKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog:
    def __init__(self, *, api_key: builtins.str, application_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param application_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_key AppflowConnectorProfile#application_key}.
        '''
        if __debug__:
            def stub(*, api_key: builtins.str, application_key: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument application_key", value=application_key, expected_type=type_hints["application_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
            "application_key": application_key,
        }

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_key AppflowConnectorProfile#application_key}.'''
        result = self._values.get("application_key")
        assert result is not None, "Required property 'application_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference",
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
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationKeyInput")
    def application_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="applicationKey")
    def application_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationKey"))

    @application_key.setter
    def application_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace",
    jsii_struct_bases=[],
    name_mapping={"api_token": "apiToken"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace:
    def __init__(self, *, api_token: builtins.str) -> None:
        '''
        :param api_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_token AppflowConnectorProfile#api_token}.
        '''
        if __debug__:
            def stub(*, api_token: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument api_token", value=api_token, expected_type=type_hints["api_token"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_token": api_token,
        }

    @builtins.property
    def api_token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_token AppflowConnectorProfile#api_token}.'''
        result = self._values.get("api_token")
        assert result is not None, "Required property 'api_token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference",
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
    @jsii.member(jsii_name="apiTokenInput")
    def api_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="apiToken")
    def api_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiToken"))

    @api_token.setter
    def api_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest", typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest(**oauth_request)
        if __debug__:
            def stub(
                *,
                client_id: builtins.str,
                client_secret: builtins.str,
                access_token: typing.Optional[builtins.str] = None,
                oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest, typing.Dict[str, typing.Any]]] = None,
                refresh_token: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            def stub(
                *,
                auth_code: typing.Optional[builtins.str] = None,
                redirect_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference",
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

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference",
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

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest", typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest(**oauth_request)
        if __debug__:
            def stub(
                *,
                access_token: typing.Optional[builtins.str] = None,
                oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest, typing.Dict[str, typing.Any]]] = None,
                refresh_token: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            def stub(
                *,
                auth_code: typing.Optional[builtins.str] = None,
                redirect_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference",
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

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference",
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

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus",
    jsii_struct_bases=[],
    name_mapping={
        "access_key_id": "accessKeyId",
        "datakey": "datakey",
        "secret_access_key": "secretAccessKey",
        "user_id": "userId",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus:
    def __init__(
        self,
        *,
        access_key_id: builtins.str,
        datakey: builtins.str,
        secret_access_key: builtins.str,
        user_id: builtins.str,
    ) -> None:
        '''
        :param access_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_key_id AppflowConnectorProfile#access_key_id}.
        :param datakey: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datakey AppflowConnectorProfile#datakey}.
        :param secret_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_access_key AppflowConnectorProfile#secret_access_key}.
        :param user_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#user_id AppflowConnectorProfile#user_id}.
        '''
        if __debug__:
            def stub(
                *,
                access_key_id: builtins.str,
                datakey: builtins.str,
                secret_access_key: builtins.str,
                user_id: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument access_key_id", value=access_key_id, expected_type=type_hints["access_key_id"])
            check_type(argname="argument datakey", value=datakey, expected_type=type_hints["datakey"])
            check_type(argname="argument secret_access_key", value=secret_access_key, expected_type=type_hints["secret_access_key"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_key_id": access_key_id,
            "datakey": datakey,
            "secret_access_key": secret_access_key,
            "user_id": user_id,
        }

    @builtins.property
    def access_key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_key_id AppflowConnectorProfile#access_key_id}.'''
        result = self._values.get("access_key_id")
        assert result is not None, "Required property 'access_key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datakey(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datakey AppflowConnectorProfile#datakey}.'''
        result = self._values.get("datakey")
        assert result is not None, "Required property 'datakey' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_access_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_access_key AppflowConnectorProfile#secret_access_key}.'''
        result = self._values.get("secret_access_key")
        assert result is not None, "Required property 'secret_access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#user_id AppflowConnectorProfile#user_id}.'''
        result = self._values.get("user_id")
        assert result is not None, "Required property 'user_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference",
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
    @jsii.member(jsii_name="accessKeyIdInput")
    def access_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datakeyInput")
    def datakey_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datakeyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretAccessKeyInput")
    def secret_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyId")
    def access_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKeyId"))

    @access_key_id.setter
    def access_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="datakey")
    def datakey(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datakey"))

    @datakey.setter
    def datakey(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datakey", value)

    @builtins.property
    @jsii.member(jsii_name="secretAccessKey")
    def secret_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretAccessKey"))

    @secret_access_key.setter
    def secret_access_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest(**oauth_request)
        if __debug__:
            def stub(
                *,
                client_id: builtins.str,
                client_secret: builtins.str,
                access_token: typing.Optional[builtins.str] = None,
                oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            def stub(
                *,
                auth_code: typing.Optional[builtins.str] = None,
                redirect_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference",
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

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference",
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

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference",
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

    @jsii.member(jsii_name="putAmplitude")
    def put_amplitude(self, *, api_key: builtins.str, secret_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_key AppflowConnectorProfile#secret_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude(
            api_key=api_key, secret_key=secret_key
        )

        return typing.cast(None, jsii.invoke(self, "putAmplitude", [value]))

    @jsii.member(jsii_name="putCustomConnector")
    def put_custom_connector(
        self,
        *,
        authentication_type: builtins.str,
        api_key: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey, typing.Dict[str, typing.Any]]] = None,
        basic: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic, typing.Dict[str, typing.Any]]] = None,
        custom: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom, typing.Dict[str, typing.Any]]] = None,
        oauth2: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#authentication_type AppflowConnectorProfile#authentication_type}.
        :param api_key: api_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}
        :param basic: basic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic AppflowConnectorProfile#basic}
        :param custom: custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom AppflowConnectorProfile#custom}
        :param oauth2: oauth2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2 AppflowConnectorProfile#oauth2}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector(
            authentication_type=authentication_type,
            api_key=api_key,
            basic=basic,
            custom=custom,
            oauth2=oauth2,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomConnector", [value]))

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(
        self,
        *,
        api_key: builtins.str,
        application_key: builtins.str,
    ) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        :param application_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_key AppflowConnectorProfile#application_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog(
            api_key=api_key, application_key=application_key
        )

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putDynatrace")
    def put_dynatrace(self, *, api_token: builtins.str) -> None:
        '''
        :param api_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_token AppflowConnectorProfile#api_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace(
            api_token=api_token
        )

        return typing.cast(None, jsii.invoke(self, "putDynatrace", [value]))

    @jsii.member(jsii_name="putGoogleAnalytics")
    def put_google_analytics(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest, typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putGoogleAnalytics", [value]))

    @jsii.member(jsii_name="putHoneycode")
    def put_honeycode(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest, typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode(
            access_token=access_token,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putHoneycode", [value]))

    @jsii.member(jsii_name="putInforNexus")
    def put_infor_nexus(
        self,
        *,
        access_key_id: builtins.str,
        datakey: builtins.str,
        secret_access_key: builtins.str,
        user_id: builtins.str,
    ) -> None:
        '''
        :param access_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_key_id AppflowConnectorProfile#access_key_id}.
        :param datakey: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datakey AppflowConnectorProfile#datakey}.
        :param secret_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#secret_access_key AppflowConnectorProfile#secret_access_key}.
        :param user_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#user_id AppflowConnectorProfile#user_id}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus(
            access_key_id=access_key_id,
            datakey=datakey,
            secret_access_key=secret_access_key,
            user_id=user_id,
        )

        return typing.cast(None, jsii.invoke(self, "putInforNexus", [value]))

    @jsii.member(jsii_name="putMarketo")
    def put_marketo(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
        )

        return typing.cast(None, jsii.invoke(self, "putMarketo", [value]))

    @jsii.member(jsii_name="putRedshift")
    def put_redshift(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putRedshift", [value]))

    @jsii.member(jsii_name="putSalesforce")
    def put_salesforce(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        client_credentials_arn: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest", typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param client_credentials_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_credentials_arn AppflowConnectorProfile#client_credentials_arn}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce(
            access_token=access_token,
            client_credentials_arn=client_credentials_arn,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putSalesforce", [value]))

    @jsii.member(jsii_name="putSapoData")
    def put_sapo_data(
        self,
        *,
        basic_auth_credentials: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials", typing.Dict[str, typing.Any]]] = None,
        oauth_credentials: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param basic_auth_credentials: basic_auth_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic_auth_credentials AppflowConnectorProfile#basic_auth_credentials}
        :param oauth_credentials: oauth_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_credentials AppflowConnectorProfile#oauth_credentials}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData(
            basic_auth_credentials=basic_auth_credentials,
            oauth_credentials=oauth_credentials,
        )

        return typing.cast(None, jsii.invoke(self, "putSapoData", [value]))

    @jsii.member(jsii_name="putServiceNow")
    def put_service_now(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putServiceNow", [value]))

    @jsii.member(jsii_name="putSingular")
    def put_singular(self, *, api_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular(
            api_key=api_key
        )

        return typing.cast(None, jsii.invoke(self, "putSingular", [value]))

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
        )

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="putSnowflake")
    def put_snowflake(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putSnowflake", [value]))

    @jsii.member(jsii_name="putTrendmicro")
    def put_trendmicro(self, *, api_secret_key: builtins.str) -> None:
        '''
        :param api_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro(
            api_secret_key=api_secret_key
        )

        return typing.cast(None, jsii.invoke(self, "putTrendmicro", [value]))

    @jsii.member(jsii_name="putVeeva")
    def put_veeva(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putVeeva", [value]))

    @jsii.member(jsii_name="putZendesk")
    def put_zendesk(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
        )

        return typing.cast(None, jsii.invoke(self, "putZendesk", [value]))

    @jsii.member(jsii_name="resetAmplitude")
    def reset_amplitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmplitude", []))

    @jsii.member(jsii_name="resetCustomConnector")
    def reset_custom_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomConnector", []))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetDynatrace")
    def reset_dynatrace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynatrace", []))

    @jsii.member(jsii_name="resetGoogleAnalytics")
    def reset_google_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleAnalytics", []))

    @jsii.member(jsii_name="resetHoneycode")
    def reset_honeycode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHoneycode", []))

    @jsii.member(jsii_name="resetInforNexus")
    def reset_infor_nexus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInforNexus", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetRedshift")
    def reset_redshift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshift", []))

    @jsii.member(jsii_name="resetSalesforce")
    def reset_salesforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalesforce", []))

    @jsii.member(jsii_name="resetSapoData")
    def reset_sapo_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSapoData", []))

    @jsii.member(jsii_name="resetServiceNow")
    def reset_service_now(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceNow", []))

    @jsii.member(jsii_name="resetSingular")
    def reset_singular(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingular", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetSnowflake")
    def reset_snowflake(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnowflake", []))

    @jsii.member(jsii_name="resetTrendmicro")
    def reset_trendmicro(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrendmicro", []))

    @jsii.member(jsii_name="resetVeeva")
    def reset_veeva(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVeeva", []))

    @jsii.member(jsii_name="resetZendesk")
    def reset_zendesk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZendesk", []))

    @builtins.property
    @jsii.member(jsii_name="amplitude")
    def amplitude(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference, jsii.get(self, "amplitude"))

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference, jsii.get(self, "customConnector"))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="dynatrace")
    def dynatrace(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference, jsii.get(self, "dynatrace"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalytics")
    def google_analytics(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference, jsii.get(self, "googleAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="honeycode")
    def honeycode(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference, jsii.get(self, "honeycode"))

    @builtins.property
    @jsii.member(jsii_name="inforNexus")
    def infor_nexus(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference, jsii.get(self, "inforNexus"))

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference, jsii.get(self, "marketo"))

    @builtins.property
    @jsii.member(jsii_name="redshift")
    def redshift(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference", jsii.get(self, "redshift"))

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference", jsii.get(self, "salesforce"))

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference", jsii.get(self, "sapoData"))

    @builtins.property
    @jsii.member(jsii_name="serviceNow")
    def service_now(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference", jsii.get(self, "serviceNow"))

    @builtins.property
    @jsii.member(jsii_name="singular")
    def singular(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference", jsii.get(self, "singular"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="snowflake")
    def snowflake(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference", jsii.get(self, "snowflake"))

    @builtins.property
    @jsii.member(jsii_name="trendmicro")
    def trendmicro(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference", jsii.get(self, "trendmicro"))

    @builtins.property
    @jsii.member(jsii_name="veeva")
    def veeva(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference", jsii.get(self, "veeva"))

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference", jsii.get(self, "zendesk"))

    @builtins.property
    @jsii.member(jsii_name="amplitudeInput")
    def amplitude_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude], jsii.get(self, "amplitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="dynatraceInput")
    def dynatrace_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace], jsii.get(self, "dynatraceInput"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalyticsInput")
    def google_analytics_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics], jsii.get(self, "googleAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="honeycodeInput")
    def honeycode_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode], jsii.get(self, "honeycodeInput"))

    @builtins.property
    @jsii.member(jsii_name="inforNexusInput")
    def infor_nexus_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus], jsii.get(self, "inforNexusInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftInput")
    def redshift_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift"], jsii.get(self, "redshiftInput"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce"], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData"], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNowInput")
    def service_now_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow"], jsii.get(self, "serviceNowInput"))

    @builtins.property
    @jsii.member(jsii_name="singularInput")
    def singular_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular"], jsii.get(self, "singularInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="snowflakeInput")
    def snowflake_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake"], jsii.get(self, "snowflakeInput"))

    @builtins.property
    @jsii.member(jsii_name="trendmicroInput")
    def trendmicro_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro"], jsii.get(self, "trendmicroInput"))

    @builtins.property
    @jsii.member(jsii_name="veevaInput")
    def veeva_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva"], jsii.get(self, "veevaInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk"], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            def stub(*, password: builtins.str, username: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference",
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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "client_credentials_arn": "clientCredentialsArn",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        client_credentials_arn: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest", typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param client_credentials_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_credentials_arn AppflowConnectorProfile#client_credentials_arn}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest(**oauth_request)
        if __debug__:
            def stub(
                *,
                access_token: typing.Optional[builtins.str] = None,
                client_credentials_arn: typing.Optional[builtins.str] = None,
                oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest, typing.Dict[str, typing.Any]]] = None,
                refresh_token: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument client_credentials_arn", value=client_credentials_arn, expected_type=type_hints["client_credentials_arn"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if client_credentials_arn is not None:
            self._values["client_credentials_arn"] = client_credentials_arn
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_credentials_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_credentials_arn AppflowConnectorProfile#client_credentials_arn}.'''
        result = self._values.get("client_credentials_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            def stub(
                *,
                auth_code: typing.Optional[builtins.str] = None,
                redirect_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference",
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

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference",
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

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetClientCredentialsArn")
    def reset_client_credentials_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCredentialsArn", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCredentialsArnInput")
    def client_credentials_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCredentialsArnInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientCredentialsArn")
    def client_credentials_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCredentialsArn"))

    @client_credentials_arn.setter
    def client_credentials_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCredentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData",
    jsii_struct_bases=[],
    name_mapping={
        "basic_auth_credentials": "basicAuthCredentials",
        "oauth_credentials": "oauthCredentials",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData:
    def __init__(
        self,
        *,
        basic_auth_credentials: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials", typing.Dict[str, typing.Any]]] = None,
        oauth_credentials: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param basic_auth_credentials: basic_auth_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic_auth_credentials AppflowConnectorProfile#basic_auth_credentials}
        :param oauth_credentials: oauth_credentials block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_credentials AppflowConnectorProfile#oauth_credentials}
        '''
        if isinstance(basic_auth_credentials, dict):
            basic_auth_credentials = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials(**basic_auth_credentials)
        if isinstance(oauth_credentials, dict):
            oauth_credentials = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials(**oauth_credentials)
        if __debug__:
            def stub(
                *,
                basic_auth_credentials: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials, typing.Dict[str, typing.Any]]] = None,
                oauth_credentials: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument basic_auth_credentials", value=basic_auth_credentials, expected_type=type_hints["basic_auth_credentials"])
            check_type(argname="argument oauth_credentials", value=oauth_credentials, expected_type=type_hints["oauth_credentials"])
        self._values: typing.Dict[str, typing.Any] = {}
        if basic_auth_credentials is not None:
            self._values["basic_auth_credentials"] = basic_auth_credentials
        if oauth_credentials is not None:
            self._values["oauth_credentials"] = oauth_credentials

    @builtins.property
    def basic_auth_credentials(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials"]:
        '''basic_auth_credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#basic_auth_credentials AppflowConnectorProfile#basic_auth_credentials}
        '''
        result = self._values.get("basic_auth_credentials")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials"], result)

    @builtins.property
    def oauth_credentials(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials"]:
        '''oauth_credentials block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_credentials AppflowConnectorProfile#oauth_credentials}
        '''
        result = self._values.get("oauth_credentials")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            def stub(*, password: builtins.str, username: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference",
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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
        "refresh_token": "refreshToken",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest", typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest(**oauth_request)
        if __debug__:
            def stub(
                *,
                client_id: builtins.str,
                client_secret: builtins.str,
                access_token: typing.Optional[builtins.str] = None,
                oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest, typing.Dict[str, typing.Any]]] = None,
                refresh_token: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest"], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            def stub(
                *,
                auth_code: typing.Optional[builtins.str] = None,
                redirect_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference",
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

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference",
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

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference",
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

    @jsii.member(jsii_name="putBasicAuthCredentials")
    def put_basic_auth_credentials(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putBasicAuthCredentials", [value]))

    @jsii.member(jsii_name="putOauthCredentials")
    def put_oauth_credentials(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest, typing.Dict[str, typing.Any]]] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#refresh_token AppflowConnectorProfile#refresh_token}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            oauth_request=oauth_request,
            refresh_token=refresh_token,
        )

        return typing.cast(None, jsii.invoke(self, "putOauthCredentials", [value]))

    @jsii.member(jsii_name="resetBasicAuthCredentials")
    def reset_basic_auth_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthCredentials", []))

    @jsii.member(jsii_name="resetOauthCredentials")
    def reset_oauth_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthCredentials", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuthCredentials")
    def basic_auth_credentials(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference, jsii.get(self, "basicAuthCredentials"))

    @builtins.property
    @jsii.member(jsii_name="oauthCredentials")
    def oauth_credentials(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference, jsii.get(self, "oauthCredentials"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthCredentialsInput")
    def basic_auth_credentials_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials], jsii.get(self, "basicAuthCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthCredentialsInput")
    def oauth_credentials_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials], jsii.get(self, "oauthCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            def stub(*, password: builtins.str, username: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference",
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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular:
    def __init__(self, *, api_key: builtins.str) -> None:
        '''
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.
        '''
        if __debug__:
            def stub(*, api_key: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
        }

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_key AppflowConnectorProfile#api_key}.'''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference",
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
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest(**oauth_request)
        if __debug__:
            def stub(
                *,
                client_id: builtins.str,
                client_secret: builtins.str,
                access_token: typing.Optional[builtins.str] = None,
                oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            def stub(
                *,
                auth_code: typing.Optional[builtins.str] = None,
                redirect_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference",
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

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference",
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

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            def stub(*, password: builtins.str, username: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference",
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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro",
    jsii_struct_bases=[],
    name_mapping={"api_secret_key": "apiSecretKey"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro:
    def __init__(self, *, api_secret_key: builtins.str) -> None:
        '''
        :param api_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.
        '''
        if __debug__:
            def stub(*, api_secret_key: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument api_secret_key", value=api_secret_key, expected_type=type_hints["api_secret_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_secret_key": api_secret_key,
        }

    @builtins.property
    def api_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#api_secret_key AppflowConnectorProfile#api_secret_key}.'''
        result = self._values.get("api_secret_key")
        assert result is not None, "Required property 'api_secret_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference",
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
    @jsii.member(jsii_name="apiSecretKeyInput")
    def api_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiSecretKey")
    def api_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiSecretKey"))

    @api_secret_key.setter
    def api_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.
        '''
        if __debug__:
            def stub(*, password: builtins.str, username: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#password AppflowConnectorProfile#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#username AppflowConnectorProfile#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference",
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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "access_token": "accessToken",
        "oauth_request": "oauthRequest",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        oauth_request: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.
        :param oauth_request: oauth_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        if isinstance(oauth_request, dict):
            oauth_request = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest(**oauth_request)
        if __debug__:
            def stub(
                *,
                client_id: builtins.str,
                client_secret: builtins.str,
                access_token: typing.Optional[builtins.str] = None,
                oauth_request: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument oauth_request", value=oauth_request, expected_type=type_hints["oauth_request"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if access_token is not None:
            self._values["access_token"] = access_token
        if oauth_request is not None:
            self._values["oauth_request"] = oauth_request

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_id AppflowConnectorProfile#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_secret AppflowConnectorProfile#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#access_token AppflowConnectorProfile#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_request(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest"]:
        '''oauth_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_request AppflowConnectorProfile#oauth_request}
        '''
        result = self._values.get("oauth_request")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest",
    jsii_struct_bases=[],
    name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest:
    def __init__(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        if __debug__:
            def stub(
                *,
                auth_code: typing.Optional[builtins.str] = None,
                redirect_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auth_code is not None:
            self._values["auth_code"] = auth_code
        if redirect_uri is not None:
            self._values["redirect_uri"] = redirect_uri

    @builtins.property
    def auth_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.'''
        result = self._values.get("auth_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.'''
        result = self._values.get("redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference",
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

    @jsii.member(jsii_name="resetAuthCode")
    def reset_auth_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthCode", []))

    @jsii.member(jsii_name="resetRedirectUri")
    def reset_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectUri", []))

    @builtins.property
    @jsii.member(jsii_name="authCodeInput")
    def auth_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectUriInput")
    def redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="authCode")
    def auth_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCode"))

    @auth_code.setter
    def auth_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCode", value)

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @redirect_uri.setter
    def redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference",
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

    @jsii.member(jsii_name="putOauthRequest")
    def put_oauth_request(
        self,
        *,
        auth_code: typing.Optional[builtins.str] = None,
        redirect_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code AppflowConnectorProfile#auth_code}.
        :param redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redirect_uri AppflowConnectorProfile#redirect_uri}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest(
            auth_code=auth_code, redirect_uri=redirect_uri
        )

        return typing.cast(None, jsii.invoke(self, "putOauthRequest", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetOauthRequest")
    def reset_oauth_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthRequest", []))

    @builtins.property
    @jsii.member(jsii_name="oauthRequest")
    def oauth_request(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference, jsii.get(self, "oauthRequest"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthRequestInput")
    def oauth_request_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest], jsii.get(self, "oauthRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties",
    jsii_struct_bases=[],
    name_mapping={
        "amplitude": "amplitude",
        "custom_connector": "customConnector",
        "datadog": "datadog",
        "dynatrace": "dynatrace",
        "google_analytics": "googleAnalytics",
        "honeycode": "honeycode",
        "infor_nexus": "inforNexus",
        "marketo": "marketo",
        "redshift": "redshift",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "service_now": "serviceNow",
        "singular": "singular",
        "slack": "slack",
        "snowflake": "snowflake",
        "trendmicro": "trendmicro",
        "veeva": "veeva",
        "zendesk": "zendesk",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties:
    def __init__(
        self,
        *,
        amplitude: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude", typing.Dict[str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector", typing.Dict[str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog", typing.Dict[str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace", typing.Dict[str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics", typing.Dict[str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode", typing.Dict[str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus", typing.Dict[str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo", typing.Dict[str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift", typing.Dict[str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce", typing.Dict[str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData", typing.Dict[str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow", typing.Dict[str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular", typing.Dict[str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack", typing.Dict[str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake", typing.Dict[str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro", typing.Dict[str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva", typing.Dict[str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        if isinstance(amplitude, dict):
            amplitude = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude(**amplitude)
        if isinstance(custom_connector, dict):
            custom_connector = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector(**custom_connector)
        if isinstance(datadog, dict):
            datadog = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog(**datadog)
        if isinstance(dynatrace, dict):
            dynatrace = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace(**dynatrace)
        if isinstance(google_analytics, dict):
            google_analytics = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics(**google_analytics)
        if isinstance(honeycode, dict):
            honeycode = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode(**honeycode)
        if isinstance(infor_nexus, dict):
            infor_nexus = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus(**infor_nexus)
        if isinstance(marketo, dict):
            marketo = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo(**marketo)
        if isinstance(redshift, dict):
            redshift = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift(**redshift)
        if isinstance(salesforce, dict):
            salesforce = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce(**salesforce)
        if isinstance(sapo_data, dict):
            sapo_data = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData(**sapo_data)
        if isinstance(service_now, dict):
            service_now = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow(**service_now)
        if isinstance(singular, dict):
            singular = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular(**singular)
        if isinstance(slack, dict):
            slack = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack(**slack)
        if isinstance(snowflake, dict):
            snowflake = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake(**snowflake)
        if isinstance(trendmicro, dict):
            trendmicro = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro(**trendmicro)
        if isinstance(veeva, dict):
            veeva = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva(**veeva)
        if isinstance(zendesk, dict):
            zendesk = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk(**zendesk)
        if __debug__:
            def stub(
                *,
                amplitude: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude, typing.Dict[str, typing.Any]]] = None,
                custom_connector: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector, typing.Dict[str, typing.Any]]] = None,
                datadog: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog, typing.Dict[str, typing.Any]]] = None,
                dynatrace: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace, typing.Dict[str, typing.Any]]] = None,
                google_analytics: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics, typing.Dict[str, typing.Any]]] = None,
                honeycode: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode, typing.Dict[str, typing.Any]]] = None,
                infor_nexus: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus, typing.Dict[str, typing.Any]]] = None,
                marketo: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo, typing.Dict[str, typing.Any]]] = None,
                redshift: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift, typing.Dict[str, typing.Any]]] = None,
                salesforce: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce, typing.Dict[str, typing.Any]]] = None,
                sapo_data: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData, typing.Dict[str, typing.Any]]] = None,
                service_now: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow, typing.Dict[str, typing.Any]]] = None,
                singular: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular, typing.Dict[str, typing.Any]]] = None,
                slack: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack, typing.Dict[str, typing.Any]]] = None,
                snowflake: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake, typing.Dict[str, typing.Any]]] = None,
                trendmicro: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro, typing.Dict[str, typing.Any]]] = None,
                veeva: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva, typing.Dict[str, typing.Any]]] = None,
                zendesk: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
            check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
            check_type(argname="argument honeycode", value=honeycode, expected_type=type_hints["honeycode"])
            check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
            check_type(argname="argument trendmicro", value=trendmicro, expected_type=type_hints["trendmicro"])
            check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
            check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
        self._values: typing.Dict[str, typing.Any] = {}
        if amplitude is not None:
            self._values["amplitude"] = amplitude
        if custom_connector is not None:
            self._values["custom_connector"] = custom_connector
        if datadog is not None:
            self._values["datadog"] = datadog
        if dynatrace is not None:
            self._values["dynatrace"] = dynatrace
        if google_analytics is not None:
            self._values["google_analytics"] = google_analytics
        if honeycode is not None:
            self._values["honeycode"] = honeycode
        if infor_nexus is not None:
            self._values["infor_nexus"] = infor_nexus
        if marketo is not None:
            self._values["marketo"] = marketo
        if redshift is not None:
            self._values["redshift"] = redshift
        if salesforce is not None:
            self._values["salesforce"] = salesforce
        if sapo_data is not None:
            self._values["sapo_data"] = sapo_data
        if service_now is not None:
            self._values["service_now"] = service_now
        if singular is not None:
            self._values["singular"] = singular
        if slack is not None:
            self._values["slack"] = slack
        if snowflake is not None:
            self._values["snowflake"] = snowflake
        if trendmicro is not None:
            self._values["trendmicro"] = trendmicro
        if veeva is not None:
            self._values["veeva"] = veeva
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def amplitude(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude"]:
        '''amplitude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        '''
        result = self._values.get("amplitude")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude"], result)

    @builtins.property
    def custom_connector(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector"]:
        '''custom_connector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        '''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector"], result)

    @builtins.property
    def datadog(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog"], result)

    @builtins.property
    def dynatrace(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace"]:
        '''dynatrace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        '''
        result = self._values.get("dynatrace")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace"], result)

    @builtins.property
    def google_analytics(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics"]:
        '''google_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        '''
        result = self._values.get("google_analytics")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics"], result)

    @builtins.property
    def honeycode(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode"]:
        '''honeycode block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        '''
        result = self._values.get("honeycode")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode"], result)

    @builtins.property
    def infor_nexus(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus"]:
        '''infor_nexus block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        '''
        result = self._values.get("infor_nexus")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus"], result)

    @builtins.property
    def marketo(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo"]:
        '''marketo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        '''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo"], result)

    @builtins.property
    def redshift(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift"]:
        '''redshift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift"], result)

    @builtins.property
    def salesforce(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce"]:
        '''salesforce block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        '''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce"], result)

    @builtins.property
    def sapo_data(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData"]:
        '''sapo_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        '''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData"], result)

    @builtins.property
    def service_now(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow"]:
        '''service_now block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        '''
        result = self._values.get("service_now")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow"], result)

    @builtins.property
    def singular(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular"]:
        '''singular block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        '''
        result = self._values.get("singular")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular"], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack"], result)

    @builtins.property
    def snowflake(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake"]:
        '''snowflake block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        '''
        result = self._values.get("snowflake")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake"], result)

    @builtins.property
    def trendmicro(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro"]:
        '''trendmicro block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        '''
        result = self._values.get("trendmicro")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro"], result)

    @builtins.property
    def veeva(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva"]:
        '''veeva block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        '''
        result = self._values.get("veeva")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva"], result)

    @builtins.property
    def zendesk(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk"]:
        '''zendesk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector",
    jsii_struct_bases=[],
    name_mapping={
        "oauth2_properties": "oauth2Properties",
        "profile_properties": "profileProperties",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector:
    def __init__(
        self,
        *,
        oauth2_properties: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties", typing.Dict[str, typing.Any]]] = None,
        profile_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param oauth2_properties: oauth2_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_properties AppflowConnectorProfile#oauth2_properties}
        :param profile_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#profile_properties AppflowConnectorProfile#profile_properties}.
        '''
        if isinstance(oauth2_properties, dict):
            oauth2_properties = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties(**oauth2_properties)
        if __debug__:
            def stub(
                *,
                oauth2_properties: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties, typing.Dict[str, typing.Any]]] = None,
                profile_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument oauth2_properties", value=oauth2_properties, expected_type=type_hints["oauth2_properties"])
            check_type(argname="argument profile_properties", value=profile_properties, expected_type=type_hints["profile_properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if oauth2_properties is not None:
            self._values["oauth2_properties"] = oauth2_properties
        if profile_properties is not None:
            self._values["profile_properties"] = profile_properties

    @builtins.property
    def oauth2_properties(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties"]:
        '''oauth2_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_properties AppflowConnectorProfile#oauth2_properties}
        '''
        result = self._values.get("oauth2_properties")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties"], result)

    @builtins.property
    def profile_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#profile_properties AppflowConnectorProfile#profile_properties}.'''
        result = self._values.get("profile_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties",
    jsii_struct_bases=[],
    name_mapping={
        "oauth2_grant_type": "oauth2GrantType",
        "token_url": "tokenUrl",
        "token_url_custom_properties": "tokenUrlCustomProperties",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties:
    def __init__(
        self,
        *,
        oauth2_grant_type: builtins.str,
        token_url: builtins.str,
        token_url_custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param oauth2_grant_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_grant_type AppflowConnectorProfile#oauth2_grant_type}.
        :param token_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.
        :param token_url_custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url_custom_properties AppflowConnectorProfile#token_url_custom_properties}.
        '''
        if __debug__:
            def stub(
                *,
                oauth2_grant_type: builtins.str,
                token_url: builtins.str,
                token_url_custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument oauth2_grant_type", value=oauth2_grant_type, expected_type=type_hints["oauth2_grant_type"])
            check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
            check_type(argname="argument token_url_custom_properties", value=token_url_custom_properties, expected_type=type_hints["token_url_custom_properties"])
        self._values: typing.Dict[str, typing.Any] = {
            "oauth2_grant_type": oauth2_grant_type,
            "token_url": token_url,
        }
        if token_url_custom_properties is not None:
            self._values["token_url_custom_properties"] = token_url_custom_properties

    @builtins.property
    def oauth2_grant_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_grant_type AppflowConnectorProfile#oauth2_grant_type}.'''
        result = self._values.get("oauth2_grant_type")
        assert result is not None, "Required property 'oauth2_grant_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.'''
        result = self._values.get("token_url")
        assert result is not None, "Required property 'token_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_url_custom_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url_custom_properties AppflowConnectorProfile#token_url_custom_properties}.'''
        result = self._values.get("token_url_custom_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference",
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

    @jsii.member(jsii_name="resetTokenUrlCustomProperties")
    def reset_token_url_custom_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenUrlCustomProperties", []))

    @builtins.property
    @jsii.member(jsii_name="oauth2GrantTypeInput")
    def oauth2_grant_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauth2GrantTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUrlCustomPropertiesInput")
    def token_url_custom_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tokenUrlCustomPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUrlInput")
    def token_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2GrantType")
    def oauth2_grant_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2GrantType"))

    @oauth2_grant_type.setter
    def oauth2_grant_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauth2GrantType", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUrl")
    def token_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenUrl"))

    @token_url.setter
    def token_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUrl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUrlCustomProperties")
    def token_url_custom_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tokenUrlCustomProperties"))

    @token_url_custom_properties.setter
    def token_url_custom_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUrlCustomProperties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference",
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

    @jsii.member(jsii_name="putOauth2Properties")
    def put_oauth2_properties(
        self,
        *,
        oauth2_grant_type: builtins.str,
        token_url: builtins.str,
        token_url_custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param oauth2_grant_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_grant_type AppflowConnectorProfile#oauth2_grant_type}.
        :param token_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.
        :param token_url_custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url_custom_properties AppflowConnectorProfile#token_url_custom_properties}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties(
            oauth2_grant_type=oauth2_grant_type,
            token_url=token_url,
            token_url_custom_properties=token_url_custom_properties,
        )

        return typing.cast(None, jsii.invoke(self, "putOauth2Properties", [value]))

    @jsii.member(jsii_name="resetOauth2Properties")
    def reset_oauth2_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth2Properties", []))

    @jsii.member(jsii_name="resetProfileProperties")
    def reset_profile_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfileProperties", []))

    @builtins.property
    @jsii.member(jsii_name="oauth2Properties")
    def oauth2_properties(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference, jsii.get(self, "oauth2Properties"))

    @builtins.property
    @jsii.member(jsii_name="oauth2PropertiesInput")
    def oauth2_properties_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties], jsii.get(self, "oauth2PropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="profilePropertiesInput")
    def profile_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "profilePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="profileProperties")
    def profile_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "profileProperties"))

    @profile_properties.setter
    def profile_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileProperties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            def stub(*, instance_url: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference",
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
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            def stub(*, instance_url: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference",
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
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            def stub(*, instance_url: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference",
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
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            def stub(*, instance_url: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference",
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
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference",
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

    @jsii.member(jsii_name="putAmplitude")
    def put_amplitude(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude()

        return typing.cast(None, jsii.invoke(self, "putAmplitude", [value]))

    @jsii.member(jsii_name="putCustomConnector")
    def put_custom_connector(
        self,
        *,
        oauth2_properties: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties, typing.Dict[str, typing.Any]]] = None,
        profile_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param oauth2_properties: oauth2_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth2_properties AppflowConnectorProfile#oauth2_properties}
        :param profile_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#profile_properties AppflowConnectorProfile#profile_properties}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector(
            oauth2_properties=oauth2_properties, profile_properties=profile_properties
        )

        return typing.cast(None, jsii.invoke(self, "putCustomConnector", [value]))

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putDynatrace")
    def put_dynatrace(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putDynatrace", [value]))

    @jsii.member(jsii_name="putGoogleAnalytics")
    def put_google_analytics(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics()

        return typing.cast(None, jsii.invoke(self, "putGoogleAnalytics", [value]))

    @jsii.member(jsii_name="putHoneycode")
    def put_honeycode(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode()

        return typing.cast(None, jsii.invoke(self, "putHoneycode", [value]))

    @jsii.member(jsii_name="putInforNexus")
    def put_infor_nexus(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putInforNexus", [value]))

    @jsii.member(jsii_name="putMarketo")
    def put_marketo(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putMarketo", [value]))

    @jsii.member(jsii_name="putRedshift")
    def put_redshift(
        self,
        *,
        bucket_name: builtins.str,
        role_arn: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        database_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#role_arn AppflowConnectorProfile#role_arn}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.
        :param database_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#database_url AppflowConnectorProfile#database_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift(
            bucket_name=bucket_name,
            role_arn=role_arn,
            bucket_prefix=bucket_prefix,
            database_url=database_url,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshift", [value]))

    @jsii.member(jsii_name="putSalesforce")
    def put_salesforce(
        self,
        *,
        instance_url: typing.Optional[builtins.str] = None,
        is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        :param is_sandbox_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#is_sandbox_environment AppflowConnectorProfile#is_sandbox_environment}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce(
            instance_url=instance_url, is_sandbox_environment=is_sandbox_environment
        )

        return typing.cast(None, jsii.invoke(self, "putSalesforce", [value]))

    @jsii.member(jsii_name="putSapoData")
    def put_sapo_data(
        self,
        *,
        application_host_url: builtins.str,
        application_service_path: builtins.str,
        client_number: builtins.str,
        port_number: jsii.Number,
        logon_language: typing.Optional[builtins.str] = None,
        oauth_properties: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties", typing.Dict[str, typing.Any]]] = None,
        private_link_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_host_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_host_url AppflowConnectorProfile#application_host_url}.
        :param application_service_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_service_path AppflowConnectorProfile#application_service_path}.
        :param client_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_number AppflowConnectorProfile#client_number}.
        :param port_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#port_number AppflowConnectorProfile#port_number}.
        :param logon_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#logon_language AppflowConnectorProfile#logon_language}.
        :param oauth_properties: oauth_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_properties AppflowConnectorProfile#oauth_properties}
        :param private_link_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData(
            application_host_url=application_host_url,
            application_service_path=application_service_path,
            client_number=client_number,
            port_number=port_number,
            logon_language=logon_language,
            oauth_properties=oauth_properties,
            private_link_service_name=private_link_service_name,
        )

        return typing.cast(None, jsii.invoke(self, "putSapoData", [value]))

    @jsii.member(jsii_name="putServiceNow")
    def put_service_now(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putServiceNow", [value]))

    @jsii.member(jsii_name="putSingular")
    def put_singular(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular()

        return typing.cast(None, jsii.invoke(self, "putSingular", [value]))

    @jsii.member(jsii_name="putSlack")
    def put_slack(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="putSnowflake")
    def put_snowflake(
        self,
        *,
        bucket_name: builtins.str,
        stage: builtins.str,
        warehouse: builtins.str,
        account_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        private_link_service_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.
        :param stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#stage AppflowConnectorProfile#stage}.
        :param warehouse: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#warehouse AppflowConnectorProfile#warehouse}.
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#account_name AppflowConnectorProfile#account_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.
        :param private_link_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#region AppflowConnectorProfile#region}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake(
            bucket_name=bucket_name,
            stage=stage,
            warehouse=warehouse,
            account_name=account_name,
            bucket_prefix=bucket_prefix,
            private_link_service_name=private_link_service_name,
            region=region,
        )

        return typing.cast(None, jsii.invoke(self, "putSnowflake", [value]))

    @jsii.member(jsii_name="putTrendmicro")
    def put_trendmicro(self) -> None:
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro()

        return typing.cast(None, jsii.invoke(self, "putTrendmicro", [value]))

    @jsii.member(jsii_name="putVeeva")
    def put_veeva(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putVeeva", [value]))

    @jsii.member(jsii_name="putZendesk")
    def put_zendesk(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk(
            instance_url=instance_url
        )

        return typing.cast(None, jsii.invoke(self, "putZendesk", [value]))

    @jsii.member(jsii_name="resetAmplitude")
    def reset_amplitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmplitude", []))

    @jsii.member(jsii_name="resetCustomConnector")
    def reset_custom_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomConnector", []))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetDynatrace")
    def reset_dynatrace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynatrace", []))

    @jsii.member(jsii_name="resetGoogleAnalytics")
    def reset_google_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleAnalytics", []))

    @jsii.member(jsii_name="resetHoneycode")
    def reset_honeycode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHoneycode", []))

    @jsii.member(jsii_name="resetInforNexus")
    def reset_infor_nexus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInforNexus", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetRedshift")
    def reset_redshift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshift", []))

    @jsii.member(jsii_name="resetSalesforce")
    def reset_salesforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalesforce", []))

    @jsii.member(jsii_name="resetSapoData")
    def reset_sapo_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSapoData", []))

    @jsii.member(jsii_name="resetServiceNow")
    def reset_service_now(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceNow", []))

    @jsii.member(jsii_name="resetSingular")
    def reset_singular(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingular", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetSnowflake")
    def reset_snowflake(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnowflake", []))

    @jsii.member(jsii_name="resetTrendmicro")
    def reset_trendmicro(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrendmicro", []))

    @jsii.member(jsii_name="resetVeeva")
    def reset_veeva(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVeeva", []))

    @jsii.member(jsii_name="resetZendesk")
    def reset_zendesk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZendesk", []))

    @builtins.property
    @jsii.member(jsii_name="amplitude")
    def amplitude(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference, jsii.get(self, "amplitude"))

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference, jsii.get(self, "customConnector"))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="dynatrace")
    def dynatrace(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference, jsii.get(self, "dynatrace"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalytics")
    def google_analytics(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference, jsii.get(self, "googleAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="honeycode")
    def honeycode(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference, jsii.get(self, "honeycode"))

    @builtins.property
    @jsii.member(jsii_name="inforNexus")
    def infor_nexus(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference, jsii.get(self, "inforNexus"))

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference, jsii.get(self, "marketo"))

    @builtins.property
    @jsii.member(jsii_name="redshift")
    def redshift(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference", jsii.get(self, "redshift"))

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference", jsii.get(self, "salesforce"))

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference", jsii.get(self, "sapoData"))

    @builtins.property
    @jsii.member(jsii_name="serviceNow")
    def service_now(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference", jsii.get(self, "serviceNow"))

    @builtins.property
    @jsii.member(jsii_name="singular")
    def singular(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference", jsii.get(self, "singular"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="snowflake")
    def snowflake(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference", jsii.get(self, "snowflake"))

    @builtins.property
    @jsii.member(jsii_name="trendmicro")
    def trendmicro(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference", jsii.get(self, "trendmicro"))

    @builtins.property
    @jsii.member(jsii_name="veeva")
    def veeva(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference", jsii.get(self, "veeva"))

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(
        self,
    ) -> "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference":
        return typing.cast("AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference", jsii.get(self, "zendesk"))

    @builtins.property
    @jsii.member(jsii_name="amplitudeInput")
    def amplitude_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude], jsii.get(self, "amplitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="dynatraceInput")
    def dynatrace_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace], jsii.get(self, "dynatraceInput"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalyticsInput")
    def google_analytics_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics], jsii.get(self, "googleAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="honeycodeInput")
    def honeycode_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode], jsii.get(self, "honeycodeInput"))

    @builtins.property
    @jsii.member(jsii_name="inforNexusInput")
    def infor_nexus_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus], jsii.get(self, "inforNexusInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftInput")
    def redshift_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift"], jsii.get(self, "redshiftInput"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce"], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData"], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNowInput")
    def service_now_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow"], jsii.get(self, "serviceNowInput"))

    @builtins.property
    @jsii.member(jsii_name="singularInput")
    def singular_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular"], jsii.get(self, "singularInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="snowflakeInput")
    def snowflake_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake"], jsii.get(self, "snowflakeInput"))

    @builtins.property
    @jsii.member(jsii_name="trendmicroInput")
    def trendmicro_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro"], jsii.get(self, "trendmicroInput"))

    @builtins.property
    @jsii.member(jsii_name="veevaInput")
    def veeva_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva"], jsii.get(self, "veevaInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk"]:
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk"], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "role_arn": "roleArn",
        "bucket_prefix": "bucketPrefix",
        "database_url": "databaseUrl",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        role_arn: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        database_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#role_arn AppflowConnectorProfile#role_arn}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.
        :param database_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#database_url AppflowConnectorProfile#database_url}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: builtins.str,
                role_arn: builtins.str,
                bucket_prefix: typing.Optional[builtins.str] = None,
                database_url: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument database_url", value=database_url, expected_type=type_hints["database_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "role_arn": role_arn,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if database_url is not None:
            self._values["database_url"] = database_url

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#role_arn AppflowConnectorProfile#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#database_url AppflowConnectorProfile#database_url}.'''
        result = self._values.get("database_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference",
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

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetDatabaseUrl")
    def reset_database_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseUrl", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseUrlInput")
    def database_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="databaseUrl")
    def database_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseUrl"))

    @database_url.setter
    def database_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce",
    jsii_struct_bases=[],
    name_mapping={
        "instance_url": "instanceUrl",
        "is_sandbox_environment": "isSandboxEnvironment",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce:
    def __init__(
        self,
        *,
        instance_url: typing.Optional[builtins.str] = None,
        is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        :param is_sandbox_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#is_sandbox_environment AppflowConnectorProfile#is_sandbox_environment}.
        '''
        if __debug__:
            def stub(
                *,
                instance_url: typing.Optional[builtins.str] = None,
                is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            check_type(argname="argument is_sandbox_environment", value=is_sandbox_environment, expected_type=type_hints["is_sandbox_environment"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_url is not None:
            self._values["instance_url"] = instance_url
        if is_sandbox_environment is not None:
            self._values["is_sandbox_environment"] = is_sandbox_environment

    @builtins.property
    def instance_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_sandbox_environment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#is_sandbox_environment AppflowConnectorProfile#is_sandbox_environment}.'''
        result = self._values.get("is_sandbox_environment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference",
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

    @jsii.member(jsii_name="resetInstanceUrl")
    def reset_instance_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceUrl", []))

    @jsii.member(jsii_name="resetIsSandboxEnvironment")
    def reset_is_sandbox_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsSandboxEnvironment", []))

    @builtins.property
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="isSandboxEnvironmentInput")
    def is_sandbox_environment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isSandboxEnvironmentInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="isSandboxEnvironment")
    def is_sandbox_environment(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isSandboxEnvironment"))

    @is_sandbox_environment.setter
    def is_sandbox_environment(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isSandboxEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData",
    jsii_struct_bases=[],
    name_mapping={
        "application_host_url": "applicationHostUrl",
        "application_service_path": "applicationServicePath",
        "client_number": "clientNumber",
        "port_number": "portNumber",
        "logon_language": "logonLanguage",
        "oauth_properties": "oauthProperties",
        "private_link_service_name": "privateLinkServiceName",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData:
    def __init__(
        self,
        *,
        application_host_url: builtins.str,
        application_service_path: builtins.str,
        client_number: builtins.str,
        port_number: jsii.Number,
        logon_language: typing.Optional[builtins.str] = None,
        oauth_properties: typing.Optional[typing.Union["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties", typing.Dict[str, typing.Any]]] = None,
        private_link_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_host_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_host_url AppflowConnectorProfile#application_host_url}.
        :param application_service_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_service_path AppflowConnectorProfile#application_service_path}.
        :param client_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_number AppflowConnectorProfile#client_number}.
        :param port_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#port_number AppflowConnectorProfile#port_number}.
        :param logon_language: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#logon_language AppflowConnectorProfile#logon_language}.
        :param oauth_properties: oauth_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_properties AppflowConnectorProfile#oauth_properties}
        :param private_link_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.
        '''
        if isinstance(oauth_properties, dict):
            oauth_properties = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties(**oauth_properties)
        if __debug__:
            def stub(
                *,
                application_host_url: builtins.str,
                application_service_path: builtins.str,
                client_number: builtins.str,
                port_number: jsii.Number,
                logon_language: typing.Optional[builtins.str] = None,
                oauth_properties: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties, typing.Dict[str, typing.Any]]] = None,
                private_link_service_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument application_host_url", value=application_host_url, expected_type=type_hints["application_host_url"])
            check_type(argname="argument application_service_path", value=application_service_path, expected_type=type_hints["application_service_path"])
            check_type(argname="argument client_number", value=client_number, expected_type=type_hints["client_number"])
            check_type(argname="argument port_number", value=port_number, expected_type=type_hints["port_number"])
            check_type(argname="argument logon_language", value=logon_language, expected_type=type_hints["logon_language"])
            check_type(argname="argument oauth_properties", value=oauth_properties, expected_type=type_hints["oauth_properties"])
            check_type(argname="argument private_link_service_name", value=private_link_service_name, expected_type=type_hints["private_link_service_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "application_host_url": application_host_url,
            "application_service_path": application_service_path,
            "client_number": client_number,
            "port_number": port_number,
        }
        if logon_language is not None:
            self._values["logon_language"] = logon_language
        if oauth_properties is not None:
            self._values["oauth_properties"] = oauth_properties
        if private_link_service_name is not None:
            self._values["private_link_service_name"] = private_link_service_name

    @builtins.property
    def application_host_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_host_url AppflowConnectorProfile#application_host_url}.'''
        result = self._values.get("application_host_url")
        assert result is not None, "Required property 'application_host_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_service_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#application_service_path AppflowConnectorProfile#application_service_path}.'''
        result = self._values.get("application_service_path")
        assert result is not None, "Required property 'application_service_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_number(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#client_number AppflowConnectorProfile#client_number}.'''
        result = self._values.get("client_number")
        assert result is not None, "Required property 'client_number' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port_number(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#port_number AppflowConnectorProfile#port_number}.'''
        result = self._values.get("port_number")
        assert result is not None, "Required property 'port_number' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def logon_language(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#logon_language AppflowConnectorProfile#logon_language}.'''
        result = self._values.get("logon_language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_properties(
        self,
    ) -> typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties"]:
        '''oauth_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_properties AppflowConnectorProfile#oauth_properties}
        '''
        result = self._values.get("oauth_properties")
        return typing.cast(typing.Optional["AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties"], result)

    @builtins.property
    def private_link_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.'''
        result = self._values.get("private_link_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties",
    jsii_struct_bases=[],
    name_mapping={
        "auth_code_url": "authCodeUrl",
        "oauth_scopes": "oauthScopes",
        "token_url": "tokenUrl",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties:
    def __init__(
        self,
        *,
        auth_code_url: builtins.str,
        oauth_scopes: typing.Sequence[builtins.str],
        token_url: builtins.str,
    ) -> None:
        '''
        :param auth_code_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code_url AppflowConnectorProfile#auth_code_url}.
        :param oauth_scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_scopes AppflowConnectorProfile#oauth_scopes}.
        :param token_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.
        '''
        if __debug__:
            def stub(
                *,
                auth_code_url: builtins.str,
                oauth_scopes: typing.Sequence[builtins.str],
                token_url: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auth_code_url", value=auth_code_url, expected_type=type_hints["auth_code_url"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "auth_code_url": auth_code_url,
            "oauth_scopes": oauth_scopes,
            "token_url": token_url,
        }

    @builtins.property
    def auth_code_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code_url AppflowConnectorProfile#auth_code_url}.'''
        result = self._values.get("auth_code_url")
        assert result is not None, "Required property 'auth_code_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth_scopes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_scopes AppflowConnectorProfile#oauth_scopes}.'''
        result = self._values.get("oauth_scopes")
        assert result is not None, "Required property 'oauth_scopes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def token_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.'''
        result = self._values.get("token_url")
        assert result is not None, "Required property 'token_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference",
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
    @jsii.member(jsii_name="authCodeUrlInput")
    def auth_code_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authCodeUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUrlInput")
    def token_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="authCodeUrl")
    def auth_code_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authCodeUrl"))

    @auth_code_url.setter
    def auth_code_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authCodeUrl", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUrl")
    def token_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenUrl"))

    @token_url.setter
    def token_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference",
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

    @jsii.member(jsii_name="putOauthProperties")
    def put_oauth_properties(
        self,
        *,
        auth_code_url: builtins.str,
        oauth_scopes: typing.Sequence[builtins.str],
        token_url: builtins.str,
    ) -> None:
        '''
        :param auth_code_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#auth_code_url AppflowConnectorProfile#auth_code_url}.
        :param oauth_scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#oauth_scopes AppflowConnectorProfile#oauth_scopes}.
        :param token_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#token_url AppflowConnectorProfile#token_url}.
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties(
            auth_code_url=auth_code_url, oauth_scopes=oauth_scopes, token_url=token_url
        )

        return typing.cast(None, jsii.invoke(self, "putOauthProperties", [value]))

    @jsii.member(jsii_name="resetLogonLanguage")
    def reset_logon_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogonLanguage", []))

    @jsii.member(jsii_name="resetOauthProperties")
    def reset_oauth_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthProperties", []))

    @jsii.member(jsii_name="resetPrivateLinkServiceName")
    def reset_private_link_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="oauthProperties")
    def oauth_properties(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference, jsii.get(self, "oauthProperties"))

    @builtins.property
    @jsii.member(jsii_name="applicationHostUrlInput")
    def application_host_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationHostUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationServicePathInput")
    def application_service_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationServicePathInput"))

    @builtins.property
    @jsii.member(jsii_name="clientNumberInput")
    def client_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="logonLanguageInput")
    def logon_language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logonLanguageInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthPropertiesInput")
    def oauth_properties_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties], jsii.get(self, "oauthPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="portNumberInput")
    def port_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceNameInput")
    def private_link_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateLinkServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationHostUrl")
    def application_host_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationHostUrl"))

    @application_host_url.setter
    def application_host_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationHostUrl", value)

    @builtins.property
    @jsii.member(jsii_name="applicationServicePath")
    def application_service_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationServicePath"))

    @application_service_path.setter
    def application_service_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationServicePath", value)

    @builtins.property
    @jsii.member(jsii_name="clientNumber")
    def client_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientNumber"))

    @client_number.setter
    def client_number(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientNumber", value)

    @builtins.property
    @jsii.member(jsii_name="logonLanguage")
    def logon_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logonLanguage"))

    @logon_language.setter
    def logon_language(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logonLanguage", value)

    @builtins.property
    @jsii.member(jsii_name="portNumber")
    def port_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "portNumber"))

    @port_number.setter
    def port_number(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portNumber", value)

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceName")
    def private_link_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateLinkServiceName"))

    @private_link_service_name.setter
    def private_link_service_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateLinkServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            def stub(*, instance_url: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference",
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
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            def stub(*, instance_url: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference",
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
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "stage": "stage",
        "warehouse": "warehouse",
        "account_name": "accountName",
        "bucket_prefix": "bucketPrefix",
        "private_link_service_name": "privateLinkServiceName",
        "region": "region",
    },
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        stage: builtins.str,
        warehouse: builtins.str,
        account_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        private_link_service_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.
        :param stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#stage AppflowConnectorProfile#stage}.
        :param warehouse: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#warehouse AppflowConnectorProfile#warehouse}.
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#account_name AppflowConnectorProfile#account_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.
        :param private_link_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#region AppflowConnectorProfile#region}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: builtins.str,
                stage: builtins.str,
                warehouse: builtins.str,
                account_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                private_link_service_name: typing.Optional[builtins.str] = None,
                region: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
            check_type(argname="argument warehouse", value=warehouse, expected_type=type_hints["warehouse"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument private_link_service_name", value=private_link_service_name, expected_type=type_hints["private_link_service_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "stage": stage,
            "warehouse": warehouse,
        }
        if account_name is not None:
            self._values["account_name"] = account_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if private_link_service_name is not None:
            self._values["private_link_service_name"] = private_link_service_name
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_name AppflowConnectorProfile#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stage(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#stage AppflowConnectorProfile#stage}.'''
        result = self._values.get("stage")
        assert result is not None, "Required property 'stage' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def warehouse(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#warehouse AppflowConnectorProfile#warehouse}.'''
        result = self._values.get("warehouse")
        assert result is not None, "Required property 'warehouse' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#account_name AppflowConnectorProfile#account_name}.'''
        result = self._values.get("account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#bucket_prefix AppflowConnectorProfile#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_link_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#private_link_service_name AppflowConnectorProfile#private_link_service_name}.'''
        result = self._values.get("private_link_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#region AppflowConnectorProfile#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference",
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

    @jsii.member(jsii_name="resetAccountName")
    def reset_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetPrivateLinkServiceName")
    def reset_private_link_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateLinkServiceName", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceNameInput")
    def private_link_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateLinkServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="stageInput")
    def stage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stageInput"))

    @builtins.property
    @jsii.member(jsii_name="warehouseInput")
    def warehouse_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouseInput"))

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="privateLinkServiceName")
    def private_link_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateLinkServiceName"))

    @private_link_service_name.setter
    def private_link_service_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateLinkServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stage"))

    @stage.setter
    def stage(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stage", value)

    @builtins.property
    @jsii.member(jsii_name="warehouse")
    def warehouse(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warehouse"))

    @warehouse.setter
    def warehouse(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouse", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            def stub(*, instance_url: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference",
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
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk",
    jsii_struct_bases=[],
    name_mapping={"instance_url": "instanceUrl"},
)
class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk:
    def __init__(self, *, instance_url: builtins.str) -> None:
        '''
        :param instance_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.
        '''
        if __debug__:
            def stub(*, instance_url: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_url": instance_url,
        }

    @builtins.property
    def instance_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#instance_url AppflowConnectorProfile#instance_url}.'''
        result = self._values.get("instance_url")
        assert result is not None, "Required property 'instance_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference",
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
    @jsii.member(jsii_name="instanceUrlInput")
    def instance_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceUrl")
    def instance_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceUrl"))

    @instance_url.setter
    def instance_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowConnectorProfileConnectorProfileConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowConnectorProfile.AppflowConnectorProfileConnectorProfileConfigOutputReference",
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

    @jsii.member(jsii_name="putConnectorProfileCredentials")
    def put_connector_profile_credentials(
        self,
        *,
        amplitude: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude, typing.Dict[str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector, typing.Dict[str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog, typing.Dict[str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace, typing.Dict[str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics, typing.Dict[str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode, typing.Dict[str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus, typing.Dict[str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo, typing.Dict[str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift, typing.Dict[str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce, typing.Dict[str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData, typing.Dict[str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow, typing.Dict[str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular, typing.Dict[str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack, typing.Dict[str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake, typing.Dict[str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro, typing.Dict[str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva, typing.Dict[str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials(
            amplitude=amplitude,
            custom_connector=custom_connector,
            datadog=datadog,
            dynatrace=dynatrace,
            google_analytics=google_analytics,
            honeycode=honeycode,
            infor_nexus=infor_nexus,
            marketo=marketo,
            redshift=redshift,
            salesforce=salesforce,
            sapo_data=sapo_data,
            service_now=service_now,
            singular=singular,
            slack=slack,
            snowflake=snowflake,
            trendmicro=trendmicro,
            veeva=veeva,
            zendesk=zendesk,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectorProfileCredentials", [value]))

    @jsii.member(jsii_name="putConnectorProfileProperties")
    def put_connector_profile_properties(
        self,
        *,
        amplitude: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude, typing.Dict[str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector, typing.Dict[str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog, typing.Dict[str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace, typing.Dict[str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics, typing.Dict[str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode, typing.Dict[str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus, typing.Dict[str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo, typing.Dict[str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift, typing.Dict[str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce, typing.Dict[str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData, typing.Dict[str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow, typing.Dict[str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular, typing.Dict[str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack, typing.Dict[str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake, typing.Dict[str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro, typing.Dict[str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva, typing.Dict[str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union[AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#amplitude AppflowConnectorProfile#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#custom_connector AppflowConnectorProfile#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#datadog AppflowConnectorProfile#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#dynatrace AppflowConnectorProfile#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#google_analytics AppflowConnectorProfile#google_analytics}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#honeycode AppflowConnectorProfile#honeycode}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#infor_nexus AppflowConnectorProfile#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#marketo AppflowConnectorProfile#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#redshift AppflowConnectorProfile#redshift}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#salesforce AppflowConnectorProfile#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#sapo_data AppflowConnectorProfile#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#service_now AppflowConnectorProfile#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#singular AppflowConnectorProfile#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#slack AppflowConnectorProfile#slack}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#snowflake AppflowConnectorProfile#snowflake}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#trendmicro AppflowConnectorProfile#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#veeva AppflowConnectorProfile#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_connector_profile#zendesk AppflowConnectorProfile#zendesk}
        '''
        value = AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties(
            amplitude=amplitude,
            custom_connector=custom_connector,
            datadog=datadog,
            dynatrace=dynatrace,
            google_analytics=google_analytics,
            honeycode=honeycode,
            infor_nexus=infor_nexus,
            marketo=marketo,
            redshift=redshift,
            salesforce=salesforce,
            sapo_data=sapo_data,
            service_now=service_now,
            singular=singular,
            slack=slack,
            snowflake=snowflake,
            trendmicro=trendmicro,
            veeva=veeva,
            zendesk=zendesk,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectorProfileProperties", [value]))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileCredentials")
    def connector_profile_credentials(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference, jsii.get(self, "connectorProfileCredentials"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileProperties")
    def connector_profile_properties(
        self,
    ) -> AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference:
        return typing.cast(AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference, jsii.get(self, "connectorProfileProperties"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileCredentialsInput")
    def connector_profile_credentials_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials], jsii.get(self, "connectorProfileCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfilePropertiesInput")
    def connector_profile_properties_input(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties], jsii.get(self, "connectorProfilePropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowConnectorProfileConnectorProfileConfig]:
        return typing.cast(typing.Optional[AppflowConnectorProfileConnectorProfileConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowConnectorProfileConnectorProfileConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowConnectorProfileConnectorProfileConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppflowConnectorProfile",
    "AppflowConnectorProfileConfig",
    "AppflowConnectorProfileConnectorProfileConfig",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentials",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfileProperties",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk",
    "AppflowConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskOutputReference",
    "AppflowConnectorProfileConnectorProfileConfigOutputReference",
]

publication.publish()
