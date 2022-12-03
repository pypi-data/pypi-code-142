'''
# `aws_apigatewayv2_authorizer`

Refer to the Terraform Registory for docs: [`aws_apigatewayv2_authorizer`](https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer).
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


class Apigatewayv2Authorizer(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apigatewayv2Authorizer.Apigatewayv2Authorizer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer aws_apigatewayv2_authorizer}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        authorizer_type: builtins.str,
        name: builtins.str,
        authorizer_credentials_arn: typing.Optional[builtins.str] = None,
        authorizer_payload_format_version: typing.Optional[builtins.str] = None,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        authorizer_uri: typing.Optional[builtins.str] = None,
        enable_simple_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
        jwt_configuration: typing.Optional[typing.Union["Apigatewayv2AuthorizerJwtConfiguration", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer aws_apigatewayv2_authorizer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#api_id Apigatewayv2Authorizer#api_id}.
        :param authorizer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_type Apigatewayv2Authorizer#authorizer_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#name Apigatewayv2Authorizer#name}.
        :param authorizer_credentials_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_credentials_arn Apigatewayv2Authorizer#authorizer_credentials_arn}.
        :param authorizer_payload_format_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_payload_format_version Apigatewayv2Authorizer#authorizer_payload_format_version}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_result_ttl_in_seconds Apigatewayv2Authorizer#authorizer_result_ttl_in_seconds}.
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_uri Apigatewayv2Authorizer#authorizer_uri}.
        :param enable_simple_responses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#enable_simple_responses Apigatewayv2Authorizer#enable_simple_responses}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#id Apigatewayv2Authorizer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_sources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#identity_sources Apigatewayv2Authorizer#identity_sources}.
        :param jwt_configuration: jwt_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#jwt_configuration Apigatewayv2Authorizer#jwt_configuration}
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
                api_id: builtins.str,
                authorizer_type: builtins.str,
                name: builtins.str,
                authorizer_credentials_arn: typing.Optional[builtins.str] = None,
                authorizer_payload_format_version: typing.Optional[builtins.str] = None,
                authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
                authorizer_uri: typing.Optional[builtins.str] = None,
                enable_simple_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                identity_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
                jwt_configuration: typing.Optional[typing.Union[Apigatewayv2AuthorizerJwtConfiguration, typing.Dict[str, typing.Any]]] = None,
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
        config = Apigatewayv2AuthorizerConfig(
            api_id=api_id,
            authorizer_type=authorizer_type,
            name=name,
            authorizer_credentials_arn=authorizer_credentials_arn,
            authorizer_payload_format_version=authorizer_payload_format_version,
            authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
            authorizer_uri=authorizer_uri,
            enable_simple_responses=enable_simple_responses,
            id=id,
            identity_sources=identity_sources,
            jwt_configuration=jwt_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putJwtConfiguration")
    def put_jwt_configuration(
        self,
        *,
        audience: typing.Optional[typing.Sequence[builtins.str]] = None,
        issuer: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audience: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#audience Apigatewayv2Authorizer#audience}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#issuer Apigatewayv2Authorizer#issuer}.
        '''
        value = Apigatewayv2AuthorizerJwtConfiguration(
            audience=audience, issuer=issuer
        )

        return typing.cast(None, jsii.invoke(self, "putJwtConfiguration", [value]))

    @jsii.member(jsii_name="resetAuthorizerCredentialsArn")
    def reset_authorizer_credentials_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizerCredentialsArn", []))

    @jsii.member(jsii_name="resetAuthorizerPayloadFormatVersion")
    def reset_authorizer_payload_format_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizerPayloadFormatVersion", []))

    @jsii.member(jsii_name="resetAuthorizerResultTtlInSeconds")
    def reset_authorizer_result_ttl_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizerResultTtlInSeconds", []))

    @jsii.member(jsii_name="resetAuthorizerUri")
    def reset_authorizer_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizerUri", []))

    @jsii.member(jsii_name="resetEnableSimpleResponses")
    def reset_enable_simple_responses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSimpleResponses", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentitySources")
    def reset_identity_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentitySources", []))

    @jsii.member(jsii_name="resetJwtConfiguration")
    def reset_jwt_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJwtConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="jwtConfiguration")
    def jwt_configuration(
        self,
    ) -> "Apigatewayv2AuthorizerJwtConfigurationOutputReference":
        return typing.cast("Apigatewayv2AuthorizerJwtConfigurationOutputReference", jsii.get(self, "jwtConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerCredentialsArnInput")
    def authorizer_credentials_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerCredentialsArnInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerPayloadFormatVersionInput")
    def authorizer_payload_format_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerPayloadFormatVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSecondsInput")
    def authorizer_result_ttl_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authorizerResultTtlInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerTypeInput")
    def authorizer_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizerUriInput")
    def authorizer_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerUriInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSimpleResponsesInput")
    def enable_simple_responses_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableSimpleResponsesInput"))

    @builtins.property
    @jsii.member(jsii_name="identitySourcesInput")
    def identity_sources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identitySourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jwtConfigurationInput")
    def jwt_configuration_input(
        self,
    ) -> typing.Optional["Apigatewayv2AuthorizerJwtConfiguration"]:
        return typing.cast(typing.Optional["Apigatewayv2AuthorizerJwtConfiguration"], jsii.get(self, "jwtConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerCredentialsArn")
    def authorizer_credentials_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizerCredentialsArn"))

    @authorizer_credentials_arn.setter
    def authorizer_credentials_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerCredentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerPayloadFormatVersion")
    def authorizer_payload_format_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizerPayloadFormatVersion"))

    @authorizer_payload_format_version.setter
    def authorizer_payload_format_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerPayloadFormatVersion", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authorizerResultTtlInSeconds"))

    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerResultTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerType")
    def authorizer_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizerType"))

    @authorizer_type.setter
    def authorizer_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerType", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerUri")
    def authorizer_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizerUri"))

    @authorizer_uri.setter
    def authorizer_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerUri", value)

    @builtins.property
    @jsii.member(jsii_name="enableSimpleResponses")
    def enable_simple_responses(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableSimpleResponses"))

    @enable_simple_responses.setter
    def enable_simple_responses(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSimpleResponses", value)

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
    @jsii.member(jsii_name="identitySources")
    def identity_sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identitySources"))

    @identity_sources.setter
    def identity_sources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identitySources", value)

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
    jsii_type="@cdktf/provider-aws.apigatewayv2Authorizer.Apigatewayv2AuthorizerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_id": "apiId",
        "authorizer_type": "authorizerType",
        "name": "name",
        "authorizer_credentials_arn": "authorizerCredentialsArn",
        "authorizer_payload_format_version": "authorizerPayloadFormatVersion",
        "authorizer_result_ttl_in_seconds": "authorizerResultTtlInSeconds",
        "authorizer_uri": "authorizerUri",
        "enable_simple_responses": "enableSimpleResponses",
        "id": "id",
        "identity_sources": "identitySources",
        "jwt_configuration": "jwtConfiguration",
    },
)
class Apigatewayv2AuthorizerConfig(cdktf.TerraformMetaArguments):
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
        api_id: builtins.str,
        authorizer_type: builtins.str,
        name: builtins.str,
        authorizer_credentials_arn: typing.Optional[builtins.str] = None,
        authorizer_payload_format_version: typing.Optional[builtins.str] = None,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        authorizer_uri: typing.Optional[builtins.str] = None,
        enable_simple_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
        jwt_configuration: typing.Optional[typing.Union["Apigatewayv2AuthorizerJwtConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#api_id Apigatewayv2Authorizer#api_id}.
        :param authorizer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_type Apigatewayv2Authorizer#authorizer_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#name Apigatewayv2Authorizer#name}.
        :param authorizer_credentials_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_credentials_arn Apigatewayv2Authorizer#authorizer_credentials_arn}.
        :param authorizer_payload_format_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_payload_format_version Apigatewayv2Authorizer#authorizer_payload_format_version}.
        :param authorizer_result_ttl_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_result_ttl_in_seconds Apigatewayv2Authorizer#authorizer_result_ttl_in_seconds}.
        :param authorizer_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_uri Apigatewayv2Authorizer#authorizer_uri}.
        :param enable_simple_responses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#enable_simple_responses Apigatewayv2Authorizer#enable_simple_responses}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#id Apigatewayv2Authorizer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_sources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#identity_sources Apigatewayv2Authorizer#identity_sources}.
        :param jwt_configuration: jwt_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#jwt_configuration Apigatewayv2Authorizer#jwt_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(jwt_configuration, dict):
            jwt_configuration = Apigatewayv2AuthorizerJwtConfiguration(**jwt_configuration)
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
                api_id: builtins.str,
                authorizer_type: builtins.str,
                name: builtins.str,
                authorizer_credentials_arn: typing.Optional[builtins.str] = None,
                authorizer_payload_format_version: typing.Optional[builtins.str] = None,
                authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
                authorizer_uri: typing.Optional[builtins.str] = None,
                enable_simple_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                identity_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
                jwt_configuration: typing.Optional[typing.Union[Apigatewayv2AuthorizerJwtConfiguration, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument authorizer_type", value=authorizer_type, expected_type=type_hints["authorizer_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument authorizer_credentials_arn", value=authorizer_credentials_arn, expected_type=type_hints["authorizer_credentials_arn"])
            check_type(argname="argument authorizer_payload_format_version", value=authorizer_payload_format_version, expected_type=type_hints["authorizer_payload_format_version"])
            check_type(argname="argument authorizer_result_ttl_in_seconds", value=authorizer_result_ttl_in_seconds, expected_type=type_hints["authorizer_result_ttl_in_seconds"])
            check_type(argname="argument authorizer_uri", value=authorizer_uri, expected_type=type_hints["authorizer_uri"])
            check_type(argname="argument enable_simple_responses", value=enable_simple_responses, expected_type=type_hints["enable_simple_responses"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_sources", value=identity_sources, expected_type=type_hints["identity_sources"])
            check_type(argname="argument jwt_configuration", value=jwt_configuration, expected_type=type_hints["jwt_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "authorizer_type": authorizer_type,
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
        if authorizer_credentials_arn is not None:
            self._values["authorizer_credentials_arn"] = authorizer_credentials_arn
        if authorizer_payload_format_version is not None:
            self._values["authorizer_payload_format_version"] = authorizer_payload_format_version
        if authorizer_result_ttl_in_seconds is not None:
            self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        if authorizer_uri is not None:
            self._values["authorizer_uri"] = authorizer_uri
        if enable_simple_responses is not None:
            self._values["enable_simple_responses"] = enable_simple_responses
        if id is not None:
            self._values["id"] = id
        if identity_sources is not None:
            self._values["identity_sources"] = identity_sources
        if jwt_configuration is not None:
            self._values["jwt_configuration"] = jwt_configuration

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
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#api_id Apigatewayv2Authorizer#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_type Apigatewayv2Authorizer#authorizer_type}.'''
        result = self._values.get("authorizer_type")
        assert result is not None, "Required property 'authorizer_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#name Apigatewayv2Authorizer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_credentials_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_credentials_arn Apigatewayv2Authorizer#authorizer_credentials_arn}.'''
        result = self._values.get("authorizer_credentials_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorizer_payload_format_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_payload_format_version Apigatewayv2Authorizer#authorizer_payload_format_version}.'''
        result = self._values.get("authorizer_payload_format_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_result_ttl_in_seconds Apigatewayv2Authorizer#authorizer_result_ttl_in_seconds}.'''
        result = self._values.get("authorizer_result_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def authorizer_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#authorizer_uri Apigatewayv2Authorizer#authorizer_uri}.'''
        result = self._values.get("authorizer_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_simple_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#enable_simple_responses Apigatewayv2Authorizer#enable_simple_responses}.'''
        result = self._values.get("enable_simple_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#id Apigatewayv2Authorizer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_sources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#identity_sources Apigatewayv2Authorizer#identity_sources}.'''
        result = self._values.get("identity_sources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jwt_configuration(
        self,
    ) -> typing.Optional["Apigatewayv2AuthorizerJwtConfiguration"]:
        '''jwt_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#jwt_configuration Apigatewayv2Authorizer#jwt_configuration}
        '''
        result = self._values.get("jwt_configuration")
        return typing.cast(typing.Optional["Apigatewayv2AuthorizerJwtConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2AuthorizerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apigatewayv2Authorizer.Apigatewayv2AuthorizerJwtConfiguration",
    jsii_struct_bases=[],
    name_mapping={"audience": "audience", "issuer": "issuer"},
)
class Apigatewayv2AuthorizerJwtConfiguration:
    def __init__(
        self,
        *,
        audience: typing.Optional[typing.Sequence[builtins.str]] = None,
        issuer: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audience: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#audience Apigatewayv2Authorizer#audience}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#issuer Apigatewayv2Authorizer#issuer}.
        '''
        if __debug__:
            def stub(
                *,
                audience: typing.Optional[typing.Sequence[builtins.str]] = None,
                issuer: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument audience", value=audience, expected_type=type_hints["audience"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
        self._values: typing.Dict[str, typing.Any] = {}
        if audience is not None:
            self._values["audience"] = audience
        if issuer is not None:
            self._values["issuer"] = issuer

    @builtins.property
    def audience(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#audience Apigatewayv2Authorizer#audience}.'''
        result = self._values.get("audience")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer#issuer Apigatewayv2Authorizer#issuer}.'''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2AuthorizerJwtConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Apigatewayv2AuthorizerJwtConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apigatewayv2Authorizer.Apigatewayv2AuthorizerJwtConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetAudience")
    def reset_audience(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudience", []))

    @jsii.member(jsii_name="resetIssuer")
    def reset_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuer", []))

    @builtins.property
    @jsii.member(jsii_name="audienceInput")
    def audience_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "audienceInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="audience")
    def audience(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "audience"))

    @audience.setter
    def audience(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audience", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Apigatewayv2AuthorizerJwtConfiguration]:
        return typing.cast(typing.Optional[Apigatewayv2AuthorizerJwtConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Apigatewayv2AuthorizerJwtConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Apigatewayv2AuthorizerJwtConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Apigatewayv2Authorizer",
    "Apigatewayv2AuthorizerConfig",
    "Apigatewayv2AuthorizerJwtConfiguration",
    "Apigatewayv2AuthorizerJwtConfigurationOutputReference",
]

publication.publish()
