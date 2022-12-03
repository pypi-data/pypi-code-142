'''
# `aws_api_gateway_method_settings`

Refer to the Terraform Registory for docs: [`aws_api_gateway_method_settings`](https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings).
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


class ApiGatewayMethodSettings(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apiGatewayMethodSettings.ApiGatewayMethodSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings aws_api_gateway_method_settings}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        method_path: builtins.str,
        rest_api_id: builtins.str,
        settings: typing.Union["ApiGatewayMethodSettingsSettings", typing.Dict[str, typing.Any]],
        stage_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings aws_api_gateway_method_settings} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param method_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#method_path ApiGatewayMethodSettings#method_path}.
        :param rest_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#rest_api_id ApiGatewayMethodSettings#rest_api_id}.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#settings ApiGatewayMethodSettings#settings}
        :param stage_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#stage_name ApiGatewayMethodSettings#stage_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#id ApiGatewayMethodSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                method_path: builtins.str,
                rest_api_id: builtins.str,
                settings: typing.Union[ApiGatewayMethodSettingsSettings, typing.Dict[str, typing.Any]],
                stage_name: builtins.str,
                id: typing.Optional[builtins.str] = None,
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
        config = ApiGatewayMethodSettingsConfig(
            method_path=method_path,
            rest_api_id=rest_api_id,
            settings=settings,
            stage_name=stage_name,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        *,
        cache_data_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cache_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        caching_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data_trace_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        logging_level: typing.Optional[builtins.str] = None,
        metrics_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_authorization_for_cache_control: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        throttling_burst_limit: typing.Optional[jsii.Number] = None,
        throttling_rate_limit: typing.Optional[jsii.Number] = None,
        unauthorized_cache_control_header_strategy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cache_data_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#cache_data_encrypted ApiGatewayMethodSettings#cache_data_encrypted}.
        :param cache_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#cache_ttl_in_seconds ApiGatewayMethodSettings#cache_ttl_in_seconds}.
        :param caching_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#caching_enabled ApiGatewayMethodSettings#caching_enabled}.
        :param data_trace_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#data_trace_enabled ApiGatewayMethodSettings#data_trace_enabled}.
        :param logging_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#logging_level ApiGatewayMethodSettings#logging_level}.
        :param metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#metrics_enabled ApiGatewayMethodSettings#metrics_enabled}.
        :param require_authorization_for_cache_control: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#require_authorization_for_cache_control ApiGatewayMethodSettings#require_authorization_for_cache_control}.
        :param throttling_burst_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#throttling_burst_limit ApiGatewayMethodSettings#throttling_burst_limit}.
        :param throttling_rate_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#throttling_rate_limit ApiGatewayMethodSettings#throttling_rate_limit}.
        :param unauthorized_cache_control_header_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#unauthorized_cache_control_header_strategy ApiGatewayMethodSettings#unauthorized_cache_control_header_strategy}.
        '''
        value = ApiGatewayMethodSettingsSettings(
            cache_data_encrypted=cache_data_encrypted,
            cache_ttl_in_seconds=cache_ttl_in_seconds,
            caching_enabled=caching_enabled,
            data_trace_enabled=data_trace_enabled,
            logging_level=logging_level,
            metrics_enabled=metrics_enabled,
            require_authorization_for_cache_control=require_authorization_for_cache_control,
            throttling_burst_limit=throttling_burst_limit,
            throttling_rate_limit=throttling_rate_limit,
            unauthorized_cache_control_header_strategy=unauthorized_cache_control_header_strategy,
        )

        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "ApiGatewayMethodSettingsSettingsOutputReference":
        return typing.cast("ApiGatewayMethodSettingsSettingsOutputReference", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="methodPathInput")
    def method_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodPathInput"))

    @builtins.property
    @jsii.member(jsii_name="restApiIdInput")
    def rest_api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restApiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional["ApiGatewayMethodSettingsSettings"]:
        return typing.cast(typing.Optional["ApiGatewayMethodSettingsSettings"], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="stageNameInput")
    def stage_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stageNameInput"))

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
    @jsii.member(jsii_name="methodPath")
    def method_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "methodPath"))

    @method_path.setter
    def method_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "methodPath", value)

    @builtins.property
    @jsii.member(jsii_name="restApiId")
    def rest_api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restApiId"))

    @rest_api_id.setter
    def rest_api_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restApiId", value)

    @builtins.property
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stageName"))

    @stage_name.setter
    def stage_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stageName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apiGatewayMethodSettings.ApiGatewayMethodSettingsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "method_path": "methodPath",
        "rest_api_id": "restApiId",
        "settings": "settings",
        "stage_name": "stageName",
        "id": "id",
    },
)
class ApiGatewayMethodSettingsConfig(cdktf.TerraformMetaArguments):
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
        method_path: builtins.str,
        rest_api_id: builtins.str,
        settings: typing.Union["ApiGatewayMethodSettingsSettings", typing.Dict[str, typing.Any]],
        stage_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param method_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#method_path ApiGatewayMethodSettings#method_path}.
        :param rest_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#rest_api_id ApiGatewayMethodSettings#rest_api_id}.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#settings ApiGatewayMethodSettings#settings}
        :param stage_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#stage_name ApiGatewayMethodSettings#stage_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#id ApiGatewayMethodSettings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(settings, dict):
            settings = ApiGatewayMethodSettingsSettings(**settings)
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
                method_path: builtins.str,
                rest_api_id: builtins.str,
                settings: typing.Union[ApiGatewayMethodSettingsSettings, typing.Dict[str, typing.Any]],
                stage_name: builtins.str,
                id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument method_path", value=method_path, expected_type=type_hints["method_path"])
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "method_path": method_path,
            "rest_api_id": rest_api_id,
            "settings": settings,
            "stage_name": stage_name,
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
    def method_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#method_path ApiGatewayMethodSettings#method_path}.'''
        result = self._values.get("method_path")
        assert result is not None, "Required property 'method_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#rest_api_id ApiGatewayMethodSettings#rest_api_id}.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def settings(self) -> "ApiGatewayMethodSettingsSettings":
        '''settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#settings ApiGatewayMethodSettings#settings}
        '''
        result = self._values.get("settings")
        assert result is not None, "Required property 'settings' is missing"
        return typing.cast("ApiGatewayMethodSettingsSettings", result)

    @builtins.property
    def stage_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#stage_name ApiGatewayMethodSettings#stage_name}.'''
        result = self._values.get("stage_name")
        assert result is not None, "Required property 'stage_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#id ApiGatewayMethodSettings#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayMethodSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apiGatewayMethodSettings.ApiGatewayMethodSettingsSettings",
    jsii_struct_bases=[],
    name_mapping={
        "cache_data_encrypted": "cacheDataEncrypted",
        "cache_ttl_in_seconds": "cacheTtlInSeconds",
        "caching_enabled": "cachingEnabled",
        "data_trace_enabled": "dataTraceEnabled",
        "logging_level": "loggingLevel",
        "metrics_enabled": "metricsEnabled",
        "require_authorization_for_cache_control": "requireAuthorizationForCacheControl",
        "throttling_burst_limit": "throttlingBurstLimit",
        "throttling_rate_limit": "throttlingRateLimit",
        "unauthorized_cache_control_header_strategy": "unauthorizedCacheControlHeaderStrategy",
    },
)
class ApiGatewayMethodSettingsSettings:
    def __init__(
        self,
        *,
        cache_data_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cache_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        caching_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data_trace_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        logging_level: typing.Optional[builtins.str] = None,
        metrics_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_authorization_for_cache_control: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        throttling_burst_limit: typing.Optional[jsii.Number] = None,
        throttling_rate_limit: typing.Optional[jsii.Number] = None,
        unauthorized_cache_control_header_strategy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cache_data_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#cache_data_encrypted ApiGatewayMethodSettings#cache_data_encrypted}.
        :param cache_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#cache_ttl_in_seconds ApiGatewayMethodSettings#cache_ttl_in_seconds}.
        :param caching_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#caching_enabled ApiGatewayMethodSettings#caching_enabled}.
        :param data_trace_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#data_trace_enabled ApiGatewayMethodSettings#data_trace_enabled}.
        :param logging_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#logging_level ApiGatewayMethodSettings#logging_level}.
        :param metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#metrics_enabled ApiGatewayMethodSettings#metrics_enabled}.
        :param require_authorization_for_cache_control: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#require_authorization_for_cache_control ApiGatewayMethodSettings#require_authorization_for_cache_control}.
        :param throttling_burst_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#throttling_burst_limit ApiGatewayMethodSettings#throttling_burst_limit}.
        :param throttling_rate_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#throttling_rate_limit ApiGatewayMethodSettings#throttling_rate_limit}.
        :param unauthorized_cache_control_header_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#unauthorized_cache_control_header_strategy ApiGatewayMethodSettings#unauthorized_cache_control_header_strategy}.
        '''
        if __debug__:
            def stub(
                *,
                cache_data_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                cache_ttl_in_seconds: typing.Optional[jsii.Number] = None,
                caching_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                data_trace_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                logging_level: typing.Optional[builtins.str] = None,
                metrics_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                require_authorization_for_cache_control: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                throttling_burst_limit: typing.Optional[jsii.Number] = None,
                throttling_rate_limit: typing.Optional[jsii.Number] = None,
                unauthorized_cache_control_header_strategy: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cache_data_encrypted", value=cache_data_encrypted, expected_type=type_hints["cache_data_encrypted"])
            check_type(argname="argument cache_ttl_in_seconds", value=cache_ttl_in_seconds, expected_type=type_hints["cache_ttl_in_seconds"])
            check_type(argname="argument caching_enabled", value=caching_enabled, expected_type=type_hints["caching_enabled"])
            check_type(argname="argument data_trace_enabled", value=data_trace_enabled, expected_type=type_hints["data_trace_enabled"])
            check_type(argname="argument logging_level", value=logging_level, expected_type=type_hints["logging_level"])
            check_type(argname="argument metrics_enabled", value=metrics_enabled, expected_type=type_hints["metrics_enabled"])
            check_type(argname="argument require_authorization_for_cache_control", value=require_authorization_for_cache_control, expected_type=type_hints["require_authorization_for_cache_control"])
            check_type(argname="argument throttling_burst_limit", value=throttling_burst_limit, expected_type=type_hints["throttling_burst_limit"])
            check_type(argname="argument throttling_rate_limit", value=throttling_rate_limit, expected_type=type_hints["throttling_rate_limit"])
            check_type(argname="argument unauthorized_cache_control_header_strategy", value=unauthorized_cache_control_header_strategy, expected_type=type_hints["unauthorized_cache_control_header_strategy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cache_data_encrypted is not None:
            self._values["cache_data_encrypted"] = cache_data_encrypted
        if cache_ttl_in_seconds is not None:
            self._values["cache_ttl_in_seconds"] = cache_ttl_in_seconds
        if caching_enabled is not None:
            self._values["caching_enabled"] = caching_enabled
        if data_trace_enabled is not None:
            self._values["data_trace_enabled"] = data_trace_enabled
        if logging_level is not None:
            self._values["logging_level"] = logging_level
        if metrics_enabled is not None:
            self._values["metrics_enabled"] = metrics_enabled
        if require_authorization_for_cache_control is not None:
            self._values["require_authorization_for_cache_control"] = require_authorization_for_cache_control
        if throttling_burst_limit is not None:
            self._values["throttling_burst_limit"] = throttling_burst_limit
        if throttling_rate_limit is not None:
            self._values["throttling_rate_limit"] = throttling_rate_limit
        if unauthorized_cache_control_header_strategy is not None:
            self._values["unauthorized_cache_control_header_strategy"] = unauthorized_cache_control_header_strategy

    @builtins.property
    def cache_data_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#cache_data_encrypted ApiGatewayMethodSettings#cache_data_encrypted}.'''
        result = self._values.get("cache_data_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cache_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#cache_ttl_in_seconds ApiGatewayMethodSettings#cache_ttl_in_seconds}.'''
        result = self._values.get("cache_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def caching_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#caching_enabled ApiGatewayMethodSettings#caching_enabled}.'''
        result = self._values.get("caching_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def data_trace_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#data_trace_enabled ApiGatewayMethodSettings#data_trace_enabled}.'''
        result = self._values.get("data_trace_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def logging_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#logging_level ApiGatewayMethodSettings#logging_level}.'''
        result = self._values.get("logging_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#metrics_enabled ApiGatewayMethodSettings#metrics_enabled}.'''
        result = self._values.get("metrics_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def require_authorization_for_cache_control(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#require_authorization_for_cache_control ApiGatewayMethodSettings#require_authorization_for_cache_control}.'''
        result = self._values.get("require_authorization_for_cache_control")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def throttling_burst_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#throttling_burst_limit ApiGatewayMethodSettings#throttling_burst_limit}.'''
        result = self._values.get("throttling_burst_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throttling_rate_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#throttling_rate_limit ApiGatewayMethodSettings#throttling_rate_limit}.'''
        result = self._values.get("throttling_rate_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unauthorized_cache_control_header_strategy(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_method_settings#unauthorized_cache_control_header_strategy ApiGatewayMethodSettings#unauthorized_cache_control_header_strategy}.'''
        result = self._values.get("unauthorized_cache_control_header_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayMethodSettingsSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiGatewayMethodSettingsSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apiGatewayMethodSettings.ApiGatewayMethodSettingsSettingsOutputReference",
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

    @jsii.member(jsii_name="resetCacheDataEncrypted")
    def reset_cache_data_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheDataEncrypted", []))

    @jsii.member(jsii_name="resetCacheTtlInSeconds")
    def reset_cache_ttl_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheTtlInSeconds", []))

    @jsii.member(jsii_name="resetCachingEnabled")
    def reset_caching_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCachingEnabled", []))

    @jsii.member(jsii_name="resetDataTraceEnabled")
    def reset_data_trace_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataTraceEnabled", []))

    @jsii.member(jsii_name="resetLoggingLevel")
    def reset_logging_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingLevel", []))

    @jsii.member(jsii_name="resetMetricsEnabled")
    def reset_metrics_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsEnabled", []))

    @jsii.member(jsii_name="resetRequireAuthorizationForCacheControl")
    def reset_require_authorization_for_cache_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireAuthorizationForCacheControl", []))

    @jsii.member(jsii_name="resetThrottlingBurstLimit")
    def reset_throttling_burst_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThrottlingBurstLimit", []))

    @jsii.member(jsii_name="resetThrottlingRateLimit")
    def reset_throttling_rate_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThrottlingRateLimit", []))

    @jsii.member(jsii_name="resetUnauthorizedCacheControlHeaderStrategy")
    def reset_unauthorized_cache_control_header_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnauthorizedCacheControlHeaderStrategy", []))

    @builtins.property
    @jsii.member(jsii_name="cacheDataEncryptedInput")
    def cache_data_encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cacheDataEncryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheTtlInSecondsInput")
    def cache_ttl_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cacheTtlInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingEnabledInput")
    def caching_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cachingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTraceEnabledInput")
    def data_trace_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dataTraceEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingLevelInput")
    def logging_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsEnabledInput")
    def metrics_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "metricsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="requireAuthorizationForCacheControlInput")
    def require_authorization_for_cache_control_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireAuthorizationForCacheControlInput"))

    @builtins.property
    @jsii.member(jsii_name="throttlingBurstLimitInput")
    def throttling_burst_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throttlingBurstLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="throttlingRateLimitInput")
    def throttling_rate_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throttlingRateLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="unauthorizedCacheControlHeaderStrategyInput")
    def unauthorized_cache_control_header_strategy_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unauthorizedCacheControlHeaderStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheDataEncrypted")
    def cache_data_encrypted(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cacheDataEncrypted"))

    @cache_data_encrypted.setter
    def cache_data_encrypted(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheDataEncrypted", value)

    @builtins.property
    @jsii.member(jsii_name="cacheTtlInSeconds")
    def cache_ttl_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cacheTtlInSeconds"))

    @cache_ttl_in_seconds.setter
    def cache_ttl_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="cachingEnabled")
    def caching_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cachingEnabled"))

    @caching_enabled.setter
    def caching_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="dataTraceEnabled")
    def data_trace_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dataTraceEnabled"))

    @data_trace_enabled.setter
    def data_trace_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTraceEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="loggingLevel")
    def logging_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loggingLevel"))

    @logging_level.setter
    def logging_level(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingLevel", value)

    @builtins.property
    @jsii.member(jsii_name="metricsEnabled")
    def metrics_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "metricsEnabled"))

    @metrics_enabled.setter
    def metrics_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="requireAuthorizationForCacheControl")
    def require_authorization_for_cache_control(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireAuthorizationForCacheControl"))

    @require_authorization_for_cache_control.setter
    def require_authorization_for_cache_control(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireAuthorizationForCacheControl", value)

    @builtins.property
    @jsii.member(jsii_name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throttlingBurstLimit"))

    @throttling_burst_limit.setter
    def throttling_burst_limit(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throttlingBurstLimit", value)

    @builtins.property
    @jsii.member(jsii_name="throttlingRateLimit")
    def throttling_rate_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throttlingRateLimit"))

    @throttling_rate_limit.setter
    def throttling_rate_limit(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throttlingRateLimit", value)

    @builtins.property
    @jsii.member(jsii_name="unauthorizedCacheControlHeaderStrategy")
    def unauthorized_cache_control_header_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unauthorizedCacheControlHeaderStrategy"))

    @unauthorized_cache_control_header_strategy.setter
    def unauthorized_cache_control_header_strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unauthorizedCacheControlHeaderStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiGatewayMethodSettingsSettings]:
        return typing.cast(typing.Optional[ApiGatewayMethodSettingsSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiGatewayMethodSettingsSettings],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[ApiGatewayMethodSettingsSettings]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiGatewayMethodSettings",
    "ApiGatewayMethodSettingsConfig",
    "ApiGatewayMethodSettingsSettings",
    "ApiGatewayMethodSettingsSettingsOutputReference",
]

publication.publish()
