'''
# `aws_fsx_openzfs_file_system`

Refer to the Terraform Registory for docs: [`aws_fsx_openzfs_file_system`](https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system).
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


class FsxOpenzfsFileSystem(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystem",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system aws_fsx_openzfs_file_system}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        deployment_type: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        throughput_capacity: jsii.Number,
        automatic_backup_retention_days: typing.Optional[jsii.Number] = None,
        backup_id: typing.Optional[builtins.str] = None,
        copy_tags_to_backups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        copy_tags_to_volumes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        daily_automatic_backup_start_time: typing.Optional[builtins.str] = None,
        disk_iops_configuration: typing.Optional[typing.Union["FsxOpenzfsFileSystemDiskIopsConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        root_volume_configuration: typing.Optional[typing.Union["FsxOpenzfsFileSystemRootVolumeConfiguration", typing.Dict[str, typing.Any]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxOpenzfsFileSystemTimeouts", typing.Dict[str, typing.Any]]] = None,
        weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system aws_fsx_openzfs_file_system} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param deployment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#deployment_type FsxOpenzfsFileSystem#deployment_type}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#subnet_ids FsxOpenzfsFileSystem#subnet_ids}.
        :param throughput_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#throughput_capacity FsxOpenzfsFileSystem#throughput_capacity}.
        :param automatic_backup_retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#automatic_backup_retention_days FsxOpenzfsFileSystem#automatic_backup_retention_days}.
        :param backup_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#backup_id FsxOpenzfsFileSystem#backup_id}.
        :param copy_tags_to_backups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#copy_tags_to_backups FsxOpenzfsFileSystem#copy_tags_to_backups}.
        :param copy_tags_to_volumes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#copy_tags_to_volumes FsxOpenzfsFileSystem#copy_tags_to_volumes}.
        :param daily_automatic_backup_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#daily_automatic_backup_start_time FsxOpenzfsFileSystem#daily_automatic_backup_start_time}.
        :param disk_iops_configuration: disk_iops_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#disk_iops_configuration FsxOpenzfsFileSystem#disk_iops_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#id FsxOpenzfsFileSystem#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#kms_key_id FsxOpenzfsFileSystem#kms_key_id}.
        :param root_volume_configuration: root_volume_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#root_volume_configuration FsxOpenzfsFileSystem#root_volume_configuration}
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#security_group_ids FsxOpenzfsFileSystem#security_group_ids}.
        :param storage_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#storage_capacity FsxOpenzfsFileSystem#storage_capacity}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#storage_type FsxOpenzfsFileSystem#storage_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#tags FsxOpenzfsFileSystem#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#tags_all FsxOpenzfsFileSystem#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#timeouts FsxOpenzfsFileSystem#timeouts}
        :param weekly_maintenance_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#weekly_maintenance_start_time FsxOpenzfsFileSystem#weekly_maintenance_start_time}.
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
                deployment_type: builtins.str,
                subnet_ids: typing.Sequence[builtins.str],
                throughput_capacity: jsii.Number,
                automatic_backup_retention_days: typing.Optional[jsii.Number] = None,
                backup_id: typing.Optional[builtins.str] = None,
                copy_tags_to_backups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                copy_tags_to_volumes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                daily_automatic_backup_start_time: typing.Optional[builtins.str] = None,
                disk_iops_configuration: typing.Optional[typing.Union[FsxOpenzfsFileSystemDiskIopsConfiguration, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                root_volume_configuration: typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfiguration, typing.Dict[str, typing.Any]]] = None,
                security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
                storage_capacity: typing.Optional[jsii.Number] = None,
                storage_type: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[FsxOpenzfsFileSystemTimeouts, typing.Dict[str, typing.Any]]] = None,
                weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
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
        config = FsxOpenzfsFileSystemConfig(
            deployment_type=deployment_type,
            subnet_ids=subnet_ids,
            throughput_capacity=throughput_capacity,
            automatic_backup_retention_days=automatic_backup_retention_days,
            backup_id=backup_id,
            copy_tags_to_backups=copy_tags_to_backups,
            copy_tags_to_volumes=copy_tags_to_volumes,
            daily_automatic_backup_start_time=daily_automatic_backup_start_time,
            disk_iops_configuration=disk_iops_configuration,
            id=id,
            kms_key_id=kms_key_id,
            root_volume_configuration=root_volume_configuration,
            security_group_ids=security_group_ids,
            storage_capacity=storage_capacity,
            storage_type=storage_type,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            weekly_maintenance_start_time=weekly_maintenance_start_time,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDiskIopsConfiguration")
    def put_disk_iops_configuration(
        self,
        *,
        iops: typing.Optional[jsii.Number] = None,
        mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#iops FsxOpenzfsFileSystem#iops}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#mode FsxOpenzfsFileSystem#mode}.
        '''
        value = FsxOpenzfsFileSystemDiskIopsConfiguration(iops=iops, mode=mode)

        return typing.cast(None, jsii.invoke(self, "putDiskIopsConfiguration", [value]))

    @jsii.member(jsii_name="putRootVolumeConfiguration")
    def put_root_volume_configuration(
        self,
        *,
        copy_tags_to_snapshots: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data_compression_type: typing.Optional[builtins.str] = None,
        nfs_exports: typing.Optional[typing.Union["FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports", typing.Dict[str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        record_size_kib: typing.Optional[jsii.Number] = None,
        user_and_group_quotas: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param copy_tags_to_snapshots: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#copy_tags_to_snapshots FsxOpenzfsFileSystem#copy_tags_to_snapshots}.
        :param data_compression_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#data_compression_type FsxOpenzfsFileSystem#data_compression_type}.
        :param nfs_exports: nfs_exports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#nfs_exports FsxOpenzfsFileSystem#nfs_exports}
        :param read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#read_only FsxOpenzfsFileSystem#read_only}.
        :param record_size_kib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#record_size_kib FsxOpenzfsFileSystem#record_size_kib}.
        :param user_and_group_quotas: user_and_group_quotas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#user_and_group_quotas FsxOpenzfsFileSystem#user_and_group_quotas}
        '''
        value = FsxOpenzfsFileSystemRootVolumeConfiguration(
            copy_tags_to_snapshots=copy_tags_to_snapshots,
            data_compression_type=data_compression_type,
            nfs_exports=nfs_exports,
            read_only=read_only,
            record_size_kib=record_size_kib,
            user_and_group_quotas=user_and_group_quotas,
        )

        return typing.cast(None, jsii.invoke(self, "putRootVolumeConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#create FsxOpenzfsFileSystem#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#delete FsxOpenzfsFileSystem#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#update FsxOpenzfsFileSystem#update}.
        '''
        value = FsxOpenzfsFileSystemTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutomaticBackupRetentionDays")
    def reset_automatic_backup_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticBackupRetentionDays", []))

    @jsii.member(jsii_name="resetBackupId")
    def reset_backup_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupId", []))

    @jsii.member(jsii_name="resetCopyTagsToBackups")
    def reset_copy_tags_to_backups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTagsToBackups", []))

    @jsii.member(jsii_name="resetCopyTagsToVolumes")
    def reset_copy_tags_to_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTagsToVolumes", []))

    @jsii.member(jsii_name="resetDailyAutomaticBackupStartTime")
    def reset_daily_automatic_backup_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDailyAutomaticBackupStartTime", []))

    @jsii.member(jsii_name="resetDiskIopsConfiguration")
    def reset_disk_iops_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskIopsConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetRootVolumeConfiguration")
    def reset_root_volume_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootVolumeConfiguration", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetStorageCapacity")
    def reset_storage_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageCapacity", []))

    @jsii.member(jsii_name="resetStorageType")
    def reset_storage_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageType", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWeeklyMaintenanceStartTime")
    def reset_weekly_maintenance_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklyMaintenanceStartTime", []))

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
    @jsii.member(jsii_name="diskIopsConfiguration")
    def disk_iops_configuration(
        self,
    ) -> "FsxOpenzfsFileSystemDiskIopsConfigurationOutputReference":
        return typing.cast("FsxOpenzfsFileSystemDiskIopsConfigurationOutputReference", jsii.get(self, "diskIopsConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIds")
    def network_interface_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkInterfaceIds"))

    @builtins.property
    @jsii.member(jsii_name="ownerId")
    def owner_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownerId"))

    @builtins.property
    @jsii.member(jsii_name="rootVolumeConfiguration")
    def root_volume_configuration(
        self,
    ) -> "FsxOpenzfsFileSystemRootVolumeConfigurationOutputReference":
        return typing.cast("FsxOpenzfsFileSystemRootVolumeConfigurationOutputReference", jsii.get(self, "rootVolumeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="rootVolumeId")
    def root_volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootVolumeId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FsxOpenzfsFileSystemTimeoutsOutputReference":
        return typing.cast("FsxOpenzfsFileSystemTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="automaticBackupRetentionDaysInput")
    def automatic_backup_retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "automaticBackupRetentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="backupIdInput")
    def backup_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToBackupsInput")
    def copy_tags_to_backups_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "copyTagsToBackupsInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToVolumesInput")
    def copy_tags_to_volumes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "copyTagsToVolumesInput"))

    @builtins.property
    @jsii.member(jsii_name="dailyAutomaticBackupStartTimeInput")
    def daily_automatic_backup_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dailyAutomaticBackupStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentTypeInput")
    def deployment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="diskIopsConfigurationInput")
    def disk_iops_configuration_input(
        self,
    ) -> typing.Optional["FsxOpenzfsFileSystemDiskIopsConfiguration"]:
        return typing.cast(typing.Optional["FsxOpenzfsFileSystemDiskIopsConfiguration"], jsii.get(self, "diskIopsConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="rootVolumeConfigurationInput")
    def root_volume_configuration_input(
        self,
    ) -> typing.Optional["FsxOpenzfsFileSystemRootVolumeConfiguration"]:
        return typing.cast(typing.Optional["FsxOpenzfsFileSystemRootVolumeConfiguration"], jsii.get(self, "rootVolumeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCapacityInput")
    def storage_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

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
    @jsii.member(jsii_name="throughputCapacityInput")
    def throughput_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["FsxOpenzfsFileSystemTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FsxOpenzfsFileSystemTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyMaintenanceStartTimeInput")
    def weekly_maintenance_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weeklyMaintenanceStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticBackupRetentionDays")
    def automatic_backup_retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "automaticBackupRetentionDays"))

    @automatic_backup_retention_days.setter
    def automatic_backup_retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticBackupRetentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="backupId")
    def backup_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupId"))

    @backup_id.setter
    def backup_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupId", value)

    @builtins.property
    @jsii.member(jsii_name="copyTagsToBackups")
    def copy_tags_to_backups(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "copyTagsToBackups"))

    @copy_tags_to_backups.setter
    def copy_tags_to_backups(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTagsToBackups", value)

    @builtins.property
    @jsii.member(jsii_name="copyTagsToVolumes")
    def copy_tags_to_volumes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "copyTagsToVolumes"))

    @copy_tags_to_volumes.setter
    def copy_tags_to_volumes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTagsToVolumes", value)

    @builtins.property
    @jsii.member(jsii_name="dailyAutomaticBackupStartTime")
    def daily_automatic_backup_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dailyAutomaticBackupStartTime"))

    @daily_automatic_backup_start_time.setter
    def daily_automatic_backup_start_time(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dailyAutomaticBackupStartTime", value)

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
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

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

    @builtins.property
    @jsii.member(jsii_name="throughputCapacity")
    def throughput_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughputCapacity"))

    @throughput_capacity.setter
    def throughput_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughputCapacity", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "deployment_type": "deploymentType",
        "subnet_ids": "subnetIds",
        "throughput_capacity": "throughputCapacity",
        "automatic_backup_retention_days": "automaticBackupRetentionDays",
        "backup_id": "backupId",
        "copy_tags_to_backups": "copyTagsToBackups",
        "copy_tags_to_volumes": "copyTagsToVolumes",
        "daily_automatic_backup_start_time": "dailyAutomaticBackupStartTime",
        "disk_iops_configuration": "diskIopsConfiguration",
        "id": "id",
        "kms_key_id": "kmsKeyId",
        "root_volume_configuration": "rootVolumeConfiguration",
        "security_group_ids": "securityGroupIds",
        "storage_capacity": "storageCapacity",
        "storage_type": "storageType",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "weekly_maintenance_start_time": "weeklyMaintenanceStartTime",
    },
)
class FsxOpenzfsFileSystemConfig(cdktf.TerraformMetaArguments):
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
        deployment_type: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        throughput_capacity: jsii.Number,
        automatic_backup_retention_days: typing.Optional[jsii.Number] = None,
        backup_id: typing.Optional[builtins.str] = None,
        copy_tags_to_backups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        copy_tags_to_volumes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        daily_automatic_backup_start_time: typing.Optional[builtins.str] = None,
        disk_iops_configuration: typing.Optional[typing.Union["FsxOpenzfsFileSystemDiskIopsConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        root_volume_configuration: typing.Optional[typing.Union["FsxOpenzfsFileSystemRootVolumeConfiguration", typing.Dict[str, typing.Any]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FsxOpenzfsFileSystemTimeouts", typing.Dict[str, typing.Any]]] = None,
        weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param deployment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#deployment_type FsxOpenzfsFileSystem#deployment_type}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#subnet_ids FsxOpenzfsFileSystem#subnet_ids}.
        :param throughput_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#throughput_capacity FsxOpenzfsFileSystem#throughput_capacity}.
        :param automatic_backup_retention_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#automatic_backup_retention_days FsxOpenzfsFileSystem#automatic_backup_retention_days}.
        :param backup_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#backup_id FsxOpenzfsFileSystem#backup_id}.
        :param copy_tags_to_backups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#copy_tags_to_backups FsxOpenzfsFileSystem#copy_tags_to_backups}.
        :param copy_tags_to_volumes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#copy_tags_to_volumes FsxOpenzfsFileSystem#copy_tags_to_volumes}.
        :param daily_automatic_backup_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#daily_automatic_backup_start_time FsxOpenzfsFileSystem#daily_automatic_backup_start_time}.
        :param disk_iops_configuration: disk_iops_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#disk_iops_configuration FsxOpenzfsFileSystem#disk_iops_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#id FsxOpenzfsFileSystem#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#kms_key_id FsxOpenzfsFileSystem#kms_key_id}.
        :param root_volume_configuration: root_volume_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#root_volume_configuration FsxOpenzfsFileSystem#root_volume_configuration}
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#security_group_ids FsxOpenzfsFileSystem#security_group_ids}.
        :param storage_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#storage_capacity FsxOpenzfsFileSystem#storage_capacity}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#storage_type FsxOpenzfsFileSystem#storage_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#tags FsxOpenzfsFileSystem#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#tags_all FsxOpenzfsFileSystem#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#timeouts FsxOpenzfsFileSystem#timeouts}
        :param weekly_maintenance_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#weekly_maintenance_start_time FsxOpenzfsFileSystem#weekly_maintenance_start_time}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(disk_iops_configuration, dict):
            disk_iops_configuration = FsxOpenzfsFileSystemDiskIopsConfiguration(**disk_iops_configuration)
        if isinstance(root_volume_configuration, dict):
            root_volume_configuration = FsxOpenzfsFileSystemRootVolumeConfiguration(**root_volume_configuration)
        if isinstance(timeouts, dict):
            timeouts = FsxOpenzfsFileSystemTimeouts(**timeouts)
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
                deployment_type: builtins.str,
                subnet_ids: typing.Sequence[builtins.str],
                throughput_capacity: jsii.Number,
                automatic_backup_retention_days: typing.Optional[jsii.Number] = None,
                backup_id: typing.Optional[builtins.str] = None,
                copy_tags_to_backups: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                copy_tags_to_volumes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                daily_automatic_backup_start_time: typing.Optional[builtins.str] = None,
                disk_iops_configuration: typing.Optional[typing.Union[FsxOpenzfsFileSystemDiskIopsConfiguration, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                root_volume_configuration: typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfiguration, typing.Dict[str, typing.Any]]] = None,
                security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
                storage_capacity: typing.Optional[jsii.Number] = None,
                storage_type: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[FsxOpenzfsFileSystemTimeouts, typing.Dict[str, typing.Any]]] = None,
                weekly_maintenance_start_time: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument throughput_capacity", value=throughput_capacity, expected_type=type_hints["throughput_capacity"])
            check_type(argname="argument automatic_backup_retention_days", value=automatic_backup_retention_days, expected_type=type_hints["automatic_backup_retention_days"])
            check_type(argname="argument backup_id", value=backup_id, expected_type=type_hints["backup_id"])
            check_type(argname="argument copy_tags_to_backups", value=copy_tags_to_backups, expected_type=type_hints["copy_tags_to_backups"])
            check_type(argname="argument copy_tags_to_volumes", value=copy_tags_to_volumes, expected_type=type_hints["copy_tags_to_volumes"])
            check_type(argname="argument daily_automatic_backup_start_time", value=daily_automatic_backup_start_time, expected_type=type_hints["daily_automatic_backup_start_time"])
            check_type(argname="argument disk_iops_configuration", value=disk_iops_configuration, expected_type=type_hints["disk_iops_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument root_volume_configuration", value=root_volume_configuration, expected_type=type_hints["root_volume_configuration"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument storage_capacity", value=storage_capacity, expected_type=type_hints["storage_capacity"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument weekly_maintenance_start_time", value=weekly_maintenance_start_time, expected_type=type_hints["weekly_maintenance_start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "deployment_type": deployment_type,
            "subnet_ids": subnet_ids,
            "throughput_capacity": throughput_capacity,
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
        if automatic_backup_retention_days is not None:
            self._values["automatic_backup_retention_days"] = automatic_backup_retention_days
        if backup_id is not None:
            self._values["backup_id"] = backup_id
        if copy_tags_to_backups is not None:
            self._values["copy_tags_to_backups"] = copy_tags_to_backups
        if copy_tags_to_volumes is not None:
            self._values["copy_tags_to_volumes"] = copy_tags_to_volumes
        if daily_automatic_backup_start_time is not None:
            self._values["daily_automatic_backup_start_time"] = daily_automatic_backup_start_time
        if disk_iops_configuration is not None:
            self._values["disk_iops_configuration"] = disk_iops_configuration
        if id is not None:
            self._values["id"] = id
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if root_volume_configuration is not None:
            self._values["root_volume_configuration"] = root_volume_configuration
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if storage_capacity is not None:
            self._values["storage_capacity"] = storage_capacity
        if storage_type is not None:
            self._values["storage_type"] = storage_type
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if weekly_maintenance_start_time is not None:
            self._values["weekly_maintenance_start_time"] = weekly_maintenance_start_time

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
    def deployment_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#deployment_type FsxOpenzfsFileSystem#deployment_type}.'''
        result = self._values.get("deployment_type")
        assert result is not None, "Required property 'deployment_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#subnet_ids FsxOpenzfsFileSystem#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def throughput_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#throughput_capacity FsxOpenzfsFileSystem#throughput_capacity}.'''
        result = self._values.get("throughput_capacity")
        assert result is not None, "Required property 'throughput_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def automatic_backup_retention_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#automatic_backup_retention_days FsxOpenzfsFileSystem#automatic_backup_retention_days}.'''
        result = self._values.get("automatic_backup_retention_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backup_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#backup_id FsxOpenzfsFileSystem#backup_id}.'''
        result = self._values.get("backup_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def copy_tags_to_backups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#copy_tags_to_backups FsxOpenzfsFileSystem#copy_tags_to_backups}.'''
        result = self._values.get("copy_tags_to_backups")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def copy_tags_to_volumes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#copy_tags_to_volumes FsxOpenzfsFileSystem#copy_tags_to_volumes}.'''
        result = self._values.get("copy_tags_to_volumes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def daily_automatic_backup_start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#daily_automatic_backup_start_time FsxOpenzfsFileSystem#daily_automatic_backup_start_time}.'''
        result = self._values.get("daily_automatic_backup_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_iops_configuration(
        self,
    ) -> typing.Optional["FsxOpenzfsFileSystemDiskIopsConfiguration"]:
        '''disk_iops_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#disk_iops_configuration FsxOpenzfsFileSystem#disk_iops_configuration}
        '''
        result = self._values.get("disk_iops_configuration")
        return typing.cast(typing.Optional["FsxOpenzfsFileSystemDiskIopsConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#id FsxOpenzfsFileSystem#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#kms_key_id FsxOpenzfsFileSystem#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_volume_configuration(
        self,
    ) -> typing.Optional["FsxOpenzfsFileSystemRootVolumeConfiguration"]:
        '''root_volume_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#root_volume_configuration FsxOpenzfsFileSystem#root_volume_configuration}
        '''
        result = self._values.get("root_volume_configuration")
        return typing.cast(typing.Optional["FsxOpenzfsFileSystemRootVolumeConfiguration"], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#security_group_ids FsxOpenzfsFileSystem#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def storage_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#storage_capacity FsxOpenzfsFileSystem#storage_capacity}.'''
        result = self._values.get("storage_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#storage_type FsxOpenzfsFileSystem#storage_type}.'''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#tags FsxOpenzfsFileSystem#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#tags_all FsxOpenzfsFileSystem#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FsxOpenzfsFileSystemTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#timeouts FsxOpenzfsFileSystem#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FsxOpenzfsFileSystemTimeouts"], result)

    @builtins.property
    def weekly_maintenance_start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#weekly_maintenance_start_time FsxOpenzfsFileSystem#weekly_maintenance_start_time}.'''
        result = self._values.get("weekly_maintenance_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsFileSystemConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemDiskIopsConfiguration",
    jsii_struct_bases=[],
    name_mapping={"iops": "iops", "mode": "mode"},
)
class FsxOpenzfsFileSystemDiskIopsConfiguration:
    def __init__(
        self,
        *,
        iops: typing.Optional[jsii.Number] = None,
        mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#iops FsxOpenzfsFileSystem#iops}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#mode FsxOpenzfsFileSystem#mode}.
        '''
        if __debug__:
            def stub(
                *,
                iops: typing.Optional[jsii.Number] = None,
                mode: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[str, typing.Any] = {}
        if iops is not None:
            self._values["iops"] = iops
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#iops FsxOpenzfsFileSystem#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#mode FsxOpenzfsFileSystem#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsFileSystemDiskIopsConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOpenzfsFileSystemDiskIopsConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemDiskIopsConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxOpenzfsFileSystemDiskIopsConfiguration]:
        return typing.cast(typing.Optional[FsxOpenzfsFileSystemDiskIopsConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOpenzfsFileSystemDiskIopsConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[FsxOpenzfsFileSystemDiskIopsConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "copy_tags_to_snapshots": "copyTagsToSnapshots",
        "data_compression_type": "dataCompressionType",
        "nfs_exports": "nfsExports",
        "read_only": "readOnly",
        "record_size_kib": "recordSizeKib",
        "user_and_group_quotas": "userAndGroupQuotas",
    },
)
class FsxOpenzfsFileSystemRootVolumeConfiguration:
    def __init__(
        self,
        *,
        copy_tags_to_snapshots: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data_compression_type: typing.Optional[builtins.str] = None,
        nfs_exports: typing.Optional[typing.Union["FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports", typing.Dict[str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        record_size_kib: typing.Optional[jsii.Number] = None,
        user_and_group_quotas: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param copy_tags_to_snapshots: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#copy_tags_to_snapshots FsxOpenzfsFileSystem#copy_tags_to_snapshots}.
        :param data_compression_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#data_compression_type FsxOpenzfsFileSystem#data_compression_type}.
        :param nfs_exports: nfs_exports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#nfs_exports FsxOpenzfsFileSystem#nfs_exports}
        :param read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#read_only FsxOpenzfsFileSystem#read_only}.
        :param record_size_kib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#record_size_kib FsxOpenzfsFileSystem#record_size_kib}.
        :param user_and_group_quotas: user_and_group_quotas block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#user_and_group_quotas FsxOpenzfsFileSystem#user_and_group_quotas}
        '''
        if isinstance(nfs_exports, dict):
            nfs_exports = FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports(**nfs_exports)
        if __debug__:
            def stub(
                *,
                copy_tags_to_snapshots: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                data_compression_type: typing.Optional[builtins.str] = None,
                nfs_exports: typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports, typing.Dict[str, typing.Any]]] = None,
                read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                record_size_kib: typing.Optional[jsii.Number] = None,
                user_and_group_quotas: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument copy_tags_to_snapshots", value=copy_tags_to_snapshots, expected_type=type_hints["copy_tags_to_snapshots"])
            check_type(argname="argument data_compression_type", value=data_compression_type, expected_type=type_hints["data_compression_type"])
            check_type(argname="argument nfs_exports", value=nfs_exports, expected_type=type_hints["nfs_exports"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument record_size_kib", value=record_size_kib, expected_type=type_hints["record_size_kib"])
            check_type(argname="argument user_and_group_quotas", value=user_and_group_quotas, expected_type=type_hints["user_and_group_quotas"])
        self._values: typing.Dict[str, typing.Any] = {}
        if copy_tags_to_snapshots is not None:
            self._values["copy_tags_to_snapshots"] = copy_tags_to_snapshots
        if data_compression_type is not None:
            self._values["data_compression_type"] = data_compression_type
        if nfs_exports is not None:
            self._values["nfs_exports"] = nfs_exports
        if read_only is not None:
            self._values["read_only"] = read_only
        if record_size_kib is not None:
            self._values["record_size_kib"] = record_size_kib
        if user_and_group_quotas is not None:
            self._values["user_and_group_quotas"] = user_and_group_quotas

    @builtins.property
    def copy_tags_to_snapshots(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#copy_tags_to_snapshots FsxOpenzfsFileSystem#copy_tags_to_snapshots}.'''
        result = self._values.get("copy_tags_to_snapshots")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def data_compression_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#data_compression_type FsxOpenzfsFileSystem#data_compression_type}.'''
        result = self._values.get("data_compression_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nfs_exports(
        self,
    ) -> typing.Optional["FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports"]:
        '''nfs_exports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#nfs_exports FsxOpenzfsFileSystem#nfs_exports}
        '''
        result = self._values.get("nfs_exports")
        return typing.cast(typing.Optional["FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#read_only FsxOpenzfsFileSystem#read_only}.'''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def record_size_kib(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#record_size_kib FsxOpenzfsFileSystem#record_size_kib}.'''
        result = self._values.get("record_size_kib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_and_group_quotas(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas"]]]:
        '''user_and_group_quotas block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#user_and_group_quotas FsxOpenzfsFileSystem#user_and_group_quotas}
        '''
        result = self._values.get("user_and_group_quotas")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsFileSystemRootVolumeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports",
    jsii_struct_bases=[],
    name_mapping={"client_configurations": "clientConfigurations"},
)
class FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports:
    def __init__(
        self,
        *,
        client_configurations: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param client_configurations: client_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#client_configurations FsxOpenzfsFileSystem#client_configurations}
        '''
        if __debug__:
            def stub(
                *,
                client_configurations: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_configurations", value=client_configurations, expected_type=type_hints["client_configurations"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_configurations": client_configurations,
        }

    @builtins.property
    def client_configurations(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations"]]:
        '''client_configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#client_configurations FsxOpenzfsFileSystem#client_configurations}
        '''
        result = self._values.get("client_configurations")
        assert result is not None, "Required property 'client_configurations' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations",
    jsii_struct_bases=[],
    name_mapping={"clients": "clients", "options": "options"},
)
class FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations:
    def __init__(
        self,
        *,
        clients: builtins.str,
        options: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param clients: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#clients FsxOpenzfsFileSystem#clients}.
        :param options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#options FsxOpenzfsFileSystem#options}.
        '''
        if __debug__:
            def stub(
                *,
                clients: builtins.str,
                options: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument clients", value=clients, expected_type=type_hints["clients"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        self._values: typing.Dict[str, typing.Any] = {
            "clients": clients,
            "options": options,
        }

    @builtins.property
    def clients(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#clients FsxOpenzfsFileSystem#clients}.'''
        result = self._values.get("clients")
        assert result is not None, "Required property 'clients' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def options(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#options FsxOpenzfsFileSystem#options}.'''
        result = self._values.get("options")
        assert result is not None, "Required property 'options' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsList",
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
    ) -> "FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsOutputReference",
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
    @jsii.member(jsii_name="clientsInput")
    def clients_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientsInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clients")
    def clients(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clients"))

    @clients.setter
    def clients(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clients", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsOutputReference",
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

    @jsii.member(jsii_name="putClientConfigurations")
    def put_client_configurations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClientConfigurations", [value]))

    @builtins.property
    @jsii.member(jsii_name="clientConfigurations")
    def client_configurations(
        self,
    ) -> FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsList:
        return typing.cast(FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsList, jsii.get(self, "clientConfigurations"))

    @builtins.property
    @jsii.member(jsii_name="clientConfigurationsInput")
    def client_configurations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations]]], jsii.get(self, "clientConfigurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports]:
        return typing.cast(typing.Optional[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxOpenzfsFileSystemRootVolumeConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfigurationOutputReference",
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

    @jsii.member(jsii_name="putNfsExports")
    def put_nfs_exports(
        self,
        *,
        client_configurations: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param client_configurations: client_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#client_configurations FsxOpenzfsFileSystem#client_configurations}
        '''
        value = FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports(
            client_configurations=client_configurations
        )

        return typing.cast(None, jsii.invoke(self, "putNfsExports", [value]))

    @jsii.member(jsii_name="putUserAndGroupQuotas")
    def put_user_and_group_quotas(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUserAndGroupQuotas", [value]))

    @jsii.member(jsii_name="resetCopyTagsToSnapshots")
    def reset_copy_tags_to_snapshots(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTagsToSnapshots", []))

    @jsii.member(jsii_name="resetDataCompressionType")
    def reset_data_compression_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataCompressionType", []))

    @jsii.member(jsii_name="resetNfsExports")
    def reset_nfs_exports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfsExports", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetRecordSizeKib")
    def reset_record_size_kib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordSizeKib", []))

    @jsii.member(jsii_name="resetUserAndGroupQuotas")
    def reset_user_and_group_quotas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAndGroupQuotas", []))

    @builtins.property
    @jsii.member(jsii_name="nfsExports")
    def nfs_exports(
        self,
    ) -> FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsOutputReference:
        return typing.cast(FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsOutputReference, jsii.get(self, "nfsExports"))

    @builtins.property
    @jsii.member(jsii_name="userAndGroupQuotas")
    def user_and_group_quotas(
        self,
    ) -> "FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasList":
        return typing.cast("FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasList", jsii.get(self, "userAndGroupQuotas"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToSnapshotsInput")
    def copy_tags_to_snapshots_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "copyTagsToSnapshotsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataCompressionTypeInput")
    def data_compression_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataCompressionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsExportsInput")
    def nfs_exports_input(
        self,
    ) -> typing.Optional[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports]:
        return typing.cast(typing.Optional[FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports], jsii.get(self, "nfsExportsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="recordSizeKibInput")
    def record_size_kib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "recordSizeKibInput"))

    @builtins.property
    @jsii.member(jsii_name="userAndGroupQuotasInput")
    def user_and_group_quotas_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas"]]], jsii.get(self, "userAndGroupQuotasInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToSnapshots")
    def copy_tags_to_snapshots(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "copyTagsToSnapshots"))

    @copy_tags_to_snapshots.setter
    def copy_tags_to_snapshots(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTagsToSnapshots", value)

    @builtins.property
    @jsii.member(jsii_name="dataCompressionType")
    def data_compression_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataCompressionType"))

    @data_compression_type.setter
    def data_compression_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataCompressionType", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="recordSizeKib")
    def record_size_kib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "recordSizeKib"))

    @record_size_kib.setter
    def record_size_kib(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordSizeKib", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FsxOpenzfsFileSystemRootVolumeConfiguration]:
        return typing.cast(typing.Optional[FsxOpenzfsFileSystemRootVolumeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FsxOpenzfsFileSystemRootVolumeConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[FsxOpenzfsFileSystemRootVolumeConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "storage_capacity_quota_gib": "storageCapacityQuotaGib",
        "type": "type",
    },
)
class FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas:
    def __init__(
        self,
        *,
        id: jsii.Number,
        storage_capacity_quota_gib: jsii.Number,
        type: builtins.str,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#id FsxOpenzfsFileSystem#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param storage_capacity_quota_gib: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#storage_capacity_quota_gib FsxOpenzfsFileSystem#storage_capacity_quota_gib}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#type FsxOpenzfsFileSystem#type}.
        '''
        if __debug__:
            def stub(
                *,
                id: jsii.Number,
                storage_capacity_quota_gib: jsii.Number,
                type: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument storage_capacity_quota_gib", value=storage_capacity_quota_gib, expected_type=type_hints["storage_capacity_quota_gib"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "storage_capacity_quota_gib": storage_capacity_quota_gib,
            "type": type,
        }

    @builtins.property
    def id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#id FsxOpenzfsFileSystem#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_capacity_quota_gib(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#storage_capacity_quota_gib FsxOpenzfsFileSystem#storage_capacity_quota_gib}.'''
        result = self._values.get("storage_capacity_quota_gib")
        assert result is not None, "Required property 'storage_capacity_quota_gib' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#type FsxOpenzfsFileSystem#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasList",
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
    ) -> "FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasOutputReference",
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
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCapacityQuotaGibInput")
    def storage_capacity_quota_gib_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacityQuotaGibInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageCapacityQuotaGib"))

    @storage_capacity_quota_gib.setter
    def storage_capacity_quota_gib(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacityQuotaGib", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class FsxOpenzfsFileSystemTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#create FsxOpenzfsFileSystem#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#delete FsxOpenzfsFileSystem#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#update FsxOpenzfsFileSystem#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#create FsxOpenzfsFileSystem#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#delete FsxOpenzfsFileSystem#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/fsx_openzfs_file_system#update FsxOpenzfsFileSystem#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FsxOpenzfsFileSystemTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FsxOpenzfsFileSystemTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.fsxOpenzfsFileSystem.FsxOpenzfsFileSystemTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[FsxOpenzfsFileSystemTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FsxOpenzfsFileSystemTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FsxOpenzfsFileSystemTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[FsxOpenzfsFileSystemTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FsxOpenzfsFileSystem",
    "FsxOpenzfsFileSystemConfig",
    "FsxOpenzfsFileSystemDiskIopsConfiguration",
    "FsxOpenzfsFileSystemDiskIopsConfigurationOutputReference",
    "FsxOpenzfsFileSystemRootVolumeConfiguration",
    "FsxOpenzfsFileSystemRootVolumeConfigurationNfsExports",
    "FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurations",
    "FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsList",
    "FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationsOutputReference",
    "FsxOpenzfsFileSystemRootVolumeConfigurationNfsExportsOutputReference",
    "FsxOpenzfsFileSystemRootVolumeConfigurationOutputReference",
    "FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotas",
    "FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasList",
    "FsxOpenzfsFileSystemRootVolumeConfigurationUserAndGroupQuotasOutputReference",
    "FsxOpenzfsFileSystemTimeouts",
    "FsxOpenzfsFileSystemTimeoutsOutputReference",
]

publication.publish()
