'''
# `aws_fsx_file_cache`

Refer to the Terraform Registory for docs: [`aws_fsx_file_cache`](https://www.terraform.io/docs/providers/aws/r/fsx_file_cache).
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


class FsxFileCache(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCache",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache aws_fsx_file_cache}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        file_cache_type: builtins.str,
        file_cache_type_version: builtins.str,
        storage_capacity: jsii.Number,
        subnet_ids: typing.Sequence[builtins.str],
        copy_tags_to_data_repository_associations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data_repository_association: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxFileCacheDataRepositoryAssociation", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lustre_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxFileCacheLustreConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxFileCacheTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache aws_fsx_file_cache} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param file_cache_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#file_cache_type FsxFileCache#file_cache_type}.
        :param file_cache_type_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#file_cache_type_version FsxFileCache#file_cache_type_version}.
        :param storage_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#storage_capacity FsxFileCache#storage_capacity}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#subnet_ids FsxFileCache#subnet_ids}.
        :param copy_tags_to_data_repository_associations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#copy_tags_to_data_repository_associations FsxFileCache#copy_tags_to_data_repository_associations}.
        :param data_repository_association: data_repository_association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#data_repository_association FsxFileCache#data_repository_association}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#id FsxFileCache#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#kms_key_id FsxFileCache#kms_key_id}.
        :param lustre_configuration: lustre_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#lustre_configuration FsxFileCache#lustre_configuration}
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#security_group_ids FsxFileCache#security_group_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#tags FsxFileCache#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#tags_all FsxFileCache#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#timeouts FsxFileCache#timeouts}
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
                file_cache_type: builtins.str,
                file_cache_type_version: builtins.str,
                storage_capacity: jsii.Number,
                subnet_ids: typing.Sequence[builtins.str],
                copy_tags_to_data_repository_associations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                data_repository_association: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheDataRepositoryAssociation, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                lustre_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheLustreConfiguration, typing.Dict[str, typing.Any]]]]] = None,
                security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[FsxFileCacheTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = FsxFileCacheConfig(
            file_cache_type=file_cache_type,
            file_cache_type_version=file_cache_type_version,
            storage_capacity=storage_capacity,
            subnet_ids=subnet_ids,
            copy_tags_to_data_repository_associations=copy_tags_to_data_repository_associations,
            data_repository_association=data_repository_association,
            id=id,
            kms_key_id=kms_key_id,
            lustre_configuration=lustre_configuration,
            security_group_ids=security_group_ids,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDataRepositoryAssociation")
    def put_data_repository_association(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxFileCacheDataRepositoryAssociation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheDataRepositoryAssociation, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDataRepositoryAssociation", [value]))

    @jsii.member(jsii_name="putLustreConfiguration")
    def put_lustre_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxFileCacheLustreConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheLustreConfiguration, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLustreConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#create FsxFileCache#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#delete FsxFileCache#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#update FsxFileCache#update}.
        '''
        value = FsxFileCacheTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCopyTagsToDataRepositoryAssociations")
    def reset_copy_tags_to_data_repository_associations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTagsToDataRepositoryAssociations", []))

    @jsii.member(jsii_name="resetDataRepositoryAssociation")
    def reset_data_repository_association(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataRepositoryAssociation", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetLustreConfiguration")
    def reset_lustre_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLustreConfiguration", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="dataRepositoryAssociation")
    def data_repository_association(
        self,
    ) -> "FsxFileCacheDataRepositoryAssociationList":
        return typing.cast("FsxFileCacheDataRepositoryAssociationList", jsii.get(self, "dataRepositoryAssociation"))

    @builtins.property
    @jsii.member(jsii_name="dataRepositoryAssociationIds")
    def data_repository_association_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dataRepositoryAssociationIds"))

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property
    @jsii.member(jsii_name="fileCacheId")
    def file_cache_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileCacheId"))

    @builtins.property
    @jsii.member(jsii_name="lustreConfiguration")
    def lustre_configuration(self) -> "FsxFileCacheLustreConfigurationList":
        return typing.cast("FsxFileCacheLustreConfigurationList", jsii.get(self, "lustreConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIds")
    def network_interface_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkInterfaceIds"))

    @builtins.property
    @jsii.member(jsii_name="ownerId")
    def owner_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownerId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FsxFileCacheTimeoutsOutputReference":
        return typing.cast("FsxFileCacheTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToDataRepositoryAssociationsInput")
    def copy_tags_to_data_repository_associations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "copyTagsToDataRepositoryAssociationsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataRepositoryAssociationInput")
    def data_repository_association_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheDataRepositoryAssociation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheDataRepositoryAssociation"]]], jsii.get(self, "dataRepositoryAssociationInput"))

    @builtins.property
    @jsii.member(jsii_name="fileCacheTypeInput")
    def file_cache_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileCacheTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="fileCacheTypeVersionInput")
    def file_cache_type_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileCacheTypeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="lustreConfigurationInput")
    def lustre_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheLustreConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheLustreConfiguration"]]], jsii.get(self, "lustreConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCapacityInput")
    def storage_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

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
    ) -> typing.Optional[typing.Union["FsxFileCacheTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FsxFileCacheTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToDataRepositoryAssociations")
    def copy_tags_to_data_repository_associations(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "copyTagsToDataRepositoryAssociations"))

    @copy_tags_to_data_repository_associations.setter
    def copy_tags_to_data_repository_associations(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTagsToDataRepositoryAssociations", value)

    @builtins.property
    @jsii.member(jsii_name="fileCacheType")
    def file_cache_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileCacheType"))

    @file_cache_type.setter
    def file_cache_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileCacheType", value)

    @builtins.property
    @jsii.member(jsii_name="fileCacheTypeVersion")
    def file_cache_type_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileCacheTypeVersion"))

    @file_cache_type_version.setter
    def file_cache_type_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileCacheTypeVersion", value)

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
    @jsii.member(jsii_name="storageCapacity")
    def storage_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageCapacity"))

    @storage_capacity.setter
    def storage_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

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
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "file_cache_type": "fileCacheType",
        "file_cache_type_version": "fileCacheTypeVersion",
        "storage_capacity": "storageCapacity",
        "subnet_ids": "subnetIds",
        "copy_tags_to_data_repository_associations": "copyTagsToDataRepositoryAssociations",
        "data_repository_association": "dataRepositoryAssociation",
        "id": "id",
        "kms_key_id": "kmsKeyId",
        "lustre_configuration": "lustreConfiguration",
        "security_group_ids": "securityGroupIds",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class FsxFileCacheConfig(cdktf.TerraformMetaArguments):
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
        file_cache_type: builtins.str,
        file_cache_type_version: builtins.str,
        storage_capacity: jsii.Number,
        subnet_ids: typing.Sequence[builtins.str],
        copy_tags_to_data_repository_associations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data_repository_association: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxFileCacheDataRepositoryAssociation", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lustre_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxFileCacheLustreConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxFileCacheTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param file_cache_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#file_cache_type FsxFileCache#file_cache_type}.
        :param file_cache_type_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#file_cache_type_version FsxFileCache#file_cache_type_version}.
        :param storage_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#storage_capacity FsxFileCache#storage_capacity}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#subnet_ids FsxFileCache#subnet_ids}.
        :param copy_tags_to_data_repository_associations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#copy_tags_to_data_repository_associations FsxFileCache#copy_tags_to_data_repository_associations}.
        :param data_repository_association: data_repository_association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#data_repository_association FsxFileCache#data_repository_association}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#id FsxFileCache#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#kms_key_id FsxFileCache#kms_key_id}.
        :param lustre_configuration: lustre_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#lustre_configuration FsxFileCache#lustre_configuration}
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#security_group_ids FsxFileCache#security_group_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#tags FsxFileCache#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#tags_all FsxFileCache#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#timeouts FsxFileCache#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = FsxFileCacheTimeouts(**timeouts)
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
                file_cache_type: builtins.str,
                file_cache_type_version: builtins.str,
                storage_capacity: jsii.Number,
                subnet_ids: typing.Sequence[builtins.str],
                copy_tags_to_data_repository_associations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                data_repository_association: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheDataRepositoryAssociation, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                lustre_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheLustreConfiguration, typing.Dict[str, typing.Any]]]]] = None,
                security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[FsxFileCacheTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument file_cache_type", value=file_cache_type, expected_type=type_hints["file_cache_type"])
            check_type(argname="argument file_cache_type_version", value=file_cache_type_version, expected_type=type_hints["file_cache_type_version"])
            check_type(argname="argument storage_capacity", value=storage_capacity, expected_type=type_hints["storage_capacity"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument copy_tags_to_data_repository_associations", value=copy_tags_to_data_repository_associations, expected_type=type_hints["copy_tags_to_data_repository_associations"])
            check_type(argname="argument data_repository_association", value=data_repository_association, expected_type=type_hints["data_repository_association"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument lustre_configuration", value=lustre_configuration, expected_type=type_hints["lustre_configuration"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "file_cache_type": file_cache_type,
            "file_cache_type_version": file_cache_type_version,
            "storage_capacity": storage_capacity,
            "subnet_ids": subnet_ids,
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
        if copy_tags_to_data_repository_associations is not None:
            self._values["copy_tags_to_data_repository_associations"] = copy_tags_to_data_repository_associations
        if data_repository_association is not None:
            self._values["data_repository_association"] = data_repository_association
        if id is not None:
            self._values["id"] = id
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if lustre_configuration is not None:
            self._values["lustre_configuration"] = lustre_configuration
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def file_cache_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#file_cache_type FsxFileCache#file_cache_type}.'''
        result = self._values.get("file_cache_type")
        assert result is not None, "Required property 'file_cache_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_cache_type_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#file_cache_type_version FsxFileCache#file_cache_type_version}.'''
        result = self._values.get("file_cache_type_version")
        assert result is not None, "Required property 'file_cache_type_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#storage_capacity FsxFileCache#storage_capacity}.'''
        result = self._values.get("storage_capacity")
        assert result is not None, "Required property 'storage_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#subnet_ids FsxFileCache#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def copy_tags_to_data_repository_associations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#copy_tags_to_data_repository_associations FsxFileCache#copy_tags_to_data_repository_associations}.'''
        result = self._values.get("copy_tags_to_data_repository_associations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def data_repository_association(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheDataRepositoryAssociation"]]]:
        '''data_repository_association block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#data_repository_association FsxFileCache#data_repository_association}
        '''
        result = self._values.get("data_repository_association")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheDataRepositoryAssociation"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#id FsxFileCache#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#kms_key_id FsxFileCache#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lustre_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheLustreConfiguration"]]]:
        '''lustre_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#lustre_configuration FsxFileCache#lustre_configuration}
        '''
        result = self._values.get("lustre_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheLustreConfiguration"]]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#security_group_ids FsxFileCache#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#tags FsxFileCache#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#tags_all FsxFileCache#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FsxFileCacheTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#timeouts FsxFileCache#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FsxFileCacheTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxFileCacheConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheDataRepositoryAssociation",
    jsii_struct_bases=[],
    name_mapping={
        "data_repository_path": "dataRepositoryPath",
        "file_cache_path": "fileCachePath",
        "data_repository_subdirectories": "dataRepositorySubdirectories",
        "nfs": "nfs",
        "tags": "tags",
    },
)
class FsxFileCacheDataRepositoryAssociation:
    def __init__(
        self,
        *,
        data_repository_path: builtins.str,
        file_cache_path: builtins.str,
        data_repository_subdirectories: typing.Optional[typing.Sequence[builtins.str]] = None,
        nfs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxFileCacheDataRepositoryAssociationNfs", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param data_repository_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#data_repository_path FsxFileCache#data_repository_path}.
        :param file_cache_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#file_cache_path FsxFileCache#file_cache_path}.
        :param data_repository_subdirectories: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#data_repository_subdirectories FsxFileCache#data_repository_subdirectories}.
        :param nfs: nfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#nfs FsxFileCache#nfs}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#tags FsxFileCache#tags}.
        '''
        if __debug__:
            def stub(
                *,
                data_repository_path: builtins.str,
                file_cache_path: builtins.str,
                data_repository_subdirectories: typing.Optional[typing.Sequence[builtins.str]] = None,
                nfs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheDataRepositoryAssociationNfs, typing.Dict[str, typing.Any]]]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument data_repository_path", value=data_repository_path, expected_type=type_hints["data_repository_path"])
            check_type(argname="argument file_cache_path", value=file_cache_path, expected_type=type_hints["file_cache_path"])
            check_type(argname="argument data_repository_subdirectories", value=data_repository_subdirectories, expected_type=type_hints["data_repository_subdirectories"])
            check_type(argname="argument nfs", value=nfs, expected_type=type_hints["nfs"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_repository_path": data_repository_path,
            "file_cache_path": file_cache_path,
        }
        if data_repository_subdirectories is not None:
            self._values["data_repository_subdirectories"] = data_repository_subdirectories
        if nfs is not None:
            self._values["nfs"] = nfs
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_repository_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#data_repository_path FsxFileCache#data_repository_path}.'''
        result = self._values.get("data_repository_path")
        assert result is not None, "Required property 'data_repository_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_cache_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#file_cache_path FsxFileCache#file_cache_path}.'''
        result = self._values.get("file_cache_path")
        assert result is not None, "Required property 'file_cache_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_repository_subdirectories(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#data_repository_subdirectories FsxFileCache#data_repository_subdirectories}.'''
        result = self._values.get("data_repository_subdirectories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def nfs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheDataRepositoryAssociationNfs"]]]:
        '''nfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#nfs FsxFileCache#nfs}
        '''
        result = self._values.get("nfs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheDataRepositoryAssociationNfs"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#tags FsxFileCache#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxFileCacheDataRepositoryAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxFileCacheDataRepositoryAssociationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheDataRepositoryAssociationList",
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
    ) -> "FsxFileCacheDataRepositoryAssociationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxFileCacheDataRepositoryAssociationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociation]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociation]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheDataRepositoryAssociationNfs",
    jsii_struct_bases=[],
    name_mapping={"version": "version", "dns_ips": "dnsIps"},
)
class FsxFileCacheDataRepositoryAssociationNfs:
    def __init__(
        self,
        *,
        version: builtins.str,
        dns_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#version FsxFileCache#version}.
        :param dns_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#dns_ips FsxFileCache#dns_ips}.
        '''
        if __debug__:
            def stub(
                *,
                version: builtins.str,
                dns_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument dns_ips", value=dns_ips, expected_type=type_hints["dns_ips"])
        self._values: typing.Dict[str, typing.Any] = {
            "version": version,
        }
        if dns_ips is not None:
            self._values["dns_ips"] = dns_ips

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#version FsxFileCache#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#dns_ips FsxFileCache#dns_ips}.'''
        result = self._values.get("dns_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxFileCacheDataRepositoryAssociationNfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxFileCacheDataRepositoryAssociationNfsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheDataRepositoryAssociationNfsList",
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
    ) -> "FsxFileCacheDataRepositoryAssociationNfsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxFileCacheDataRepositoryAssociationNfsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociationNfs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociationNfs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociationNfs]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociationNfs]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxFileCacheDataRepositoryAssociationNfsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheDataRepositoryAssociationNfsOutputReference",
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

    @jsii.member(jsii_name="resetDnsIps")
    def reset_dns_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsIps", []))

    @builtins.property
    @jsii.member(jsii_name="dnsIpsInput")
    def dns_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsIps")
    def dns_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsIps"))

    @dns_ips.setter
    def dns_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsIps", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FsxFileCacheDataRepositoryAssociationNfs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxFileCacheDataRepositoryAssociationNfs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxFileCacheDataRepositoryAssociationNfs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[FsxFileCacheDataRepositoryAssociationNfs, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxFileCacheDataRepositoryAssociationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheDataRepositoryAssociationOutputReference",
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

    @jsii.member(jsii_name="putNfs")
    def put_nfs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheDataRepositoryAssociationNfs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheDataRepositoryAssociationNfs, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNfs", [value]))

    @jsii.member(jsii_name="resetDataRepositorySubdirectories")
    def reset_data_repository_subdirectories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataRepositorySubdirectories", []))

    @jsii.member(jsii_name="resetNfs")
    def reset_nfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfs", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="associationId")
    def association_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associationId"))

    @builtins.property
    @jsii.member(jsii_name="fileCacheId")
    def file_cache_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileCacheId"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemPath")
    def file_system_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemPath"))

    @builtins.property
    @jsii.member(jsii_name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "importedFileChunkSize"))

    @builtins.property
    @jsii.member(jsii_name="nfs")
    def nfs(self) -> FsxFileCacheDataRepositoryAssociationNfsList:
        return typing.cast(FsxFileCacheDataRepositoryAssociationNfsList, jsii.get(self, "nfs"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @builtins.property
    @jsii.member(jsii_name="dataRepositoryPathInput")
    def data_repository_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataRepositoryPathInput"))

    @builtins.property
    @jsii.member(jsii_name="dataRepositorySubdirectoriesInput")
    def data_repository_subdirectories_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataRepositorySubdirectoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="fileCachePathInput")
    def file_cache_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileCachePathInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsInput")
    def nfs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociationNfs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheDataRepositoryAssociationNfs]]], jsii.get(self, "nfsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataRepositoryPath")
    def data_repository_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataRepositoryPath"))

    @data_repository_path.setter
    def data_repository_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRepositoryPath", value)

    @builtins.property
    @jsii.member(jsii_name="dataRepositorySubdirectories")
    def data_repository_subdirectories(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dataRepositorySubdirectories"))

    @data_repository_subdirectories.setter
    def data_repository_subdirectories(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRepositorySubdirectories", value)

    @builtins.property
    @jsii.member(jsii_name="fileCachePath")
    def file_cache_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileCachePath"))

    @file_cache_path.setter
    def file_cache_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileCachePath", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FsxFileCacheDataRepositoryAssociation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxFileCacheDataRepositoryAssociation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxFileCacheDataRepositoryAssociation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[FsxFileCacheDataRepositoryAssociation, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheLustreConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_type": "deploymentType",
        "metadata_configuration": "metadataConfiguration",
        "per_unit_storage_throughput": "perUnitStorageThroughput",
        "weekly_maintenance_start_time": "weeklyMaintenanceStartTime",
    },
)
class FsxFileCacheLustreConfiguration:
    def __init__(
        self,
        *,
        deployment_type: builtins.str,
        metadata_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxFileCacheLustreConfigurationMetadataConfiguration", typing.Dict[str, typing.Any]]]],
        per_unit_storage_throughput: jsii.Number,
        weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deployment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#deployment_type FsxFileCache#deployment_type}.
        :param metadata_configuration: metadata_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#metadata_configuration FsxFileCache#metadata_configuration}
        :param per_unit_storage_throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#per_unit_storage_throughput FsxFileCache#per_unit_storage_throughput}.
        :param weekly_maintenance_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#weekly_maintenance_start_time FsxFileCache#weekly_maintenance_start_time}.
        '''
        if __debug__:
            def stub(
                *,
                deployment_type: builtins.str,
                metadata_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheLustreConfigurationMetadataConfiguration, typing.Dict[str, typing.Any]]]],
                per_unit_storage_throughput: jsii.Number,
                weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
            check_type(argname="argument metadata_configuration", value=metadata_configuration, expected_type=type_hints["metadata_configuration"])
            check_type(argname="argument per_unit_storage_throughput", value=per_unit_storage_throughput, expected_type=type_hints["per_unit_storage_throughput"])
            check_type(argname="argument weekly_maintenance_start_time", value=weekly_maintenance_start_time, expected_type=type_hints["weekly_maintenance_start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "deployment_type": deployment_type,
            "metadata_configuration": metadata_configuration,
            "per_unit_storage_throughput": per_unit_storage_throughput,
        }
        if weekly_maintenance_start_time is not None:
            self._values["weekly_maintenance_start_time"] = weekly_maintenance_start_time

    @builtins.property
    def deployment_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#deployment_type FsxFileCache#deployment_type}.'''
        result = self._values.get("deployment_type")
        assert result is not None, "Required property 'deployment_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metadata_configuration(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheLustreConfigurationMetadataConfiguration"]]:
        '''metadata_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#metadata_configuration FsxFileCache#metadata_configuration}
        '''
        result = self._values.get("metadata_configuration")
        assert result is not None, "Required property 'metadata_configuration' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["FsxFileCacheLustreConfigurationMetadataConfiguration"]], result)

    @builtins.property
    def per_unit_storage_throughput(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#per_unit_storage_throughput FsxFileCache#per_unit_storage_throughput}.'''
        result = self._values.get("per_unit_storage_throughput")
        assert result is not None, "Required property 'per_unit_storage_throughput' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def weekly_maintenance_start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#weekly_maintenance_start_time FsxFileCache#weekly_maintenance_start_time}.'''
        result = self._values.get("weekly_maintenance_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxFileCacheLustreConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxFileCacheLustreConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheLustreConfigurationList",
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
    ) -> "FsxFileCacheLustreConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxFileCacheLustreConfigurationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfiguration]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfiguration]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheLustreConfigurationLogConfiguration",
    jsii_struct_bases=[],
    name_mapping={},
)
class FsxFileCacheLustreConfigurationLogConfiguration:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxFileCacheLustreConfigurationLogConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxFileCacheLustreConfigurationLogConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheLustreConfigurationLogConfigurationList",
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
    ) -> "FsxFileCacheLustreConfigurationLogConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxFileCacheLustreConfigurationLogConfigurationOutputReference", jsii.invoke(self, "get", [index]))

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


class FsxFileCacheLustreConfigurationLogConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheLustreConfigurationLogConfigurationOutputReference",
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
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxFileCacheLustreConfigurationLogConfiguration]:
        return typing.cast(typing.Optional[FsxFileCacheLustreConfigurationLogConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxFileCacheLustreConfigurationLogConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[FsxFileCacheLustreConfigurationLogConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheLustreConfigurationMetadataConfiguration",
    jsii_struct_bases=[],
    name_mapping={"storage_capacity": "storageCapacity"},
)
class FsxFileCacheLustreConfigurationMetadataConfiguration:
    def __init__(self, *, storage_capacity: jsii.Number) -> None:
        '''
        :param storage_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#storage_capacity FsxFileCache#storage_capacity}.
        '''
        if __debug__:
            def stub(*, storage_capacity: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument storage_capacity", value=storage_capacity, expected_type=type_hints["storage_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage_capacity": storage_capacity,
        }

    @builtins.property
    def storage_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#storage_capacity FsxFileCache#storage_capacity}.'''
        result = self._values.get("storage_capacity")
        assert result is not None, "Required property 'storage_capacity' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxFileCacheLustreConfigurationMetadataConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxFileCacheLustreConfigurationMetadataConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheLustreConfigurationMetadataConfigurationList",
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
    ) -> "FsxFileCacheLustreConfigurationMetadataConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxFileCacheLustreConfigurationMetadataConfigurationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfigurationMetadataConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfigurationMetadataConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfigurationMetadataConfiguration]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfigurationMetadataConfiguration]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxFileCacheLustreConfigurationMetadataConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheLustreConfigurationMetadataConfigurationOutputReference",
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
    @jsii.member(jsii_name="storageCapacityInput")
    def storage_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCapacity")
    def storage_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageCapacity"))

    @storage_capacity.setter
    def storage_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FsxFileCacheLustreConfigurationMetadataConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxFileCacheLustreConfigurationMetadataConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxFileCacheLustreConfigurationMetadataConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[FsxFileCacheLustreConfigurationMetadataConfiguration, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxFileCacheLustreConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheLustreConfigurationOutputReference",
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

    @jsii.member(jsii_name="putMetadataConfiguration")
    def put_metadata_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheLustreConfigurationMetadataConfiguration, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxFileCacheLustreConfigurationMetadataConfiguration, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetadataConfiguration", [value]))

    @jsii.member(jsii_name="resetWeeklyMaintenanceStartTime")
    def reset_weekly_maintenance_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklyMaintenanceStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="logConfiguration")
    def log_configuration(self) -> FsxFileCacheLustreConfigurationLogConfigurationList:
        return typing.cast(FsxFileCacheLustreConfigurationLogConfigurationList, jsii.get(self, "logConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="metadataConfiguration")
    def metadata_configuration(
        self,
    ) -> FsxFileCacheLustreConfigurationMetadataConfigurationList:
        return typing.cast(FsxFileCacheLustreConfigurationMetadataConfigurationList, jsii.get(self, "metadataConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="mountName")
    def mount_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountName"))

    @builtins.property
    @jsii.member(jsii_name="deploymentTypeInput")
    def deployment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataConfigurationInput")
    def metadata_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfigurationMetadataConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxFileCacheLustreConfigurationMetadataConfiguration]]], jsii.get(self, "metadataConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="perUnitStorageThroughputInput")
    def per_unit_storage_throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "perUnitStorageThroughputInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyMaintenanceStartTimeInput")
    def weekly_maintenance_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weeklyMaintenanceStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentType")
    def deployment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentType"))

    @deployment_type.setter
    def deployment_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentType", value)

    @builtins.property
    @jsii.member(jsii_name="perUnitStorageThroughput")
    def per_unit_storage_throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "perUnitStorageThroughput"))

    @per_unit_storage_throughput.setter
    def per_unit_storage_throughput(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perUnitStorageThroughput", value)

    @builtins.property
    @jsii.member(jsii_name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weeklyMaintenanceStartTime"))

    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeklyMaintenanceStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FsxFileCacheLustreConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxFileCacheLustreConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxFileCacheLustreConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[FsxFileCacheLustreConfiguration, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class FsxFileCacheTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#create FsxFileCache#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#delete FsxFileCache#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#update FsxFileCache#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#create FsxFileCache#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#delete FsxFileCache#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_file_cache#update FsxFileCache#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxFileCacheTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxFileCacheTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxFileCache.FsxFileCacheTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[FsxFileCacheTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxFileCacheTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxFileCacheTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[FsxFileCacheTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FsxFileCache",
    "FsxFileCacheConfig",
    "FsxFileCacheDataRepositoryAssociation",
    "FsxFileCacheDataRepositoryAssociationList",
    "FsxFileCacheDataRepositoryAssociationNfs",
    "FsxFileCacheDataRepositoryAssociationNfsList",
    "FsxFileCacheDataRepositoryAssociationNfsOutputReference",
    "FsxFileCacheDataRepositoryAssociationOutputReference",
    "FsxFileCacheLustreConfiguration",
    "FsxFileCacheLustreConfigurationList",
    "FsxFileCacheLustreConfigurationLogConfiguration",
    "FsxFileCacheLustreConfigurationLogConfigurationList",
    "FsxFileCacheLustreConfigurationLogConfigurationOutputReference",
    "FsxFileCacheLustreConfigurationMetadataConfiguration",
    "FsxFileCacheLustreConfigurationMetadataConfigurationList",
    "FsxFileCacheLustreConfigurationMetadataConfigurationOutputReference",
    "FsxFileCacheLustreConfigurationOutputReference",
    "FsxFileCacheTimeouts",
    "FsxFileCacheTimeoutsOutputReference",
]

publication.publish()
