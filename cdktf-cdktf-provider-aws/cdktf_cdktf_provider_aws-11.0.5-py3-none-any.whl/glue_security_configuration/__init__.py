'''
# `aws_glue_security_configuration`

Refer to the Terraform Registory for docs: [`aws_glue_security_configuration`](https://www.terraform.io/docs/providers/aws/r/glue_security_configuration).
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


class GlueSecurityConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration aws_glue_security_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        encryption_configuration: typing.Union["GlueSecurityConfigurationEncryptionConfiguration", typing.Dict[str, typing.Any]],
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration aws_glue_security_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#encryption_configuration GlueSecurityConfiguration#encryption_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#name GlueSecurityConfiguration#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#id GlueSecurityConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                encryption_configuration: typing.Union[GlueSecurityConfigurationEncryptionConfiguration, typing.Dict[str, typing.Any]],
                name: builtins.str,
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
        config = GlueSecurityConfigurationConfig(
            encryption_configuration=encryption_configuration,
            name=name,
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

    @jsii.member(jsii_name="putEncryptionConfiguration")
    def put_encryption_configuration(
        self,
        *,
        cloudwatch_encryption: typing.Union["GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption", typing.Dict[str, typing.Any]],
        job_bookmarks_encryption: typing.Union["GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption", typing.Dict[str, typing.Any]],
        s3_encryption: typing.Union["GlueSecurityConfigurationEncryptionConfigurationS3Encryption", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param cloudwatch_encryption: cloudwatch_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#cloudwatch_encryption GlueSecurityConfiguration#cloudwatch_encryption}
        :param job_bookmarks_encryption: job_bookmarks_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#job_bookmarks_encryption GlueSecurityConfiguration#job_bookmarks_encryption}
        :param s3_encryption: s3_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#s3_encryption GlueSecurityConfiguration#s3_encryption}
        '''
        value = GlueSecurityConfigurationEncryptionConfiguration(
            cloudwatch_encryption=cloudwatch_encryption,
            job_bookmarks_encryption=job_bookmarks_encryption,
            s3_encryption=s3_encryption,
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfiguration", [value]))

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
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> "GlueSecurityConfigurationEncryptionConfigurationOutputReference":
        return typing.cast("GlueSecurityConfigurationEncryptionConfigurationOutputReference", jsii.get(self, "encryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigurationInput")
    def encryption_configuration_input(
        self,
    ) -> typing.Optional["GlueSecurityConfigurationEncryptionConfiguration"]:
        return typing.cast(typing.Optional["GlueSecurityConfigurationEncryptionConfiguration"], jsii.get(self, "encryptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "encryption_configuration": "encryptionConfiguration",
        "name": "name",
        "id": "id",
    },
)
class GlueSecurityConfigurationConfig(cdktf.TerraformMetaArguments):
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
        encryption_configuration: typing.Union["GlueSecurityConfigurationEncryptionConfiguration", typing.Dict[str, typing.Any]],
        name: builtins.str,
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
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#encryption_configuration GlueSecurityConfiguration#encryption_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#name GlueSecurityConfiguration#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#id GlueSecurityConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(encryption_configuration, dict):
            encryption_configuration = GlueSecurityConfigurationEncryptionConfiguration(**encryption_configuration)
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
                encryption_configuration: typing.Union[GlueSecurityConfigurationEncryptionConfiguration, typing.Dict[str, typing.Any]],
                name: builtins.str,
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
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "encryption_configuration": encryption_configuration,
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
    def encryption_configuration(
        self,
    ) -> "GlueSecurityConfigurationEncryptionConfiguration":
        '''encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#encryption_configuration GlueSecurityConfiguration#encryption_configuration}
        '''
        result = self._values.get("encryption_configuration")
        assert result is not None, "Required property 'encryption_configuration' is missing"
        return typing.cast("GlueSecurityConfigurationEncryptionConfiguration", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#name GlueSecurityConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#id GlueSecurityConfiguration#id}.

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
        return "GlueSecurityConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfigurationEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_encryption": "cloudwatchEncryption",
        "job_bookmarks_encryption": "jobBookmarksEncryption",
        "s3_encryption": "s3Encryption",
    },
)
class GlueSecurityConfigurationEncryptionConfiguration:
    def __init__(
        self,
        *,
        cloudwatch_encryption: typing.Union["GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption", typing.Dict[str, typing.Any]],
        job_bookmarks_encryption: typing.Union["GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption", typing.Dict[str, typing.Any]],
        s3_encryption: typing.Union["GlueSecurityConfigurationEncryptionConfigurationS3Encryption", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param cloudwatch_encryption: cloudwatch_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#cloudwatch_encryption GlueSecurityConfiguration#cloudwatch_encryption}
        :param job_bookmarks_encryption: job_bookmarks_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#job_bookmarks_encryption GlueSecurityConfiguration#job_bookmarks_encryption}
        :param s3_encryption: s3_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#s3_encryption GlueSecurityConfiguration#s3_encryption}
        '''
        if isinstance(cloudwatch_encryption, dict):
            cloudwatch_encryption = GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption(**cloudwatch_encryption)
        if isinstance(job_bookmarks_encryption, dict):
            job_bookmarks_encryption = GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption(**job_bookmarks_encryption)
        if isinstance(s3_encryption, dict):
            s3_encryption = GlueSecurityConfigurationEncryptionConfigurationS3Encryption(**s3_encryption)
        if __debug__:
            def stub(
                *,
                cloudwatch_encryption: typing.Union[GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption, typing.Dict[str, typing.Any]],
                job_bookmarks_encryption: typing.Union[GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption, typing.Dict[str, typing.Any]],
                s3_encryption: typing.Union[GlueSecurityConfigurationEncryptionConfigurationS3Encryption, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cloudwatch_encryption", value=cloudwatch_encryption, expected_type=type_hints["cloudwatch_encryption"])
            check_type(argname="argument job_bookmarks_encryption", value=job_bookmarks_encryption, expected_type=type_hints["job_bookmarks_encryption"])
            check_type(argname="argument s3_encryption", value=s3_encryption, expected_type=type_hints["s3_encryption"])
        self._values: typing.Dict[str, typing.Any] = {
            "cloudwatch_encryption": cloudwatch_encryption,
            "job_bookmarks_encryption": job_bookmarks_encryption,
            "s3_encryption": s3_encryption,
        }

    @builtins.property
    def cloudwatch_encryption(
        self,
    ) -> "GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption":
        '''cloudwatch_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#cloudwatch_encryption GlueSecurityConfiguration#cloudwatch_encryption}
        '''
        result = self._values.get("cloudwatch_encryption")
        assert result is not None, "Required property 'cloudwatch_encryption' is missing"
        return typing.cast("GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption", result)

    @builtins.property
    def job_bookmarks_encryption(
        self,
    ) -> "GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption":
        '''job_bookmarks_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#job_bookmarks_encryption GlueSecurityConfiguration#job_bookmarks_encryption}
        '''
        result = self._values.get("job_bookmarks_encryption")
        assert result is not None, "Required property 'job_bookmarks_encryption' is missing"
        return typing.cast("GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption", result)

    @builtins.property
    def s3_encryption(
        self,
    ) -> "GlueSecurityConfigurationEncryptionConfigurationS3Encryption":
        '''s3_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#s3_encryption GlueSecurityConfiguration#s3_encryption}
        '''
        result = self._values.get("s3_encryption")
        assert result is not None, "Required property 's3_encryption' is missing"
        return typing.cast("GlueSecurityConfigurationEncryptionConfigurationS3Encryption", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueSecurityConfigurationEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_encryption_mode": "cloudwatchEncryptionMode",
        "kms_key_arn": "kmsKeyArn",
    },
)
class GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption:
    def __init__(
        self,
        *,
        cloudwatch_encryption_mode: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloudwatch_encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#cloudwatch_encryption_mode GlueSecurityConfiguration#cloudwatch_encryption_mode}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#kms_key_arn GlueSecurityConfiguration#kms_key_arn}.
        '''
        if __debug__:
            def stub(
                *,
                cloudwatch_encryption_mode: typing.Optional[builtins.str] = None,
                kms_key_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cloudwatch_encryption_mode", value=cloudwatch_encryption_mode, expected_type=type_hints["cloudwatch_encryption_mode"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudwatch_encryption_mode is not None:
            self._values["cloudwatch_encryption_mode"] = cloudwatch_encryption_mode
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn

    @builtins.property
    def cloudwatch_encryption_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#cloudwatch_encryption_mode GlueSecurityConfiguration#cloudwatch_encryption_mode}.'''
        result = self._values.get("cloudwatch_encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#kms_key_arn GlueSecurityConfiguration#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryptionOutputReference",
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

    @jsii.member(jsii_name="resetCloudwatchEncryptionMode")
    def reset_cloudwatch_encryption_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchEncryptionMode", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchEncryptionModeInput")
    def cloudwatch_encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchEncryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchEncryptionMode")
    def cloudwatch_encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchEncryptionMode"))

    @cloudwatch_encryption_mode.setter
    def cloudwatch_encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchEncryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption]:
        return typing.cast(typing.Optional[GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption",
    jsii_struct_bases=[],
    name_mapping={
        "job_bookmarks_encryption_mode": "jobBookmarksEncryptionMode",
        "kms_key_arn": "kmsKeyArn",
    },
)
class GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption:
    def __init__(
        self,
        *,
        job_bookmarks_encryption_mode: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param job_bookmarks_encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#job_bookmarks_encryption_mode GlueSecurityConfiguration#job_bookmarks_encryption_mode}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#kms_key_arn GlueSecurityConfiguration#kms_key_arn}.
        '''
        if __debug__:
            def stub(
                *,
                job_bookmarks_encryption_mode: typing.Optional[builtins.str] = None,
                kms_key_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument job_bookmarks_encryption_mode", value=job_bookmarks_encryption_mode, expected_type=type_hints["job_bookmarks_encryption_mode"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if job_bookmarks_encryption_mode is not None:
            self._values["job_bookmarks_encryption_mode"] = job_bookmarks_encryption_mode
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn

    @builtins.property
    def job_bookmarks_encryption_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#job_bookmarks_encryption_mode GlueSecurityConfiguration#job_bookmarks_encryption_mode}.'''
        result = self._values.get("job_bookmarks_encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#kms_key_arn GlueSecurityConfiguration#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionOutputReference",
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

    @jsii.member(jsii_name="resetJobBookmarksEncryptionMode")
    def reset_job_bookmarks_encryption_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobBookmarksEncryptionMode", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @builtins.property
    @jsii.member(jsii_name="jobBookmarksEncryptionModeInput")
    def job_bookmarks_encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobBookmarksEncryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="jobBookmarksEncryptionMode")
    def job_bookmarks_encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobBookmarksEncryptionMode"))

    @job_bookmarks_encryption_mode.setter
    def job_bookmarks_encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobBookmarksEncryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption]:
        return typing.cast(typing.Optional[GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueSecurityConfigurationEncryptionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfigurationEncryptionConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchEncryption")
    def put_cloudwatch_encryption(
        self,
        *,
        cloudwatch_encryption_mode: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloudwatch_encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#cloudwatch_encryption_mode GlueSecurityConfiguration#cloudwatch_encryption_mode}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#kms_key_arn GlueSecurityConfiguration#kms_key_arn}.
        '''
        value = GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption(
            cloudwatch_encryption_mode=cloudwatch_encryption_mode,
            kms_key_arn=kms_key_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchEncryption", [value]))

    @jsii.member(jsii_name="putJobBookmarksEncryption")
    def put_job_bookmarks_encryption(
        self,
        *,
        job_bookmarks_encryption_mode: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param job_bookmarks_encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#job_bookmarks_encryption_mode GlueSecurityConfiguration#job_bookmarks_encryption_mode}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#kms_key_arn GlueSecurityConfiguration#kms_key_arn}.
        '''
        value = GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption(
            job_bookmarks_encryption_mode=job_bookmarks_encryption_mode,
            kms_key_arn=kms_key_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putJobBookmarksEncryption", [value]))

    @jsii.member(jsii_name="putS3Encryption")
    def put_s3_encryption(
        self,
        *,
        kms_key_arn: typing.Optional[builtins.str] = None,
        s3_encryption_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#kms_key_arn GlueSecurityConfiguration#kms_key_arn}.
        :param s3_encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#s3_encryption_mode GlueSecurityConfiguration#s3_encryption_mode}.
        '''
        value = GlueSecurityConfigurationEncryptionConfigurationS3Encryption(
            kms_key_arn=kms_key_arn, s3_encryption_mode=s3_encryption_mode
        )

        return typing.cast(None, jsii.invoke(self, "putS3Encryption", [value]))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchEncryption")
    def cloudwatch_encryption(
        self,
    ) -> GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryptionOutputReference:
        return typing.cast(GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryptionOutputReference, jsii.get(self, "cloudwatchEncryption"))

    @builtins.property
    @jsii.member(jsii_name="jobBookmarksEncryption")
    def job_bookmarks_encryption(
        self,
    ) -> GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionOutputReference:
        return typing.cast(GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionOutputReference, jsii.get(self, "jobBookmarksEncryption"))

    @builtins.property
    @jsii.member(jsii_name="s3Encryption")
    def s3_encryption(
        self,
    ) -> "GlueSecurityConfigurationEncryptionConfigurationS3EncryptionOutputReference":
        return typing.cast("GlueSecurityConfigurationEncryptionConfigurationS3EncryptionOutputReference", jsii.get(self, "s3Encryption"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchEncryptionInput")
    def cloudwatch_encryption_input(
        self,
    ) -> typing.Optional[GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption]:
        return typing.cast(typing.Optional[GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption], jsii.get(self, "cloudwatchEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="jobBookmarksEncryptionInput")
    def job_bookmarks_encryption_input(
        self,
    ) -> typing.Optional[GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption]:
        return typing.cast(typing.Optional[GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption], jsii.get(self, "jobBookmarksEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="s3EncryptionInput")
    def s3_encryption_input(
        self,
    ) -> typing.Optional["GlueSecurityConfigurationEncryptionConfigurationS3Encryption"]:
        return typing.cast(typing.Optional["GlueSecurityConfigurationEncryptionConfigurationS3Encryption"], jsii.get(self, "s3EncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueSecurityConfigurationEncryptionConfiguration]:
        return typing.cast(typing.Optional[GlueSecurityConfigurationEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueSecurityConfigurationEncryptionConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GlueSecurityConfigurationEncryptionConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfigurationEncryptionConfigurationS3Encryption",
    jsii_struct_bases=[],
    name_mapping={
        "kms_key_arn": "kmsKeyArn",
        "s3_encryption_mode": "s3EncryptionMode",
    },
)
class GlueSecurityConfigurationEncryptionConfigurationS3Encryption:
    def __init__(
        self,
        *,
        kms_key_arn: typing.Optional[builtins.str] = None,
        s3_encryption_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#kms_key_arn GlueSecurityConfiguration#kms_key_arn}.
        :param s3_encryption_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#s3_encryption_mode GlueSecurityConfiguration#s3_encryption_mode}.
        '''
        if __debug__:
            def stub(
                *,
                kms_key_arn: typing.Optional[builtins.str] = None,
                s3_encryption_mode: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument s3_encryption_mode", value=s3_encryption_mode, expected_type=type_hints["s3_encryption_mode"])
        self._values: typing.Dict[str, typing.Any] = {}
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if s3_encryption_mode is not None:
            self._values["s3_encryption_mode"] = s3_encryption_mode

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#kms_key_arn GlueSecurityConfiguration#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_encryption_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_security_configuration#s3_encryption_mode GlueSecurityConfiguration#s3_encryption_mode}.'''
        result = self._values.get("s3_encryption_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueSecurityConfigurationEncryptionConfigurationS3Encryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueSecurityConfigurationEncryptionConfigurationS3EncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueSecurityConfiguration.GlueSecurityConfigurationEncryptionConfigurationS3EncryptionOutputReference",
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

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetS3EncryptionMode")
    def reset_s3_encryption_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3EncryptionMode", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3EncryptionModeInput")
    def s3_encryption_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3EncryptionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3EncryptionMode")
    def s3_encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3EncryptionMode"))

    @s3_encryption_mode.setter
    def s3_encryption_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3EncryptionMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueSecurityConfigurationEncryptionConfigurationS3Encryption]:
        return typing.cast(typing.Optional[GlueSecurityConfigurationEncryptionConfigurationS3Encryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueSecurityConfigurationEncryptionConfigurationS3Encryption],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GlueSecurityConfigurationEncryptionConfigurationS3Encryption],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GlueSecurityConfiguration",
    "GlueSecurityConfigurationConfig",
    "GlueSecurityConfigurationEncryptionConfiguration",
    "GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryption",
    "GlueSecurityConfigurationEncryptionConfigurationCloudwatchEncryptionOutputReference",
    "GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryption",
    "GlueSecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionOutputReference",
    "GlueSecurityConfigurationEncryptionConfigurationOutputReference",
    "GlueSecurityConfigurationEncryptionConfigurationS3Encryption",
    "GlueSecurityConfigurationEncryptionConfigurationS3EncryptionOutputReference",
]

publication.publish()
