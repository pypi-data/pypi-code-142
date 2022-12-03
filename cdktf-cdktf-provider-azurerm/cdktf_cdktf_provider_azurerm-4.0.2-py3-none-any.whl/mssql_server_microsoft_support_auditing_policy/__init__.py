'''
# `azurerm_mssql_server_microsoft_support_auditing_policy`

Refer to the Terraform Registory for docs: [`azurerm_mssql_server_microsoft_support_auditing_policy`](https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy).
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


class MssqlServerMicrosoftSupportAuditingPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlServerMicrosoftSupportAuditingPolicy.MssqlServerMicrosoftSupportAuditingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy azurerm_mssql_server_microsoft_support_auditing_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        server_id: builtins.str,
        blob_storage_endpoint: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        log_monitoring_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_account_subscription_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MssqlServerMicrosoftSupportAuditingPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy azurerm_mssql_server_microsoft_support_auditing_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param server_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#server_id MssqlServerMicrosoftSupportAuditingPolicy#server_id}.
        :param blob_storage_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#blob_storage_endpoint MssqlServerMicrosoftSupportAuditingPolicy#blob_storage_endpoint}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#enabled MssqlServerMicrosoftSupportAuditingPolicy#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#id MssqlServerMicrosoftSupportAuditingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_monitoring_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#log_monitoring_enabled MssqlServerMicrosoftSupportAuditingPolicy#log_monitoring_enabled}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#storage_account_access_key MssqlServerMicrosoftSupportAuditingPolicy#storage_account_access_key}.
        :param storage_account_subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#storage_account_subscription_id MssqlServerMicrosoftSupportAuditingPolicy#storage_account_subscription_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#timeouts MssqlServerMicrosoftSupportAuditingPolicy#timeouts}
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
                server_id: builtins.str,
                blob_storage_endpoint: typing.Optional[builtins.str] = None,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                log_monitoring_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                storage_account_access_key: typing.Optional[builtins.str] = None,
                storage_account_subscription_id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[MssqlServerMicrosoftSupportAuditingPolicyTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = MssqlServerMicrosoftSupportAuditingPolicyConfig(
            server_id=server_id,
            blob_storage_endpoint=blob_storage_endpoint,
            enabled=enabled,
            id=id,
            log_monitoring_enabled=log_monitoring_enabled,
            storage_account_access_key=storage_account_access_key,
            storage_account_subscription_id=storage_account_subscription_id,
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
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#create MssqlServerMicrosoftSupportAuditingPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#delete MssqlServerMicrosoftSupportAuditingPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#read MssqlServerMicrosoftSupportAuditingPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#update MssqlServerMicrosoftSupportAuditingPolicy#update}.
        '''
        value = MssqlServerMicrosoftSupportAuditingPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBlobStorageEndpoint")
    def reset_blob_storage_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlobStorageEndpoint", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogMonitoringEnabled")
    def reset_log_monitoring_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogMonitoringEnabled", []))

    @jsii.member(jsii_name="resetStorageAccountAccessKey")
    def reset_storage_account_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountAccessKey", []))

    @jsii.member(jsii_name="resetStorageAccountSubscriptionId")
    def reset_storage_account_subscription_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountSubscriptionId", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "MssqlServerMicrosoftSupportAuditingPolicyTimeoutsOutputReference":
        return typing.cast("MssqlServerMicrosoftSupportAuditingPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="blobStorageEndpointInput")
    def blob_storage_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blobStorageEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logMonitoringEnabledInput")
    def log_monitoring_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logMonitoringEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="serverIdInput")
    def server_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKeyInput")
    def storage_account_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountAccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountSubscriptionIdInput")
    def storage_account_subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountSubscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MssqlServerMicrosoftSupportAuditingPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MssqlServerMicrosoftSupportAuditingPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="blobStorageEndpoint")
    def blob_storage_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blobStorageEndpoint"))

    @blob_storage_endpoint.setter
    def blob_storage_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blobStorageEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

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
    @jsii.member(jsii_name="logMonitoringEnabled")
    def log_monitoring_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logMonitoringEnabled"))

    @log_monitoring_enabled.setter
    def log_monitoring_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logMonitoringEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="serverId")
    def server_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverId"))

    @server_id.setter
    def server_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverId", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountAccessKey")
    def storage_account_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountAccessKey"))

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountAccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountSubscriptionId")
    def storage_account_subscription_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountSubscriptionId"))

    @storage_account_subscription_id.setter
    def storage_account_subscription_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountSubscriptionId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlServerMicrosoftSupportAuditingPolicy.MssqlServerMicrosoftSupportAuditingPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "server_id": "serverId",
        "blob_storage_endpoint": "blobStorageEndpoint",
        "enabled": "enabled",
        "id": "id",
        "log_monitoring_enabled": "logMonitoringEnabled",
        "storage_account_access_key": "storageAccountAccessKey",
        "storage_account_subscription_id": "storageAccountSubscriptionId",
        "timeouts": "timeouts",
    },
)
class MssqlServerMicrosoftSupportAuditingPolicyConfig(cdktf.TerraformMetaArguments):
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
        server_id: builtins.str,
        blob_storage_endpoint: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        log_monitoring_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        storage_account_access_key: typing.Optional[builtins.str] = None,
        storage_account_subscription_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MssqlServerMicrosoftSupportAuditingPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param server_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#server_id MssqlServerMicrosoftSupportAuditingPolicy#server_id}.
        :param blob_storage_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#blob_storage_endpoint MssqlServerMicrosoftSupportAuditingPolicy#blob_storage_endpoint}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#enabled MssqlServerMicrosoftSupportAuditingPolicy#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#id MssqlServerMicrosoftSupportAuditingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_monitoring_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#log_monitoring_enabled MssqlServerMicrosoftSupportAuditingPolicy#log_monitoring_enabled}.
        :param storage_account_access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#storage_account_access_key MssqlServerMicrosoftSupportAuditingPolicy#storage_account_access_key}.
        :param storage_account_subscription_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#storage_account_subscription_id MssqlServerMicrosoftSupportAuditingPolicy#storage_account_subscription_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#timeouts MssqlServerMicrosoftSupportAuditingPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = MssqlServerMicrosoftSupportAuditingPolicyTimeouts(**timeouts)
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
                server_id: builtins.str,
                blob_storage_endpoint: typing.Optional[builtins.str] = None,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                log_monitoring_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                storage_account_access_key: typing.Optional[builtins.str] = None,
                storage_account_subscription_id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[MssqlServerMicrosoftSupportAuditingPolicyTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument server_id", value=server_id, expected_type=type_hints["server_id"])
            check_type(argname="argument blob_storage_endpoint", value=blob_storage_endpoint, expected_type=type_hints["blob_storage_endpoint"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_monitoring_enabled", value=log_monitoring_enabled, expected_type=type_hints["log_monitoring_enabled"])
            check_type(argname="argument storage_account_access_key", value=storage_account_access_key, expected_type=type_hints["storage_account_access_key"])
            check_type(argname="argument storage_account_subscription_id", value=storage_account_subscription_id, expected_type=type_hints["storage_account_subscription_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "server_id": server_id,
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
        if blob_storage_endpoint is not None:
            self._values["blob_storage_endpoint"] = blob_storage_endpoint
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if log_monitoring_enabled is not None:
            self._values["log_monitoring_enabled"] = log_monitoring_enabled
        if storage_account_access_key is not None:
            self._values["storage_account_access_key"] = storage_account_access_key
        if storage_account_subscription_id is not None:
            self._values["storage_account_subscription_id"] = storage_account_subscription_id
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
    def server_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#server_id MssqlServerMicrosoftSupportAuditingPolicy#server_id}.'''
        result = self._values.get("server_id")
        assert result is not None, "Required property 'server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def blob_storage_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#blob_storage_endpoint MssqlServerMicrosoftSupportAuditingPolicy#blob_storage_endpoint}.'''
        result = self._values.get("blob_storage_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#enabled MssqlServerMicrosoftSupportAuditingPolicy#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#id MssqlServerMicrosoftSupportAuditingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_monitoring_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#log_monitoring_enabled MssqlServerMicrosoftSupportAuditingPolicy#log_monitoring_enabled}.'''
        result = self._values.get("log_monitoring_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def storage_account_access_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#storage_account_access_key MssqlServerMicrosoftSupportAuditingPolicy#storage_account_access_key}.'''
        result = self._values.get("storage_account_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_subscription_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#storage_account_subscription_id MssqlServerMicrosoftSupportAuditingPolicy#storage_account_subscription_id}.'''
        result = self._values.get("storage_account_subscription_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["MssqlServerMicrosoftSupportAuditingPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#timeouts MssqlServerMicrosoftSupportAuditingPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MssqlServerMicrosoftSupportAuditingPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlServerMicrosoftSupportAuditingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.mssqlServerMicrosoftSupportAuditingPolicy.MssqlServerMicrosoftSupportAuditingPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MssqlServerMicrosoftSupportAuditingPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#create MssqlServerMicrosoftSupportAuditingPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#delete MssqlServerMicrosoftSupportAuditingPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#read MssqlServerMicrosoftSupportAuditingPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#update MssqlServerMicrosoftSupportAuditingPolicy#update}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
                read: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#create MssqlServerMicrosoftSupportAuditingPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#delete MssqlServerMicrosoftSupportAuditingPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#read MssqlServerMicrosoftSupportAuditingPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/mssql_server_microsoft_support_auditing_policy#update MssqlServerMicrosoftSupportAuditingPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MssqlServerMicrosoftSupportAuditingPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MssqlServerMicrosoftSupportAuditingPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.mssqlServerMicrosoftSupportAuditingPolicy.MssqlServerMicrosoftSupportAuditingPolicyTimeoutsOutputReference",
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

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

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
    ) -> typing.Optional[typing.Union[MssqlServerMicrosoftSupportAuditingPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MssqlServerMicrosoftSupportAuditingPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MssqlServerMicrosoftSupportAuditingPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[MssqlServerMicrosoftSupportAuditingPolicyTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MssqlServerMicrosoftSupportAuditingPolicy",
    "MssqlServerMicrosoftSupportAuditingPolicyConfig",
    "MssqlServerMicrosoftSupportAuditingPolicyTimeouts",
    "MssqlServerMicrosoftSupportAuditingPolicyTimeoutsOutputReference",
]

publication.publish()
