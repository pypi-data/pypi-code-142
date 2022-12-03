'''
# `aws_directory_service_radius_settings`

Refer to the Terraform Registory for docs: [`aws_directory_service_radius_settings`](https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings).
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


class DirectoryServiceRadiusSettings(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.directoryServiceRadiusSettings.DirectoryServiceRadiusSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings aws_directory_service_radius_settings}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        authentication_protocol: builtins.str,
        directory_id: builtins.str,
        display_label: builtins.str,
        radius_port: jsii.Number,
        radius_retries: jsii.Number,
        radius_servers: typing.Sequence[builtins.str],
        radius_timeout: jsii.Number,
        shared_secret: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DirectoryServiceRadiusSettingsTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_same_username: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings aws_directory_service_radius_settings} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param authentication_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#authentication_protocol DirectoryServiceRadiusSettings#authentication_protocol}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#directory_id DirectoryServiceRadiusSettings#directory_id}.
        :param display_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#display_label DirectoryServiceRadiusSettings#display_label}.
        :param radius_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_port DirectoryServiceRadiusSettings#radius_port}.
        :param radius_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_retries DirectoryServiceRadiusSettings#radius_retries}.
        :param radius_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_servers DirectoryServiceRadiusSettings#radius_servers}.
        :param radius_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_timeout DirectoryServiceRadiusSettings#radius_timeout}.
        :param shared_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#shared_secret DirectoryServiceRadiusSettings#shared_secret}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#id DirectoryServiceRadiusSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#timeouts DirectoryServiceRadiusSettings#timeouts}
        :param use_same_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#use_same_username DirectoryServiceRadiusSettings#use_same_username}.
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
                authentication_protocol: builtins.str,
                directory_id: builtins.str,
                display_label: builtins.str,
                radius_port: jsii.Number,
                radius_retries: jsii.Number,
                radius_servers: typing.Sequence[builtins.str],
                radius_timeout: jsii.Number,
                shared_secret: builtins.str,
                id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[DirectoryServiceRadiusSettingsTimeouts, typing.Dict[str, typing.Any]]] = None,
                use_same_username: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        config = DirectoryServiceRadiusSettingsConfig(
            authentication_protocol=authentication_protocol,
            directory_id=directory_id,
            display_label=display_label,
            radius_port=radius_port,
            radius_retries=radius_retries,
            radius_servers=radius_servers,
            radius_timeout=radius_timeout,
            shared_secret=shared_secret,
            id=id,
            timeouts=timeouts,
            use_same_username=use_same_username,
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
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#create DirectoryServiceRadiusSettings#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#update DirectoryServiceRadiusSettings#update}.
        '''
        value = DirectoryServiceRadiusSettingsTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUseSameUsername")
    def reset_use_same_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseSameUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DirectoryServiceRadiusSettingsTimeoutsOutputReference":
        return typing.cast("DirectoryServiceRadiusSettingsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="authenticationProtocolInput")
    def authentication_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryIdInput")
    def directory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="displayLabelInput")
    def display_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusPortInput")
    def radius_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "radiusPortInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusRetriesInput")
    def radius_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "radiusRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusServersInput")
    def radius_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "radiusServersInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusTimeoutInput")
    def radius_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "radiusTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedSecretInput")
    def shared_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DirectoryServiceRadiusSettingsTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DirectoryServiceRadiusSettingsTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="useSameUsernameInput")
    def use_same_username_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useSameUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationProtocol")
    def authentication_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationProtocol"))

    @authentication_protocol.setter
    def authentication_protocol(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="displayLabel")
    def display_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayLabel"))

    @display_label.setter
    def display_label(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayLabel", value)

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
    @jsii.member(jsii_name="radiusPort")
    def radius_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "radiusPort"))

    @radius_port.setter
    def radius_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radiusPort", value)

    @builtins.property
    @jsii.member(jsii_name="radiusRetries")
    def radius_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "radiusRetries"))

    @radius_retries.setter
    def radius_retries(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radiusRetries", value)

    @builtins.property
    @jsii.member(jsii_name="radiusServers")
    def radius_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "radiusServers"))

    @radius_servers.setter
    def radius_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radiusServers", value)

    @builtins.property
    @jsii.member(jsii_name="radiusTimeout")
    def radius_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "radiusTimeout"))

    @radius_timeout.setter
    def radius_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radiusTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="sharedSecret")
    def shared_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedSecret"))

    @shared_secret.setter
    def shared_secret(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedSecret", value)

    @builtins.property
    @jsii.member(jsii_name="useSameUsername")
    def use_same_username(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useSameUsername"))

    @use_same_username.setter
    def use_same_username(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useSameUsername", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.directoryServiceRadiusSettings.DirectoryServiceRadiusSettingsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "authentication_protocol": "authenticationProtocol",
        "directory_id": "directoryId",
        "display_label": "displayLabel",
        "radius_port": "radiusPort",
        "radius_retries": "radiusRetries",
        "radius_servers": "radiusServers",
        "radius_timeout": "radiusTimeout",
        "shared_secret": "sharedSecret",
        "id": "id",
        "timeouts": "timeouts",
        "use_same_username": "useSameUsername",
    },
)
class DirectoryServiceRadiusSettingsConfig(cdktf.TerraformMetaArguments):
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
        authentication_protocol: builtins.str,
        directory_id: builtins.str,
        display_label: builtins.str,
        radius_port: jsii.Number,
        radius_retries: jsii.Number,
        radius_servers: typing.Sequence[builtins.str],
        radius_timeout: jsii.Number,
        shared_secret: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DirectoryServiceRadiusSettingsTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_same_username: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param authentication_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#authentication_protocol DirectoryServiceRadiusSettings#authentication_protocol}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#directory_id DirectoryServiceRadiusSettings#directory_id}.
        :param display_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#display_label DirectoryServiceRadiusSettings#display_label}.
        :param radius_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_port DirectoryServiceRadiusSettings#radius_port}.
        :param radius_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_retries DirectoryServiceRadiusSettings#radius_retries}.
        :param radius_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_servers DirectoryServiceRadiusSettings#radius_servers}.
        :param radius_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_timeout DirectoryServiceRadiusSettings#radius_timeout}.
        :param shared_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#shared_secret DirectoryServiceRadiusSettings#shared_secret}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#id DirectoryServiceRadiusSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#timeouts DirectoryServiceRadiusSettings#timeouts}
        :param use_same_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#use_same_username DirectoryServiceRadiusSettings#use_same_username}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DirectoryServiceRadiusSettingsTimeouts(**timeouts)
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
                authentication_protocol: builtins.str,
                directory_id: builtins.str,
                display_label: builtins.str,
                radius_port: jsii.Number,
                radius_retries: jsii.Number,
                radius_servers: typing.Sequence[builtins.str],
                radius_timeout: jsii.Number,
                shared_secret: builtins.str,
                id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[DirectoryServiceRadiusSettingsTimeouts, typing.Dict[str, typing.Any]]] = None,
                use_same_username: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument authentication_protocol", value=authentication_protocol, expected_type=type_hints["authentication_protocol"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
            check_type(argname="argument display_label", value=display_label, expected_type=type_hints["display_label"])
            check_type(argname="argument radius_port", value=radius_port, expected_type=type_hints["radius_port"])
            check_type(argname="argument radius_retries", value=radius_retries, expected_type=type_hints["radius_retries"])
            check_type(argname="argument radius_servers", value=radius_servers, expected_type=type_hints["radius_servers"])
            check_type(argname="argument radius_timeout", value=radius_timeout, expected_type=type_hints["radius_timeout"])
            check_type(argname="argument shared_secret", value=shared_secret, expected_type=type_hints["shared_secret"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument use_same_username", value=use_same_username, expected_type=type_hints["use_same_username"])
        self._values: typing.Dict[str, typing.Any] = {
            "authentication_protocol": authentication_protocol,
            "directory_id": directory_id,
            "display_label": display_label,
            "radius_port": radius_port,
            "radius_retries": radius_retries,
            "radius_servers": radius_servers,
            "radius_timeout": radius_timeout,
            "shared_secret": shared_secret,
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
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if use_same_username is not None:
            self._values["use_same_username"] = use_same_username

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
    def authentication_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#authentication_protocol DirectoryServiceRadiusSettings#authentication_protocol}.'''
        result = self._values.get("authentication_protocol")
        assert result is not None, "Required property 'authentication_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#directory_id DirectoryServiceRadiusSettings#directory_id}.'''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#display_label DirectoryServiceRadiusSettings#display_label}.'''
        result = self._values.get("display_label")
        assert result is not None, "Required property 'display_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def radius_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_port DirectoryServiceRadiusSettings#radius_port}.'''
        result = self._values.get("radius_port")
        assert result is not None, "Required property 'radius_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def radius_retries(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_retries DirectoryServiceRadiusSettings#radius_retries}.'''
        result = self._values.get("radius_retries")
        assert result is not None, "Required property 'radius_retries' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def radius_servers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_servers DirectoryServiceRadiusSettings#radius_servers}.'''
        result = self._values.get("radius_servers")
        assert result is not None, "Required property 'radius_servers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def radius_timeout(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#radius_timeout DirectoryServiceRadiusSettings#radius_timeout}.'''
        result = self._values.get("radius_timeout")
        assert result is not None, "Required property 'radius_timeout' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def shared_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#shared_secret DirectoryServiceRadiusSettings#shared_secret}.'''
        result = self._values.get("shared_secret")
        assert result is not None, "Required property 'shared_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#id DirectoryServiceRadiusSettings#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DirectoryServiceRadiusSettingsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#timeouts DirectoryServiceRadiusSettings#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DirectoryServiceRadiusSettingsTimeouts"], result)

    @builtins.property
    def use_same_username(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#use_same_username DirectoryServiceRadiusSettings#use_same_username}.'''
        result = self._values.get("use_same_username")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectoryServiceRadiusSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.directoryServiceRadiusSettings.DirectoryServiceRadiusSettingsTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class DirectoryServiceRadiusSettingsTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#create DirectoryServiceRadiusSettings#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#update DirectoryServiceRadiusSettings#update}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#create DirectoryServiceRadiusSettings#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/directory_service_radius_settings#update DirectoryServiceRadiusSettings#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectoryServiceRadiusSettingsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DirectoryServiceRadiusSettingsTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.directoryServiceRadiusSettings.DirectoryServiceRadiusSettingsTimeoutsOutputReference",
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

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
    ) -> typing.Optional[typing.Union[DirectoryServiceRadiusSettingsTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DirectoryServiceRadiusSettingsTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DirectoryServiceRadiusSettingsTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DirectoryServiceRadiusSettingsTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DirectoryServiceRadiusSettings",
    "DirectoryServiceRadiusSettingsConfig",
    "DirectoryServiceRadiusSettingsTimeouts",
    "DirectoryServiceRadiusSettingsTimeoutsOutputReference",
]

publication.publish()
