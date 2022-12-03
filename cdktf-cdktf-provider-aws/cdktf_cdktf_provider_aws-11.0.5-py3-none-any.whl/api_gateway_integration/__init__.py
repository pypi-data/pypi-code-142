'''
# `aws_api_gateway_integration`

Refer to the Terraform Registory for docs: [`aws_api_gateway_integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration).
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


class ApiGatewayIntegration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apiGatewayIntegration.ApiGatewayIntegration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration aws_api_gateway_integration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        http_method: builtins.str,
        resource_id: builtins.str,
        rest_api_id: builtins.str,
        type: builtins.str,
        cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_namespace: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[builtins.str] = None,
        content_handling: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_http_method: typing.Optional[builtins.str] = None,
        passthrough_behavior: typing.Optional[builtins.str] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout_milliseconds: typing.Optional[jsii.Number] = None,
        tls_config: typing.Optional[typing.Union["ApiGatewayIntegrationTlsConfig", typing.Dict[str, typing.Any]]] = None,
        uri: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration aws_api_gateway_integration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#http_method ApiGatewayIntegration#http_method}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#resource_id ApiGatewayIntegration#resource_id}.
        :param rest_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#rest_api_id ApiGatewayIntegration#rest_api_id}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#type ApiGatewayIntegration#type}.
        :param cache_key_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#cache_key_parameters ApiGatewayIntegration#cache_key_parameters}.
        :param cache_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#cache_namespace ApiGatewayIntegration#cache_namespace}.
        :param connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#connection_id ApiGatewayIntegration#connection_id}.
        :param connection_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#connection_type ApiGatewayIntegration#connection_type}.
        :param content_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#content_handling ApiGatewayIntegration#content_handling}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#credentials ApiGatewayIntegration#credentials}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#id ApiGatewayIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#integration_http_method ApiGatewayIntegration#integration_http_method}.
        :param passthrough_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#passthrough_behavior ApiGatewayIntegration#passthrough_behavior}.
        :param request_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#request_parameters ApiGatewayIntegration#request_parameters}.
        :param request_templates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#request_templates ApiGatewayIntegration#request_templates}.
        :param timeout_milliseconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#timeout_milliseconds ApiGatewayIntegration#timeout_milliseconds}.
        :param tls_config: tls_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#tls_config ApiGatewayIntegration#tls_config}
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#uri ApiGatewayIntegration#uri}.
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
                http_method: builtins.str,
                resource_id: builtins.str,
                rest_api_id: builtins.str,
                type: builtins.str,
                cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
                cache_namespace: typing.Optional[builtins.str] = None,
                connection_id: typing.Optional[builtins.str] = None,
                connection_type: typing.Optional[builtins.str] = None,
                content_handling: typing.Optional[builtins.str] = None,
                credentials: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                integration_http_method: typing.Optional[builtins.str] = None,
                passthrough_behavior: typing.Optional[builtins.str] = None,
                request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeout_milliseconds: typing.Optional[jsii.Number] = None,
                tls_config: typing.Optional[typing.Union[ApiGatewayIntegrationTlsConfig, typing.Dict[str, typing.Any]]] = None,
                uri: typing.Optional[builtins.str] = None,
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
        config = ApiGatewayIntegrationConfig(
            http_method=http_method,
            resource_id=resource_id,
            rest_api_id=rest_api_id,
            type=type,
            cache_key_parameters=cache_key_parameters,
            cache_namespace=cache_namespace,
            connection_id=connection_id,
            connection_type=connection_type,
            content_handling=content_handling,
            credentials=credentials,
            id=id,
            integration_http_method=integration_http_method,
            passthrough_behavior=passthrough_behavior,
            request_parameters=request_parameters,
            request_templates=request_templates,
            timeout_milliseconds=timeout_milliseconds,
            tls_config=tls_config,
            uri=uri,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTlsConfig")
    def put_tls_config(
        self,
        *,
        insecure_skip_verification: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param insecure_skip_verification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#insecure_skip_verification ApiGatewayIntegration#insecure_skip_verification}.
        '''
        value = ApiGatewayIntegrationTlsConfig(
            insecure_skip_verification=insecure_skip_verification
        )

        return typing.cast(None, jsii.invoke(self, "putTlsConfig", [value]))

    @jsii.member(jsii_name="resetCacheKeyParameters")
    def reset_cache_key_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheKeyParameters", []))

    @jsii.member(jsii_name="resetCacheNamespace")
    def reset_cache_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheNamespace", []))

    @jsii.member(jsii_name="resetConnectionId")
    def reset_connection_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionId", []))

    @jsii.member(jsii_name="resetConnectionType")
    def reset_connection_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionType", []))

    @jsii.member(jsii_name="resetContentHandling")
    def reset_content_handling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentHandling", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIntegrationHttpMethod")
    def reset_integration_http_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationHttpMethod", []))

    @jsii.member(jsii_name="resetPassthroughBehavior")
    def reset_passthrough_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassthroughBehavior", []))

    @jsii.member(jsii_name="resetRequestParameters")
    def reset_request_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestParameters", []))

    @jsii.member(jsii_name="resetRequestTemplates")
    def reset_request_templates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestTemplates", []))

    @jsii.member(jsii_name="resetTimeoutMilliseconds")
    def reset_timeout_milliseconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutMilliseconds", []))

    @jsii.member(jsii_name="resetTlsConfig")
    def reset_tls_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsConfig", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfig")
    def tls_config(self) -> "ApiGatewayIntegrationTlsConfigOutputReference":
        return typing.cast("ApiGatewayIntegrationTlsConfigOutputReference", jsii.get(self, "tlsConfig"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyParametersInput")
    def cache_key_parameters_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cacheKeyParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheNamespaceInput")
    def cache_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionIdInput")
    def connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionTypeInput")
    def connection_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="contentHandlingInput")
    def content_handling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentHandlingInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationHttpMethodInput")
    def integration_http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationHttpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="passthroughBehaviorInput")
    def passthrough_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passthroughBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="requestParametersInput")
    def request_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="requestTemplatesInput")
    def request_templates_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestTemplatesInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="restApiIdInput")
    def rest_api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restApiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutMillisecondsInput")
    def timeout_milliseconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutMillisecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfigInput")
    def tls_config_input(self) -> typing.Optional["ApiGatewayIntegrationTlsConfig"]:
        return typing.cast(typing.Optional["ApiGatewayIntegrationTlsConfig"], jsii.get(self, "tlsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyParameters")
    def cache_key_parameters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cacheKeyParameters"))

    @cache_key_parameters.setter
    def cache_key_parameters(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheKeyParameters", value)

    @builtins.property
    @jsii.member(jsii_name="cacheNamespace")
    def cache_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheNamespace"))

    @cache_namespace.setter
    def cache_namespace(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheNamespace", value)

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
    @jsii.member(jsii_name="connectionType")
    def connection_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionType"))

    @connection_type.setter
    def connection_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionType", value)

    @builtins.property
    @jsii.member(jsii_name="contentHandling")
    def content_handling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentHandling"))

    @content_handling.setter
    def content_handling(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentHandling", value)

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentials", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

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
    @jsii.member(jsii_name="integrationHttpMethod")
    def integration_http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationHttpMethod"))

    @integration_http_method.setter
    def integration_http_method(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationHttpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="passthroughBehavior")
    def passthrough_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passthroughBehavior"))

    @passthrough_behavior.setter
    def passthrough_behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passthroughBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="requestParameters")
    def request_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestParameters"))

    @request_parameters.setter
    def request_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestParameters", value)

    @builtins.property
    @jsii.member(jsii_name="requestTemplates")
    def request_templates(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestTemplates"))

    @request_templates.setter
    def request_templates(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTemplates", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

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
    @jsii.member(jsii_name="timeoutMilliseconds")
    def timeout_milliseconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutMilliseconds"))

    @timeout_milliseconds.setter
    def timeout_milliseconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutMilliseconds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apiGatewayIntegration.ApiGatewayIntegrationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "http_method": "httpMethod",
        "resource_id": "resourceId",
        "rest_api_id": "restApiId",
        "type": "type",
        "cache_key_parameters": "cacheKeyParameters",
        "cache_namespace": "cacheNamespace",
        "connection_id": "connectionId",
        "connection_type": "connectionType",
        "content_handling": "contentHandling",
        "credentials": "credentials",
        "id": "id",
        "integration_http_method": "integrationHttpMethod",
        "passthrough_behavior": "passthroughBehavior",
        "request_parameters": "requestParameters",
        "request_templates": "requestTemplates",
        "timeout_milliseconds": "timeoutMilliseconds",
        "tls_config": "tlsConfig",
        "uri": "uri",
    },
)
class ApiGatewayIntegrationConfig(cdktf.TerraformMetaArguments):
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
        http_method: builtins.str,
        resource_id: builtins.str,
        rest_api_id: builtins.str,
        type: builtins.str,
        cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_namespace: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[builtins.str] = None,
        content_handling: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_http_method: typing.Optional[builtins.str] = None,
        passthrough_behavior: typing.Optional[builtins.str] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout_milliseconds: typing.Optional[jsii.Number] = None,
        tls_config: typing.Optional[typing.Union["ApiGatewayIntegrationTlsConfig", typing.Dict[str, typing.Any]]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#http_method ApiGatewayIntegration#http_method}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#resource_id ApiGatewayIntegration#resource_id}.
        :param rest_api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#rest_api_id ApiGatewayIntegration#rest_api_id}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#type ApiGatewayIntegration#type}.
        :param cache_key_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#cache_key_parameters ApiGatewayIntegration#cache_key_parameters}.
        :param cache_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#cache_namespace ApiGatewayIntegration#cache_namespace}.
        :param connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#connection_id ApiGatewayIntegration#connection_id}.
        :param connection_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#connection_type ApiGatewayIntegration#connection_type}.
        :param content_handling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#content_handling ApiGatewayIntegration#content_handling}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#credentials ApiGatewayIntegration#credentials}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#id ApiGatewayIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#integration_http_method ApiGatewayIntegration#integration_http_method}.
        :param passthrough_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#passthrough_behavior ApiGatewayIntegration#passthrough_behavior}.
        :param request_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#request_parameters ApiGatewayIntegration#request_parameters}.
        :param request_templates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#request_templates ApiGatewayIntegration#request_templates}.
        :param timeout_milliseconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#timeout_milliseconds ApiGatewayIntegration#timeout_milliseconds}.
        :param tls_config: tls_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#tls_config ApiGatewayIntegration#tls_config}
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#uri ApiGatewayIntegration#uri}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(tls_config, dict):
            tls_config = ApiGatewayIntegrationTlsConfig(**tls_config)
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
                http_method: builtins.str,
                resource_id: builtins.str,
                rest_api_id: builtins.str,
                type: builtins.str,
                cache_key_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
                cache_namespace: typing.Optional[builtins.str] = None,
                connection_id: typing.Optional[builtins.str] = None,
                connection_type: typing.Optional[builtins.str] = None,
                content_handling: typing.Optional[builtins.str] = None,
                credentials: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                integration_http_method: typing.Optional[builtins.str] = None,
                passthrough_behavior: typing.Optional[builtins.str] = None,
                request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeout_milliseconds: typing.Optional[jsii.Number] = None,
                tls_config: typing.Optional[typing.Union[ApiGatewayIntegrationTlsConfig, typing.Dict[str, typing.Any]]] = None,
                uri: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument cache_key_parameters", value=cache_key_parameters, expected_type=type_hints["cache_key_parameters"])
            check_type(argname="argument cache_namespace", value=cache_namespace, expected_type=type_hints["cache_namespace"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument connection_type", value=connection_type, expected_type=type_hints["connection_type"])
            check_type(argname="argument content_handling", value=content_handling, expected_type=type_hints["content_handling"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument integration_http_method", value=integration_http_method, expected_type=type_hints["integration_http_method"])
            check_type(argname="argument passthrough_behavior", value=passthrough_behavior, expected_type=type_hints["passthrough_behavior"])
            check_type(argname="argument request_parameters", value=request_parameters, expected_type=type_hints["request_parameters"])
            check_type(argname="argument request_templates", value=request_templates, expected_type=type_hints["request_templates"])
            check_type(argname="argument timeout_milliseconds", value=timeout_milliseconds, expected_type=type_hints["timeout_milliseconds"])
            check_type(argname="argument tls_config", value=tls_config, expected_type=type_hints["tls_config"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "http_method": http_method,
            "resource_id": resource_id,
            "rest_api_id": rest_api_id,
            "type": type,
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
        if cache_key_parameters is not None:
            self._values["cache_key_parameters"] = cache_key_parameters
        if cache_namespace is not None:
            self._values["cache_namespace"] = cache_namespace
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if connection_type is not None:
            self._values["connection_type"] = connection_type
        if content_handling is not None:
            self._values["content_handling"] = content_handling
        if credentials is not None:
            self._values["credentials"] = credentials
        if id is not None:
            self._values["id"] = id
        if integration_http_method is not None:
            self._values["integration_http_method"] = integration_http_method
        if passthrough_behavior is not None:
            self._values["passthrough_behavior"] = passthrough_behavior
        if request_parameters is not None:
            self._values["request_parameters"] = request_parameters
        if request_templates is not None:
            self._values["request_templates"] = request_templates
        if timeout_milliseconds is not None:
            self._values["timeout_milliseconds"] = timeout_milliseconds
        if tls_config is not None:
            self._values["tls_config"] = tls_config
        if uri is not None:
            self._values["uri"] = uri

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
    def http_method(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#http_method ApiGatewayIntegration#http_method}.'''
        result = self._values.get("http_method")
        assert result is not None, "Required property 'http_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#resource_id ApiGatewayIntegration#resource_id}.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#rest_api_id ApiGatewayIntegration#rest_api_id}.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#type ApiGatewayIntegration#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cache_key_parameters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#cache_key_parameters ApiGatewayIntegration#cache_key_parameters}.'''
        result = self._values.get("cache_key_parameters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#cache_namespace ApiGatewayIntegration#cache_namespace}.'''
        result = self._values.get("cache_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#connection_id ApiGatewayIntegration#connection_id}.'''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#connection_type ApiGatewayIntegration#connection_type}.'''
        result = self._values.get("connection_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_handling(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#content_handling ApiGatewayIntegration#content_handling}.'''
        result = self._values.get("content_handling")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#credentials ApiGatewayIntegration#credentials}.'''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#id ApiGatewayIntegration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_http_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#integration_http_method ApiGatewayIntegration#integration_http_method}.'''
        result = self._values.get("integration_http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def passthrough_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#passthrough_behavior ApiGatewayIntegration#passthrough_behavior}.'''
        result = self._values.get("passthrough_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#request_parameters ApiGatewayIntegration#request_parameters}.'''
        result = self._values.get("request_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def request_templates(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#request_templates ApiGatewayIntegration#request_templates}.'''
        result = self._values.get("request_templates")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeout_milliseconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#timeout_milliseconds ApiGatewayIntegration#timeout_milliseconds}.'''
        result = self._values.get("timeout_milliseconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls_config(self) -> typing.Optional["ApiGatewayIntegrationTlsConfig"]:
        '''tls_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#tls_config ApiGatewayIntegration#tls_config}
        '''
        result = self._values.get("tls_config")
        return typing.cast(typing.Optional["ApiGatewayIntegrationTlsConfig"], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#uri ApiGatewayIntegration#uri}.'''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayIntegrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apiGatewayIntegration.ApiGatewayIntegrationTlsConfig",
    jsii_struct_bases=[],
    name_mapping={"insecure_skip_verification": "insecureSkipVerification"},
)
class ApiGatewayIntegrationTlsConfig:
    def __init__(
        self,
        *,
        insecure_skip_verification: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param insecure_skip_verification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#insecure_skip_verification ApiGatewayIntegration#insecure_skip_verification}.
        '''
        if __debug__:
            def stub(
                *,
                insecure_skip_verification: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument insecure_skip_verification", value=insecure_skip_verification, expected_type=type_hints["insecure_skip_verification"])
        self._values: typing.Dict[str, typing.Any] = {}
        if insecure_skip_verification is not None:
            self._values["insecure_skip_verification"] = insecure_skip_verification

    @builtins.property
    def insecure_skip_verification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_integration#insecure_skip_verification ApiGatewayIntegration#insecure_skip_verification}.'''
        result = self._values.get("insecure_skip_verification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayIntegrationTlsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiGatewayIntegrationTlsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apiGatewayIntegration.ApiGatewayIntegrationTlsConfigOutputReference",
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

    @jsii.member(jsii_name="resetInsecureSkipVerification")
    def reset_insecure_skip_verification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSkipVerification", []))

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerificationInput")
    def insecure_skip_verification_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureSkipVerificationInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerification")
    def insecure_skip_verification(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insecureSkipVerification"))

    @insecure_skip_verification.setter
    def insecure_skip_verification(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSkipVerification", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiGatewayIntegrationTlsConfig]:
        return typing.cast(typing.Optional[ApiGatewayIntegrationTlsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiGatewayIntegrationTlsConfig],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[ApiGatewayIntegrationTlsConfig]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiGatewayIntegration",
    "ApiGatewayIntegrationConfig",
    "ApiGatewayIntegrationTlsConfig",
    "ApiGatewayIntegrationTlsConfigOutputReference",
]

publication.publish()
