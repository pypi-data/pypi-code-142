'''
# `aws_api_gateway_domain_name`

Refer to the Terraform Registory for docs: [`aws_api_gateway_domain_name`](https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name).
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


class ApiGatewayDomainName(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apiGatewayDomainName.ApiGatewayDomainName",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name aws_api_gateway_domain_name}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        certificate_body: typing.Optional[builtins.str] = None,
        certificate_chain: typing.Optional[builtins.str] = None,
        certificate_name: typing.Optional[builtins.str] = None,
        certificate_private_key: typing.Optional[builtins.str] = None,
        endpoint_configuration: typing.Optional[typing.Union["ApiGatewayDomainNameEndpointConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        mutual_tls_authentication: typing.Optional[typing.Union["ApiGatewayDomainNameMutualTlsAuthentication", typing.Dict[str, typing.Any]]] = None,
        ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
        regional_certificate_arn: typing.Optional[builtins.str] = None,
        regional_certificate_name: typing.Optional[builtins.str] = None,
        security_policy: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name aws_api_gateway_domain_name} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#domain_name ApiGatewayDomainName#domain_name}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_arn ApiGatewayDomainName#certificate_arn}.
        :param certificate_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_body ApiGatewayDomainName#certificate_body}.
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_chain ApiGatewayDomainName#certificate_chain}.
        :param certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_name ApiGatewayDomainName#certificate_name}.
        :param certificate_private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_private_key ApiGatewayDomainName#certificate_private_key}.
        :param endpoint_configuration: endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#endpoint_configuration ApiGatewayDomainName#endpoint_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#id ApiGatewayDomainName#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mutual_tls_authentication: mutual_tls_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#mutual_tls_authentication ApiGatewayDomainName#mutual_tls_authentication}
        :param ownership_verification_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#ownership_verification_certificate_arn ApiGatewayDomainName#ownership_verification_certificate_arn}.
        :param regional_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_arn ApiGatewayDomainName#regional_certificate_arn}.
        :param regional_certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_name ApiGatewayDomainName#regional_certificate_name}.
        :param security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#security_policy ApiGatewayDomainName#security_policy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags ApiGatewayDomainName#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags_all ApiGatewayDomainName#tags_all}.
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
                domain_name: builtins.str,
                certificate_arn: typing.Optional[builtins.str] = None,
                certificate_body: typing.Optional[builtins.str] = None,
                certificate_chain: typing.Optional[builtins.str] = None,
                certificate_name: typing.Optional[builtins.str] = None,
                certificate_private_key: typing.Optional[builtins.str] = None,
                endpoint_configuration: typing.Optional[typing.Union[ApiGatewayDomainNameEndpointConfiguration, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                mutual_tls_authentication: typing.Optional[typing.Union[ApiGatewayDomainNameMutualTlsAuthentication, typing.Dict[str, typing.Any]]] = None,
                ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
                regional_certificate_arn: typing.Optional[builtins.str] = None,
                regional_certificate_name: typing.Optional[builtins.str] = None,
                security_policy: typing.Optional[builtins.str] = None,
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
        config = ApiGatewayDomainNameConfig(
            domain_name=domain_name,
            certificate_arn=certificate_arn,
            certificate_body=certificate_body,
            certificate_chain=certificate_chain,
            certificate_name=certificate_name,
            certificate_private_key=certificate_private_key,
            endpoint_configuration=endpoint_configuration,
            id=id,
            mutual_tls_authentication=mutual_tls_authentication,
            ownership_verification_certificate_arn=ownership_verification_certificate_arn,
            regional_certificate_arn=regional_certificate_arn,
            regional_certificate_name=regional_certificate_name,
            security_policy=security_policy,
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

    @jsii.member(jsii_name="putEndpointConfiguration")
    def put_endpoint_configuration(
        self,
        *,
        types: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#types ApiGatewayDomainName#types}.
        '''
        value = ApiGatewayDomainNameEndpointConfiguration(types=types)

        return typing.cast(None, jsii.invoke(self, "putEndpointConfiguration", [value]))

    @jsii.member(jsii_name="putMutualTlsAuthentication")
    def put_mutual_tls_authentication(
        self,
        *,
        truststore_uri: builtins.str,
        truststore_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param truststore_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_uri ApiGatewayDomainName#truststore_uri}.
        :param truststore_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_version ApiGatewayDomainName#truststore_version}.
        '''
        value = ApiGatewayDomainNameMutualTlsAuthentication(
            truststore_uri=truststore_uri, truststore_version=truststore_version
        )

        return typing.cast(None, jsii.invoke(self, "putMutualTlsAuthentication", [value]))

    @jsii.member(jsii_name="resetCertificateArn")
    def reset_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateArn", []))

    @jsii.member(jsii_name="resetCertificateBody")
    def reset_certificate_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateBody", []))

    @jsii.member(jsii_name="resetCertificateChain")
    def reset_certificate_chain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateChain", []))

    @jsii.member(jsii_name="resetCertificateName")
    def reset_certificate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateName", []))

    @jsii.member(jsii_name="resetCertificatePrivateKey")
    def reset_certificate_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePrivateKey", []))

    @jsii.member(jsii_name="resetEndpointConfiguration")
    def reset_endpoint_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMutualTlsAuthentication")
    def reset_mutual_tls_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMutualTlsAuthentication", []))

    @jsii.member(jsii_name="resetOwnershipVerificationCertificateArn")
    def reset_ownership_verification_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwnershipVerificationCertificateArn", []))

    @jsii.member(jsii_name="resetRegionalCertificateArn")
    def reset_regional_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionalCertificateArn", []))

    @jsii.member(jsii_name="resetRegionalCertificateName")
    def reset_regional_certificate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionalCertificateName", []))

    @jsii.member(jsii_name="resetSecurityPolicy")
    def reset_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityPolicy", []))

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
    @jsii.member(jsii_name="certificateUploadDate")
    def certificate_upload_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateUploadDate"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontDomainName")
    def cloudfront_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudfrontDomainName"))

    @builtins.property
    @jsii.member(jsii_name="cloudfrontZoneId")
    def cloudfront_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudfrontZoneId"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> "ApiGatewayDomainNameEndpointConfigurationOutputReference":
        return typing.cast("ApiGatewayDomainNameEndpointConfigurationOutputReference", jsii.get(self, "endpointConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> "ApiGatewayDomainNameMutualTlsAuthenticationOutputReference":
        return typing.cast("ApiGatewayDomainNameMutualTlsAuthenticationOutputReference", jsii.get(self, "mutualTlsAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="regionalDomainName")
    def regional_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionalDomainName"))

    @builtins.property
    @jsii.member(jsii_name="regionalZoneId")
    def regional_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionalZoneId"))

    @builtins.property
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateBodyInput")
    def certificate_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateNameInput")
    def certificate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePrivateKeyInput")
    def certificate_private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePrivateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfigurationInput")
    def endpoint_configuration_input(
        self,
    ) -> typing.Optional["ApiGatewayDomainNameEndpointConfiguration"]:
        return typing.cast(typing.Optional["ApiGatewayDomainNameEndpointConfiguration"], jsii.get(self, "endpointConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mutualTlsAuthenticationInput")
    def mutual_tls_authentication_input(
        self,
    ) -> typing.Optional["ApiGatewayDomainNameMutualTlsAuthentication"]:
        return typing.cast(typing.Optional["ApiGatewayDomainNameMutualTlsAuthentication"], jsii.get(self, "mutualTlsAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="ownershipVerificationCertificateArnInput")
    def ownership_verification_certificate_arn_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownershipVerificationCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="regionalCertificateArnInput")
    def regional_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionalCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="regionalCertificateNameInput")
    def regional_certificate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionalCertificateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyInput")
    def security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyInput"))

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
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="certificateBody")
    def certificate_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateBody"))

    @certificate_body.setter
    def certificate_body(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateBody", value)

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="certificateName")
    def certificate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateName"))

    @certificate_name.setter
    def certificate_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateName", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePrivateKey")
    def certificate_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePrivateKey"))

    @certificate_private_key.setter
    def certificate_private_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

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
    @jsii.member(jsii_name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownershipVerificationCertificateArn"))

    @ownership_verification_certificate_arn.setter
    def ownership_verification_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownershipVerificationCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="regionalCertificateArn")
    def regional_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionalCertificateArn"))

    @regional_certificate_arn.setter
    def regional_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionalCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="regionalCertificateName")
    def regional_certificate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionalCertificateName"))

    @regional_certificate_name.setter
    def regional_certificate_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionalCertificateName", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicy")
    def security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicy"))

    @security_policy.setter
    def security_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicy", value)

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
    jsii_type="@cdktf/provider-aws.apiGatewayDomainName.ApiGatewayDomainNameConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain_name": "domainName",
        "certificate_arn": "certificateArn",
        "certificate_body": "certificateBody",
        "certificate_chain": "certificateChain",
        "certificate_name": "certificateName",
        "certificate_private_key": "certificatePrivateKey",
        "endpoint_configuration": "endpointConfiguration",
        "id": "id",
        "mutual_tls_authentication": "mutualTlsAuthentication",
        "ownership_verification_certificate_arn": "ownershipVerificationCertificateArn",
        "regional_certificate_arn": "regionalCertificateArn",
        "regional_certificate_name": "regionalCertificateName",
        "security_policy": "securityPolicy",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ApiGatewayDomainNameConfig(cdktf.TerraformMetaArguments):
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
        domain_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        certificate_body: typing.Optional[builtins.str] = None,
        certificate_chain: typing.Optional[builtins.str] = None,
        certificate_name: typing.Optional[builtins.str] = None,
        certificate_private_key: typing.Optional[builtins.str] = None,
        endpoint_configuration: typing.Optional[typing.Union["ApiGatewayDomainNameEndpointConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        mutual_tls_authentication: typing.Optional[typing.Union["ApiGatewayDomainNameMutualTlsAuthentication", typing.Dict[str, typing.Any]]] = None,
        ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
        regional_certificate_arn: typing.Optional[builtins.str] = None,
        regional_certificate_name: typing.Optional[builtins.str] = None,
        security_policy: typing.Optional[builtins.str] = None,
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
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#domain_name ApiGatewayDomainName#domain_name}.
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_arn ApiGatewayDomainName#certificate_arn}.
        :param certificate_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_body ApiGatewayDomainName#certificate_body}.
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_chain ApiGatewayDomainName#certificate_chain}.
        :param certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_name ApiGatewayDomainName#certificate_name}.
        :param certificate_private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_private_key ApiGatewayDomainName#certificate_private_key}.
        :param endpoint_configuration: endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#endpoint_configuration ApiGatewayDomainName#endpoint_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#id ApiGatewayDomainName#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mutual_tls_authentication: mutual_tls_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#mutual_tls_authentication ApiGatewayDomainName#mutual_tls_authentication}
        :param ownership_verification_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#ownership_verification_certificate_arn ApiGatewayDomainName#ownership_verification_certificate_arn}.
        :param regional_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_arn ApiGatewayDomainName#regional_certificate_arn}.
        :param regional_certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_name ApiGatewayDomainName#regional_certificate_name}.
        :param security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#security_policy ApiGatewayDomainName#security_policy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags ApiGatewayDomainName#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags_all ApiGatewayDomainName#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(endpoint_configuration, dict):
            endpoint_configuration = ApiGatewayDomainNameEndpointConfiguration(**endpoint_configuration)
        if isinstance(mutual_tls_authentication, dict):
            mutual_tls_authentication = ApiGatewayDomainNameMutualTlsAuthentication(**mutual_tls_authentication)
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
                domain_name: builtins.str,
                certificate_arn: typing.Optional[builtins.str] = None,
                certificate_body: typing.Optional[builtins.str] = None,
                certificate_chain: typing.Optional[builtins.str] = None,
                certificate_name: typing.Optional[builtins.str] = None,
                certificate_private_key: typing.Optional[builtins.str] = None,
                endpoint_configuration: typing.Optional[typing.Union[ApiGatewayDomainNameEndpointConfiguration, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                mutual_tls_authentication: typing.Optional[typing.Union[ApiGatewayDomainNameMutualTlsAuthentication, typing.Dict[str, typing.Any]]] = None,
                ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
                regional_certificate_arn: typing.Optional[builtins.str] = None,
                regional_certificate_name: typing.Optional[builtins.str] = None,
                security_policy: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument certificate_body", value=certificate_body, expected_type=type_hints["certificate_body"])
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument certificate_private_key", value=certificate_private_key, expected_type=type_hints["certificate_private_key"])
            check_type(argname="argument endpoint_configuration", value=endpoint_configuration, expected_type=type_hints["endpoint_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mutual_tls_authentication", value=mutual_tls_authentication, expected_type=type_hints["mutual_tls_authentication"])
            check_type(argname="argument ownership_verification_certificate_arn", value=ownership_verification_certificate_arn, expected_type=type_hints["ownership_verification_certificate_arn"])
            check_type(argname="argument regional_certificate_arn", value=regional_certificate_arn, expected_type=type_hints["regional_certificate_arn"])
            check_type(argname="argument regional_certificate_name", value=regional_certificate_name, expected_type=type_hints["regional_certificate_name"])
            check_type(argname="argument security_policy", value=security_policy, expected_type=type_hints["security_policy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
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
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
        if certificate_body is not None:
            self._values["certificate_body"] = certificate_body
        if certificate_chain is not None:
            self._values["certificate_chain"] = certificate_chain
        if certificate_name is not None:
            self._values["certificate_name"] = certificate_name
        if certificate_private_key is not None:
            self._values["certificate_private_key"] = certificate_private_key
        if endpoint_configuration is not None:
            self._values["endpoint_configuration"] = endpoint_configuration
        if id is not None:
            self._values["id"] = id
        if mutual_tls_authentication is not None:
            self._values["mutual_tls_authentication"] = mutual_tls_authentication
        if ownership_verification_certificate_arn is not None:
            self._values["ownership_verification_certificate_arn"] = ownership_verification_certificate_arn
        if regional_certificate_arn is not None:
            self._values["regional_certificate_arn"] = regional_certificate_arn
        if regional_certificate_name is not None:
            self._values["regional_certificate_name"] = regional_certificate_name
        if security_policy is not None:
            self._values["security_policy"] = security_policy
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
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#domain_name ApiGatewayDomainName#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_arn ApiGatewayDomainName#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_body ApiGatewayDomainName#certificate_body}.'''
        result = self._values.get("certificate_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_chain ApiGatewayDomainName#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_name ApiGatewayDomainName#certificate_name}.'''
        result = self._values.get("certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_private_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#certificate_private_key ApiGatewayDomainName#certificate_private_key}.'''
        result = self._values.get("certificate_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_configuration(
        self,
    ) -> typing.Optional["ApiGatewayDomainNameEndpointConfiguration"]:
        '''endpoint_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#endpoint_configuration ApiGatewayDomainName#endpoint_configuration}
        '''
        result = self._values.get("endpoint_configuration")
        return typing.cast(typing.Optional["ApiGatewayDomainNameEndpointConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#id ApiGatewayDomainName#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mutual_tls_authentication(
        self,
    ) -> typing.Optional["ApiGatewayDomainNameMutualTlsAuthentication"]:
        '''mutual_tls_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#mutual_tls_authentication ApiGatewayDomainName#mutual_tls_authentication}
        '''
        result = self._values.get("mutual_tls_authentication")
        return typing.cast(typing.Optional["ApiGatewayDomainNameMutualTlsAuthentication"], result)

    @builtins.property
    def ownership_verification_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#ownership_verification_certificate_arn ApiGatewayDomainName#ownership_verification_certificate_arn}.'''
        result = self._values.get("ownership_verification_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regional_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_arn ApiGatewayDomainName#regional_certificate_arn}.'''
        result = self._values.get("regional_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regional_certificate_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#regional_certificate_name ApiGatewayDomainName#regional_certificate_name}.'''
        result = self._values.get("regional_certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#security_policy ApiGatewayDomainName#security_policy}.'''
        result = self._values.get("security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags ApiGatewayDomainName#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#tags_all ApiGatewayDomainName#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayDomainNameConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apiGatewayDomainName.ApiGatewayDomainNameEndpointConfiguration",
    jsii_struct_bases=[],
    name_mapping={"types": "types"},
)
class ApiGatewayDomainNameEndpointConfiguration:
    def __init__(self, *, types: typing.Sequence[builtins.str]) -> None:
        '''
        :param types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#types ApiGatewayDomainName#types}.
        '''
        if __debug__:
            def stub(*, types: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument types", value=types, expected_type=type_hints["types"])
        self._values: typing.Dict[str, typing.Any] = {
            "types": types,
        }

    @builtins.property
    def types(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#types ApiGatewayDomainName#types}.'''
        result = self._values.get("types")
        assert result is not None, "Required property 'types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayDomainNameEndpointConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiGatewayDomainNameEndpointConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apiGatewayDomainName.ApiGatewayDomainNameEndpointConfigurationOutputReference",
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
    @jsii.member(jsii_name="typesInput")
    def types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "typesInput"))

    @builtins.property
    @jsii.member(jsii_name="types")
    def types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "types"))

    @types.setter
    def types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "types", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiGatewayDomainNameEndpointConfiguration]:
        return typing.cast(typing.Optional[ApiGatewayDomainNameEndpointConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiGatewayDomainNameEndpointConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[ApiGatewayDomainNameEndpointConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.apiGatewayDomainName.ApiGatewayDomainNameMutualTlsAuthentication",
    jsii_struct_bases=[],
    name_mapping={
        "truststore_uri": "truststoreUri",
        "truststore_version": "truststoreVersion",
    },
)
class ApiGatewayDomainNameMutualTlsAuthentication:
    def __init__(
        self,
        *,
        truststore_uri: builtins.str,
        truststore_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param truststore_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_uri ApiGatewayDomainName#truststore_uri}.
        :param truststore_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_version ApiGatewayDomainName#truststore_version}.
        '''
        if __debug__:
            def stub(
                *,
                truststore_uri: builtins.str,
                truststore_version: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument truststore_uri", value=truststore_uri, expected_type=type_hints["truststore_uri"])
            check_type(argname="argument truststore_version", value=truststore_version, expected_type=type_hints["truststore_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "truststore_uri": truststore_uri,
        }
        if truststore_version is not None:
            self._values["truststore_version"] = truststore_version

    @builtins.property
    def truststore_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_uri ApiGatewayDomainName#truststore_uri}.'''
        result = self._values.get("truststore_uri")
        assert result is not None, "Required property 'truststore_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def truststore_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/api_gateway_domain_name#truststore_version ApiGatewayDomainName#truststore_version}.'''
        result = self._values.get("truststore_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayDomainNameMutualTlsAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiGatewayDomainNameMutualTlsAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.apiGatewayDomainName.ApiGatewayDomainNameMutualTlsAuthenticationOutputReference",
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

    @jsii.member(jsii_name="resetTruststoreVersion")
    def reset_truststore_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTruststoreVersion", []))

    @builtins.property
    @jsii.member(jsii_name="truststoreUriInput")
    def truststore_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststoreUriInput"))

    @builtins.property
    @jsii.member(jsii_name="truststoreVersionInput")
    def truststore_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "truststoreVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="truststoreUri")
    def truststore_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststoreUri"))

    @truststore_uri.setter
    def truststore_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststoreUri", value)

    @builtins.property
    @jsii.member(jsii_name="truststoreVersion")
    def truststore_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "truststoreVersion"))

    @truststore_version.setter
    def truststore_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "truststoreVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiGatewayDomainNameMutualTlsAuthentication]:
        return typing.cast(typing.Optional[ApiGatewayDomainNameMutualTlsAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiGatewayDomainNameMutualTlsAuthentication],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[ApiGatewayDomainNameMutualTlsAuthentication],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiGatewayDomainName",
    "ApiGatewayDomainNameConfig",
    "ApiGatewayDomainNameEndpointConfiguration",
    "ApiGatewayDomainNameEndpointConfigurationOutputReference",
    "ApiGatewayDomainNameMutualTlsAuthentication",
    "ApiGatewayDomainNameMutualTlsAuthenticationOutputReference",
]

publication.publish()
