'''
# `aws_s3control_storage_lens_configuration`

Refer to the Terraform Registory for docs: [`aws_s3control_storage_lens_configuration`](https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration).
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


class S3ControlStorageLensConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration aws_s3control_storage_lens_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        config_id: builtins.str,
        storage_lens_configuration: typing.Union["S3ControlStorageLensConfigurationStorageLensConfiguration", typing.Dict[str, typing.Any]],
        account_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration aws_s3control_storage_lens_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#config_id S3ControlStorageLensConfiguration#config_id}.
        :param storage_lens_configuration: storage_lens_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_lens_configuration S3ControlStorageLensConfiguration#storage_lens_configuration}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#id S3ControlStorageLensConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags S3ControlStorageLensConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags_all S3ControlStorageLensConfiguration#tags_all}.
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
                config_id: builtins.str,
                storage_lens_configuration: typing.Union[S3ControlStorageLensConfigurationStorageLensConfiguration, typing.Dict[str, typing.Any]],
                account_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
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
        config = S3ControlStorageLensConfigurationConfig(
            config_id=config_id,
            storage_lens_configuration=storage_lens_configuration,
            account_id=account_id,
            id=id,
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

    @jsii.member(jsii_name="putStorageLensConfiguration")
    def put_storage_lens_configuration(
        self,
        *,
        account_level: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel", typing.Dict[str, typing.Any]],
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        aws_org: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg", typing.Dict[str, typing.Any]]] = None,
        data_export: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExport", typing.Dict[str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationExclude", typing.Dict[str, typing.Any]]] = None,
        include: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationInclude", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param account_level: account_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_level S3ControlStorageLensConfiguration#account_level}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        :param aws_org: aws_org block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#aws_org S3ControlStorageLensConfiguration#aws_org}
        :param data_export: data_export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#data_export S3ControlStorageLensConfiguration#data_export}
        :param exclude: exclude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#exclude S3ControlStorageLensConfiguration#exclude}
        :param include: include block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#include S3ControlStorageLensConfiguration#include}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfiguration(
            account_level=account_level,
            enabled=enabled,
            aws_org=aws_org,
            data_export=data_export,
            exclude=exclude,
            include=include,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageLensConfiguration", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="storageLensConfiguration")
    def storage_lens_configuration(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference", jsii.get(self, "storageLensConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configIdInput")
    def config_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="storageLensConfigurationInput")
    def storage_lens_configuration_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfiguration"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfiguration"], jsii.get(self, "storageLensConfigurationInput"))

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
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

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
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "config_id": "configId",
        "storage_lens_configuration": "storageLensConfiguration",
        "account_id": "accountId",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class S3ControlStorageLensConfigurationConfig(cdktf.TerraformMetaArguments):
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
        config_id: builtins.str,
        storage_lens_configuration: typing.Union["S3ControlStorageLensConfigurationStorageLensConfiguration", typing.Dict[str, typing.Any]],
        account_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
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
        :param config_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#config_id S3ControlStorageLensConfiguration#config_id}.
        :param storage_lens_configuration: storage_lens_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_lens_configuration S3ControlStorageLensConfiguration#storage_lens_configuration}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#id S3ControlStorageLensConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags S3ControlStorageLensConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags_all S3ControlStorageLensConfiguration#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(storage_lens_configuration, dict):
            storage_lens_configuration = S3ControlStorageLensConfigurationStorageLensConfiguration(**storage_lens_configuration)
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
                config_id: builtins.str,
                storage_lens_configuration: typing.Union[S3ControlStorageLensConfigurationStorageLensConfiguration, typing.Dict[str, typing.Any]],
                account_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument storage_lens_configuration", value=storage_lens_configuration, expected_type=type_hints["storage_lens_configuration"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "config_id": config_id,
            "storage_lens_configuration": storage_lens_configuration,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if id is not None:
            self._values["id"] = id
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
    def config_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#config_id S3ControlStorageLensConfiguration#config_id}.'''
        result = self._values.get("config_id")
        assert result is not None, "Required property 'config_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_lens_configuration(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfiguration":
        '''storage_lens_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_lens_configuration S3ControlStorageLensConfiguration#storage_lens_configuration}
        '''
        result = self._values.get("storage_lens_configuration")
        assert result is not None, "Required property 'storage_lens_configuration' is missing"
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfiguration", result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#id S3ControlStorageLensConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags S3ControlStorageLensConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags_all S3ControlStorageLensConfiguration#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "account_level": "accountLevel",
        "enabled": "enabled",
        "aws_org": "awsOrg",
        "data_export": "dataExport",
        "exclude": "exclude",
        "include": "include",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfiguration:
    def __init__(
        self,
        *,
        account_level: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel", typing.Dict[str, typing.Any]],
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        aws_org: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg", typing.Dict[str, typing.Any]]] = None,
        data_export: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExport", typing.Dict[str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationExclude", typing.Dict[str, typing.Any]]] = None,
        include: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationInclude", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param account_level: account_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_level S3ControlStorageLensConfiguration#account_level}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        :param aws_org: aws_org block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#aws_org S3ControlStorageLensConfiguration#aws_org}
        :param data_export: data_export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#data_export S3ControlStorageLensConfiguration#data_export}
        :param exclude: exclude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#exclude S3ControlStorageLensConfiguration#exclude}
        :param include: include block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#include S3ControlStorageLensConfiguration#include}
        '''
        if isinstance(account_level, dict):
            account_level = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel(**account_level)
        if isinstance(aws_org, dict):
            aws_org = S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg(**aws_org)
        if isinstance(data_export, dict):
            data_export = S3ControlStorageLensConfigurationStorageLensConfigurationDataExport(**data_export)
        if isinstance(exclude, dict):
            exclude = S3ControlStorageLensConfigurationStorageLensConfigurationExclude(**exclude)
        if isinstance(include, dict):
            include = S3ControlStorageLensConfigurationStorageLensConfigurationInclude(**include)
        if __debug__:
            def stub(
                *,
                account_level: typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel, typing.Dict[str, typing.Any]],
                enabled: typing.Union[builtins.bool, cdktf.IResolvable],
                aws_org: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg, typing.Dict[str, typing.Any]]] = None,
                data_export: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport, typing.Dict[str, typing.Any]]] = None,
                exclude: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationExclude, typing.Dict[str, typing.Any]]] = None,
                include: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationInclude, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument account_level", value=account_level, expected_type=type_hints["account_level"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument aws_org", value=aws_org, expected_type=type_hints["aws_org"])
            check_type(argname="argument data_export", value=data_export, expected_type=type_hints["data_export"])
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_level": account_level,
            "enabled": enabled,
        }
        if aws_org is not None:
            self._values["aws_org"] = aws_org
        if data_export is not None:
            self._values["data_export"] = data_export
        if exclude is not None:
            self._values["exclude"] = exclude
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def account_level(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel":
        '''account_level block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_level S3ControlStorageLensConfiguration#account_level}
        '''
        result = self._values.get("account_level")
        assert result is not None, "Required property 'account_level' is missing"
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel", result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def aws_org(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg"]:
        '''aws_org block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#aws_org S3ControlStorageLensConfiguration#aws_org}
        '''
        result = self._values.get("aws_org")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg"], result)

    @builtins.property
    def data_export(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExport"]:
        '''data_export block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#data_export S3ControlStorageLensConfiguration#data_export}
        '''
        result = self._values.get("data_export")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExport"], result)

    @builtins.property
    def exclude(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationExclude"]:
        '''exclude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#exclude S3ControlStorageLensConfiguration#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationExclude"], result)

    @builtins.property
    def include(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationInclude"]:
        '''include block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#include S3ControlStorageLensConfiguration#include}
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationInclude"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_level": "bucketLevel",
        "activity_metrics": "activityMetrics",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel:
    def __init__(
        self,
        *,
        bucket_level: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel", typing.Dict[str, typing.Any]],
        activity_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_level: bucket_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#bucket_level S3ControlStorageLensConfiguration#bucket_level}
        :param activity_metrics: activity_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        '''
        if isinstance(bucket_level, dict):
            bucket_level = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel(**bucket_level)
        if isinstance(activity_metrics, dict):
            activity_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics(**activity_metrics)
        if __debug__:
            def stub(
                *,
                bucket_level: typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel, typing.Dict[str, typing.Any]],
                activity_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_level", value=bucket_level, expected_type=type_hints["bucket_level"])
            check_type(argname="argument activity_metrics", value=activity_metrics, expected_type=type_hints["activity_metrics"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_level": bucket_level,
        }
        if activity_metrics is not None:
            self._values["activity_metrics"] = activity_metrics

    @builtins.property
    def bucket_level(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel":
        '''bucket_level block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#bucket_level S3ControlStorageLensConfiguration#bucket_level}
        '''
        result = self._values.get("bucket_level")
        assert result is not None, "Required property 'bucket_level' is missing"
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel", result)

    @builtins.property
    def activity_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics"]:
        '''activity_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        '''
        result = self._values.get("activity_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel",
    jsii_struct_bases=[],
    name_mapping={
        "activity_metrics": "activityMetrics",
        "prefix_level": "prefixLevel",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel:
    def __init__(
        self,
        *,
        activity_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics", typing.Dict[str, typing.Any]]] = None,
        prefix_level: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param activity_metrics: activity_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        :param prefix_level: prefix_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix_level S3ControlStorageLensConfiguration#prefix_level}
        '''
        if isinstance(activity_metrics, dict):
            activity_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics(**activity_metrics)
        if isinstance(prefix_level, dict):
            prefix_level = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel(**prefix_level)
        if __debug__:
            def stub(
                *,
                activity_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics, typing.Dict[str, typing.Any]]] = None,
                prefix_level: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument activity_metrics", value=activity_metrics, expected_type=type_hints["activity_metrics"])
            check_type(argname="argument prefix_level", value=prefix_level, expected_type=type_hints["prefix_level"])
        self._values: typing.Dict[str, typing.Any] = {}
        if activity_metrics is not None:
            self._values["activity_metrics"] = activity_metrics
        if prefix_level is not None:
            self._values["prefix_level"] = prefix_level

    @builtins.property
    def activity_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics"]:
        '''activity_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        '''
        result = self._values.get("activity_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics"], result)

    @builtins.property
    def prefix_level(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel"]:
        '''prefix_level block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix_level S3ControlStorageLensConfiguration#prefix_level}
        '''
        result = self._values.get("prefix_level")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference",
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

    @jsii.member(jsii_name="putActivityMetrics")
    def put_activity_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putActivityMetrics", [value]))

    @jsii.member(jsii_name="putPrefixLevel")
    def put_prefix_level(
        self,
        *,
        storage_metrics: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param storage_metrics: storage_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_metrics S3ControlStorageLensConfiguration#storage_metrics}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel(
            storage_metrics=storage_metrics
        )

        return typing.cast(None, jsii.invoke(self, "putPrefixLevel", [value]))

    @jsii.member(jsii_name="resetActivityMetrics")
    def reset_activity_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivityMetrics", []))

    @jsii.member(jsii_name="resetPrefixLevel")
    def reset_prefix_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixLevel", []))

    @builtins.property
    @jsii.member(jsii_name="activityMetrics")
    def activity_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference, jsii.get(self, "activityMetrics"))

    @builtins.property
    @jsii.member(jsii_name="prefixLevel")
    def prefix_level(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference", jsii.get(self, "prefixLevel"))

    @builtins.property
    @jsii.member(jsii_name="activityMetricsInput")
    def activity_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics], jsii.get(self, "activityMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixLevelInput")
    def prefix_level_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel"], jsii.get(self, "prefixLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel",
    jsii_struct_bases=[],
    name_mapping={"storage_metrics": "storageMetrics"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel:
    def __init__(
        self,
        *,
        storage_metrics: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param storage_metrics: storage_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_metrics S3ControlStorageLensConfiguration#storage_metrics}
        '''
        if isinstance(storage_metrics, dict):
            storage_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics(**storage_metrics)
        if __debug__:
            def stub(
                *,
                storage_metrics: typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument storage_metrics", value=storage_metrics, expected_type=type_hints["storage_metrics"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage_metrics": storage_metrics,
        }

    @builtins.property
    def storage_metrics(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics":
        '''storage_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_metrics S3ControlStorageLensConfiguration#storage_metrics}
        '''
        result = self._values.get("storage_metrics")
        assert result is not None, "Required property 'storage_metrics' is missing"
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference",
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

    @jsii.member(jsii_name="putStorageMetrics")
    def put_storage_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        selection_criteria: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        :param selection_criteria: selection_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#selection_criteria S3ControlStorageLensConfiguration#selection_criteria}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics(
            enabled=enabled, selection_criteria=selection_criteria
        )

        return typing.cast(None, jsii.invoke(self, "putStorageMetrics", [value]))

    @builtins.property
    @jsii.member(jsii_name="storageMetrics")
    def storage_metrics(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference", jsii.get(self, "storageMetrics"))

    @builtins.property
    @jsii.member(jsii_name="storageMetricsInput")
    def storage_metrics_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics"], jsii.get(self, "storageMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "selection_criteria": "selectionCriteria"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        selection_criteria: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        :param selection_criteria: selection_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#selection_criteria S3ControlStorageLensConfiguration#selection_criteria}
        '''
        if isinstance(selection_criteria, dict):
            selection_criteria = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria(**selection_criteria)
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                selection_criteria: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if selection_criteria is not None:
            self._values["selection_criteria"] = selection_criteria

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def selection_criteria(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria"]:
        '''selection_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#selection_criteria S3ControlStorageLensConfiguration#selection_criteria}
        '''
        result = self._values.get("selection_criteria")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference",
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

    @jsii.member(jsii_name="putSelectionCriteria")
    def put_selection_criteria(
        self,
        *,
        delimiter: typing.Optional[builtins.str] = None,
        max_depth: typing.Optional[jsii.Number] = None,
        min_storage_bytes_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#delimiter S3ControlStorageLensConfiguration#delimiter}.
        :param max_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#max_depth S3ControlStorageLensConfiguration#max_depth}.
        :param min_storage_bytes_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#min_storage_bytes_percentage S3ControlStorageLensConfiguration#min_storage_bytes_percentage}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria(
            delimiter=delimiter,
            max_depth=max_depth,
            min_storage_bytes_percentage=min_storage_bytes_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putSelectionCriteria", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetSelectionCriteria")
    def reset_selection_criteria(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectionCriteria", []))

    @builtins.property
    @jsii.member(jsii_name="selectionCriteria")
    def selection_criteria(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference", jsii.get(self, "selectionCriteria"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="selectionCriteriaInput")
    def selection_criteria_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria"], jsii.get(self, "selectionCriteriaInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria",
    jsii_struct_bases=[],
    name_mapping={
        "delimiter": "delimiter",
        "max_depth": "maxDepth",
        "min_storage_bytes_percentage": "minStorageBytesPercentage",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria:
    def __init__(
        self,
        *,
        delimiter: typing.Optional[builtins.str] = None,
        max_depth: typing.Optional[jsii.Number] = None,
        min_storage_bytes_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#delimiter S3ControlStorageLensConfiguration#delimiter}.
        :param max_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#max_depth S3ControlStorageLensConfiguration#max_depth}.
        :param min_storage_bytes_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#min_storage_bytes_percentage S3ControlStorageLensConfiguration#min_storage_bytes_percentage}.
        '''
        if __debug__:
            def stub(
                *,
                delimiter: typing.Optional[builtins.str] = None,
                max_depth: typing.Optional[jsii.Number] = None,
                min_storage_bytes_percentage: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
            check_type(argname="argument max_depth", value=max_depth, expected_type=type_hints["max_depth"])
            check_type(argname="argument min_storage_bytes_percentage", value=min_storage_bytes_percentage, expected_type=type_hints["min_storage_bytes_percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delimiter is not None:
            self._values["delimiter"] = delimiter
        if max_depth is not None:
            self._values["max_depth"] = max_depth
        if min_storage_bytes_percentage is not None:
            self._values["min_storage_bytes_percentage"] = min_storage_bytes_percentage

    @builtins.property
    def delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#delimiter S3ControlStorageLensConfiguration#delimiter}.'''
        result = self._values.get("delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_depth(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#max_depth S3ControlStorageLensConfiguration#max_depth}.'''
        result = self._values.get("max_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_storage_bytes_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#min_storage_bytes_percentage S3ControlStorageLensConfiguration#min_storage_bytes_percentage}.'''
        result = self._values.get("min_storage_bytes_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference",
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

    @jsii.member(jsii_name="resetDelimiter")
    def reset_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelimiter", []))

    @jsii.member(jsii_name="resetMaxDepth")
    def reset_max_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDepth", []))

    @jsii.member(jsii_name="resetMinStorageBytesPercentage")
    def reset_min_storage_bytes_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinStorageBytesPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="delimiterInput")
    def delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDepthInput")
    def max_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="minStorageBytesPercentageInput")
    def min_storage_bytes_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minStorageBytesPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="delimiter")
    def delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delimiter"))

    @delimiter.setter
    def delimiter(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delimiter", value)

    @builtins.property
    @jsii.member(jsii_name="maxDepth")
    def max_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDepth"))

    @max_depth.setter
    def max_depth(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDepth", value)

    @builtins.property
    @jsii.member(jsii_name="minStorageBytesPercentage")
    def min_storage_bytes_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minStorageBytesPercentage"))

    @min_storage_bytes_percentage.setter
    def min_storage_bytes_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minStorageBytesPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference",
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

    @jsii.member(jsii_name="putActivityMetrics")
    def put_activity_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putActivityMetrics", [value]))

    @jsii.member(jsii_name="putBucketLevel")
    def put_bucket_level(
        self,
        *,
        activity_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics, typing.Dict[str, typing.Any]]] = None,
        prefix_level: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param activity_metrics: activity_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        :param prefix_level: prefix_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix_level S3ControlStorageLensConfiguration#prefix_level}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel(
            activity_metrics=activity_metrics, prefix_level=prefix_level
        )

        return typing.cast(None, jsii.invoke(self, "putBucketLevel", [value]))

    @jsii.member(jsii_name="resetActivityMetrics")
    def reset_activity_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivityMetrics", []))

    @builtins.property
    @jsii.member(jsii_name="activityMetrics")
    def activity_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference, jsii.get(self, "activityMetrics"))

    @builtins.property
    @jsii.member(jsii_name="bucketLevel")
    def bucket_level(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference, jsii.get(self, "bucketLevel"))

    @builtins.property
    @jsii.member(jsii_name="activityMetricsInput")
    def activity_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics], jsii.get(self, "activityMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketLevelInput")
    def bucket_level_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel], jsii.get(self, "bucketLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg:
    def __init__(self, *, arn: builtins.str) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.
        '''
        if __debug__:
            def stub(*, arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference",
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
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExport",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_watch_metrics": "cloudWatchMetrics",
        "s3_bucket_destination": "s3BucketDestination",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExport:
    def __init__(
        self,
        *,
        cloud_watch_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics", typing.Dict[str, typing.Any]]] = None,
        s3_bucket_destination: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloud_watch_metrics: cloud_watch_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#cloud_watch_metrics S3ControlStorageLensConfiguration#cloud_watch_metrics}
        :param s3_bucket_destination: s3_bucket_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#s3_bucket_destination S3ControlStorageLensConfiguration#s3_bucket_destination}
        '''
        if isinstance(cloud_watch_metrics, dict):
            cloud_watch_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics(**cloud_watch_metrics)
        if isinstance(s3_bucket_destination, dict):
            s3_bucket_destination = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination(**s3_bucket_destination)
        if __debug__:
            def stub(
                *,
                cloud_watch_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics, typing.Dict[str, typing.Any]]] = None,
                s3_bucket_destination: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cloud_watch_metrics", value=cloud_watch_metrics, expected_type=type_hints["cloud_watch_metrics"])
            check_type(argname="argument s3_bucket_destination", value=s3_bucket_destination, expected_type=type_hints["s3_bucket_destination"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloud_watch_metrics is not None:
            self._values["cloud_watch_metrics"] = cloud_watch_metrics
        if s3_bucket_destination is not None:
            self._values["s3_bucket_destination"] = s3_bucket_destination

    @builtins.property
    def cloud_watch_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics"]:
        '''cloud_watch_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#cloud_watch_metrics S3ControlStorageLensConfiguration#cloud_watch_metrics}
        '''
        result = self._values.get("cloud_watch_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics"], result)

    @builtins.property
    def s3_bucket_destination(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination"]:
        '''s3_bucket_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#s3_bucket_destination S3ControlStorageLensConfiguration#s3_bucket_destination}
        '''
        result = self._values.get("s3_bucket_destination")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExport(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference",
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

    @jsii.member(jsii_name="putCloudWatchMetrics")
    def put_cloud_watch_metrics(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putCloudWatchMetrics", [value]))

    @jsii.member(jsii_name="putS3BucketDestination")
    def put_s3_bucket_destination(
        self,
        *,
        account_id: builtins.str,
        arn: builtins.str,
        format: builtins.str,
        output_schema_version: builtins.str,
        encryption: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption", typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#format S3ControlStorageLensConfiguration#format}.
        :param output_schema_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#output_schema_version S3ControlStorageLensConfiguration#output_schema_version}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#encryption S3ControlStorageLensConfiguration#encryption}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix S3ControlStorageLensConfiguration#prefix}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination(
            account_id=account_id,
            arn=arn,
            format=format,
            output_schema_version=output_schema_version,
            encryption=encryption,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3BucketDestination", [value]))

    @jsii.member(jsii_name="resetCloudWatchMetrics")
    def reset_cloud_watch_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudWatchMetrics", []))

    @jsii.member(jsii_name="resetS3BucketDestination")
    def reset_s3_bucket_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BucketDestination", []))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchMetrics")
    def cloud_watch_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference, jsii.get(self, "cloudWatchMetrics"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketDestination")
    def s3_bucket_destination(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference", jsii.get(self, "s3BucketDestination"))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchMetricsInput")
    def cloud_watch_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics], jsii.get(self, "cloudWatchMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketDestinationInput")
    def s3_bucket_destination_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination"], jsii.get(self, "s3BucketDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "arn": "arn",
        "format": "format",
        "output_schema_version": "outputSchemaVersion",
        "encryption": "encryption",
        "prefix": "prefix",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        arn: builtins.str,
        format: builtins.str,
        output_schema_version: builtins.str,
        encryption: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption", typing.Dict[str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#format S3ControlStorageLensConfiguration#format}.
        :param output_schema_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#output_schema_version S3ControlStorageLensConfiguration#output_schema_version}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#encryption S3ControlStorageLensConfiguration#encryption}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix S3ControlStorageLensConfiguration#prefix}.
        '''
        if isinstance(encryption, dict):
            encryption = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption(**encryption)
        if __debug__:
            def stub(
                *,
                account_id: builtins.str,
                arn: builtins.str,
                format: builtins.str,
                output_schema_version: builtins.str,
                encryption: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption, typing.Dict[str, typing.Any]]] = None,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument output_schema_version", value=output_schema_version, expected_type=type_hints["output_schema_version"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "arn": arn,
            "format": format,
            "output_schema_version": output_schema_version,
        }
        if encryption is not None:
            self._values["encryption"] = encryption
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#format S3ControlStorageLensConfiguration#format}.'''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output_schema_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#output_schema_version S3ControlStorageLensConfiguration#output_schema_version}.'''
        result = self._values.get("output_schema_version")
        assert result is not None, "Required property 'output_schema_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption"]:
        '''encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#encryption S3ControlStorageLensConfiguration#encryption}
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption"], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix S3ControlStorageLensConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption",
    jsii_struct_bases=[],
    name_mapping={"sse_kms": "sseKms", "sse_s3": "sseS3"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption:
    def __init__(
        self,
        *,
        sse_kms: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms", typing.Dict[str, typing.Any]]] = None,
        sse_s3: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param sse_kms: sse_kms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_kms S3ControlStorageLensConfiguration#sse_kms}
        :param sse_s3: sse_s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_s3 S3ControlStorageLensConfiguration#sse_s3}
        '''
        if isinstance(sse_kms, dict):
            sse_kms = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms(**sse_kms)
        if __debug__:
            def stub(
                *,
                sse_kms: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms, typing.Dict[str, typing.Any]]] = None,
                sse_s3: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument sse_kms", value=sse_kms, expected_type=type_hints["sse_kms"])
            check_type(argname="argument sse_s3", value=sse_s3, expected_type=type_hints["sse_s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if sse_kms is not None:
            self._values["sse_kms"] = sse_kms
        if sse_s3 is not None:
            self._values["sse_s3"] = sse_s3

    @builtins.property
    def sse_kms(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms"]:
        '''sse_kms block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_kms S3ControlStorageLensConfiguration#sse_kms}
        '''
        result = self._values.get("sse_kms")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms"], result)

    @builtins.property
    def sse_s3(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3"]]]:
        '''sse_s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_s3 S3ControlStorageLensConfiguration#sse_s3}
        '''
        result = self._values.get("sse_s3")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference",
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

    @jsii.member(jsii_name="putSseKms")
    def put_sse_kms(self, *, key_id: builtins.str) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#key_id S3ControlStorageLensConfiguration#key_id}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms(
            key_id=key_id
        )

        return typing.cast(None, jsii.invoke(self, "putSseKms", [value]))

    @jsii.member(jsii_name="putSseS3")
    def put_sse_s3(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSseS3", [value]))

    @jsii.member(jsii_name="resetSseKms")
    def reset_sse_kms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseKms", []))

    @jsii.member(jsii_name="resetSseS3")
    def reset_sse_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseS3", []))

    @builtins.property
    @jsii.member(jsii_name="sseKms")
    def sse_kms(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference", jsii.get(self, "sseKms"))

    @builtins.property
    @jsii.member(jsii_name="sseS3")
    def sse_s3(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List", jsii.get(self, "sseS3"))

    @builtins.property
    @jsii.member(jsii_name="sseKmsInput")
    def sse_kms_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms"], jsii.get(self, "sseKmsInput"))

    @builtins.property
    @jsii.member(jsii_name="sseS3Input")
    def sse_s3_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3"]]], jsii.get(self, "sseS3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms",
    jsii_struct_bases=[],
    name_mapping={"key_id": "keyId"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms:
    def __init__(self, *, key_id: builtins.str) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#key_id S3ControlStorageLensConfiguration#key_id}.
        '''
        if __debug__:
            def stub(*, key_id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_id": key_id,
        }

    @builtins.property
    def key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#key_id S3ControlStorageLensConfiguration#key_id}.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference",
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
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3",
    jsii_struct_bases=[],
    name_mapping={},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List",
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
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference",
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

    @jsii.member(jsii_name="putEncryption")
    def put_encryption(
        self,
        *,
        sse_kms: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms, typing.Dict[str, typing.Any]]] = None,
        sse_s3: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param sse_kms: sse_kms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_kms S3ControlStorageLensConfiguration#sse_kms}
        :param sse_s3: sse_s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_s3 S3ControlStorageLensConfiguration#sse_s3}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption(
            sse_kms=sse_kms, sse_s3=sse_s3
        )

        return typing.cast(None, jsii.invoke(self, "putEncryption", [value]))

    @jsii.member(jsii_name="resetEncryption")
    def reset_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryption", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference, jsii.get(self, "encryption"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="outputSchemaVersionInput")
    def output_schema_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputSchemaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

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
    @jsii.member(jsii_name="outputSchemaVersion")
    def output_schema_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputSchemaVersion"))

    @output_schema_version.setter
    def output_schema_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputSchemaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationExclude",
    jsii_struct_bases=[],
    name_mapping={"buckets": "buckets", "regions": "regions"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationExclude:
    def __init__(
        self,
        *,
        buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.
        :param regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.
        '''
        if __debug__:
            def stub(
                *,
                buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
                regions: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument buckets", value=buckets, expected_type=type_hints["buckets"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if buckets is not None:
            self._values["buckets"] = buckets
        if regions is not None:
            self._values["regions"] = regions

    @builtins.property
    def buckets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.'''
        result = self._values.get("buckets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.'''
        result = self._values.get("regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationExclude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference",
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

    @jsii.member(jsii_name="resetBuckets")
    def reset_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuckets", []))

    @jsii.member(jsii_name="resetRegions")
    def reset_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegions", []))

    @builtins.property
    @jsii.member(jsii_name="bucketsInput")
    def buckets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionsInput")
    def regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "regionsInput"))

    @builtins.property
    @jsii.member(jsii_name="buckets")
    def buckets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "buckets"))

    @buckets.setter
    def buckets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buckets", value)

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationInclude",
    jsii_struct_bases=[],
    name_mapping={"buckets": "buckets", "regions": "regions"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationInclude:
    def __init__(
        self,
        *,
        buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.
        :param regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.
        '''
        if __debug__:
            def stub(
                *,
                buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
                regions: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument buckets", value=buckets, expected_type=type_hints["buckets"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if buckets is not None:
            self._values["buckets"] = buckets
        if regions is not None:
            self._values["regions"] = regions

    @builtins.property
    def buckets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.'''
        result = self._values.get("buckets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.'''
        result = self._values.get("regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationInclude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference",
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

    @jsii.member(jsii_name="resetBuckets")
    def reset_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuckets", []))

    @jsii.member(jsii_name="resetRegions")
    def reset_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegions", []))

    @builtins.property
    @jsii.member(jsii_name="bucketsInput")
    def buckets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionsInput")
    def regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "regionsInput"))

    @builtins.property
    @jsii.member(jsii_name="buckets")
    def buckets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "buckets"))

    @buckets.setter
    def buckets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buckets", value)

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference",
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

    @jsii.member(jsii_name="putAccountLevel")
    def put_account_level(
        self,
        *,
        bucket_level: typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel, typing.Dict[str, typing.Any]],
        activity_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_level: bucket_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#bucket_level S3ControlStorageLensConfiguration#bucket_level}
        :param activity_metrics: activity_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel(
            bucket_level=bucket_level, activity_metrics=activity_metrics
        )

        return typing.cast(None, jsii.invoke(self, "putAccountLevel", [value]))

    @jsii.member(jsii_name="putAwsOrg")
    def put_aws_org(self, *, arn: builtins.str) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg(
            arn=arn
        )

        return typing.cast(None, jsii.invoke(self, "putAwsOrg", [value]))

    @jsii.member(jsii_name="putDataExport")
    def put_data_export(
        self,
        *,
        cloud_watch_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics, typing.Dict[str, typing.Any]]] = None,
        s3_bucket_destination: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloud_watch_metrics: cloud_watch_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#cloud_watch_metrics S3ControlStorageLensConfiguration#cloud_watch_metrics}
        :param s3_bucket_destination: s3_bucket_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#s3_bucket_destination S3ControlStorageLensConfiguration#s3_bucket_destination}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExport(
            cloud_watch_metrics=cloud_watch_metrics,
            s3_bucket_destination=s3_bucket_destination,
        )

        return typing.cast(None, jsii.invoke(self, "putDataExport", [value]))

    @jsii.member(jsii_name="putExclude")
    def put_exclude(
        self,
        *,
        buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.
        :param regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationExclude(
            buckets=buckets, regions=regions
        )

        return typing.cast(None, jsii.invoke(self, "putExclude", [value]))

    @jsii.member(jsii_name="putInclude")
    def put_include(
        self,
        *,
        buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.
        :param regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationInclude(
            buckets=buckets, regions=regions
        )

        return typing.cast(None, jsii.invoke(self, "putInclude", [value]))

    @jsii.member(jsii_name="resetAwsOrg")
    def reset_aws_org(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsOrg", []))

    @jsii.member(jsii_name="resetDataExport")
    def reset_data_export(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataExport", []))

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="accountLevel")
    def account_level(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference, jsii.get(self, "accountLevel"))

    @builtins.property
    @jsii.member(jsii_name="awsOrg")
    def aws_org(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference, jsii.get(self, "awsOrg"))

    @builtins.property
    @jsii.member(jsii_name="dataExport")
    def data_export(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference, jsii.get(self, "dataExport"))

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference, jsii.get(self, "exclude"))

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference, jsii.get(self, "include"))

    @builtins.property
    @jsii.member(jsii_name="accountLevelInput")
    def account_level_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel], jsii.get(self, "accountLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="awsOrgInput")
    def aws_org_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg], jsii.get(self, "awsOrgInput"))

    @builtins.property
    @jsii.member(jsii_name="dataExportInput")
    def data_export_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport], jsii.get(self, "dataExportInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude], jsii.get(self, "includeInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfiguration]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3ControlStorageLensConfiguration",
    "S3ControlStorageLensConfigurationConfig",
    "S3ControlStorageLensConfigurationStorageLensConfiguration",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExport",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationExclude",
    "S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationInclude",
    "S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference",
]

publication.publish()
