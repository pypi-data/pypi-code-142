'''
# `aws_cloudfront_cache_policy`

Refer to the Terraform Registory for docs: [`aws_cloudfront_cache_policy`](https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy).
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


class CloudfrontCachePolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy aws_cloudfront_cache_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        parameters_in_cache_key_and_forwarded_to_origin: typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin", typing.Dict[str, typing.Any]],
        comment: typing.Optional[builtins.str] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        min_ttl: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy aws_cloudfront_cache_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#name CloudfrontCachePolicy#name}.
        :param parameters_in_cache_key_and_forwarded_to_origin: parameters_in_cache_key_and_forwarded_to_origin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#parameters_in_cache_key_and_forwarded_to_origin CloudfrontCachePolicy#parameters_in_cache_key_and_forwarded_to_origin}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#comment CloudfrontCachePolicy#comment}.
        :param default_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#default_ttl CloudfrontCachePolicy#default_ttl}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#id CloudfrontCachePolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#max_ttl CloudfrontCachePolicy#max_ttl}.
        :param min_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#min_ttl CloudfrontCachePolicy#min_ttl}.
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
                parameters_in_cache_key_and_forwarded_to_origin: typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin, typing.Dict[str, typing.Any]],
                comment: typing.Optional[builtins.str] = None,
                default_ttl: typing.Optional[jsii.Number] = None,
                id: typing.Optional[builtins.str] = None,
                max_ttl: typing.Optional[jsii.Number] = None,
                min_ttl: typing.Optional[jsii.Number] = None,
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
        config = CloudfrontCachePolicyConfig(
            name=name,
            parameters_in_cache_key_and_forwarded_to_origin=parameters_in_cache_key_and_forwarded_to_origin,
            comment=comment,
            default_ttl=default_ttl,
            id=id,
            max_ttl=max_ttl,
            min_ttl=min_ttl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putParametersInCacheKeyAndForwardedToOrigin")
    def put_parameters_in_cache_key_and_forwarded_to_origin(
        self,
        *,
        cookies_config: typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig", typing.Dict[str, typing.Any]],
        headers_config: typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig", typing.Dict[str, typing.Any]],
        query_strings_config: typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig", typing.Dict[str, typing.Any]],
        enable_accept_encoding_brotli: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_accept_encoding_gzip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cookies_config: cookies_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#cookies_config CloudfrontCachePolicy#cookies_config}
        :param headers_config: headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#headers_config CloudfrontCachePolicy#headers_config}
        :param query_strings_config: query_strings_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#query_strings_config CloudfrontCachePolicy#query_strings_config}
        :param enable_accept_encoding_brotli: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#enable_accept_encoding_brotli CloudfrontCachePolicy#enable_accept_encoding_brotli}.
        :param enable_accept_encoding_gzip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#enable_accept_encoding_gzip CloudfrontCachePolicy#enable_accept_encoding_gzip}.
        '''
        value = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin(
            cookies_config=cookies_config,
            headers_config=headers_config,
            query_strings_config=query_strings_config,
            enable_accept_encoding_brotli=enable_accept_encoding_brotli,
            enable_accept_encoding_gzip=enable_accept_encoding_gzip,
        )

        return typing.cast(None, jsii.invoke(self, "putParametersInCacheKeyAndForwardedToOrigin", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDefaultTtl")
    def reset_default_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTtl", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxTtl")
    def reset_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTtl", []))

    @jsii.member(jsii_name="resetMinTtl")
    def reset_min_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTtl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="parametersInCacheKeyAndForwardedToOrigin")
    def parameters_in_cache_key_and_forwarded_to_origin(
        self,
    ) -> "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginOutputReference":
        return typing.cast("CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginOutputReference", jsii.get(self, "parametersInCacheKeyAndForwardedToOrigin"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTtlInput")
    def default_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTtlInput")
    def max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="minTtlInput")
    def min_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInCacheKeyAndForwardedToOriginInput")
    def parameters_in_cache_key_and_forwarded_to_origin_input(
        self,
    ) -> typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin"]:
        return typing.cast(typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin"], jsii.get(self, "parametersInCacheKeyAndForwardedToOriginInput"))

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
    @jsii.member(jsii_name="defaultTtl")
    def default_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTtl"))

    @default_ttl.setter
    def default_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTtl", value)

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
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @max_ttl.setter
    def max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="minTtl")
    def min_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minTtl"))

    @min_ttl.setter
    def min_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTtl", value)

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
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyConfig",
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
        "parameters_in_cache_key_and_forwarded_to_origin": "parametersInCacheKeyAndForwardedToOrigin",
        "comment": "comment",
        "default_ttl": "defaultTtl",
        "id": "id",
        "max_ttl": "maxTtl",
        "min_ttl": "minTtl",
    },
)
class CloudfrontCachePolicyConfig(cdktf.TerraformMetaArguments):
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
        parameters_in_cache_key_and_forwarded_to_origin: typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin", typing.Dict[str, typing.Any]],
        comment: typing.Optional[builtins.str] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        min_ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#name CloudfrontCachePolicy#name}.
        :param parameters_in_cache_key_and_forwarded_to_origin: parameters_in_cache_key_and_forwarded_to_origin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#parameters_in_cache_key_and_forwarded_to_origin CloudfrontCachePolicy#parameters_in_cache_key_and_forwarded_to_origin}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#comment CloudfrontCachePolicy#comment}.
        :param default_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#default_ttl CloudfrontCachePolicy#default_ttl}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#id CloudfrontCachePolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#max_ttl CloudfrontCachePolicy#max_ttl}.
        :param min_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#min_ttl CloudfrontCachePolicy#min_ttl}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(parameters_in_cache_key_and_forwarded_to_origin, dict):
            parameters_in_cache_key_and_forwarded_to_origin = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin(**parameters_in_cache_key_and_forwarded_to_origin)
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
                parameters_in_cache_key_and_forwarded_to_origin: typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin, typing.Dict[str, typing.Any]],
                comment: typing.Optional[builtins.str] = None,
                default_ttl: typing.Optional[jsii.Number] = None,
                id: typing.Optional[builtins.str] = None,
                max_ttl: typing.Optional[jsii.Number] = None,
                min_ttl: typing.Optional[jsii.Number] = None,
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
            check_type(argname="argument parameters_in_cache_key_and_forwarded_to_origin", value=parameters_in_cache_key_and_forwarded_to_origin, expected_type=type_hints["parameters_in_cache_key_and_forwarded_to_origin"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default_ttl", value=default_ttl, expected_type=type_hints["default_ttl"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_ttl", value=max_ttl, expected_type=type_hints["max_ttl"])
            check_type(argname="argument min_ttl", value=min_ttl, expected_type=type_hints["min_ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "parameters_in_cache_key_and_forwarded_to_origin": parameters_in_cache_key_and_forwarded_to_origin,
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
        if default_ttl is not None:
            self._values["default_ttl"] = default_ttl
        if id is not None:
            self._values["id"] = id
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if min_ttl is not None:
            self._values["min_ttl"] = min_ttl

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#name CloudfrontCachePolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters_in_cache_key_and_forwarded_to_origin(
        self,
    ) -> "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin":
        '''parameters_in_cache_key_and_forwarded_to_origin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#parameters_in_cache_key_and_forwarded_to_origin CloudfrontCachePolicy#parameters_in_cache_key_and_forwarded_to_origin}
        '''
        result = self._values.get("parameters_in_cache_key_and_forwarded_to_origin")
        assert result is not None, "Required property 'parameters_in_cache_key_and_forwarded_to_origin' is missing"
        return typing.cast("CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin", result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#comment CloudfrontCachePolicy#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#default_ttl CloudfrontCachePolicy#default_ttl}.'''
        result = self._values.get("default_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#id CloudfrontCachePolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#max_ttl CloudfrontCachePolicy#max_ttl}.'''
        result = self._values.get("max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#min_ttl CloudfrontCachePolicy#min_ttl}.'''
        result = self._values.get("min_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontCachePolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin",
    jsii_struct_bases=[],
    name_mapping={
        "cookies_config": "cookiesConfig",
        "headers_config": "headersConfig",
        "query_strings_config": "queryStringsConfig",
        "enable_accept_encoding_brotli": "enableAcceptEncodingBrotli",
        "enable_accept_encoding_gzip": "enableAcceptEncodingGzip",
    },
)
class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin:
    def __init__(
        self,
        *,
        cookies_config: typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig", typing.Dict[str, typing.Any]],
        headers_config: typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig", typing.Dict[str, typing.Any]],
        query_strings_config: typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig", typing.Dict[str, typing.Any]],
        enable_accept_encoding_brotli: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_accept_encoding_gzip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cookies_config: cookies_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#cookies_config CloudfrontCachePolicy#cookies_config}
        :param headers_config: headers_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#headers_config CloudfrontCachePolicy#headers_config}
        :param query_strings_config: query_strings_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#query_strings_config CloudfrontCachePolicy#query_strings_config}
        :param enable_accept_encoding_brotli: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#enable_accept_encoding_brotli CloudfrontCachePolicy#enable_accept_encoding_brotli}.
        :param enable_accept_encoding_gzip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#enable_accept_encoding_gzip CloudfrontCachePolicy#enable_accept_encoding_gzip}.
        '''
        if isinstance(cookies_config, dict):
            cookies_config = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig(**cookies_config)
        if isinstance(headers_config, dict):
            headers_config = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig(**headers_config)
        if isinstance(query_strings_config, dict):
            query_strings_config = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig(**query_strings_config)
        if __debug__:
            def stub(
                *,
                cookies_config: typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig, typing.Dict[str, typing.Any]],
                headers_config: typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig, typing.Dict[str, typing.Any]],
                query_strings_config: typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig, typing.Dict[str, typing.Any]],
                enable_accept_encoding_brotli: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enable_accept_encoding_gzip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cookies_config", value=cookies_config, expected_type=type_hints["cookies_config"])
            check_type(argname="argument headers_config", value=headers_config, expected_type=type_hints["headers_config"])
            check_type(argname="argument query_strings_config", value=query_strings_config, expected_type=type_hints["query_strings_config"])
            check_type(argname="argument enable_accept_encoding_brotli", value=enable_accept_encoding_brotli, expected_type=type_hints["enable_accept_encoding_brotli"])
            check_type(argname="argument enable_accept_encoding_gzip", value=enable_accept_encoding_gzip, expected_type=type_hints["enable_accept_encoding_gzip"])
        self._values: typing.Dict[str, typing.Any] = {
            "cookies_config": cookies_config,
            "headers_config": headers_config,
            "query_strings_config": query_strings_config,
        }
        if enable_accept_encoding_brotli is not None:
            self._values["enable_accept_encoding_brotli"] = enable_accept_encoding_brotli
        if enable_accept_encoding_gzip is not None:
            self._values["enable_accept_encoding_gzip"] = enable_accept_encoding_gzip

    @builtins.property
    def cookies_config(
        self,
    ) -> "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig":
        '''cookies_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#cookies_config CloudfrontCachePolicy#cookies_config}
        '''
        result = self._values.get("cookies_config")
        assert result is not None, "Required property 'cookies_config' is missing"
        return typing.cast("CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig", result)

    @builtins.property
    def headers_config(
        self,
    ) -> "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig":
        '''headers_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#headers_config CloudfrontCachePolicy#headers_config}
        '''
        result = self._values.get("headers_config")
        assert result is not None, "Required property 'headers_config' is missing"
        return typing.cast("CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig", result)

    @builtins.property
    def query_strings_config(
        self,
    ) -> "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig":
        '''query_strings_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#query_strings_config CloudfrontCachePolicy#query_strings_config}
        '''
        result = self._values.get("query_strings_config")
        assert result is not None, "Required property 'query_strings_config' is missing"
        return typing.cast("CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig", result)

    @builtins.property
    def enable_accept_encoding_brotli(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#enable_accept_encoding_brotli CloudfrontCachePolicy#enable_accept_encoding_brotli}.'''
        result = self._values.get("enable_accept_encoding_brotli")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_accept_encoding_gzip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#enable_accept_encoding_gzip CloudfrontCachePolicy#enable_accept_encoding_gzip}.'''
        result = self._values.get("enable_accept_encoding_gzip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig",
    jsii_struct_bases=[],
    name_mapping={"cookie_behavior": "cookieBehavior", "cookies": "cookies"},
)
class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig:
    def __init__(
        self,
        *,
        cookie_behavior: builtins.str,
        cookies: typing.Optional[typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cookie_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#cookie_behavior CloudfrontCachePolicy#cookie_behavior}.
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#cookies CloudfrontCachePolicy#cookies}
        '''
        if isinstance(cookies, dict):
            cookies = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies(**cookies)
        if __debug__:
            def stub(
                *,
                cookie_behavior: builtins.str,
                cookies: typing.Optional[typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cookie_behavior", value=cookie_behavior, expected_type=type_hints["cookie_behavior"])
            check_type(argname="argument cookies", value=cookies, expected_type=type_hints["cookies"])
        self._values: typing.Dict[str, typing.Any] = {
            "cookie_behavior": cookie_behavior,
        }
        if cookies is not None:
            self._values["cookies"] = cookies

    @builtins.property
    def cookie_behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#cookie_behavior CloudfrontCachePolicy#cookie_behavior}.'''
        result = self._values.get("cookie_behavior")
        assert result is not None, "Required property 'cookie_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cookies(
        self,
    ) -> typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies"]:
        '''cookies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#cookies CloudfrontCachePolicy#cookies}
        '''
        result = self._values.get("cookies")
        return typing.cast(typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#items CloudfrontCachePolicy#items}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#items CloudfrontCachePolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesOutputReference",
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
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigOutputReference",
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

    @jsii.member(jsii_name="putCookies")
    def put_cookies(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#items CloudfrontCachePolicy#items}.
        '''
        value = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putCookies", [value]))

    @jsii.member(jsii_name="resetCookies")
    def reset_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookies", []))

    @builtins.property
    @jsii.member(jsii_name="cookies")
    def cookies(
        self,
    ) -> CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesOutputReference:
        return typing.cast(CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesOutputReference, jsii.get(self, "cookies"))

    @builtins.property
    @jsii.member(jsii_name="cookieBehaviorInput")
    def cookie_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cookieBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesInput")
    def cookies_input(
        self,
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies], jsii.get(self, "cookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieBehavior")
    def cookie_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieBehavior"))

    @cookie_behavior.setter
    def cookie_behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig",
    jsii_struct_bases=[],
    name_mapping={"header_behavior": "headerBehavior", "headers": "headers"},
)
class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig:
    def __init__(
        self,
        *,
        header_behavior: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param header_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#header_behavior CloudfrontCachePolicy#header_behavior}.
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#headers CloudfrontCachePolicy#headers}
        '''
        if isinstance(headers, dict):
            headers = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders(**headers)
        if __debug__:
            def stub(
                *,
                header_behavior: typing.Optional[builtins.str] = None,
                headers: typing.Optional[typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument header_behavior", value=header_behavior, expected_type=type_hints["header_behavior"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
        self._values: typing.Dict[str, typing.Any] = {}
        if header_behavior is not None:
            self._values["header_behavior"] = header_behavior
        if headers is not None:
            self._values["headers"] = headers

    @builtins.property
    def header_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#header_behavior CloudfrontCachePolicy#header_behavior}.'''
        result = self._values.get("header_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders"]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#headers CloudfrontCachePolicy#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#items CloudfrontCachePolicy#items}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#items CloudfrontCachePolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersOutputReference",
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
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigOutputReference",
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

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#items CloudfrontCachePolicy#items}.
        '''
        value = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="resetHeaderBehavior")
    def reset_header_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderBehavior", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersOutputReference:
        return typing.cast(CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersOutputReference, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="headerBehaviorInput")
    def header_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="headerBehavior")
    def header_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerBehavior"))

    @header_behavior.setter
    def header_behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginOutputReference",
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

    @jsii.member(jsii_name="putCookiesConfig")
    def put_cookies_config(
        self,
        *,
        cookie_behavior: builtins.str,
        cookies: typing.Optional[typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cookie_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#cookie_behavior CloudfrontCachePolicy#cookie_behavior}.
        :param cookies: cookies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#cookies CloudfrontCachePolicy#cookies}
        '''
        value = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig(
            cookie_behavior=cookie_behavior, cookies=cookies
        )

        return typing.cast(None, jsii.invoke(self, "putCookiesConfig", [value]))

    @jsii.member(jsii_name="putHeadersConfig")
    def put_headers_config(
        self,
        *,
        header_behavior: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param header_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#header_behavior CloudfrontCachePolicy#header_behavior}.
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#headers CloudfrontCachePolicy#headers}
        '''
        value = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig(
            header_behavior=header_behavior, headers=headers
        )

        return typing.cast(None, jsii.invoke(self, "putHeadersConfig", [value]))

    @jsii.member(jsii_name="putQueryStringsConfig")
    def put_query_strings_config(
        self,
        *,
        query_string_behavior: builtins.str,
        query_strings: typing.Optional[typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param query_string_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#query_string_behavior CloudfrontCachePolicy#query_string_behavior}.
        :param query_strings: query_strings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#query_strings CloudfrontCachePolicy#query_strings}
        '''
        value = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig(
            query_string_behavior=query_string_behavior, query_strings=query_strings
        )

        return typing.cast(None, jsii.invoke(self, "putQueryStringsConfig", [value]))

    @jsii.member(jsii_name="resetEnableAcceptEncodingBrotli")
    def reset_enable_accept_encoding_brotli(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAcceptEncodingBrotli", []))

    @jsii.member(jsii_name="resetEnableAcceptEncodingGzip")
    def reset_enable_accept_encoding_gzip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAcceptEncodingGzip", []))

    @builtins.property
    @jsii.member(jsii_name="cookiesConfig")
    def cookies_config(
        self,
    ) -> CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigOutputReference:
        return typing.cast(CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigOutputReference, jsii.get(self, "cookiesConfig"))

    @builtins.property
    @jsii.member(jsii_name="headersConfig")
    def headers_config(
        self,
    ) -> CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigOutputReference:
        return typing.cast(CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigOutputReference, jsii.get(self, "headersConfig"))

    @builtins.property
    @jsii.member(jsii_name="queryStringsConfig")
    def query_strings_config(
        self,
    ) -> "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigOutputReference":
        return typing.cast("CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigOutputReference", jsii.get(self, "queryStringsConfig"))

    @builtins.property
    @jsii.member(jsii_name="cookiesConfigInput")
    def cookies_config_input(
        self,
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig], jsii.get(self, "cookiesConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAcceptEncodingBrotliInput")
    def enable_accept_encoding_brotli_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAcceptEncodingBrotliInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAcceptEncodingGzipInput")
    def enable_accept_encoding_gzip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAcceptEncodingGzipInput"))

    @builtins.property
    @jsii.member(jsii_name="headersConfigInput")
    def headers_config_input(
        self,
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig], jsii.get(self, "headersConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringsConfigInput")
    def query_strings_config_input(
        self,
    ) -> typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig"]:
        return typing.cast(typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig"], jsii.get(self, "queryStringsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAcceptEncodingBrotli")
    def enable_accept_encoding_brotli(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAcceptEncodingBrotli"))

    @enable_accept_encoding_brotli.setter
    def enable_accept_encoding_brotli(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAcceptEncodingBrotli", value)

    @builtins.property
    @jsii.member(jsii_name="enableAcceptEncodingGzip")
    def enable_accept_encoding_gzip(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAcceptEncodingGzip"))

    @enable_accept_encoding_gzip.setter
    def enable_accept_encoding_gzip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAcceptEncodingGzip", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "query_string_behavior": "queryStringBehavior",
        "query_strings": "queryStrings",
    },
)
class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig:
    def __init__(
        self,
        *,
        query_string_behavior: builtins.str,
        query_strings: typing.Optional[typing.Union["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param query_string_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#query_string_behavior CloudfrontCachePolicy#query_string_behavior}.
        :param query_strings: query_strings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#query_strings CloudfrontCachePolicy#query_strings}
        '''
        if isinstance(query_strings, dict):
            query_strings = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings(**query_strings)
        if __debug__:
            def stub(
                *,
                query_string_behavior: builtins.str,
                query_strings: typing.Optional[typing.Union[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument query_string_behavior", value=query_string_behavior, expected_type=type_hints["query_string_behavior"])
            check_type(argname="argument query_strings", value=query_strings, expected_type=type_hints["query_strings"])
        self._values: typing.Dict[str, typing.Any] = {
            "query_string_behavior": query_string_behavior,
        }
        if query_strings is not None:
            self._values["query_strings"] = query_strings

    @builtins.property
    def query_string_behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#query_string_behavior CloudfrontCachePolicy#query_string_behavior}.'''
        result = self._values.get("query_string_behavior")
        assert result is not None, "Required property 'query_string_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_strings(
        self,
    ) -> typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings"]:
        '''query_strings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#query_strings CloudfrontCachePolicy#query_strings}
        '''
        result = self._values.get("query_strings")
        return typing.cast(typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigOutputReference",
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

    @jsii.member(jsii_name="putQueryStrings")
    def put_query_strings(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#items CloudfrontCachePolicy#items}.
        '''
        value = CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putQueryStrings", [value]))

    @jsii.member(jsii_name="resetQueryStrings")
    def reset_query_strings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStrings", []))

    @builtins.property
    @jsii.member(jsii_name="queryStrings")
    def query_strings(
        self,
    ) -> "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsOutputReference":
        return typing.cast("CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsOutputReference", jsii.get(self, "queryStrings"))

    @builtins.property
    @jsii.member(jsii_name="queryStringBehaviorInput")
    def query_string_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryStringBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringsInput")
    def query_strings_input(
        self,
    ) -> typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings"]:
        return typing.cast(typing.Optional["CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings"], jsii.get(self, "queryStringsInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringBehavior")
    def query_string_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryStringBehavior"))

    @query_string_behavior.setter
    def query_string_behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param items: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#items CloudfrontCachePolicy#items}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_cache_policy#items CloudfrontCachePolicy#items}.'''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontCachePolicy.CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsOutputReference",
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
    ) -> typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings]:
        return typing.cast(typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudfrontCachePolicy",
    "CloudfrontCachePolicyConfig",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOrigin",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesOutputReference",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigOutputReference",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersOutputReference",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigOutputReference",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginOutputReference",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigOutputReference",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings",
    "CloudfrontCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsOutputReference",
]

publication.publish()
