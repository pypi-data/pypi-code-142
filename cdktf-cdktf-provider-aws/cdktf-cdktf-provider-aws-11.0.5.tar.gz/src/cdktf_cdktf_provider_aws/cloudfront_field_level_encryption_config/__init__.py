'''
# `aws_cloudfront_field_level_encryption_config`

Refer to the Terraform Registory for docs: [`aws_cloudfront_field_level_encryption_config`](https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config).
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


class CloudfrontFieldLevelEncryptionConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config aws_cloudfront_field_level_encryption_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        content_type_profile_config: typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig", typing.Dict[str, typing.Any]],
        query_arg_profile_config: typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig", typing.Dict[str, typing.Any]],
        comment: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config aws_cloudfront_field_level_encryption_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param content_type_profile_config: content_type_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profile_config CloudfrontFieldLevelEncryptionConfig#content_type_profile_config}
        :param query_arg_profile_config: query_arg_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profile_config CloudfrontFieldLevelEncryptionConfig#query_arg_profile_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#comment CloudfrontFieldLevelEncryptionConfig#comment}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#id CloudfrontFieldLevelEncryptionConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                content_type_profile_config: typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig, typing.Dict[str, typing.Any]],
                query_arg_profile_config: typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig, typing.Dict[str, typing.Any]],
                comment: typing.Optional[builtins.str] = None,
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
        config = CloudfrontFieldLevelEncryptionConfigConfig(
            content_type_profile_config=content_type_profile_config,
            query_arg_profile_config=query_arg_profile_config,
            comment=comment,
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

    @jsii.member(jsii_name="putContentTypeProfileConfig")
    def put_content_type_profile_config(
        self,
        *,
        content_type_profiles: typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles", typing.Dict[str, typing.Any]],
        forward_when_content_type_is_unknown: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param content_type_profiles: content_type_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profiles CloudfrontFieldLevelEncryptionConfig#content_type_profiles}
        :param forward_when_content_type_is_unknown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_content_type_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_content_type_is_unknown}.
        '''
        value = CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig(
            content_type_profiles=content_type_profiles,
            forward_when_content_type_is_unknown=forward_when_content_type_is_unknown,
        )

        return typing.cast(None, jsii.invoke(self, "putContentTypeProfileConfig", [value]))

    @jsii.member(jsii_name="putQueryArgProfileConfig")
    def put_query_arg_profile_config(
        self,
        *,
        forward_when_query_arg_profile_is_unknown: typing.Union[builtins.bool, cdktf.IResolvable],
        query_arg_profiles: typing.Optional[typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param forward_when_query_arg_profile_is_unknown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_query_arg_profile_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_query_arg_profile_is_unknown}.
        :param query_arg_profiles: query_arg_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profiles CloudfrontFieldLevelEncryptionConfig#query_arg_profiles}
        '''
        value = CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig(
            forward_when_query_arg_profile_is_unknown=forward_when_query_arg_profile_is_unknown,
            query_arg_profiles=query_arg_profiles,
        )

        return typing.cast(None, jsii.invoke(self, "putQueryArgProfileConfig", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

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
    @jsii.member(jsii_name="callerReference")
    def caller_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "callerReference"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeProfileConfig")
    def content_type_profile_config(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference":
        return typing.cast("CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference", jsii.get(self, "contentTypeProfileConfig"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="queryArgProfileConfig")
    def query_arg_profile_config(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference":
        return typing.cast("CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference", jsii.get(self, "queryArgProfileConfig"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeProfileConfigInput")
    def content_type_profile_config_input(
        self,
    ) -> typing.Optional["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig"]:
        return typing.cast(typing.Optional["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig"], jsii.get(self, "contentTypeProfileConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="queryArgProfileConfigInput")
    def query_arg_profile_config_input(
        self,
    ) -> typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig"]:
        return typing.cast(typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig"], jsii.get(self, "queryArgProfileConfigInput"))

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "content_type_profile_config": "contentTypeProfileConfig",
        "query_arg_profile_config": "queryArgProfileConfig",
        "comment": "comment",
        "id": "id",
    },
)
class CloudfrontFieldLevelEncryptionConfigConfig(cdktf.TerraformMetaArguments):
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
        content_type_profile_config: typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig", typing.Dict[str, typing.Any]],
        query_arg_profile_config: typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig", typing.Dict[str, typing.Any]],
        comment: typing.Optional[builtins.str] = None,
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
        :param content_type_profile_config: content_type_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profile_config CloudfrontFieldLevelEncryptionConfig#content_type_profile_config}
        :param query_arg_profile_config: query_arg_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profile_config CloudfrontFieldLevelEncryptionConfig#query_arg_profile_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#comment CloudfrontFieldLevelEncryptionConfig#comment}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#id CloudfrontFieldLevelEncryptionConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(content_type_profile_config, dict):
            content_type_profile_config = CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig(**content_type_profile_config)
        if isinstance(query_arg_profile_config, dict):
            query_arg_profile_config = CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig(**query_arg_profile_config)
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
                content_type_profile_config: typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig, typing.Dict[str, typing.Any]],
                query_arg_profile_config: typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig, typing.Dict[str, typing.Any]],
                comment: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument content_type_profile_config", value=content_type_profile_config, expected_type=type_hints["content_type_profile_config"])
            check_type(argname="argument query_arg_profile_config", value=query_arg_profile_config, expected_type=type_hints["query_arg_profile_config"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_type_profile_config": content_type_profile_config,
            "query_arg_profile_config": query_arg_profile_config,
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
    def content_type_profile_config(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig":
        '''content_type_profile_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profile_config CloudfrontFieldLevelEncryptionConfig#content_type_profile_config}
        '''
        result = self._values.get("content_type_profile_config")
        assert result is not None, "Required property 'content_type_profile_config' is missing"
        return typing.cast("CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig", result)

    @builtins.property
    def query_arg_profile_config(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig":
        '''query_arg_profile_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profile_config CloudfrontFieldLevelEncryptionConfig#query_arg_profile_config}
        '''
        result = self._values.get("query_arg_profile_config")
        assert result is not None, "Required property 'query_arg_profile_config' is missing"
        return typing.cast("CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig", result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#comment CloudfrontFieldLevelEncryptionConfig#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#id CloudfrontFieldLevelEncryptionConfig#id}.

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
        return "CloudfrontFieldLevelEncryptionConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig",
    jsii_struct_bases=[],
    name_mapping={
        "content_type_profiles": "contentTypeProfiles",
        "forward_when_content_type_is_unknown": "forwardWhenContentTypeIsUnknown",
    },
)
class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig:
    def __init__(
        self,
        *,
        content_type_profiles: typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles", typing.Dict[str, typing.Any]],
        forward_when_content_type_is_unknown: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param content_type_profiles: content_type_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profiles CloudfrontFieldLevelEncryptionConfig#content_type_profiles}
        :param forward_when_content_type_is_unknown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_content_type_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_content_type_is_unknown}.
        '''
        if isinstance(content_type_profiles, dict):
            content_type_profiles = CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles(**content_type_profiles)
        if __debug__:
            def stub(
                *,
                content_type_profiles: typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles, typing.Dict[str, typing.Any]],
                forward_when_content_type_is_unknown: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content_type_profiles", value=content_type_profiles, expected_type=type_hints["content_type_profiles"])
            check_type(argname="argument forward_when_content_type_is_unknown", value=forward_when_content_type_is_unknown, expected_type=type_hints["forward_when_content_type_is_unknown"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_type_profiles": content_type_profiles,
            "forward_when_content_type_is_unknown": forward_when_content_type_is_unknown,
        }

    @builtins.property
    def content_type_profiles(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles":
        '''content_type_profiles block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profiles CloudfrontFieldLevelEncryptionConfig#content_type_profiles}
        '''
        result = self._values.get("content_type_profiles")
        assert result is not None, "Required property 'content_type_profiles' is missing"
        return typing.cast("CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles", result)

    @builtins.property
    def forward_when_content_type_is_unknown(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_content_type_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_content_type_is_unknown}.'''
        result = self._values.get("forward_when_content_type_is_unknown")
        assert result is not None, "Required property 'forward_when_content_type_is_unknown' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles:
    def __init__(
        self,
        *,
        items: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        if __debug__:
            def stub(
                *,
                items: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[str, typing.Any] = {
            "items": items,
        }

    @builtins.property
    def items(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems"]]:
        '''items block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        result = self._values.get("items")
        assert result is not None, "Required property 'items' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems",
    jsii_struct_bases=[],
    name_mapping={
        "content_type": "contentType",
        "format": "format",
        "profile_id": "profileId",
    },
)
class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems:
    def __init__(
        self,
        *,
        content_type: builtins.str,
        format: builtins.str,
        profile_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type CloudfrontFieldLevelEncryptionConfig#content_type}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#format CloudfrontFieldLevelEncryptionConfig#format}.
        :param profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#profile_id CloudfrontFieldLevelEncryptionConfig#profile_id}.
        '''
        if __debug__:
            def stub(
                *,
                content_type: builtins.str,
                format: builtins.str,
                profile_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_type": content_type,
            "format": format,
        }
        if profile_id is not None:
            self._values["profile_id"] = profile_id

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type CloudfrontFieldLevelEncryptionConfig#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#format CloudfrontFieldLevelEncryptionConfig#format}.'''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#profile_id CloudfrontFieldLevelEncryptionConfig#profile_id}.'''
        result = self._values.get("profile_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList",
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
    ) -> "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference",
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

    @jsii.member(jsii_name="resetProfileId")
    def reset_profile_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfileId", []))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="profileIdInput")
    def profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference",
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putItems", [value]))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(
        self,
    ) -> CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList:
        return typing.cast(CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList, jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference",
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

    @jsii.member(jsii_name="putContentTypeProfiles")
    def put_content_type_profiles(
        self,
        *,
        items: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        value = CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putContentTypeProfiles", [value]))

    @builtins.property
    @jsii.member(jsii_name="contentTypeProfiles")
    def content_type_profiles(
        self,
    ) -> CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference:
        return typing.cast(CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference, jsii.get(self, "contentTypeProfiles"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeProfilesInput")
    def content_type_profiles_input(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles], jsii.get(self, "contentTypeProfilesInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardWhenContentTypeIsUnknownInput")
    def forward_when_content_type_is_unknown_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forwardWhenContentTypeIsUnknownInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardWhenContentTypeIsUnknown")
    def forward_when_content_type_is_unknown(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forwardWhenContentTypeIsUnknown"))

    @forward_when_content_type_is_unknown.setter
    def forward_when_content_type_is_unknown(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardWhenContentTypeIsUnknown", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig",
    jsii_struct_bases=[],
    name_mapping={
        "forward_when_query_arg_profile_is_unknown": "forwardWhenQueryArgProfileIsUnknown",
        "query_arg_profiles": "queryArgProfiles",
    },
)
class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig:
    def __init__(
        self,
        *,
        forward_when_query_arg_profile_is_unknown: typing.Union[builtins.bool, cdktf.IResolvable],
        query_arg_profiles: typing.Optional[typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param forward_when_query_arg_profile_is_unknown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_query_arg_profile_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_query_arg_profile_is_unknown}.
        :param query_arg_profiles: query_arg_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profiles CloudfrontFieldLevelEncryptionConfig#query_arg_profiles}
        '''
        if isinstance(query_arg_profiles, dict):
            query_arg_profiles = CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles(**query_arg_profiles)
        if __debug__:
            def stub(
                *,
                forward_when_query_arg_profile_is_unknown: typing.Union[builtins.bool, cdktf.IResolvable],
                query_arg_profiles: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument forward_when_query_arg_profile_is_unknown", value=forward_when_query_arg_profile_is_unknown, expected_type=type_hints["forward_when_query_arg_profile_is_unknown"])
            check_type(argname="argument query_arg_profiles", value=query_arg_profiles, expected_type=type_hints["query_arg_profiles"])
        self._values: typing.Dict[str, typing.Any] = {
            "forward_when_query_arg_profile_is_unknown": forward_when_query_arg_profile_is_unknown,
        }
        if query_arg_profiles is not None:
            self._values["query_arg_profiles"] = query_arg_profiles

    @builtins.property
    def forward_when_query_arg_profile_is_unknown(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_query_arg_profile_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_query_arg_profile_is_unknown}.'''
        result = self._values.get("forward_when_query_arg_profile_is_unknown")
        assert result is not None, "Required property 'forward_when_query_arg_profile_is_unknown' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def query_arg_profiles(
        self,
    ) -> typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles"]:
        '''query_arg_profiles block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profiles CloudfrontFieldLevelEncryptionConfig#query_arg_profiles}
        '''
        result = self._values.get("query_arg_profiles")
        return typing.cast(typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference",
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

    @jsii.member(jsii_name="putQueryArgProfiles")
    def put_query_arg_profiles(
        self,
        *,
        items: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        value = CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putQueryArgProfiles", [value]))

    @jsii.member(jsii_name="resetQueryArgProfiles")
    def reset_query_arg_profiles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryArgProfiles", []))

    @builtins.property
    @jsii.member(jsii_name="queryArgProfiles")
    def query_arg_profiles(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference":
        return typing.cast("CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference", jsii.get(self, "queryArgProfiles"))

    @builtins.property
    @jsii.member(jsii_name="forwardWhenQueryArgProfileIsUnknownInput")
    def forward_when_query_arg_profile_is_unknown_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forwardWhenQueryArgProfileIsUnknownInput"))

    @builtins.property
    @jsii.member(jsii_name="queryArgProfilesInput")
    def query_arg_profiles_input(
        self,
    ) -> typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles"]:
        return typing.cast(typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles"], jsii.get(self, "queryArgProfilesInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardWhenQueryArgProfileIsUnknown")
    def forward_when_query_arg_profile_is_unknown(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forwardWhenQueryArgProfileIsUnknown"))

    @forward_when_query_arg_profile_is_unknown.setter
    def forward_when_query_arg_profile_is_unknown(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardWhenQueryArgProfileIsUnknown", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        if __debug__:
            def stub(
                *,
                items: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, typing.Dict[str, typing.Any]]]]] = None,
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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems"]]]:
        '''items block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems",
    jsii_struct_bases=[],
    name_mapping={"profile_id": "profileId", "query_arg": "queryArg"},
)
class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems:
    def __init__(self, *, profile_id: builtins.str, query_arg: builtins.str) -> None:
        '''
        :param profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#profile_id CloudfrontFieldLevelEncryptionConfig#profile_id}.
        :param query_arg: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg CloudfrontFieldLevelEncryptionConfig#query_arg}.
        '''
        if __debug__:
            def stub(*, profile_id: builtins.str, query_arg: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
            check_type(argname="argument query_arg", value=query_arg, expected_type=type_hints["query_arg"])
        self._values: typing.Dict[str, typing.Any] = {
            "profile_id": profile_id,
            "query_arg": query_arg,
        }

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#profile_id CloudfrontFieldLevelEncryptionConfig#profile_id}.'''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_arg(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg CloudfrontFieldLevelEncryptionConfig#query_arg}.'''
        result = self._values.get("query_arg")
        assert result is not None, "Required property 'query_arg' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList",
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
    ) -> "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference",
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
    @jsii.member(jsii_name="profileIdInput")
    def profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryArgInput")
    def query_arg_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryArgInput"))

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value)

    @builtins.property
    @jsii.member(jsii_name="queryArg")
    def query_arg(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryArg"))

    @query_arg.setter
    def query_arg(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryArg", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference",
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, typing.Dict[str, typing.Any]]]],
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
    def items(
        self,
    ) -> CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList:
        return typing.cast(CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList, jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudfrontFieldLevelEncryptionConfig",
    "CloudfrontFieldLevelEncryptionConfigConfig",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference",
]

publication.publish()
