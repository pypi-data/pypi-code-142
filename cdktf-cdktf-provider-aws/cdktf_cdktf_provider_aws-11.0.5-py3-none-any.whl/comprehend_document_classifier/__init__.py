'''
# `aws_comprehend_document_classifier`

Refer to the Terraform Registory for docs: [`aws_comprehend_document_classifier`](https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier).
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


class ComprehendDocumentClassifier(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifier",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier aws_comprehend_document_classifier}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_access_role_arn: builtins.str,
        input_data_config: typing.Union["ComprehendDocumentClassifierInputDataConfig", typing.Dict[str, typing.Any]],
        language_code: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        model_kms_key_id: typing.Optional[builtins.str] = None,
        output_data_config: typing.Optional[typing.Union["ComprehendDocumentClassifierOutputDataConfig", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComprehendDocumentClassifierTimeouts", typing.Dict[str, typing.Any]]] = None,
        version_name: typing.Optional[builtins.str] = None,
        version_name_prefix: typing.Optional[builtins.str] = None,
        volume_kms_key_id: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["ComprehendDocumentClassifierVpcConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier aws_comprehend_document_classifier} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#data_access_role_arn ComprehendDocumentClassifier#data_access_role_arn}.
        :param input_data_config: input_data_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#input_data_config ComprehendDocumentClassifier#input_data_config}
        :param language_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#language_code ComprehendDocumentClassifier#language_code}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#name ComprehendDocumentClassifier#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#id ComprehendDocumentClassifier#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#mode ComprehendDocumentClassifier#mode}.
        :param model_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#model_kms_key_id ComprehendDocumentClassifier#model_kms_key_id}.
        :param output_data_config: output_data_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#output_data_config ComprehendDocumentClassifier#output_data_config}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#tags ComprehendDocumentClassifier#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#tags_all ComprehendDocumentClassifier#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#timeouts ComprehendDocumentClassifier#timeouts}
        :param version_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#version_name ComprehendDocumentClassifier#version_name}.
        :param version_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#version_name_prefix ComprehendDocumentClassifier#version_name_prefix}.
        :param volume_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#volume_kms_key_id ComprehendDocumentClassifier#volume_kms_key_id}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#vpc_config ComprehendDocumentClassifier#vpc_config}
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
                data_access_role_arn: builtins.str,
                input_data_config: typing.Union[ComprehendDocumentClassifierInputDataConfig, typing.Dict[str, typing.Any]],
                language_code: builtins.str,
                name: builtins.str,
                id: typing.Optional[builtins.str] = None,
                mode: typing.Optional[builtins.str] = None,
                model_kms_key_id: typing.Optional[builtins.str] = None,
                output_data_config: typing.Optional[typing.Union[ComprehendDocumentClassifierOutputDataConfig, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[ComprehendDocumentClassifierTimeouts, typing.Dict[str, typing.Any]]] = None,
                version_name: typing.Optional[builtins.str] = None,
                version_name_prefix: typing.Optional[builtins.str] = None,
                volume_kms_key_id: typing.Optional[builtins.str] = None,
                vpc_config: typing.Optional[typing.Union[ComprehendDocumentClassifierVpcConfig, typing.Dict[str, typing.Any]]] = None,
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
        config = ComprehendDocumentClassifierConfig(
            data_access_role_arn=data_access_role_arn,
            input_data_config=input_data_config,
            language_code=language_code,
            name=name,
            id=id,
            mode=mode,
            model_kms_key_id=model_kms_key_id,
            output_data_config=output_data_config,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            version_name=version_name,
            version_name_prefix=version_name_prefix,
            volume_kms_key_id=volume_kms_key_id,
            vpc_config=vpc_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInputDataConfig")
    def put_input_data_config(
        self,
        *,
        augmented_manifests: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComprehendDocumentClassifierInputDataConfigAugmentedManifests", typing.Dict[str, typing.Any]]]]] = None,
        data_format: typing.Optional[builtins.str] = None,
        label_delimiter: typing.Optional[builtins.str] = None,
        s3_uri: typing.Optional[builtins.str] = None,
        test_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param augmented_manifests: augmented_manifests block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#augmented_manifests ComprehendDocumentClassifier#augmented_manifests}
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#data_format ComprehendDocumentClassifier#data_format}.
        :param label_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#label_delimiter ComprehendDocumentClassifier#label_delimiter}.
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#s3_uri ComprehendDocumentClassifier#s3_uri}.
        :param test_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#test_s3_uri ComprehendDocumentClassifier#test_s3_uri}.
        '''
        value = ComprehendDocumentClassifierInputDataConfig(
            augmented_manifests=augmented_manifests,
            data_format=data_format,
            label_delimiter=label_delimiter,
            s3_uri=s3_uri,
            test_s3_uri=test_s3_uri,
        )

        return typing.cast(None, jsii.invoke(self, "putInputDataConfig", [value]))

    @jsii.member(jsii_name="putOutputDataConfig")
    def put_output_data_config(
        self,
        *,
        s3_uri: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#s3_uri ComprehendDocumentClassifier#s3_uri}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#kms_key_id ComprehendDocumentClassifier#kms_key_id}.
        '''
        value = ComprehendDocumentClassifierOutputDataConfig(
            s3_uri=s3_uri, kms_key_id=kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putOutputDataConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#create ComprehendDocumentClassifier#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#delete ComprehendDocumentClassifier#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#update ComprehendDocumentClassifier#update}.
        '''
        value = ComprehendDocumentClassifierTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpcConfig")
    def put_vpc_config(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#security_group_ids ComprehendDocumentClassifier#security_group_ids}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#subnets ComprehendDocumentClassifier#subnets}.
        '''
        value = ComprehendDocumentClassifierVpcConfig(
            security_group_ids=security_group_ids, subnets=subnets
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfig", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetModelKmsKeyId")
    def reset_model_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModelKmsKeyId", []))

    @jsii.member(jsii_name="resetOutputDataConfig")
    def reset_output_data_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputDataConfig", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVersionName")
    def reset_version_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionName", []))

    @jsii.member(jsii_name="resetVersionNamePrefix")
    def reset_version_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionNamePrefix", []))

    @jsii.member(jsii_name="resetVolumeKmsKeyId")
    def reset_volume_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeKmsKeyId", []))

    @jsii.member(jsii_name="resetVpcConfig")
    def reset_vpc_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfig", []))

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
    @jsii.member(jsii_name="inputDataConfig")
    def input_data_config(
        self,
    ) -> "ComprehendDocumentClassifierInputDataConfigOutputReference":
        return typing.cast("ComprehendDocumentClassifierInputDataConfigOutputReference", jsii.get(self, "inputDataConfig"))

    @builtins.property
    @jsii.member(jsii_name="outputDataConfig")
    def output_data_config(
        self,
    ) -> "ComprehendDocumentClassifierOutputDataConfigOutputReference":
        return typing.cast("ComprehendDocumentClassifierOutputDataConfigOutputReference", jsii.get(self, "outputDataConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComprehendDocumentClassifierTimeoutsOutputReference":
        return typing.cast("ComprehendDocumentClassifierTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(self) -> "ComprehendDocumentClassifierVpcConfigOutputReference":
        return typing.cast("ComprehendDocumentClassifierVpcConfigOutputReference", jsii.get(self, "vpcConfig"))

    @builtins.property
    @jsii.member(jsii_name="dataAccessRoleArnInput")
    def data_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputDataConfigInput")
    def input_data_config_input(
        self,
    ) -> typing.Optional["ComprehendDocumentClassifierInputDataConfig"]:
        return typing.cast(typing.Optional["ComprehendDocumentClassifierInputDataConfig"], jsii.get(self, "inputDataConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="languageCodeInput")
    def language_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="modelKmsKeyIdInput")
    def model_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="outputDataConfigInput")
    def output_data_config_input(
        self,
    ) -> typing.Optional["ComprehendDocumentClassifierOutputDataConfig"]:
        return typing.cast(typing.Optional["ComprehendDocumentClassifierOutputDataConfig"], jsii.get(self, "outputDataConfigInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComprehendDocumentClassifierTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComprehendDocumentClassifierTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionNameInput")
    def version_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionNamePrefixInput")
    def version_name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNamePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeKmsKeyIdInput")
    def volume_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfigInput")
    def vpc_config_input(
        self,
    ) -> typing.Optional["ComprehendDocumentClassifierVpcConfig"]:
        return typing.cast(typing.Optional["ComprehendDocumentClassifierVpcConfig"], jsii.get(self, "vpcConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="dataAccessRoleArn")
    def data_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataAccessRoleArn"))

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataAccessRoleArn", value)

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
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="modelKmsKeyId")
    def model_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelKmsKeyId"))

    @model_kms_key_id.setter
    def model_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelKmsKeyId", value)

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

    @builtins.property
    @jsii.member(jsii_name="versionName")
    def version_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionName"))

    @version_name.setter
    def version_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionName", value)

    @builtins.property
    @jsii.member(jsii_name="versionNamePrefix")
    def version_name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionNamePrefix"))

    @version_name_prefix.setter
    def version_name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionNamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeKmsKeyId"))

    @volume_kms_key_id.setter
    def volume_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeKmsKeyId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_access_role_arn": "dataAccessRoleArn",
        "input_data_config": "inputDataConfig",
        "language_code": "languageCode",
        "name": "name",
        "id": "id",
        "mode": "mode",
        "model_kms_key_id": "modelKmsKeyId",
        "output_data_config": "outputDataConfig",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "version_name": "versionName",
        "version_name_prefix": "versionNamePrefix",
        "volume_kms_key_id": "volumeKmsKeyId",
        "vpc_config": "vpcConfig",
    },
)
class ComprehendDocumentClassifierConfig(cdktf.TerraformMetaArguments):
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
        data_access_role_arn: builtins.str,
        input_data_config: typing.Union["ComprehendDocumentClassifierInputDataConfig", typing.Dict[str, typing.Any]],
        language_code: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        model_kms_key_id: typing.Optional[builtins.str] = None,
        output_data_config: typing.Optional[typing.Union["ComprehendDocumentClassifierOutputDataConfig", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComprehendDocumentClassifierTimeouts", typing.Dict[str, typing.Any]]] = None,
        version_name: typing.Optional[builtins.str] = None,
        version_name_prefix: typing.Optional[builtins.str] = None,
        volume_kms_key_id: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["ComprehendDocumentClassifierVpcConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#data_access_role_arn ComprehendDocumentClassifier#data_access_role_arn}.
        :param input_data_config: input_data_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#input_data_config ComprehendDocumentClassifier#input_data_config}
        :param language_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#language_code ComprehendDocumentClassifier#language_code}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#name ComprehendDocumentClassifier#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#id ComprehendDocumentClassifier#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#mode ComprehendDocumentClassifier#mode}.
        :param model_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#model_kms_key_id ComprehendDocumentClassifier#model_kms_key_id}.
        :param output_data_config: output_data_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#output_data_config ComprehendDocumentClassifier#output_data_config}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#tags ComprehendDocumentClassifier#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#tags_all ComprehendDocumentClassifier#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#timeouts ComprehendDocumentClassifier#timeouts}
        :param version_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#version_name ComprehendDocumentClassifier#version_name}.
        :param version_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#version_name_prefix ComprehendDocumentClassifier#version_name_prefix}.
        :param volume_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#volume_kms_key_id ComprehendDocumentClassifier#volume_kms_key_id}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#vpc_config ComprehendDocumentClassifier#vpc_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(input_data_config, dict):
            input_data_config = ComprehendDocumentClassifierInputDataConfig(**input_data_config)
        if isinstance(output_data_config, dict):
            output_data_config = ComprehendDocumentClassifierOutputDataConfig(**output_data_config)
        if isinstance(timeouts, dict):
            timeouts = ComprehendDocumentClassifierTimeouts(**timeouts)
        if isinstance(vpc_config, dict):
            vpc_config = ComprehendDocumentClassifierVpcConfig(**vpc_config)
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
                data_access_role_arn: builtins.str,
                input_data_config: typing.Union[ComprehendDocumentClassifierInputDataConfig, typing.Dict[str, typing.Any]],
                language_code: builtins.str,
                name: builtins.str,
                id: typing.Optional[builtins.str] = None,
                mode: typing.Optional[builtins.str] = None,
                model_kms_key_id: typing.Optional[builtins.str] = None,
                output_data_config: typing.Optional[typing.Union[ComprehendDocumentClassifierOutputDataConfig, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[ComprehendDocumentClassifierTimeouts, typing.Dict[str, typing.Any]]] = None,
                version_name: typing.Optional[builtins.str] = None,
                version_name_prefix: typing.Optional[builtins.str] = None,
                volume_kms_key_id: typing.Optional[builtins.str] = None,
                vpc_config: typing.Optional[typing.Union[ComprehendDocumentClassifierVpcConfig, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument data_access_role_arn", value=data_access_role_arn, expected_type=type_hints["data_access_role_arn"])
            check_type(argname="argument input_data_config", value=input_data_config, expected_type=type_hints["input_data_config"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument model_kms_key_id", value=model_kms_key_id, expected_type=type_hints["model_kms_key_id"])
            check_type(argname="argument output_data_config", value=output_data_config, expected_type=type_hints["output_data_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument version_name", value=version_name, expected_type=type_hints["version_name"])
            check_type(argname="argument version_name_prefix", value=version_name_prefix, expected_type=type_hints["version_name_prefix"])
            check_type(argname="argument volume_kms_key_id", value=volume_kms_key_id, expected_type=type_hints["volume_kms_key_id"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_access_role_arn": data_access_role_arn,
            "input_data_config": input_data_config,
            "language_code": language_code,
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
        if mode is not None:
            self._values["mode"] = mode
        if model_kms_key_id is not None:
            self._values["model_kms_key_id"] = model_kms_key_id
        if output_data_config is not None:
            self._values["output_data_config"] = output_data_config
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if version_name is not None:
            self._values["version_name"] = version_name
        if version_name_prefix is not None:
            self._values["version_name_prefix"] = version_name_prefix
        if volume_kms_key_id is not None:
            self._values["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

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
    def data_access_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#data_access_role_arn ComprehendDocumentClassifier#data_access_role_arn}.'''
        result = self._values.get("data_access_role_arn")
        assert result is not None, "Required property 'data_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_data_config(self) -> "ComprehendDocumentClassifierInputDataConfig":
        '''input_data_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#input_data_config ComprehendDocumentClassifier#input_data_config}
        '''
        result = self._values.get("input_data_config")
        assert result is not None, "Required property 'input_data_config' is missing"
        return typing.cast("ComprehendDocumentClassifierInputDataConfig", result)

    @builtins.property
    def language_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#language_code ComprehendDocumentClassifier#language_code}.'''
        result = self._values.get("language_code")
        assert result is not None, "Required property 'language_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#name ComprehendDocumentClassifier#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#id ComprehendDocumentClassifier#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#mode ComprehendDocumentClassifier#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#model_kms_key_id ComprehendDocumentClassifier#model_kms_key_id}.'''
        result = self._values.get("model_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_data_config(
        self,
    ) -> typing.Optional["ComprehendDocumentClassifierOutputDataConfig"]:
        '''output_data_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#output_data_config ComprehendDocumentClassifier#output_data_config}
        '''
        result = self._values.get("output_data_config")
        return typing.cast(typing.Optional["ComprehendDocumentClassifierOutputDataConfig"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#tags ComprehendDocumentClassifier#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#tags_all ComprehendDocumentClassifier#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComprehendDocumentClassifierTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#timeouts ComprehendDocumentClassifier#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComprehendDocumentClassifierTimeouts"], result)

    @builtins.property
    def version_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#version_name ComprehendDocumentClassifier#version_name}.'''
        result = self._values.get("version_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#version_name_prefix ComprehendDocumentClassifier#version_name_prefix}.'''
        result = self._values.get("version_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#volume_kms_key_id ComprehendDocumentClassifier#volume_kms_key_id}.'''
        result = self._values.get("volume_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_config(self) -> typing.Optional["ComprehendDocumentClassifierVpcConfig"]:
        '''vpc_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#vpc_config ComprehendDocumentClassifier#vpc_config}
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional["ComprehendDocumentClassifierVpcConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendDocumentClassifierConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierInputDataConfig",
    jsii_struct_bases=[],
    name_mapping={
        "augmented_manifests": "augmentedManifests",
        "data_format": "dataFormat",
        "label_delimiter": "labelDelimiter",
        "s3_uri": "s3Uri",
        "test_s3_uri": "testS3Uri",
    },
)
class ComprehendDocumentClassifierInputDataConfig:
    def __init__(
        self,
        *,
        augmented_manifests: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComprehendDocumentClassifierInputDataConfigAugmentedManifests", typing.Dict[str, typing.Any]]]]] = None,
        data_format: typing.Optional[builtins.str] = None,
        label_delimiter: typing.Optional[builtins.str] = None,
        s3_uri: typing.Optional[builtins.str] = None,
        test_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param augmented_manifests: augmented_manifests block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#augmented_manifests ComprehendDocumentClassifier#augmented_manifests}
        :param data_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#data_format ComprehendDocumentClassifier#data_format}.
        :param label_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#label_delimiter ComprehendDocumentClassifier#label_delimiter}.
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#s3_uri ComprehendDocumentClassifier#s3_uri}.
        :param test_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#test_s3_uri ComprehendDocumentClassifier#test_s3_uri}.
        '''
        if __debug__:
            def stub(
                *,
                augmented_manifests: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComprehendDocumentClassifierInputDataConfigAugmentedManifests, typing.Dict[str, typing.Any]]]]] = None,
                data_format: typing.Optional[builtins.str] = None,
                label_delimiter: typing.Optional[builtins.str] = None,
                s3_uri: typing.Optional[builtins.str] = None,
                test_s3_uri: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument augmented_manifests", value=augmented_manifests, expected_type=type_hints["augmented_manifests"])
            check_type(argname="argument data_format", value=data_format, expected_type=type_hints["data_format"])
            check_type(argname="argument label_delimiter", value=label_delimiter, expected_type=type_hints["label_delimiter"])
            check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
            check_type(argname="argument test_s3_uri", value=test_s3_uri, expected_type=type_hints["test_s3_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if augmented_manifests is not None:
            self._values["augmented_manifests"] = augmented_manifests
        if data_format is not None:
            self._values["data_format"] = data_format
        if label_delimiter is not None:
            self._values["label_delimiter"] = label_delimiter
        if s3_uri is not None:
            self._values["s3_uri"] = s3_uri
        if test_s3_uri is not None:
            self._values["test_s3_uri"] = test_s3_uri

    @builtins.property
    def augmented_manifests(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComprehendDocumentClassifierInputDataConfigAugmentedManifests"]]]:
        '''augmented_manifests block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#augmented_manifests ComprehendDocumentClassifier#augmented_manifests}
        '''
        result = self._values.get("augmented_manifests")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComprehendDocumentClassifierInputDataConfigAugmentedManifests"]]], result)

    @builtins.property
    def data_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#data_format ComprehendDocumentClassifier#data_format}.'''
        result = self._values.get("data_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label_delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#label_delimiter ComprehendDocumentClassifier#label_delimiter}.'''
        result = self._values.get("label_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#s3_uri ComprehendDocumentClassifier#s3_uri}.'''
        result = self._values.get("s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#test_s3_uri ComprehendDocumentClassifier#test_s3_uri}.'''
        result = self._values.get("test_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendDocumentClassifierInputDataConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierInputDataConfigAugmentedManifests",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_names": "attributeNames",
        "s3_uri": "s3Uri",
        "annotation_data_s3_uri": "annotationDataS3Uri",
        "document_type": "documentType",
        "source_documents_s3_uri": "sourceDocumentsS3Uri",
        "split": "split",
    },
)
class ComprehendDocumentClassifierInputDataConfigAugmentedManifests:
    def __init__(
        self,
        *,
        attribute_names: typing.Sequence[builtins.str],
        s3_uri: builtins.str,
        annotation_data_s3_uri: typing.Optional[builtins.str] = None,
        document_type: typing.Optional[builtins.str] = None,
        source_documents_s3_uri: typing.Optional[builtins.str] = None,
        split: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param attribute_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#attribute_names ComprehendDocumentClassifier#attribute_names}.
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#s3_uri ComprehendDocumentClassifier#s3_uri}.
        :param annotation_data_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#annotation_data_s3_uri ComprehendDocumentClassifier#annotation_data_s3_uri}.
        :param document_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#document_type ComprehendDocumentClassifier#document_type}.
        :param source_documents_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#source_documents_s3_uri ComprehendDocumentClassifier#source_documents_s3_uri}.
        :param split: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#split ComprehendDocumentClassifier#split}.
        '''
        if __debug__:
            def stub(
                *,
                attribute_names: typing.Sequence[builtins.str],
                s3_uri: builtins.str,
                annotation_data_s3_uri: typing.Optional[builtins.str] = None,
                document_type: typing.Optional[builtins.str] = None,
                source_documents_s3_uri: typing.Optional[builtins.str] = None,
                split: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument attribute_names", value=attribute_names, expected_type=type_hints["attribute_names"])
            check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
            check_type(argname="argument annotation_data_s3_uri", value=annotation_data_s3_uri, expected_type=type_hints["annotation_data_s3_uri"])
            check_type(argname="argument document_type", value=document_type, expected_type=type_hints["document_type"])
            check_type(argname="argument source_documents_s3_uri", value=source_documents_s3_uri, expected_type=type_hints["source_documents_s3_uri"])
            check_type(argname="argument split", value=split, expected_type=type_hints["split"])
        self._values: typing.Dict[str, typing.Any] = {
            "attribute_names": attribute_names,
            "s3_uri": s3_uri,
        }
        if annotation_data_s3_uri is not None:
            self._values["annotation_data_s3_uri"] = annotation_data_s3_uri
        if document_type is not None:
            self._values["document_type"] = document_type
        if source_documents_s3_uri is not None:
            self._values["source_documents_s3_uri"] = source_documents_s3_uri
        if split is not None:
            self._values["split"] = split

    @builtins.property
    def attribute_names(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#attribute_names ComprehendDocumentClassifier#attribute_names}.'''
        result = self._values.get("attribute_names")
        assert result is not None, "Required property 'attribute_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#s3_uri ComprehendDocumentClassifier#s3_uri}.'''
        result = self._values.get("s3_uri")
        assert result is not None, "Required property 's3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def annotation_data_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#annotation_data_s3_uri ComprehendDocumentClassifier#annotation_data_s3_uri}.'''
        result = self._values.get("annotation_data_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#document_type ComprehendDocumentClassifier#document_type}.'''
        result = self._values.get("document_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_documents_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#source_documents_s3_uri ComprehendDocumentClassifier#source_documents_s3_uri}.'''
        result = self._values.get("source_documents_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def split(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#split ComprehendDocumentClassifier#split}.'''
        result = self._values.get("split")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendDocumentClassifierInputDataConfigAugmentedManifests(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendDocumentClassifierInputDataConfigAugmentedManifestsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierInputDataConfigAugmentedManifestsList",
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
    ) -> "ComprehendDocumentClassifierInputDataConfigAugmentedManifestsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComprehendDocumentClassifierInputDataConfigAugmentedManifestsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComprehendDocumentClassifierInputDataConfigAugmentedManifests]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComprehendDocumentClassifierInputDataConfigAugmentedManifests]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComprehendDocumentClassifierInputDataConfigAugmentedManifests]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComprehendDocumentClassifierInputDataConfigAugmentedManifests]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComprehendDocumentClassifierInputDataConfigAugmentedManifestsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierInputDataConfigAugmentedManifestsOutputReference",
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

    @jsii.member(jsii_name="resetAnnotationDataS3Uri")
    def reset_annotation_data_s3_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotationDataS3Uri", []))

    @jsii.member(jsii_name="resetDocumentType")
    def reset_document_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentType", []))

    @jsii.member(jsii_name="resetSourceDocumentsS3Uri")
    def reset_source_documents_s3_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDocumentsS3Uri", []))

    @jsii.member(jsii_name="resetSplit")
    def reset_split(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplit", []))

    @builtins.property
    @jsii.member(jsii_name="annotationDataS3UriInput")
    def annotation_data_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "annotationDataS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeNamesInput")
    def attribute_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "attributeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="documentTypeInput")
    def document_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="s3UriInput")
    def s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDocumentsS3UriInput")
    def source_documents_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDocumentsS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="splitInput")
    def split_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "splitInput"))

    @builtins.property
    @jsii.member(jsii_name="annotationDataS3Uri")
    def annotation_data_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "annotationDataS3Uri"))

    @annotation_data_s3_uri.setter
    def annotation_data_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotationDataS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="attributeNames")
    def attribute_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attributeNames"))

    @attribute_names.setter
    def attribute_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeNames", value)

    @builtins.property
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentType"))

    @document_type.setter
    def document_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentType", value)

    @builtins.property
    @jsii.member(jsii_name="s3Uri")
    def s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Uri"))

    @s3_uri.setter
    def s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDocumentsS3Uri")
    def source_documents_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDocumentsS3Uri"))

    @source_documents_s3_uri.setter
    def source_documents_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDocumentsS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="split")
    def split(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "split"))

    @split.setter
    def split(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "split", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComprehendDocumentClassifierInputDataConfigAugmentedManifests, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComprehendDocumentClassifierInputDataConfigAugmentedManifests, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComprehendDocumentClassifierInputDataConfigAugmentedManifests, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[ComprehendDocumentClassifierInputDataConfigAugmentedManifests, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComprehendDocumentClassifierInputDataConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierInputDataConfigOutputReference",
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

    @jsii.member(jsii_name="putAugmentedManifests")
    def put_augmented_manifests(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComprehendDocumentClassifierInputDataConfigAugmentedManifests, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComprehendDocumentClassifierInputDataConfigAugmentedManifests, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAugmentedManifests", [value]))

    @jsii.member(jsii_name="resetAugmentedManifests")
    def reset_augmented_manifests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAugmentedManifests", []))

    @jsii.member(jsii_name="resetDataFormat")
    def reset_data_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFormat", []))

    @jsii.member(jsii_name="resetLabelDelimiter")
    def reset_label_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelDelimiter", []))

    @jsii.member(jsii_name="resetS3Uri")
    def reset_s3_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Uri", []))

    @jsii.member(jsii_name="resetTestS3Uri")
    def reset_test_s3_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestS3Uri", []))

    @builtins.property
    @jsii.member(jsii_name="augmentedManifests")
    def augmented_manifests(
        self,
    ) -> ComprehendDocumentClassifierInputDataConfigAugmentedManifestsList:
        return typing.cast(ComprehendDocumentClassifierInputDataConfigAugmentedManifestsList, jsii.get(self, "augmentedManifests"))

    @builtins.property
    @jsii.member(jsii_name="augmentedManifestsInput")
    def augmented_manifests_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComprehendDocumentClassifierInputDataConfigAugmentedManifests]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComprehendDocumentClassifierInputDataConfigAugmentedManifests]]], jsii.get(self, "augmentedManifestsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFormatInput")
    def data_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="labelDelimiterInput")
    def label_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="s3UriInput")
    def s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="testS3UriInput")
    def test_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "testS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFormat")
    def data_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFormat"))

    @data_format.setter
    def data_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFormat", value)

    @builtins.property
    @jsii.member(jsii_name="labelDelimiter")
    def label_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelDelimiter"))

    @label_delimiter.setter
    def label_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="s3Uri")
    def s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Uri"))

    @s3_uri.setter
    def s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="testS3Uri")
    def test_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testS3Uri"))

    @test_s3_uri.setter
    def test_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComprehendDocumentClassifierInputDataConfig]:
        return typing.cast(typing.Optional[ComprehendDocumentClassifierInputDataConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComprehendDocumentClassifierInputDataConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[ComprehendDocumentClassifierInputDataConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierOutputDataConfig",
    jsii_struct_bases=[],
    name_mapping={"s3_uri": "s3Uri", "kms_key_id": "kmsKeyId"},
)
class ComprehendDocumentClassifierOutputDataConfig:
    def __init__(
        self,
        *,
        s3_uri: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#s3_uri ComprehendDocumentClassifier#s3_uri}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#kms_key_id ComprehendDocumentClassifier#kms_key_id}.
        '''
        if __debug__:
            def stub(
                *,
                s3_uri: builtins.str,
                kms_key_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_uri": s3_uri,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#s3_uri ComprehendDocumentClassifier#s3_uri}.'''
        result = self._values.get("s3_uri")
        assert result is not None, "Required property 's3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#kms_key_id ComprehendDocumentClassifier#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendDocumentClassifierOutputDataConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendDocumentClassifierOutputDataConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierOutputDataConfigOutputReference",
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

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="outputS3Uri")
    def output_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputS3Uri"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3UriInput")
    def s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="s3Uri")
    def s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Uri"))

    @s3_uri.setter
    def s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ComprehendDocumentClassifierOutputDataConfig]:
        return typing.cast(typing.Optional[ComprehendDocumentClassifierOutputDataConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComprehendDocumentClassifierOutputDataConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[ComprehendDocumentClassifierOutputDataConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComprehendDocumentClassifierTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#create ComprehendDocumentClassifier#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#delete ComprehendDocumentClassifier#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#update ComprehendDocumentClassifier#update}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#create ComprehendDocumentClassifier#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#delete ComprehendDocumentClassifier#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#update ComprehendDocumentClassifier#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendDocumentClassifierTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendDocumentClassifierTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierTimeoutsOutputReference",
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

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComprehendDocumentClassifierTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComprehendDocumentClassifierTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComprehendDocumentClassifierTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[ComprehendDocumentClassifierTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierVpcConfig",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
)
class ComprehendDocumentClassifierVpcConfig:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#security_group_ids ComprehendDocumentClassifier#security_group_ids}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#subnets ComprehendDocumentClassifier#subnets}.
        '''
        if __debug__:
            def stub(
                *,
                security_group_ids: typing.Sequence[builtins.str],
                subnets: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
        self._values: typing.Dict[str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnets": subnets,
        }

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#security_group_ids ComprehendDocumentClassifier#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/comprehend_document_classifier#subnets ComprehendDocumentClassifier#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComprehendDocumentClassifierVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComprehendDocumentClassifierVpcConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.comprehendDocumentClassifier.ComprehendDocumentClassifierVpcConfigOutputReference",
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
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComprehendDocumentClassifierVpcConfig]:
        return typing.cast(typing.Optional[ComprehendDocumentClassifierVpcConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComprehendDocumentClassifierVpcConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[ComprehendDocumentClassifierVpcConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComprehendDocumentClassifier",
    "ComprehendDocumentClassifierConfig",
    "ComprehendDocumentClassifierInputDataConfig",
    "ComprehendDocumentClassifierInputDataConfigAugmentedManifests",
    "ComprehendDocumentClassifierInputDataConfigAugmentedManifestsList",
    "ComprehendDocumentClassifierInputDataConfigAugmentedManifestsOutputReference",
    "ComprehendDocumentClassifierInputDataConfigOutputReference",
    "ComprehendDocumentClassifierOutputDataConfig",
    "ComprehendDocumentClassifierOutputDataConfigOutputReference",
    "ComprehendDocumentClassifierTimeouts",
    "ComprehendDocumentClassifierTimeoutsOutputReference",
    "ComprehendDocumentClassifierVpcConfig",
    "ComprehendDocumentClassifierVpcConfigOutputReference",
]

publication.publish()
