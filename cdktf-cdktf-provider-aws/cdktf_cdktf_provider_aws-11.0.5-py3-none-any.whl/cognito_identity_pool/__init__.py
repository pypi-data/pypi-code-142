'''
# `aws_cognito_identity_pool`

Refer to the Terraform Registory for docs: [`aws_cognito_identity_pool`](https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool).
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


class CognitoIdentityPool(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoIdentityPool.CognitoIdentityPool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool aws_cognito_identity_pool}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        identity_pool_name: builtins.str,
        allow_classic_flow: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_unauthenticated_identities: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cognito_identity_providers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CognitoIdentityPoolCognitoIdentityProviders", typing.Dict[str, typing.Any]]]]] = None,
        developer_provider_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        openid_connect_provider_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        saml_provider_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        supported_login_providers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool aws_cognito_identity_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#identity_pool_name CognitoIdentityPool#identity_pool_name}.
        :param allow_classic_flow: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#allow_classic_flow CognitoIdentityPool#allow_classic_flow}.
        :param allow_unauthenticated_identities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#allow_unauthenticated_identities CognitoIdentityPool#allow_unauthenticated_identities}.
        :param cognito_identity_providers: cognito_identity_providers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#cognito_identity_providers CognitoIdentityPool#cognito_identity_providers}
        :param developer_provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#developer_provider_name CognitoIdentityPool#developer_provider_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#id CognitoIdentityPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param openid_connect_provider_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#openid_connect_provider_arns CognitoIdentityPool#openid_connect_provider_arns}.
        :param saml_provider_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#saml_provider_arns CognitoIdentityPool#saml_provider_arns}.
        :param supported_login_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#supported_login_providers CognitoIdentityPool#supported_login_providers}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#tags CognitoIdentityPool#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#tags_all CognitoIdentityPool#tags_all}.
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
                identity_pool_name: builtins.str,
                allow_classic_flow: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                allow_unauthenticated_identities: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                cognito_identity_providers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CognitoIdentityPoolCognitoIdentityProviders, typing.Dict[str, typing.Any]]]]] = None,
                developer_provider_name: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                openid_connect_provider_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
                saml_provider_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
                supported_login_providers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
        config = CognitoIdentityPoolConfig(
            identity_pool_name=identity_pool_name,
            allow_classic_flow=allow_classic_flow,
            allow_unauthenticated_identities=allow_unauthenticated_identities,
            cognito_identity_providers=cognito_identity_providers,
            developer_provider_name=developer_provider_name,
            id=id,
            openid_connect_provider_arns=openid_connect_provider_arns,
            saml_provider_arns=saml_provider_arns,
            supported_login_providers=supported_login_providers,
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

    @jsii.member(jsii_name="putCognitoIdentityProviders")
    def put_cognito_identity_providers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CognitoIdentityPoolCognitoIdentityProviders", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CognitoIdentityPoolCognitoIdentityProviders, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCognitoIdentityProviders", [value]))

    @jsii.member(jsii_name="resetAllowClassicFlow")
    def reset_allow_classic_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowClassicFlow", []))

    @jsii.member(jsii_name="resetAllowUnauthenticatedIdentities")
    def reset_allow_unauthenticated_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowUnauthenticatedIdentities", []))

    @jsii.member(jsii_name="resetCognitoIdentityProviders")
    def reset_cognito_identity_providers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCognitoIdentityProviders", []))

    @jsii.member(jsii_name="resetDeveloperProviderName")
    def reset_developer_provider_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeveloperProviderName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOpenidConnectProviderArns")
    def reset_openid_connect_provider_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenidConnectProviderArns", []))

    @jsii.member(jsii_name="resetSamlProviderArns")
    def reset_saml_provider_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamlProviderArns", []))

    @jsii.member(jsii_name="resetSupportedLoginProviders")
    def reset_supported_login_providers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportedLoginProviders", []))

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
    @jsii.member(jsii_name="cognitoIdentityProviders")
    def cognito_identity_providers(
        self,
    ) -> "CognitoIdentityPoolCognitoIdentityProvidersList":
        return typing.cast("CognitoIdentityPoolCognitoIdentityProvidersList", jsii.get(self, "cognitoIdentityProviders"))

    @builtins.property
    @jsii.member(jsii_name="allowClassicFlowInput")
    def allow_classic_flow_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowClassicFlowInput"))

    @builtins.property
    @jsii.member(jsii_name="allowUnauthenticatedIdentitiesInput")
    def allow_unauthenticated_identities_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowUnauthenticatedIdentitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="cognitoIdentityProvidersInput")
    def cognito_identity_providers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CognitoIdentityPoolCognitoIdentityProviders"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CognitoIdentityPoolCognitoIdentityProviders"]]], jsii.get(self, "cognitoIdentityProvidersInput"))

    @builtins.property
    @jsii.member(jsii_name="developerProviderNameInput")
    def developer_provider_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "developerProviderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityPoolNameInput")
    def identity_pool_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityPoolNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="openidConnectProviderArnsInput")
    def openid_connect_provider_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "openidConnectProviderArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="samlProviderArnsInput")
    def saml_provider_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "samlProviderArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="supportedLoginProvidersInput")
    def supported_login_providers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "supportedLoginProvidersInput"))

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
    @jsii.member(jsii_name="allowClassicFlow")
    def allow_classic_flow(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowClassicFlow"))

    @allow_classic_flow.setter
    def allow_classic_flow(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowClassicFlow", value)

    @builtins.property
    @jsii.member(jsii_name="allowUnauthenticatedIdentities")
    def allow_unauthenticated_identities(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowUnauthenticatedIdentities"))

    @allow_unauthenticated_identities.setter
    def allow_unauthenticated_identities(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowUnauthenticatedIdentities", value)

    @builtins.property
    @jsii.member(jsii_name="developerProviderName")
    def developer_provider_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "developerProviderName"))

    @developer_provider_name.setter
    def developer_provider_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "developerProviderName", value)

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
    @jsii.member(jsii_name="identityPoolName")
    def identity_pool_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityPoolName"))

    @identity_pool_name.setter
    def identity_pool_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityPoolName", value)

    @builtins.property
    @jsii.member(jsii_name="openidConnectProviderArns")
    def openid_connect_provider_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "openidConnectProviderArns"))

    @openid_connect_provider_arns.setter
    def openid_connect_provider_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openidConnectProviderArns", value)

    @builtins.property
    @jsii.member(jsii_name="samlProviderArns")
    def saml_provider_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "samlProviderArns"))

    @saml_provider_arns.setter
    def saml_provider_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samlProviderArns", value)

    @builtins.property
    @jsii.member(jsii_name="supportedLoginProviders")
    def supported_login_providers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "supportedLoginProviders"))

    @supported_login_providers.setter
    def supported_login_providers(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportedLoginProviders", value)

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
    jsii_type="@cdktf/provider-aws.cognitoIdentityPool.CognitoIdentityPoolCognitoIdentityProviders",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "provider_name": "providerName",
        "server_side_token_check": "serverSideTokenCheck",
    },
)
class CognitoIdentityPoolCognitoIdentityProviders:
    def __init__(
        self,
        *,
        client_id: typing.Optional[builtins.str] = None,
        provider_name: typing.Optional[builtins.str] = None,
        server_side_token_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#client_id CognitoIdentityPool#client_id}.
        :param provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#provider_name CognitoIdentityPool#provider_name}.
        :param server_side_token_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#server_side_token_check CognitoIdentityPool#server_side_token_check}.
        '''
        if __debug__:
            def stub(
                *,
                client_id: typing.Optional[builtins.str] = None,
                provider_name: typing.Optional[builtins.str] = None,
                server_side_token_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument server_side_token_check", value=server_side_token_check, expected_type=type_hints["server_side_token_check"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_id is not None:
            self._values["client_id"] = client_id
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if server_side_token_check is not None:
            self._values["server_side_token_check"] = server_side_token_check

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#client_id CognitoIdentityPool#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#provider_name CognitoIdentityPool#provider_name}.'''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_token_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#server_side_token_check CognitoIdentityPool#server_side_token_check}.'''
        result = self._values.get("server_side_token_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoIdentityPoolCognitoIdentityProviders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoIdentityPoolCognitoIdentityProvidersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoIdentityPool.CognitoIdentityPoolCognitoIdentityProvidersList",
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
    ) -> "CognitoIdentityPoolCognitoIdentityProvidersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CognitoIdentityPoolCognitoIdentityProvidersOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CognitoIdentityPoolCognitoIdentityProviders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CognitoIdentityPoolCognitoIdentityProviders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CognitoIdentityPoolCognitoIdentityProviders]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CognitoIdentityPoolCognitoIdentityProviders]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoIdentityPoolCognitoIdentityProvidersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cognitoIdentityPool.CognitoIdentityPoolCognitoIdentityProvidersOutputReference",
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

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetProviderName")
    def reset_provider_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProviderName", []))

    @jsii.member(jsii_name="resetServerSideTokenCheck")
    def reset_server_side_token_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideTokenCheck", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="providerNameInput")
    def provider_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideTokenCheckInput")
    def server_side_token_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "serverSideTokenCheckInput"))

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
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerName"))

    @provider_name.setter
    def provider_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerName", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideTokenCheck")
    def server_side_token_check(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "serverSideTokenCheck"))

    @server_side_token_check.setter
    def server_side_token_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideTokenCheck", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CognitoIdentityPoolCognitoIdentityProviders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CognitoIdentityPoolCognitoIdentityProviders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CognitoIdentityPoolCognitoIdentityProviders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CognitoIdentityPoolCognitoIdentityProviders, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cognitoIdentityPool.CognitoIdentityPoolConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "identity_pool_name": "identityPoolName",
        "allow_classic_flow": "allowClassicFlow",
        "allow_unauthenticated_identities": "allowUnauthenticatedIdentities",
        "cognito_identity_providers": "cognitoIdentityProviders",
        "developer_provider_name": "developerProviderName",
        "id": "id",
        "openid_connect_provider_arns": "openidConnectProviderArns",
        "saml_provider_arns": "samlProviderArns",
        "supported_login_providers": "supportedLoginProviders",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CognitoIdentityPoolConfig(cdktf.TerraformMetaArguments):
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
        identity_pool_name: builtins.str,
        allow_classic_flow: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_unauthenticated_identities: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cognito_identity_providers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CognitoIdentityPoolCognitoIdentityProviders, typing.Dict[str, typing.Any]]]]] = None,
        developer_provider_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        openid_connect_provider_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        saml_provider_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        supported_login_providers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
        :param identity_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#identity_pool_name CognitoIdentityPool#identity_pool_name}.
        :param allow_classic_flow: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#allow_classic_flow CognitoIdentityPool#allow_classic_flow}.
        :param allow_unauthenticated_identities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#allow_unauthenticated_identities CognitoIdentityPool#allow_unauthenticated_identities}.
        :param cognito_identity_providers: cognito_identity_providers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#cognito_identity_providers CognitoIdentityPool#cognito_identity_providers}
        :param developer_provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#developer_provider_name CognitoIdentityPool#developer_provider_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#id CognitoIdentityPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param openid_connect_provider_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#openid_connect_provider_arns CognitoIdentityPool#openid_connect_provider_arns}.
        :param saml_provider_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#saml_provider_arns CognitoIdentityPool#saml_provider_arns}.
        :param supported_login_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#supported_login_providers CognitoIdentityPool#supported_login_providers}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#tags CognitoIdentityPool#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#tags_all CognitoIdentityPool#tags_all}.
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
                identity_pool_name: builtins.str,
                allow_classic_flow: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                allow_unauthenticated_identities: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                cognito_identity_providers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CognitoIdentityPoolCognitoIdentityProviders, typing.Dict[str, typing.Any]]]]] = None,
                developer_provider_name: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                openid_connect_provider_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
                saml_provider_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
                supported_login_providers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
            check_type(argname="argument identity_pool_name", value=identity_pool_name, expected_type=type_hints["identity_pool_name"])
            check_type(argname="argument allow_classic_flow", value=allow_classic_flow, expected_type=type_hints["allow_classic_flow"])
            check_type(argname="argument allow_unauthenticated_identities", value=allow_unauthenticated_identities, expected_type=type_hints["allow_unauthenticated_identities"])
            check_type(argname="argument cognito_identity_providers", value=cognito_identity_providers, expected_type=type_hints["cognito_identity_providers"])
            check_type(argname="argument developer_provider_name", value=developer_provider_name, expected_type=type_hints["developer_provider_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument openid_connect_provider_arns", value=openid_connect_provider_arns, expected_type=type_hints["openid_connect_provider_arns"])
            check_type(argname="argument saml_provider_arns", value=saml_provider_arns, expected_type=type_hints["saml_provider_arns"])
            check_type(argname="argument supported_login_providers", value=supported_login_providers, expected_type=type_hints["supported_login_providers"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_pool_name": identity_pool_name,
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
        if allow_classic_flow is not None:
            self._values["allow_classic_flow"] = allow_classic_flow
        if allow_unauthenticated_identities is not None:
            self._values["allow_unauthenticated_identities"] = allow_unauthenticated_identities
        if cognito_identity_providers is not None:
            self._values["cognito_identity_providers"] = cognito_identity_providers
        if developer_provider_name is not None:
            self._values["developer_provider_name"] = developer_provider_name
        if id is not None:
            self._values["id"] = id
        if openid_connect_provider_arns is not None:
            self._values["openid_connect_provider_arns"] = openid_connect_provider_arns
        if saml_provider_arns is not None:
            self._values["saml_provider_arns"] = saml_provider_arns
        if supported_login_providers is not None:
            self._values["supported_login_providers"] = supported_login_providers
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
    def identity_pool_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#identity_pool_name CognitoIdentityPool#identity_pool_name}.'''
        result = self._values.get("identity_pool_name")
        assert result is not None, "Required property 'identity_pool_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_classic_flow(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#allow_classic_flow CognitoIdentityPool#allow_classic_flow}.'''
        result = self._values.get("allow_classic_flow")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_unauthenticated_identities(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#allow_unauthenticated_identities CognitoIdentityPool#allow_unauthenticated_identities}.'''
        result = self._values.get("allow_unauthenticated_identities")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cognito_identity_providers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CognitoIdentityPoolCognitoIdentityProviders]]]:
        '''cognito_identity_providers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#cognito_identity_providers CognitoIdentityPool#cognito_identity_providers}
        '''
        result = self._values.get("cognito_identity_providers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CognitoIdentityPoolCognitoIdentityProviders]]], result)

    @builtins.property
    def developer_provider_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#developer_provider_name CognitoIdentityPool#developer_provider_name}.'''
        result = self._values.get("developer_provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#id CognitoIdentityPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def openid_connect_provider_arns(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#openid_connect_provider_arns CognitoIdentityPool#openid_connect_provider_arns}.'''
        result = self._values.get("openid_connect_provider_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def saml_provider_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#saml_provider_arns CognitoIdentityPool#saml_provider_arns}.'''
        result = self._values.get("saml_provider_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def supported_login_providers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#supported_login_providers CognitoIdentityPool#supported_login_providers}.'''
        result = self._values.get("supported_login_providers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#tags CognitoIdentityPool#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_identity_pool#tags_all CognitoIdentityPool#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoIdentityPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CognitoIdentityPool",
    "CognitoIdentityPoolCognitoIdentityProviders",
    "CognitoIdentityPoolCognitoIdentityProvidersList",
    "CognitoIdentityPoolCognitoIdentityProvidersOutputReference",
    "CognitoIdentityPoolConfig",
]

publication.publish()
