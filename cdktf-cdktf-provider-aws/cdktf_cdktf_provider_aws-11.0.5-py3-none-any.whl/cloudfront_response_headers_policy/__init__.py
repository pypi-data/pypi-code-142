'''
# `aws_cloudfront_response_headers_policy`

Refer to the Terraform Registory for docs: [`aws_cloudfront_response_headers_policy`](https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy).
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


class CloudfrontResponseHeadersPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy aws_cloudfront_response_headers_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        cors_config: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicyCorsConfig", typing.Dict[str, typing.Any]]] = None,
        custom_headers_config: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicyCustomHeadersConfig", typing.Dict[str, typing.Any]]] = None,
        etag: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        security_headers_config: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfig", typing.Dict[str, typing.Any]]] = None,
        server_timing_headers_config: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicyServerTimingHeadersConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy aws_cloudfront_response_headers_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#name CloudfrontResponseHeadersPolicy#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#comment CloudfrontResponseHeadersPolicy#comment}.
        :param cors_config: cors_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#cors_config CloudfrontResponseHeadersPolicy#cors_config}
        :param custom_headers_config: custom_headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#custom_headers_config CloudfrontResponseHeadersPolicy#custom_headers_config}
        :param etag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#etag CloudfrontResponseHeadersPolicy#etag}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#id CloudfrontResponseHeadersPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_headers_config: security_headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#security_headers_config CloudfrontResponseHeadersPolicy#security_headers_config}
        :param server_timing_headers_config: server_timing_headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#server_timing_headers_config CloudfrontResponseHeadersPolicy#server_timing_headers_config}
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
                name: builtins.str,
                comment: typing.Optional[builtins.str] = None,
                cors_config: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyCorsConfig, typing.Dict[str, typing.Any]]] = None,
                custom_headers_config: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyCustomHeadersConfig, typing.Dict[str, typing.Any]]] = None,
                etag: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                security_headers_config: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicySecurityHeadersConfig, typing.Dict[str, typing.Any]]] = None,
                server_timing_headers_config: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyServerTimingHeadersConfig, typing.Dict[str, typing.Any]]] = None,
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
        config = CloudfrontResponseHeadersPolicyConfig(
            name=name,
            comment=comment,
            cors_config=cors_config,
            custom_headers_config=custom_headers_config,
            etag=etag,
            id=id,
            security_headers_config=security_headers_config,
            server_timing_headers_config=server_timing_headers_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCorsConfig")
    def put_cors_config(
        self,
        *,
        access_control_allow_credentials: typing.Union[builtins.bool, cdktf.IResolvable],
        access_control_allow_headers: typing.Union["CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders", typing.Dict[str, typing.Any]],
        access_control_allow_methods: typing.Union["CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods", typing.Dict[str, typing.Any]],
        access_control_allow_origins: typing.Union["CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins", typing.Dict[str, typing.Any]],
        origin_override: typing.Union[builtins.bool, cdktf.IResolvable],
        access_control_expose_headers: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders", typing.Dict[str, typing.Any]]] = None,
        access_control_max_age_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param access_control_allow_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_credentials CloudfrontResponseHeadersPolicy#access_control_allow_credentials}.
        :param access_control_allow_headers: access_control_allow_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_headers CloudfrontResponseHeadersPolicy#access_control_allow_headers}
        :param access_control_allow_methods: access_control_allow_methods block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_methods CloudfrontResponseHeadersPolicy#access_control_allow_methods}
        :param access_control_allow_origins: access_control_allow_origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_origins CloudfrontResponseHeadersPolicy#access_control_allow_origins}
        :param origin_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#origin_override CloudfrontResponseHeadersPolicy#origin_override}.
        :param access_control_expose_headers: access_control_expose_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_expose_headers CloudfrontResponseHeadersPolicy#access_control_expose_headers}
        :param access_control_max_age_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_max_age_sec CloudfrontResponseHeadersPolicy#access_control_max_age_sec}.
        '''
        value = CloudfrontResponseHeadersPolicyCorsConfig(
            access_control_allow_credentials=access_control_allow_credentials,
            access_control_allow_headers=access_control_allow_headers,
            access_control_allow_methods=access_control_allow_methods,
            access_control_allow_origins=access_control_allow_origins,
            origin_override=origin_override,
            access_control_expose_headers=access_control_expose_headers,
            access_control_max_age_sec=access_control_max_age_sec,
        )

        return typing.cast(None, jsii.invoke(self, "putCorsConfig", [value]))

    @jsii.member(jsii_name="putCustomHeadersConfig")
    def put_custom_headers_config(
        self,
        *,
        items: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudfrontResponseHeadersPolicyCustomHeadersConfigItems", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}
        '''
        value = CloudfrontResponseHeadersPolicyCustomHeadersConfig(items=items)

        return typing.cast(None, jsii.invoke(self, "putCustomHeadersConfig", [value]))

    @jsii.member(jsii_name="putSecurityHeadersConfig")
    def put_security_headers_config(
        self,
        *,
        content_security_policy: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy", typing.Dict[str, typing.Any]]] = None,
        content_type_options: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions", typing.Dict[str, typing.Any]]] = None,
        frame_options: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions", typing.Dict[str, typing.Any]]] = None,
        referrer_policy: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy", typing.Dict[str, typing.Any]]] = None,
        strict_transport_security: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity", typing.Dict[str, typing.Any]]] = None,
        xss_protection: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param content_security_policy: content_security_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#content_security_policy CloudfrontResponseHeadersPolicy#content_security_policy}
        :param content_type_options: content_type_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#content_type_options CloudfrontResponseHeadersPolicy#content_type_options}
        :param frame_options: frame_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#frame_options CloudfrontResponseHeadersPolicy#frame_options}
        :param referrer_policy: referrer_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#referrer_policy CloudfrontResponseHeadersPolicy#referrer_policy}
        :param strict_transport_security: strict_transport_security block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#strict_transport_security CloudfrontResponseHeadersPolicy#strict_transport_security}
        :param xss_protection: xss_protection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#xss_protection CloudfrontResponseHeadersPolicy#xss_protection}
        '''
        value = CloudfrontResponseHeadersPolicySecurityHeadersConfig(
            content_security_policy=content_security_policy,
            content_type_options=content_type_options,
            frame_options=frame_options,
            referrer_policy=referrer_policy,
            strict_transport_security=strict_transport_security,
            xss_protection=xss_protection,
        )

        return typing.cast(None, jsii.invoke(self, "putSecurityHeadersConfig", [value]))

    @jsii.member(jsii_name="putServerTimingHeadersConfig")
    def put_server_timing_headers_config(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        sampling_rate: jsii.Number,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#enabled CloudfrontResponseHeadersPolicy#enabled}.
        :param sampling_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#sampling_rate CloudfrontResponseHeadersPolicy#sampling_rate}.
        '''
        value = CloudfrontResponseHeadersPolicyServerTimingHeadersConfig(
            enabled=enabled, sampling_rate=sampling_rate
        )

        return typing.cast(None, jsii.invoke(self, "putServerTimingHeadersConfig", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetCorsConfig")
    def reset_cors_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorsConfig", []))

    @jsii.member(jsii_name="resetCustomHeadersConfig")
    def reset_custom_headers_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHeadersConfig", []))

    @jsii.member(jsii_name="resetEtag")
    def reset_etag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEtag", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecurityHeadersConfig")
    def reset_security_headers_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityHeadersConfig", []))

    @jsii.member(jsii_name="resetServerTimingHeadersConfig")
    def reset_server_timing_headers_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerTimingHeadersConfig", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="corsConfig")
    def cors_config(self) -> "CloudfrontResponseHeadersPolicyCorsConfigOutputReference":
        return typing.cast("CloudfrontResponseHeadersPolicyCorsConfigOutputReference", jsii.get(self, "corsConfig"))

    @builtins.property
    @jsii.member(jsii_name="customHeadersConfig")
    def custom_headers_config(
        self,
    ) -> "CloudfrontResponseHeadersPolicyCustomHeadersConfigOutputReference":
        return typing.cast("CloudfrontResponseHeadersPolicyCustomHeadersConfigOutputReference", jsii.get(self, "customHeadersConfig"))

    @builtins.property
    @jsii.member(jsii_name="securityHeadersConfig")
    def security_headers_config(
        self,
    ) -> "CloudfrontResponseHeadersPolicySecurityHeadersConfigOutputReference":
        return typing.cast("CloudfrontResponseHeadersPolicySecurityHeadersConfigOutputReference", jsii.get(self, "securityHeadersConfig"))

    @builtins.property
    @jsii.member(jsii_name="serverTimingHeadersConfig")
    def server_timing_headers_config(
        self,
    ) -> "CloudfrontResponseHeadersPolicyServerTimingHeadersConfigOutputReference":
        return typing.cast("CloudfrontResponseHeadersPolicyServerTimingHeadersConfigOutputReference", jsii.get(self, "serverTimingHeadersConfig"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="corsConfigInput")
    def cors_config_input(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicyCorsConfig"]:
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicyCorsConfig"], jsii.get(self, "corsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="customHeadersConfigInput")
    def custom_headers_config_input(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicyCustomHeadersConfig"]:
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicyCustomHeadersConfig"], jsii.get(self, "customHeadersConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="etagInput")
    def etag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "etagInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityHeadersConfigInput")
    def security_headers_config_input(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfig"]:
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfig"], jsii.get(self, "securityHeadersConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="serverTimingHeadersConfigInput")
    def server_timing_headers_config_input(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicyServerTimingHeadersConfig"]:
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicyServerTimingHeadersConfig"], jsii.get(self, "serverTimingHeadersConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @etag.setter
    def etag(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "etag", value)

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
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "comment": "comment",
        "cors_config": "corsConfig",
        "custom_headers_config": "customHeadersConfig",
        "etag": "etag",
        "id": "id",
        "security_headers_config": "securityHeadersConfig",
        "server_timing_headers_config": "serverTimingHeadersConfig",
    },
)
class CloudfrontResponseHeadersPolicyConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        cors_config: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicyCorsConfig", typing.Dict[str, typing.Any]]] = None,
        custom_headers_config: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicyCustomHeadersConfig", typing.Dict[str, typing.Any]]] = None,
        etag: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        security_headers_config: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfig", typing.Dict[str, typing.Any]]] = None,
        server_timing_headers_config: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicyServerTimingHeadersConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#name CloudfrontResponseHeadersPolicy#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#comment CloudfrontResponseHeadersPolicy#comment}.
        :param cors_config: cors_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#cors_config CloudfrontResponseHeadersPolicy#cors_config}
        :param custom_headers_config: custom_headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#custom_headers_config CloudfrontResponseHeadersPolicy#custom_headers_config}
        :param etag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#etag CloudfrontResponseHeadersPolicy#etag}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#id CloudfrontResponseHeadersPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_headers_config: security_headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#security_headers_config CloudfrontResponseHeadersPolicy#security_headers_config}
        :param server_timing_headers_config: server_timing_headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#server_timing_headers_config CloudfrontResponseHeadersPolicy#server_timing_headers_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cors_config, dict):
            cors_config = CloudfrontResponseHeadersPolicyCorsConfig(**cors_config)
        if isinstance(custom_headers_config, dict):
            custom_headers_config = CloudfrontResponseHeadersPolicyCustomHeadersConfig(**custom_headers_config)
        if isinstance(security_headers_config, dict):
            security_headers_config = CloudfrontResponseHeadersPolicySecurityHeadersConfig(**security_headers_config)
        if isinstance(server_timing_headers_config, dict):
            server_timing_headers_config = CloudfrontResponseHeadersPolicyServerTimingHeadersConfig(**server_timing_headers_config)
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
                name: builtins.str,
                comment: typing.Optional[builtins.str] = None,
                cors_config: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyCorsConfig, typing.Dict[str, typing.Any]]] = None,
                custom_headers_config: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyCustomHeadersConfig, typing.Dict[str, typing.Any]]] = None,
                etag: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                security_headers_config: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicySecurityHeadersConfig, typing.Dict[str, typing.Any]]] = None,
                server_timing_headers_config: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyServerTimingHeadersConfig, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument cors_config", value=cors_config, expected_type=type_hints["cors_config"])
            check_type(argname="argument custom_headers_config", value=custom_headers_config, expected_type=type_hints["custom_headers_config"])
            check_type(argname="argument etag", value=etag, expected_type=type_hints["etag"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument security_headers_config", value=security_headers_config, expected_type=type_hints["security_headers_config"])
            check_type(argname="argument server_timing_headers_config", value=server_timing_headers_config, expected_type=type_hints["server_timing_headers_config"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if comment is not None:
            self._values["comment"] = comment
        if cors_config is not None:
            self._values["cors_config"] = cors_config
        if custom_headers_config is not None:
            self._values["custom_headers_config"] = custom_headers_config
        if etag is not None:
            self._values["etag"] = etag
        if id is not None:
            self._values["id"] = id
        if security_headers_config is not None:
            self._values["security_headers_config"] = security_headers_config
        if server_timing_headers_config is not None:
            self._values["server_timing_headers_config"] = server_timing_headers_config

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#name CloudfrontResponseHeadersPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#comment CloudfrontResponseHeadersPolicy#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cors_config(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicyCorsConfig"]:
        '''cors_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#cors_config CloudfrontResponseHeadersPolicy#cors_config}
        '''
        result = self._values.get("cors_config")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicyCorsConfig"], result)

    @builtins.property
    def custom_headers_config(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicyCustomHeadersConfig"]:
        '''custom_headers_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#custom_headers_config CloudfrontResponseHeadersPolicy#custom_headers_config}
        '''
        result = self._values.get("custom_headers_config")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicyCustomHeadersConfig"], result)

    @builtins.property
    def etag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#etag CloudfrontResponseHeadersPolicy#etag}.'''
        result = self._values.get("etag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#id CloudfrontResponseHeadersPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_headers_config(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfig"]:
        '''security_headers_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#security_headers_config CloudfrontResponseHeadersPolicy#security_headers_config}
        '''
        result = self._values.get("security_headers_config")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfig"], result)

    @builtins.property
    def server_timing_headers_config(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicyServerTimingHeadersConfig"]:
        '''server_timing_headers_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#server_timing_headers_config CloudfrontResponseHeadersPolicy#server_timing_headers_config}
        '''
        result = self._values.get("server_timing_headers_config")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicyServerTimingHeadersConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "access_control_allow_credentials": "accessControlAllowCredentials",
        "access_control_allow_headers": "accessControlAllowHeaders",
        "access_control_allow_methods": "accessControlAllowMethods",
        "access_control_allow_origins": "accessControlAllowOrigins",
        "origin_override": "originOverride",
        "access_control_expose_headers": "accessControlExposeHeaders",
        "access_control_max_age_sec": "accessControlMaxAgeSec",
    },
)
class CloudfrontResponseHeadersPolicyCorsConfig:
    def __init__(
        self,
        *,
        access_control_allow_credentials: typing.Union[builtins.bool, cdktf.IResolvable],
        access_control_allow_headers: typing.Union["CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders", typing.Dict[str, typing.Any]],
        access_control_allow_methods: typing.Union["CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods", typing.Dict[str, typing.Any]],
        access_control_allow_origins: typing.Union["CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins", typing.Dict[str, typing.Any]],
        origin_override: typing.Union[builtins.bool, cdktf.IResolvable],
        access_control_expose_headers: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders", typing.Dict[str, typing.Any]]] = None,
        access_control_max_age_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param access_control_allow_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_credentials CloudfrontResponseHeadersPolicy#access_control_allow_credentials}.
        :param access_control_allow_headers: access_control_allow_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_headers CloudfrontResponseHeadersPolicy#access_control_allow_headers}
        :param access_control_allow_methods: access_control_allow_methods block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_methods CloudfrontResponseHeadersPolicy#access_control_allow_methods}
        :param access_control_allow_origins: access_control_allow_origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_origins CloudfrontResponseHeadersPolicy#access_control_allow_origins}
        :param origin_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#origin_override CloudfrontResponseHeadersPolicy#origin_override}.
        :param access_control_expose_headers: access_control_expose_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_expose_headers CloudfrontResponseHeadersPolicy#access_control_expose_headers}
        :param access_control_max_age_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_max_age_sec CloudfrontResponseHeadersPolicy#access_control_max_age_sec}.
        '''
        if isinstance(access_control_allow_headers, dict):
            access_control_allow_headers = CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders(**access_control_allow_headers)
        if isinstance(access_control_allow_methods, dict):
            access_control_allow_methods = CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods(**access_control_allow_methods)
        if isinstance(access_control_allow_origins, dict):
            access_control_allow_origins = CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins(**access_control_allow_origins)
        if isinstance(access_control_expose_headers, dict):
            access_control_expose_headers = CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders(**access_control_expose_headers)
        if __debug__:
            def stub(
                *,
                access_control_allow_credentials: typing.Union[builtins.bool, cdktf.IResolvable],
                access_control_allow_headers: typing.Union[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders, typing.Dict[str, typing.Any]],
                access_control_allow_methods: typing.Union[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods, typing.Dict[str, typing.Any]],
                access_control_allow_origins: typing.Union[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins, typing.Dict[str, typing.Any]],
                origin_override: typing.Union[builtins.bool, cdktf.IResolvable],
                access_control_expose_headers: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders, typing.Dict[str, typing.Any]]] = None,
                access_control_max_age_sec: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument access_control_allow_credentials", value=access_control_allow_credentials, expected_type=type_hints["access_control_allow_credentials"])
            check_type(argname="argument access_control_allow_headers", value=access_control_allow_headers, expected_type=type_hints["access_control_allow_headers"])
            check_type(argname="argument access_control_allow_methods", value=access_control_allow_methods, expected_type=type_hints["access_control_allow_methods"])
            check_type(argname="argument access_control_allow_origins", value=access_control_allow_origins, expected_type=type_hints["access_control_allow_origins"])
            check_type(argname="argument origin_override", value=origin_override, expected_type=type_hints["origin_override"])
            check_type(argname="argument access_control_expose_headers", value=access_control_expose_headers, expected_type=type_hints["access_control_expose_headers"])
            check_type(argname="argument access_control_max_age_sec", value=access_control_max_age_sec, expected_type=type_hints["access_control_max_age_sec"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_control_allow_credentials": access_control_allow_credentials,
            "access_control_allow_headers": access_control_allow_headers,
            "access_control_allow_methods": access_control_allow_methods,
            "access_control_allow_origins": access_control_allow_origins,
            "origin_override": origin_override,
        }
        if access_control_expose_headers is not None:
            self._values["access_control_expose_headers"] = access_control_expose_headers
        if access_control_max_age_sec is not None:
            self._values["access_control_max_age_sec"] = access_control_max_age_sec

    @builtins.property
    def access_control_allow_credentials(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_credentials CloudfrontResponseHeadersPolicy#access_control_allow_credentials}.'''
        result = self._values.get("access_control_allow_credentials")
        assert result is not None, "Required property 'access_control_allow_credentials' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def access_control_allow_headers(
        self,
    ) -> "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders":
        '''access_control_allow_headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_headers CloudfrontResponseHeadersPolicy#access_control_allow_headers}
        '''
        result = self._values.get("access_control_allow_headers")
        assert result is not None, "Required property 'access_control_allow_headers' is missing"
        return typing.cast("CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders", result)

    @builtins.property
    def access_control_allow_methods(
        self,
    ) -> "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods":
        '''access_control_allow_methods block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_methods CloudfrontResponseHeadersPolicy#access_control_allow_methods}
        '''
        result = self._values.get("access_control_allow_methods")
        assert result is not None, "Required property 'access_control_allow_methods' is missing"
        return typing.cast("CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods", result)

    @builtins.property
    def access_control_allow_origins(
        self,
    ) -> "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins":
        '''access_control_allow_origins block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_allow_origins CloudfrontResponseHeadersPolicy#access_control_allow_origins}
        '''
        result = self._values.get("access_control_allow_origins")
        assert result is not None, "Required property 'access_control_allow_origins' is missing"
        return typing.cast("CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins", result)

    @builtins.property
    def origin_override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#origin_override CloudfrontResponseHeadersPolicy#origin_override}.'''
        result = self._values.get("origin_override")
        assert result is not None, "Required property 'origin_override' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def access_control_expose_headers(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders"]:
        '''access_control_expose_headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_expose_headers CloudfrontResponseHeadersPolicy#access_control_expose_headers}
        '''
        result = self._values.get("access_control_expose_headers")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders"], result)

    @builtins.property
    def access_control_max_age_sec(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_max_age_sec CloudfrontResponseHeadersPolicy#access_control_max_age_sec}.'''
        result = self._values.get("access_control_max_age_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicyCorsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.
        '''
        if __debug__:
            def stub(
                *,
                items: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[str, typing.Any] = {}
        if items is not None:
            self._values["items"] = items

    @builtins.property
    def items(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeadersOutputReference",
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

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "items"))

    @items.setter
    def items(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "items", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.
        '''
        if __debug__:
            def stub(
                *,
                items: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[str, typing.Any] = {}
        if items is not None:
            self._values["items"] = items

    @builtins.property
    def items(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethodsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethodsOutputReference",
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

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "items"))

    @items.setter
    def items(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "items", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.
        '''
        if __debug__:
            def stub(
                *,
                items: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[str, typing.Any] = {}
        if items is not None:
            self._values["items"] = items

    @builtins.property
    def items(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOriginsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOriginsOutputReference",
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

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "items"))

    @items.setter
    def items(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "items", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.
        '''
        if __debug__:
            def stub(
                *,
                items: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[str, typing.Any] = {}
        if items is not None:
            self._values["items"] = items

    @builtins.property
    def items(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeadersOutputReference",
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

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "items"))

    @items.setter
    def items(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "items", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontResponseHeadersPolicyCorsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCorsConfigOutputReference",
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

    @jsii.member(jsii_name="putAccessControlAllowHeaders")
    def put_access_control_allow_headers(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.
        '''
        value = CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putAccessControlAllowHeaders", [value]))

    @jsii.member(jsii_name="putAccessControlAllowMethods")
    def put_access_control_allow_methods(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.
        '''
        value = CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putAccessControlAllowMethods", [value]))

    @jsii.member(jsii_name="putAccessControlAllowOrigins")
    def put_access_control_allow_origins(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.
        '''
        value = CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putAccessControlAllowOrigins", [value]))

    @jsii.member(jsii_name="putAccessControlExposeHeaders")
    def put_access_control_expose_headers(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}.
        '''
        value = CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putAccessControlExposeHeaders", [value]))

    @jsii.member(jsii_name="resetAccessControlExposeHeaders")
    def reset_access_control_expose_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessControlExposeHeaders", []))

    @jsii.member(jsii_name="resetAccessControlMaxAgeSec")
    def reset_access_control_max_age_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessControlMaxAgeSec", []))

    @builtins.property
    @jsii.member(jsii_name="accessControlAllowHeaders")
    def access_control_allow_headers(
        self,
    ) -> CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeadersOutputReference:
        return typing.cast(CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeadersOutputReference, jsii.get(self, "accessControlAllowHeaders"))

    @builtins.property
    @jsii.member(jsii_name="accessControlAllowMethods")
    def access_control_allow_methods(
        self,
    ) -> CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethodsOutputReference:
        return typing.cast(CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethodsOutputReference, jsii.get(self, "accessControlAllowMethods"))

    @builtins.property
    @jsii.member(jsii_name="accessControlAllowOrigins")
    def access_control_allow_origins(
        self,
    ) -> CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOriginsOutputReference:
        return typing.cast(CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOriginsOutputReference, jsii.get(self, "accessControlAllowOrigins"))

    @builtins.property
    @jsii.member(jsii_name="accessControlExposeHeaders")
    def access_control_expose_headers(
        self,
    ) -> CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeadersOutputReference:
        return typing.cast(CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeadersOutputReference, jsii.get(self, "accessControlExposeHeaders"))

    @builtins.property
    @jsii.member(jsii_name="accessControlAllowCredentialsInput")
    def access_control_allow_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "accessControlAllowCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="accessControlAllowHeadersInput")
    def access_control_allow_headers_input(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders], jsii.get(self, "accessControlAllowHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="accessControlAllowMethodsInput")
    def access_control_allow_methods_input(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods], jsii.get(self, "accessControlAllowMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="accessControlAllowOriginsInput")
    def access_control_allow_origins_input(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins], jsii.get(self, "accessControlAllowOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="accessControlExposeHeadersInput")
    def access_control_expose_headers_input(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders], jsii.get(self, "accessControlExposeHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="accessControlMaxAgeSecInput")
    def access_control_max_age_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accessControlMaxAgeSecInput"))

    @builtins.property
    @jsii.member(jsii_name="originOverrideInput")
    def origin_override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "originOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="accessControlAllowCredentials")
    def access_control_allow_credentials(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "accessControlAllowCredentials"))

    @access_control_allow_credentials.setter
    def access_control_allow_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessControlAllowCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="accessControlMaxAgeSec")
    def access_control_max_age_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accessControlMaxAgeSec"))

    @access_control_max_age_sec.setter
    def access_control_max_age_sec(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessControlMaxAgeSec", value)

    @builtins.property
    @jsii.member(jsii_name="originOverride")
    def origin_override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "originOverride"))

    @origin_override.setter
    def origin_override(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originOverride", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCorsConfig]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCorsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicyCorsConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCustomHeadersConfig",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontResponseHeadersPolicyCustomHeadersConfig:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudfrontResponseHeadersPolicyCustomHeadersConfigItems", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}
        '''
        if __debug__:
            def stub(
                *,
                items: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[str, typing.Any] = {}
        if items is not None:
            self._values["items"] = items

    @builtins.property
    def items(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudfrontResponseHeadersPolicyCustomHeadersConfigItems"]]]:
        '''items block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#items CloudfrontResponseHeadersPolicy#items}
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudfrontResponseHeadersPolicyCustomHeadersConfigItems"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicyCustomHeadersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCustomHeadersConfigItems",
    jsii_struct_bases=[],
    name_mapping={"header": "header", "override": "override", "value": "value"},
)
class CloudfrontResponseHeadersPolicyCustomHeadersConfigItems:
    def __init__(
        self,
        *,
        header: builtins.str,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
        value: builtins.str,
    ) -> None:
        '''
        :param header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#header CloudfrontResponseHeadersPolicy#header}.
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#value CloudfrontResponseHeadersPolicy#value}.
        '''
        if __debug__:
            def stub(
                *,
                header: builtins.str,
                override: typing.Union[builtins.bool, cdktf.IResolvable],
                value: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "header": header,
            "override": override,
            "value": value,
        }

    @builtins.property
    def header(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#header CloudfrontResponseHeadersPolicy#header}.'''
        result = self._values.get("header")
        assert result is not None, "Required property 'header' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.'''
        result = self._values.get("override")
        assert result is not None, "Required property 'override' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#value CloudfrontResponseHeadersPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicyCustomHeadersConfigItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsList",
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
    ) -> "CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsOutputReference",
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
    @jsii.member(jsii_name="headerInput")
    def header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "header"))

    @header.setter
    def header(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "header", value)

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "override"))

    @override.setter
    def override(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "override", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontResponseHeadersPolicyCustomHeadersConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyCustomHeadersConfigOutputReference",
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

    @jsii.member(jsii_name="putItems")
    def put_items(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putItems", [value]))

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsList:
        return typing.cast(CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsList, jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontResponseHeadersPolicyCustomHeadersConfigItems]]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyCustomHeadersConfig]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyCustomHeadersConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicyCustomHeadersConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicyCustomHeadersConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfig",
    jsii_struct_bases=[],
    name_mapping={
        "content_security_policy": "contentSecurityPolicy",
        "content_type_options": "contentTypeOptions",
        "frame_options": "frameOptions",
        "referrer_policy": "referrerPolicy",
        "strict_transport_security": "strictTransportSecurity",
        "xss_protection": "xssProtection",
    },
)
class CloudfrontResponseHeadersPolicySecurityHeadersConfig:
    def __init__(
        self,
        *,
        content_security_policy: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy", typing.Dict[str, typing.Any]]] = None,
        content_type_options: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions", typing.Dict[str, typing.Any]]] = None,
        frame_options: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions", typing.Dict[str, typing.Any]]] = None,
        referrer_policy: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy", typing.Dict[str, typing.Any]]] = None,
        strict_transport_security: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity", typing.Dict[str, typing.Any]]] = None,
        xss_protection: typing.Optional[typing.Union["CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param content_security_policy: content_security_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#content_security_policy CloudfrontResponseHeadersPolicy#content_security_policy}
        :param content_type_options: content_type_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#content_type_options CloudfrontResponseHeadersPolicy#content_type_options}
        :param frame_options: frame_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#frame_options CloudfrontResponseHeadersPolicy#frame_options}
        :param referrer_policy: referrer_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#referrer_policy CloudfrontResponseHeadersPolicy#referrer_policy}
        :param strict_transport_security: strict_transport_security block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#strict_transport_security CloudfrontResponseHeadersPolicy#strict_transport_security}
        :param xss_protection: xss_protection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#xss_protection CloudfrontResponseHeadersPolicy#xss_protection}
        '''
        if isinstance(content_security_policy, dict):
            content_security_policy = CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy(**content_security_policy)
        if isinstance(content_type_options, dict):
            content_type_options = CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions(**content_type_options)
        if isinstance(frame_options, dict):
            frame_options = CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions(**frame_options)
        if isinstance(referrer_policy, dict):
            referrer_policy = CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy(**referrer_policy)
        if isinstance(strict_transport_security, dict):
            strict_transport_security = CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity(**strict_transport_security)
        if isinstance(xss_protection, dict):
            xss_protection = CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection(**xss_protection)
        if __debug__:
            def stub(
                *,
                content_security_policy: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy, typing.Dict[str, typing.Any]]] = None,
                content_type_options: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions, typing.Dict[str, typing.Any]]] = None,
                frame_options: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions, typing.Dict[str, typing.Any]]] = None,
                referrer_policy: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy, typing.Dict[str, typing.Any]]] = None,
                strict_transport_security: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity, typing.Dict[str, typing.Any]]] = None,
                xss_protection: typing.Optional[typing.Union[CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content_security_policy", value=content_security_policy, expected_type=type_hints["content_security_policy"])
            check_type(argname="argument content_type_options", value=content_type_options, expected_type=type_hints["content_type_options"])
            check_type(argname="argument frame_options", value=frame_options, expected_type=type_hints["frame_options"])
            check_type(argname="argument referrer_policy", value=referrer_policy, expected_type=type_hints["referrer_policy"])
            check_type(argname="argument strict_transport_security", value=strict_transport_security, expected_type=type_hints["strict_transport_security"])
            check_type(argname="argument xss_protection", value=xss_protection, expected_type=type_hints["xss_protection"])
        self._values: typing.Dict[str, typing.Any] = {}
        if content_security_policy is not None:
            self._values["content_security_policy"] = content_security_policy
        if content_type_options is not None:
            self._values["content_type_options"] = content_type_options
        if frame_options is not None:
            self._values["frame_options"] = frame_options
        if referrer_policy is not None:
            self._values["referrer_policy"] = referrer_policy
        if strict_transport_security is not None:
            self._values["strict_transport_security"] = strict_transport_security
        if xss_protection is not None:
            self._values["xss_protection"] = xss_protection

    @builtins.property
    def content_security_policy(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy"]:
        '''content_security_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#content_security_policy CloudfrontResponseHeadersPolicy#content_security_policy}
        '''
        result = self._values.get("content_security_policy")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy"], result)

    @builtins.property
    def content_type_options(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions"]:
        '''content_type_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#content_type_options CloudfrontResponseHeadersPolicy#content_type_options}
        '''
        result = self._values.get("content_type_options")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions"], result)

    @builtins.property
    def frame_options(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions"]:
        '''frame_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#frame_options CloudfrontResponseHeadersPolicy#frame_options}
        '''
        result = self._values.get("frame_options")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions"], result)

    @builtins.property
    def referrer_policy(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy"]:
        '''referrer_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#referrer_policy CloudfrontResponseHeadersPolicy#referrer_policy}
        '''
        result = self._values.get("referrer_policy")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy"], result)

    @builtins.property
    def strict_transport_security(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity"]:
        '''strict_transport_security block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#strict_transport_security CloudfrontResponseHeadersPolicy#strict_transport_security}
        '''
        result = self._values.get("strict_transport_security")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity"], result)

    @builtins.property
    def xss_protection(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection"]:
        '''xss_protection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#xss_protection CloudfrontResponseHeadersPolicy#xss_protection}
        '''
        result = self._values.get("xss_protection")
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicySecurityHeadersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "content_security_policy": "contentSecurityPolicy",
        "override": "override",
    },
)
class CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy:
    def __init__(
        self,
        *,
        content_security_policy: builtins.str,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param content_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#content_security_policy CloudfrontResponseHeadersPolicy#content_security_policy}.
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        '''
        if __debug__:
            def stub(
                *,
                content_security_policy: builtins.str,
                override: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content_security_policy", value=content_security_policy, expected_type=type_hints["content_security_policy"])
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_security_policy": content_security_policy,
            "override": override,
        }

    @builtins.property
    def content_security_policy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#content_security_policy CloudfrontResponseHeadersPolicy#content_security_policy}.'''
        result = self._values.get("content_security_policy")
        assert result is not None, "Required property 'content_security_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.'''
        result = self._values.get("override")
        assert result is not None, "Required property 'override' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyOutputReference",
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
    @jsii.member(jsii_name="contentSecurityPolicyInput")
    def content_security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentSecurityPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="contentSecurityPolicy")
    def content_security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentSecurityPolicy"))

    @content_security_policy.setter
    def content_security_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentSecurityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "override"))

    @override.setter
    def override(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "override", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions",
    jsii_struct_bases=[],
    name_mapping={"override": "override"},
)
class CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions:
    def __init__(
        self,
        *,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        '''
        if __debug__:
            def stub(
                *,
                override: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
        self._values: typing.Dict[str, typing.Any] = {
            "override": override,
        }

    @builtins.property
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.'''
        result = self._values.get("override")
        assert result is not None, "Required property 'override' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsOutputReference",
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
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "override"))

    @override.setter
    def override(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "override", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions",
    jsii_struct_bases=[],
    name_mapping={"frame_option": "frameOption", "override": "override"},
)
class CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions:
    def __init__(
        self,
        *,
        frame_option: builtins.str,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param frame_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#frame_option CloudfrontResponseHeadersPolicy#frame_option}.
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        '''
        if __debug__:
            def stub(
                *,
                frame_option: builtins.str,
                override: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument frame_option", value=frame_option, expected_type=type_hints["frame_option"])
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
        self._values: typing.Dict[str, typing.Any] = {
            "frame_option": frame_option,
            "override": override,
        }

    @builtins.property
    def frame_option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#frame_option CloudfrontResponseHeadersPolicy#frame_option}.'''
        result = self._values.get("frame_option")
        assert result is not None, "Required property 'frame_option' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.'''
        result = self._values.get("override")
        assert result is not None, "Required property 'override' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptionsOutputReference",
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
    @jsii.member(jsii_name="frameOptionInput")
    def frame_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="frameOption")
    def frame_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frameOption"))

    @frame_option.setter
    def frame_option(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameOption", value)

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "override"))

    @override.setter
    def override(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "override", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontResponseHeadersPolicySecurityHeadersConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigOutputReference",
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

    @jsii.member(jsii_name="putContentSecurityPolicy")
    def put_content_security_policy(
        self,
        *,
        content_security_policy: builtins.str,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param content_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#content_security_policy CloudfrontResponseHeadersPolicy#content_security_policy}.
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        '''
        value = CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy(
            content_security_policy=content_security_policy, override=override
        )

        return typing.cast(None, jsii.invoke(self, "putContentSecurityPolicy", [value]))

    @jsii.member(jsii_name="putContentTypeOptions")
    def put_content_type_options(
        self,
        *,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        '''
        value = CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions(
            override=override
        )

        return typing.cast(None, jsii.invoke(self, "putContentTypeOptions", [value]))

    @jsii.member(jsii_name="putFrameOptions")
    def put_frame_options(
        self,
        *,
        frame_option: builtins.str,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param frame_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#frame_option CloudfrontResponseHeadersPolicy#frame_option}.
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        '''
        value = CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions(
            frame_option=frame_option, override=override
        )

        return typing.cast(None, jsii.invoke(self, "putFrameOptions", [value]))

    @jsii.member(jsii_name="putReferrerPolicy")
    def put_referrer_policy(
        self,
        *,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
        referrer_policy: builtins.str,
    ) -> None:
        '''
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        :param referrer_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#referrer_policy CloudfrontResponseHeadersPolicy#referrer_policy}.
        '''
        value = CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy(
            override=override, referrer_policy=referrer_policy
        )

        return typing.cast(None, jsii.invoke(self, "putReferrerPolicy", [value]))

    @jsii.member(jsii_name="putStrictTransportSecurity")
    def put_strict_transport_security(
        self,
        *,
        access_control_max_age_sec: jsii.Number,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
        include_subdomains: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preload: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param access_control_max_age_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_max_age_sec CloudfrontResponseHeadersPolicy#access_control_max_age_sec}.
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        :param include_subdomains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#include_subdomains CloudfrontResponseHeadersPolicy#include_subdomains}.
        :param preload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#preload CloudfrontResponseHeadersPolicy#preload}.
        '''
        value = CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity(
            access_control_max_age_sec=access_control_max_age_sec,
            override=override,
            include_subdomains=include_subdomains,
            preload=preload,
        )

        return typing.cast(None, jsii.invoke(self, "putStrictTransportSecurity", [value]))

    @jsii.member(jsii_name="putXssProtection")
    def put_xss_protection(
        self,
        *,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
        protection: typing.Union[builtins.bool, cdktf.IResolvable],
        mode_block: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        report_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        :param protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#protection CloudfrontResponseHeadersPolicy#protection}.
        :param mode_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#mode_block CloudfrontResponseHeadersPolicy#mode_block}.
        :param report_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#report_uri CloudfrontResponseHeadersPolicy#report_uri}.
        '''
        value = CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection(
            override=override,
            protection=protection,
            mode_block=mode_block,
            report_uri=report_uri,
        )

        return typing.cast(None, jsii.invoke(self, "putXssProtection", [value]))

    @jsii.member(jsii_name="resetContentSecurityPolicy")
    def reset_content_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentSecurityPolicy", []))

    @jsii.member(jsii_name="resetContentTypeOptions")
    def reset_content_type_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentTypeOptions", []))

    @jsii.member(jsii_name="resetFrameOptions")
    def reset_frame_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrameOptions", []))

    @jsii.member(jsii_name="resetReferrerPolicy")
    def reset_referrer_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReferrerPolicy", []))

    @jsii.member(jsii_name="resetStrictTransportSecurity")
    def reset_strict_transport_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStrictTransportSecurity", []))

    @jsii.member(jsii_name="resetXssProtection")
    def reset_xss_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXssProtection", []))

    @builtins.property
    @jsii.member(jsii_name="contentSecurityPolicy")
    def content_security_policy(
        self,
    ) -> CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyOutputReference:
        return typing.cast(CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyOutputReference, jsii.get(self, "contentSecurityPolicy"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeOptions")
    def content_type_options(
        self,
    ) -> CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsOutputReference:
        return typing.cast(CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsOutputReference, jsii.get(self, "contentTypeOptions"))

    @builtins.property
    @jsii.member(jsii_name="frameOptions")
    def frame_options(
        self,
    ) -> CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptionsOutputReference:
        return typing.cast(CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptionsOutputReference, jsii.get(self, "frameOptions"))

    @builtins.property
    @jsii.member(jsii_name="referrerPolicy")
    def referrer_policy(
        self,
    ) -> "CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicyOutputReference":
        return typing.cast("CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicyOutputReference", jsii.get(self, "referrerPolicy"))

    @builtins.property
    @jsii.member(jsii_name="strictTransportSecurity")
    def strict_transport_security(
        self,
    ) -> "CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityOutputReference":
        return typing.cast("CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityOutputReference", jsii.get(self, "strictTransportSecurity"))

    @builtins.property
    @jsii.member(jsii_name="xssProtection")
    def xss_protection(
        self,
    ) -> "CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtectionOutputReference":
        return typing.cast("CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtectionOutputReference", jsii.get(self, "xssProtection"))

    @builtins.property
    @jsii.member(jsii_name="contentSecurityPolicyInput")
    def content_security_policy_input(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy], jsii.get(self, "contentSecurityPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeOptionsInput")
    def content_type_options_input(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions], jsii.get(self, "contentTypeOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="frameOptionsInput")
    def frame_options_input(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions], jsii.get(self, "frameOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="referrerPolicyInput")
    def referrer_policy_input(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy"]:
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy"], jsii.get(self, "referrerPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="strictTransportSecurityInput")
    def strict_transport_security_input(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity"]:
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity"], jsii.get(self, "strictTransportSecurityInput"))

    @builtins.property
    @jsii.member(jsii_name="xssProtectionInput")
    def xss_protection_input(
        self,
    ) -> typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection"]:
        return typing.cast(typing.Optional["CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection"], jsii.get(self, "xssProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfig]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy",
    jsii_struct_bases=[],
    name_mapping={"override": "override", "referrer_policy": "referrerPolicy"},
)
class CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy:
    def __init__(
        self,
        *,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
        referrer_policy: builtins.str,
    ) -> None:
        '''
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        :param referrer_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#referrer_policy CloudfrontResponseHeadersPolicy#referrer_policy}.
        '''
        if __debug__:
            def stub(
                *,
                override: typing.Union[builtins.bool, cdktf.IResolvable],
                referrer_policy: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
            check_type(argname="argument referrer_policy", value=referrer_policy, expected_type=type_hints["referrer_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "override": override,
            "referrer_policy": referrer_policy,
        }

    @builtins.property
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.'''
        result = self._values.get("override")
        assert result is not None, "Required property 'override' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def referrer_policy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#referrer_policy CloudfrontResponseHeadersPolicy#referrer_policy}.'''
        result = self._values.get("referrer_policy")
        assert result is not None, "Required property 'referrer_policy' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicyOutputReference",
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
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="referrerPolicyInput")
    def referrer_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "referrerPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "override"))

    @override.setter
    def override(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "override", value)

    @builtins.property
    @jsii.member(jsii_name="referrerPolicy")
    def referrer_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "referrerPolicy"))

    @referrer_policy.setter
    def referrer_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "referrerPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity",
    jsii_struct_bases=[],
    name_mapping={
        "access_control_max_age_sec": "accessControlMaxAgeSec",
        "override": "override",
        "include_subdomains": "includeSubdomains",
        "preload": "preload",
    },
)
class CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity:
    def __init__(
        self,
        *,
        access_control_max_age_sec: jsii.Number,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
        include_subdomains: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        preload: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param access_control_max_age_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_max_age_sec CloudfrontResponseHeadersPolicy#access_control_max_age_sec}.
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        :param include_subdomains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#include_subdomains CloudfrontResponseHeadersPolicy#include_subdomains}.
        :param preload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#preload CloudfrontResponseHeadersPolicy#preload}.
        '''
        if __debug__:
            def stub(
                *,
                access_control_max_age_sec: jsii.Number,
                override: typing.Union[builtins.bool, cdktf.IResolvable],
                include_subdomains: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                preload: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument access_control_max_age_sec", value=access_control_max_age_sec, expected_type=type_hints["access_control_max_age_sec"])
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
            check_type(argname="argument include_subdomains", value=include_subdomains, expected_type=type_hints["include_subdomains"])
            check_type(argname="argument preload", value=preload, expected_type=type_hints["preload"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_control_max_age_sec": access_control_max_age_sec,
            "override": override,
        }
        if include_subdomains is not None:
            self._values["include_subdomains"] = include_subdomains
        if preload is not None:
            self._values["preload"] = preload

    @builtins.property
    def access_control_max_age_sec(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#access_control_max_age_sec CloudfrontResponseHeadersPolicy#access_control_max_age_sec}.'''
        result = self._values.get("access_control_max_age_sec")
        assert result is not None, "Required property 'access_control_max_age_sec' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.'''
        result = self._values.get("override")
        assert result is not None, "Required property 'override' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def include_subdomains(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#include_subdomains CloudfrontResponseHeadersPolicy#include_subdomains}.'''
        result = self._values.get("include_subdomains")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def preload(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#preload CloudfrontResponseHeadersPolicy#preload}.'''
        result = self._values.get("preload")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityOutputReference",
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

    @jsii.member(jsii_name="resetIncludeSubdomains")
    def reset_include_subdomains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeSubdomains", []))

    @jsii.member(jsii_name="resetPreload")
    def reset_preload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreload", []))

    @builtins.property
    @jsii.member(jsii_name="accessControlMaxAgeSecInput")
    def access_control_max_age_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accessControlMaxAgeSecInput"))

    @builtins.property
    @jsii.member(jsii_name="includeSubdomainsInput")
    def include_subdomains_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeSubdomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="preloadInput")
    def preload_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preloadInput"))

    @builtins.property
    @jsii.member(jsii_name="accessControlMaxAgeSec")
    def access_control_max_age_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accessControlMaxAgeSec"))

    @access_control_max_age_sec.setter
    def access_control_max_age_sec(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessControlMaxAgeSec", value)

    @builtins.property
    @jsii.member(jsii_name="includeSubdomains")
    def include_subdomains(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeSubdomains"))

    @include_subdomains.setter
    def include_subdomains(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeSubdomains", value)

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "override"))

    @override.setter
    def override(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "override", value)

    @builtins.property
    @jsii.member(jsii_name="preload")
    def preload(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preload"))

    @preload.setter
    def preload(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection",
    jsii_struct_bases=[],
    name_mapping={
        "override": "override",
        "protection": "protection",
        "mode_block": "modeBlock",
        "report_uri": "reportUri",
    },
)
class CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection:
    def __init__(
        self,
        *,
        override: typing.Union[builtins.bool, cdktf.IResolvable],
        protection: typing.Union[builtins.bool, cdktf.IResolvable],
        mode_block: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        report_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.
        :param protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#protection CloudfrontResponseHeadersPolicy#protection}.
        :param mode_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#mode_block CloudfrontResponseHeadersPolicy#mode_block}.
        :param report_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#report_uri CloudfrontResponseHeadersPolicy#report_uri}.
        '''
        if __debug__:
            def stub(
                *,
                override: typing.Union[builtins.bool, cdktf.IResolvable],
                protection: typing.Union[builtins.bool, cdktf.IResolvable],
                mode_block: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                report_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
            check_type(argname="argument protection", value=protection, expected_type=type_hints["protection"])
            check_type(argname="argument mode_block", value=mode_block, expected_type=type_hints["mode_block"])
            check_type(argname="argument report_uri", value=report_uri, expected_type=type_hints["report_uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "override": override,
            "protection": protection,
        }
        if mode_block is not None:
            self._values["mode_block"] = mode_block
        if report_uri is not None:
            self._values["report_uri"] = report_uri

    @builtins.property
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#override CloudfrontResponseHeadersPolicy#override}.'''
        result = self._values.get("override")
        assert result is not None, "Required property 'override' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#protection CloudfrontResponseHeadersPolicy#protection}.'''
        result = self._values.get("protection")
        assert result is not None, "Required property 'protection' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def mode_block(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#mode_block CloudfrontResponseHeadersPolicy#mode_block}.'''
        result = self._values.get("mode_block")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def report_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#report_uri CloudfrontResponseHeadersPolicy#report_uri}.'''
        result = self._values.get("report_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtectionOutputReference",
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

    @jsii.member(jsii_name="resetModeBlock")
    def reset_mode_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModeBlock", []))

    @jsii.member(jsii_name="resetReportUri")
    def reset_report_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReportUri", []))

    @builtins.property
    @jsii.member(jsii_name="modeBlockInput")
    def mode_block_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "modeBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="protectionInput")
    def protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "protectionInput"))

    @builtins.property
    @jsii.member(jsii_name="reportUriInput")
    def report_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reportUriInput"))

    @builtins.property
    @jsii.member(jsii_name="modeBlock")
    def mode_block(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "modeBlock"))

    @mode_block.setter
    def mode_block(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modeBlock", value)

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "override"))

    @override.setter
    def override(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "override", value)

    @builtins.property
    @jsii.member(jsii_name="protection")
    def protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "protection"))

    @protection.setter
    def protection(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protection", value)

    @builtins.property
    @jsii.member(jsii_name="reportUri")
    def report_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reportUri"))

    @report_uri.setter
    def report_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyServerTimingHeadersConfig",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "sampling_rate": "samplingRate"},
)
class CloudfrontResponseHeadersPolicyServerTimingHeadersConfig:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        sampling_rate: jsii.Number,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#enabled CloudfrontResponseHeadersPolicy#enabled}.
        :param sampling_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#sampling_rate CloudfrontResponseHeadersPolicy#sampling_rate}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Union[builtins.bool, cdktf.IResolvable],
                sampling_rate: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument sampling_rate", value=sampling_rate, expected_type=type_hints["sampling_rate"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
            "sampling_rate": sampling_rate,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#enabled CloudfrontResponseHeadersPolicy#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def sampling_rate(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_response_headers_policy#sampling_rate CloudfrontResponseHeadersPolicy#sampling_rate}.'''
        result = self._values.get("sampling_rate")
        assert result is not None, "Required property 'sampling_rate' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontResponseHeadersPolicyServerTimingHeadersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontResponseHeadersPolicyServerTimingHeadersConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontResponseHeadersPolicy.CloudfrontResponseHeadersPolicyServerTimingHeadersConfigOutputReference",
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
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="samplingRateInput")
    def sampling_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingRateInput"))

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
    @jsii.member(jsii_name="samplingRate")
    def sampling_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingRate"))

    @sampling_rate.setter
    def sampling_rate(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingRate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontResponseHeadersPolicyServerTimingHeadersConfig]:
        return typing.cast(typing.Optional[CloudfrontResponseHeadersPolicyServerTimingHeadersConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontResponseHeadersPolicyServerTimingHeadersConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontResponseHeadersPolicyServerTimingHeadersConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudfrontResponseHeadersPolicy",
    "CloudfrontResponseHeadersPolicyConfig",
    "CloudfrontResponseHeadersPolicyCorsConfig",
    "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeaders",
    "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowHeadersOutputReference",
    "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethods",
    "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowMethodsOutputReference",
    "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOrigins",
    "CloudfrontResponseHeadersPolicyCorsConfigAccessControlAllowOriginsOutputReference",
    "CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeaders",
    "CloudfrontResponseHeadersPolicyCorsConfigAccessControlExposeHeadersOutputReference",
    "CloudfrontResponseHeadersPolicyCorsConfigOutputReference",
    "CloudfrontResponseHeadersPolicyCustomHeadersConfig",
    "CloudfrontResponseHeadersPolicyCustomHeadersConfigItems",
    "CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsList",
    "CloudfrontResponseHeadersPolicyCustomHeadersConfigItemsOutputReference",
    "CloudfrontResponseHeadersPolicyCustomHeadersConfigOutputReference",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfig",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyOutputReference",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptions",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsOutputReference",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptions",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigFrameOptionsOutputReference",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigOutputReference",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicy",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigReferrerPolicyOutputReference",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityOutputReference",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtection",
    "CloudfrontResponseHeadersPolicySecurityHeadersConfigXssProtectionOutputReference",
    "CloudfrontResponseHeadersPolicyServerTimingHeadersConfig",
    "CloudfrontResponseHeadersPolicyServerTimingHeadersConfigOutputReference",
]

publication.publish()
